#!/usr/bin/env python3
"""
ebc_bao_fit2.py — EBC: BAO-Fit mit zwei freien Parametern (H₀, Ω_m)
=====================================================================
Autor : Wolfgang Mattis <ebc@wm0.eu>
Stand : 2026-04-24

Methode:
  Strategie „profil-chi2 über Ω_m":
    Für jedes Ω_m im Raster → analytische H₀-Minimierung
    (alle BAO-Observablen ∝ 1/H₀ für festes Ω_m und festes r_d).
  Zusätzlich: 2D-chi2-Raster in (Ω_m, H₀) für Konturplot.

Einschränkung (Methodische Prüfung — EBC-Abschnitt 4):
  r_d = 147.09 Mpc festgehalten (Planck 2018, Ω_b = 0.0493).
  Bei freiem Ω_m wäre r_d(Ω_m, h²) mitzufitten (3-Parameter-Problem).
  Die hier ermittelten Werte sind daher obere Schranken auf die
  Modellspannung. Nächster Entwicklungsschritt: r_d(Ω_m, H₀)
  über Aubourg-Formel (arXiv:1411.1074) selbstkonsistent einbeziehen.

DESI-Daten: arXiv:2404.03002, Tabelle 1 (12 Messpunkte, 7 Bins)
"""

import numpy as np
from scipy import integrate, optimize
import warnings

# ============================================================
# Konstanten
# ============================================================
C_KMS     = 299792.458    # Lichtgeschwindigkeit [km/s]
H0_PLANCK = 67.4          # Planck 2018 [km/s/Mpc]
OM_PLANCK = 0.315         # Planck 2018
OM_DESI   = 0.295         # DESI-bevorzugt (arXiv:2404.03002)
RD_MPC    = 147.09        # Schallhorizont [Mpc], Planck 2018 — festgehalten
OMEGA_R   = 9.2e-5        # Strahlungsdichte (festgehalten)
KM_TO_GYR = 978.5         # 1/(H0[km/s/Mpc]) -> Gyr

# ============================================================
# DESI DR1 Tabelle 1  (arXiv:2404.03002)
# ============================================================
# Anisotropisch: (z, DM/rd, sDM, DH/rd, sDH, r, Label)
DESI_FULL = [
    (0.510, 13.62, 0.25, 20.98, 0.61, -0.445, "LRG1"),
    (0.706, 16.85, 0.32, 20.08, 0.60, -0.420, "LRG2"),
    (0.930, 21.71, 0.28, 17.88, 0.35, -0.389, "LRG3+ELG1"),
    (1.317, 27.79, 0.69, 13.82, 0.42, -0.444, "ELG2"),
    (2.330, 39.71, 0.94,  8.52, 0.17, -0.477, "Lya"),
]
# Isotropisch: (z, DV/rd, sDV, Label)
DESI_DV = [
    (0.295,  7.93, 0.15, "BGS"),
    (1.491, 26.07, 0.67, "QSO"),
]

# ============================================================
# EBC- und ΛCDM-Hubblefunktionen
# ============================================================

def omega_de_ebc(omega_m, x_star):
    """Ω_DE aus EBC-Flachheitsbedingung (Abschnitt 3, EBC1 bei x=1)."""
    return (1.0 - omega_m - OMEGA_R) / (1.0 - 1.0/x_star**2)

def E_ebc(z, omega_m, x_star):
    """E(z) = H(z)/H₀ für EBC. Ω_DE aus Flachheitsbedingung."""
    x   = 1.0 / (1.0 + z)
    ode = omega_de_ebc(omega_m, x_star)
    val = omega_m/x**3 + OMEGA_R/x**4 + ode*(1.0/x - x/x_star**2)
    return np.sqrt(max(val, 0.0))

def E_lcdm(z, omega_m):
    """E(z) = H(z)/H₀ für ΛCDM. Ω_Λ aus Flachheitsbedingung."""
    omega_l = 1.0 - omega_m - OMEGA_R
    return np.sqrt(omega_m*(1+z)**3 + OMEGA_R*(1+z)**4 + omega_l)

# ============================================================
# BAO-Observablen (Vorhersagen bei H₀ = 1 km/s/Mpc)
# A_DH * (1/H0) = DH/rd   usw.
# ============================================================

def A_DH(z, E_fn, *args):
    return C_KMS / (E_fn(z, *args) * RD_MPC)

def A_DM(z, E_fn, *args, n=600):
    zz = np.linspace(0.0, z, n)
    Ez = np.array([E_fn(zi, *args) for zi in zz])
    return np.trapezoid(C_KMS / Ez, zz) / RD_MPC

def A_DV(z, E_fn, *args):
    aDM = A_DM(z, E_fn, *args) * RD_MPC
    aDH = A_DH(z, E_fn, *args) * RD_MPC
    return (z * aDM**2 * aDH)**(1.0/3.0) / RD_MPC

# ============================================================
# Analytischer H₀-Fit für festes Ω_m
# chi2(u) = u²·S_AA − 2u·S_OA + S_OO  (u = 1/H₀)
# Minimum: u_opt = S_OA / S_AA
# ============================================================

def fit_H0_given_om(omega_m, x_star=None, is_lcdm=False):
    """
    Analytische H₀-Minimierung bei festem Ω_m und festem r_d.
    Gibt dict zurück: H0, sH0, chi2, chi2_red.
    """
    if is_lcdm:
        E_fn  = E_lcdm
        args  = (omega_m,)
    else:
        E_fn  = E_ebc
        args  = (omega_m, x_star)

    S_AA = 0.0; S_OA = 0.0

    # Anisotropische Bins (DM/rd, DH/rd mit Kovarianz)
    for (z, DM, sDM, DH, sDH, r, _) in DESI_FULL:
        aDM = A_DM(z, E_fn, *args)
        aDH = A_DH(z, E_fn, *args)
        A   = np.array([aDM, aDH])
        O   = np.array([DM,  DH])
        C   = np.array([[sDM**2, r*sDM*sDH],
                        [r*sDM*sDH, sDH**2]])
        Ci  = np.linalg.inv(C)
        S_AA += A @ Ci @ A
        S_OA += O @ Ci @ A

    # Isotropische Bins (DV/rd)
    for (z, DV, sDV, _) in DESI_DV:
        aDV = A_DV(z, E_fn, *args)
        S_AA += aDV**2 / sDV**2
        S_OA += DV * aDV / sDV**2

    u_opt  = S_OA / S_AA
    H0_opt = 1.0 / u_opt
    sH0    = H0_opt**2 / np.sqrt(S_AA)

    # chi2 im Minimum
    chi2 = 0.0
    for (z, DM, sDM, DH, sDH, r, _) in DESI_FULL:
        aDM = A_DM(z, E_fn, *args)
        aDH = A_DH(z, E_fn, *args)
        res = np.array([u_opt*aDM - DM, u_opt*aDH - DH])
        C   = np.array([[sDM**2, r*sDM*sDH],
                        [r*sDM*sDH, sDH**2]])
        chi2 += res @ np.linalg.inv(C) @ res
    for (z, DV, sDV, _) in DESI_DV:
        aDV = A_DV(z, E_fn, *args)
        chi2 += ((u_opt*aDV - DV)/sDV)**2

    # dof = 12 Datenpunkte − 2 freie Parameter
    return dict(H0=H0_opt, sH0=sH0, chi2=chi2, chi2_red=chi2/10,
                omega_m=omega_m)

# ============================================================
# Direktes chi2(H0, Ω_m) für 2D-Raster
# ============================================================

def chi2_2d(H0, omega_m, x_star=None, is_lcdm=False):
    """chi2 direkt für gegebenes (H0, Ω_m)."""
    u = 1.0/H0
    if is_lcdm:
        E_fn = E_lcdm; args = (omega_m,)
    else:
        E_fn = E_ebc;  args = (omega_m, x_star)

    chi2 = 0.0
    for (z, DM, sDM, DH, sDH, r, _) in DESI_FULL:
        aDM = A_DM(z, E_fn, *args)
        aDH = A_DH(z, E_fn, *args)
        res = np.array([u*aDM - DM, u*aDH - DH])
        C   = np.array([[sDM**2, r*sDM*sDH],
                        [r*sDM*sDH, sDH**2]])
        chi2 += res @ np.linalg.inv(C) @ res
    for (z, DV, sDV, _) in DESI_DV:
        aDV = A_DV(z, E_fn, *args)
        chi2 += ((u*aDV - DV)/sDV)**2
    return chi2

# ============================================================
# Weltalter (EBC1-Integral, wie in ebc_physical.py)
# ============================================================

def compute_t0(H0, omega_m, x_star=None, is_lcdm=False):
    if is_lcdm:
        fn = lambda z: 1.0/((1+z)*E_lcdm(z, omega_m))
    else:
        fn = lambda z: 1.0/((1+z)*E_ebc(z, omega_m, x_star))
    H0t0, _ = integrate.quad(fn, 0.0, 1e4, limit=200, epsrel=1e-9)
    return H0t0, H0t0 * KM_TO_GYR / H0

# ============================================================
# Residuen-Ausgabe
# ============================================================

def print_residuals(H0, omega_m, x_star, label="EBC"):
    u    = 1.0/H0
    args = (omega_m, x_star)
    print(f"\n   Residuen {label} (Ω_m={omega_m:.3f}, H₀={H0:.2f}):")
    print(f"   {'Tracer':<14} {'z':>5}  {'DM/σ':>6}  {'DH/σ':>6}")
    for (z, DM, sDM, DH, sDH, r, lab) in DESI_FULL:
        pDM = (u*A_DM(z, E_ebc, *args) - DM)/sDM
        pDH = (u*A_DH(z, E_ebc, *args) - DH)/sDH
        print(f"   {lab:<14} {z:>5.3f}  {pDM:>+6.2f}σ  {pDH:>+6.2f}σ")
    for (z, DV, sDV, lab) in DESI_DV:
        pDV = (u*A_DV(z, E_ebc, *args) - DV)/sDV
        print(f"   {lab:<14} {z:>5.3f}  {'DV:':>6}  {pDV:>+6.2f}σ")

# ============================================================
# Hauptprogramm
# ============================================================

def main():
    sep = "=" * 72
    X0s    = [0.06, 0.10, 0.15]
    XSTARs = [1.0/x for x in X0s]
    OM_GRID = np.linspace(0.23, 0.43, 80)

    print(sep)
    print("EBC — BAO-Fit mit zwei freien Parametern (H₀, Ω_m)")
    print(f"DESI DR1 | arXiv:2404.03002 | r_d = {RD_MPC} Mpc (festgehalten)")
    print(f"WARNUNG: r_d bei variablem Ω_m ideell mitzufitten — Ergebnisse")
    print(f"         als obere Schranke auf Modellspannung interpretieren.")
    print(sep)

    # ── Schritt 1: Profil-chi2 über Ω_m ──────────────────────────────────
    print("\n── Schritt 1: Profil-χ²(Ω_m) — analytische H₀-Minimierung ────────")

    all_profiles = {}  # key: (label, xs oder "lcdm") -> arrays

    # EBC
    for x0, xs in zip(X0s, XSTARs):
        res = []
        for om in OM_GRID:
            try:
                f = fit_H0_given_om(om, x_star=xs)
                res.append((om, f["H0"], f["chi2"], f["chi2_red"]))
            except Exception:
                res.append((om, np.nan, np.nan, np.nan))
        res     = np.array(res)
        all_profiles[f"EBC x0={x0}"] = res
        # Minimum
        idx = np.nanargmin(res[:,2])
        print(f"   EBC x0={x0}: Ω_m_opt={res[idx,0]:.3f}  "
              f"H₀_opt={res[idx,1]:.2f}  χ²={res[idx,2]:.2f}  "
              f"χ²/dof={res[idx,3]:.3f}")

    # ΛCDM
    res_l = []
    for om in OM_GRID:
        try:
            f = fit_H0_given_om(om, is_lcdm=True)
            res_l.append((om, f["H0"], f["chi2"], f["chi2_red"]))
        except Exception:
            res_l.append((om, np.nan, np.nan, np.nan))
    res_l = np.array(res_l)
    all_profiles["LCDM"] = res_l
    idx_l = np.nanargmin(res_l[:,2])
    print(f"   ΛCDM:       Ω_m_opt={res_l[idx_l,0]:.3f}  "
          f"H₀_opt={res_l[idx_l,1]:.2f}  χ²={res_l[idx_l,2]:.2f}  "
          f"χ²/dof={res_l[idx_l,3]:.3f}")

    # ── Schritt 2: Detaillierte Ergebnisse am Minimum ─────────────────────
    print("\n── Schritt 2: Detaillierte Ergebnisse am globalen Minimum ─────────")
    print(f"\n   {'Modell':<18} {'Ω_m':>6} {'H₀':>7} {'χ²':>7} "
          f"{'χ²/dof':>7} {'H₀t₀':>7} {'t₀[Gyr]':>9}")
    print(f"   {'-'*68}")

    best_fits = {}
    for label, prof in all_profiles.items():
        idx = np.nanargmin(prof[:,2])
        om_opt, H0_opt = prof[idx,0], prof[idx,1]
        chi2, chi2r    = prof[idx,2], prof[idx,3]

        if label == "LCDM":
            H0t0, t0 = compute_t0(H0_opt, om_opt, is_lcdm=True)
        else:
            xs = XSTARs[X0s.index(float(label.split("=")[1]))]
            H0t0, t0 = compute_t0(H0_opt, om_opt, x_star=xs)

        best_fits[label] = dict(om=om_opt, H0=H0_opt, chi2=chi2,
                                chi2r=chi2r, H0t0=H0t0, t0=t0)
        print(f"   {label:<18} {om_opt:>6.3f} {H0_opt:>7.2f} {chi2:>7.3f} "
              f"{chi2r:>7.3f} {H0t0:>7.4f} {t0:>9.2f}")

    # ── Schritt 3: Delta-chi2-Konfidenzintervalle (Ω_m-Profil) ───────────
    print("\n── Schritt 3: Δχ²-Konfidenzintervalle (1σ, 2σ) ────────────────────")
    print(f"   [Δχ²=1.00 → 1σ-Rand im Profil; 2D-Konfidenz: Δχ²=2.30/6.17]\n")
    for label, prof in all_profiles.items():
        idx    = np.nanargmin(prof[:,2])
        chi2_0 = prof[idx,2]
        om_opt = prof[idx,0]
        # Einfacher 1σ-Bereich aus Profil (Δchi2 = 1)
        mask1s = prof[:,2] < chi2_0 + 1.0
        if np.any(mask1s):
            om_lo = prof[mask1s,0].min()
            om_hi = prof[mask1s,0].max()
            print(f"   {label:<18}: Ω_m = {om_opt:.3f}  "
                  f"[{om_lo:.3f}, {om_hi:.3f}]  (Δχ²<1, Profil)")
        else:
            print(f"   {label:<18}: Profil-Intervall nicht bestimmbar")

    # ── Schritt 4: Vergleich 1-Parameter vs. 2-Parameter ─────────────────
    print("\n── Schritt 4: Verbesserung durch zweiten Parameter ─────────────────")

    # 1-Parameter-Ergebnisse (Ω_m=0.315 fest, wie in ebc_bao_fit.py)
    chi2_1p = {}
    for x0, xs in zip(X0s, XSTARs):
        f = fit_H0_given_om(OM_PLANCK, x_star=xs)
        chi2_1p[f"EBC x0={x0}"] = f["chi2"]
    f_l = fit_H0_given_om(OM_PLANCK, is_lcdm=True)
    chi2_1p["LCDM"] = f_l["chi2"]

    print(f"\n   {'Modell':<18} {'χ²(1-Par)':>10} {'χ²(2-Par)':>10} {'Δχ²':>7}")
    print(f"   {'-'*50}")
    for label in best_fits:
        c1 = chi2_1p[label]
        c2 = best_fits[label]["chi2"]
        print(f"   {label:<18} {c1:>10.3f} {c2:>10.3f} {c2-c1:>+7.3f}")

    print("\n   (Δχ² < 0: 2-Parameter-Fit besser)")
    print("   AIC-Korrektur: Δχ²_AIC = Δχ² + 2 × ΔPar = Δχ² + 2")
    print("   Verbesserung signifikant wenn Δχ² < −2 (AIC-Kriterium)")

    # ── Schritt 5: Residuen am besten EBC-Minimum ─────────────────────────
    best_ebc_label = min(
        [k for k in best_fits if k != "LCDM"],
        key=lambda k: best_fits[k]["chi2"]
    )
    bf = best_fits[best_ebc_label]
    xs_b = XSTARs[X0s.index(float(best_ebc_label.split("=")[1]))]
    print_residuals(bf["H0"], bf["om"], xs_b, label=best_ebc_label)

    # ── Plot ──────────────────────────────────────────────────────────────
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.gridspec as gridspec

        COLORS = ["#1565C0", "#E53935", "#2E7D32"]

        fig = plt.figure(figsize=(16, 12))
        gs  = gridspec.GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.38)

        ax_prof  = fig.add_subplot(gs[0, :2])   # Profil-chi2 (breit)
        ax_delta = fig.add_subplot(gs[0, 2])    # Delta chi2 vs 1-Par
        ax_c0    = fig.add_subplot(gs[1, 0])    # 2D-Kontur EBC x0=0.06
        ax_c1    = fig.add_subplot(gs[1, 1])    # 2D-Kontur EBC x0=0.10
        ax_cl    = fig.add_subplot(gs[1, 2])    # 2D-Kontur LCDM

        # ── Profil-chi2 über Ω_m ─────────────────────────────────────────
        for (label, col) in zip(all_profiles, COLORS + ["k"]):
            prof = all_profiles[label]
            lty  = "--" if label == "LCDM" else "-"
            lcol = "k"  if label == "LCDM" else col
            ax_prof.plot(prof[:,0], prof[:,2], color=lcol, lw=2.0,
                         ls=lty, label=label)
            idx = np.nanargmin(prof[:,2])
            ax_prof.scatter(prof[idx,0], prof[idx,2],
                            color=lcol, s=60, zorder=5)

        ax_prof.axvline(OM_PLANCK, color="gray", ls=":", lw=1.0,
                        label=f"Ω_m (Planck) = {OM_PLANCK}")
        ax_prof.axvline(OM_DESI,   color="orange", ls=":", lw=1.0,
                        label=f"Ω_m (DESI)   = {OM_DESI}")
        ax_prof.set_xlabel("Ω_m")
        ax_prof.set_ylabel("χ² (BAO, profil-minimiert über H₀)")
        ax_prof.set_title("Profil-χ²(Ω_m)  [r_d = 147.09 Mpc festgehalten]",
                          fontsize=11)
        ax_prof.legend(fontsize=8.5)
        ax_prof.grid(alpha=0.25)
        ax_prof.set_xlim(0.23, 0.43)

        # ── Delta chi2 (2-Par minus 1-Par) ───────────────────────────────
        labels_plot = list(all_profiles.keys())
        delta_vals  = [best_fits[l]["chi2"] - chi2_1p[l] for l in labels_plot]
        bar_colors  = COLORS + ["k"]
        bars = ax_delta.bar(range(len(labels_plot)), delta_vals,
                            color=bar_colors[:len(labels_plot)])
        ax_delta.axhline(-2, color="red", ls="--", lw=1.0,
                         label="AIC-Schwelle (−2)")
        ax_delta.axhline(0, color="k", ls="-", lw=0.7)
        ax_delta.set_xticks(range(len(labels_plot)))
        ax_delta.set_xticklabels(
            [l.replace("EBC ", "").replace("LCDM", "Λ") for l in labels_plot],
            fontsize=8)
        ax_delta.set_ylabel("Δχ² = χ²(2-Par) − χ²(1-Par)")
        ax_delta.set_title("Verbesserung durch freies Ω_m", fontsize=11)
        ax_delta.legend(fontsize=8); ax_delta.grid(alpha=0.25, axis="y")

        # ── 2D-Konturplots (chi2 direkt) ──────────────────────────────────
        H0_2d  = np.linspace(59.0, 74.0, 35)
        OM_2d  = np.linspace(0.25, 0.42, 35)
        HH, OO = np.meshgrid(H0_2d, OM_2d)

        plot_triples = [
            (ax_c0, 0, XSTARs[0], f"EBC x0={X0s[0]}",  COLORS[0]),
            (ax_c1, 1, XSTARs[1], f"EBC x0={X0s[1]}",  COLORS[1]),
            (ax_cl, None, None,   "ΛCDM",               "k"),
        ]

        for (ax, ix, xs, label, col) in plot_triples:
            ZZ = np.zeros_like(HH)
            for i in range(HH.shape[0]):
                for j in range(HH.shape[1]):
                    if xs is not None:
                        ZZ[i,j] = chi2_2d(HH[i,j], OO[i,j], x_star=xs)
                    else:
                        ZZ[i,j] = chi2_2d(HH[i,j], OO[i,j], is_lcdm=True)

            chi2_min = ZZ.min()
            DZ = ZZ - chi2_min
            # Δchi2-Konturen: 68.3% (2.30), 95.4% (6.17)
            cs = ax.contourf(HH, OO, DZ, levels=[0, 2.30, 6.17, 12],
                             colors=["white", "lightblue", "steelblue", "navy"],
                             alpha=0.7)
            ax.contour(HH, OO, DZ, levels=[2.30, 6.17],
                       colors=[col, col], linewidths=[1.5, 1.0])
            ax.axvline(H0_PLANCK, color="gray", ls="--", lw=0.8)
            ax.axhline(OM_PLANCK, color="gray", ls="--", lw=0.8)
            ax.axhline(OM_DESI,   color="orange", ls="--", lw=0.8)

            # Minimum markieren
            idx_flat = np.argmin(ZZ)
            i0, j0   = np.unravel_index(idx_flat, ZZ.shape)
            ax.scatter(HH[i0,j0], OO[i0,j0], color=col, s=60, zorder=6,
                       marker="*", label=f"Min: H₀={HH[i0,j0]:.1f}, "
                                         f"Ω_m={OO[i0,j0]:.3f}")

            ax.set_xlabel("H₀ [km/s/Mpc]")
            ax.set_ylabel("Ω_m")
            ax.set_title(f"Δχ²-Kontur: {label}", fontsize=10)
            ax.legend(fontsize=7.5)
            ax.grid(alpha=0.20)

        fig.suptitle(
            "EBC — 2-Parameter BAO-Fit: (H₀, Ω_m)   |   DESI DR1 2024\n"
            "Warnung: r_d = 147.09 Mpc festgehalten (Einschränkung, s. Text)",
            fontsize=11, y=1.01
        )

        out = "/mnt/user-data/outputs/ebc_bao_fit2.png"
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print(f"\nPlot gespeichert: {out}")

    except Exception as e:
        print(f"\n(Plot fehlgeschlagen: {e})")
        import traceback; traceback.print_exc()

    # ── Paper-Text-Entwurf ─────────────────────────────────────────────────
    bef = best_fits[best_ebc_label]
    bel = best_fits["LCDM"]
    chi1_ebc = chi2_1p[best_ebc_label]
    chi1_lcdm = chi2_1p["LCDM"]

    print(f"\n{sep}")
    print("Paper-Text-Entwurf: Section 8 Item 3b (2-Parameter-BAO-Fit)")
    print(sep)
    print(f"""
[Item 3b] Two-parameter BAO fit: H₀ and Ω_m simultaneously

We extend the one-parameter BAO fit of Section 8 Item 3a by treating
Ω_m as a second free parameter alongside H₀. For each value of Ω_m on
a grid, H₀ is minimised analytically (all observables scale as 1/H₀ at
fixed Ω_m and fixed r_d). The sound horizon r_d = 147.09 Mpc is held
fixed (Planck 2018 baseline); a self-consistent determination of
r_d(Ω_m, h²) (cf. Aubourg et al. 2015) is deferred to future work.

Results (dof = 10 = 12 data points − 2 free parameters):

  {best_ebc_label} (optimal):
    Ω_m = {bef['om']:.3f}
    H₀  = {bef['H0']:.2f} km/s/Mpc
    χ²  = {bef['chi2']:.2f}   χ²/dof = {bef['chi2r']:.3f}
    H₀·t₀ = {bef['H0t0']:.4f}  →  t₀ = {bef['t0']:.1f} Gyr
    Δχ² vs. one-parameter fit: {bef['chi2'] - chi1_ebc:+.2f}

  ΛCDM (reference):
    Ω_m = {bel['om']:.3f}
    H₀  = {bel['H0']:.2f} km/s/Mpc
    χ²  = {bel['chi2']:.2f}   χ²/dof = {bel['chi2r']:.3f}
    H₀·t₀ = {bel['H0t0']:.4f}  →  t₀ = {bel['t0']:.1f} Gyr
    Δχ² vs. one-parameter fit: {bel['chi2'] - chi1_lcdm:+.2f}

The AIC criterion (ΔAIC = Δχ² + 2ΔPar) penalises the additional
parameter by +2. A genuine improvement therefore requires Δχ² < −2.
The present fit uses a fixed r_d, introducing a systematic coupling
between Ω_m and r_d(Ω_m, h²) that is not accounted for; results
should be interpreted as bounds on the model tension rather than
self-consistent constraints.
""")


if __name__ == "__main__":
    main()
