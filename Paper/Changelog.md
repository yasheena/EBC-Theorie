---
title: EBC Paper — Changelog
status: laufend
tags: [EBC, Paper, Versionshistorie]
aktualisiert: 2026-04-23
---

# EBC Paper — Changelog

---

## v3 — draft (2026-04-23) — noch nicht veröffentlicht

**Datei:** `EBC_paper_v3_draft.md`

### Korrekturen
- **Section 3.2:** Materie-Korrektur vollständig überarbeitet.
  - Vorzeichen korrigiert: Materie *verkürzt* den Zyklus (Ratio ≈ 0,87–0,92),
    nicht verlängert (zuvor fälschlich 1,15–1,25).
  - Analytische Abschätzung ersetzt durch vollständige numerische Integration
    (EBC1 + EBC2 mit Ω_m = 0,315, Ω_r = 9,2×10⁻⁵).
  - Quantitative Tabelle eingefügt (T_free, T_mat, Ratio, f für x₀ = 0,06–0,15).
  - Zeitbudget für x₀ = 0,10 eingefügt.
  - T-Bereich aktualisiert: 190–320 Gyr (zuvor 105–290 Gyr).
  - Zyklusposition aktualisiert: f ≈ 4–7% (zuvor 5–13%).

### Ergänzungen
- **Section 3.2:** Neuer Absatz „H₀·t₀ consistency":
  - EBC1-basierter Wert: H₀·t₀ ≈ 0,893 → t₀ ≈ 12,95 Gyr (−6% vs. ΛCDM).
  - Hinweis: Die 13,8 Gyr sind eine ΛCDM-abhängige Inferenz; das 6%-Defizit
    ist eine obere Schranke auf die echte Modellspannung.
- **Section 8:** Item 3 aktualisiert (neue numerische Ergebnisse).
  - Neuer Punkt 3a: „H₀·t₀ consistency and self-consistent parameter fit"
    als Entwicklungspriorität ausgewiesen.
- **Abstract:** T-Bereich auf 190–320 Gyr aktualisiert.
- **Section 4.1:** Zykluspositionsangabe auf 4–7% aktualisiert.

### Hintergrund
Korrekturprotokoll: `Paper/EBC_paper_v2_Korrektur_3_2.md`
Numerik-Skript: `Numerik/ebc_physical.py`

---

## v2 / v1.2 — (veröffentlicht, Zenodo)

**Datei:** `EBC_paper_v2.md` / `EBC_paper_v2_DE.md`
**DOI:** https://doi.org/10.5281/zenodo.19399593

Veröffentlichter Stand. Enthält englische und deutsche Version.
Keine inhaltlichen Änderungen gegenüber v1.1 außer redaktionellen
Korrekturen (Formulierungen, Formatierung).

---

## v1.1 — (Zenodo, Vorgängerversion)

Erste vollständige Version mit allen zehn Postulaten, analytischer
w₀ = −2/3-Herleitung und numerischer Illustration (materiefreier Grenzfall).

---

## v1.0 — (Zenodo, Erstveröffentlichung)

Initiale Veröffentlichung.
