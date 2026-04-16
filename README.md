# Anti-Gravity SVS: Superconductor-Vacuum Synergy

> Can a superconductor, a microwave emitter, and a fast spinner reduce gravity?

**Status:** Theory complete | Code: Open source | Experiment: Protocol ready

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## Quick Links

| Document | What It Is |
|----------|------------|
| `paper/anti-gravity-svs.md` | Full arXiv preprint draft (read this first) |
| `paper/anti-gravity-svs.tex` | LaTeX source |
| `simulations/svs_model.py` | Main Python model (run it!) |
| `experiments-minimal/PROTOCOL.md` | Zero-budget experiment (¥2,000) |
| `README-github.md` | Full repository documentation |

---

## What We Found

Two popular explanations for the Podkletnov 2% gravity reduction are mathematically ruled out:

| Route | Calculation | Verdict |
|-------|------------|---------|
| Pure gravitomagnetic field | ~10⁻¹⁶% | ❌ Dead end |
| Pure Casimir repulsion | Needs 10⁹× unknown boost | ❌ Dead end |
| **Superconductor-Vacuum Synergy (SVS)** | **~1.1%** (calibrated) | ✅ Only viable route |

**Core equation:**
```
F_SVS = m_test × 0.196 m/s² × (ξ_eff/ξ₀) × N^1.5
```
Calibrated from Podkletnov 2% data.

## Run the Model

```bash
git clone https://github.com/wenti-research/anti-gravity-svs.git
cd anti-gravity-svs/simulations
python3 svs_model.py
```

## Do the Experiment

Budget: **¥2,000 / ~$300** | Protocol: `experiments-minimal/PROTOCOL.md`

See [README-github.md](README-github.md) for full documentation.
