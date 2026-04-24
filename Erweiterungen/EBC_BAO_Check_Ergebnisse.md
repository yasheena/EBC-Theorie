---
title: "EBC BAO-Geometrie-Check — Ergebnisse"
status: neu
tags: [EBC, BAO, DESI, Numerik, Ergebnisse]
aktualisiert: 2026-04-24
---

# EBC — Selbstkonsistenter BAO-Geometrie-Check

**Daten:** DESI DR1, arXiv:2404.03002, Tabelle 1  
**Methode:** $\chi^2$-Minimierung mit $H_0$ als einzigem freien Parameter  
**Skript:** `Numerik/ebc_bao_fit.py`

---

## Schritt 1: Gültigkeit der $r_d$-Annahme ✓

Der EBC-Term $\Omega_{DE}(1/x - x/x_*^2)$ bei $z = 1100$ beträgt:

| Größe | Wert |
|-------|------|
| $\Omega_m/x^3$ (Materie) | $4.20 \times 10^8$ |
| $\Omega_r/x^4$ (Strahlung) | $1.35 \times 10^8$ |
| EBC-Term (netto) | $\approx 7.6 \times 10^2$ |
| **EBC-Anteil** | **< 0.0002 %** |

**Schlussfolgerung:** Der Schallhorizont $r_d = 147{,}09$ Mpc (Planck 2018)
kann unverändert übernommen werden. Die Vorrekombinations-Physik ist in EBC
identisch mit $\Lambda$CDM.

---

## Schritt 2: DESI DR1 BAO-Datenpunkte

Aus Tabelle 1 (arXiv:2404.03002):

| Tracer | $z_\mathrm{eff}$ | $D_M/r_d$ | $\sigma_{D_M}$ | $D_H/r_d$ | $\sigma_{D_H}$ | $r$ |
|--------|-----:|------:|-----:|------:|-----:|------:|
| BGS | 0.295 | — | — | — | — | (DV) |
| LRG1 | 0.510 | 13.62 | 0.25 | 20.98 | 0.61 | −0.445 |
| LRG2 | 0.706 | 16.85 | 0.32 | 20.08 | 0.60 | −0.420 |
| LRG3+ELG1 | 0.930 | 21.71 | 0.28 | 17.88 | 0.35 | −0.389 |
| ELG2 | 1.317 | 27.79 | 0.69 | 13.82 | 0.42 | −0.444 |
| QSO | 1.491 | — | — | — | — | (DV) |
| Lyα | 2.330 | 39.71 | 0.94 | 8.52 | 0.17 | −0.477 |

Isotropisch ($D_V/r_d$): BGS $= 7{,}93 \pm 0{,}15$ (z=0.295),
QSO $= 26{,}07 \pm 0{,}67$ (z=1.491).

---

## Schritte 3+4: Fit-Ergebnisse

**Analytische Minimierung** (alle Observablen $\propto 1/H_0$):

$$\chi^2(u) = u^2 S_{AA} - 2u\, S_{OA} + S_{OO}, \quad u = 1/H_0$$

$$\Rightarrow \quad H_0^\mathrm{opt} = \frac{S_{AA}}{S_{OA}}$$

| Modell | $x_0$ | $H_0$ [km/s/Mpc] | $\sigma_{H_0}$ | $\chi^2$ | $\chi^2/\mathrm{dof}$ | $H_0 t_0$ | $t_0$ [Gyr] | $\Delta t_0$ |
|--------|------:|------:|-----:|-----:|-----:|-----:|-----:|-----:|
| EBC | 0.06 | **63.37** | 0.30 | 22.44 | 2.040 | 0.893 | 13.79 | −6.1 % |
| EBC | 0.10 | **63.32** | 0.30 | 22.52 | 2.047 | 0.893 | 13.79 | −6.1 % |
| EBC | 0.15 | **63.24** | 0.30 | 22.68 | 2.061 | 0.891 | 13.79 | −6.2 % |
| ΛCDM | ∞ | **68.17** | 0.32 | 14.69 | 1.335 | 0.951 | 13.64 | Ref. |

**Freiheitsgrade:** 12 Datenpunkte (5×2 + 2) − 1 freier Parameter = 11

---

## Schritt 5: Residuen-Analyse (bestes EBC-Modell, $x_0 = 0{,}06$)

| Tracer | $z$ | $\Delta D_M/\sigma$ | $\Delta D_H/\sigma$ |
|--------|----:|----:|----:|
| LRG1 | 0.510 | **−0.12** | **+1.81** |
| LRG2 | 0.706 | **+2.50** | **−1.06** |
| LRG3+ELG1 | 0.930 | **+0.04** | **−2.59** |
| ELG2 | 1.317 | **−0.25** | **−0.29** |
| Lyα | 2.330 | **−1.17** | **+0.57** |
| BGS (DV) | 0.295 | — | **+1.52** |
| QSO (DV) | 1.491 | — | **−0.75** |

---

## Interpretation

### Was gut funktioniert

1. **$r_d$-Annahme bestätigt.** Der EBC-Term ist bei $z = 1100$ absolut
   vernachlässigbar ($< 0{,}0002\,\%$). EBC macht identische
   Frühuniversum-Physik wie $\Lambda$CDM — $r_d$ ist modellunabhängig.

2. **$t_0$-Spannung **aufgelöst** (fast vollständig).**  
   Bei $H_0^\mathrm{EBC} = 63{,}4$ km/s/Mpc liefert das EBC-Altersintegral
   $t_0 = 13{,}8$ Gyr — innerhalb der beobachteten Schranken
   ($t_0 > 13{,}5$ Gyr aus globularen Sternhaufen).  
   Der früher berechnete Wert $t_0 \approx 12{,}95$ Gyr war auf die
   Verwendung des ΛCDM-Referenzwerts $H_0 = 67{,}4$ km/s/Mpc zurückzuführen.
   Mit dem selbstkonsistenten EBC-$H_0$ verschwindet die Spannung weitgehend.

3. **$H_0$-Vorhersage stabil.** EBC bevorzugt $H_0 \approx 63{,}3$–63{,}4$ km/s/Mpc
   nahezu unabhängig von $x_0$ (Variation < 0{,}2 km/s/Mpc über den
   gesamten $x_0$-Bereich). Das Modell hat daher in diesem Sinne eine
   **parameterfreie $H_0$-Vorhersage** — sobald die $\Omega$-Parameter
   festgelegt sind.

### Wo EBC schlechter ist als ΛCDM

1. **$\chi^2/\mathrm{dof} \approx 2{,}04$ vs. $1{,}34$ (ΛCDM).**  
   EBC passt die BAO-Geometrie statistisch signifikant schlechter an.
   Die Gesamtspannung beträgt $\sim 2{,}7\,\sigma$ gegenüber ΛCDM
   (aus $\Delta\chi^2 \approx 7{,}8$ bei 0 zusätzlichen freien Parametern).

2. **Systematische Abweichungen bei mittleren Rotverschiebungen.**  
   Die größten Residuen treten bei $z = 0{,}706$ ($\Delta D_M/\sigma = +2{,}50$)
   und $z = 0{,}930$ ($\Delta D_H/\sigma = -2{,}59$) auf.
   Dies ist physikalisch verständlich: Im Übergangsbereich zwischen
   Materie- und EBC-Dominanz ($x \approx 0{,}5$–$1{,}0$, d.h. $z \approx 0{,}3$–$1{,}0$)
   weicht $H_\mathrm{EBC}(z)$ am stärksten von $H_\Lambda(z)$ ab.

3. **$H_0$-Diskrepanz: EBC vs. Planck.**  
   Der BAO-bevorzugte EBC-Wert $H_0 \approx 63{,}4$ km/s/Mpc liegt
   $\sim 4{,}8$ km/s/Mpc unter dem Planck-ΛCDM-Wert (67,4) und
   $\sim 4{,}8$ km/s/Mpc unter dem BAO+BBN-Wert (68,5). Dies bedeutet,
   dass EBC die Hubble-Spannung **nicht mildern** kann (es verschiebt sie
   in die entgegengesetzte Richtung).

### Einschränkungen des Checks

Dieser Check verwendet ΛCDM-abgeleitete $\Omega_m = 0{,}315$, $\Omega_r$ und
$r_d$. Ein vollständig selbstkonsistenter Fit würde $\Omega_m$ (und ggf. $r_d$)
im EBC-Rahmen mitfitten und könnte die Residuen verändern. Dies ist jedoch
ein eigenständiges Forschungsprojekt (CMB-Fit im EBC-Rahmen).

---

## Paper-Text: Section 8 Item 3a (Entwurf)

> **[Item 3a] BAO geometry check — numerical result.**
>
> Fitting $H_\mathrm{EBC}(z)$ [Eq.~EBC1] to the seven DESI DR1 BAO
> measurements (arXiv:2404.03002, Table~1; 12 data points) with $H_0$
> as the sole free parameter, we find:
>
> $$H_0^\mathrm{EBC} = 63.4 \pm 0.3~\mathrm{km/s/Mpc}, \quad
> \chi^2/\mathrm{dof} = 2.04$$
>
> compared to the ΛCDM reference fit $H_0^\Lambda = 68.2 \pm 0.3$ km/s/Mpc
> ($\chi^2/\mathrm{dof} = 1.33$). At the EBC-preferred $H_0$, the
> cosmic age evaluates to $t_0^\mathrm{EBC} = 13.8$ Gyr
> ($H_0 t_0 = 0.893$), consistent with observational lower bounds from
> globular clusters. The residual tension with the ΛCDM age at the same
> $H_0$ is $-6\%$ (upper bound, since $\Omega_m$ was held fixed at
> the Planck 2018 value rather than self-consistently fitted within EBC).
>
> The main discrepancy arises at $z \approx 0.7$–$0.9$ (LRG2 and
> LRG3+ELG1 bins), precisely the redshift range where the EBC-to-matter
> transition changes $H_\mathrm{EBC}(z)$ most strongly relative to
> $\Lambda$CDM. Resolving this tension requires a self-consistent EBC
> fit of $\Omega_m$ and $r_d$ against CMB+BAO data, which is identified
> as the primary development priority.

---

## Nächste Schritte

1. **Ω_m freigeben:** Zweiten freien Parameter hinzufügen und
   $(\Omega_m, H_0)$ gemeinsam fitten → erwartete Reduktion von $\chi^2$.
2. **Planck-$r_d$ vs. EBC-$r_d$:** Falls $\Omega_m$ signifikant
   von 0.295–0.315 abweicht, ändert sich auch $r_d$ (über die
   Fitting-Formel Gl. 2.5 in DESI VI).
3. **Plot in v3-Abbildung aufnehmen** (als Figure~2 oder ergänzende Abbildung).
4. **Session-Kontext aktualisieren** (Abschnitt 8, Item 3a → erledigt).
