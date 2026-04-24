# Prompt: EBC — BAO-Geometrie-Check (selbstkonsistenter Fit)

## Kontext
[EBC_paper_v2.md und EBC-Session-Kontext.md hochladen]

Wir setzen EBC-Arbeit fort. Kontext in den hochgeladenen Dateien.

## Ziel dieser Session
Selbstkonsistenten BAO-Geometrie-Check durchführen: Wie gut beschreibt
$H_\mathrm{EBC}(z)$ die DESI-BAO-Beobachtungsdaten — und welches $H_0$
sowie welches $t_0$ folgen daraus im EBC-Rahmen?

## Hintergrund (bereits erarbeitet)
Das EBC-Modell liefert aus der Friedmann-Gleichung (EBC1):

$$H^2_\mathrm{EBC}(z) = H_0^2 \left[\frac{\Omega_m}{x^3} +
\frac{\Omega_r}{x^4} + \Omega_{DE}\!\left(\frac{1}{x} -
\frac{x}{x_*^2}\right)\right], \quad x = \frac{1}{1+z}$$

mit $\Omega_{DE} = (1 - \Omega_m - \Omega_r)/(1 - 1/x_*^2)$.

Die EBC-Altersvorhersage ergibt $H_0 t_0 \approx 0{,}893$ (d.h. $t_0
\approx 12{,}95$ Gyr), während ΛCDM $H_0 t_0 = 0{,}951$ liefert (6%
Defizit). Diese Spannung ist jedoch eine **obere Schranke**, weil die
ΛCDM-Referenz selbst aus einem ΛCDM-Fit an CMB/BAO-Daten stammt.

## Begründung, warum BAO hier der richtige Ansatzpunkt ist
Der Schallhorizont $r_s$ entsteht bei $z \gtrsim 1100$, wo der EBC-Term
($\Omega_{DE}/x \sim \Omega_{DE} \cdot (1+z)$) bei $z \sim 1100$ zwar groß
ist, aber bitte **zunächst numerisch prüfen**, ob er gegenüber
$\Omega_m (1+z)^3$ und $\Omega_r (1+z)^4$ vernachlässigbar ist.
Falls ja: $r_s$ ist in EBC identisch mit dem ΛCDM-Wert und kann als
bekannte Größe übernommen werden ($r_s \approx 147{,}09$ Mpc, Planck 2018).

Die BAO-Observablen messen dann:
$$D_H(z)/r_s = \frac{c}{H_\mathrm{EBC}(z) \cdot r_s}, \qquad
D_M(z)/r_s = \frac{1}{r_s}\int_0^z \frac{c\,dz'}{H_\mathrm{EBC}(z')}$$

## Konkrete Aufgaben

### Schritt 1: Prüfung der r_s-Annahme
- EBC-Term bei $z = 1100$ numerisch berechnen und mit $\Omega_m(1+z)^3$
  und $\Omega_r(1+z)^4$ vergleichen.
- Falls EBC-Term < 1% der Gesamtdichte: $r_s$ übernehmen. Sonst: $r_s$
  numerisch in EBC neu berechnen.

### Schritt 2: DESI-BAO-Datenpunkte einlesen
DESI 2024 (arXiv:2404.03002) liefert $D_H/r_s$ und $D_M/r_s$ bei:
$z = 0{,}30,\ 0{,}51,\ 0{,}71,\ 0{,}93,\ 1{,}32,\ 1{,}49,\ 2{,}33$
(Werte aus Tabelle 1 des Papers — bitte per web_search/web_fetch abrufen
und als Array ins Skript eintragen).

### Schritt 3: EBC-Vorhersage berechnen und plotten
- $D_H(z)/r_s$ und $D_M(z)/r_s$ in EBC für verschiedene $x_0$-Werte
  (0.06, 0.10, 0.15) sowie für ΛCDM berechnen.
- Gegen DESI-Datenpunkte plotten.
- $\chi^2$ oder einfaches Residuen-Maß ausrechnen.

### Schritt 4: Freien Parameter $H_0$ anpassen
- $H_0$ als einzigen freien Parameter behandeln (alle $\Omega$ fixiert).
- Besten EBC-$H_0$ durch Minimierung der BAO-Residuen bestimmen.
- Daraus $t_0^{(\mathrm{EBC,fit})}$ berechnen und mit 13,8 Gyr vergleichen.

### Schritt 5: Ergebnisinterpretation
- Ist die EBC-Kurve innerhalb der DESI-Fehlerbalken?
- Wie groß ist die verbleibende Spannung in $t_0$?
- Bewertung für Paper-Abschnitt 8, Item 3a.

## Output
- Python-Skript `ebc_bao_fit.py` (vault-kompatibel, Numerik/)
- Plot als PNG
- Zusammenfassung als Markdown (Ergebnisse + Paper-Text-Entwurf für
  Section 8 Item 3a)

## Kommunikation
Bitte auf Deutsch. Outputs als Markdown oder Python.
