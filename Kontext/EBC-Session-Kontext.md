---
title: EBC Session-Kontext
status: aktuell
tags: [EBC, Kontext, Session]
aktualisiert: 2026-04-22
---

# EBC Session-Kontext — Übergabedokument

Dieses Dokument fasst den gesamten bisherigen Stand der EBC-Arbeit zusammen
und dient als Einstieg für neue Chat-Sessions.

---

## 1. Wer bin ich?

Wolfgang Mattis, Leipzig. Hintergrund: Elektrotechnik / Softwareentwicklung,
~25 Jahre interdisziplinäre Selbststudien (Physik, Kosmologie).
ORCID: 0009-0006-9810-7819 | ebc@wm0.eu

---

## 2. Was ist EBC?

**Elastic Bounce Cosmology (EBC)** — ein zyklisches Kosmologiemodell, das
den Urknall als elastischen Rückprall einer vorherigen Kontraktionsphase
beschreibt. Kernmerkmale:

- Erweiterung der Friedmann-Gleichungen um einen elastischen Term Λ_EBC(a) ∝ 1/a
  und einen Dämpfungsterm γ(a)·H
- **Parameterfreie Vorhersage: w₀ = −2/3** (Zustandsgleichung der Dunklen Energie)
- Konsistent mit DESI 2024: w₀ = −0.70 ± 0.10 (1σ)
- Singularität wird vermieden: elastischer Term wird bei Kompression repulsiv

**Publikation:** DOI: https://doi.org/10.5281/zenodo.19399593, Zenodo-Record: https://zenodo.org/records/19399593, Paper: EBC_paper_v2.md / EBC_paper_v2_DE.md
Dort auch: englische Originalversion + deutsche Übersetzung als separates File.

---

## 3. Kerngleichungen

In dimensionslosen H₀-Einheiten (x = a/a₀, τ = H₀·t):

**EBC1 (Friedmann):**
$$\left(\frac{\dot{x}}{x}\right)^2 = \frac{\Omega_m}{x^3} + \frac{\Omega_r}{x^4} + \Omega_{DE}\left(\frac{1}{x} - \frac{x}{x_*^2}\right)$$

**EBC2 (Beschleunigung):**
$$\ddot{x} = \Omega_{DE}(1 - x^2/x_*^2) - \frac{\Omega_m}{2x^2} - \frac{\Omega_r}{x^3} - \gamma_\mathrm{eff}\,|x/x_* - 1|\,\dot{x}$$

Dabei: x₀ = a₀/a* = aktueller Skalenfaktor / Expansionsmaximum ≈ 0.06–0.15

**Zustandsgleichung (analytisch exakt):**
$$w_0 = -\frac{2}{3}$$
(aus Kontinuitätsgleichung: Λ_EBC ∝ 1/a → ρ ∝ a^{−1} → w = −1 − (−1)/3 = −2/3)

---

## 4. Bisherige numerische Ergebnisse

### 4a. Paper-Illustration (dimensionslose Einheiten, ohne Materie)
- Bounce-Minimum bei x_bounce ≈ 0.515 (illustrativ, nicht physikalisch)
- x_max ≈ 1.73, Zyklusdauer ΔΤ ≈ 4.87 (dimensionslos)
- K = 0.527, K_b = 0.005, γ̃ = 1.5×10⁻³

### 4b. Physikalische Integration (H₀-Einheiten, mit Materie/Strahlung)
Verwendete Werte: Ω_m = 0.315, Ω_r = 9.2×10⁻⁵, Ω_DE = 0.6849, 1/H₀ = 14.51 Gyr

| x₀   | x*   | T_free [Gyr] | T_Materie [Gyr] | Ratio | f = t₀/T |
|------|------|-------------|----------------|-------|-----------|
| 0.06 | 16.7 | 375         | 320            | 0.854 | 4.3%      |
| 0.08 | 12.5 | 325         | 269            | 0.829 | 5.1%      |
| 0.10 | 10.0 | 291         | 234            | 0.805 | 5.9%      |
| 0.13 |  7.7 | 255         | 197            | 0.774 | 7.0%      |
| 0.15 |  6.7 | 237         | 179            | 0.754 | 7.7%      |

**Zeitbudget für x₀ = 0.10 (Halbzyklus):**
- Strahlungsdominiert (x < 3×10⁻⁴): ~0 Gyr (vernachlässigbar)
- Materiedominiert (3×10⁻⁴ < x < 0.65): 7.76 Gyr
- Materie-EBC-Übergang (0.65 < x < 1): 5.21 Gyr
- EBC-dominiert (1 < x < x*): 103.96 Gyr
- Gesamt Halbzyklus: ~117 Gyr → T ≈ 234 Gyr

**H₀·t₀-Konsistenz:**
- Standard-ΛCDM: H₀·t₀ = 0.9506 ✓
- EBC (alle x₀): H₀·t₀ ≈ 0.894 (ca. −6% gegenüber ΛCDM)
→ kleine Spannung, Paper-relevant

---

## 5. Wichtige Korrektur gegenüber Paper-Abschnitt 3.2

Das Paper behauptet (Abschnitt 3.2, Formel):
> T_mit_Materie / T_materefrei ≈ 1.15–1.25 (Materie *verlängert* Zyklus um 15–25%)

**Die physikalische Integration zeigt das Gegenteil:**
Ratio ≈ 0.75–0.85 → Materie *verkürzt* den Zyklus um 15–25%.

**Physikalische Erklärung:** Im frühen Universum (x ≪ 1) dominiert Ω_m/x³
die Hubble-Rate. Das bedeutet schnellere Expansion, schnellere Durchquerung
der Frühphase → kürzerer Gesamtzyklus. Der EBC₂-Bremseffekt ist kleiner
als der EBC₁-Beschleunigungseffekt durch Materie bei kleinen x.

**→ Paper muss in Abschnitt 3.2 korrigiert werden (Priorität 1).**

---

## 6. Bianchi-Defektterm (theoretisches Problem)

Aus der Herleitung (Chat 5329e5ce): Differenziert man EBC1 und vergleicht
mit EBC2, ergibt sich kein konsistentes ∇_μ T^μν = 0. Der Defektterm:

$$\dot{\rho} + 3H(\rho+p) = \underbrace{-\frac{\dot{\Lambda}_{EBC} + \dot{\Lambda}_b}{8\pi G}}_{D_\Lambda} \underbrace{-\frac{3\gamma(a)H^2}{4\pi G}}_{D_\gamma}$$

- **D_Λ**: lösbar — analog Quintessenz (effektives Skalarfeld)
- **D_γ**: offen — kein Standardmechanismus für Energiefluss in Raumzeit
  (berührt thermodynamische Gravitation: Jacobson, Verlinde)

Diese Frage wurde an Prof. Brandenberger (McGill) und Prof. Steinhardt
(Princeton) gesendet. Bislang keine Antwort.

---

## 7. Outreach-Status

| Kanal                   | Status                            |
|-------------------------|-----------------------------------|
| Zenodo (EN)             | ✅ veröffentlicht                 |
| Zenodo (DE)             | ✅ hinzugefügt                    |
| Physikerboard.de        | ⚠️ gepostet, als "offtopic" markiert |
| Prof. Brandenberger     | 📤 gesendet, keine Antwort        |
| Prof. Steinhardt        | 📤 gesendet, keine Antwort        |
| Reddit r/cosmology      | 🔲 geplant                        |
| YouTube "Breaking Lab"  | 🔲 bei passendem Video            |

---

## 8. Offene Punkte / nächste Schritte

**Sofort (Paper-Korrekturen):**
1. Abschnitt 3.2 korrigieren: Ratio 0.75–0.85 statt 1.15–1.25
2. Quantitative Tabelle (Abschnitt 4b) ins Paper einfügen
3. H₀·t₀-Spannung (~6%) als Diskussionspunkt ergänzen
4. Offener Punkt 3 in Section 8 als erledigt markieren

**Mittelfristig:**
5. ebc_physical.py neu erstellen und validieren (Session-Absturz)
6. Abbildung aus physikalischer Integration als neue Figure ins Paper
7. Reddit-Post verfassen
8. Bianchi-Defektterm: theoretische Ausarbeitung

**Langfristig:**
9. Schwarze-Loch-Erweiterung (τ_ext-Paper)
10. Verknüpfung EBC ↔ Buch "Perfect Universe" / Gedankenspieler

---

## 9. Dateien im Vault (EBC-Theorie/)

| Datei                          | Ort                    | Status     |
|-------------------------------|------------------------|------------|
| EBC_paper_v2.md               | Paper/                 | ✅ aktuell |
| EBC_paper_v2_DE.md            | Paper/                 | ✅ aktuell |
| ebc_physical.py               | Numerik/               | ⚠️ neu erstellen |
| Session-Kontext.md (diese)    | Kontext/               | ✅ aktuell |
| Offene-Punkte.md              | —                      | 🔲 anlegen |
| Emails.md                     | Outreach/              | 🔲 anlegen |
| Foren.md                      | Outreach/              | 🔲 anlegen |
| Changelog.md                  | Paper/                 | 🔲 später  |

---

## 10. Wie neue Sessions starten

1. Diese Datei + EBC_paper_v2.md + ebc_physical.py hochladen
2. Einstieg: *"Wir setzen EBC-Arbeit fort — Kontext in hochgeladenen Dateien."*
3. Erstes Ziel benennen (z.B. "Paper Abschnitt 3.2 korrigieren")
