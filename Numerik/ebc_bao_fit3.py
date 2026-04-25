#!/usr/bin/env python3
"""
ebc_bao_fit3.py — EBC: BAO-Fit mit selbstkonsistentem r_d (Aubourg-Formel)
=========================================================================
Autor : Wolfgang Mattis <ebc@wm0.eu>
Stand : 2026-04-24

Methode:
  Erweiterung von ebc_bao_fit2.py: r_d wird nicht mehr festgehalten,
  sondern via Aubourg-Formel (arXiv:1411.1074, Eq. 16) aus (Omega_m, h^2,
  Omega_b h^2) selbstkonsistent berechnet. Bei Omega_b h^2 = 0.02237
  (Planck 2018 / BBN) fest reduziert sich dies auf einen 2-Parameter-Fit
  mit konsistenter r_d(Omega_m, H0)-Kopplung -- physikalisch der korrekte
  Vergleich zu fit2.

  Optional: Omega_b h^2 frei mit Gauss-Prior aus BBN (Variante B).

Unterschied zu fit2:
  fit2 haelt r_d = 147.09 Mpc fest -> Omega_m und r_d entkoppelt (obere Schranke)
  fit3 bindet r_d = r_d(Omega_m, h)  -> selbstkonsistent (korrekte Modellspannung)

Gueltigkeitscheck:
  - Aubourg-Formel kalibriert gegen CAMB/CLASS in LCDM-Standardkosmologie.
  - EBC-Term bei z_drag ~ 1060 numerisch < 0.0002% (vernachlaessigbar).
  - Aubourg bleibt im EBC-Rahmen unveraendert anwendbar.
  - Kovarianzen DM/DH aus DESI Y1 Tab. 1 (identisch zu fit2).

DESI-Daten: arXiv:2404.03002, Tabelle 1 (12 Messpunkte, 7 Bins)
"""

import numpy as np
from scipy import integrate, optimize

C_KMS     = 299792.458
H0_PLANCK = 67.4
OM_PLANCK = 0.315
OM_DESI   = 0.295
OMEGA_R   = 9.2e-5
KM_TO_GYR = 978.5

OMEGA_B_H2_BBN = 0.02237
OMEGA_B_H2_SIG = 0.00015
OMEGA_NU_H2    = 0.0006

RD_REF_MPC = 147.09

DESI_FULL = [
    (0.510, 13.62, 0.25, 20.98, 0.61, -0.445, "LRG1"),
    (0.706, 16.85, 0.32, 20.08, 0.60, -0.420, "LRG2"),
    (0.930, 21.71, 0.28, 17.88, 0.35, -0.389, "LRG3+ELG1"),
    (1.317, 27.79, 0.69, 13.82, 0.42, -0.444, "ELG2"),
    (2.330, 39.71, 0.94,  8.52, 0.17, -0.477, "Lya"),
]
DESI_DV = [
    (0.295,  7.93, 0.15, "BGS"),
    (1.491, 26.07, 0.67, "QSO"),
]


def omega_de_ebc(omega_m, x_star):
    return (1.0 - omega_m - OMEGA_R) / (1.0 - 1.0/x_star**2)

def E_ebc(z, omega_m, x_star):
    x   = 1.0 / (1.0 + z)
    ode = omega_de_ebc(omega_m, x_star)
    val = omega_m/x**3 + OMEGA_R/x**4 + ode*(1.0/x - x/x_star**2)
    return np.sqrt(max(val, 0.0))

def E_lcdm(z, omega_m):
    omega_l = 1.0 - omega_m - OMEGA_R
    return np.sqrt(omega_m*(1+z)**3 + OMEGA_R*(1+z)**4 + omega_l)


def r_d_aubourg(omega_m, h, omega_b_h2=OMEGA_B_H2_BBN,
                omega_nu_h2=OMEGA_NU_H2):
    om_m_h2 = omega_m * h * h
    num = 55.154 * np.exp(-72.3 * (omega_nu_h2 + 0.0006)**2)
    den = (om_m_h2**0.25351) * (omega_b_h2**0.12807)
    return num / den


def DM_over_rd(z, H0, E_fn, rd, *args, n=600):
    zz = np.linspace(0.0, z, n)
    Ez = np.array([E_fn(zi, *args) for zi in zz])
    DM_com = np.trapezoid(C_KMS / Ez, zz) / H0
    return DM_com / rd

def DH_over_rd(z, H0, E_fn, rd, *args):
    DH = C_KMS / (E_fn(z, *args) * H0)
    return DH / rd

def DV_over_rd(z, H0, E_fn, rd, *args):
    DM = DM_over_rd(z, H0, E_fn, rd, *args) * rd
    DH = DH_over_rd(z, H0, E_fn, rd, *args) * rd
    return (z * DM*DM * DH)**(1.0/3.0) / rd


def chi2_bao(H0, omega_m, x_star=None, is_lcdm=False,
             omega_b_h2=OMEGA_B_H2_BBN):
    if is_lcdm:
        E_fn, args = E_lcdm, (omega_m,)
    else:
        E_fn, args = E_ebc, (omega_m, x_star)

    h  = H0 / 100.0
    rd = r_d_aubourg(omega_m, h, omega_b_h2)

    chi2 = 0.0
    for (z, DMv, sDM, DHv, sDH, r, _) in DESI_FULL:
        pDM = DM_over_rd(z, H0, E_fn, rd, *args)
        pDH = DH_over_rd(z, H0, E_fn, rd, *args)
        res = np.array([pDM - DMv, pDH - DHv])
        C   = np.array([[sDM**2,        r*sDM*sDH],
                        [r*sDM*sDH,     sDH**2   ]])
        chi2 += res @ np.linalg.inv(C) @ res

    for (z, DVv, sDV, _) in DESI_DV:
        pDV = DV_over_rd(z, H0, E_fn, rd, *args)
        chi2 += ((pDV - DVv)/sDV)**2

    return chi2, rd


def fit_H0_given_om(omega_m, x_star=None, is_lcdm=False,
                    omega_b_h2=OMEGA_B_H2_BBN, H0_init=66.0):
    def _obj(H0_arr):
        H0 = H0_arr[0]
        if H0 < 20 or H0 > 120:
            return 1e10
        chi2, _ = chi2_bao(H0, omega_m, x_star, is_lcdm, omega_b_h2)
        return chi2
    res = optimize.minimize(_obj, x0=[H0_init], method="Nelder-Mead",
                            options={"xatol": 1e-4, "fatol": 1e-6,
                                     "maxiter": 2000})
    H0_opt = res.x[0]
    chi2_opt, rd_opt = chi2_bao(H0_opt, omega_m, x_star, is_lcdm, omega_b_h2)
    return dict(H0=H0_opt, chi2=chi2_opt, chi2_red=chi2_opt/10,
                omega_m=omega_m, r_d=rd_opt)


def fit_full_variant_A(x_star=None, is_lcdm=False):
    def _obj(p):
        H0, Om = p
        if H0 < 20 or H0 > 120 or Om <= 0.01 or Om >= 0.99:
            return 1e10
        chi2, _ = chi2_bao(H0, Om, x_star, is_lcdm)
        return chi2
    res = optimize.minimize(_obj, x0=[65.0, 0.30], method="Nelder-Mead",
                            options={"xatol": 1e-5, "fatol": 1e-7,
                                     "maxiter": 5000})
    H0, Om = res.x
    chi2, rd = chi2_bao(H0, Om, x_star, is_lcdm)
    return dict(H0=H0, omega_m=Om, chi2=chi2, chi2_red=chi2/10, r_d=rd,
                omega_b_h2=OMEGA_B_H2_BBN)


def fit_full_variant_B(x_star=None, is_lcdm=False):
    def _obj(p):
        H0, Om, Obh2 = p
        if H0<20 or H0>120 or Om<=0.01 or Om>=0.99 or Obh2<=0:
            return 1e10
        chi2, _ = chi2_bao(H0, Om, x_star, is_lcdm, omega_b_h2=Obh2)
        chi2 += ((Obh2 - OMEGA_B_H2_BBN)/OMEGA_B_H2_SIG)**2
        return chi2
    res = optimize.minimize(_obj, x0=[65.0, 0.30, 0.02237],
                            method="Nelder-Mead",
                            options={"xatol": 1e-6, "fatol": 1e-8,
                                     "maxiter": 10000})
    H0, Om, Obh2 = res.x
    chi2, rd = chi2_bao(H0, Om, x_star, is_lcdm, omega_b_h2=Obh2)
    dof = 12 - 3
    return dict(H0=H0, omega_m=Om, omega_b_h2=Obh2, chi2=chi2,
                chi2_red=chi2/dof, r_d=rd)


def compute_t0(H0, omega_m, x_star=None, is_lcdm=False):
    if is_lcdm:
        fn = lambda z: 1.0/((1+z)*E_lcdm(z, omega_m))
    else:
        fn = lambda z: 1.0/((1+z)*E_ebc(z, omega_m, x_star))
    H0t0, _ = integrate.quad(fn, 0.0, 1e4, limit=200, epsrel=1e-9)
    return H0t0, H0t0 * KM_TO_GYR / H0


def print_residuals(H0, omega_m, x_star, rd, label="EBC"):
    args = (omega_m, x_star)
    print(f"\n   Residuen {label} (Om={omega_m:.3f}, H0={H0:.2f}, r_d={rd:.2f}):")
    print(f"   {'Tracer':<14} {'z':>5}  {'DM/sig':>7}  {'DH/sig':>7}")
    for (z, DMv, sDM, DHv, sDH, r, lab) in DESI_FULL:
        pDM = (DM_over_rd(z, H0, E_ebc, rd, *args) - DMv)/sDM
        pDH = (DH_over_rd(z, H0, E_ebc, rd, *args) - DHv)/sDH
        mark_DM = " **" if abs(pDM) > 2.0 else "   "
        mark_DH = " **" if abs(pDH) > 2.0 else "   "
        print(f"   {lab:<14} {z:>5.3f}  {pDM:>+6.2f}{mark_DM} "
              f"{pDH:>+6.2f}{mark_DH}")
    print(f"   {'':<14} {'':5}  {'DV/sig':>7}")
    for (z, DVv, sDV, lab) in DESI_DV:
        pDV = (DV_over_rd(z, H0, E_ebc, rd, *args) - DVv)/sDV
        mark = " **" if abs(pDV) > 2.0 else "   "
        print(f"   {lab:<14} {z:>5.3f}  {pDV:>+6.2f}{mark}")


def main():
    sep = "=" * 78
    print(sep)
    print("EBC 3-Parameter-Fit: selbstkonsistentes r_d (Aubourg-Formel)")
    print("DESI Y1 BAO (arXiv:2404.03002) mit vollen DM/DH-Korrelationen")
    print(sep)

    X0s     = [0.06, 0.10, 0.15]
    X0_STRS = ["0.06", "0.10", "0.15"]
    XSTARs  = [1.0/x for x in X0s]

    print("\n-- Schritt 1: Variante A (H0, Om frei; Omega_b h^2 = 0.02237 fest) --")
    best_fits = {}
    for x0, x0s, xs in zip(X0s, X0_STRS, XSTARs):
        fit = fit_full_variant_A(x_star=xs)
        _, t0 = compute_t0(fit["H0"], fit["omega_m"], xs)
        fit["t0"] = t0
        label = f"EBC x0={x0s}"
        best_fits[label] = fit
        print(f"   {label:<14} Om={fit['omega_m']:.4f}  H0={fit['H0']:6.2f}"
              f"  r_d={fit['r_d']:6.2f}  chi2={fit['chi2']:6.3f}"
              f"  chi2/dof={fit['chi2_red']:.3f}  t0={t0:.2f} Gyr")
    fit_l = fit_full_variant_A(is_lcdm=True)
    _, t0_l = compute_t0(fit_l["H0"], fit_l["omega_m"], is_lcdm=True)
    fit_l["t0"] = t0_l
    best_fits["LCDM"] = fit_l
    print(f"   {'LCDM':<14} Om={fit_l['omega_m']:.4f}  H0={fit_l['H0']:6.2f}"
          f"  r_d={fit_l['r_d']:6.2f}  chi2={fit_l['chi2']:6.3f}"
          f"  chi2/dof={fit_l['chi2_red']:.3f}  t0={t0_l:.2f} Gyr")

    print("\n-- Schritt 2: Variante B (H0, Om, Omega_b h^2 frei mit BBN-Prior) --")
    for x0, x0s, xs in zip(X0s, X0_STRS, XSTARs):
        fit = fit_full_variant_B(x_star=xs)
        _, t0 = compute_t0(fit["H0"], fit["omega_m"], xs)
        label = f"EBC x0={x0s}"
        print(f"   {label:<14} Om={fit['omega_m']:.4f}  H0={fit['H0']:6.2f}"
              f"  Ob_h2={fit['omega_b_h2']:.5f}"
              f"  r_d={fit['r_d']:6.2f}  chi2={fit['chi2']:6.3f}"
              f"  t0={t0:.2f} Gyr")
    fit_lB = fit_full_variant_B(is_lcdm=True)
    _, t0_lB = compute_t0(fit_lB["H0"], fit_lB["omega_m"], is_lcdm=True)
    print(f"   {'LCDM':<14} Om={fit_lB['omega_m']:.4f}  H0={fit_lB['H0']:6.2f}"
          f"  Ob_h2={fit_lB['omega_b_h2']:.5f}"
          f"  r_d={fit_lB['r_d']:6.2f}  chi2={fit_lB['chi2']:6.3f}"
          f"  t0={t0_lB:.2f} Gyr")

    print("\n-- Schritt 3: Profil-chi2 ueber Om (Variante A) --")
    om_grid = np.linspace(0.23, 0.40, 35)
    all_profiles = {}
    for x0, x0s, xs in zip(X0s, X0_STRS, XSTARs):
        prof = []
        for om in om_grid:
            f = fit_H0_given_om(om, x_star=xs,
                                H0_init=best_fits[f"EBC x0={x0s}"]["H0"])
            prof.append([om, f["H0"], f["chi2"], f["r_d"]])
        prof = np.array(prof)
        all_profiles[f"EBC x0={x0s}"] = prof
        om_opt = prof[np.argmin(prof[:,2]), 0]
        chi2min = prof[:,2].min()
        mask = prof[:,2] - chi2min < 1.0
        if mask.any():
            om_lo, om_hi = prof[mask,0].min(), prof[mask,0].max()
            print(f"   EBC x0={x0:.2f}: Om = {om_opt:.3f}  "
                  f"[{om_lo:.3f}, {om_hi:.3f}]  (Delta chi2 < 1)")

    prof_l = []
    for om in om_grid:
        f = fit_H0_given_om(om, is_lcdm=True, H0_init=fit_l["H0"])
        prof_l.append([om, f["H0"], f["chi2"], f["r_d"]])
    prof_l = np.array(prof_l)
    all_profiles["LCDM"] = prof_l
    om_opt = prof_l[np.argmin(prof_l[:,2]), 0]
    chi2min = prof_l[:,2].min()
    mask = prof_l[:,2] - chi2min < 1.0
    if mask.any():
        om_lo, om_hi = prof_l[mask,0].min(), prof_l[mask,0].max()
        print(f"   LCDM:         Om = {om_opt:.3f}  "
              f"[{om_lo:.3f}, {om_hi:.3f}]  (Delta chi2 < 1)")

    print("\n-- Schritt 4: Vergleich fit2 (fest r_d) vs. fit3 (Aubourg) --")
    fit2_ref = {
        "EBC x0=0.06": dict(Om=0.283, H0=64.48, chi2_red=1.869),
        "EBC x0=0.10": dict(Om=0.283, H0=64.43, chi2_red=1.879),
        "EBC x0=0.15": dict(Om=0.283, H0=64.33, chi2_red=1.900),
        "LCDM":        dict(Om=0.293, H0=69.32, chi2_red=1.281),
    }
    print(f"   {'Modell':<14} {'Variante':<12} {'Om':>7} {'H0':>7}"
          f" {'r_d':>7} {'chi2/dof':>9}")
    print(f"   {'-'*62}")
    for label in ["EBC x0=0.06", "EBC x0=0.10", "EBC x0=0.15", "LCDM"]:
        ref = fit2_ref[label]
        new = best_fits[label]
        print(f"   {label:<14} {'fit2 (fest)':<12} {ref['Om']:>7.3f}"
              f" {ref['H0']:>7.2f} {'147.09':>7} {ref['chi2_red']:>9.3f}")
        print(f"   {label:<14} {'fit3 (self)':<12} {new['omega_m']:>7.3f}"
              f" {new['H0']:>7.2f} {new['r_d']:>7.2f} {new['chi2_red']:>9.3f}")
        print(f"   {'-'*62}")

    best_ebc_label = min([k for k in best_fits if k.startswith("EBC")],
                         key=lambda k: best_fits[k]["chi2"])
    bf = best_fits[best_ebc_label]
    xs_b = XSTARs[X0s.index(float(best_ebc_label.split("=")[1]))]
    print_residuals(bf["H0"], bf["omega_m"], xs_b, bf["r_d"],
                    label=best_ebc_label)

    # Sanity-Check: Aubourg bei Planck-Werten
    print("\n-- Sanity-Check Aubourg-Formel --")
    for (Om, h, desc) in [(0.315, 0.674, "Planck 2018"),
                           (0.30,  0.70,  "Round numbers"),
                           (0.293, 0.693, "fit2 LCDM"),
                           (0.283, 0.645, "fit2 EBC")]:
        rd = r_d_aubourg(Om, h)
        print(f"   {desc:<18} Om={Om}, h={h}: r_d = {rd:.3f} Mpc")

    # Plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.gridspec as gridspec

        COLORS = ["#1565C0", "#E53935", "#2E7D32"]
        fig = plt.figure(figsize=(15, 10))
        gs  = gridspec.GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.28)
        ax_prof = fig.add_subplot(gs[0, :])
        ax_res  = fig.add_subplot(gs[1, 0])
        ax_cmp  = fig.add_subplot(gs[1, 1])

        for (label, col) in zip(["EBC x0=0.06","EBC x0=0.10","EBC x0=0.15"],
                                 COLORS):
            prof = all_profiles[label]
            ax_prof.plot(prof[:,0], prof[:,2] - prof[:,2].min(),
                         color=col, lw=2, label=label)
        ax_prof.plot(prof_l[:,0], prof_l[:,2] - prof_l[:,2].min(),
                     color="k", ls="--", lw=2, label="LCDM")
        ax_prof.axhline(1, color="gray", ls=":", lw=0.8, label="1 sigma")
        ax_prof.axhline(4, color="gray", ls="--", lw=0.8, label="2 sigma")
        ax_prof.axvline(OM_PLANCK, color="gray", ls=":", lw=0.8)
        ax_prof.axvline(OM_DESI, color="orange", ls=":", lw=0.8)
        ax_prof.set_xlabel("Omega_m")
        ax_prof.set_ylabel("Delta chi2 (profil-min. ueber H0)")
        ax_prof.set_title("Profil-Likelihood Om (Variante A, r_d = Aubourg)")
        ax_prof.legend(fontsize=9, ncol=2)
        ax_prof.grid(alpha=0.25)
        ax_prof.set_ylim(0, 15)

        labels_bar = []
        res_ebc = []
        res_lcdm = []
        bf_l = fit_l
        for (z, DMv, sDM, DHv, sDH, r, lab) in DESI_FULL:
            pDM_e = (DM_over_rd(z, bf["H0"], E_ebc, bf["r_d"],
                                bf["omega_m"], xs_b) - DMv)/sDM
            pDH_e = (DH_over_rd(z, bf["H0"], E_ebc, bf["r_d"],
                                bf["omega_m"], xs_b) - DHv)/sDH
            pDM_l = (DM_over_rd(z, bf_l["H0"], E_lcdm, bf_l["r_d"],
                                bf_l["omega_m"]) - DMv)/sDM
            pDH_l = (DH_over_rd(z, bf_l["H0"], E_lcdm, bf_l["r_d"],
                                bf_l["omega_m"]) - DHv)/sDH
            labels_bar.extend([f"{lab}\nDM z={z}", f"{lab}\nDH z={z}"])
            res_ebc.extend([pDM_e, pDH_e])
            res_lcdm.extend([pDM_l, pDH_l])
        xpos = np.arange(len(labels_bar))
        w = 0.4
        ax_res.bar(xpos - w/2, res_ebc, w, color=COLORS[0],
                   label=best_ebc_label)
        ax_res.bar(xpos + w/2, res_lcdm, w, color="gray", label="LCDM")
        ax_res.axhline(0, color="k", lw=0.5)
        ax_res.axhline(2, color="r", ls=":", lw=0.7)
        ax_res.axhline(-2, color="r", ls=":", lw=0.7)
        ax_res.set_xticks(xpos)
        ax_res.set_xticklabels(labels_bar, fontsize=6.5, rotation=45,
                               ha="right")
        ax_res.set_ylabel("(Pred - Obs) / sigma")
        ax_res.set_title("Residuen (selbstkonsistent)")
        ax_res.legend(fontsize=9)
        ax_res.grid(alpha=0.25, axis="y")

        labs = ["EBC x0=0.06", "EBC x0=0.10", "EBC x0=0.15", "LCDM"]
        H0_fit2 = [fit2_ref[l]["H0"] for l in labs]
        H0_fit3 = [best_fits[l]["H0"] for l in labs]
        rd_fit3 = [best_fits[l]["r_d"] for l in labs]
        xp = np.arange(len(labs))
        w = 0.38
        ax_cmp.bar(xp - w/2, H0_fit2, w, color="steelblue",
                   label="fit2 (r_d=147.09 fest)")
        ax_cmp.bar(xp + w/2, H0_fit3, w, color="darkorange",
                   label="fit3 (r_d via Aubourg)")
        for i, rd in enumerate(rd_fit3):
            ax_cmp.text(xp[i] + w/2, H0_fit3[i] + 0.3,
                        f"r_d={rd:.1f}", fontsize=7, ha="center")
        ax_cmp.axhline(73.0, color="red", ls=":", lw=1,
                       label="SH0ES H0 ~ 73")
        ax_cmp.axhline(67.4, color="green", ls=":", lw=1,
                       label="Planck H0 ~ 67.4")
        ax_cmp.set_xticks(xp)
        ax_cmp.set_xticklabels(labs, fontsize=8, rotation=15)
        ax_cmp.set_ylabel("H0 [km/s/Mpc]")
        ax_cmp.set_title("H0-Verschiebung durch Selbstkonsistenz")
        ax_cmp.legend(fontsize=8)
        ax_cmp.grid(alpha=0.25, axis="y")
        ax_cmp.set_ylim(55, 80)

        fig.suptitle(
            "EBC -- 3-Parameter-Fit (self-consistent r_d) vs. fit2 (fixed r_d)\n"
            f"DESI Y1 BAO, Omega_b h^2 = {OMEGA_B_H2_BBN} (BBN/Planck), "
            "mit DM/DH-Kovarianzen",
            fontsize=11, y=1.00
        )

        out = "/home/claude/ebc_bao_fit3.png"
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print(f"\nPlot gespeichert: {out}")
    except Exception as e:
        print(f"\n(Plot fehlgeschlagen: {e})")
        import traceback; traceback.print_exc()


if __name__ == "__main__":
    main()
