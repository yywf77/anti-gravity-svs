# 🔬 Anti-Gravity SVS: Superconductor-Vacuum Synergy Research

> **Can a superconductor, a microwave emitter, and a fast spinner reduce gravity?**
> 
> We built the theory. We need you to test it.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-Preprint-orange.svg)](https://arxiv.org)
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)

---

## What is this?

In 1992, Russian physicist Evgeny Podkletnov reported that a rotating YBCO superconductor illuminated by radio-frequency (RF) radiation reduced the weight of a nearby object by **~2%**. No independent lab has confirmed it. The result was largely dismissed.

We spent two weeks analyzing the physics. Here's what we found:

**Two popular explanations are mathematically ruled out:**

| Route | Calculation | Verdict |
|-------|------------|---------|
| Pure GEM gravitomagnetic field | ~10⁻¹⁶% effect | ❌ Dead end |
| Pure Casimir repulsion | Needs 10⁹× unknown amplification | ❌ Dead end |
| **Superconductor-Vacuum Synergy (SVS)** | ~1.1% (calibrated) | ✅ Only viable route |

The SVS mechanism proposes that **rotating Cooper pairs + RF radiation + quantum vacuum coupling** combine to genuinely modify the local gravitational field — without violating any known physics.

---

## The SVS Equation

```
F_SVS = m_test × ω_SVS × (ξ_eff/ξ₀) × N^γ    [Newman form]
```

Where:
- `ω_SVS ≈ 0.196 m/s²` — characteristic SVS acceleration (calibrated from Podkletnov 2%)
- `ξ_eff/ξ₀` — RF-enhanced coherence length ratio
- `N^γ, γ≈1.5` — multi-layer cooperative amplification
- `F_SVS ∝ m_test` — **the effect is linear in test mass**, confirming gravity modification (not a force)

### Key Predictions

| # | Prediction | Test |
|---|-----------|------|
| P1 | RF resonance peak at **10–20 GHz** | RF frequency scan |
| P2 | Gravity reduction independent of test mass | Vary mass 1g–10g |
| P3 | Multi-layer amplification: `Δg/g ∝ N^1.5` | Test N=1,2,5,10 |
| P4 | Optimal rotation: `ω ~ 10⁵–10⁶ rad/s` | Rotation speed scan |
| P5 | Saturation above `P_RF ~ 10⁴ W/m²` | RF power scan |

---

## Repository Structure

```
anti-gravity-svs/
├── README.md
├── LICENSE (MIT)
├── paper/
│   ├── anti-gravity-svs.md          ← Full paper (Markdown, arXiv-ready)
│   ├── anti-gravity-svs.tex         ← LaTeX source
│   └── refs/references.bib          ← BibTeX
├── simulations/
│   ├── svs_model.py                 ← Core SVS model (Python)
│   ├── casimir_model.py             ← Casimir force model
│   ├── gem_model.py                 ← GEM gravitomagnetic model
│   └── README.md                    ← How to run simulations
├── experiments-minimal/
│   ├── PROTOCOL.md                  ← Step-by-step experimental protocol
│   ├── BILL_OF_MATERIALS.md        ← Budget breakdown
│   └── DATA_SHEET.md               ← Recording templates
└── docs/
    ├── THEORY.md                   ← Full theoretical derivation
    ├── RF_DYNAMICS.md              ← RF-superconductor analysis
    └── predictions.md              ← All 5+1 predictions, how to test each
```

---

## Quick Start (Python)

```bash
git clone https://github.com/wenti-research/anti-gravity-svs.git
cd anti-gravity-svs/simulations

# Run SVS model
python3 svs_model.py

# Expected output: ~1.1% at Podkletnov parameters (ω=524 rad/s, P_RF=100 W/m²)
```

Sample output:
```
Podkletnov baseline: 1g → 1.10% gravity reduction
RF @ 10 kW/m²:       1g → 5.04% gravity reduction
N=100 layers, γ=1.5: 1g → 4.0×10⁵ % (needs verification)
```

---

## The Minimal Budget Experiment

**Total cost: ~¥2,000 / ~$300 USD**

Can verify or rule out the SVS effect with equipment available from regular universities or hobbyist suppliers:

| Item | Cost | Source |
|------|------|--------|
| NdFeB magnets × 4 | ¥50 | Taobao/Amazon |
| DC motor (12V, 10k rpm) | ¥80 | Electronics store |
| Tungsten wire (10 µm) | ¥10 | Lab supplier |
| Quartz spheres (1–5 g) | ¥50 | Mineral shop |
| Bi-2212 superconductor pellet | ¥200 | Lab supplier |
| Modified microwave magnetron (RF source) | ¥30 | Salvaged microwave |
| Electronic precision balance (0.01g) | ¥500 | Taobao |
| Liquid nitrogen (10L) | ¥100 | Gas supplier |
| **Total** | **¥1,020** | |

See `experiments-minimal/PROTOCOL.md` for full step-by-step procedure.

---

## Current Status

| Milestone | Status |
|-----------|--------|
| SVS theory (literature review + derivation) | ✅ Complete |
| Numerical model (Python, reproducible) | ✅ Complete |
| arXiv preprint | 📝 Draft ready |
| Minimal budget experiment protocol | ✅ Complete |
| Independent verification | ⏳ Needed |

---

## Why Should You Care?

**If the SVS effect is real:**
- A new form of gravity modification without exotic materials
- Portable anti-gravity devices for space, transportation, medicine
- A window into quantum gravity from tabletop experiments

**If the SVS effect is NOT real:**
- This is the most thorough theoretical analysis ruling out GEM + Casimir routes
- Saves the physics community decades of dead-end exploration
- Establishes clear upper bounds on superconductor-gravity coupling

Either way, this is publishable, citable science.

---

## Contributing

We welcome contributions from:
- 👩‍🔬 **Experimental physicists** — run the protocol and report results
- 👨‍💻 **Theoreticians** — improve the SVS mathematical framework
- 🛠️ **Engineers** — build the experiment or improve the RF system
- 📝 **Writers** — improve the paper's clarity and technical precision

**Open an issue** if you want to:
- Report results (positive or negative!)
- Propose improvements to the experiment
- Point out errors in the theory
- Suggest collaborators or funding sources

---

## License

MIT — use it, improve it, but please cite if you build on this work.

---

## Contact

- Email: `wenti.research@proton.me`
- GitHub Issues: [Open a ticket](https://github.com/wenti-research/anti-gravity-svs/issues)
- arXiv preprint: Coming soon (check back)

---

*This project is conducted independently without institutional funding. All results are open and reproducible.*
