---
title: EBC Session-Kontext
status: aktuell
tags: [EBC, Kontext, Session]
aktualisiert: 2026-04-24 (abends — nach 3-Par-Fit + Paper v3)
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

**Publikation:** Zenodo v2, DOI: https://doi.org/10.5281/zenodo.19399593
**Aktueller Arbeitstand:** EBC_paper_v3.md (Patches applied, noch nicht
veröffentlicht — Pre-Publication-Review steht aus).

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

**Schallhorizont r_d (Aubourg 2015, Eq. 16):**
$$r_d = \frac{55.154 \cdot \exp[-72.3\,(\Omega_\nu h^2 + 0.0006)^2]}{(\Omega_m h^2)^{0.25351} \cdot (\Omega_b h^2)^{0.12807}}\ \mathrm{Mpc}$$

Gültig in EBC, da Λ_EBC bei z_drag ≈ 1060 < 0.0002 % von H² beiträgt.

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
| **r_d (Schallhorizont)** | BAO-Observablen | Gültig via Aubourg bei EBC, solange EBC-Term bei z ≈ 1100 vernachlässigbar (< 0.0002 % verifiziert) |
| **Zyklische Geometrie** | Volumenintegrale, Entropie | Standardformeln gelten nur im aktuellen Halbzyklus |
| **Keine Inflation ab Zyklus 2** (P7) | Horizont- und Flachheitsproblem | ΛCDM-Inflationsformeln nicht übertragbar |
| **Hubble-Spannung** | alle H₀-Bestimmungen | EBC löst die Spannung nicht (w₀>−1 modifiziert nur spätes Universum) |

### 4b. Bekannte Prüfergebnisse (dokumentiert)

| Berechnung | Methode gültig? | Quelle |
|------------|----------------|--------|
| Altersintegral H₀·t₀ über EBC1 | ✅ Ja | ebc_physical.py |
| Altersintegral über EBC2-ODE | ❌ Nein (Bianchi-Artefakt) | ebc_physical.py |
| Schallhorizont r_d aus Planck 2018 / Aubourg | ✅ Ja (EBC-Term < 0.0002% bei z=1100) | ebc_bao_fit3.py |
| BAO-Observablen DM/rd, DH/rd | ✅ Ja, wenn H_EBC(z) verwendet | ebc_bao_fit3.py |
| 1-Par-Fit (H₀, Ω_m=0.315 fest) | ✅ Ja (Ω_m als Einschränkung) | ebc_bao_fit.py |
| 2-Par-Fit (H₀, Ω_m frei, r_d=147.09 fest) | ⚠️ Obere Schranke (r_d-Kopplung ignoriert) | ebc_bao_fit2.py |
| 3-Par-Fit (H₀, Ω_m, r_d via Aubourg selbstkonsistent) | ✅ Ja | ebc_bao_fit3.py |
| Joint BAO + SNe Ia + CMB θ_* | 🔲 Offen — nächster Entwicklungsschritt | — |
| CMB-Anisotropien, Transferfunktion | ❌ Offen (τ_ext, kein EBC-CMB-Modell) | Paper Section 8 |
| Primordialspektrum / Inflation | ❌ Nicht übertragbar (P7) | Paper Section 6 |

---

## 5. Numerische Ergebnisse (Stand 2026-04-24 abends)

Verwendete Werte: Ω_m = 0.315 (Planck) bzw. freie Variable, Ω_r = 9.2×10⁻⁵,
1/H₀ = 14.51 Gyr bei H₀ = 67.4, KM_TO_GYR = 978.5.

### 5a. Halbzyklus-Zeiten

| x₀   | x*   | T_free [Gyr] | T_mat [Gyr] | Ratio | f = t₀/T |
|------|------|-------------|------------|-------|-----------|
| 0.06 | 16.7 | 349         | 320        | 0.917 | 4.3%      |
| 0.10 | 10.0 | 269         | 240        | 0.893 | 5.7%      |
| 0.15 |  6.7 | 218         | 190        | 0.869 | 7.3%      |

### 5b. BAO-Fits (DESI Y1, 12 Datenpunkte, mit DM/DH-Kovarianz)

| Fit-Typ | Modell | Ω_m | H₀ | r_d [Mpc] | χ²/dof | t₀ [Gyr] |
|---|---|---:|---:|---:|---:|---:|
| **1-Par** (Ω_m=0.315 fest) | EBC x₀=0.06 | 0.315 | 63.37 | 147.09 | 2.040 | 13.79 |
| 1-Par | ΛCDM | 0.315 | 68.17 | 147.09 | 1.335 | 13.64 |
| **2-Par** (r_d=147.09 fest) | EBC x₀=0.06 | 0.283 | 64.48 | 147.09 | 1.869 | 13.87 |
| 2-Par | ΛCDM | 0.293 | 69.32 | 147.09 | 1.281 | 13.69 |
| **3-Par** (r_d Aubourg, self-consistent) | EBC x₀=0.06 | 0.282 | **58.46** | **162.31** | 1.869 | **15.31** |
| 3-Par | ΛCDM | 0.294 | 68.99 | 147.67 | 1.280 | 13.74 |

**Kernbefund 3-Par-Fit:**
- χ² identisch zu 2-Par (die Verbesserung kam aus Ω_m-Freiheit, nicht aus r_d-Entkopplung)
- (H₀, r_d)-Degeneration in reinen BAO-Daten — Aufbrechen erfordert SNe Ia oder CMB θ_*
- Hubble-Spannung von EBC **nicht gelöst**, sondern leicht verschärft (58.5 vs. SH0ES 73)
- Weltalter t₀ ≈ 15.3 Gyr komfortabel mit Kugelsternhaufen konsistent
- Residuen robust: LRG2 (z=0.706, DM: +2.06σ), LRG3+ELG1 (z=0.930, DH: −2.27σ)

**Ω_b h² mit BBN-Prior frei:** liefert identische Ergebnisse (BAO allein
ist nicht sensitiv auf Ω_b getrennt von r_d).

---

## 6. Paper-Entwicklungsstand

### v2 (veröffentlicht auf Zenodo)

DOI: https://doi.org/10.5281/zenodo.19399593 (EN + DE)

### v3 (lokal, Patches angewendet 2026-04-24)

Alle vier inhaltlichen Patches aus EBC_paper_v3_patches.md auf
EBC_paper_v3_draft.md angewendet. Ergebnis: EBC_paper_v3.md (623 Zeilen).

**Geänderte Abschnitte:**
1. **Abstract** — "5–15%" → "4–7%" korrigiert; Hubble-Spannung ehrlich eingeordnet
2. **Section 3.2, H₀·t₀-Block** — 6%-Deficit-Narrativ durch self-consistent-Diskussion ersetzt
3. **Section 4.2 (Hubble Tension)** — Komplett-Neuschrieb: EBC löst die Spannung nicht
4. **Section 8, Item 3** — aus Absichtserklärung wurden vier Items:
   - 3a: 1-Par-Fit Ergebnisse
   - 3b: 2-Par-Fit Ergebnisse (mit Caveat fixes r_d)
   - 3c: 3-Par-Fit Ergebnisse (self-consistent)
   - 3d: Joint-Fit BAO + SNe + CMB θ_* (als nächster Schritt deklariert)

**Status vor Zenodo-Publikation:** Pre-Publication-Review steht aus —
komplettes Paper mit Claude als Reviewer noch einmal durchgehen.

---

## 7. Bianchi-Defektterm (offenes theoretisches Problem)

$$\dot{\rho} + 3H(\rho+p) = \underbrace{-\frac{\dot{\Lambda}_{EBC} + \dot{\Lambda}_b}{8\pi G}}_{D_\Lambda} \underbrace{-\frac{3\gamma(a)H^2}{4\pi G}}_{D_\gamma}$$

- **D_Λ**: lösbar — analog Quintessenz
- **D_γ**: offen — kein Standardmechanismus bekannt

Kontakt: Prof. Brandenberger (McGill), Prof. Steinhardt (Princeton) — bislang keine Antwort.

---

## 8. Outreach-Status

| Kanal | Status |
|---|---|
| Zenodo (EN) | ✅ veröffentlicht (v2) |
| Zenodo (DE) | ✅ hinzugefügt (v2) |
| Zenodo (v3) | 🔲 geplant (nach Review) |
| Physikerboard.de | ⚠️ gepostet, als "offtopic" markiert |
| Prof. Brandenberger | 📤 gesendet, keine Antwort |
| Prof. Steinhardt | 📤 gesendet, keine Antwort |
| Reddit r/cosmology | 🔲 geplant |
| YouTube "Breaking Lab" | 🔲 bei passendem Video |

---

## 9. Offene Punkte / nächste Schritte

**Priorität 1 — aktuelles Ziel (neuer Chat):**
**Joint-Fit BAO + SNe Ia + CMB θ_* (Item 3d konkretisieren)**
- Bricht die (H₀, r_d)-Degeneration aus 3c
- Pantheon+ oder Union3 für SNe; CMB θ_* als Prior aus Planck
- Erwartung: EBC-H₀ zwischen ~58 und ~65, mit engen Fehlerbalken
- Liefert neues Section-8-Item für Paper v3 (Erweiterung oder v3.1)
- Datenquellen klären: Pantheon+ = pantheonplussh0es.github.io; Planck θ_* = 100·θ_* = 1.04109±0.00030

**Priorität 2 — nach Joint-Fit:**
- Pre-Publication-Review des vollständigen EBC_paper_v3.md
- Dann Zenodo v3 publizieren
- Changelog v2 → v3 schreiben

**Priorität 3 — mittelfristig:**
- Reddit-Post verfassen (Fokus: w₀ = −2/3, ehrliche BAO-Diskussion inkl. H₀-Frage)
- Bianchi-Defektterm: theoretische Ausarbeitung
- Schwarze-Loch-Erweiterung (τ_ext-Paper): Motivation *nicht* über Merger-Dynamik, sondern über Singularitätsvermeidung im Inneren; Anschluss an Rovelli/Ashtekar (Planck stars, LQG)

---

## 10. Dateien im Vault (EBC-Theorie/)

| Datei | Ort | Status |
|-------|-----|--------|
| EBC_paper_v2.md | Paper/ | ✅ eingefroren (Zenodo) |
| EBC_paper_v2_DE.md | Paper/ | ✅ eingefroren (Zenodo) |
| EBC_paper_v3_draft.md | Paper/ | ⚠️ Vorgänger von v3 |
| **EBC_paper_v3.md** | Paper/ | ✅ **aktueller Stand (Patches applied)** |
| EBC_paper_v3_patches.md | Paper/ | 📋 Änderungsprotokoll v3-draft → v3 |
| Changelog.md | Paper/ | 🔲 auf v3 zu aktualisieren |
| ebc_physical.py | Numerik/ | ✅ aktuell |
| ebc_bao_fit.py | Numerik/ | ✅ 1-Par-Fit |
| ebc_bao_fit2.py | Numerik/ | ✅ 2-Par-Fit (fest r_d) |
| **ebc_bao_fit3.py** | Numerik/ | ✅ **3-Par-Fit (Aubourg)** |
| ebc_bao_fit.png | Numerik/Ergebnisse/ | ✅ |
| ebc_bao_fit2.png | Numerik/Ergebnisse/ | ✅ |
| ebc_bao_fit3.png | Numerik/Ergebnisse/ | ✅ neu |
| ebc_joint_fit.py | Numerik/ | 🔲 nächster Chat |
| EBC-Session-Kontext.md | Kontext/ | ✅ diese Datei (aktualisiert) |

---

## 11. Wie neuen Chat starten

**Upload (Pflicht):**
- EBC-Session-Kontext.md (diese Datei)
- EBC_paper_v3.md (aktueller Paper-Stand)
- ebc_bao_fit3.py (als Strukturvorlage für ebc_joint_fit.py)

**Upload (je nach Bedarf):**
- ebc_physical.py (falls Zeitintegrale/Weltalter relevant)

**Einstiegssatz:**
> "Wir setzen EBC-Arbeit fort — Kontext in hochgeladenen Dateien.
> Nächstes Ziel: Joint-Fit BAO + SNe Ia + CMB θ_* (Section 8, Item 3d).
> Bricht die (H₀, r_d)-Degeneration aus 3c und liefert für Paper v3
> ein schärferes H₀. Bitte zuerst kurz den Plan skizzieren — welche
> Datenquellen, welche Likelihood-Kombination, welche Annahmen —
> bevor Du anfängst zu rechnen."

**Hintergrund für Claude:** Wolfgang hat keinen Physik-Hintergrund und
kann Rechenschritte nicht unabhängig prüfen. Methodische Annahmen daher
vor dem Ausführen erklären, Caveats sichtbar machen, kritisch statt
enthusiastisch bleiben.
