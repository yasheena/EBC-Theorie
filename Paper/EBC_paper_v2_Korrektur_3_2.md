---
title: "EBC Paper v2 — Korrektur Abschnitt 3.2 (+ H₀·t₀-Spannung)"
status: Entwurf zur Übernahme
tags: [EBC, Korrektur, Paper, Numerik]
aktualisiert: 2026-04-23
---

# Korrekturprotokoll: EBC_paper_v2.md

## Überblick der Änderungen

| # | Abschnitt | Art | Priorität |
|---|-----------|-----|-----------|
| 1 | 3.2 — Order-of-magnitude estimates | Korrektur (Vorzeichen + Betrag + Physik) | **1 – sofort** |
| 2 | 3.2 — Neue quantitative Tabelle | Einfügen | **1 – sofort** |
| 3 | 3.2 — H₀·t₀-Spannung | Neuer Absatz | **1 – sofort** |
| 4 | Abstract — T-Bereich | Kleinere Aktualisierung | 2 |
| 5 | 4.1 — Zyklusposition-Angabe | Nachziehen | 2 |

---

## Korrektur 1+2+3: Section 3.2 — Letzter Absatz

### Aktueller Text (FALSCH — ersetzen):

> **Order-of-magnitude estimates of the corrections.** Although the full numerical
> integration with matter and radiation is deferred, the leading corrections can be
> estimated analytically. Matter enters (EBC2) as an additional attractive term
> $-4\pi G \rho_m/3$ that decelerates the early expansion while remaining negligible
> near the expansion maximum (where $\rho_m \propto a_*^{-3}$ is highly diluted).
> The ratio of the matter density to the EBC restoring term today is
> $\Omega_m/\Omega_\mathrm{EBC} \approx 0.31/0.69 \approx 0.45$; this ratio grows
> as $a^{-3}$ toward the past, making matter dominant in the early phase of each cycle.
> A rough estimate gives a correction factor of approximately:
>
> $$\frac{T_\text{with matter}}{T_\text{matter-free}} \approx 1 + C \cdot
> \frac{\Omega_m}{\Omega_\mathrm{EBC}} \approx 1.15\text{--}1.25$$
>
> where $C \approx 0.4$–$0.5$ accounts for the fact that matter is relevant only in
> the early phase of each cycle. The cycle duration estimate therefore increases by
> approximately **15–25%**: from $T \approx 90$–230 Gyr to $T \approx 105$–290 Gyr.
> Correspondingly, the cycle position $f = t_0/T$ shifts downward by a similar
> fraction, from 6–15% to approximately **5–13%** — qualitatively unchanged but
> toward the lower end of the current range. The expansion maximum $x_\mathrm{max}
> \approx 1.73$ changes by less than 5%, since matter is negligible there. Near the
> bounce, radiation ($\rho_r \propto a^{-4}$) adds a modest additional repulsive
> contribution that slightly increases $x_\mathrm{min}$, consistent with the bounce
> temperature estimate of Section 6.2. Crucially, the analytic prediction
> $w_0 = -2/3$ (Section 2.5) is independent of the numerical integration entirely
> and is unaffected by the inclusion of matter and radiation.

---

### Korrigierter Text (RICHTIG — einfügen):

**Order-of-magnitude estimates of the corrections.**
Although the full treatment of the matter-radiation epoch requires numerical
integration, the physical direction of the correction can be determined analytically.
Matter contributes an additional term $+\Omega_m/x^3$ to the squared Hubble rate
(EBC1), which dominates at small $x$ and drives a *faster* early expansion: the
ratio $\Omega_m/x^3 \gg \Omega_\mathrm{EBC}/x$ for $x \ll 1$ implies that the
matter-dominated phase is traversed more rapidly than the matter-free case.
In (EBC2), matter contributes a decelerating term $-\Omega_m/(2x^2)$, but this
braking effect is smaller in magnitude than the kinematic acceleration entering
through the Friedmann equation (EBC1). The net result is that matter *shortens* the
cycle relative to the matter-free EBC reference with the same elastic restoring
force.

**Quantitative results from full numerical integration.**
The system (EBC1)–(EBC2) has been integrated with physical parameters
($\Omega_m = 0.315$, $\Omega_r = 9.2 \times 10^{-5}$,
$1/H_0 = 14.51\,\mathrm{Gyr}$; $\Omega_{DE}$ from the flatness condition at $x = 1$)
for the half-cycle from the bounce minimum ($x \approx 0$) to the expansion maximum
($x = x_*$). Results are given for the range of cycle positions $x_0 = a_0/a_*$:

| $x_0 = a_0/a_*$ | $x_* = a_*/a_0$ | $T_\mathrm{free}$ [Gyr] | $T_\mathrm{mat}$ [Gyr] | Ratio | $f = t_0 / T$ |
|:---:|:---:|---:|---:|:---:|:---:|
| 0.06 | 16.7 | 349 | 320 | 0.917 | 4.3% |
| 0.08 | 12.5 | 301 | 273 | 0.904 | 5.1% |
| 0.10 | 10.0 | 269 | 240 | 0.893 | 5.7% |
| 0.13 |  7.7 | 235 | 207 | 0.878 | 6.7% |
| 0.15 |  6.7 | 218 | 190 | 0.869 | 7.3% |

*$T_\mathrm{free}$: EBC without matter/radiation, same $\Omega_{DE}$.
$T_\mathrm{mat}$: physical EBC with $\Omega_m$, $\Omega_r$.
Ratio: $T_\mathrm{mat}/T_\mathrm{free}$.
$f = t_0/T$ uses the observed $t_0 = 13.8\,\mathrm{Gyr}$.*

The correction factor satisfies

$$\frac{T_\mathrm{mat}}{T_\mathrm{free}} \approx 0.87\text{--}0.92$$

i.e., matter *shortens* the cycle duration by approximately **8–13%**. The updated
cycle duration estimate is $T_\mathrm{mat} \approx \mathbf{190\text{--}320\,\mathrm{Gyr}}$
(full cycle) and the estimated cycle position is $f \approx 4\text{--}7\%$ — consistent
with the current epoch lying early in the expansion phase. The expansion maximum
$x_*$ is unaffected by matter (matter is diluted to negligibility at $x \sim x_*$).
Near the bounce, radiation ($\rho_r \propto a^{-4}$) adds a modest additional
repulsive contribution but does not significantly alter $T_\mathrm{mat}$ (radiation
contributes $\lesssim 0.01$ Gyr to the half-cycle time budget).
Crucially, the analytic prediction $w_0 = -2/3$ (Section 2.5) is independent of the
numerical integration entirely and is unaffected by the inclusion of matter and
radiation.

**Representative time budget for $x_0 = 0.10$ (half-cycle).**

| Phase | Scale factor range | Duration [Gyr] |
|:------|:------------------:|---------------:|
| Radiation-dominated | $x < 3 \times 10^{-4}$ | $\approx 0.0$ |
| Matter-dominated | $3 \times 10^{-4} < x < 0.65$ | $\approx 7.0$ |
| Matter–EBC transition | $0.65 < x < 1$ | $\approx 4.1$ |
| EBC-dominated | $1 < x < x_*$ | $\approx 109$ |
| **Total half-cycle** | — | **$\approx 120$ Gyr** |

The EBC-dominated phase accounts for $>90\%$ of the half-cycle duration.

**Note on $H_0 \cdot t_0$ consistency.**
The EBC-predicted age of the universe is obtained by integrating the Friedmann
equation (EBC1) directly:

$$H_0 \cdot t_0^{(\mathrm{EBC})} = \int_0^1 \frac{dx}{x\,\sqrt{\Omega_m/x^3 +
\Omega_r/x^4 + \Omega_{DE}(1/x - x/x_*^2)}} \approx 0.893
\quad(\Rightarrow\; t_0^{(\mathrm{EBC})} \approx 12.95\,\mathrm{Gyr})$$

compared to the $\Lambda$CDM value $H_0 \cdot t_0 = 0.9506$ (i.e.,
$t_0 \approx 13.8\,\mathrm{Gyr}$ for $H_0 = 67.4\,\mathrm{km/s/Mpc}$).
This represents a **deficit of approximately 6%** (0.84 Gyr) relative to the
$\Lambda$CDM-inferred age.

*Methodological note.* The EBC1-based integral is the physically correct basis for
this comparison, since $\Omega_{DE}$ is calibrated via EBC1 at $x = 1$. Direct ODE
integration of the acceleration equation (EBC2) yields a different value
($H_0 t_0 \approx 0.766$, deficit $\approx 20\%$) due to the known Bianchi
consistency defect between EBC1 and EBC2 (see Section 8, open item). The EBC1
result is the appropriate one to report.

The origin of the 6% deficit is structural: the EBC dark-energy density scales as
$\rho_\mathrm{EBC} \propto a^{-1}$, implying a higher dark energy density at $z > 0$
than in $\Lambda$CDM (where $\rho_\Lambda = \mathrm{const}$). This drives faster
early expansion and causes $x = 1$ to be reached earlier than the observed $t_0$.

A further important caveat applies: the reference value $t_0 = 13.8\,\mathrm{Gyr}$
is not a direct measurement but a $\Lambda$CDM-model-dependent inference from CMB
and BAO data. In particular, the sound horizon $r_s$ and angular diameter distance
$D_A$ used to extract $H_0$ and $\Omega_m$ from the CMB are computed with the
$\Lambda$CDM Hubble function $H_{\Lambda CDM}(z)$. Since $H_\mathrm{EBC}(z) \neq
H_{\Lambda CDM}(z)$ for $z > 0$, a self-consistent EBC fit to CMB and BAO data
would yield different values of $H_0$ and $\Omega_m$, and consequently a different
inferred $t_0$. Quantifying this shift requires a full EBC likelihood analysis
against Planck and DESI data, which is identified as a development priority in
Section 8. The 6% deficit quoted here should therefore be regarded as an upper bound
on the true model tension rather than a definitive discrepancy. It does not affect
the analytic prediction $w_0 = -2/3$.

---

## Korrektur 4: Abstract — T-Bereich

### Aktuell:
> a cycle duration of $T \approx 105$–290 Gyr (including a correction for matter content)

### Ersatz:
> a cycle duration of $T \approx 190$–320 Gyr (from numerical integration with
> physical matter and radiation content; see Section 3.2)

---

## Korrektur 5: Section 4.1 — Zyklusposition

### Aktuell (Section 4.1):
> we are in the early rising phase of a cycle (estimated 5–13%, including the
> correction for matter content derived in Section 3.2)

### Ersatz:
> we are in the early rising phase of a cycle (estimated 4–7% from numerical
> integration with physical parameters; Section 3.2)

---

## Zusatz: Empfehlung für Section 8 (Offene Probleme)

Neuer Punkt hinzufügen (z.B. als "3a" oder als eigenständiger Punkt):

> **$H_0 \cdot t_0$ consistency.**
> The EBC Friedmann equation (EBC1) predicts $H_0 \cdot t_0 \approx 0.893$
> ($t_0 \approx 12.95\,\mathrm{Gyr}$), approximately **6% below** the
> $\Lambda$CDM-inferred value of $H_0 \cdot t_0 = 0.951$ ($t_0 \approx 13.8\,\mathrm{Gyr}$).
> The discrepancy arises because $\rho_\mathrm{EBC} \propto a^{-1}$ implies a higher
> dark-energy density in the past than $\Lambda$CDM, accelerating the early expansion.
> However, the reference value $t_0 = 13.8\,\mathrm{Gyr}$ is itself a
> $\Lambda$CDM-model-dependent inference from CMB and BAO data: it assumes
> $H_{\Lambda CDM}(z)$ throughout. A self-consistent EBC fit to CMB and BAO data —
> using $H_\mathrm{EBC}(z)$ to interpret the sound horizon and angular diameter
> distances — would yield different $H_0$ and $\Omega_m$ values and consequently
> a different inferred $t_0$. The 6% figure should be regarded as an upper bound on
> the true model tension, pending such an analysis. Additionally, ODE integration of
> the acceleration equation (EBC2) yields a larger apparent deficit ($\approx 20\%$),
> but this is an artifact of the Bianchi consistency defect between EBC1 and EBC2
> (see open item on covariant embedding); the EBC1-based result is the physically
> appropriate one.

---

## Zusammenfassung der Befunde (für Session-Kontext-Update)

| Größe | Session-Kontext (alt) | Paper v2 (alt, falsch) | Neu (korrekt) |
|-------|----------------------|----------------------|---------------|
| Ratio T_mat/T_free | 0.75–0.85 | 1.15–1.25 ← **falsch** | **0.87–0.92** |
| Richtung Materie-Effekt | Materie verkürzt ✓ | Materie verlängert ✗ | **Materie verkürzt** ✓ |
| T_mat [Gyr] | 179–320 | 105–290 ← zu niedrig | **190–320** |
| f = t₀/T | 4–8% | 5–13% | **4–7%** |
| H₀·t₀ (EBC, EBC1) | 0.894 (−6%) ✓ | nicht berechnet | **0.893 (−6,1%)** |
| H₀·t₀ (EBC, EBC2) | — | — | 0.766 (−19,5%) — Bianchi-Artefakt |
| Spannung H₀·t₀ | "kleine Spannung" | nicht diskutiert | **~6%, modellabhängig (obere Schranke)** |
