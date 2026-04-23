---
title: "Elastische-Bounce-Kosmologie (EBC): Ein phänomenologischer Rahmen für quasi-zyklische kosmische Expansion mit einer dynamischen räumlichen Rückstellkraft"
date: "März 2026"
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{booktabs}
  - \usepackage{hyperref}
  - \usepackage[table]{xcolor}
---

**Wolfgang Mattis** — Unabhängiger Forscher  
ebc@wm0.eu · ORCID: [0009-0006-9810-7819](https://orcid.org/0009-0006-9810-7819)

---

## Zusammenfassung

Wir stellen die Elastische-Bounce-Kosmologie (EBC) vor, einen phänomenologischen Rahmen, in dem der kosmische Skalenfaktor durch modifizierte Friedmann-Gleichungen bestimmt wird, die einen dynamischen, skalenfaktorabhängigen effektiven kosmologischen Term beinhalten. Die zentrale Hypothese lautet, dass der Raum eine intrinsische elastische Eigenschaft besitzt — eine geometrische Rückstellkraft, die oszillatorische Expansion und Kontraktion antreibt, ohne je eine Singularität zu erreichen. Dabei wird die kosmologische Konstante durch einen dynamischen Term $\Lambda_\mathrm{EBC}(a) = \Lambda_0(a_*/a - a/a_*)$ ersetzt, wobei $a_*$ der Gleichgewichts-Skalenfaktor ist, ergänzt durch einen Bounce-Term $\Lambda_b(a) = \Lambda_b(a_\mathrm{min}/a)^4$, der einen singulären Kollaps verhindert.

Ein zentrales analytisches Ergebnis folgt direkt aus diesem Ansatz: Die effektive Zustands\-gleichung der Dunklen Energie im aktuellen Beobachtungsregime ($a \ll a_*$) lautet

$$w_\mathrm{EBC}(a) = -1 + \frac{1+x^2}{3(1-x^2)},\quad x = a/a_*,$$

woraus sich $w_0 \approx -2/3 \approx -0{,}667$ im Grenzfall $a_0 \ll a_*$ ergibt, ohne jegliche Abstimmung von Modellparametern. Dies stimmt mit der DESI-2024-Messung $w_0 = -0{,}70 \pm 0{,}10$ auf dem $1\sigma$-Niveau überein. Numerische Integration demonstriert schwach gedämpftes quasi-zyklisches Verhalten, das zahlreiche Expansions-Kontraktions-Phasen aufrechthält, bevor es sich asymptotisch dem Gleichgewicht annähert.

Mehrere offene Probleme der Standardkosmologie werden in diesem Rahmen behandelt: die Natur der Dunklen Energie (neu interpretiert als geometrische Raumeigenschaft), die Hubble-Spannung (zurückgeführt auf räumliche Inhomogenitäten, die sich über Zyklen angesammelt haben), CMB-Anomalien, das Lithium-7-Problem (selektive nukleare Photodisintegration beim Bounce) und die Baryogenese (verteilt über einen oder mehrere vollständige Zyklen). Wir schätzen, dass die aktuelle Epoche im 3. oder 4. Zyklus liegt, etwa 5–15 % in die aktuelle Expansionsphase hinein, was eine Zyklusdauer von $T \approx 105$–290 Gyr impliziert (einschließlich einer Korrektur für den Materieanteil).

Der Rahmen ist explizit phänomenologischer Natur. Eine kovariante Ableitung aus einer modifizierten Einstein-Hilbert-Wirkung, eine quantitative Reproduktion der akustischen CMB-Peaks und eine vollständige Behandlung unter Einbeziehung von Materie und Strahlung bleiben zukünftiger Arbeit vorbehalten. Wir identifizieren den Ruck-Parameter $j_0$ als den am leichtesten zugänglichen kurzfristigen observationellen Diskriminator zwischen EBC und $\Lambda$CDM.

---

## 1. Einleitung

### 1.1 Erfolge und offene Probleme des $\Lambda$CDM

Das Standardmodell der Kosmologie ($\Lambda$CDM) liefert eine quantitativ genaue Beschreibung des kosmischen Mikrowellenhintergrunds (CMB), der Großraumstruktur, der primordialen Nukleosynthese und der beschleunigten Expansion des Universums. Dennoch steht es vor mehreren grundlegenden konzeptuellen und empirischen Herausforderungen.

**Das Dunkle-Energie-Problem.** Etwa 68 % der gesamten Energiedichte des Universums werden der Dunklen Energie zugeschrieben, einer Komponente, deren physikalischer Ursprung völlig unbekannt bleibt. Die Quantenfeldtheorie sagt eine Vakuumenergie voraus, die den beobachteten Wert um 120 Größenordnungen übersteigt — das gravierendste Feinabstimmungsproblem der Physik [25].

**Die Hubble-Spannung.** Zwei unabhängige Bestimmungen der kosmischen Expansionsrate stimmen auf dem 4–5$\sigma$-Niveau nicht überein: der CMB-basierte Wert $H_0 \approx 67{,}4$ km/s/Mpc [Planck 2020] und der lokale Entfernungsleiter-Wert $H_0 \approx 73{,}0$ km/s/Mpc [Riess et al. 2022]. Diese Diskrepanz ist gegenüber bekannten systematischen Effekten robust und wird weitgehend als Hinweis auf Physik jenseits des Standardmodells betrachtet [22].

**DESI 2024.** Messungen von Baryonischen Akustischen Oszillationen durch das Dark Energy Spectroscopic Instrument zeigen Hinweise darauf, dass der Zustandsgleichungsparameter $w$ der Dunklen Energie nicht konstant bei $w = -1$ ist, wie es eine kosmologische Konstante erfordert [DESI Collaboration 2024]. Wenn dies mit höherer Signifikanz bestätigt wird, würde dies das $\Lambda$CDM-Bild grundlegend verändern.

**Das Inflationsproblem.** Die postulierte inflationäre Expansion des frühen Universums löst elegant die Horizont- und Flachheitsprobleme, wurde aber observationell nicht direkt bestätigt. Primordiale Gravitationswellen — die direkteste Signatur der Inflation — bleiben unentdeckt ($r < 0{,}036$, BICEP/Keck 2021), konsistent mit EBCs struktureller Vorhersage $r \approx 0$ (Abschnitt 6.2).

**Das Baryogeneseproblem.** Die standardmäßige elektroschwache Baryogenese erfordert eine CP-Verletzung der Größenordnung $\eta \sim 10^{-10}$, aber der CKM-Mechanismus liefert nur $\delta_\mathrm{CKM} \sim 10^{-20}$ — zehn Größenordnungen zu wenig.

### 1.2 Motivation und Umfang

Diese ungelösten Spannungen motivieren die Erkundung alternativer kosmologischer Rahmen. Die vorliegende Arbeit stellt die Elastische-Bounce-Kosmologie vor, die vier konzeptuelle Neuausrichtungen vorschlägt:

1. Kosmische Expansion als intrinsische geometrische Eigenschaft des Raums, nicht als Wirkung eines Vakuumenergiefeldes.
2. Zyklische Dynamik mit gedämpften Oszillationen statt monotoner Expansion.
3. Inflation als relativistisches Zeitdilatationsartefakt statt einer unabhängigen Feldphase.
4. Baryogenese als langsamer Akkumulationsprozess, verteilt über Zyklen.

Der Rahmen ist explizit phänomenologisch und ersetzt die Allgemeine Relativitätstheorie nicht auf fundamentaler Ebene. Er bietet eine qualitativ eigenständige alternative Perspektive und macht mehrere falsifizierbare Vorhersagen, die mit in naher Zukunft verfügbaren Instrumenten testbar sind.

### 1.3 Verwandte Arbeiten

Zyklische und Bounce-Kosmologien bilden ein aktives Forschungsgebiet. Die wesentlichen Vorläufer sind:

- **Schleifen-Quantenkosmologie** [19, 20]: Bounce verhindert durch Quantengravitationseffekte bei der Planck-Dichte.
- **Ekpyrotisches/Zyklisches Universum** [Steinhardt & Turok 2002, 2005]: Zyklen angetrieben durch extradimensionale Membrankollisionen.
- **Konforme Zyklische Kosmologie** [Penrose 2010]: Zyklen verbunden durch konforme Umskalierung mit Entropie-Reset.

EBC unterscheidet sich von allen dreien in seiner Behandlung der Dunklen Energie (neu interpretiert als dynamische räumliche Eigenschaft statt eines Feldes), seinem Mechanismus zur Vermeidung der Singularität (ein elastischer Bounce-Term in den Friedmann-Gleichungen statt Quantengravitation oder extra Dimensionen) und seiner phänomenologischen statt fundamentalen Ableitung. Entscheidend ist, dass EBC eine spezifische Zustandsgleichungs-Vorhersage ($w_0 = -2/3$) ableitet, die direkt gegen DESI-Daten testbar ist — ein Merkmal, das LQC [19, 20], CCC und dem ekpyrotischen Modell fehlt.

---

## 2. Das dynamische EBC-Modell

### 2.1 Konzeptuelles Fundament

Das zentrale Postulat ist, dass sich der Raum wie ein elastisches Medium mit einer charakteristischen Gleichgewichtsskala $a_*$ verhält. Kompression unterhalb von $a_*$ erzeugt eine abstoßende Rückstellkraft; Ausdehnung über $a_*$ hinaus erzeugt eine anziehende Rückstellkraft. Dies ist keine Kraft, die innerhalb des Raums wirkt, sondern eine geometrische Eigenschaft des Raums selbst — analog zum elastischen Modul eines kompressiblen Mediums. Die standardmäßige kosmologische Konstante $\Lambda$ wird als Grenzfall kleiner Amplitude dieser dynamischen Eigenschaft in der aktuellen Epoche ($a_0 \ll a_*$) neu interpretiert.

Zwei separate Postulate begleiten dies:

- **Externe Referenzzeit** ($\tau_\mathrm{ext}$): Die Oszillation des Raums verläuft gleichmäßig in einem externen Bezugssystem, unabhängig von der relativistischen Zeit innerhalb des Universums. Beobachter innerhalb des Universums, die in der frühen dichten Phase extremer gravitativer Zeitdilatation ausgesetzt sind, nehmen die anfängliche Expansion als enorm schnell wahr — was als Inflation erscheint. Dieses Postulat erweitert die Allgemeine Relativitätstheorie und ist das spekulativste Element des Rahmens; es erfordert formale Entwicklung (Abschnitt 8). Das Horizont- und das Flachheitsproblem, die die Inflation ursprünglich lösen sollte, werden in EBC durch die Bounce-Geometrie selbst gelöst, nicht durch dieses Postulat — siehe Abschnitt 4.8 für die detaillierte Argumentation.

- **Keine Singularität**: Der minimale Skalenfaktor $a_\mathrm{min} > 0$ ist ein explizites Postulat. Es gibt keine physikalischen Belege dafür, dass die Extrapolation $a \to 0$ einer physikalischen Realität entspricht.

### 2.2 Modifizierte Friedmann-Gleichungen

Der EBC-Rahmen modifiziert die Standard-Friedmann-Gleichungen, indem $\Lambda = \mathrm{const}$ durch zwei dynamische Terme ersetzt wird:

$$H^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2} + \frac{\Lambda_\mathrm{EBC}(a)}{3} + \frac{\Lambda_b(a)}{3} \tag{EBC1}$$

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}(\rho + 3p) + \frac{\Lambda_\mathrm{EBC}(a)}{3} + \frac{\Lambda_b(a)}{3} - \gamma H \tag{EBC2}$$

**Elastischer Rückstellterm** (treibt die Oszillation):
$$\Lambda_\mathrm{EBC}(a) = \Lambda_0\!\left(\frac{a_*}{a} - \frac{a}{a_*}\right)$$

**Bounce-Term** (verhindert Singularität):
$$\Lambda_b(a) = \Lambda_b\!\left(\frac{a_\mathrm{min}}{a}\right)^{\!4}$$

**Dämpfungsterm**: Die Dämpfung in EBC2 ist zustandsabhängig:
$$-\gamma(a)\,H, \quad \gamma(a) = \gamma_0\left|\frac{a - a_*}{a_*}\right|$$
Diese Form verschwindet bei der Gleichgewichtsskala $a_*$ und ist am größten weit vom Gleichgewicht entfernt. Sie kodiert das physikalische Bild, dass die Energiedissipation in die Strukturbildung (Sterne, Galaxien, Cluster) während der stark nichtäquilibrierten Kompressions- und Expansionsphasen am effizientesten ist und abnimmt, wenn sich das System seinem Ruhezustand nähert. Im Grenzfall $a \ll a_*$ (aktuelle Epoche) vereinfacht sich dies zu $\gamma(a) \approx \gamma_0$, was eine nahezu konstante effektive Dämpfungsrate ergibt. Die Wahl dieser funktionalen Form ist durch Einfachheit und physikalische Intuition motiviert; alternative Dämpfungsvorschriften sind möglich und würden die detaillierte Zyklusevolution modifizieren, ohne das analytische $w_\mathrm{EBC}$-Ergebnis aus Abschnitt 2.5 zu beeinflussen.

### 2.3 Physikalische Eigenschaften des elastischen Terms

Der elastische Term $\Lambda_\mathrm{EBC}(a)$ zeigt qualitativ unterschiedliches Verhalten in verschiedenen Epochen:

| Epoche                          | $a$ relativ zu $a_*$ | $\Lambda_\mathrm{EBC}$  | Physikalische Konsequenz         |
|---------------------------------|-----------------------|-------------------------|----------------------------------|
| Frühe Expansion (aktuell) | $a \ll a_*$ | $\approx +\Lambda_0 a_*/a > 0$ | Beschleunigte Expansion (Dunkle Energie) |
| Expansionsmaximum | $a = a_*$ | $= 0$ | Wendepunkt, Ende der Beschleunigung |
| Jenseits des Maximums | $a > a_*$ | $< 0$ | Kontraktion |
| Nahe Bounce | $a \to a_\mathrm{min}$ | $\Lambda_b$ dominiert $\to +\infty$ | Elastischer Bounce, keine Singularität |

### 2.4 Normierung und Parameterreduktion

Bei der aktuellen Epoche $a = a_0$ muss der elastische Term die beobachtete Dunkle-Energie-Dichte reproduzieren:

$$\Lambda_\mathrm{EBC}(a_0) \approx \Lambda_\mathrm{obs} \approx 1{,}1 \times 10^{-52}\ \mathrm{m}^{-2}$$

Für $a_0 \ll a_*$ ergibt sich:

$$\Lambda_0 \approx \Lambda_\mathrm{obs} \cdot \frac{a_0}{a_*} = \Lambda_\mathrm{obs} \cdot f_\mathrm{Zyklus}$$

wobei $f_\mathrm{Zyklus} = t_0/T$ die Bruchposition innerhalb des aktuellen Zyklus ist, unabhängig aus der $H_0 \cdot t_0$-Bedingung in Abschnitt 5.2 abgeschätzt ($f_\mathrm{Zyklus} \approx 0{,}06$–$0{,}15$). Bei einer solchen unabhängigen Schätzung von $f_\mathrm{Zyklus}$ ist $\Lambda_0$ kein freier Parameter, sondern eine abgeleitete Größe:

$$\Lambda_0 \approx (0{,}6\text{–}1{,}7) \times 10^{-53}\ \mathrm{m}^{-2}$$

Es sei darauf hingewiesen, dass $f_\mathrm{Zyklus}$ und $T$ genuinen unabhängige Unbekannte sind, die durch separate Observablen ($H_0$, $t_0$, $q_0$) eingeschränkt werden, sodass diese Normierung keine Zirkularität einführt.

### 2.5 Effektive Zustandsgleichung

Unter Verwendung der EBC-Dunkle-Energie-Dichte $\rho_\mathrm{EBC} = \Lambda_\mathrm{EBC}/(8\pi G)$ und Anwendung der Kontinuitätsgleichung:

$$\dot{\rho}_\mathrm{EBC} + 3H(1 + w_\mathrm{EBC})\rho_\mathrm{EBC} = 0$$

Wir behandeln $\rho_\mathrm{EBC}$ als effektive Fluidkomponente; dies ist formal analog zur Standardbehandlung der kosmologischen Konstante als Vakuumenergie und ist auf dem Hintergrundniveau selbstkonsistent, da $\Lambda_\mathrm{EBC}(a)$ nur vom homogenen Hintergrunds-Skalenfaktor abhängt und die Bianchi-Identität innerhalb des FRW-Rahmens nicht verletzt (die modifizierten Friedmann-Gleichungen (EBC1)–(EBC2) bleiben per Konstruktion gegenseitig konsistent). Eine kovariante Verallgemeinerung über FRW hinaus bleibt zukünftiger Arbeit vorbehalten (Abschnitt 8, Punkt 1).

$$w_\mathrm{EBC} = -1 - \frac{1}{3}\frac{d\ln\Lambda_\mathrm{EBC}}{d\ln a}$$

Für $\Lambda_\mathrm{EBC}(a) = \Lambda_0(a_*/a - a/a_*)$, mit $x = a/a_*$:

$$\boxed{w_\mathrm{EBC}(x) = -1 + \frac{1 + x^2}{3(1 - x^2)}}$$

Im aktuellen Beobachtungsregime $x = a_0/a_* \ll 1$:

$$w_0 \equiv w_\mathrm{EBC}(a_0) \approx -\frac{2}{3} \approx -0{,}667$$

Dies ist eine Vorhersage des Modells, die **einzig aus der $1/a$-Skalierung des elastischen Terms** im Grenzfall $a_0 \ll a_*$ folgt: weder $\Lambda_0$ noch $a_*$ müssen abgestimmt werden, um $w_0 \approx -2/3$ zu reproduzieren. Es sei darauf hingewiesen, dass der vollständige EBC-Rahmen weitere Parameter enthält ($a_*$, $\gamma_0$, $\Lambda_b$, $a_\mathrm{min}$), die durch andere Observablen eingeschränkt werden. Der Anspruch der Parameterfreiheit gilt spezifisch für die $w_0$-Vorhersage, nicht für das Modell als Ganzes.

Die DESI-2024-BAO-Messung $w_0 = -0{,}70 \pm 0{,}10$ [8] stimmt mit dieser Vorhersage auf dem $1\sigma$-Niveau überein. Diese Ergebnisse wurden noch nicht durch einen unabhängigen Datensatz bestätigt und sollten als vorläufige Motivation, nicht als definitiver Beweis betrachtet werden. Die physikalische Interpretation: Die effektive EBC-Dunkle-Energie skaliert in der aktuellen Epoche als $\rho_\mathrm{EBC} \propto a^{-1}$, was $w = -2/3$ ergibt — formal äquivalent zu einem Netzwerk topologischer Domänenwände.

**Zeitliche Entwicklung von $w$**: Wenn $x$ von 0 gegen 1 ansteigt (das Expansionsmaximum), steigt $w_\mathrm{EBC}$ monoton von $-2/3$ in Richtung 0 und darüber hinaus. In der CPL-Parametrisierung $w(a) = w_0 + w_a(1-a)$:

$$w_a \approx -\frac{8}{3} \cdot \frac{a_0}{a_*^2} < 0$$

Dies sagt vorher, dass $w$ in der Vergangenheit negativer war — qualitativ konsistent mit dem DESI-Trend ($w_a < 0$).

---

## 3. Numerische Illustration

### 3.1 Aufbau

Wir integrieren die Gleichungen (EBC1)–(EBC2) im materiefreien Grenzfall ($\rho = p = 0$, $k = 0$), unter Verwendung dimensionsloser Variablen $x = a/a_*$ und $\tau = t\sqrt{\Lambda_0/3}$. Mit der zustandsabhängigen Dämpfung $\gamma(a) = \gamma_0|a/a_* - 1|$ aus Abschnitt 2.2 vereinfacht sich das System zu:

$$x'' + \tilde{\gamma}|x - 1|\,x' = K\!\left(\frac{1}{x^2} - x\right) + K_b\left(\frac{x_\mathrm{min}}{x}\right)^{\!4} x$$

Dies ist konsistent mit (EBC2): Der Term $\tilde{\gamma}|x-1|x'$ entspricht $\gamma(a)H$ in dimensionsloser Form, verschwindet im Gleichgewicht ($x=1$) und wächst mit der Auslenkung.

mit dimensionslosen Parametern $K$, $K_b = \Lambda_b/\Lambda_0$, $\tilde{\gamma} = \gamma/\sqrt{\Lambda_0/3}$ und $x_\mathrm{min} = a_\mathrm{min}/a_*$.

Für die Illustration verwendete numerische Werte: $x_\mathrm{min} = 0{,}01$, $K_b = 0{,}005$, $\tilde{\gamma} = 1{,}5 \times 10^{-3}$. Integration mittels Runge-Kutta-Verfahren vierter Ordnung (scipy `solve_ivp`, `RK45`, $\mathrm{rtol} = 10^{-10}$, $\mathrm{atol} = 10^{-13}$).

### 3.2 Ergebnisse

![Abb. 1a](EBC_fig1a_final.pdf){ width=100% }
![Abb. 1b](EBC_fig1b_final.pdf){ width=100% }

Die Integration demonstriert (Abb. 1):

- Starke anfängliche Beschleunigung vom Bounce-Minimum.
- Wiederholte Expansions-Kontraktions-Phasen mit langsam abnehmender Amplitude.
- Erstes Expansionsmaximum bei $x_\mathrm{max} \approx 1{,}73$.
- Zyklusdauer über frühe Zyklen hinweg annähernd konstant ($\Delta\tau \approx 4{,}87$).
- Das Bounce-Minimum steigt durch Dämpfung langsam mit jedem Zyklus ($x_\mathrm{min,k} \nearrow$), konsistent mit gradueller Strukturerhaltung.

Die Markierung der „aktuellen Epoche" ist zu Beginn des 3. Zyklus gesetzt, bei etwa 6–10 % der Zyklusdauer. Ein Hinweis zum Maßstab dieser Illustration: Das illustrative Bounce-Minimum dieser Integration liegt bei $x_\mathrm{bounce} \approx 0{,}515$, bestimmt durch Energieerhaltung des elastischen Terms für $x_\mathrm{max} \approx 1{,}73$. Der Bounce-Term-Parameter $x_\mathrm{min} = 0{,}01$ dient als Singularitätsschutz und ist für diese Trajektorie nicht aktiv. Das physikalische Verhältnis $a_0/a_* \approx 0{,}06$–$0{,}15$ (Abschnitt 5) ist viel kleiner als das illustrative Bounce-Minimum, konsistent damit, dass die aktuelle Epoche sehr früh in ihrem Zyklus liegt. Die analytisch abgeleitete Zustandsgleichung $w_\mathrm{EBC} \approx -2/3$ gilt im Grenzfall $a_0/a_* \ll 1$ (Abschnitt 2.5) und ist unabhängig vom illustrierten Maßstab.

**Wichtiger Vorbehalt**: Diese numerische Illustration lässt Materie und Strahlung aus. Die Zykluspositionsschätzung von 6–15 % (Abschnitt 5) und die Markierung der „aktuellen Epoche" in Abb. 1 sind daher nur illustrativ — sie repräsentieren den materiefreien Grenzfall und sollten nicht als quantitative Vorhersagen aufgefasst werden. Die Einbeziehung von Standardmaterie ($\Omega_m \approx 0{,}31$) und Strahlung wird sowohl die Zyklusdauer als auch die Positionsschätzung modifizieren; dies ist als Entwicklungspunkt 3 in Abschnitt 8 identifiziert.

**Größenordnungsschätzungen der Korrekturen.** Obwohl die vollständige numerische Integration mit Materie und Strahlung zurückgestellt wird, können die führenden Korrekturen analytisch abgeschätzt werden. Materie tritt in (EBC2) als zusätzlicher anziehender Term $-4\pi G \rho_m/3$ ein, der die frühe Expansion verzögert, aber nahe dem Expansionsmaximum vernachlässigbar bleibt (wo $\rho_m \propto a_*^{-3}$ stark verdünnt ist). Das Verhältnis der Materiedichte zum EBC-Rückstellterm heute beträgt $\Omega_m/\Omega_\mathrm{EBC} \approx 0{,}31/0{,}69 \approx 0{,}45$; dieses Verhältnis wächst als $a^{-3}$ in die Vergangenheit, was Materie in der frühen Phase jedes Zyklus dominant macht. Eine grobe Schätzung ergibt einen Korrekturfaktor von ungefähr:

$$\frac{T_\text{mit Materie}}{T_\text{materiefrei}} \approx 1 + C \cdot \frac{\Omega_m}{\Omega_\mathrm{EBC}} \approx 1{,}15\text{–}1{,}25$$

wobei $C \approx 0{,}4$–$0{,}5$ der Tatsache Rechnung trägt, dass Materie nur in der frühen Phase jedes Zyklus relevant ist. Die Zyklusdauerschätzung erhöht sich daher um etwa **15–25 %**: von $T \approx 90$–230 Gyr auf $T \approx 105$–290 Gyr. Entsprechend verschiebt sich die Zyklusposition $f = t_0/T$ um eine ähnliche Fraktion nach unten, von 6–15 % auf etwa **5–13 %** — qualitativ unverändert, aber zum unteren Ende des aktuellen Bereichs hin. Das Expansionsmaximum $x_\mathrm{max} \approx 1{,}73$ ändert sich um weniger als 5 %, da Materie dort vernachlässigbar ist. Nahe dem Bounce liefert Strahlung ($\rho_r \propto a^{-4}$) einen bescheidenen zusätzlichen abstoßenden Beitrag, der $x_\mathrm{min}$ leicht erhöht, konsistent mit der Bounce-Temperaturschätzung in Abschnitt 6.2. Entscheidend ist, dass die analytische Vorhersage $w_0 = -2/3$ (Abschnitt 2.5) vollständig unabhängig von der numerischen Integration ist und durch die Einbeziehung von Materie und Strahlung nicht beeinflusst wird.

---

## 4. Observationelle Vergleiche

### 4.1 Beschleunigte Expansion und DESI 2024

Die aktuell beobachtete beschleunigte Expansion ($q_0 \approx -0{,}55$) ist vollständig konsistent mit dem EBC-Modell: Wir befinden uns in der frühen Aufstiegsphase eines Zyklus (geschätzte 5–13 %, einschließlich der in Abschnitt 3.2 abgeleiteten Korrektur für den Materiegehalt), wo der elastische Rückstellterm positive Beschleunigung antreibt. Die Beschleunigung wird enden, wenn das Expansionsmaximum $a_*$ erreicht ist, mehrere zehn Milliarden Jahre in der Zukunft.

Die DESI-2024-BAO-Ergebnisse ($w_0 \approx -0{,}7$, $w_a \approx -0{,}65$, $2{,}5$–$3{,}9\sigma$ von $\Lambda$CDM entfernt) liefern observationelle Motivation für dynamische Dunkle-Energie-Modelle einschließlich EBC. Die Vorhersage des Modells $w_0 \approx -2/3$ liegt innerhalb des DESI-$1\sigma$-Intervalls. Diese Ergebnisse müssen noch durch unabhängige Datensätze bestätigt werden; $\Lambda$CDM ist noch nicht ausgeschlossen, und die DESI-Spannung kann zum Teil systematische Effekte widerspiegeln. EBC wird daher als ein mit aufkommenden Daten konsistenter Rahmen präsentiert, nicht als einer, der durch sie bestätigt wird.

### 4.2 Hubble-Spannung

Der EBC-Rahmen bietet eine mögliche Interpretation der $H_0$-Diskrepanz: Wenn das Universum mehrere Zyklen durchlaufen hat, werden sich leichte geometrische Verformungen durch interne Dynamik (Strukturbildung, Gravitationsinstabilitäten) angesammelt haben, was zu räumlich variierenden lokalen Expansionsraten führt. Das CMB-basierte $H_0$ misst einen großräumigen Durchschnitt; lokale Entfernungsleiter-Messungen erfassen ein kleineres Volumen, das sich systematisch unterscheiden kann. Diese Interpretation ist qualitativ und erfordert quantitative Entwicklung.

### 4.3 CMB-Anomalien

Der CMB zeigt mehrere statistisch signifikante Anomalien, die innerhalb von $\Lambda$CDM nicht erklärt werden:

- **Quadrupolausrichtung** („Achse des Bösen"): Die niedrigsten Multipolmomente sind anomal ausgerichtet [21, 28].
- **Kalter Fleck** im Eridanus: Statistisch signifikante kalte Region ohne Standarderklärung [26].
- **Anomale Massenströmungen**: Kohärente Galaxienhaufenbewegungen auf Gpc-Skalen, die erwartete Amplituden überschreiten [27].

Im EBC-Rahmen liefern geometrische Asymmetrien, die sich über Zyklen angesammelt haben, einen natürlichen Ursprung für diese Merkmale. Der aktuelle Zyklus muss nicht perfekt kugelförmig-symmetrisch sein; Restverformungen aus vorherigen Zyklen sind physikalisch zu erwarten.

### 4.4 Das Lithium-7-Problem

Standard-BBN sagt Li/H $\approx (3\text{–}4) \times 10^{-10}$ voraus, während Beobachtungen alter metallarmer Sterne Li/H $\approx 1{,}6 \times 10^{-10}$ ergeben — eine Diskrepanz um einen Faktor $\sim 2$–3 [Cyburt et al. 2016].

EBC bietet einen physikalischen Mechanismus: **selektive nukleare Photodisintegration beim Bounce**. Verschiedene Nuklide haben unterschiedliche Photodisintegrationsschwellen:

**Tabelle 1: Photodisintegrationstemperaturen wichtiger Nuklide**

| Nuklid | Photodisintegrationstemperatur |
|--------|-------------------------------|
| Li-7 | $\approx 3$–$5 \times 10^9$ K |
| Deuterium | $\approx 6 \times 10^9$ K |
| He-4 | $\approx 2 \times 10^{10}$ K (wesentlich stabiler) |

Wenn die Bounce-Temperatur $T_\mathrm{bounce} \approx T_\mathrm{CMB} \cdot (a_0/a_\mathrm{min})$ im Bereich $\sim 10^9$–$10^{10}$ K liegt, wird Li-7 photodisintegriert, während He-4 überlebt. BBN im nachfolgenden Zyklus beginnt dann unter He-4-angereicherten Bedingungen und produziert weniger Li-7.

Dieser Mechanismus liefert eine korrelierte Doppelvorhersage: (a) Li-7/H unterhalb des Standard-BBN-Werts (beobachtet, konsistent), und (b) He-4-Massenanteil $Y_p$ leicht über $0{,}2470$ aufgrund des He-4-Samens, der den Bounce überlebt. Aktuelle Messung: $Y_p = 0{,}2449 \pm 0{,}0040$ [Aver et al. 2015]. Der Zentralwert liegt unterhalb der vorhergesagten Schwelle von $0{,}2470$, was die EBC-Vorhersage außerhalb des $1\sigma$-Bereichs platziert — dies stellt eine echte Spannung dar, keine Bestätigung. Es könnte darauf hindeuten, dass die Bounce-Temperatur näher an der He-4-Photodisintegrationsschwelle liegt als modelliert, oder dass die $Y_p$-Messung mit hochpräziseren Daten verschoben wird. Zukünftige JWST-Spektroskopie metallreicher HII-Regionen bei hoher Rotverschiebung wird entscheidend sein. Bemerkenswert ist, dass das Li-7-Defizit und die erhöhte $Y_p$-Vorhersage aus demselben Mechanismus resultieren und gemeinsam testbar sind, was die Unterscheidungskraft einer zukünftigen kombinierten Messung maximiert.

### 4.5 Baryogenese

Das Standardmodell der elektroschwachen Baryogenese scheitert quantitativ: Die CKM-CP-Verletzung ist $\sim 10^{10}$ Mal zu klein, um die beobachtete Baryonasymmetrie $\eta \approx 6{,}09 \times 10^{-10}$ zu erzeugen [Sakharov-Bedingungen]. Dies ist eines der genuinen ungelösten Probleme des Standardmodells.

**Die Rolle der Bounce-Temperatur.** Eine zentrale Einschränkung regelt die Baryogenese in jedem zyklischen Modell: Baryonenzahl-verletzende Prozesse (elektroschwache Sphalerone) sind nur oberhalb der elektroschwachen Skala ($T \gtrsim 100$ GeV) aktiv und darunter exponentiell unterdrückt. Die aktuelle EBC-Bounce-Temperatur von $T_\mathrm{bounce} \approx 4 \times 10^9$ K $\approx 0{,}3$ MeV liegt etwa fünf Größenordnungen unterhalb dieser Schwelle. Sphalerongetriebene Baryogenese beim Bounce ist daher in den aktuellen oder jüngsten Zyklen nicht verfügbar. Entsprechend bleibt die netto Baryonasymmetrie $\eta$ als thermisches Relikt durch jeden Bounce erhalten — der Bounce thermalisiert baryonische Strukturen, verletzt aber keine Baryonenzahl, konsistent mit dem physikalischen Bild aus Abschnitt 4.7.

**Zeitdruckentlastung.** Der zentrale Beitrag von EBC zum Baryogeneseproblem ist kein neuer Produktionsmechanismus beim Bounce, sondern eine dramatische Entspannung der Zeitbeschränkung. Mechanismen wie Leptogenese durch schwere Neutrinozerfälle oder der Affleck-Dine-Mechanismus erfordern keine Sphalerontemperaturen; sie benötigen nur ausreichend Zeit und eine bescheidene CP-verletzende Rate. Im Standardmodell beträgt das gesamte verfügbare Zeitfenster $\sim 13{,}8$ Gyr. In EBC steht die gesamte Zyklusdauer von $T \approx 200$ Gyr zur Verfügung, was eine erforderliche durchschnittliche Produktionsrate von folgendem ergibt:

$$\frac{d\eta}{dt} \approx \frac{6 \times 10^{-10}}{200 \times 10^9\ \mathrm{yr}} \approx 3 \times 10^{-21}\ \mathrm{yr}^{-1}$$
Diese Rate ist für Leptogenese via schwere Neutrinos oder Affleck-Dine-Mechanismen erreichbar, die im Standardmodell nicht wegen prinzipieller Unmöglichkeit, sondern wegen Zeitdruck scheitern. Dasselbe Argument gilt über mehrere Zyklen: $\eta$ akkumuliert sich graduell innerhalb jedes Zyklus während der heißen frühen Phase, wenn baryonenzahlverletzende Prozesse am aktivsten sind, und wird dann unversehrt durch den Bounce in den nächsten Zyklus überführt.

**Die beobachtete $\eta$ als kumulatives Relikt.** Die beobachtete Asymmetrie $\eta \approx 6{,}09 \times 10^{-10}$ ist daher das kumulative Ergebnis langsamer Baryogenese über mehrere Zyklen hinweg. Als grober Durchschnitt trägt jeder der $N = 3$ Zyklen $\delta\eta \approx \eta/N \approx 2 \times 10^{-10}$ bei — obwohl der Beitrag in der Praxis auf die heiße frühe Phase jedes Zyklus konzentriert war (wenn baryonenzahlverletzende Prozesse am aktivsten waren) und nicht gleichmäßig über die Zeit verteilt war. Die in Abschnitt 5.4 beschriebene langfristige thermische Evolution impliziert, dass die heißesten, frühesten Zyklen überproportional beigetragen haben; die aktuellen und jüngsten Zyklen tragen aufgrund ihrer sub-MeV-Bounce-Temperaturen vernachlässigbar bei. Dieses Bild ist vollständig konsistent mit Abschnitt 4.7: Genau wie Schwarze Löcher und Alpha-Elemente den Bounce physikalisch überleben, überlebt die netto Baryonasymmetrie ihn thermodynamisch als erhaltene Ladung.

EBC löst das Baryogeneseproblem nicht, sondern formuliert es neu: Die Frage ist nicht, wie $\eta$ in 13,8 Gyr unter extremem Zeitdruck produziert wurde, sondern wie eine kleine CP-verletzende Rate über zwei vollständige Zyklen von je $\sim 200$ Gyr operierte — ein wesentlich weniger eingeschränktes Problem, das für bekannte Erweiterungen des Standardmodells zugänglich ist.

### 4.6 Großräumige Strukturanomalien

Die **Herkules-Corona-Borealis-Große-Mauer** ($\sim 3$ Gpc bei $z \approx 2$) wurde als etwa zehnmal so groß wie die theoretische Maximalgröße kosmischer Strukturen in $\Lambda$CDM berichtet und wäre in 13,8 Gyr schwer zu bilden. Wir weisen darauf hin, dass die statistische Signifikanz dieser Struktur in der Literatur diskutiert wurde und ihre Realität als einzelne kohärente Struktur nicht allgemein akzeptiert wird [vgl. z.B. [29] und nachfolgende Kritiken]. Wenn bestätigt, wäre sie eine natürliche Reliktstruktur im zyklischen Modell mit $N \geq 3$ Zyklen.

**Primodiale Magnetfelder in intergalaktischen Leerräumen** ($\sim 10^{-16}$–$10^{-15}$ G, Fermi-LAT [23]) sind in $\Lambda$CDM unerklärlich. Im zyklischen Modell könnten sie Reliktfelder sein, die sich über mehrere Zyklen angesammelt haben.

### 4.7 Transzykliche Erbschaft: Schwarze-Loch-Keime, chemische Anreicherung und die JWST-Anomalie

*Der folgende Abschnitt entwickelt eine spekulative, aber intern konsistente Erweiterung des EBC-Rahmens und erkundet qualitative Konsequenzen des Bounce-Filter-Mechanismus über mehrere Zyklen hinweg. Er bildet keinen Teil des minimalen mathematischen Kerns von EBC und sollte als Sammlung motivierter Vermutungen und nicht als abgeleitete Ergebnisse gelesen werden.*

Eine distinctive und weitgehend unerforschte Konsequenz der zyklischen Struktur von EBC ist die **Akkumulation kompakter Relikte über Zyklen hinweg**. Der Bounce bei $T_\mathrm{bounce} \approx 4 \times 10^9$ K wirkt als selektiver physikalischer Filter (Abschnitt 4.4): Gewöhnliche Sterne, Gaswolken und leichte Nuklide werden vollständig thermalisiert, während kompakte Objekte, deren interne Energieskalen weit über der Bounce-Temperatur liegen, unberührt passieren.

**Der Bounce-Filter nach Objektklasse.** Stellare Schwarze Löcher verdampfen durch Hawking-Strahlung [30] auf Zeitskalen der Größenordnung $10^{67}$ Jahre — ungefähr $10^{55}$ Zyklusdauern. Supermassive Schwarze Löcher ($M \sim 10^9$–$10^{11}\ M_\odot$) bestehen für $\sim 10^{100}$ Jahre. Neutronensterne überleben auf ähnlichen Zeitskalen. Dunkle-Materie-Halos interagieren nur gravitativ und werden durch den Bounce lediglich komprimiert und wieder ausgedehnt. Alle diese Objekte überleben jeden Bounce im Wesentlichen massenunverändert, während normale baryonische Struktur vollständig zurückgesetzt wird.

**Zyklus 1 ($T \approx 200$ Gyr).** Beginnend mit einem reinen H/He-Gas mit nahezu null Baryonasymmetrie und ohne vorhandene Struktur hat der erste Zyklus die gesamte Zyklusdauer, um ungehindert Komplexität aufzubauen. Population-III-Sterne — massiv, metallfrei, mit Lebensdauern von $10^6$–$10^7$ Jahren — bilden sich und explodieren als Supernovae innerhalb der ersten paar hundert Millionen Jahre, bereichern das intergalaktische Medium mit C, N, O, Si und Fe und hinterlassen stellare Schwarze Löcher als Überreste. Über $\sim 200$ Gyr verschmelzen diese stellaren Schwarzen Löcher hierarchisch durch aufeinanderfolgende Galaxienhaufenkollisionen und produzieren supermassive Schwarze Löcher, die $M \gtrsim 10^{11}\ M_\odot$ erreichen — weit massereicher als die heute bei hoher Rotverschiebung beobachteten $\sim 10^9\ M_\odot$-Objekte. Galaktische Dynamos verstärken schwache Saatmagnetfelder über Milliarden von Jahren in Zyklus 1; in Leerraumregionen, wo keine nachfolgende Dynamoaktivität sie zerstören kann, überleben diese Felder den Bounce als verdünnte Relikte in Zyklus 2 und darüber hinaus. Die beobachteten $\sim 10^{-16}$–$10^{-15}$ G intergalaktischen Leerraumfelder (Fermi-LAT [23]) sind konsistent damit, genau solche Zyklus-1-Relikte zu sein.

**Zyklus 2 ($T \approx 180$ Gyr, leicht gedämpft).** Das sich wieder ausdehnende Universum von Zyklus 2 ist kosmologisch nicht mehr unberührt. Es erbt von Zyklus 1: (i) eine Population von Schwarzen Löchern, die stellare bis supermassive Massen überspannt, verteilt durch die sich neu bildende Großraumstruktur; (ii) ein Dunkle-Materie-Netz aus Filamenten und Halos, das sich nie aufgelöst hat und ein sofortiges gravitatives Gerüst bereitstellt; (iii) ein chemisches Inventar, dominiert von He-4 (Bounce-Überlebender), schwereren Alpha-Elementen (O, Si, Fe; Bounce-Überlebende) und im Wesentlichen null Li-7 oder Deuterium (bounce-zerstört). Die Sternbildung in Zyklus 2 ist gegenüber Zyklus 1 beschleunigt: Vorhandene SL-Keime ermöglichen schnellen Aufbau aktiver galaktischer Kerne, und das vorhandene DM-Gerüst führt Baryonen schneller in Halos als in einem strukturell leeren Universum.

**Die JWST-Anomalie als transzykliche Vorhersage.** Das James-Webb-Weltraumteleskop hat massive, entwickelte Galaxien und aktive supermassive Schwarze Löcher bei Rotverschiebungen $z > 10$ [31] enthüllt — entsprechend weniger als 500 Myr nach dem Urknall im $\Lambda$CDM-Rahmen — die durch Standard-Strukturbildung innerhalb einer einzelnen 13,8-Gyr-Expansionsgeschichte schwer zu erklären sind. Diese Beobachtungen werden noch aktiv diskutiert, und einige könnten innerhalb erweiterter $\Lambda$CDM-Modelle erklärbar sein. EBC bietet einen natürlichen Rahmen für ihr Verständnis: Die bei $z > 10$ in Zyklus 3 beobachteten supermassiven Schwarzen Löcher sind konsistent damit, direkte Nachfolger der während der Zyklen 1 und 2 assemblierten SL-Population zu sein, die zu Beginn von Zyklus 3 als vorgeformte Saatobjekte vorhanden waren und nicht von Grund auf innerhalb von 13,8 Gyr gewachsen sind. Dies stellt eine qualitative, falsifizierbare Vorhersage dar: Die Massenfunktion und Spinverteilung der hochrotverschobenen ($z > 10$) Schwarzen Löcher sollten einen charakteristischen Boden zeigen — eine Mindestmasse, die durch die typische SL-Masse am Ende von Zyklus 2 gesetzt wird — anstatt der kontinuierlichen Bottom-up-Wachstumsverteilung, die in $\Lambda$CDM erwartet wird.

**Chemischer Abdruck auf ultra-metallarmen Sternen.** Der EBC-Bounce-Filter sagt auch eine spezifische chemische Signatur in den metallärmsten Sternen von Zyklus 3 voraus. Sterne, die ganz am Anfang von Zyklus 3 in Regionen bilden, die noch nicht von Zyklus-2-Supernovaauswürfen erreicht wurden, sollten das charakteristische Bounce-Filter-Muster zeigen: normales oder erhöhtes O, Si und Fe (Alpha-Elemente, die den Bounce überleben), und anomal unterdrücktes Li, Be und B (beim Bounce zerstört). Dieses Muster ist qualitativ distinct von Standard-Population-III-Supernovaausbeuten und gemeinsam mit JWST-Spektroskopie von extrem metallarmen $z > 5$-Sternen testbar.

Eine Zusammenfassung der transzyklichen Erbschaft ist in Tabelle 2 gegeben.

**Tabelle 2: Transzykliche Erbschaft im EBC-Rahmen ($N = 3$)**

```{=latex}
\rowcolors{2}{gray!12}{white}
```

| Ererbte Größe                  | Ursprung                         | Zyklus-3-Beobachtungskandidat    |
|--------------------------------|----------------------------------|----------------------------------|
| Supermassive SL-Keime | Zyklisches SL-Wachstum (Z1+Z2) | JWST: massive SL bei $z > 10$ |
| Relikt-Leerraummagnetfelder | Zyklus-1-galaktische Dynamos | Fermi-LAT: $\sim 10^{-16}$ G in Leerräumen |
| Vorgeformtes DM-Gerüst | DM-Halos (Z1+Z2) | Frühe Großraumstruktur |
| He-4-Überabundanz ($Y_p$) | Zwei Bounce-Filter | $Y_p > 0{,}2470$ (Vorhersage) |
| Li-7-Defizit | Zwei Bounce-Destruktionen | Kosmologisches Lithiumproblem |
| Bounce-Filter-Elementmuster | Alpha-Element-Überleben | UMP-Sterne bei $z > 5$ (JWST) |

```{=latex}
\rowcolors{0}{}{}
```

### 4.8 Horizont- und Flachheitsproblem

Die Standardkosmologie erfordert eine inflationäre Phase, um zwei anderweitig fein abgestimmte Beobachtungen zu erklären: die nahezu perfekte Isotropie des CMB über Regionen hinweg, die kausal getrennt erscheinen (Horizontproblem), und die nahezu exakte räumliche Flachheit des Universums ($|\Omega - 1| < 0{,}01$, Flachheitsproblem). EBC löst beide durch seine dynamische Struktur, ohne ein Inflatonfeld zu postulieren.

**Horizontproblem.** In der Standard-Urknallkosmologie stammten die CMB-Photonen, die aus entgegengesetzten Himmelsrichtungen ankommen, aus Regionen, deren Lichtkegel sich zum Zeitpunkt der letzten Streuung nicht überlappt haben — sie waren nie in kausalem Kontakt, und doch stimmen ihre Temperaturen auf einen Teil in $10^5$ überein. Inflation löst dies durch exponentielle Streckung einer kleinen, kausal verbundenen Region, um das gesamte beobachtbare Universum zu umfassen.

In EBC ist die Auflösung direkter und folgt aus der Bounce-Bedingung selbst. Am Bounce-Minimum $a = a_\mathrm{min}$ gilt per Definition $\dot{a} = 0$, und daher ist der Hubble-Parameter $H = \dot{a}/a = 0$. Der Hubble-Radius $d_H = c/|H| \to \infty$ beim Bounce: Das gesamte Universum liegt zu diesem Zeitpunkt innerhalb eines einzigen kausalen Volumens. Jede Region des beobachtbaren Universums war daher beim Bounce in kausalem Kontakt, unabhängig davon, wie groß das Universum in der vorhergehenden Expansionsphase gewachsen war. CMB-Isotropie ist keine Feinabstimmungskoinzidenz, sondern eine direkte Konsequenz der zyklischen Struktur — das Universum wurde bei jedem Bounce auf eine gemeinsame Temperatur thermalisiert, und diese thermische Erinnerung persistiert in die nachfolgende Expansion. Dieses Argument ist stärker als die bloße Feststellung, dass Regionen während der Kontraktionsphase in Kontakt waren: Die Divergenz des kausalen Horizonts bei $H = 0$ ist ein universelles Merkmal jedes nicht-singulären Bounces, unabhängig von den Details des EBC-Potentials.

**Flachheitsproblem.** Der Dichteparameter $\Omega = \rho/\rho_\mathrm{krit}$ erfüllt:
$$\Omega - 1 = \frac{kc^2}{a^2 H^2}$$
wobei $k$ die Raumkrümmung ist. In der Standardkosmologie gilt $(\Omega - 1) \propto a^2$ während Materiedominanz und $\propto a$ während Strahlungsdominanz — beide wachsen mit $a$, was $\Omega = 1$ zu einem instabilen Fixpunkt macht. Jede anfängliche Abweichung von der Flachheit wächst mit der Zeit, was extreme Feinabstimmung des frühen Universums erfordert, um das beobachtete $|\Omega_0 - 1| < 0{,}01$ zu erklären.

Während der EBC-Kontraktionsphase kehrt sich die Entwicklung um. Aus der Friedmann-Gleichung gilt $H^2 \propto \rho$, also $a^2 H^2 \propto a^2 \rho$. Für Materiedominanz ($\rho \propto a^{-3}$) ergibt das $a^2 H^2 \propto a^{-1}$, und daher:
$$(\Omega - 1) = \frac{kc^2}{a^2 H^2} \propto a \to 0 \quad \text{für } a \to a_\mathrm{min}$$
Für Strahlungsdominanz ($\rho \propto a^{-4}$) gilt $a^2 H^2 \propto a^{-2}$, also $(\Omega - 1) \propto a^2 \to 0$ sogar noch schneller. Jede anfängliche Krümmung, ob positiv oder negativ, wird während der Kontraktionsphase dynamisch gegen null getrieben — $\Omega = 1$ wird zu einem **Attraktor** statt zu einem instabilen Fixpunkt. Dies ist ein allgemeines Merkmal kontrahierender Kosmologien und gilt direkt für EBC: Jede Kontraktionsphase setzt die Krümmung in Richtung Flachheit zurück, ohne anfängliche Feinabstimmung zu erfordern. Nach $N = 3$ Zyklen aus Kontraktion und Expansion wird die Restabweichung von der Flachheit durch wiederholte Anwendung dieses Attraktor-Mechanismus unterdrückt, was das beobachtete $|\Omega_0 - 1| < 0{,}01$ zu einem natürlichen Ergebnis macht.

**Vergleich mit Inflation.** Inflation löst beide Probleme durch exponentielle Expansion, die durch ein Skalarfeld mit einem spezifischen Potential angetrieben wird — ein Mechanismus, der seine eigene Feinabstimmung einführt (das Inflatonpotential muss extrem flach sein) und nicht direkt beobachtet wurde (keine primordialen Gravitationswellen entdeckt, $r < 0{,}036$). EBC löst beide Probleme durch die Geometrie des Bounces selbst, ohne zusätzliche Felder oder Feinabstimmung, und ist konsistent mit $r \approx 0$ als struktureller Vorhersage (Abschnitt 6.2, Vorhersage 4). Ein direkter Vergleich mit anderen Bounce-Kosmologien zu diesen Punkten findet sich in Abschnitt 7.

---

## 5. Zyklusdauer- und Positionsschätzungen

### 5.1 Einfache Schätzung aus der Zyklusposition

Aus $T = t_0 / f_\mathrm{Zyklus}$:

| Angenommenes $f$ | Zyklusdauer $T$ |
|-----------------|----------------|
| 6 % | 230 Gyr |
| 10 % | 138 Gyr |
| 15 % | 92 Gyr |

**Wahrscheinlicher Bereich: $T \approx 90$–230 Gyr.**

### 5.2 Eingeschränkte Schätzung aus $H_0 \cdot t_0$

Für eine materiefreie sinusförmige Oszillation mit $a_\mathrm{min} \approx 0$ gilt folgende Beziehung:

$$H_0 \cdot t_0 \approx \varphi \cdot \tan\!\left(\frac{\varphi}{2}\right), \quad \varphi = 2\pi f$$

Mit dem beobachteten $H_0 \cdot t_0 \approx 0{,}95$ (dimensionslos) ergibt die numerische Lösung $\varphi \approx 0{,}9$–$1{,}3$ rad, also $f \approx 15$–$21\%$. Für realistisches $a_\mathrm{min} > 0$ nimmt die effektive Phase auf $f \approx 6$–$15\%$ ab.

Eine vollständige Lösung erfordert das Gleichungssystem:

$$\begin{aligned}
H_0 &= \frac{A\omega\sin\varphi}{a_\mathrm{min} + A(1-\cos\varphi)}, \\
q_0 &= -\frac{A\omega^2\cos\varphi \cdot [a_\mathrm{min} + A(1-\cos\varphi)]}{[A\omega\sin\varphi]^2}, \\
T   &= \frac{2\pi t_0}{\varphi}
\end{aligned}$$

mit den Unbekannten $\{\varphi, A/a_\mathrm{min}, \omega\}$. Dies erfordert eine zusätzliche Einschränkung, idealerweise den Ruck-Parameter $j_0$ (siehe Abschnitt 6.3).

### 5.3 Zyklusanzahl

Belege für $N \geq 3$ Zyklen:

| Beobachtung                                    | Abgeleitetes $N$ | Stärke           |
|------------------------------------------------|------------------|------------------|
| CMB-Isotropie (guter thermischer Reset) | $N \leq 4$ | begrenzt hohes $N$ |
| CMB-Quadrupolanomalie | $N \geq 3$ | schwach |
| Herkules-CrB-Große-Mauer | $N \geq 3$–4 | moderat |
| Primodiale Leerraummagnetfelder | $N \geq 3$ | moderat |
| Li-7-Problem (selektiver Bounce) | $N \geq 3$ | schwach–moderat |
| Baryogenese (langsame Akkumulation über $N$ Zyklen, kein Zeitdruck) | $N \geq 2$ | schwach–moderat |
| JWST: massive SL und Galaxien bei $z > 10$ | $N \geq 2$ | moderat–stark |

Aktuelle Daten unterstützen $N = 3$ oder $N = 4$. Das wahre Gesamtalter des Universums wäre dann:

$$t_\mathrm{gesamt} \approx (N-1)\cdot T + t_0 \approx \begin{cases} 474\ \mathrm{Gyr} & (N=3,\ T=230\ \mathrm{Gyr}) \\ 704\ \mathrm{Gyr} & (N=4,\ T=230\ \mathrm{Gyr}) \end{cases}$$

**Interzykliche chemische und strukturelle Anreicherung.** Das Argument für $N \geq 3$ wird durch die Betrachtung gestärkt, was jeder Zyklus für den nächsten hinterlässt (Abschnitt 4.7). Der Bounce-Filter bei $T_\mathrm{bounce} \approx 4 \times 10^9$ K zerstört alle leichten Nuklide (Li, Be, B, D) und alle stellaren Strukturen, während er Schwarze Löcher, Neutronensterne, Dunkle-Materie-Halos und die schwereren Alpha-Elemente (O, Si, Fe) in kompakten Überresten erhält. Nach $N-1$ vollständigen Zyklen werden drei kumulative Effekte erwartet:

Erstens verschiebt sich die **Schwarze-Loch-Massenfunktion** mit jedem Zyklus nach oben. Ein in Zyklus 1 über 200 Gyr assembliertes supermassives Schwarzes Loch persistiert als vorgeformter Keim in Zyklus 2 und ermöglicht schnelle AGN-Aktivität und massiven Galaxienaufbau weit früher in Zyklus 2, als reines Bottom-up-Wachstum aus stellaren Überresten erlauben würde. Zu Beginn von Zyklus 3 stehen SL-Keime aus beiden vorherigen Zyklen am Anfang der Expansion zur Verfügung — was eine direkte und parameterfreie Erklärung für die JWST-Beobachtungen von $M > 10^8\ M_\odot$-Schwarzen Löchern bei $z > 10$ bietet, die innerhalb einer einzigen 13,8-Gyr-Geschichte unter Standard-$\Lambda$CDM-Wachstumsmodellen schwer zu produzieren sind.

Zweitens steigt der **He-4-Massenanteil $Y_p$** monoton mit $N$: Jeder Bounce zerstört H und leichte Elemente, lässt He-4 aber intakt, und stellare Nukleosynthese innerhalb jedes Zyklus wandelt zusätzliches H in He-4 um. Die Vorhersage $Y_p > 0{,}2470$ (Abschnitt 4.4) wird mit zunehmendem $N$ stringenter und liefert eine prinzipielle Einschränkung der Zyklusanzahl aus zukünftigen Präzisionsmessungen der Heliumhäufigkeit.

Drittens wird das **Dunkle-Materie-Gerüst** niemals zurückgesetzt. DM-Halos aus den Zyklen 1 und 2 werden durch den Bounce komprimiert und wieder ausgedehnt, behalten aber ihre Masse und näherungsweise Topologie bei. Zyklus-3-Struktur bildet sich daher auf einem geerbten gravitativen Skelett, was den Aufbau von Galaxien und Clustern gegenüber einem Universum beschleunigt, das von einem glatten Anfangszustand ausgeht. Dies kann zur beobachteten frühen Entstehung von Großraumstruktur in JWST-Daten und zu Anomalien im Materiepower-Spektrum auf großen Skalen beitragen.

Die obere Grenze $N \leq 4$ wird durch CMB-Isotropie gesetzt: Jeder Zyklus akkumuliert geometrische Asymmetrien (Abschnitt 4.3), die den CMB progressiv verzerren würden, wenn zu viele Zyklen dem aktuellen vorausgingen. Ein großes $N$ würde beobachtbare CMB-Anisotropie erzeugen, die mit Planck-Daten unvereinbar ist, und liefert damit eine komplementäre Einschränkung. Die Kombination $N = 3$ bleibt der bevorzugte Wert, mit $N = 4$ marginal konsistent.

### 5.4 Langfristige Entwicklung: Schwellenwert-Kaskade

*Der folgende Abschnitt extrapoliert den EBC-Rahmen auf Zeitskalen weit jenseits jeder observationellen Reichweite. Er wird als strukturell motivierte Konsequenz des Dämpfungsterms präsentiert, nicht als empirische Vorhersage. Quantitative Details sind stark modellabhängig.*

Die gedämpfte Oszillatorstruktur von EBC impliziert, dass die Bounce-Temperatur monoton über Zyklen hinweg abnimmt. Dies hat eine konkrete physikalische Konsequenz: Mehrere separate physikalische Prozesse — jeder durch seine eigene Temperaturschwelle gesteuert — hören in Folge dauerhaft auf, wenn sich das System dem Gleichgewicht bei $a_*$ nähert.

**Bounce-Temperaturentwicklung.** Aus den EBC-Gleichungen skaliert die Rückstellenergie am Bounce-Minimum als $E \sim \Lambda_0/a_\mathrm{min}$. Unter Dämpfung mit Rate $\gamma$ nimmt die Schwingungsamplitude ab und $a_\mathrm{min}$ steigt entsprechend. Im schwach gedämpften Grenzfall nimmt die Bounce-Temperatur geometrisch über Zyklen ab:

$$T_\mathrm{bounce}(N) \approx T_\mathrm{bounce,0} \cdot e^{-\alpha N}$$

wobei $\alpha$ die effektive Dämpfungsfraktion pro Zyklus ist, die mit dem dimensionslosen Dämpfungsparameter $\tilde{\gamma}$ von (EBC2) durch $\alpha \approx \pi \tilde{\gamma}$ für einen schwach gedämpften Oszillator zusammenhängt (ein Zyklus reduziert die Amplitude um $e^{-\pi\tilde{\gamma}}$). Mit $\tilde{\gamma} = 1{,}5 \times 10^{-3}$ aus der numerischen Illustration gilt $\alpha \approx 5 \times 10^{-3}$. Die Anzahl der Zyklen, bevor eine gegebene physikalische Schwelle $T_\mathrm{Schwelle}$ dauerhaft überschritten wird, beträgt:

$$N_\mathrm{Schwelle} \approx \frac{1}{\alpha}\ln\!\left(\frac{T_\mathrm{bounce,0}}{T_\mathrm{Schwelle}}\right)$$

**Die vierphasige Kaskade.** Drei aufeinanderfolgende Schwellen definieren qualitativ unterschiedliche kosmologische Epochen:

| Phase                             | $T_\mathrm{bounce}$ | Physik beim Bounce                                  | Zyklusschätzung             |
|-----------------------------------|---------------------|-----------------------------------------------------|-----------------------------|
| **I — aktuell** | $\gtrsim 10^9$ K | BBN, selektive Photodis\-integration, He-4-Anreicherung | $N \lesssim 1{,}4/\alpha$ |
| **II — post-BBN** | $3000\text{–}10^9$ K | Volles Plasma, CMB bildet sich; keine neue Nukleosynthese | $1{,}4/\alpha \lesssim N \lesssim 14{,}8/\alpha$ |
| **III — post-Plasma** | $\ll 3000$ K | Keine Plasmaphase; keine neue CMB-Oberfläche letzter Streuung | $N \gtrsim 14{,}8/\alpha$ |
| **IV — asymptotisch** | $\to T_\mathrm{Gleich}$ | $a_\mathrm{min} \to a_*$; statisches Gleichgewicht | $N \to \infty$ |

Für die aktuelle Epoche ($N = 3$) impliziert die Nähe von $T_\mathrm{bounce} \approx 4 \times 10^9$ K zur BBN-Schwelle von $\sim 10^9$ K — einem Faktor von nur $\sim 4$ — dass wir uns nahe dem **Ende von Phase I** befinden. Der Übergang zu Phase II, wo Bounces heiß genug sind, um Plasma zu bilden und einen neuen CMB zu erzeugen, aber keine Nukleosynthese mehr antreiben, wird innerhalb von $N_\mathrm{BBN} - 3 \approx (1{,}4/\alpha) - 3$ weiteren Zyklen eintreten. Für $\alpha \sim 10^{-3}$ sind das $\mathcal{O}(10^3)$ Zyklen oder $\mathcal{O}(200\,\mathrm{Tyr})$ in der Zukunft.

**Ein verstärkender Effekt durch kompakte Reliktakkumulation.** Die obige Schätzung geht davon aus, dass der thermisch verfügbare Gasanteil über Zyklen konstant bleibt. In der Praxis beschleunigt ein zusätzlicher Prozess die Kaskade: Mit jedem Zyklus wird ein zunehmender Anteil baryonischer Materie in Schwarzen Löchern und Neutronensternen eingeschlossen (Abschnitt 4.7), die den Bounce thermisch inert überleben. Diese progressive Erschöpfung des ionisierbaren Gasanteils reduziert effektiv die optische Tiefe der Plasmaphase, noch bevor die Bounce-Temperatur selbst unter die Ionisationsschwelle des Wasserstoffs ($\sim 10^4$ K) fällt. Die beiden Effekte — sinkende $T_\mathrm{bounce}$ und sinkender Gasanteil — verstärken sich gegenseitig und verkürzen die Phase-I-II- und Phase-II-III-Übergänge gegenüber der Einzel-Prozess-Schätzung oben. Eine quantitative Behandlung dieses zusammengesetzten Zerfalls erfordert ein Modell für die Rate der Baryonensperrung pro Zyklus, was den Rahmen dieser Arbeit übersteigt und als Thema für zukünftige Entwicklung identifiziert wird.

**Observationelle Irrelevanz, strukturelle Relevanz.** Phase III und IV liegen weit jenseits jedes observationellen Horizonts und haben keine direkten empirischen Konsequenzen. Ihre Bedeutung ist strukturell: Der EBC-Rahmen hat einen natürlichen, thermodynamisch motivierten Endpunkt — ein statisches, Schwarzes-Loch-dominiertes Universum bei Skala $a_*$ — ohne einen Big Rip, einen Wärmetod im $\Lambda$CDM-Sinne oder einen externen Cutoff zu postulieren. Die Kaskade von Phase I zu Phase IV ist eine direkte Konsequenz des in Abschnitt 2.2 eingeführten Dämpfungsterms $-\gamma H$ und schließt die thermodynamische Buchführung des Rahmens.

---

## 6. Testbare Vorhersagen und Vergleich mit $\Lambda$CDM

### 6.1 Zusammenfassender Vergleich

| Größe               | $\Lambda$CDM    | EBC ($a_0 \ll a_*$) | DESI 2024      |
|---------------------|-----------------|---------------------|----------------|
| $w_0$ | $-1$ (exakt) | $\mathbf{-2/3 \approx -0{,}667}$ | $-0{,}70 \pm 0{,}10$ $\checkmark$ |
| $w_a$ | 0 | $< 0$ ($w$ steigt mit $a$) | $-0{,}65 \pm 0{,}25$ $\checkmark$ |
| Singularität | ja | **nein** ($a_\mathrm{min} > 0$) | — |
| Monotone Expansion | ja | **nein** (Wendepunkt) | — |
| Inflation | erforderliches Feld | Zeitdilatationsartefakt | — |

### 6.2 Falsifizierbare Vorhersagen

1. **$w_0 \approx -2/3$**: Parameterfreie Vorhersage. Euclid und DESI Year 5 können dies mit $<5\%$ Präzision testen.

2. **Monoton steigendes $w(a)$**: $w$ sollte von $-2/3$ in Richtung 0 steigen, wenn $a \to a_*$. Das Vorzeichen von $w_a$ ist bereits in DESI-Daten angedeutet.

3. **Ruck-Parameter $j_0 < 1$**: Der Ruck-Parameter $j_0 \equiv \dddot{a}\,a^2/\dot{a}^3$ liefert den stärksten kurzfristigen Diskriminator. In $\Lambda$CDM gilt $j_0 = 1$ exakt für ein flaches Universum mit echter kosmologischer Konstante. In EBC ergibt sich durch Differentiation von (EBC2) nach der Zeit und Ausdruck des Ergebnisses in Termen von $w_\mathrm{EBC}(a)$ und $\Omega_\mathrm{EBC}$:
$$j_0 = 1 + \frac{9}{2}w_\mathrm{EBC}(1 + w_\mathrm{EBC})\,\Omega_\mathrm{EBC} + \frac{3}{2}\frac{dw_\mathrm{EBC}}{d\ln a}\,\Omega_\mathrm{EBC}$$
Mit $w_\mathrm{EBC} \approx -2/3 + (4/3)x^2$ und $dw/d\ln a \approx (8/3)x^2$ für $x \ll 1$ sowie $\Omega_\mathrm{EBC} \approx \Omega_\Lambda \approx 0{,}68$ heute:
$$j_0(\mathrm{EBC}) \approx 1 - \frac{1}{6}\Omega_\mathrm{EBC}\cdot O(x^2) < 1$$
Die Abweichung von eins ist von der Größenordnung $f_\mathrm{Zyklus}^2 \sim 10^{-3}$–$10^{-2}$, klein, aber prinzipiell messbar mit Rubin LSST und DESI-Year-5-Supernovaproben. Eine vollständige Ableitung unter Einbeziehung von Materie bleibt zukünftiger Arbeit vorbehalten.

4. **Keine primordialen Gravitationswellen**: Konsistent mit der Nicht-Detektion $r < 0{,}036$ (BICEP/Keck 2021), da Inflation in EBC ein Zeitdilatationsartefakt ist, kein unabhängiges Feld. Diese Vorhersage erhält quantitative Unterstützung, wenn die Bounce-Energieskala direkt aus dem Modell abgeschätzt wird.

   **Bounce-Temperatur und minimaler Skalenfaktor.** Der Li-7-Photodisintegrationsmechanismus (Abschnitt 4.4) schränkt die Bounce-Temperatur auf $T_\mathrm{bounce} \approx 3$–$5 \times 10^9\ \mathrm{K}$ ein. Mit $T \propto a^{-1}$ und $T_\mathrm{CMB} = 2{,}725\ \mathrm{K}$:
   $$\frac{a_\mathrm{min}}{a_0} = \frac{T_\mathrm{CMB}}{T_\mathrm{bounce}} \approx \frac{2{,}725}{4 \times 10^9} \approx 7 \times 10^{-10}$$
   Die entsprechende Energieskala beim Bounce beträgt $k_\mathrm{B} T_\mathrm{bounce} \approx 0{,}3\ \mathrm{MeV}$ — genau im Bereich der Kernphysik, nicht der Quantengravitation.

   **Entsprechung zu kosmologischen Standardepochen.** Im $\Lambda$CDM-Zeitplan entspricht eine Temperatur von $\sim 4 \times 10^9\ \mathrm{K}$ etwa $t \approx 1$–$20$ Sekunden nach dem Urknall — dem Beginn der Urknall-Nukleosynthese, nicht der inflationären Epoche. Standardinflation erfordert Energieskalen der Größenordnung $10^{15}$–$10^{16}\ \mathrm{GeV}$ (GUT-Skala) bis $10^{19}\ \mathrm{GeV}$ (Planck-Skala). Der EBC-Bounce operiert etwa $10^{19}$–$10^{22}$ Mal unterhalb dieser Skalen. Da das Tensor-Skalar-Verhältnis $r \propto (H_\mathrm{Inf}/m_\mathrm{Pl})^2$ erfüllt und die effektive Hubble-Rate beim EBC-Bounce durch die MeV-Skala-Temperatur gesetzt wird, sagt EBC $r \ll 10^{-10}$ voraus — effektiv null für jedes absehbare Experiment.

   **Endliche anfängliche Oszillationsenergie.** EBC erfordert nicht, dass der erste Bounce bei der Planck-Dichte stattgefunden hat. Der minimale Skalenfaktor wird durch die anfängliche Oszillationsenergie $E_0$ des elastischen Raummodus bestimmt — eine endliche Größe, die den Planck-Bereich nicht erreichen muss. Dies ist strukturell distinct von der Schleifen-Quantenkosmologie, wo der Bounce spezifisch durch Planck-skalige Quantengeometrieeffekte ausgelöst wird. In EBC ist $E_0$ ein freier Parameter des Rahmens, der in einem Multiversum-Kontext unterschiedliche Werte über verschiedene Realisierungen annehmen könnte und Universen mit unterschiedlichen Zyklusamplituden, -dauern und — durch den BBN-Mechanismus — unterschiedlichen Leichtelementhäufigkeiten produzieren würde. Die Nicht-Detektion primordialer Gravitationswellen ist in EBC daher keine Koinzidenz, sondern eine direkte strukturelle Konsequenz der sub-Planck-Bounce-Energieskala.

5. **Direktionale $H_0$-Variationen**: Systematische Unterschiede in $H_0$ über Himmelsrichtungen hinweg sollten mit zukünftigen Präzisionsmessungen detektierbar sein.

6. **Korreliertes Li-7/He-4-Signal**: Li-7/H unterhalb von Standard-BBN und $Y_p > 0{,}2470$, beide resultierend aus demselben Bounce-Photodisintegrationsmechanismus; gemeinsam mit JWST testbar.

7. **Li-7-Rotverschiebungsgradient**: Primodiales Li-7 bei $z > 5$ sollte sich systematisch von Werten bei $z \approx 2$–3 unterscheiden.

---

## 7. Vergleich mit Bounce-Kosmologien

```{=latex}
\scriptsize
\rowcolors{2}{gray!12}{white}
```

| Aspekt          | EBC (diese Arbeit)   | LQK             | KZK (Penrose)   | Ekpyrotisch       |
|-----------------|----------------------|-----------------|-----------------|-------------------|
| Bounce-Mechanismus | Dynamisches $\Lambda_\mathrm{EBC}(a)$ (phänomenologisch) | Quantengravitation | Konformer Übergang | Membrankollision |
| Singularitätsvermeidung | $a_\mathrm{min} > 0$ per Postulat + Bounce-Term | Quanteneffekte bei Planck-Dichte | Konforme Umskalierung | Langsame Kontraktion |
| Inflation | Zeitdilatationsartefakt | Bounce ersetzt Inflation | Nicht erforderlich | Nicht erforderlich |
| Dunkle Energie | Dynamische Raumeigenschaft | Kosmologische Konstante | Nicht primär | Nicht primär |
| Zustandsgleichung | $w_0 = -2/3$ (analytisch) | Nicht spezifiziert | Nicht primär | Nicht spezifiziert |
| Entropiebehandlung | Struktur als Dämpfung | Ungewiss | Reset durch konformen Übergang | Niedrigentropie-Zyklen |
| Horizontproblem | $H=0$ beim Bounce $\Rightarrow$ $d_H \to \infty$ (kausaler Reset) | Kausaler Kontakt vor Bounce | Konforme Kontinuität | Kausaler Kontakt in Kontraktion |
| Flachheitsproblem | $\Omega \to 1$ Attraktor während Kontraktion | Über Quantengeometrie gelöst | Nicht primär | Attraktor während ekpyrotischer Kontraktion |
| Primodiale GW ($r$) | $r \approx 0$ (sub-MeV-Bounce, strukturell) | Modellabhängig | Nicht primär | $r \approx 0$ (langsame Kontraktion) |

```{=latex}
\normalsize
\rowcolors{0}{}{}
```

---

## 8. Einschränkungen und erforderliche Entwicklung

Der vorliegende Rahmen ist explizit phänomenologisch. Die folgenden Punkte erfordern Lösung, bevor er als vollständige physikalische Theorie betrachtet werden kann:

1. **Kovariante Einbettung**: Die Modifikation $\Lambda_\mathrm{EBC}(a)$ muss aus einer modifizierten Einstein-Hilbert-Wirkung abgeleitet werden:
$$G_{\mu\nu} + \Lambda_\mathrm{EBC}(g_{\mu\nu}, R_{\mu\nu\alpha\beta})\,g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu}$$
Die Definition von $\Lambda_\mathrm{EBC}$ als Funktion von Krümmungsskalaren würde den Rahmen auf eine rigorose kovariante Grundlage stellen.

2. **Externe Referenzzeit $\tau_\mathrm{ext}$**: Die postulierte Entkopplung der Raumoszillation von der inneren relativistischen Zeit erfordert formale Definition. Eine vorläufige Formulierung: $a(\tau_\mathrm{int}) = a(\tau_\mathrm{ext}) \cdot [\text{Zeitdilatationsfaktor}(\rho)]$, wobei $\tau_\mathrm{int}$ die Robertson-Walker-Koordinatenzeit ist. Dies bleibt zu präzisieren.

3. **Materie und Strahlung**: Die numerische Integration (Abschnitt 3) lässt Materie und Strahlung aus. Der Materieterm $-4\pi G\rho_m/3$ in (EBC2) ist technisch unkompliziert einzubeziehen — es erfordert das Hinzufügen von Standard-$\rho \propto a^{-3}$- und $\rho \propto a^{-4}$-Komponenten und Reintegration der dimensionslosen ODE. Analytische Größenordnungsschätzungen (Abschnitt 3.2) legen nahe, dass die Zyklusdauer um etwa 15–25 % zunimmt und die Zykluspositionsschätzung auf $f \approx 5$–13 % verschoben wird, während das Expansionsmaximum und die analytische $w_0 = -2/3$-Vorhersage im Wesentlichen unverändert bleiben. Eine vollständige numerische Integration mit Materie und Strahlung ist erforderlich, bevor die Zyklusdauer- und Positionsschätzungen quantitativ mit Beobachtungsdaten verglichen werden können.

4. **Akustische CMB-Physik**: Das Bounce-Szenario muss die beobachteten CMB-Peak-Positionen reproduzieren ($\ell \approx 220, 540, 800$). Es muss gezeigt werden, dass die akustische Physik des Prä-Bounce-Plasmas dieselbe Signatur wie Standard-Rekombination erzeugt.

5. **Entropiehaushalt**: Der Dämpfungsterm $-\gamma H$ muss thermodynamisch konsistent sein. Eine vollständige Behandlung muss $\Delta S > 0$ über Zyklen demonstrieren.

6. **Quantitative $q_0$-Reproduktion**: Der Verzögerungsparameter muss quantitativ durch Einbeziehung von Materie angepasst werden ($q_0 = \Omega_m/2 - \Omega_\Lambda \approx -0{,}55$). Dies ist prinzipiell unkompliziert, erfordert aber das vollständige (EBC1) einschließlich $\rho$.

7. **Bounce-Mechanismus aus ersten Prinzipien**: Der Bounce-Term $\Lambda_b \propto a^{-4}$ ist durch seine strahlungsähnliche Skalierung motiviert, entbehrt aber einer mikroskopischen Ableitung.

8. **Kontinuierliche versus impulsive Energieeinspeisung**: Eine alternative Klasse von Bounce-Modellen könnte die Einspeisung von Oszillationsenergie prinzipiell auf die Bounce-Phase allein beschränken, wobei der elastische Term während der Expansions- und Kontraktionsphasen fehlt. In EBC ist diese Möglichkeit per Konstruktion ausgeschlossen: Die analytische Ableitung von $w_0 = -2/3$ (Abschnitt 2.5) hängt davon ab, dass $\Lambda_\mathrm{EBC}(a)$ zu allen Zeiten aktiv ist — sie folgt aus der logarithmischen Ableitung $d\ln\Lambda_\mathrm{EBC}/d\ln a$, ausgewertet in der aktuellen Epoche. Eine rein impulsive (nur-Bounce-)Energieeinspeisung würde den elastischen Term aus der aktuellen Epoche entfernen, die parameterfreie Vorhersage $w_0 = -2/3$ unerreichbar machen und einen separaten Dunkle-Energie-Mechanismus erfordern. Der kontinuierliche elastische Term ist daher kein optionales Merkmal, sondern eine strukturelle Notwendigkeit des Rahmens. Der mikroskopische Ursprung dieser stets aktiven geometrischen Elastizität — und ihre Beziehung zum Bounce-Mechanismus — bleibt eine offene Frage für zukünftige Entwicklung.

---

## 9. Schlussfolgerung

Wir haben die Elastische-Bounce-Kosmologie vorgestellt, einen phänomenologischen Rahmen, in dem die kosmische Expansion durch modifizierte Friedmann-Gleichungen mit einer dynamischen elastischen Rückstellkraft gesteuert wird. Der Rahmen erzeugt quasi-zyklische Skalenfaktor\-entwicklung ohne Singularitäten und liefert die parameterfreie Vorhersage $w_0 = -2/3$, konsistent mit DESI 2024 auf $1\sigma$.

Das Modell befasst sich mit mehreren offenen Problemen der Standardkosmologie in einem einheitlichen konzeptuellen Rahmen. Dunkle Energie wird als dynamische geometrische Eigenschaft des Raums statt als Vakuumenergiefield neu interpretiert. Die Hubble-Spannung wird auf räumliche Inhomogenitäten zurückgeführt, die sich über Zyklen angesammelt haben. Das Lithium-7-Problem wird durch selektive nukleare Photodisintegration beim Bounce erklärt, mit einer korrelierten He-4-Überabundanz-Vorhersage, die mit JWST testbar ist. Baryogenese wird als langsame Akkumulation über erweiterte Zyklusdauern neu gerahmt, was die schwere Zeitdruckbeschränkung der standardmäßigen elektroschwachen Baryogenese entspannt. Das Horizont- und das Flachheitsproblem werden durch die Bounce-Geometrie selbst gelöst: $H = 0$ beim Bounce macht den kausalen Horizont unendlich, und die Kontraktionsphase treibt $\Omega \to 1$ als dynamischen Attraktor — beides ohne Postulierung eines Inflatonfeldes.

Ein bedeutendes neues Ergebnis dieser Arbeit ist der **transzykliche Erbschaftsrahmen** (Abschnitt 4.7): Der Bounce wirkt als selektiver physikalischer Filter, der gewöhnliche baryonische Materie thermalisiert, während er kompakte Relikte — Schwarze Löcher, Neutronensterne und Dunkle-Materie-Halos — im Wesentlichen unverändert lässt. Dies führt zu einer natürlichen Erklärung für die JWST-Beobachtungen massiver Schwarzer Löcher und Galaxien bei $z > 10$: Diese Objekte sind direkte Nachkommen von Schwarze-Loch-Populationen, die während früherer Zyklen assembliert wurden. Derselbe Rahmen sagt ein charakteristisches Elementhäufungsmuster in ultra-metallarmen Sternen voraus und impliziert einen monoton steigenden He-4-Massenanteil mit der Zyklusanzahl.

Die langfristige Entwicklung von EBC folgt einer **Schwellenwert-Kaskade** (Abschnitt 5.4): Wenn die Bounce-Temperatur geometrisch über Zyklen abnimmt, hören sukzessive physikalische Prozesse — Nukleosynthese, Plasmabildung, CMB-Emission — dauerhaft in Folge auf, wobei der Rahmen einem statischen, Schwarzes-Loch-dominierten Gleichgewicht bei Skala $a_*$ asymptotisch zustrebt.

EBC ersetzt die Allgemeine Relativitätstheorie explizit nicht, sondern parametrisiert mögliche zusätzliche Beiträge zur großräumigen Hintergrundevolution. Mehrere seiner qualitativen Vorhersagen sind mit naher-Zukunft-Instrumenten testbar: Euclid, DESI Year 5 und Rubin LSST für den Ruck-Parameter $j_0 < 1$, $w_0$ und $w_a$; JWST für das korrelierte Li-7/He-4-Signal, ultra-metallarme Sternhäufigkeiten und die hochrotverschobene Schwarze-Loch-Massenfunktion; und BICEP/CMB-S4 für die fortgesetzte Nicht-Detektion primordialer Gravitationswellen.

Der Ruck-Parameter $j_0$ bleibt der am leichtesten zugängliche kurzfristige Diskriminator: EBC sagt $j_0 < 1$ voraus, während $\Lambda$CDM $j_0 = 1$ exakt erfordert.

---

## Danksagung

Der Autor erkennt die Verwendung KI-gestützter Werkzeuge (Claude, Anthropic; ChatGPT, OpenAI) bei der Strukturierung und Verfeinerung dieses Manuskripts, der Formalisierung des mathematischen Rahmens, der Verknüpfung mit der observationellen Literatur und der Übersetzung aus dem Deutschen an. Das konzeptuelle Rahmenwerk — alle wissenschaftlichen Ideen, physikalischen Intuitionen und die zehn Postulate, die EBC zugrundeliegen (aufgelistet in Anhang A) — stammt vom Autor. Die vollständige redaktionelle Verantwortung liegt beim Autor.

---

## Anhang A: Die zehn Postulate der EBC

Die folgenden zehn Postulate bilden das originale konzeptuelle Fundament, aus dem der EBC-Rahmen entwickelt wurde. Sie sind hier in ihrer ursprünglichen Form aufgelistet, mit Verweisen auf die Abschnitte des Papers, wo jedes Postulat entwickelt oder verwendet wird.

**P1 — Intrinsische Expansion; Dunkle Energie als räumliche Eigenschaft.**
Die Expansion des Raums im Universum hängt nur schwach von seinem materiellen Inhalt ab. Die sogenannte Dunkle Energie existiert nicht als separate Konstituente innerhalb des Universums. Expansion ist eine Eigenschaft des Raums selbst und wird nicht von dem in ihm enthaltenen Energieinhalt dominiert. *(Abschnitte 2.1, 2.3)*

**P2 — Gedämpfte Oszillation; kein Kollaps zur Singularität.**
Bei der Entstehung des Raums — gemeinhin als Urknall bezeichnet — begann der Raum sich von einem hochkomprimierten Zustand aus auszudehnen, erreichte schließlich eine maximale Ausdehnung und zog sich wieder zusammen. Das Skalenfaktor-Zeit-Diagramm folgt einer gedämpften Oszillation: Der Raum kollabiert nicht zurück zu einer Singularität, sondern erreicht seinen Wendepunkt bei einer endlichen, nicht-null minimalen Skala. *(Abschnitte 2.1, 2.2)*

**P3 — Externe Referenzzeit.**
Die Zeitskala für die Expansion des Raums ist unabhängig vom Fortschreiten der Zeit innerhalb des Raums. Die Oszillation des Raums verläuft mit gleichmäßiger Rate in einem externen Bezugssystem, entkoppelt von der relativistischen Koordinatenzeit innerhalb des Universums. *(Abschnitt 2.1)*

**P4 — CMB-Bildung nur in frühen Zyklen.**
In den ersten Zyklen wird Materie beim Bounce-Minimum auf eine ausreichende Dichte und Temperatur komprimiert, dass sie für Strahlung undurchsichtig wird und der kosmische Mikrowellenhintergrund sich bilden kann. Jenseits eines bestimmten Zyklus erreicht der Bounce nicht mehr die für die Plasmabildung erforderlichen Temperaturen, und kein neuer CMB kann entstehen. *(Abschnitt 5.4)*

**P5 — Progressive Strukturerhaltung.**
Je nach Zyklus werden immer weniger Strukturen beim Expansionsminimum zerstört. Letztendlich wird die Oszillation des Raums kaum noch Einfluss auf seinen Inhalt haben — kompakte Überreste und Großraumstrukturen werden über Bounces hinweg zunehmend erhalten. *(Abschnitte 4.7, 5.4)*

**P6 — Nicht-sphärische Expansion ab dem 2. Zyklus.**
Ab mindestens dem zweiten Zyklus kann nicht angenommen werden, dass das Universum als perfekte Kugel expandiert. Ereignisse innerhalb des Raums führen zu leichten Verformungen der räumlichen Geometrie, was auch implizieren kann, dass der Raum nicht überall mit exakt derselben Rate expandiert, wobei kleine lokale Unterschiede möglich sind. *(Abschnitte 4.2, 4.3)*

**P7 — Inflation nur am Anfang des ersten Zyklus.**
Die inflationäre Phase fand nur am Anfang des ersten Zyklus statt. Sie wiederholt sich in nachfolgenden Zyklen nicht. *(Abschnitte 1.2, 6.2)*

**P8 — Inflation als Zeitdilatationsartefakt.**
Inflation erscheint als sehr schnelle Expansion innerhalb eines kurzen Zeitintervalls, weil diese Zeit relativistisch ist: Aufgrund der extremen Masse-/Energiekonzentration vergeht innere Zeit quasi gar nicht oder extrem langsam. Kraft P3 verläuft die Expansion des Raums aus der Perspektive des externen Bezugssystems gleichmäßig. *(Abschnitt 2.1)*

**P9 — Baryogenese verteilt über Zyklen.**
Das Materie-Antimaterie-Paradoxon wird aufgelöst, weil die Bildung des Materie-Antimaterie-Ungleichgewichts sich über den gesamten ersten Zyklus oder sogar über mehrere Zyklen erstrecken kann. Die Zeitdruckbeschränkung, die die standardmäßige elektroschwache Baryogenese so schwierig macht, wird dadurch aufgehoben. *(Abschnitt 4.5)*

**P10 — Das Universum ist endlich.**
Aus den vorhergehenden Postulaten folgt: Das Universum ist in seiner Größe endlich. Eine maximale Skala $a_*$ existiert, jenseits derer die elastische Rückstellkraft die Expansion umkehrt. Das Universum expandiert nicht unbegrenzt. *(Abschnitte 2.1, 2.3)*

---

## Literaturverzeichnis

1. Planck Collaboration (2020). Planck 2018 results VI: Cosmological parameters. *A&A* 641, A6. DOI: 10.1051/0004-6361/201833910
2. Planck Collaboration (2020). Planck 2018 results X: Constraints on inflation. *A&A* 641, A10. DOI: 10.1051/0004-6361/201833887
3. Riess et al. (2022). A comprehensive measurement of the local value of the Hubble constant with the SH0ES collaboration. *ApJ* 934, L7. DOI: 10.3847/2041-8213/ac5c5b
4. Perlmutter et al. (1999). Measurements of $\Omega$ and $\Lambda$ from 42 high-redshift supernovae. *ApJ* 517, 565. DOI: 10.1086/307221
5. Riess et al. (1998). Observational evidence from supernovae for an accelerating universe. *AJ* 116, 1009. DOI: 10.1086/300499
6. Scolnic et al. (2022). The Pantheon+ analysis: the full data set and light-curve release. *ApJ* 938, 113. DOI: 10.3847/1538-4357/ac8b7a
7. Brout et al. (2022). The Pantheon+ analysis: cosmological constraints. *ApJ* 938, 110. DOI: 10.3847/1538-4357/ac8e04
8. DESI Collaboration (2024). DESI 2024 VI: Cosmological constraints from BAO measurements. *JCAP* 2024, 040. arXiv:2404.03002. DOI: 10.1088/1475-7516/2024/02/021
9. Eisenstein et al. (2005). Detection of baryon acoustic oscillations in the correlation function of a large sample of red galaxies. *ApJ* 633, 560. DOI: 10.1086/466512
10. Fixsen (2009). The temperature of the cosmic microwave background. *ApJ* 707, 916. DOI: 10.1088/0004-637X/707/2/916
11. BICEP/Keck Collaboration (2021). Improved constraints on primordial gravitational waves. *Phys. Rev. Lett.* 127, 151301. DOI: 10.1103/PhysRevLett.127.151301
12. Wong et al. (2020). H0LiCOW XIII: A 2.4% measurement of $H_0$ from lensed quasars. *MNRAS* 498, 1420. DOI: 10.1093/mnras/stz3094
13. Aver et al. (2015). The effects of He I \ensuremath{\lambda}10830 on helium abundance determinations. *JCAP* 2015, 011. DOI: 10.1088/1475-7516/2015/07/011
14. Cooke et al. (2018). One percent determination of the primordial deuterium abundance. *ApJ* 843, 2. DOI: 10.3847/1538-4357/aab9ab
15. Cyburt et al. (2016). Big bang nucleosynthesis: Present status. *Rev. Mod. Phys.* 88, 015004. DOI: 10.1103/RevModPhys.88.015004
16. Penrose, R. (2010). *Cycles of Time*. Bodley Head, London.
17. Steinhardt, P.J. & Turok, N. (2002). A cyclic universe cosmological model. *Science* 296, 1436. DOI: 10.1126/science.1070462
18. Steinhardt, P.J. & Turok, N. (2005). The cyclic model simplified. *New Astron. Rev.* 49, 43. DOI: 10.1016/j.newar.2005.01.003
19. Bojowald, M. (2001). Absence of a singularity in loop quantum cosmology. *Phys. Rev. Lett.* 86, 5227. DOI: 10.1103/PhysRevLett.86.5227
20. Ashtekar, A., Pawlowski, T. & Singh, P. (2006). Quantum nature of the big bang. *Phys. Rev. Lett.* 96, 141301. DOI: 10.1103/PhysRevLett.96.141301
21. Land, K. & Magueijo, J. (2005). Examination of evidence for a preferred axis in the cosmic radiation anisotropy. *Phys. Rev. Lett.* 95, 071301. DOI: 10.1103/PhysRevLett.95.071301
22. Di Valentino, E. et al. (2021). In the realm of the Hubble tension — a review of solutions. *Astropart. Phys.* 131, 102605. DOI: 10.1016/j.astropartphys.2021.102605
23. Neronov, A. & Vovk, I. (2010). Evidence for strong extragalactic magnetic fields from Fermi observations of TeV blazars. *Science* 328, 73. DOI: 10.1126/science.1184192
24. Davari, Z. & Khosravi, N. (2022). Can CP violation address the Hubble tension? arXiv:2203.09439
25. Martin, J. (2012). Everything you always wanted to know about the cosmological constant problem. *Comptes Rendus Physique* 13, 566. DOI: 10.1016/j.crhy.2012.04.008
26. Cruz, M. et al. (2005). Detection of a non-Gaussian spot in WMAP. *MNRAS* 356, 29. DOI: 10.1111/j.1365-2966.2004.08419.x
27. Watkins, R. et al. (2009). Consistently large cosmic flows on scales of 100 $h^{-1}$ Mpc. *MNRAS* 392, 743. DOI: 10.1111/j.1365-2966.2008.14089.x
28. Planck Collaboration (2016). Planck 2015 results XVI: Isotropy and statistics of the CMB. *A&A* 594, A16. DOI: 10.1051/0004-6361/201526681
29. Horvath, I. et al. (2015). New data support the existence of the Hercules-Corona Borealis Great Wall. *A&A* 584, A48. DOI: 10.1051/0004-6361/201424829
30. Hawking, S.W. (1975). Particle creation by black holes. *Commun. Math. Phys.* 43, 199. DOI: 10.1007/BF02345020
31. Labbé, I. et al. (2023). A population of red candidate massive galaxies ~600 Myr after the Big Bang. *Nature* 616, 266. DOI: 10.1038/s41586-023-05786-2

---

*Dieses Paper präsentiert ein konzeptuelles Rahmenwerk mit einem minimalen mathematischen Kern (Abschnitte 2.2–2.5). Es erfordert weitere mathematische Entwicklung — insbesondere eine kovariante Einbettung — sowie eine Begutachtung durch Fachkollegen.*
