---
title: "Elastic Bounce Cosmology (EBC): A Phenomenological Framework for Quasi-Cyclic Cosmic Expansion with a Dynamic Spatial Restoring Force"
date: "March 2026"
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{booktabs}
  - \usepackage{hyperref}
  - \usepackage[table]{xcolor}
---

**Wolfgang Mattis** — Independent Researcher  
ebc@wm0.eu · ORCID: [0009-0006-9810-7819](https://orcid.org/0009-0006-9810-7819)

---

## Abstract

We present Elastic Bounce Cosmology (EBC), a phenomenological framework in which the cosmic scale factor is governed by modified Friedmann equations incorporating a dynamic, scale-factor-dependent effective cosmological term. The central hypothesis is that space possesses an intrinsic elastic property — a geometric restoring force that drives oscillatory expansion and contraction without ever reaching a singularity. This replaces the cosmological constant with a dynamical term $\Lambda_\mathrm{EBC}(a) = \Lambda_0(a_*/a - a/a_*)$, where $a_*$ is the equilibrium scale factor, supplemented by a bounce term $\Lambda_b(a) = \Lambda_b(a_\mathrm{min}/a)^4$ that prevents singular collapse.

A key analytic result follows directly from this ansatz: the effective dark-energy equation of state in the current observational regime ($a \ll a_*$) is

$$w_\mathrm{EBC}(a) = -1 + \frac{1+x^2}{3(1-x^2)},\quad x = a/a_*,$$

which yields $w_0 \approx -2/3 \approx -0.667$ in the limit $a_0 \ll a_*$, requiring no tuning of model parameters. This is consistent with the DESI 2024 measurement $w_0 = -0.70 \pm 0.10$ at the $1\sigma$ level. Numerical integration demonstrates weakly damped quasi-cyclic behavior sustaining numerous expansion–contraction phases before asymptotically approaching equilibrium.

Several open problems of standard cosmology are addressed within this framework: the nature of dark energy (reinterpreted as a geometric space property), the Hubble tension (attributed to spatial inhomogeneities accumulated over cycles), CMB anomalies, the lithium-7 problem (selective nuclear photodisintegration at the bounce), and baryogenesis (distributed across one or more full cycles). We estimate the current epoch to lie in the 3rd or 4th cycle, approximately 5–15% into the current expansion phase, implying a cycle duration of $T \approx 105$–290 Gyr (including a correction for matter content).

The framework is explicitly phenomenological. A covariant derivation from a modified Einstein–Hilbert action, a quantitative reproduction of CMB acoustic peaks, and a full treatment including matter and radiation remain open for future work. We identify the jerk parameter $j_0$ as the most accessible near-term observational discriminant between EBC and $\Lambda$CDM.

---

## 1. Introduction

### 1.1 Successes and Open Problems of $\Lambda$CDM

The standard model of cosmology ($\Lambda$CDM) provides a quantitatively accurate description of the cosmic microwave background (CMB), large-scale structure, primordial nucleosynthesis, and the accelerated expansion of the universe. Nevertheless, it faces several fundamental conceptual and empirical challenges.

**The dark energy problem.** Approximately 68% of the total energy density of the universe is attributed to dark energy, a component whose physical origin remains entirely unknown. Quantum field theory predicts a vacuum energy exceeding the observed value by 120 orders of magnitude — the most severe fine-tuning problem in physics [25].

**The Hubble tension.** Two independent determinations of the cosmic expansion rate disagree at the 4–5$\sigma$ level: the CMB-based value $H_0 \approx 67.4$ km/s/Mpc [Planck 2020] and the local distance-ladder value $H_0 \approx 73.0$ km/s/Mpc [Riess et al. 2022]. This discrepancy is robust against known systematic effects and is widely regarded as an indication of physics beyond the standard model [22].

**DESI 2024.** Baryon Acoustic Oscillation measurements from the Dark Energy Spectroscopic Instrument show hints that the dark-energy equation-of-state parameter $w$ is not constant at $w = -1$ as required by a cosmological constant [DESI Collaboration 2024]. If confirmed at higher significance, this would fundamentally alter the $\Lambda$CDM picture.

**The inflation problem.** The postulated inflationary expansion of the early universe elegantly solves the horizon and flatness problems but has not been directly confirmed observationally. Primordial gravitational waves — the most direct signature of inflation — remain undetected ($r < 0.036$, BICEP/Keck 2021), consistent with EBC's structural prediction $r \approx 0$ (Section 6.2).

**The baryogenesis problem.** Standard electroweak baryogenesis requires CP violation of order $\eta \sim 10^{-10}$ but the CKM mechanism provides only $\delta_\mathrm{CKM} \sim 10^{-20}$ — ten orders of magnitude too small.

### 1.2 Motivation and Scope

These unresolved tensions motivate the exploration of alternative cosmological frameworks. The present work introduces Elastic Bounce Cosmology, which proposes four conceptual reorientations:

1. Cosmic expansion as an intrinsic geometric property of space, not as the effect of a vacuum energy field.
2. Cyclic dynamics with damped oscillations rather than monotonic expansion.
3. Inflation as a relativistic time-dilation artifact rather than an independent field phase.
4. Baryogenesis as a slow accumulation process distributed over cycles.

The framework is explicitly phenomenological and does not replace General Relativity at the fundamental level. It provides a qualitatively distinct alternative perspective and makes several falsifiable predictions testable with near-future instruments.

### 1.3 Related Work

Cyclic and bouncing cosmologies form an active research area. The principal predecessors are:

- **Loop Quantum Cosmology** [19, 20]: bounce prevented by quantum gravity effects at Planck density.
- **Ekpyrotic/Cyclic Universe** [Steinhardt & Turok 2002, 2005]: cycles driven by extra-dimensional membrane collisions.
- **Conformal Cyclic Cosmology** [Penrose 2010]: cycles connected through conformal rescaling with entropy reset.

EBC differs from all three in its treatment of dark energy (reinterpreted as a dynamic spatial property rather than a field), its mechanism for avoiding the singularity (an elastic bounce term in the Friedmann equations rather than quantum gravity or extra dimensions), and its phenomenological rather than fundamental derivation. Crucially, EBC derives a specific equation-of-state prediction ($w_0 = -2/3$) directly testable against DESI data — a feature absent from LQC [19, 20], CCC, and ekpyrotic models.

---

## 2. The EBC Dynamical Model

### 2.1 Conceptual Foundation

The central postulate is that space behaves as an elastic medium with a characteristic equilibrium scale $a_*$. Compression below $a_*$ generates a repulsive restoring force; extension beyond $a_*$ generates an attractive restoring force. This is not a force acting within space but a geometric property of space itself — analogous to the elastic modulus of a compressible medium. The standard cosmological constant $\Lambda$ is reinterpreted as the small-amplitude limit of this dynamic property in the current epoch ($a_0 \ll a_*$).

Two separate postulates accompany this:

- **External reference time** ($\tau_\mathrm{ext}$): The oscillation of space proceeds uniformly in an external reference frame independent of relativistic time inside the universe. Observers within the universe, subject to extreme gravitational time dilation in the early dense phase, perceive the initial expansion as enormously fast — which appears as inflation. This postulate extends General Relativity and is the most speculative element of the framework; it requires formal development (Section 8). The horizon and flatness problems, which inflation was originally designed to solve, are addressed in EBC through the bounce geometry itself rather than through this postulate — see Section 4.8 for the detailed argument.

- **No singularity**: The minimum scale factor $a_\mathrm{min} > 0$ is an explicit postulate. There is no physical evidence that extrapolating $a \to 0$ corresponds to a physical reality.

### 2.2 Modified Friedmann Equations

The EBC framework modifies the standard Friedmann equations by replacing $\Lambda = \mathrm{const}$ with two dynamic terms:

$$H^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2} + \frac{\Lambda_\mathrm{EBC}(a)}{3} + \frac{\Lambda_b(a)}{3} \tag{EBC1}$$

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}(\rho + 3p) + \frac{\Lambda_\mathrm{EBC}(a)}{3} + \frac{\Lambda_b(a)}{3} - \gamma H \tag{EBC2}$$

**Elastic restoring term** (drives the oscillation):
$$\Lambda_\mathrm{EBC}(a) = \Lambda_0\!\left(\frac{a_*}{a} - \frac{a}{a_*}\right)$$

**Bounce term** (prevents singularity):
$$\Lambda_b(a) = \Lambda_b\!\left(\frac{a_\mathrm{min}}{a}\right)^{\!4}$$

**Damping term**: The damping in EBC2 is taken as state-dependent:
$$-\gamma(a)\,H, \quad \gamma(a) = \gamma_0\left|\frac{a - a_*}{a_*}\right|$$
This form vanishes at the equilibrium scale $a_*$ and is largest far from equilibrium, encoding the physical picture that energy dissipation into structure formation (stars, galaxies, clusters) is most efficient during the strongly non-equilibrium compression and expansion phases, and diminishes as the system approaches its rest state. In the limit $a \ll a_*$ (current epoch) this simplifies to $\gamma(a) \approx \gamma_0$, recovering a nearly constant effective damping rate. The choice of this functional form is motivated by simplicity and physical intuition; alternative damping prescriptions are possible and would modify the detailed cycle evolution without affecting the analytic $w_\mathrm{EBC}$ result of Section 2.5.

### 2.3 Physical Properties of the Elastic Term

The elastic term $\Lambda_\mathrm{EBC}(a)$ exhibits qualitatively different behavior in different epochs:

| Epoch                          | $a$ relative to $a_*$ | $\Lambda_\mathrm{EBC}$  | Physical consequence         |
|--------------------------------|-----------------------|-------------------------|------------------------------|
| Early expansion (current) | $a \ll a_*$ | $\approx +\Lambda_0 a_*/a > 0$ | Accelerated expansion (dark energy) |
| Expansion maximum | $a = a_*$ | $= 0$ | Turning point, end of acceleration |
| Beyond maximum | $a > a_*$ | $< 0$ | Contraction |
| Near bounce | $a \to a_\mathrm{min}$ | $\Lambda_b$ dominates $\to +\infty$ | Elastic bounce, no singularity |

### 2.4 Normalization and Parameter Reduction

At the present epoch $a = a_0$, the elastic term must reproduce the observed dark energy density:

$$\Lambda_\mathrm{EBC}(a_0) \approx \Lambda_\mathrm{obs} \approx 1.1 \times 10^{-52}\ \mathrm{m}^{-2}$$

For $a_0 \ll a_*$ this gives:

$$\Lambda_0 \approx \Lambda_\mathrm{obs} \cdot \frac{a_0}{a_*} = \Lambda_\mathrm{obs} \cdot f_\mathrm{cycle}$$

where $f_\mathrm{cycle} = t_0/T$ is the fractional position within the current cycle, estimated independently from the $H_0 \cdot t_0$ constraint in Section 5.2 ($f_\mathrm{cycle} \approx 0.06$–$0.15$). Given such an independent estimate of $f_\mathrm{cycle}$, $\Lambda_0$ is not a free parameter but a derived quantity:

$$\Lambda_0 \approx (0.6\text{--}1.7) \times 10^{-53}\ \mathrm{m}^{-2}$$

Note that $f_\mathrm{cycle}$ and $T$ are genuinely independent unknowns constrained by separate observables ($H_0$, $t_0$, $q_0$), so this normalization does not introduce a circularity.

### 2.5 Effective Equation of State

Defining the EBC dark energy density $\rho_\mathrm{EBC} = \Lambda_\mathrm{EBC}/(8\pi G)$ and applying the continuity equation:

$$\dot{\rho}_\mathrm{EBC} + 3H(1 + w_\mathrm{EBC})\rho_\mathrm{EBC} = 0$$

We treat $\rho_\mathrm{EBC}$ as an effective fluid component; this is formally analogous to the standard treatment of the cosmological constant as vacuum energy and is self-consistent at the background level, since $\Lambda_\mathrm{EBC}(a)$ depends only on the homogeneous background scale factor and does not violate the Bianchi identity within the FRW framework (the modified Friedmann equations (EBC1)–(EBC2) remain mutually consistent by construction). A covariant generalization beyond FRW is reserved for future work (Section 8, item 1).

$$w_\mathrm{EBC} = -1 - \frac{1}{3}\frac{d\ln\Lambda_\mathrm{EBC}}{d\ln a}$$

For $\Lambda_\mathrm{EBC}(a) = \Lambda_0(a_*/a - a/a_*)$, setting $x = a/a_*$:

$$\boxed{w_\mathrm{EBC}(x) = -1 + \frac{1 + x^2}{3(1 - x^2)}}$$

In the current observational regime $x = a_0/a_* \ll 1$:

$$w_0 \equiv w_\mathrm{EBC}(a_0) \approx -\frac{2}{3} \approx -0.667$$

This is a prediction of the model that **follows solely from the $1/a$ scaling of the elastic term** in the limit $a_0 \ll a_*$: neither $\Lambda_0$ nor $a_*$ need to be tuned to reproduce $w_0 \approx -2/3$. It should be noted that the full EBC framework does contain additional parameters ($a_*$, $\gamma_0$, $\Lambda_b$, $a_\mathrm{min}$), which are constrained by other observables. The claim of parameter-freedom applies specifically to the $w_0$ prediction, not to the model as a whole.

The DESI 2024 BAO measurement $w_0 = -0.70 \pm 0.10$ [8] is consistent with this prediction at the $1\sigma$ level. These results have not yet been confirmed by an independent dataset and should be regarded as preliminary motivation rather than definitive evidence. The physical interpretation: the EBC effective dark energy scales as $\rho_\mathrm{EBC} \propto a^{-1}$ in the current epoch, giving $w = -2/3$ — formally equivalent to a network of topological domain walls.

**Time evolution of $w$**: As $x$ increases from 0 toward 1 (the expansion maximum), $w_\mathrm{EBC}$ rises monotonically from $-2/3$ toward 0 and beyond. In the CPL parametrization $w(a) = w_0 + w_a(1-a)$:

$$w_a \approx -\frac{8}{3} \cdot \frac{a_0}{a_*^2} < 0$$

This predicts that $w$ was more negative in the past — qualitatively consistent with the DESI trend ($w_a < 0$).

---

## 3. Numerical Illustration

### 3.1 Setup

We integrate equations (EBC1)–(EBC2) in the matter-free limit ($\rho = p = 0$, $k = 0$), using dimensionless variables $x = a/a_*$ and $\tau = t\sqrt{\Lambda_0/3}$. With the state-dependent damping $\gamma(a) = \gamma_0|a/a_* - 1|$ from Section 2.2, the system reduces to:

$$x'' + \tilde{\gamma}|x - 1|\,x' = K\!\left(\frac{1}{x^2} - x\right) + K_b\left(\frac{x_\mathrm{min}}{x}\right)^{\!4} x$$

This is consistent with (EBC2): the term $\tilde{\gamma}|x-1|x'$ corresponds to $\gamma(a)H$ in dimensionless form, vanishing at equilibrium ($x=1$) and growing with displacement.

with dimensionless parameters $K$, $K_b = \Lambda_b/\Lambda_0$, $\tilde{\gamma} = \gamma/\sqrt{\Lambda_0/3}$, and $x_\mathrm{min} = a_\mathrm{min}/a_*$.

Numerical values used in the illustration: $x_\mathrm{min} = 0.01$, $K_b = 0.005$, $\tilde{\gamma} = 1.5 \times 10^{-3}$. Integration performed using a fourth-order Runge–Kutta method (scipy `solve_ivp`, `RK45`, $\mathrm{rtol} = 10^{-10}$, $\mathrm{atol} = 10^{-13}$).

### 3.2 Results

![Fig. 1a](EBC_fig1a_final.pdf){ width=100% }
![Fig. 1b](EBC_fig1b_final.pdf){ width=100% }

The integration demonstrates (Fig. 1):

- Strong initial acceleration from the bounce minimum.
- Repeated expansion–contraction phases with slowly decreasing amplitude.
- First expansion maximum at $x_\mathrm{max} \approx 1.73$.
- Cycle duration approximately constant across early cycles ($\Delta\tau \approx 4.87$).
- The bounce minimum increases slowly with each cycle due to damping ($x_\mathrm{min,k} \nearrow$), consistent with gradual structure preservation.

The "current epoch" marker is placed at the beginning of the 3rd cycle, at approximately 6–10% of the cycle duration. A note on the scale of this illustration: the illustrative bounce minimum of this integration lies at $x_\mathrm{bounce} \approx 0.515$, determined by energy conservation of the elastic term for $x_\mathrm{max} \approx 1.73$. The bounce term parameter $x_\mathrm{min} = 0.01$ acts as a singularity guard and is not active for this trajectory. The physical ratio $a_0/a_* \approx 0.06$–$0.15$ (Section 5) is much smaller than the illustrative bounce minimum, consistent with the current epoch lying very early in its cycle. The analytically derived equation of state $w_\mathrm{EBC} \approx -2/3$ holds in the limit $a_0/a_* \ll 1$ (Section 2.5) and is independent of the illustrated scale.

**Important caveat**: This numerical illustration omits matter and radiation. The cycle position estimate of 6–15% (Section 5) and the "current epoch" marker in Fig. 1 are therefore illustrative only — they represent the matter-free limit and should not be taken as quantitative predictions. Including standard matter ($\Omega_m \approx 0.31$) and radiation will modify both the cycle duration and the position estimate; this is identified as development item 3 in Section 8.

**Order-of-magnitude estimates of the corrections.** Although the full numerical integration with matter and radiation is deferred, the leading corrections can be estimated analytically. Matter enters (EBC2) as an additional attractive term $-4\pi G \rho_m/3$ that decelerates the early expansion while remaining negligible near the expansion maximum (where $\rho_m \propto a_*^{-3}$ is highly diluted). The ratio of the matter density to the EBC restoring term today is $\Omega_m/\Omega_\mathrm{EBC} \approx 0.31/0.69 \approx 0.45$; this ratio grows as $a^{-3}$ toward the past, making matter dominant in the early phase of each cycle. A rough estimate gives a correction factor of approximately:

$$\frac{T_\text{with matter}}{T_\text{matter-free}} \approx 1 + C \cdot \frac{\Omega_m}{\Omega_\mathrm{EBC}} \approx 1.15\text{--}1.25$$

where $C \approx 0.4$–$0.5$ accounts for the fact that matter is relevant only in the early phase of each cycle. The cycle duration estimate therefore increases by approximately **15–25%**: from $T \approx 90$–230 Gyr to $T \approx 105$–290 Gyr. Correspondingly, the cycle position $f = t_0/T$ shifts downward by a similar fraction, from 6–15% to approximately **5–13%** — qualitatively unchanged but toward the lower end of the current range. The expansion maximum $x_\mathrm{max} \approx 1.73$ changes by less than 5%, since matter is negligible there. Near the bounce, radiation ($\rho_r \propto a^{-4}$) adds a modest additional repulsive contribution that slightly increases $x_\mathrm{min}$, consistent with the bounce temperature estimate of Section 6.2. Crucially, the analytic prediction $w_0 = -2/3$ (Section 2.5) is independent of the numerical integration entirely and is unaffected by the inclusion of matter and radiation.

---

## 4. Observational Comparisons

### 4.1 Accelerated Expansion and DESI 2024

The currently observed accelerated expansion ($q_0 \approx -0.55$) is fully consistent with the EBC model: we are in the early rising phase of a cycle (estimated 5–13%, including the correction for matter content derived in Section 3.2), where the elastic restoring term drives positive acceleration. The acceleration will end when the expansion maximum $a_*$ is reached, several tens of billions of years in the future.

The DESI 2024 BAO results ($w_0 \approx -0.7$, $w_a \approx -0.65$, $2.5$–$3.9\sigma$ away from $\Lambda$CDM) provide observational motivation for dynamical dark energy models including EBC. The model's prediction $w_0 \approx -2/3$ lies within the DESI $1\sigma$ interval. These results remain to be confirmed by independent datasets; $\Lambda$CDM is not yet ruled out, and the DESI tension may partly reflect systematic effects. EBC is therefore presented as a framework consistent with emerging data, not as one confirmed by it.

### 4.2 Hubble Tension

The EBC framework offers a potential interpretation of the $H_0$ discrepancy: if the universe has undergone multiple cycles, slight geometric deformations from internal dynamics (structure formation, gravitational instabilities) will have accumulated, leading to spatially varying local expansion rates. The CMB-based $H_0$ measures a large-scale average; local distance-ladder measurements sample a smaller volume that may differ systematically. This interpretation is qualitative and requires quantitative development.

### 4.3 CMB Anomalies

The CMB shows several statistically significant anomalies unexplained within $\Lambda$CDM:

- **Quadrupole alignment** ("Axis of Evil"): The lowest multipole moments are anomalously aligned [21, 28].
- **Cold Spot** in Eridanus: Statistically significant cold region without standard explanation [26].
- **Anomalous bulk flows**: Coherent galaxy cluster motions on Gpc scales exceeding expected amplitudes [27].

In the EBC framework, geometric asymmetries accumulated across cycles provide a natural origin for these features. The current cycle need not be perfectly spherically symmetric; residual deformations from previous cycles are physically expected.

### 4.4 The Lithium-7 Problem

Standard BBN predicts Li/H $\approx (3\text{--}4) \times 10^{-10}$, while observations of old metal-poor stars give Li/H $\approx 1.6 \times 10^{-10}$ — a factor $\sim 2$–3 discrepancy [Cyburt et al. 2016].

EBC offers a physical mechanism: **selective nuclear photodisintegration at the bounce**. Different nuclides have different photodisintegration thresholds:

**Table 1: Photodisintegration temperatures of key nuclides**

| Nuclide | Photodisintegration temperature |
|---------|--------------------------------|
| Li-7 | $\approx 3$–$5 \times 10^9$ K |
| Deuterium | $\approx 6 \times 10^9$ K |
| He-4 | $\approx 2 \times 10^{10}$ K (much more stable) |

If the bounce temperature $T_\mathrm{bounce} \approx T_\mathrm{CMB} \cdot (a_0/a_\mathrm{min})$ falls in the range $\sim 10^9$–$10^{10}$ K, Li-7 is photodisintegrated while He-4 survives. BBN in the subsequent cycle then begins under He-4-enriched conditions, producing less Li-7.

This mechanism yields a correlated double prediction: (a) Li-7/H below the standard BBN value (observed, consistent), and (b) He-4 mass fraction $Y_p$ slightly above $0.2470$ due to the He-4 seed surviving the bounce. Current measurement: $Y_p = 0.2449 \pm 0.0040$ [Aver et al. 2015]. The central value lies below the predicted threshold of $0.2470$, placing the EBC prediction outside the $1\sigma$ range — this constitutes a genuine tension, not a confirmation. It may indicate that the bounce temperature is closer to the He-4 photodisintegration threshold than modelled, or that the $Y_p$ measurement will shift with higher-precision data. Future JWST spectroscopy of metal-poor HII regions at high redshift will be decisive. Notably, the Li-7 deficit and the elevated $Y_p$ prediction arise from the same mechanism and are jointly testable, which maximises the discriminating power of a future combined measurement.

### 4.5 Baryogenesis

The standard model of electroweak baryogenesis fails quantitatively: the CKM CP violation is $\sim 10^{10}$ times too small to produce the observed baryon asymmetry $\eta \approx 6.09 \times 10^{-10}$ [Sakharov conditions]. This is one of the genuine unsolved problems of the standard model.

**The role of bounce temperature.** A central constraint governs baryogenesis in any cyclic model: baryon-number-violating processes (electroweak sphalerons) are active only above the electroweak scale ($T \gtrsim 100$ GeV) and are exponentially suppressed below it. The current EBC bounce temperature of $T_\mathrm{bounce} \approx 4 \times 10^9$ K $\approx 0.3$ MeV lies approximately five orders of magnitude below this threshold. Sphaleron-driven baryogenesis at the bounce is therefore not available in the current or recent cycles. Correspondingly, the net baryon asymmetry $\eta$ is conserved through each bounce as a thermal relic — the bounce thermalizes baryonic structures but does not violate baryon number, consistent with the physical picture of Section 4.7.

**Time-pressure relaxation.** The key contribution of EBC to the baryogenesis problem is not a new production mechanism at the bounce, but a dramatic relaxation of the time constraint. Mechanisms such as leptogenesis via heavy neutrino decay or the Affleck–Dine mechanism do not require sphaleron temperatures; they require only sufficient time and a modest CP-violating rate. In the standard model, the entire available window is $\sim 13.8$ Gyr. In EBC, the full cycle duration of $T \approx 200$ Gyr is available, giving a required average production rate of:
$$\frac{d\eta}{dt} \approx \frac{6 \times 10^{-10}}{200 \times 10^9\ \mathrm{yr}} \approx 3 \times 10^{-21}\ \mathrm{yr}^{-1}$$
This rate is accessible to leptogenesis via heavy neutrinos or Affleck–Dine mechanisms, which fail in the standard model due to time pressure, not in principle. The same argument applies across multiple cycles: $\eta$ accumulates gradually within each cycle during the high-temperature early phase when baryon-number-violating processes are most active, and is then preserved intact through the bounce into the next cycle.

**The observed $\eta$ as a cumulative relic.** The observed asymmetry $\eta \approx 6.09 \times 10^{-10}$ is therefore the cumulative result of slow baryogenesis operating across multiple cycles. As a rough average, each of the $N = 3$ cycles contributes $\delta\eta \approx \eta/N \approx 2 \times 10^{-10}$ — though in practice the contribution was concentrated in the hot early phase of each cycle (when baryon-number-violating processes were most active) rather than distributed uniformly in time. The long-term thermal evolution described in Section 5.4 implies that the hottest, earliest cycles contributed disproportionately; the current and recent cycles contribute negligibly given their sub-MeV bounce temperatures. This picture is fully consistent with Section 4.7: just as black holes and alpha-elements survive the bounce physically, the net baryon asymmetry survives it thermodynamically as a conserved charge.

EBC does not solve the baryogenesis problem, but it reframes it: the question is not how $\eta$ was produced in 13.8 Gyr under extreme time pressure, but how a small CP-violating rate operated across two full cycles of $\sim 200$ Gyr each — a significantly less constrained problem accessible to known extensions of the standard model.

### 4.6 Large-Scale Structural Anomalies

The **Hercules–Corona Borealis Great Wall** ($\sim 3$ Gpc at $z \approx 2$) has been reported as approximately ten times the theoretical maximum scale of cosmic structures in $\Lambda$CDM, and would be difficult to form in 13.8 Gyr. We note that the statistical significance of this structure has been debated in the literature, and its reality as a single coherent structure is not universally accepted [see e.g. [29] vs. subsequent critiques]. If confirmed, it would be a natural relic structure in the cyclic model with $N \geq 3$ cycles.

**Primordial magnetic fields in intergalactic voids** ($\sim 10^{-16}$–$10^{-15}$ G, Fermi-LAT [23]) are unexplained in $\Lambda$CDM. In the cyclic model, they could be relic fields accumulated across multiple cycles.

### 4.7 Trans-Cyclic Inheritance: Black Hole Seeds, Chemical Enrichment, and the JWST Anomaly

*The following section develops a speculative but internally consistent extension of the EBC framework, exploring qualitative consequences of the bounce-filter mechanism across multiple cycles. It does not form part of the minimal mathematical core of EBC and should be read as a set of motivated conjectures rather than derived results.*

A distinctive and largely unexplored consequence of EBC's cyclic structure is the **accumulation of compact relics across cycles**. The bounce at $T_\mathrm{bounce} \approx 4 \times 10^9$ K acts as a selective physical filter (Section 4.4): ordinary stars, gas clouds, and light nuclei are fully thermalized, while compact objects whose internal energy scales far exceed the bounce temperature pass through unaffected.

**The bounce filter by object class.** Stellar-mass black holes evaporate via Hawking radiation [30] on timescales of order $10^{67}$ yr — approximately $10^{55}$ cycle durations. Supermassive black holes ($M \sim 10^9$–$10^{11}\ M_\odot$) persist for $\sim 10^{100}$ yr. Neutron stars survive on similar timescales. Dark matter halos interact only gravitationally and are merely compressed and re-expanded by the bounce. All of these survive every bounce essentially unchanged in mass, while normal baryonic structure is completely reset.

**Cycle 1 ($T \approx 200$ Gyr).** Beginning from a pure H/He gas with near-zero baryon asymmetry and no pre-existing structure, the first cycle has the full cycle duration to build complexity unimpeded. Population III stars — massive, metal-free, with lifetimes of $10^6$–$10^7$ yr — form and explode as supernovae within the first few hundred million years, seeding the intergalactic medium with C, N, O, Si and Fe while leaving stellar-mass black holes as remnants. Over $\sim 200$ Gyr, these stellar black holes merge hierarchically through successive galaxy-cluster collisions, producing supermassive black holes reaching $M \gtrsim 10^{11}\ M_\odot$ — far more massive than the $\sim 10^{9}\ M_\odot$ objects observed today at high redshift. Galactic dynamos amplify weak seed magnetic fields over billions of years in Cycle 1; in void regions, where no subsequent dynamo activity can destroy them, these fields survive the bounce as diluted relics into Cycle 2 and beyond. The observed $\sim 10^{-16}$–$10^{-15}$ G intergalactic void fields (Fermi-LAT [23]) are consistent with being precisely such Cycle-1 relics.

**Cycle 2 ($T \approx 180$ Gyr, slightly damped).** The re-expanding universe of Cycle 2 is not cosmologically virginal. It inherits from Cycle 1: (i) a population of black holes spanning stellar to supermassive masses, distributed throughout the re-forming large-scale structure; (ii) a dark-matter web of filaments and halos that never dissolved, providing an immediate gravitational scaffold; (iii) a chemical inventory dominated by He-4 (bounce-survivor), heavier alpha-elements (O, Si, Fe; bounce-survivors), and essentially zero Li-7 or deuterium (bounce-destroyed). Star formation in Cycle 2 is accelerated relative to Cycle 1: pre-existing BH seeds enable rapid assembly of active galactic nuclei, and the pre-existing DM scaffold guides baryons into halos faster than in a structurally empty universe.

**The JWST anomaly as a trans-cyclic prediction.** The James Webb Space Telescope has revealed massive, evolved galaxies and active supermassive black holes at redshifts $z > 10$ [31] — corresponding to less than 500 Myr after the Big Bang in the $\Lambda$CDM framework — that are difficult to account for by standard structure formation within a single 13.8 Gyr expansion history. These observations remain actively debated and some may be explicable within extended $\Lambda$CDM models. EBC provides a natural framework for understanding them: the supermassive black holes observed at $z > 10$ in Cycle 3 are consistent with being the direct descendants of the BH population assembled during Cycles 1 and 2, present at the beginning of Cycle 3 as pre-formed seed objects rather than grown from scratch within 13.8 Gyr. This constitutes a qualitative, falsifiable prediction: the mass function and spin distribution of high-redshift ($z > 10$) black holes should show a characteristic floor — a minimum mass set by the typical BH mass at the end of Cycle 2 — rather than the continuous bottom-up growth distribution expected in $\Lambda$CDM.

**Chemical imprint on ultra-metal-poor stars.** The EBC bounce filter also predicts a specific chemical signature in the most metal-poor stars of Cycle 3. Stars forming at the very beginning of Cycle 3 in regions not yet reached by Cycle-2 supernova ejecta should show the characteristic bounce-filter pattern: normal or elevated O, Si, and Fe (alpha-elements that survive the bounce), and anomalously suppressed Li, Be, and B (destroyed at the bounce temperature). This pattern is qualitatively distinct from standard Population III supernova yields and is jointly testable with JWST spectroscopy of $z > 5$ extremely metal-poor stars.

A summary of trans-cyclic inheritance is given in Table 2.

**Table 2: Trans-cyclic inheritance in the EBC framework ($N = 3$)**

| Inherited quantity             | Origin                       | Cycle 3 observational candidate  |
|--------------------------------|------------------------------|----------------------------------|
| Supermassive BH seeds | Cyclic BH growth (C1+C2) | JWST: massive BHs at $z > 10$ |
| Relic void magnetic fields | Cycle-1 galactic dynamos | Fermi-LAT: $\sim 10^{-16}$ G in voids |
| Pre-formed DM scaffold | DM halos (C1+C2) | Early large-scale structure |
| He-4 overabundance ($Y_p$) | Two bounce filters | $Y_p > 0.2470$ (prediction) |
| Li-7 deficit | Two bounce destructions | Cosmological lithium problem |
| Bounce-filter element pattern | Alpha-element survival | UMP stars at $z > 5$ (JWST) |

### 4.8 Horizon and Flatness Problems

Standard cosmology requires an inflationary phase to explain two otherwise finely tuned observations: the near-perfect isotropy of the CMB across regions that appear causally disconnected (horizon problem), and the near-exact spatial flatness of the universe ($|\Omega - 1| < 0.01$, flatness problem). EBC resolves both through its dynamical structure, without invoking an inflaton field.

**Horizon problem.** In standard Big Bang cosmology, the CMB photons arriving from opposite directions of the sky originated in regions whose light cones did not overlap at the time of last scattering — they were never in causal contact, yet their temperatures agree to one part in $10^5$. Inflation resolves this by exponentially stretching a small, causally connected region to encompass the entire observable universe.

In EBC, the resolution is more direct and follows from the bounce condition itself. At the bounce minimum $a = a_\mathrm{min}$, by definition $\dot{a} = 0$, and therefore the Hubble parameter $H = \dot{a}/a = 0$. The Hubble radius $d_H = c/|H| \to \infty$ at the bounce: the entire universe lies within a single causal volume at that moment. Every region of the observable universe was therefore in causal contact at the bounce, regardless of how large the universe had grown in the preceding expansion phase. CMB isotropy is not a fine-tuning coincidence but a direct consequence of the cyclic structure — the universe was thermalized to a common temperature at each bounce, and this thermal memory persists into the subsequent expansion. This argument is stronger than simply noting that regions were in contact during the compression phase: the divergence of the causal horizon at $H = 0$ is a universal feature of any non-singular bounce, independent of the details of the EBC potential.

**Flatness problem.** The density parameter $\Omega = \rho/\rho_\mathrm{crit}$ satisfies:
$$\Omega - 1 = \frac{kc^2}{a^2 H^2}$$
where $k$ is the spatial curvature. In standard cosmology, $(\Omega - 1) \propto a^2$ during matter domination and $\propto a$ during radiation domination — both growing with $a$, making $\Omega = 1$ an unstable fixed point. Any initial departure from flatness grows over time, requiring extreme fine-tuning of the early universe to explain the observed $|\Omega_0 - 1| < 0.01$.

During the EBC contraction phase, the evolution is reversed. From the Friedmann equation, $H^2 \propto \rho$, so $a^2 H^2 \propto a^2 \rho$. For matter domination ($\rho \propto a^{-3}$) this gives $a^2 H^2 \propto a^{-1}$, and therefore:
$$(\Omega - 1) = \frac{kc^2}{a^2 H^2} \propto a \to 0 \quad \text{as } a \to a_\mathrm{min}$$
For radiation domination ($\rho \propto a^{-4}$), $a^2 H^2 \propto a^{-2}$, so $(\Omega - 1) \propto a^2 \to 0$ even faster. Any initial curvature, whether positive or negative, is dynamically driven toward zero during the contraction phase — $\Omega = 1$ becomes an **attractor** rather than an unstable fixed point. This is a general feature of contracting cosmologies and applies directly to EBC: each contraction phase resets the curvature toward flatness without requiring any initial fine-tuning. After $N = 3$ cycles of contraction and expansion, the residual departure from flatness is suppressed by repeated application of this attractor mechanism, making the observed $|\Omega_0 - 1| < 0.01$ a natural outcome.

**Comparison with inflation.** Inflation resolves both problems through exponential expansion driven by a scalar field with a specific potential — a mechanism that introduces its own fine-tuning (the inflaton potential must be extremely flat) and has not been directly observed (no primordial gravitational waves detected, $r < 0.036$). EBC resolves both problems through the geometry of the bounce itself, without additional fields or fine-tuning, and is consistent with $r \approx 0$ as a structural prediction (Section 6.2, Prediction 4). A direct comparison with other bounce cosmologies on these points is given in Section 7.

---

## 5. Cycle Duration and Position Estimates

### 5.1 Simple Estimate from Cycle Position

From $T = t_0 / f_\mathrm{cycle}$:

| Assumed $f$ | Cycle duration $T$ |
|-------------|-------------------|
| 6% | 230 Gyr |
| 10% | 138 Gyr |
| 15% | 92 Gyr |

**Probable range: $T \approx 90$–230 Gyr.**

### 5.2 Constrained Estimate from $H_0 \cdot t_0$

For a matter-free sinusoidal oscillation with $a_\mathrm{min} \approx 0$, the following relation holds:

$$H_0 \cdot t_0 \approx \varphi \cdot \tan\!\left(\frac{\varphi}{2}\right), \quad \varphi = 2\pi f$$

With the observed $H_0 \cdot t_0 \approx 0.95$ (dimensionless), numerical solution gives $\varphi \approx 0.9$–$1.3$ rad, i.e., $f \approx 15$–$21\%$. For realistic $a_\mathrm{min} > 0$, the effective phase decreases to $f \approx 6$–$15\%$.

A full solution requires the system of three equations:

$$\begin{aligned}
H_0 &= \frac{A\omega\sin\varphi}{a_\mathrm{min} + A(1-\cos\varphi)}, \\
q_0 &= -\frac{A\omega^2\cos\varphi \cdot [a_\mathrm{min} + A(1-\cos\varphi)]}{[A\omega\sin\varphi]^2}, \\
T   &= \frac{2\pi t_0}{\varphi}
\end{aligned}$$

with unknowns $\{\varphi, A/a_\mathrm{min}, \omega\}$. This requires an additional constraint, ideally the jerk parameter $j_0$ (see Section 6.3).

### 5.3 Cycle Number

Evidence for $N \geq 3$ cycles:

| Observation                                    | Inferred $N$ | Strength        |
|------------------------------------------------|--------------|-----------------|
| CMB isotropy (good thermal reset) | $N \leq 4$ | limits high $N$ |
| CMB quadrupole anomaly | $N \geq 3$ | weak |
| Hercules–CrB Great Wall | $N \geq 3$–4 | moderate |
| Primordial void magnetic fields | $N \geq 3$ | moderate |
| Li-7 problem (selective bounce) | $N \geq 3$ | weak–moderate |
| Baryogenesis (slow accumulation over $N$ cycles, no time pressure) | $N \geq 2$ | weak–moderate |
| JWST: massive BHs and galaxies at $z > 10$ | $N \geq 2$ | moderate–strong |

Current data support $N = 3$ or $N = 4$. The true total age of the universe would then be:

$$t_\mathrm{total} \approx (N-1)\cdot T + t_0 \approx \begin{cases} 474\ \mathrm{Gyr} & (N=3,\ T=230\ \mathrm{Gyr}) \\ 704\ \mathrm{Gyr} & (N=4,\ T=230\ \mathrm{Gyr}) \end{cases}$$

**Inter-cyclic chemical and structural enrichment.** The argument for $N \geq 3$ is strengthened by considering what each cycle deposits for the next (Section 4.7). The bounce filter at $T_\mathrm{bounce} \approx 4 \times 10^9$ K destroys all light nuclei (Li, Be, B, D) and all stellar structures, while preserving black holes, neutron stars, dark matter halos, and the heavier alpha-elements (O, Si, Fe) locked in compact remnants. After $N-1$ complete cycles, three cumulative effects are expected:

First, the **black hole mass function** shifts upward with each cycle. A supermassive black hole assembled over 200 Gyr in Cycle 1 persists into Cycle 2 as a pre-formed seed, enabling rapid AGN activity and massive galaxy assembly far earlier in Cycle 2 than pure bottom-up growth from stellar remnants would permit. By Cycle 3, seed BHs from both prior cycles are available at the start of the expansion — offering a direct and parameter-free explanation for the JWST observations of $M > 10^8\ M_\odot$ black holes at $z > 10$, which are difficult to produce within a single 13.8 Gyr history under standard $\Lambda$CDM growth models.

Second, the **He-4 mass fraction $Y_p$** increases monotonically with $N$: each bounce destroys H and light elements while leaving He-4 intact, and stellar nucleosynthesis within each cycle converts additional H into He-4. The prediction $Y_p > 0.2470$ (Section 4.4) becomes more stringent with increasing $N$, providing an in-principle constraint on cycle number from future precision helium abundance measurements.

Third, the **dark matter scaffold** is never reset. DM halos from Cycles 1 and 2 are compressed and re-expanded by the bounce but retain their mass and approximate topology. Cycle 3 structure therefore forms on an inherited gravitational skeleton, accelerating the assembly of galaxies and clusters relative to a universe starting from a smooth initial state. This may contribute to the observed early emergence of large-scale structure in JWST data and to anomalies in the matter power spectrum at large scales.

The upper limit $N \leq 4$ is set by CMB isotropy: each cycle accumulates geometric asymmetries (Section 4.3) which would progressively distort the CMB if too many cycles preceded the current one. A large $N$ would produce observable CMB anisotropy incompatible with Planck data, providing a complementary constraint. The combination $N = 3$ remains the preferred value, with $N = 4$ marginally consistent.

### 5.4 Long-Term Evolution: Threshold Cascade

*The following section extrapolates the EBC framework to timescales far beyond any observational reach. It is presented as a structurally motivated consequence of the damping term, not as an empirical prediction. Quantitative details are strongly model-dependent.*

The damped oscillator structure of EBC implies that the bounce temperature decreases monotonically across cycles. This has a concrete physical consequence: several distinct physical processes — each governed by its own temperature threshold — cease permanently in succession as the system evolves toward equilibrium at $a_*$.

**Bounce temperature evolution.** From the EBC equations, the restoring energy at the bounce minimum scales as $E \sim \Lambda_0/a_\mathrm{min}$. Under damping with rate $\gamma$, the amplitude of oscillation decays and $a_\mathrm{min}$ increases correspondingly. In the weakly damped limit, the bounce temperature decreases geometrically across cycles:

$$T_\mathrm{bounce}(N) \approx T_\mathrm{bounce,0} \cdot e^{-\alpha N}$$

where $\alpha$ is the effective per-cycle damping fraction, related to the dimensionless damping parameter $\tilde{\gamma}$ of (EBC2) by $\alpha \approx \pi \tilde{\gamma}$ for a weakly damped oscillator (one cycle reduces the amplitude by $e^{-\pi\tilde{\gamma}}$). With $\tilde{\gamma} = 1.5 \times 10^{-3}$ from the numerical illustration, $\alpha \approx 5 \times 10^{-3}$. The number of cycles before a given physical threshold $T_\mathrm{thr}$ is permanently crossed is:

$$N_\mathrm{thr} \approx \frac{1}{\alpha}\ln\!\left(\frac{T_\mathrm{bounce,0}}{T_\mathrm{thr}}\right)$$

**The four-phase cascade.** Three successive thresholds define qualitatively distinct cosmological eras:

| Phase                           | $T_\mathrm{bounce}$ | Physics at bounce                                  | Cycle estimate            |
|---------------------------------|---------------------|----------------------------------------------------|---------------------------|
| **I — current** | $\gtrsim 10^9$ K | BBN, selective photodisintegration, He-4 enrichment | $N \lesssim 1.4/\alpha$ |
| **II — post-BBN** | $3000\text{--}10^9$ K | Full plasma, CMB forms; no new nucleosynthesis | $1.4/\alpha \lesssim N \lesssim 14.8/\alpha$ |
| **III — post-plasma** | $\ll 3000$ K | No plasma phase; no new CMB surface of last scattering | $N \gtrsim 14.8/\alpha$ |
| **IV — asymptotic** | $\to T_\mathrm{eq}$ | $a_\mathrm{min} \to a_*$; static equilibrium | $N \to \infty$ |

For the current epoch ($N = 3$), the proximity of $T_\mathrm{bounce} \approx 4 \times 10^9$ K to the BBN threshold of $\sim 10^9$ K — a factor of only $\sim 4$ — implies that we are near the **end of Phase I**. The transition to Phase II, where bounces are hot enough to form plasma and generate a new CMB but no longer drive nucleosynthesis, will occur within $N_\mathrm{BBN} - 3 \approx (1.4/\alpha) - 3$ further cycles. For $\alpha \sim 10^{-3}$, this is $\mathcal{O}(10^3)$ cycles or $\mathcal{O}(200\,\mathrm{Tyr})$ in the future.

**A compounding effect from compact relic accumulation.** The estimate above assumes that the thermally available gas fraction remains constant across cycles. In practice, an additional process accelerates the cascade: with each cycle, an increasing fraction of baryonic matter becomes locked in black holes and neutron stars (Section 4.7), which survive the bounce thermally inert. This progressive depletion of the ionizable gas fraction effectively reduces the optical depth of the plasma phase even before the bounce temperature itself falls below the ionization threshold of hydrogen ($\sim 10^4$ K). The two effects — falling $T_\mathrm{bounce}$ and falling gas fraction — compound, shortening the Phase I–II and Phase II–III transitions relative to the single-process estimate above. A quantitative treatment of this compound decay requires a model for the rate of baryon locking per cycle, which is beyond the scope of the present work and is identified as a topic for future development.

**Observational irrelevance, structural relevance.** Phase III and IV are far beyond any observational horizon and have no direct empirical consequences. Their significance is structural: the EBC framework has a natural, thermodynamically motivated endpoint — a static, black-hole-dominated universe at scale $a_*$ — without invoking a Big Rip, a Heat Death in the $\Lambda$CDM sense, or any external cutoff. The cascade from Phase I to Phase IV is a direct consequence of the damping term $-\gamma H$ introduced in Section 2.2, closing the thermodynamic accounting of the framework.

## 6. Testable Predictions and Comparison with $\Lambda$CDM

### 6.1 Summary Comparison

| Quantity                  | $\Lambda$CDM | EBC ($a_0 \ll a_*$) | DESI 2024      |
|---------------------------|--------------|---------------------|----------------|
| $w_0$ | $-1$ (exact) | $\mathbf{-2/3 \approx -0.667}$ | $-0.70 \pm 0.10$ $\checkmark$ |
| $w_a$ | 0 | $< 0$ ($w$ rises with $a$) | $-0.65 \pm 0.25$ $\checkmark$ |
| Singularity | yes | **no** ($a_\mathrm{min} > 0$) | — |
| Monotonic expansion | yes | **no** (turning point) | — |
| Inflation | required field | time-dilation artifact | — |

### 6.2 Falsifiable Predictions

1. **$w_0 \approx -2/3$**: Parameter-free prediction. Euclid and DESI Year 5 can test this at $<5\%$ precision.

2. **Monotonically rising $w(a)$**: $w$ should increase from $-2/3$ toward 0 as $a \to a_*$. The sign of $w_a$ is already indicated in DESI data.

3. **Jerk parameter $j_0 < 1$**: The jerk parameter $j_0 \equiv \dddot{a}\,a^2/\dot{a}^3$ provides the strongest near-term discriminant. In $\Lambda$CDM, $j_0 = 1$ exactly for a flat universe with a true cosmological constant. In EBC, differentiating (EBC2) with respect to time and expressing the result in terms of $w_\mathrm{EBC}(a)$ and $\Omega_\mathrm{EBC}$:
$$j_0 = 1 + \frac{9}{2}w_\mathrm{EBC}(1 + w_\mathrm{EBC})\,\Omega_\mathrm{EBC} + \frac{3}{2}\frac{dw_\mathrm{EBC}}{d\ln a}\,\Omega_\mathrm{EBC}$$
Using $w_\mathrm{EBC} \approx -2/3 + (4/3)x^2$ and $dw/d\ln a \approx (8/3)x^2$ for $x \ll 1$, and noting that $\Omega_\mathrm{EBC} \approx \Omega_\Lambda \approx 0.68$ today:
$$j_0(\mathrm{EBC}) \approx 1 - \frac{1}{6}\Omega_\mathrm{EBC}\cdot O(x^2) < 1$$
The deviation from unity is of order $f_\mathrm{cycle}^2 \sim 10^{-3}$–$10^{-2}$, small but in principle measurable with Rubin LSST and DESI Year 5 supernova samples. A complete derivation including matter is deferred to future work.

4. **No primordial gravitational waves**: Consistent with the non-detection $r < 0.036$ (BICEP/Keck 2021), since inflation in EBC is a time-dilation artifact, not an independent field. This prediction acquires quantitative support when the bounce energy scale is estimated directly from the model.

   **Bounce temperature and minimum scale factor.** The Li-7 photodisintegration mechanism (Section 4.4) constrains the bounce temperature to $T_\mathrm{bounce} \approx 3$–$5 \times 10^9\ \mathrm{K}$. Using $T \propto a^{-1}$ and $T_\mathrm{CMB} = 2.725\ \mathrm{K}$:
   $$\frac{a_\mathrm{min}}{a_0} = \frac{T_\mathrm{CMB}}{T_\mathrm{bounce}} \approx \frac{2.725}{4 \times 10^9} \approx 7 \times 10^{-10}$$
   The corresponding energy scale at the bounce is $k_\mathrm{B} T_\mathrm{bounce} \approx 0.3\ \mathrm{MeV}$ — squarely in the regime of nuclear physics, not quantum gravity.

   **Correspondence to standard cosmological epochs.** In the $\Lambda$CDM timeline, a temperature of $\sim 4 \times 10^9\ \mathrm{K}$ corresponds to $t \approx 1$–$20$ seconds after the Big Bang — the onset of Big Bang Nucleosynthesis, not the inflationary epoch. Standard inflation requires energy scales of order $10^{15}$–$10^{16}\ \mathrm{GeV}$ (GUT scale) to $10^{19}\ \mathrm{GeV}$ (Planck scale). The EBC bounce operates approximately $10^{19}$–$10^{22}$ times below these scales. Since the tensor-to-scalar ratio satisfies $r \propto (H_\mathrm{inf}/m_\mathrm{Pl})^2$, and the effective Hubble rate at the EBC bounce is set by the MeV-scale temperature, EBC predicts $r \ll 10^{-10}$ — effectively zero for any foreseeable experiment.

   **Finite initial oscillation energy.** EBC does not require the first bounce to have occurred at the Planck density. The minimum scale factor is determined by the initial oscillation energy $E_0$ of the elastic spatial mode — a finite quantity that need not approach the Planck regime. This is structurally distinct from Loop Quantum Cosmology, where the bounce is triggered specifically by Planck-scale quantum geometry effects. In EBC, $E_0$ is a free parameter of the framework, which in a multiverse context could take different values across different realizations, producing universes with different cycle amplitudes, durations, and — through the BBN mechanism — different light-element abundances. The non-detection of primordial gravitational waves is thus not a coincidence in EBC but a direct structural consequence of the sub-Planck bounce energy scale.

5. **Directional $H_0$ variations**: Systematic differences in $H_0$ across sky directions should be detectable with future precision measurements.

6. **Correlated Li-7/He-4 signal**: Li-7/H below standard BBN and $Y_p > 0.2470$, both arising from the same bounce-photodisintegration mechanism; jointly testable with JWST.

7. **Li-7 redshift gradient**: Primordial Li-7 at $z > 5$ should differ systematically from values at $z \approx 2$–3.

---

## 7. Comparison with Bounce Cosmologies

```{=latex}
\scriptsize
\rowcolors{2}{gray!12}{white}
```

| Aspect          | EBC (this work)   | LQC             | CCC (Penrose)   | Ekpyrotic       |
|-----------------|-------------------|-----------------|-----------------|-----------------|
| Bounce mechanism | Dynamic $\Lambda_\mathrm{EBC}(a)$ (phenomenological) | Quantum gravity | Conformal transition | Membrane collision |
| Singularity avoidance | $a_\mathrm{min} > 0$ by postulate + bounce term | Planck density quantum effects | Conformal rescaling | Slow contraction |
| Inflation | Time-dilation artifact | Bounce replaces inflation | Not required | Not required |
| Dark energy | Dynamic space property | Cosmological constant | Not primary focus | Not primary focus |
| Equation of state | $w_0 = -2/3$ (analytic) | Unspecified | Not primary | Unspecified |
| Entropy treatment | Structure as damping | Uncertain | Reset via conformal transition | Low-entropy cycles |
| Horizon problem | $H=0$ at bounce $\Rightarrow$ $d_H \to \infty$ (causal reset) | Pre-bounce causal contact | Conformal continuity | Causal contact in contraction |
| Flatness problem | $\Omega \to 1$ attractor during contraction | Addressed via quantum geometry | Not primary | Attractor during ekpyrotic contraction |
| Primordial GW ($r$) | $r \approx 0$ (sub-MeV bounce, structural) | Model-dependent | Not primary | $r \approx 0$ (slow contraction) |
```{=latex}
\normalsize
\rowcolors{0}{}{}
```

---

## 8. Limitations and Required Development

The present framework is explicitly phenomenological. The following issues require resolution before it can be considered a complete physical theory:

1. **Covariant embedding**: The modification $\Lambda_\mathrm{EBC}(a)$ must be derived from a modified Einstein–Hilbert action:
$$G_{\mu\nu} + \Lambda_\mathrm{EBC}(g_{\mu\nu}, R_{\mu\nu\alpha\beta})\,g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu}$$
Defining $\Lambda_\mathrm{EBC}$ as a function of curvature scalars would place the framework on a rigorous covariant footing.

2. **External reference time $\tau_\mathrm{ext}$**: The postulated decoupling of the space oscillation from internal relativistic time requires formal definition. A preliminary formulation: $a(\tau_\mathrm{int}) = a(\tau_\mathrm{ext}) \cdot [\text{time-dilation factor}(\rho)]$, where $\tau_\mathrm{int}$ is Robertson–Walker coordinate time. This remains to be made precise.

3. **Matter and radiation**: The numerical integration (Section 3) omits matter and radiation. The matter term $-4\pi G\rho_m/3$ in (EBC2) is technically straightforward to include — it requires adding standard $\rho \propto a^{-3}$ and $\rho \propto a^{-4}$ components and re-integrating the dimensionless ODE. Analytic order-of-magnitude estimates (Section 3.2) suggest the cycle duration increases by approximately 15–25% and the cycle position estimate shifts to $f \approx 5$–13%, while the expansion maximum and the analytic $w_0 = -2/3$ prediction remain essentially unchanged. A full numerical integration with matter and radiation is required before the cycle duration and position estimates can be compared quantitatively with observational data.

4. **CMB acoustic physics**: The bounce scenario must reproduce the observed CMB peak positions ($\ell \approx 220, 540, 800$). It must be shown that the acoustic physics of the pre-bounce plasma generates the same signature as standard recombination.

5. **Entropy budget**: The damping term $-\gamma H$ must be thermodynamically consistent. A full treatment must demonstrate $\Delta S > 0$ over cycles.

6. **Quantitative $q_0$ reproduction**: The deceleration parameter must be quantitatively matched by including matter ($q_0 = \Omega_m/2 - \Omega_\Lambda \approx -0.55$). This is straightforward in principle but requires the full (EBC1) including $\rho$.

7. **Bounce mechanism from first principles**: The bounce term $\Lambda_b \propto a^{-4}$ is motivated by its radiation-like scaling but lacks a microscopic derivation.

8. **Continuous versus impulsive energy injection**: An alternative class of bounce models could in principle restrict the injection of oscillation energy to the bounce phase alone, with the elastic term absent during the expansion and contraction phases. In EBC this possibility is excluded by construction: the analytic derivation of $w_0 = -2/3$ (Section 2.5) depends on $\Lambda_\mathrm{EBC}(a)$ being active at all times — it follows from the logarithmic derivative $d\ln\Lambda_\mathrm{EBC}/d\ln a$ evaluated at the present epoch. A purely impulsive (bounce-only) energy injection would remove the elastic term from the current epoch, making the parameter-free prediction $w_0 = -2/3$ unattainable and requiring a separate dark energy mechanism. The continuous elastic term is therefore not an optional feature but a structural necessity of the framework. The microscopic origin of this always-active geometric elasticity — and its relationship to the bounce mechanism — remains an open question for future development.

---

## 9. Conclusion

We have presented Elastic Bounce Cosmology, a phenomenological framework in which cosmic expansion is governed by modified Friedmann equations incorporating a dynamic elastic restoring force. The framework produces quasi-cyclic scale factor evolution without singularities and yields the parameter-free prediction $w_0 = -2/3$, consistent with DESI 2024 at $1\sigma$.

The model addresses several open problems of standard cosmology within a unified conceptual framework. Dark energy is reinterpreted as a dynamic geometric property of space rather than a vacuum energy field. The Hubble tension is attributed to spatial inhomogeneities accumulated across cycles. The lithium-7 problem is explained by selective nuclear photodisintegration at the bounce, with a correlated He-4 overabundance prediction testable with JWST. Baryogenesis is reframed as slow accumulation over extended cycle durations, relaxing the severe time-pressure constraint of standard electroweak baryogenesis. The horizon and flatness problems are resolved through the bounce geometry itself: $H = 0$ at the bounce renders the causal horizon infinite, and the contraction phase drives $\Omega \to 1$ as a dynamical attractor — both without invoking an inflaton field.

A significant new result developed in this work is the **trans-cyclic inheritance framework** (Section 4.7): the bounce acts as a selective physical filter that thermalizes ordinary baryonic matter while leaving compact relics — black holes, neutron stars, and dark matter halos — essentially unchanged. This leads to a natural explanation for the JWST observations of massive black holes and galaxies at $z > 10$: these objects are the direct descendants of black hole populations assembled during prior cycles. The same framework predicts a characteristic element abundance pattern in ultra-metal-poor stars and implies a monotonically increasing He-4 mass fraction with cycle number.

The long-term evolution of EBC follows a **threshold cascade** (Section 5.4): as the bounce temperature decays geometrically across cycles, successive physical processes — nucleosynthesis, plasma formation, CMB emission — cease permanently in sequence, with the framework asymptotically approaching a static, black-hole-dominated equilibrium at scale $a_*$.

EBC explicitly does not replace General Relativity but parametrizes possible additional contributions to large-scale background evolution. Several of its qualitative predictions are testable with near-future instruments: Euclid, DESI Year 5, and Rubin LSST for the jerk parameter $j_0 < 1$, $w_0$, and $w_a$; JWST for the correlated Li-7/He-4 signal, ultra-metal-poor star abundances, and the high-redshift black hole mass function; and BICEP/CMB-S4 for the continued non-detection of primordial gravitational waves.

The jerk parameter $j_0$ remains the most accessible near-term discriminant: EBC predicts $j_0 < 1$, while $\Lambda$CDM requires $j_0 = 1$ exactly.

---

## Acknowledgment

The author acknowledges the use of AI-assisted tools (Claude, Anthropic; ChatGPT, OpenAI) in structuring and refining this manuscript, formalizing the mathematical framework, linking to the observational literature, and translating from German. The conceptual framework — all scientific ideas, physical intuitions, and the ten postulates underlying EBC (listed in Appendix A) — originates with the author. Full editorial responsibility rests with the author.

---

## Appendix A: The Ten Postulates of EBC

The following ten postulates constitute the original conceptual foundation from which the EBC framework was developed. They are listed here in their original form, with references to the sections of the paper where each postulate is developed or used.

**P1 — Intrinsic expansion; dark energy as a spatial property.**
The expansion of space in the universe depends only weakly on its material content. So-called dark energy does not exist as a separate constituent within the universe. Expansion is a property of space itself and is not dominated by the energy content it contains. *(Section 2.1, 2.3)*

**P2 — Damped oscillation; no collapse to singularity.**
At the formation of space — commonly referred to as the Big Bang — space began expanding from a highly compressed state, eventually reaching a maximum extent before contracting again. The scale-factor/time diagram follows a damped oscillation: space does not collapse back to a singularity, but reaches its turning point at a finite, non-zero minimum scale. *(Sections 2.1, 2.2)*

**P3 — External reference time.**
The timescale for the expansion of space is independent of the progression of time within space. The oscillation of space proceeds at a uniform rate in an external reference frame, decoupled from relativistic coordinate time inside the universe. *(Section 2.1)*

**P4 — CMB formation only in early cycles.**
In the first cycles, matter is compressed at the bounce minimum to a sufficient density and temperature that it becomes opaque to radiation, allowing the cosmic microwave background to form. Beyond a certain cycle, the bounce no longer reaches the temperatures required for plasma formation, and no new CMB can emerge. *(Section 5.4)*

**P5 — Progressive structural preservation.**
Depending on the cycle, fewer and fewer structures are destroyed at the expansion minimum. Ultimately, the oscillation of space will have almost no influence on its contents — compact remnants and large-scale structures are increasingly preserved across bounces. *(Sections 4.7, 5.4)*

**P6 — Non-spherical expansion from cycle 2 onwards.**
From at least the second cycle, the universe cannot be assumed to expand as a perfect sphere. Events within space introduce slight deformations of the spatial geometry, which may also imply that space does not expand at exactly the same rate everywhere, with small local differences possible. *(Sections 4.2, 4.3)*

**P7 — Inflation only at the start of the first cycle.**
The inflationary phase occurred only at the beginning of the first cycle. It does not repeat in subsequent cycles. *(Sections 1.2, 6.2)*

**P8 — Inflation as a time-dilation artifact.**
Inflation appears as a very rapid expansion within a short time interval because that time is relativistic: due to the extreme mass/energy concentration, internal time passes quasi-not-at-all, or extremely slowly. By virtue of P3, the expansion of space proceeds uniformly from the perspective of the external frame. *(Section 2.1)*

**P9 — Baryogenesis distributed over cycles.**
The matter/antimatter paradox is resolved because the formation of the matter/antimatter imbalance can extend across the entire first cycle, or even across multiple cycles. The time-pressure constraint that makes standard electroweak baryogenesis so difficult is thereby removed. *(Section 4.5)*

**P10 — The universe is finite.**
From the preceding postulates it follows: the universe is finite in size. A maximum scale $a_*$ exists beyond which the elastic restoring force reverses the expansion. The universe does not expand indefinitely. *(Sections 2.1, 2.3)*

---

## References

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

*This paper presents a conceptual framework with a minimal mathematical core (Sections 2.2–2.5). It requires further mathematical development — in particular a covariant embedding — as well as peer review.*
