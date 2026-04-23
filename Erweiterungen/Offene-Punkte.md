---
title: EBC — Offene Punkte
status: laufend
tags: [EBC, TODO, Entwicklung]
aktualisiert: 2026-04-22
---

# EBC — Offene Punkte

Strukturiert nach Priorität. Erledigte Punkte bleiben stehen (mit ✅ und Datum),
damit die Entwicklungshistorie nachvollziehbar bleibt.

---

## Priorität 1 — Paper-Korrekturen (dringend)

- [ ] **Abschnitt 3.2 korrigieren:** Materie *verkürzt* Zyklus (Ratio 0.75–0.85),
      nicht verlängert (Paper behauptet 1.15–1.25). Physikalische Begründung
      einfügen (Ω_m/x³ dominiert Frühphase → schnellere Expansion).
- [ ] **Quantitative Tabelle einfügen** (x₀, T_free, T_Materie, Ratio, f = t₀/T)
      aus physikalischer Integration in Abschnitt 3.2 oder 5.
- [ ] **H₀·t₀-Spannung ergänzen:** EBC ergibt H₀·t₀ ≈ 0.894 statt 0.951 (ΛCDM),
      d.h. ca. −6%. Als Diskussionspunkt in Abschnitt 7 oder 8.
- [ ] **Section 8, Punkt 3** ("Matter and radiation") als erledigt markieren
      (numerische Integration durchgeführt, Ergebnisse in Abschnitt 3.2).

---

## Priorität 2 — Numerik

- [ ] **ebc_physical.py neu erstellen** (Session-Absturz, Datei verloren).
      Berechnet Zyklusdauer mit Materie/Strahlung in H₀-Einheiten via
      Halbzyklus-Integral ∫ dx/(H(x)·x).
- [ ] **Neue Abbildung** aus physikalischer Integration erstellen und ins Paper
      einbinden (ersetzt oder ergänzt Fig. 1a/1b).
- [ ] **ODE-Validierung:** H₀·t₀ aus ODE-Integration stimmt mit Integral überein?

---

## Priorität 3 — Theorie

- [ ] **Bianchi-Defektterm D_γ ausarbeiten:** Energiefluss durch Dämpfungsterm
      hat keinen Standardmechanismus. Verbindung zu thermodynamischer Gravitation
      (Jacobson 1995, Verlinde 2010) prüfen.
- [ ] **D_Λ als Quintessenz-Analogon formalisieren:** Λ_EBC(a) als effektives
      Skalarfeld φ mit V(φ) ausdrücken — welche Potentialform ergibt sich?

---

## Priorität 4 — Outreach

- [ ] **Reddit r/cosmology:** Englischen Post verfassen (Fokus: w₀ = −2/3 vs. DESI).
- [ ] **Antworten abwarten:** Brandenberger (McGill), Steinhardt (Princeton).
- [ ] **YouTube Breaking Lab:** Kommentar zu DESI-Video, wenn passendes erscheint.

---

## Priorität 5 — Erweiterungen (langfristig)

- [ ] **τ_ext-Paper (Schwarze Löcher):** Wie verhält sich EBC bei extremer
      Kompression? Verbindung zu Hawking-Strahlung / BH-Entropie?
- [ ] **EBC für "Perfect Universe" adaptieren:** Populärwissenschaftliche
      Darstellung für Buch-Kapitel und Gedankenspieler-Video.

---

## Erledigt

- ✅ 2026-04 Englisches Paper auf Zenodo veröffentlicht
- ✅ 2026-04 Deutsche Übersetzung zu Zenodo-Eintrag hinzugefügt
- ✅ 2026-04 Bianchi-Defektterm analytisch hergeleitet (D_Λ + D_γ)
- ✅ 2026-04 Email an Prof. Brandenberger (McGill) gesendet
- ✅ 2026-04 Email an Prof. Steinhardt (Princeton) gesendet
- ✅ 2026-04 Physikerboard.de-Post verfasst und gepostet
- ✅ 2026-04 Physikalische Integration mit Materie durchgeführt (Ergebnisse oben)
