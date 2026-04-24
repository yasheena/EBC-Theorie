---
title: EBC Session-Kontext
status: aktuell
tags: [EBC, Kontext, Session]
aktualisiert: 2026-04-24
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

**Publikation:** Zenodo, DOI: https://doi.org/10.5281/zenodo.19399593
**Aktueller Arbeitstand:** EBC_paper_v3_draft.md (Korrekturen gegenüber
veröffentlichtem v2 — siehe Abschnitt 7)

---

## 3. Kerngleichungen

In dimensionslosen H₀-Einheiten (x = a/a₀, τ = H₀·t):

**EBC1 (Friedmann, maßgeblich für Weltalter und BAO-Geometrie):**
$$\left(\frac{\dot{x}}{x}\right)^2 = \frac{\Omega_m}{x^3} + \frac{\Omega_r}{x^4} + \Omega_{DE}\left(\frac{1}{x} - \frac{x}{x_*^2}\right)$$

**EBC2 (Bewegungsgleichung, maßgeblich für Zyklusdauer und Ratio):**
$$\ddot{x} = \Omega_{DE}(1 - x^2/x_*^2) - \frac{\Omega_m}{2x^2} - \frac{\Omega_r}{x^3} - \gamma_\mathrm{eff}\,|x/x_* - 1|\,\dot{x}$$

Dabei: x₀ = a₀/a* = aktueller Skalenfaktor / Expansionsmaximum ≈ 0.06–0.15

**Zustandsgleichung (analytisch exakt):**
$$w_0 = -\frac{2}{3}$$
(aus Kontinuitätsgleichung: Λ_EBC ∝ 1/a → ρ ∝ a^{−1} → w = −2/3)

**Ω_DE** aus Flachheitsbedingung bei x = 1:
$$\Omega_{DE} = \frac{1 - \Omega_m - \Omega_r}{1 - 1/x_*^2}$$

---

## 4. Methodische Gültigkeitsprüfung

**Pflichtschritt vor jeder Berechnung:** Prüfen, ob die verwendete Methode
implizit ΛCDM voraussetzt und ob sie im EBC-Rahmen unverändert gültig ist.

### 4a. EBC-Besonderheiten und ihre Auswirkungen auf Berechnungen

| EBC-Merkmal | Betrifft | Konsequenz |
|-------------|----------|------------|
| **Bianchi-Defekt** (EBC1/EBC2-Inkonsistenz) | Weltalter, Zeitintegrale | Altersintegral ausschließlich über EBC1; EBC2-ODE-Wert (H₀·t₀ ≈ 0.766) ist Artefakt |
| **w₀ = −2/3 ≠ −1** (dynamische DE) | H(z), Distanzmaße, χ²-Fits | H_EBC(z) statt H_ΛCDM(z) verwenden |
| **Ω-Werte aus ΛCDM** (Planck 2018) | alle Fits mit freien Parametern | Als Einschränkung dokumentieren |
| **τ_ext** (externer Zeitbezug, P3) | Frühuniversum, CMB, Inflation | Standardmethoden i.d.R. ungültig — offen kennzeichnen |
| **r_d (Schallhorizont)** | BAO-Observablen | Gültig solange EBC-Term bei z ≈ 1100 vernachlässigbar; numerisch bestätigt (< 0.0002%) |
| **r_d Kopplung an Ω_m** | 2-Par-Fit | r_d = r_d(Ω_m, h²) — bei variablem Ω_m ideell mitzufitten; festgehaltenes r_d macht Ergebnisse zur oberen Schranke |
| **Zyklische Geometrie** | Volumenintegrale, Entropie | Standardformeln gelten nur im aktuellen Halbzyklus |
| **Keine Inflation ab Zyklus 2** (P7) | Horizont- und Flachheitsproblem | ΛCDM-Inflationsformeln nicht übertragbar |

### 4b. Bekannte Prüfergebnisse (dokumentiert)

| Berechnung | Methode gültig? | Quelle |
|------------|----------------|--------|
| Altersintegral H₀·t₀ über EBC1 | ✅ Ja | ebc_physical.py |
| Altersintegral über EBC2-ODE | ❌ Nein (Bianchi-Artefakt) | ebc_physical.py |
| Schallhorizont r_d aus Planck 2018 | ✅ Ja (EBC-Term < 0.0002% bei z=1100) | ebc_bao_fit.py |
| BAO-Observablen DM/rd, DH/rd | ✅ Ja, wenn H_EBC(z) verwendet | ebc_bao_fit.py |
| 1-Par-Fit (H₀, Ω_m=0.315 fest) | ✅ Ja (Ω_m als Einschränkung) | ebc_bao_fit.py |
| 2-Par-Fit (H₀, Ω_m frei, r_d fest) | ⚠️ Obere Schranke (r_d-Kopplung ignoriert) | ebc_bao_fit2.py |
| 3-Par-Fit (H₀, Ω_m, r_d selbstkonsistent) | 🔲 Offen — nächster Entwicklungsschritt | — |
| CMB-Anisotropien, Transferfunktion | ❌ Offen (τ_ext, kein EBC-CMB-Modell) | Paper Section 8 |
| Primordialspektrum / Inflation | ❌ Nicht übertragbar (P7) | Paper Section 6 |

### 4c. Handlungsregel

Vor jeder neuen Berechnung:

1. **Welche physikalische Größe wird berechnet?**
2. **Setzt die Standardmethode ΛCDM-H(z), ΛCDM-Inflation oder monotone Expansion voraus?**
3. **Welche EBC-Besonderheiten aus 4a sind betroffen?**
4. **Falls Methode angepasst oder ungültig: explizit im Output kennzeichnen.**

---

## 5. Numerische Ergebnisse (physikalische Integration)

Verwendete Werte: Ω_m = 0.315, Ω_r = 9.2×10⁻⁵, 1/H₀ = 14.51 Gyr

### 5a. Halbzyklus-Zeiten

| x₀   | x*   | T_free [Gyr] | T_mat [Gyr] | Ratio | f = t₀/T |
|------|------|-------------|------------|-------|-----------|
| 0.06 | 16.7 | 349         | 320        | 0.917 | 4.3%      |
| 0.08 | 12.5 | 301         | 273        | 0.904 | 5.1%      |
| 0.10 | 10.0 | 269         | 240        | 0.893 | 5.7%      |
| 0.13 |  7.7 | 235         | 207        | 0.878 | 6.7%      |
| 0.15 |  6.7 | 218         | 190        | 0.869 | 7.3%      |

### 5b. H₀·t₀-Konsistenz

**Maßgebliche Berechnung: EBC1-Integral:**

$$H_0 \cdot t_0^{(EBC)} = \int_0^1 \frac{dx}{x\,\sqrt{\Omega_m/x^3 + \Omega_r/x^4 + \Omega_{DE}(1/x - x/x_*^2)}} \approx 0.893$$

→ Bei H₀ = 67.4 km/s/Mpc: t₀ ≈ 12.95 Gyr (−6.1% vs. ΛCDM-Referenz)
→ Bei H₀ = 63.4 km/s/Mpc (BAO-1-Par-Fit): t₀ ≈ 13.8 Gyr ✓

**Bianchi-Artefakt:** ODE-Solver (EBC2) liefert H₀·t₀ ≈ 0.766 — nicht als Weltalter verwenden.

---

## 6. Korrekturen v2 → v3 (erledigt)

| Stelle | v2 (falsch) | v3 (korrekt) |
|--------|-------------|--------------|
| Section 3.2: Materie-Effekt | verlängert Zyklus +15–25% | verkürzt Zyklus −8–13% |
| Section 3.2: T-Bereich | 105–290 Gyr | 190–320 Gyr |
| Section 3.2: f = t₀/T | 5–13% | 4–7% |
| Section 3.2: H₀·t₀ | nicht vorhanden | 0.893 / −6% (obere Schranke) |
| Abstract: T-Bereich | 105–290 Gyr | 190–320 Gyr |
| Section 4.1: Zyklusposition | 5–13% | 4–7% |
| Section 8: Item 3 | analytische Schätzung ausstehend | numerische Ergebnisse eingetragen |
| Section 8: Item 3a | nicht vorhanden | BAO-1-Par-Check abgeschlossen |
| Section 8: Item 3b | nicht vorhanden | BAO-2-Par-Fit abgeschlossen |

---

## 7. BAO-Geometrie-Checks (abgeschlossen 2026-04-24)

### 7a. 1-Parameter-Fit (H₀, Ω_m = 0.315 fest)

**Skript:** `Numerik/ebc_bao_fit.py`

| Modell | H₀ [km/s/Mpc] | χ²/dof | t₀ [Gyr] |
|--------|-----:|-----:|-----:|
| EBC x₀=0.06 | 63.37 | 2.040 | 13.79 |
| EBC x₀=0.10 | 63.32 | 2.047 | 13.79 |
| EBC x₀=0.15 | 63.24 | 2.061 | 13.79 |
| ΛCDM (Ref.) | 68.17 | 1.335 | 13.64 |

Größte Residuen: LRG2 z=0.706 (+2.50σ DM), LRG3+ELG1 z=0.930 (−2.59σ DH).

### 7b. 2-Parameter-Fit (H₀, Ω_m frei; r_d = 147.09 Mpc festgehalten)

**Skript:** `Numerik/ebc_bao_fit2.py`  
**Einschränkung:** r_d bei variablem Ω_m ideell über Aubourg-Formel mitzufitten.
Ergebnisse sind obere Schranken auf die Modellspannung.

| Modell | Ω_m | H₀ [km/s/Mpc] | χ²/dof | Δχ² | ΔAIC | t₀ [Gyr] |
|--------|-----|-----:|-----:|-----:|-----:|-----:|
| EBC x₀=0.06 | **0.283** | **64.48** | **1.869** | −3.76 | **−1.76** | 13.87 |
| EBC x₀=0.10 | **0.283** | **64.43** | **1.879** | −3.73 | −1.73 | 13.87 |
| EBC x₀=0.15 | **0.283** | **64.33** | **1.900** | −3.68 | −1.68 | 13.88 |
| ΛCDM (Ref.) | 0.293 | 69.32 | 1.281 | −1.88 | +0.12 | 13.69 |

dof = 10 (12 Datenpunkte − 2 freie Parameter)  
Ω_m-Profil-Konfidenzintervall (Δχ²<1): EBC → [0.268, 0.298]; ΛCDM → [0.281, 0.308]

**Residuen EBC x₀=0.06 (Ω_m=0.283, H₀=64.48):**

| Tracer | z | DM/σ | DH/σ |
|--------|---|------|------|
| LRG1 | 0.510 | −0.68σ | +1.71σ |
| LRG2 | 0.706 | **+2.06σ** | −1.00σ |
| LRG3+ELG1 | 0.930 | −0.40σ | **−2.28σ** |
| ELG2 | 1.317 | −0.34σ | +0.13σ |
| Lya | 2.330 | −1.03σ | +1.73σ |
| BGS | 0.295 | — | +0.90σ (DV) |
| QSO | 1.491 | — | −0.59σ (DV) |

**Interpretation:**
- EBC profitiert stärker vom freien Ω_m als ΛCDM (ΔAIC_EBC = −1.76 vs. ΔAIC_ΛCDM = +0.12)
- EBC-bevorzugtes Ω_m = 0.283 liegt unter Planck (0.315) und DESI (0.295)
- Strukturelle Residuen im Übergangsbereich z≈0.7–0.93 reduziert aber nicht beseitigt
- χ²-Rückstand EBC vs. ΛCDM: Δχ²_min = 5.88 (~2.4σ) — strukturell, nicht parametrisch

---

## 8. Bianchi-Defektterm (offenes theoretisches Problem)

$$\dot{\rho} + 3H(\rho+p) = \underbrace{-\frac{\dot{\Lambda}_{EBC} + \dot{\Lambda}_b}{8\pi G}}_{D_\Lambda} \underbrace{-\frac{3\gamma(a)H^2}{4\pi G}}_{D_\gamma}$$

- **D_Λ**: lösbar — analog Quintessenz
- **D_γ**: offen — kein Standardmechanismus bekannt

Kontakt: Prof. Brandenberger (McGill), Prof. Steinhardt (Princeton) — bislang keine Antwort.

---

## 9. Outreach-Status

| Kanal | Status |
|---|---|
| Zenodo (EN) | ✅ veröffentlicht (v2) |
| Zenodo (DE) | ✅ hinzugefügt |
| Physikerboard.de | ⚠️ gepostet, als "offtopic" markiert |
| Prof. Brandenberger | 📤 gesendet, keine Antwort |
| Prof. Steinhardt | 📤 gesendet, keine Antwort |
| Reddit r/cosmology | 🔲 geplant |
| YouTube "Breaking Lab" | 🔲 bei passendem Video |

---

## 10. Offene Punkte / nächste Schritte

**Priorität 1 — nächster Chat:**
3-Parameter-Fit (H₀, Ω_m, r_d) mit Aubourg-Formel r_d(Ω_m, h²).
Selbstkonsistente Behandlung der r_d/Ω_m-Kopplung.
Erwartet: EBC-Ω_m-Minimum verschiebt sich, χ²-Bild ändert sich.
Hochladen: EBC_paper_v3_draft.md + dieser Kontext + ebc_bao_fit2.py

**Priorität 2 — mittelfristig:**
- Paper v3 fertigstellen: Section 8 Items 3a+3b eintragen
- Section 8 Item 3b Paper-Text aus ebc_bao_fit2.py einarbeiten
- Reddit-Post verfassen (Fokus: w₀ = −2/3, ehrliche BAO-Diskussion)

**Priorität 3 — langfristig:**
- Bianchi-Defektterm: theoretische Ausarbeitung
- Schwarze-Loch-Erweiterung (τ_ext-Paper)
- Vollständiger CMB-Fit (eigenständiges Paper)

---

## 11. Dateien im Vault (EBC-Theorie/)

| Datei | Ort | Status |
|-------|-----|--------|
| EBC_paper_v2.md | Paper/ | ✅ eingefroren (Zenodo) |
| EBC_paper_v2_DE.md | Paper/ | ✅ eingefroren (Zenodo) |
| EBC_paper_v3_draft.md | Paper/ | ✅ aktueller Arbeitsstand |
| EBC_paper_v2_Korrektur_3_2.md | Paper/ | ✅ Korrekturprotokoll |
| Changelog.md | Paper/ | ✅ aktuell |
| ebc_physical.py | Numerik/ | ✅ aktuell |
| ebc_bao_fit.py | Numerik/ | ✅ 1-Par-Fit |
| ebc_bao_fit2.py | Numerik/ | ✅ neu (2026-04-24) — 2-Par-Fit |
| ebc_bao_fit.png | Numerik/Ergebnisse/ | ✅ vorhanden |
| ebc_bao_fit2.png | Numerik/Ergebnisse/ | ✅ neu (2026-04-24) |
| EBC_BAO_Check_Ergebnisse.md | Erweiterungen/ | ✅ vorhanden |
| EBC_pandoc_template.tex | Build/ | ✅ vorhanden |
| EBC-Session-Kontext.md | Kontext/ | ✅ diese Datei |

---

## 12. Wie neue Sessions starten

1. Diese Datei + EBC_paper_v3_draft.md hochladen
2. ebc_bao_fit2.py hochladen (für 3-Par-Fortsetzung)
3. ggf. ebc_physical.py hochladen (für numerische Fortsetzungen)
4. Einstieg: *"Wir setzen EBC-Arbeit fort — Kontext in hochgeladenen Dateien."*
5. Erstes Ziel benennen

**Nächstes Ziel:** 3-Parameter-Fit (H₀, Ω_m, r_d) mit Aubourg-Formel.
