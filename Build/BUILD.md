---
title: EBC — Build-Dokumentation
status: aktuell
tags: [EBC, Build, Workflow]
aktualisiert: 2026-04-23
---

# EBC Paper — Build-Dokumentation

Diese Datei beschreibt, wie aus den Quelldateien die finalen PDF-Publikationen
erzeugt werden. Sie gilt für v2 und alle nachfolgenden Versionen.

---

## Voraussetzungen

| Tool | Zweck | Bezugsquelle |
|------|-------|--------------|
| Python 3.x | Grafik-Erzeugung | python.org |
| matplotlib, scipy, numpy | Python-Abhängigkeiten | `pip install ...` |
| Inkscape | SVG-Nachbearbeitung + PDF-Export | inkscape.org |
| pandoc | Markdown → PDF | pandoc.org |
| XeLaTeX (TeX-Distribution) | PDF-Engine für pandoc | z.B. MiKTeX, TeX Live |

---

## Pipeline: Schritt für Schritt

### Schritt 1 — Grafiken erzeugen (Python)

Skript: `Numerik/ebc_illustration.py`

```
python ebc_illustration.py
```

Erzeugt (im Skript konfigurierter Ausgabepfad, ggf. anpassen — siehe Hinweis
unten):

```
Figures/EBC_v<N>_fig1a.svg
Figures/EBC_v<N>_fig1b.svg
```

> **Pfad-Hinweis:** In den Python-Skripten sind Ausgabepfade möglicherweise
> als absolute oder relative Pfade hartcodiert. Vor dem ersten Aufruf bitte
> die Pfadvariablen im Skript-Header prüfen und ggf. auf die lokale
> Verzeichnisstruktur anpassen. Entsprechende Stellen sind im Code mit dem
> Kommentar `# PFAD ANPASSEN` markiert (oder sollten es sein).

---

### Schritt 2 — Grafiken nachbearbeiten (Inkscape)

Die Python-generierten SVGs werden in Inkscape manuell nachbearbeitet:
ungünstig platzierte Texte, Pfeile und Beschriftungen werden korrigiert
und neu positioniert.

**Eingabe:**
```
Figures/EBC_v<N>_fig1a.svg
Figures/EBC_v<N>_fig1b.svg
```

**Vorgehen in Inkscape:**
1. SVG öffnen und Layoutkorrekturen vornehmen.
2. Ergebnis speichern als:
   ```
   Figures/EBC_v<N>_fig1a_final.svg
   Figures/EBC_v<N>_fig1b_final.svg
   ```
3. PDF-Export (Datei → Exportieren → Als PDF speichern):
   ```
   Figures/EBC_v<N>_fig1a_final.pdf
   Figures/EBC_v<N>_fig1b_final.pdf
   ```

Diese PDFs werden direkt von pandoc ins Paper eingebunden.

---

### Schritt 3 — PDF-Publikation erzeugen (pandoc)

Skript: `Build/create_pdf.bat`

```
cd Build
create_pdf.bat <N>
```

Beispiele:
```
create_pdf.bat 2    → erzeugt Paper v2 (EN + DE)
create_pdf.bat 3    → erzeugt Paper v3 (EN + DE)
```

**Eingaben:**
```
Paper/EBC_paper_v<N>.md         ← englischer Quelltext
Paper/EBC_paper_v<N>_DE.md      ← deutscher Quelltext (optional)
Figures/EBC_v<N>_fig1a_final.pdf
Figures/EBC_v<N>_fig1b_final.pdf
Build/EBC_pandoc_template.tex   ← LaTeX-Template (versionsneutral)
```

**Ausgaben:**
```
Paper/EBC_v<N>_paper.pdf
Paper/EBC_v<N>_paper_DE.pdf
```

> **Hinweis für neue Versionen:** Das pandoc-Template
> (`EBC_pandoc_template.tex`) ist versionsneutral und wird nicht umbenannt.
> Abbildungsreferenzen im Markdown (`EBC_fig1a_final.pdf` o.ä.) müssen im
> Markdown-Quelltext auf den neuen Versionspräfix angepasst werden.

---

## Dateiübersicht pro Version

```
Figures/
├── EBC_v<N>_fig1a.svg            ← Python-Output (Rohversion)
├── EBC_v<N>_fig1b.svg
├── EBC_v<N>_fig1a_final.svg      ← Inkscape-Bearbeitung
├── EBC_v<N>_fig1b_final.svg
├── EBC_v<N>_fig1a_final.pdf      ← Inkscape-Export → ins Paper
└── EBC_v<N>_fig1b_final.pdf

Paper/
├── EBC_paper_v<N>.md             ← Quelltext EN
├── EBC_paper_v<N>_DE.md          ← Quelltext DE
├── EBC_v<N>_paper.pdf            ← finale Publikation EN
└── EBC_v<N>_paper_DE.pdf         ← finale Publikation DE

Build/
├── BUILD.md                      ← diese Datei
├── EBC_pandoc_template.tex       ← LaTeX-Template (versionsneutral)
└── create_pdf.bat                ← Build-Skript
```

---

## Hinweise für Git-Nutzer

- `.svg`- und `.md`-Dateien sind textbasiert und profitieren vollständig
  von Git-Versionierung (Diffs lesbar).
- `.pdf`-Dateien sind Binärdateien — sie sind im Repository enthalten,
  aber Diffs sind nicht sinnvoll lesbar. Der relevante Stand lässt sich
  über den zugehörigen Git-Tag oder Commit-Zeitstempel nachvollziehen.
- Veröffentlichte Versionen sind zusätzlich auf Zenodo archiviert
  (DOI: https://doi.org/10.5281/zenodo.19399593).
- Python-Skripte in `Numerik/` können sich zwischen Versionen ändern.
  Welcher Stand zu welcher Publikation gehört, ist im jeweiligen
  Commit-Kommentar oder im `Changelog.md` dokumentiert.
