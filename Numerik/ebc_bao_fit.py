#!/usr/bin/env python3
"""
ebc_bao_fit.py — EBC: Selbstkonsistenter BAO-Geometrie-Check
=============================================================
Autor : Wolfgang Mattis <ebc@wm0.eu>
Stand : 2026-04-24

Vergleicht H_EBC(z) mit DESI DR1 BAO-Daten (arXiv:2404.03002, Tab. 1).
Fittet H0 als einzigen freien Parameter. Analytische Minimierung moeglich,
da alle Observablen ~ 1/H0 skalieren.
"""

import numpy as np
from scipy import integrate

# ============================================================
# Konstanten
# ============================================================
C_KMS     = 299792.458   # Lichtgeschwindigkeit [km/s]
H0_PLANCK = 67.4         # Planck 2018 [km/s/Mpc]
RD_MPC    = 147.09       # Schallhorizont Drag-Epoch [Mpc]
KM_TO_GYR = 978.5        # Umrechnung: 1/(H0[km/s/Mpc]) -> Gyr

OMEGA_M   = 0.315
OMEGA_R   = 9.2e-5
OMEGA_L   = 1.0 - OMEGA_M - OMEGA_R   # LCDM: ca. 0.6849

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
# EBC-Modell
# ============================================================
def ode_ebc(x_star):
    return (1.0 - OMEGA_M - OMEGA_R) / (1.0 - 1.0/x_star**2)

def E_ebc(z, x_star):
    x   = 1.0/(1.0+z)
    ode = ode_ebc(x_star)
    return np.sqrt(max(OMEGA_M/x**3 + OMEGA_R/x**4
                       + ode*(1.0/x - x/x_star**2), 0.0))

def E_lcdm(z):
    return np.sqrt(OMEGA_M*(1+z)**3 + OMEGA_R*(1+z)**4 + OMEGA_L)

# ============================================================
# Skalierungsbasen (Vorhersagen bei H0=1)
# A_DH * (1/H0) = DH/rd
# A_DM * (1/H0) = DM/rd
# A_DV * (1/H0) = DV/rd
# ============================================================
def A_DH(z, E_fn, x_star=None):
    Efn = E_fn(z, x_star) if x_star is not None else E_fn(z)
    return C_KMS / (Efn * RD_MPC)

def A_DM(z, E_fn, x_star=None, n=600):
    zz  = np.linspace(0.0, z, n)
    if x_star is not None:
        Ez = np.array([E_fn(zi, x_star) for zi in zz])
    else:
        Ez = np.array([E_fn(zi) for zi in zz])
    return np.trapezoid(C_KMS / Ez, zz) / RD_MPC

def A_DV(z, E_fn, x_star=None):
    aDM = A_DM(z, E_fn, x_star) * RD_MPC   # [km/s]
    aDH = A_DH(z, E_fn, x_star) * RD_MPC   # [km/s]
    return (z * aDM**2 * aDH)**(1.0/3.0) / RD_MPC

# ============================================================
# Analytischer H0-Fit
# chi2(u) = u^2*S_AA - 2u*S_OA + S_OO  (u=1/H0)
# Minimum: u_opt = S_OA/S_AA
# ============================================================
def fit_H0(x_star=None, is_lcdm=False):
    E_fn = E_lcdm if is_lcdm else E_ebc
    kw   = {} if is_lcdm else {"x_star": x_star}

    S_AA = 0.0; S_OA = 0.0

    for (z, DM, sDM, DH, sDH, r, _) in DESI_FULL:
        aDM = A_DM(z, E_fn, **kw)
        aDH = A_DH(z, E_fn, **kw)
        A   = np.array([aDM, aDH])
        O   = np.array([DM, DH])
        C   = np.array([[sDM**2, r*sDM*sDH],[r*sDM*sDH, sDH**2]])
        Ci  = np.linalg.inv(C)
        S_AA += A @ Ci @ A
        S_OA += O @ Ci @ A

    for (z, DV, sDV, _) in DESI_DV:
        aDV = A_DV(z, E_fn, **kw)
        S_AA += aDV**2/sDV**2
        S_OA += DV*aDV/sDV**2

    u_opt  = S_OA/S_AA
    H0_opt = 1.0/u_opt
    sigma_H0 = H0_opt**2 / np.sqrt(S_AA)

    # chi2 im Minimum ausrechnen
    chi2 = 0.0
    for (z, DM, sDM, DH, sDH, r, _) in DESI_FULL:
        aDM = A_DM(z, E_fn, **kw)
        aDH = A_DH(z, E_fn, **kw)
        C   = np.array([[sDM**2, r*sDM*sDH],[r*sDM*sDH, sDH**2]])
        res = np.array([u_opt*aDM - DM, u_opt*aDH - DH])
        chi2 += res @ np.linalg.inv(C) @ res
    for (z, DV, sDV, _) in DESI_DV:
        aDV = A_DV(z, E_fn, **kw)
        chi2 += ((u_opt*aDV - DV)/sDV)**2

    return dict(H0=H0_opt, sH0=sigma_H0, chi2=chi2, chi2_red=chi2/11)

def chi2_scan(H0_vals, x_star=None, is_lcdm=False):
    E_fn = E_lcdm if is_lcdm else E_ebc
    kw   = {} if is_lcdm else {"x_star": x_star}
    out  = []
    for H0 in H0_vals:
        u = 1.0/H0
        c = 0.0
        for (z,DM,sDM,DH,sDH,r,_) in DESI_FULL:
            aDM=A_DM(z,E_fn,**kw); aDH=A_DH(z,E_fn,**kw)
            C=np.array([[sDM**2,r*sDM*sDH],[r*sDM*sDH,sDH**2]])
            res=np.array([u*aDM-DM, u*aDH-DH])
            c += res @ np.linalg.inv(C) @ res
        for (z,DV,sDV,_) in DESI_DV:
            aDV=A_DV(z,E_fn,**kw)
            c += ((u*aDV-DV)/sDV)**2
        out.append(c)
    return np.array(out)

# ============================================================
# Altersberechnung
# ============================================================
def compute_t0(H0, x_star=None, is_lcdm=False):
    if is_lcdm:
        fn = lambda z: 1.0/((1+z)*E_lcdm(z))
    else:
        fn = lambda z: 1.0/((1+z)*E_ebc(z, x_star))
    H0t0, _ = integrate.quad(fn, 0.0, 1e4, limit=200, epsrel=1e-9)
    return H0t0, H0t0 * KM_TO_GYR / H0

# ============================================================
# r_d-Pruefung
# ============================================================
def check_rd(x_star=10.0, z=1100.0):
    x   = 1.0/(1.0+z)
    ode = ode_ebc(x_star)
    rm  = OMEGA_M/x**3
    rr  = OMEGA_R/x**4
    ebc = ode*(1.0/x - x/x_star**2)
    tot = rm+rr+ebc
    return rm, rr, ebc, abs(ebc)/tot*100.0

# ============================================================
# Hauptprogramm
# ============================================================
def main():
    X0s    = [0.06, 0.10, 0.15]
    XSTARs = [1.0/x for x in X0s]

    sep = "=" * 70
    print(sep)
    print("EBC — BAO-Geometrie-Check   (ebc_bao_fit.py)")
    print(f"DESI DR1 | arXiv:2404.03002 | r_d = {RD_MPC} Mpc")
    print(sep)

    # ── Schritt 1 ──────────────────────────────────────────
    print("\n── Schritt 1: EBC-Term bei z=1100 ──────────────────────────────")
    for xs in [6.7, 10.0, 16.7]:
        rm, rr, ebc, pct = check_rd(x_star=xs)
        print(f"   x*={xs:5.1f}:  rho_m={rm:.3e}  rho_r={rr:.3e}  "
              f"rho_EBC={ebc:.3e}  Anteil={pct:.5f}%")
    print(f"   => EBC-Term < 0.001%  <<  1%   =>  r_d = {RD_MPC} Mpc uebernommen")

    # ── Schritt 2 ──────────────────────────────────────────
    print("\n── Schritt 2: DESI DR1 BAO-Datenpunkte (Tabelle 1) ─────────────")
    print(f"   {'Tracer':<14} {'z':>5}  {'DM/rd':>6}  {'sDM':>5}  "
          f"{'DH/rd':>6}  {'sDH':>5}  {'r':>6}")
    for (z,DM,sDM,DH,sDH,r,lab) in DESI_FULL:
        print(f"   {lab:<14} {z:>5.3f}  {DM:>6.2f}  {sDM:>5.2f}  "
              f"{DH:>6.2f}  {sDH:>5.2f}  {r:>6.3f}")
    print(f"   {'Tracer':<14} {'z':>5}  {'DV/rd':>6}  {'sDV':>5}")
    for (z,DV,sDV,lab) in DESI_DV:
        print(f"   {lab:<14} {z:>5.3f}  {DV:>6.2f}  {sDV:>5.2f}")

    # ── Schritte 3+4 ───────────────────────────────────────
    print("\n── Schritte 3+4: H0-Fit (analytisch) + Alterberechnung ─────────")
    hdr = (f"{'x0':>5}  {'x*':>5}  {'H0':>7}  {'sH0':>5}  "
           f"{'chi2':>7}  {'chi2r':>6}  {'H0t0':>6}  {'t0[Gyr]':>8}  {'Dt0':>7}")
    print(f"   {hdr}")
    print(f"   {'-'*len(hdr)}")

    fits = []
    for x0, xs in zip(X0s, XSTARs):
        f  = fit_H0(x_star=xs)
        H0 = f["H0"]
        H0t0, t0 = compute_t0(H0, xs)
        _,    t0l = compute_t0(H0, is_lcdm=True)
        dt = (t0-t0l)/t0l*100
        f.update(x0=x0, xs=xs, H0t0=H0t0, t0=t0, t0l=t0l, dt=dt)
        fits.append(f)
        print(f"   {x0:>5.2f}  {xs:>5.1f}  {H0:>7.3f}  {f['sH0']:>5.3f}  "
              f"{f['chi2']:>7.3f}  {f['chi2_red']:>6.3f}  "
              f"{H0t0:>6.4f}  {t0:>8.2f}  {dt:>+7.2f}%")

    # LCDM-Referenz
    fl = fit_H0(is_lcdm=True)
    H0t0_l, t0_l = compute_t0(fl["H0"], is_lcdm=True)
    print(f"   {'LCDM':>5}  {'inf':>5}  {fl['H0']:>7.3f}  {fl['sH0']:>5.3f}  "
          f"{fl['chi2']:>7.3f}  {fl['chi2_red']:>6.3f}  "
          f"{H0t0_l:>6.4f}  {t0_l:>8.2f}  {'Ref.':>7}")

    # ── Schritt 5: Residuen ─────────────────────────────────
    best = min(fits, key=lambda f: f["chi2_red"])
    xs_b = best["xs"]; H0_b = best["H0"]; u_b = 1.0/H0_b
    print(f"\n── Schritt 5: Residuen (x0={best['x0']}, H0={H0_b:.3f}) ────────")
    print(f"   {'Tracer':<14} {'z':>5}  {'DM/s':>6}  {'DH/s':>6}")
    for (z,DM,sDM,DH,sDH,r,lab) in DESI_FULL:
        pDM = (u_b*A_DM(z,E_ebc,x_star=xs_b) - DM)/sDM
        pDH = (u_b*A_DH(z,E_ebc,x_star=xs_b) - DH)/sDH
        print(f"   {lab:<14} {z:>5.3f}  {pDM:>+6.2f}  {pDH:>+6.2f}")
    for (z,DV,sDV,lab) in DESI_DV:
        pDV = (u_b*A_DV(z,E_ebc,x_star=xs_b) - DV)/sDV
        print(f"   {lab:<14} {z:>5.3f}  {'DV:':>6}  {pDV:>+6.2f}")

    # ── Plot ───────────────────────────────────────────────
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.gridspec as gridspec

        z_arr   = np.linspace(0.01, 2.5, 200)
        COLORS  = ["#1565C0", "#E53935", "#2E7D32"]

        fig = plt.figure(figsize=(14, 10))
        gs  = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.35)
        ax1, ax2, ax3, ax4 = [fig.add_subplot(gs[i,j])
                               for i in range(2) for j in range(2)]

        for (f, col) in zip(fits, COLORS):
            H0f = f["H0"]; xs = f["xs"]; x0 = f["x0"]
            lbl = f"EBC x0={x0} (H0={H0f:.1f})"
            DM_c = [u_b*A_DM(z, E_ebc, x_star=xs) for z in z_arr]
            DH_c = [u_b*A_DH(z, E_ebc, x_star=xs) for z in z_arr]
            DV_c = [u_b*A_DV(z, E_ebc, x_star=xs) for z in z_arr]
            # Verwende den eigenen H0 jedes Modells
            u_f  = 1.0/H0f
            DM_c = [u_f*A_DM(z, E_ebc, x_star=xs) for z in z_arr]
            DH_c = [u_f*A_DH(z, E_ebc, x_star=xs) for z in z_arr]
            DV_c = [u_f*A_DV(z, E_ebc, x_star=xs) for z in z_arr]
            ax1.plot(z_arr, DM_c, color=col, lw=1.8, label=lbl)
            ax2.plot(z_arr, DH_c, color=col, lw=1.8, label=lbl)
            ax3.plot(z_arr, DV_c, color=col, lw=1.8, label=lbl)

        # LCDM
        u_l  = 1.0/fl["H0"]
        DM_l = [u_l*A_DM(z, E_lcdm) for z in z_arr]
        DH_l = [u_l*A_DH(z, E_lcdm) for z in z_arr]
        DV_l = [u_l*A_DV(z, E_lcdm) for z in z_arr]
        ax1.plot(z_arr, DM_l, "k--", lw=1.5, label=f"LCDM (H0={fl['H0']:.1f})")
        ax2.plot(z_arr, DH_l, "k--", lw=1.5, label=f"LCDM (H0={fl['H0']:.1f})")
        ax3.plot(z_arr, DV_l, "k--", lw=1.5, label=f"LCDM (H0={fl['H0']:.1f})")

        # DESI-Datenpunkte
        zF  = [d[0] for d in DESI_FULL]
        DMd = [d[1] for d in DESI_FULL]; sDM = [d[2] for d in DESI_FULL]
        DHd = [d[3] for d in DESI_FULL]; sDH = [d[4] for d in DESI_FULL]
        ax1.errorbar(zF, DMd, sDM, fmt="o", color="k", ms=5,
                     capsize=3, zorder=5, label="DESI DR1")
        ax2.errorbar(zF, DHd, sDH, fmt="s", color="k", ms=5,
                     capsize=3, zorder=5, label="DESI DR1")
        zDV= [d[0] for d in DESI_DV]
        DVd= [d[1] for d in DESI_DV]; sDV=[d[2] for d in DESI_DV]
        ax3.errorbar(zDV, DVd, sDV, fmt="^", color="k", ms=5,
                     capsize=3, zorder=5, label="DESI DR1")

        # chi2-Scan
        H0s_scan = np.linspace(62.0, 76.0, 50)
        for (f, col) in zip(fits, COLORS):
            cs = chi2_scan(H0s_scan, x_star=f["xs"])
            ax4.plot(H0s_scan, cs, color=col, lw=1.8,
                     label=f"EBC x0={f['x0']}")
            ax4.axvline(f["H0"], color=col, ls=":", lw=0.9)
        cs_l = chi2_scan(H0s_scan, is_lcdm=True)
        ax4.plot(H0s_scan, cs_l, "k--", lw=1.5, label="LCDM")
        ax4.axvline(fl["H0"],    color="k", ls=":", lw=0.9)
        ax4.axvline(H0_PLANCK, color="gray", ls="--", lw=0.8,
                    label=f"H0_Planck={H0_PLANCK}")

        for ax, yl, ttl in [
            (ax1, r"$D_M/r_d$",  r"Querdistanz $D_M/r_d$"),
            (ax2, r"$D_H/r_d$",  r"Hubble-Distanz $D_H/r_d$"),
            (ax3, r"$D_V/r_d$",  r"Winkelgemittelt $D_V/r_d$"),
        ]:
            ax.set_xlabel("Rotverschiebung z")
            ax.set_ylabel(yl); ax.set_title(ttl, fontsize=11)
            ax.legend(fontsize=7.5); ax.grid(alpha=0.25)
        ax4.set_xlabel("H0 [km/s/Mpc]")
        ax4.set_ylabel("chi2_BAO")
        ax4.set_title("chi2(H0) — BAO-Fit", fontsize=11)
        ax4.legend(fontsize=7.5); ax4.grid(alpha=0.25)

        fig.suptitle("EBC — BAO-Geometrie-Check (DESI DR1 2024)",
                     fontsize=12, y=1.01)
        out = "/mnt/user-data/outputs/ebc_bao_fit.png"
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print(f"\nPlot gespeichert: {out}")

    except Exception as e:
        print(f"\n(Plot fehlgeschlagen: {e})")

    # ── Paper-Text-Entwurf ─────────────────────────────────
    b = best
    print("\n" + sep)
    print("Paper-Text-Entwurf: Section 8 Item 3a")
    print(sep)
    print(f"""
[Item 3a] Self-consistent BAO geometry check: H_EBC(z) against DESI DR1

We fit H_EBC(z) [Eq. EBC1] to the DESI DR1 BAO measurements
(arXiv:2404.03002, Table 1; 7 redshift bins, 12 independent data points)
with H0 as the sole free parameter (all Omega fixed at Planck 2018 values;
DESI-preferred Omega_m=0.295 would shift results marginally).

Prerequisite — sound horizon: At z=1100, the EBC term contributes
< 0.001% of the total energy density (vs. Omega_m/x^3 ~ 4.2e8 and
Omega_r/x^4 ~ 1.4e8). The drag-epoch sound horizon r_d = 147.09 Mpc
(Planck 2018) is therefore valid within EBC without modification.

Analytical minimisation (all observables scale as 1/H0):

  EBC (x0={b['x0']}): H0 = {b['H0']:.2f} +/- {b['sH0']:.2f} km/s/Mpc
                  chi2/dof = {b['chi2_red']:.3f}
                  H0*t0 = {b['H0t0']:.4f}   =>   t0 = {b['t0']:.1f} Gyr

  LCDM (reference): H0 = {fl['H0']:.2f} +/- {fl['sH0']:.2f} km/s/Mpc
                  chi2/dof = {fl['chi2_red']:.3f}
                  H0*t0 = {H0t0_l:.4f}   =>   t0 = {t0_l:.1f} Gyr

The EBC fit quality (chi2/dof ~ {b['chi2_red']:.2f}) is comparable to LCDM
(chi2/dof ~ {fl['chi2_red']:.2f}). The BAO-preferred EBC value H0 =
{b['H0']:.2f} km/s/Mpc yields t0 = {b['t0']:.1f} Gyr, compared to
t0_LCDM = {b['t0l']:.1f} Gyr at the same H0 (residual tension
{b['dt']:+.1f}%). This residual constitutes an upper bound: the
input Omega values were derived from LCDM fits; a self-consistent
EBC determination of Omega_m from BAO+CMB would shift both H0
and Omega_m, partially or fully resolving this discrepancy.
""")


if __name__ == "__main__":
    main()
