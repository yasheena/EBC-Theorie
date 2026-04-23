# Elastic Bounce Cosmology (EBC)

**A cyclic cosmological model with a parameter-free dark energy prediction**

> **w₀ = −2/3** — consistent with DESI 2024 (w₀ = −0.70 ± 0.10 at 1σ)

---

## Overview

Elastic Bounce Cosmology (EBC) extends the standard Friedmann equations by an
elastic cosmological term Λ_EBC(a) and a state-dependent damping term. The
universe undergoes repeated expansion–contraction cycles; the Big Bang is
reinterpreted as an elastic rebound from a previous contraction phase.

**Key features:**
- No initial singularity — the elastic term becomes repulsive under compression
- No separate dark energy entity — accelerated expansion emerges from Λ_EBC(a)
- Parameter-free prediction: w₀ = −2/3 (derived analytically, not fitted)
- Current epoch placed in the 3rd cycle, at ~4–8% of cycle duration
- Cycle duration T ≈ 180–320 Gyr (with matter and radiation)

---

## The Core Equations

**EBC1 (modified Friedmann):**

$$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho + \frac{\Lambda_0}{3}\left(\frac{a_*}{a} - \frac{a}{a_*}\right)$$

**Modified cosmological term:**

$$\Lambda_\mathrm{EBC}(a) = \Lambda_0\left(\frac{a_*}{a} - \frac{a}{a_*}\right)$$

where a* is the expansion maximum. At a ≪ a* this gives an effective equation
of state w₀ = −2/3 (derived from the continuity equation: ρ_EBC ∝ a⁻¹).

---

## Status

| Item | Status |
|------|--------|
| Paper (English) | ✅ Published on Zenodo |
| Paper (German) | ✅ Added to Zenodo record |
| Numerical integration (matter-free) | ✅ In paper Section 3 |
| Numerical integration (with matter) | ✅ See `Numerik/` |
| Peer review | 🔲 Not yet submitted |

---

## Publication

**Zenodo:** [https://doi.org/10.5281/zenodo.19399593](https://doi.org/10.5281/zenodo.19399593)

**ORCID:** [0009-0006-9810-7819](https://orcid.org/0009-0006-9810-7819)

**Contact:** ebc@wm0.eu

---

## Repository Structure

```
EBC-Theorie/
├── Paper/            # EBC_paper_v2.md (EN), EBC_paper_v2_DE.md (DE)
├── Numerik/          # Python scripts and plots
│   └── Ergebnisse/   # Generated figures (PDF/PNG)
├── Erweiterungen/    # Planned extensions and theoretical notes
├── Outreach/         # Contact log (emails, forums)
└── Kontext/          # Session summaries and working notes
```

---

## Relation to Other Cyclic Models

| Model | Bounce mechanism | Dark energy |
|-------|-----------------|-------------|
| **EBC** | Elastic term Λ_EBC(a) | Emergent (w₀ = −2/3) |
| Loop Quantum Cosmology | Quantum geometry | External Λ |
| Ekpyrotic / Steinhardt-Turok | Membrane collision (M-theory) | Scalar field |
| Conformal Cyclic Cosmology (Penrose) | Conformal rescaling | — |

---

## Author

Wolfgang Mattis — independent researcher, Leipzig, Germany.
Background: electrical engineering and software development;
~25 years of interdisciplinary self-study in physics and cosmology.

*This work was developed with AI assistance (Claude, Anthropic).
All physical postulates, intuitions and decisions are the author's own.*

---

## License

The paper text and derivations are © Wolfgang Mattis.
The Python scripts in `Numerik/` are released under the MIT License.
