#!/usr/bin/env python3
"""
ebc_physical.py — Elastic Bounce Cosmology: Physikalische Integration
======================================================================
Autor : Wolfgang Mattis <ebc@wm0.eu>
Stand : 2026-04-23

Integriert die EBC-Gleichungen in dimensionslosen H₀-Einheiten
(x = a/a₀, τ = H₀·t) mit physikalischen Ω-Werten.

Kerngleichungen
---------------
EBC1 (Friedmann, bestimmt Anfangsbedingungen und Weltalter):
    (ẋ/x)² = Ω_m/x³ + Ω_r/x⁴ + Ω_DE·(1/x − x/x*²)

EBC2 (Bewegungsgleichung, integriert für Zyklusdauer und Ratio):
    ẍ = Ω_DE·(1 − x²/x*²) − Ω_m/(2x²) − Ω_r/x³ − γ_eff·|x/x* − 1|·ẋ

Hier ist x* = a*/a₀ = 1/x₀ (x₀ = heutiger Anteil am Zyklus = a₀/a*).
Ω_DE wird aus der Flachheitsbedingung bei x=1 berechnet:
    Ω_m + Ω_r + Ω_DE·(1 − 1/x*²) = 1

Wichtiger Hinweis zur H₀·t₀-Berechnung
----------------------------------------
EBC1 und EBC2 sind wegen des Bianchi-Defekts (offener Punkt, Section 8)
nicht vollständig konsistent. Für das Weltalter H₀·t₀ ist ausschließlich
das EBC1-Integral maßgeblich (Funktion h0t0_from_ebc1). Der aus dem
EBC2-ODE-Solver abgelesene tau_today-Wert ist ein Bianchi-Artefakt und
wird hier nur zur Diagnose ausgegeben, aber NICHT als H₀·t₀ verwendet.

Gültigkeitsbereiche der Ausgaben:
  - T_half / T_full (Zyklusdauer):  EBC2-basiert, robust (Artefakt kürzt
                                     sich im Verhältnis T_mat/T_free weitgehend heraus)
  - Ratio T_mat/T_free:             EBC2-basiert, zuverlässigste Ausgabe
  - H₀·t₀ / t₀:                    EBC1-basiert (h0t0_from_ebc1), korrekt
  - f = t₀/T:                       gemischt: t₀ aus EBC1, T aus EBC2
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import warnings

# ── Physikalische Konstanten ──────────────────────────────────────────────────

H0_INV_GYR = 14.51      # 1/H₀ in Gyr  (H₀ ≈ 67.4 km/s/Mpc)
T0_GYR     = 13.8       # Weltalter heute [Gyr]
OMEGA_M    = 0.315      # Materiedichte  (Planck 2018)
OMEGA_R    = 9.2e-5     # Strahlungsdichte
OMEGA_DE_LCDM = 1.0 - OMEGA_M - OMEGA_R  # ≈ 0.6849

# Materie/Strahlung-Domäne-Grenzen (zur Zeitbudget-Analyse)
X_RAD_END  = 3e-4       # Ende Strahlungsdominanz  (≈ Äquivalenz)
X_MAT_END  = 0.65       # Ende Materiedominanz (geschätzt aus EBC-Übergang)

# Numerische Parameter
X_INIT     = 1e-5       # Startpunkt der Integration (≪ 1)
RTOL       = 1e-10
ATOL       = 1e-13
MAX_STEP   = 0.05       # max. Schrittweite in τ (H₀-Einheiten)


# ── Hilfsfunktionen ───────────────────────────────────────────────────────────

def omega_de(x_star: float, om: float = OMEGA_M, or_: float = OMEGA_R) -> float:
    """Ω_DE aus Flachheitsbedingung (EBC1 bei x=1, ẋ=1)."""
    return (1.0 - om - or_) / (1.0 - 1.0 / x_star**2)


def v_init_from_ebc1(x: float, x_star: float,
                     om: float, or_: float, ode: float) -> float:
    """Anfangsgeschwindigkeit ẋ aus EBC1 (Hubble-Rate bei x ≪ 1)."""
    h2 = om / x**3 + or_ / x**4 + ode * (1.0/x - x/x_star**2)
    if h2 < 0:
        raise ValueError(f"EBC1 liefert H²<0 bei x={x:.2e} — Parameter inkonsistent.")
    return x * np.sqrt(h2)


def h0t0_from_ebc1(x0_frac: float,
                   om: float = OMEGA_M,
                   or_: float = OMEGA_R) -> float:
    """
    Berechnet H₀·t₀ durch direktes Quadratur-Integral über EBC1.

    Dies ist die physikalisch korrekte Methode für das Weltalter.
    Der ODE-Solver (EBC2) liefert wegen des Bianchi-Defekts einen
    abweichenden Wert — dieser darf NICHT als H₀·t₀ verwendet werden.

    Integral:  H₀·t₀ = ∫₀¹ dx / [x · √(Ω_m/x³ + Ω_r/x⁴ + Ω_DE·(1/x − x/x*²))]

    Parameters
    ----------
    x0_frac : x₀ = a₀/a* (Zyklusposition heute)
    om      : Ω_m
    or_     : Ω_r

    Returns
    -------
    H₀·t₀ (dimensionslos)
    """
    from scipy.integrate import quad
    x_star = 1.0 / x0_frac
    ode = omega_de(x_star, om, or_)

    def integrand(x):
        h2 = om / x**3 + or_ / x**4 + ode * (1.0/x - x/x_star**2)
        if h2 <= 0:
            return 0.0
        return 1.0 / (x * np.sqrt(h2))

    val, _ = quad(integrand, 1e-8, 1.0, limit=200, epsabs=1e-10)
    return val


def ebc2_rhs(tau: float, state: list,
             x_star: float, om: float, or_: float,
             ode: float, gamma_eff: float) -> list:
    """
    Rechte Seite von EBC2 (Bewegungsgleichung).

    Parameters
    ----------
    tau      : dimensionslose Zeit H₀·t
    state    : [x, v] mit v = ẋ = dx/dτ
    x_star   : a*/a₀ (Expansionsmaximum in heutigen Einheiten)
    om       : Ω_m
    or_      : Ω_r
    ode      : Ω_DE (EBC-Dunkelenergie)
    gamma_eff: Dämpfungskoeffizient (≥ 0)

    Returns
    -------
    [dx/dτ, dv/dτ]
    """
    x, v = state
    if x <= 0.0:
        return [v, 0.0]

    elastic   =  ode * (1.0 - (x / x_star)**2)
    matter    = -om  / (2.0 * x**2)
    radiation = -or_ / x**3
    damping   = -gamma_eff * abs(x / x_star - 1.0) * v

    dvdt = elastic + matter + radiation + damping
    return [v, dvdt]


# ── Haupt-Integrationsfunktion ────────────────────────────────────────────────

def integrate_half_cycle(
        x0_frac: float,
        with_matter: bool = True,
        gamma_eff: float  = 0.0,
        x_init: float     = X_INIT,
        verbose: bool     = False,
) -> dict:
    """
    Integriert einen Halbzyklus von x_init bis x* = 1/x0_frac.

    Parameters
    ----------
    x0_frac    : x₀ = a₀/a* (Zyklusposition heute, z.B. 0.10)
    with_matter: True → physikalisch (Ω_m, Ω_r gesetzt)
                 False → materiefreie Referenz (Ω_m = Ω_r = 0)
    gamma_eff  : Dämpfungskoeffizient (Standard: 0 für physikalische Tabelle)
    x_init     : Startpunkt der Integration (sehr kleines x)
    verbose    : Zusätzliche Debug-Ausgabe

    Returns
    -------
    dict mit Schlüsseln:
        x_star, Omega_DE,
        tau_half, tau_today,
        T_half_Gyr, T_full_Gyr, t0_Gyr,
        H0t0,
        time_budget  (dict mit Phasen-Zeiten in Gyr)
        sol          (scipy ODE-Lösung)
    """
    x_star = 1.0 / x0_frac

    om  = OMEGA_M  if with_matter else 0.0
    or_ = OMEGA_R  if with_matter else 0.0
    ode = omega_de(x_star, om, or_)

    # ── Anfangsbedingungen aus EBC1 ──
    v0 = v_init_from_ebc1(x_init, x_star, om, or_, ode)
    state0 = [x_init, v0]

    # ── Ereignisse ──
    # (1) Expansionsmaximum: v = 0 (v nimmt ab)
    def ev_max(tau, s, *args):
        return s[1]
    ev_max.terminal  = True
    ev_max.direction = -1

    # (2) Heute: x = 1 (erste Durchquerung von unten)
    def ev_today(tau, s, *args):
        return s[0] - 1.0
    ev_today.terminal  = False
    ev_today.direction =  1

    # (3) Materie-EBC-Übergang: x = X_MAT_END
    def ev_mat_end(tau, s, *args):
        return s[0] - X_MAT_END
    ev_mat_end.terminal  = False
    ev_mat_end.direction =  1

    # (4) Strahlung-Materie-Übergang: x = X_RAD_END
    def ev_rad_end(tau, s, *args):
        return s[0] - X_RAD_END
    ev_rad_end.terminal  = False
    ev_rad_end.direction =  1

    args = (x_star, om, or_, ode, gamma_eff)

    sol = solve_ivp(
        ebc2_rhs,
        t_span=[0.0, 1e5],
        y0=state0,
        args=args,
        events=[ev_max, ev_today, ev_mat_end, ev_rad_end],
        rtol=RTOL, atol=ATOL,
        dense_output=True,
        max_step=MAX_STEP,
    )

    if not sol.t_events[0].size:
        warnings.warn(f"Kein Expansionsmaximum gefunden (x0={x0_frac})!")
        return None

    tau_half  = sol.t_events[0][0]          # τ beim Expansionsmaximum
    tau_today = (sol.t_events[1][0]
                 if sol.t_events[1].size else None)  # τ bei x=1

    T_half_Gyr = tau_half  * H0_INV_GYR
    T_full_Gyr = 2.0 * T_half_Gyr
    t0_Gyr     = (tau_today * H0_INV_GYR) if tau_today is not None else None
    H0t0       = tau_today if tau_today is not None else None

    # ── Zeitbudget ──
    tau_rad_end = (sol.t_events[3][0]
                   if sol.t_events[3].size else None)
    tau_mat_end = (sol.t_events[2][0]
                   if sol.t_events[2].size else None)

    time_budget = {}
    if with_matter:
        time_budget["Strahlung (x < 3e-4)"] = (
            tau_rad_end * H0_INV_GYR if tau_rad_end else 0.0)
        time_budget["Materie (3e-4 < x < 0.65)"] = (
            (tau_mat_end - tau_rad_end) * H0_INV_GYR
            if (tau_mat_end and tau_rad_end) else None)
        time_budget["Übergang (0.65 < x < 1)"] = (
            (tau_today - tau_mat_end) * H0_INV_GYR
            if (tau_today and tau_mat_end) else None)
        time_budget["EBC-dominiert (1 < x < x*)"] = (
            (tau_half - tau_today) * H0_INV_GYR
            if tau_today else None)

    if verbose:
        print(f"\nx₀ = {x0_frac:.2f}  →  x* = {x_star:.1f}")
        print(f"  Ω_DE = {ode:.5f}")
        print(f"  T_Halbzyklus = {T_half_Gyr:.1f} Gyr")
        print(f"  T_voll       = {T_full_Gyr:.1f} Gyr")
        if t0_Gyr:
            print(f"  t₀           = {t0_Gyr:.2f} Gyr   (H₀·t₀ = {H0t0:.4f})")
        if with_matter:
            print("  Zeitbudget:")
            for k, v in time_budget.items():
                if v is not None:
                    print(f"    {k}: {v:.2f} Gyr")

    return {
        "x0": x0_frac,
        "x_star": x_star,
        "Omega_DE": ode,
        "tau_half": tau_half,
        "tau_today": tau_today,
        "T_half_Gyr": T_half_Gyr,
        "T_full_Gyr": T_full_Gyr,
        "t0_Gyr": t0_Gyr,
        "H0t0": H0t0,
        "time_budget": time_budget,
        "sol": sol,
    }


# ── Haupt-Rechnung & Ausgabe ──────────────────────────────────────────────────

def main():
    import sys

    x0_values = [0.06, 0.08, 0.10, 0.13, 0.15]

    print("=" * 70)
    print("EBC — Physikalische Integration   (ebc_physical.py)")
    print(f"Ω_m = {OMEGA_M},  Ω_r = {OMEGA_R:.1e},  1/H₀ = {H0_INV_GYR} Gyr")
    print("=" * 70)

    # ── Tabelle: T_free vs T_Materie ─────────────────────────────────────────
    print("\n── Halbzyklus-Zeiten [Gyr] ────────────────────────────────────────")
    header = (f"{'x₀':>5}  {'x*':>6}  {'T_free':>10}  "
              f"{'T_Mat':>10}  {'Ratio':>7}  {'f=t₀/T':>8}  {'H₀·t₀':>7}")
    print(header)
    print("-" * len(header))

    results = []
    for x0 in x0_values:
        r_free = integrate_half_cycle(x0, with_matter=False)
        r_mat  = integrate_half_cycle(x0, with_matter=True)
        if r_free is None or r_mat is None:
            print(f"  x₀={x0}: Integration fehlgeschlagen")
            continue

        T_free = r_free["T_full_Gyr"]
        T_mat  = r_mat["T_full_Gyr"]
        ratio  = T_mat / T_free
        f      = r_mat["t0_Gyr"] / T_mat if r_mat["t0_Gyr"] else float("nan")
        H0t0   = r_mat["H0t0"] if r_mat["H0t0"] else float("nan")

        print(f"{x0:>5.2f}  {1/x0:>6.1f}  {T_free:>10.1f}  "
              f"{T_mat:>10.1f}  {ratio:>7.3f}  {f:>7.1%}  {H0t0:>7.4f}")

        results.append({
            "x0": x0, "x_star": 1/x0,
            "T_free": T_free, "T_mat": T_mat,
            "ratio": ratio, "f": f, "H0t0": H0t0,
            "res_mat": r_mat,
        })

    # ── Zeitbudget für x₀ = 0.10 ──────────────────────────────────────────
    print("\n── Zeitbudget für x₀ = 0.10 (Halbzyklus) ─────────────────────────")
    r10 = next((r for r in results if r["x0"] == 0.10), None)
    if r10:
        tb = r10["res_mat"]["time_budget"]
        for phase, t_gyr in tb.items():
            if t_gyr is not None:
                print(f"  {phase:<35}: {t_gyr:>7.2f} Gyr")
        print(f"  {'Gesamt Halbzyklus':<35}: {r10['T_mat']/2:>7.2f} Gyr")
        print(f"  {'Gesamt Vollzyklus':<35}: {r10['T_mat']:>7.2f} Gyr")

    # ── H₀·t₀ (EBC1-Integral — physikalisch korrekt) ──────────────────────
    print("\n── H₀·t₀-Konsistenz (EBC1-Integral) ──────────────────────────────")
    print("   [Maßgeblich für das Weltalter — EBC2-Wert ist Bianchi-Artefakt]")
    H0t0_LCDM = 0.9506
    print(f"  ΛCDM (Referenz):  H₀·t₀ = {H0t0_LCDM:.4f}  "
          f"→ t₀ = {H0t0_LCDM * H0_INV_GYR:.2f} Gyr")
    print()
    for r in results:
        x0 = r["x0"]
        H0t0_ebc1 = h0t0_from_ebc1(x0)
        H0t0_ebc2 = r["H0t0"]   # Bianchi-Artefakt, nur zur Diagnose
        delta_ebc1 = (H0t0_ebc1 - H0t0_LCDM) / H0t0_LCDM * 100
        print(f"  x₀={x0:.2f}:  EBC1 H₀·t₀ = {H0t0_ebc1:.4f}  "
              f"→ t₀ = {H0t0_ebc1 * H0_INV_GYR:.2f} Gyr  "
              f"(Δ = {delta_ebc1:+.1f}%)  "
              f"[EBC2-Artefakt: {H0t0_ebc2:.4f}]")

    # ── Plot (optional) ───────────────────────────────────────────────────
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # --- Plot 1: T_mat und T_free vs x₀ ---
        ax = axes[0]
        x0s     = [r["x0"]    for r in results]
        T_frees = [r["T_free"] for r in results]
        T_mats  = [r["T_mat"]  for r in results]
        ratios  = [r["ratio"]  for r in results]

        ax.plot(x0s, T_frees, "o--", label="$T_\\mathrm{free}$", color="steelblue")
        ax.plot(x0s, T_mats,  "s-",  label="$T_\\mathrm{Materie}$", color="tomato")
        ax.set_xlabel("$x_0 = a_0/a_*$")
        ax.set_ylabel("Zyklusdauer [Gyr]")
        ax.set_title("EBC: Zyklusdauer vs. Zyklusposition")
        ax.legend()
        ax.grid(True, alpha=0.3)

        # --- Plot 2: Ratio T_mat/T_free ---
        ax2 = axes[1]
        ax2.plot(x0s, ratios, "D-", color="darkorange")
        ax2.axhline(1.0, color="gray", linestyle=":", label="kein Effekt")
        ax2.fill_between(x0s, [0.87]*len(x0s), [0.92]*len(x0s),
                         alpha=0.15, color="darkorange", label="Bereich 0.87–0.92")
        ax2.set_xlabel("$x_0 = a_0/a_*$")
        ax2.set_ylabel("$T_\\mathrm{Materie}/T_\\mathrm{free}$")
        ax2.set_title("Korrekturfaktor durch Materieinhalt")
        ax2.set_ylim(0.7, 1.05)
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        out_plot = "/mnt/user-data/outputs/ebc_physical_results.png"
        plt.savefig(out_plot, dpi=150, bbox_inches="tight")
        print(f"\nPlot gespeichert: {out_plot}")

    except ImportError:
        print("\n(matplotlib nicht verfügbar — kein Plot erzeugt)")

    # ── Verbose-Detail für x₀ = 0.10 ─────────────────────────────────────
    print("\n── Verbose-Integration x₀ = 0.10 ─────────────────────────────────")
    integrate_half_cycle(0.10, with_matter=True, verbose=True)
    integrate_half_cycle(0.10, with_matter=False, verbose=True)


if __name__ == "__main__":
    main()
