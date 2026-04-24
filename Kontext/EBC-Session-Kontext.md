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

Viele Standardmethoden der Kosmologie (Altersintegral, BAO-Observablen,
Distanzmaße, CMB-Physik) sind direkt aus dem ΛCDM-Modell abgeleitet und
setzen stillschweigend dessen Struktur voraus. EBC weicht an mehreren Punkten
davon ab. Ohne explizite Prüfung können Ergebnisse systematisch falsch sein.

### 4a. EBC-Besonderheiten und ihre Auswirkungen auf Berechnungen

| EBC-Merkmal | Betrifft | Konsequenz |
|-------------|----------|------------|
| **Bianchi-Defekt** (EBC1/EBC2-Inkonsistenz) | Weltalter, Zeitintegrale | Altersintegral ausschließlich über EBC1; EBC2-ODE-Wert (H₀·t₀ ≈ 0.766) ist Artefakt |
| **w₀ = −2/3 ≠ −1** (dynamische DE) | H(z), Distanzmaße, χ²-Fits | H_EBC(z) statt H_ΛCDM(z) verwenden; ΛCDM-H(z) ergibt modellinkonsistente Resultate |
| **Ω-Werte aus ΛCDM** (Planck 2018) | alle Fits mit freien Parametern | Als Einschränkung dokumentieren; Ergebnisse sind obere Schranken auf Modellspannungen |
| **τ_ext** (externer Zeitbezug, P3) | Frühuniversum, CMB, Inflation | Standardmethoden aus ΛCDM i.d.R. ungültig; kein formaler EBC-Ersatz hergeleitet — offen kennzeichnen |
| **r_d (Schallhorizont)** | BAO-Observablen | Gültig solange EBC-Term bei z ≈ 1100 vernachlässigbar; numerisch bestätigt (< 0.0002%) |
| **Zyklische Geometrie** | Volumenintegrale, Entropie, Thermodynamik | Standardformeln gelten nur im aktuellen Halbzyklus; frühere Zyklen erfordern gesonderte Behandlung |
| **Keine Inflation ab Zyklus 2** (P7) | Horizont- und Flachheitsproblem | ΛCDM-Inflationsformeln nicht übertragbar; EBC-Argument läuft über Bouncegeometrie |

### 4b. Bekannte Prüfergebnisse (dokumentiert)

| Berechnung | Methode gültig? | Quelle |
|------------|----------------|--------|
| Altersintegral H₀·t₀ über EBC1 | ✅ Ja | Abschnitt 5c, ebc_physical.py |
| Altersintegral über EBC2-ODE | ❌ Nein (Bianchi-Artefakt) | Abschnitt 5c, ebc_physical.py |
| Schallhorizont r_d aus Planck 2018 | ✅ Ja (EBC-Term < 0.0002% bei z=1100) | BAO-Check, ebc_bao_fit.py |
| BAO-Observablen DM/rd, DH/rd | ✅ Ja, wenn H_EBC(z) verwendet | BAO-Check, ebc_bao_fit.py |
| Ω_m, Ω_r aus Planck | ⚠️ Näherung (kein EBC-eigener Fit) | alle Rechnungen; Ergebnisse als obere Schranke |
| CMB-Anisotropien, Transferfunktion | ❌ Offen (τ_ext, kein EBC-CMB-Modell) | Paper Section 8 |
| Primordialspektrum / Inflation | ❌ Nicht übertragbar (P7) | Paper Section 6 |

### 4c. Handlungsregel

Vor jeder neuen Berechnung:

1. **Welche physikalische Größe wird berechnet?**
2. **Setzt die Standardmethode ΛCDM-H(z), ΛCDM-Inflation oder monotone
   Expansion voraus?**
3. **Welche EBC-Besonderheiten aus 4a sind betroffen?**
4. **Falls Methode angepasst oder ungültig: explizit im Output kennzeichnen.**

---

## 5. Numerische Ergebnisse (physikalische Integration)

Verwendete Werte: Ω_m = 0.315, Ω_r = 9.2×10⁻⁵, 1/H₀ = 14.51 Gyr

### 4a. Halbzyklus-Zeiten

| x₀   | x*   | T_free [Gyr] | T_mat [Gyr] | Ratio | f = t₀/T |
|------|------|-------------|------------|-------|-----------|
| 0.06 | 16.7 | 349         | 320        | 0.917 | 4.3%      |
| 0.08 | 12.5 | 301         | 273        | 0.904 | 5.1%      |
| 0.10 | 10.0 | 269         | 240        | 0.893 | 5.7%      |
| 0.13 |  7.7 | 235         | 207        | 0.878 | 6.7%      |
| 0.15 |  6.7 | 218         | 190        | 0.869 | 7.3%      |

T_free: EBC ohne Materie/Strahlung. T_mat: physikalisch mit Ω_m, Ω_r.
Ratio = T_mat/T_free. Materie *verkürzt* den Zyklus um 8–13%.
**Zyklusdauer und Ratio: EBC2-basiert, robust.**
**f = t₀/T: gemischt — t₀ aus EBC1 (korrekt), T aus EBC2.**

### 4b. Zeitbudget für x₀ = 0.10 (Halbzyklus)

| Phase                              | Dauer [Gyr] |
|------------------------------------|-------------|
| Strahlungsdominiert (x < 3×10⁻⁴)  | ~0.0        |
| Materiedominiert (3×10⁻⁴ < x < 0.65) | ~7.0     |
| Materie-EBC-Übergang (0.65 < x < 1)  | ~4.1     |
| EBC-dominiert (1 < x < x*)         | ~109        |
| **Gesamt Halbzyklus**              | **~120 Gyr**|

### 4c. H₀·t₀-Konsistenz

**Maßgebliche Berechnung: EBC1-Integral** (nicht ODE-Solver):

$$H_0 \cdot t_0^{(EBC)} = \int_0^1 \frac{dx}{x\,\sqrt{\Omega_m/x^3 + \Omega_r/x^4 + \Omega_{DE}(1/x - x/x_*^2)}} \approx 0.893$$

→ Bei H₀ = 67.4 km/s/Mpc: t₀ ≈ 12.95 Gyr (−6.1% vs. ΛCDM-Referenz)
→ Bei H₀ = 63.4 km/s/Mpc (BAO-Fit): t₀ ≈ 13.8 Gyr ✓ (siehe Abschnitt 7)

**Bianchi-Artefakt:** Der ODE-Solver (EBC2) liefert H₀·t₀ ≈ 0.766 (−19.5%).
Dieser Wert darf NICHT als Weltalter verwendet werden. Er ist in
`ebc_physical.py` als Artefakt dokumentiert und nur zur Diagnose ausgegeben.

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
| Section 8: Item 3a | nicht vorhanden | BAO-Check abgeschlossen (s. Abschnitt 7) |

Korrekturprotokoll: `Paper/EBC_paper_v2_Korrektur_3_2.md`

---

## 7. BAO-Geometrie-Check (abgeschlossen 2026-04-24)

**Skript:** `Numerik/ebc_bao_fit.py`
**Plot:** `Numerik/Ergebnisse/ebc_bao_fit.png`
**Vollständige Ergebnisse:** `Erweiterungen/EBC_BAO_Check_Ergebnisse.md`

### Methode

Fit von H_EBC(z) gegen DESI DR1 BAO-Daten (arXiv:2404.03002, Tabelle 1;
7 Rotverschiebungsbins, 12 Datenpunkte) mit H₀ als einzigem freien Parameter.
Analytische χ²-Minimierung (alle Observablen ∝ 1/H₀).
Kovarianzmatrizen der korrelierten DM/rd- und DH/rd-Messungen berücksichtigt.

### Voraussetzung bestätigt: r_d gültig

EBC-Term bei z = 1100: < 0.0002% der Gesamtdichte.
→ r_d = 147.09 Mpc (Planck 2018) unverändert gültig in EBC.

### Fit-Ergebnisse

| Modell | H₀ [km/s/Mpc] | σ_H₀ | χ²/dof | H₀·t₀ | t₀ [Gyr] |
|--------|-----:|-----:|-----:|-----:|-----:|
| EBC x₀=0.06 | **63.37** | 0.30 | 2.040 | 0.893 | 13.79 |
| EBC x₀=0.10 | **63.32** | 0.30 | 2.047 | 0.893 | 13.79 |
| EBC x₀=0.15 | **63.24** | 0.30 | 2.061 | 0.891 | 13.79 |
| ΛCDM (Referenz) | **68.17** | 0.32 | 1.335 | 0.951 | 13.64 |

### Interpretation

**Positiv:**
- t₀-Spannung weitgehend aufgelöst: Bei H₀_EBC = 63.4 km/s/Mpc ergibt
  das EBC1-Altersintegral t₀ = 13.8 Gyr — ohne Konflikt mit Beobachtungen.
- H₀-Vorhersage stabil über alle x₀ (Variation < 0.2 km/s/Mpc).
- r_d-Annahme vollständig bestätigt.

**Kritisch (offen kommunizieren):**
- χ²/dof = 2.04 vs. ΛCDM 1.33 — EBC passt BAO-Geometrie statistisch
  schlechter an (~2.7σ Rückstand gegenüber ΛCDM).
- Größte Residuen bei z = 0.706 (ΔDM/σ = +2.50) und z = 0.930
  (ΔDH/σ = −2.59) — genau im EBC-Übergangsbereich Materie→EBC-Dominanz.
- H₀_EBC ≈ 63.4 km/s/Mpc verschlechtert die Hubble-Spannung statt sie
  zu mildern (liegt noch weiter unter dem Planck-Wert 67.4).

**Einschränkung:** Ω_m = 0.315 aus Planck/ΛCDM festgehalten.
Ein selbstkonsistenter Fit mit freiem Ω_m könnte die Residuen verändern
— dies ist der identifizierte nächste Entwicklungsschritt.

### Paper-Text für Section 8 Item 3a (bereit)

In `Erweiterungen/EBC_BAO_Check_Ergebnisse.md` enthalten.

---

## 8. Bianchi-Defektterm (offenes theoretisches Problem)

$$\dot{\rho} + 3H(\rho+p) = \underbrace{-\frac{\dot{\Lambda}_{EBC} + \dot{\Lambda}_b}{8\pi G}}_{D_\Lambda} \underbrace{-\frac{3\gamma(a)H^2}{4\pi G}}_{D_\gamma}$$

- **D_Λ**: lösbar — analog Quintessenz (effektives Skalarfeld)
- **D_γ**: offen — kein Standardmechanismus bekannt

Kontakt: Prof. Brandenberger (McGill), Prof. Steinhardt (Princeton) —
bislang keine Antwort.

---

## 9. Outreach-Status

| Kanal                   | Status                            |
|-------------------------|-----------------------------------|
| Zenodo (EN)             | ✅ veröffentlicht (v2)            |
| Zenodo (DE)             | ✅ hinzugefügt                    |
| Physikerboard.de        | ⚠️ gepostet, als "offtopic" markiert |
| Prof. Brandenberger     | 📤 gesendet, keine Antwort        |
| Prof. Steinhardt        | 📤 gesendet, keine Antwort        |
| Reddit r/cosmology      | 🔲 geplant                        |
| YouTube "Breaking Lab"  | 🔲 bei passendem Video            |

---

## 10. Offene Punkte / nächste Schritte

**Priorität 1 — nächster Chat:**
BAO-Fit mit freiem Ω_m (zwei freie Parameter: H₀, Ω_m).
Ziel: Klären ob EBC mit selbstkonsistentem Ω_m die Residuen bei
z ≈ 0.7–0.93 schließen kann, oder ob die Abweichung strukturell ist.
Volle Kovarianz-Behandlung beibehalten.
Hochladen: EBC_paper_v3_draft.md + dieser Kontext + ebc_bao_fit.py

**Priorität 2 — mittelfristig:**
- Paper v3 fertigstellen: Section 8 Item 3a mit BAO-Ergebnissen eintragen
- Neue Figure aus ebc_physical.py und ebc_bao_fit.py für v3
- Reddit-Post verfassen (Fokus: w₀ = −2/3 Vorhersage, ehrliche BAO-Diskussion)

**Priorität 3 — langfristig:**
- Bianchi-Defektterm: theoretische Ausarbeitung
- Schwarze-Loch-Erweiterung (τ_ext-Paper)
- Vollständiger CMB-Fit (eigenständiges Paper)

Detaillierte Liste: `Erweiterungen/Offene-Punkte.md`

---

## 11. Dateien im Vault (EBC-Theorie/)

| Datei                              | Ort                  | Status           |
|-----------------------------------|----------------------|------------------|
| EBC_paper_v2.md                   | Paper/               | ✅ eingefroren (Zenodo) |
| EBC_paper_v2_DE.md                | Paper/               | ✅ eingefroren (Zenodo) |
| EBC_paper_v3_draft.md             | Paper/               | ✅ aktueller Arbeitsstand |
| EBC_paper_v2_Korrektur_3_2.md     | Paper/               | ✅ Korrekturprotokoll |
| Changelog.md                      | Paper/               | ✅ aktuell       |
| ebc_physical.py                   | Numerik/             | ✅ aktuell (korrigiert 2026-04-23) |
| ebc_bao_fit.py                    | Numerik/             | ✅ neu (2026-04-24) |
| EBC_v2_figures_source.py          | Figures/             | ✅ eingefroren   |
| EBC_v3_figures_source.py          | Figures/             | ✅ aktuell       |
| EBC_v2_fig1a/b.svg                | Figures/             | ✅ vorhanden     |
| EBC_v2_fig1a/b_final.svg/pdf      | Figures/             | ✅ vorhanden     |
| ebc_physical_results.png          | Numerik/Ergebnisse/  | ✅ vorhanden     |
| ebc_bao_fit.png                   | Numerik/Ergebnisse/  | ✅ neu (2026-04-24) |
| EBC_BAO_Check_Ergebnisse.md       | Erweiterungen/       | ✅ neu (2026-04-24) |
| EBC_pandoc_template.tex           | Build/               | ✅ vorhanden     |
| create_pdf.bat                    | Build/               | ✅ aktualisiert  |
| BUILD.md                          | Build/               | ✅ aktuell       |
| Offene-Punkte.md                  | Erweiterungen/       | ✅ aktuell       |
| EBC-Session-Kontext.md            | Kontext/             | ✅ diese Datei   |

---

## 12. Wie neue Sessions starten

1. Diese Datei + EBC_paper_v3_draft.md hochladen
2. ebc_bao_fit.py hochladen (für BAO-Fortsetzung)
3. ggf. ebc_physical.py hochladen (für numerische Fortsetzungen)
4. Einstieg: *"Wir setzen EBC-Arbeit fort — Kontext in hochgeladenen Dateien."*
5. Erstes Ziel benennen

**Nächstes Ziel:** BAO-Fit mit freiem Ω_m (zwei Parameter: H₀, Ω_m).
