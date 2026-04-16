# SVS Simulations

This directory contains three Python models for the anti-gravity SVS research.

## Running the Models

```bash
# All models require Python 3.7+
pip install numpy matplotlib scipy

# Run SVS model (main model)
python3 svs_model.py

# Run Casimir force model
python3 casimir_model.py

# Run GEM gravitomagnetic model
python3 gem_model.py
```

## Model Descriptions

### svs_model.py — Superconductor-Vacuum Synergy Model
The main SVS model, calibrated from the Podkletnov 2% experiment.
- RF parameter scans (frequency, power)
- Temperature dependence
- Multi-layer amplification
- Optimal conditions prediction

### casimir_model.py — Casimir Force Array Model
Tests whether pure Casimir repulsion can explain the Podkletnov effect.
- Nanocavity enhancement factors
- Multi-layer amplification
- Casimir force vs plate separation
- **Conclusion:** Casimir alone is ~10⁹× too weak.

### gem_model.py — Gravitoelectromagnetic Model
Tests whether the GEM gravitomagnetic field alone can explain Podkletnov.
- Quantum coherence amplification
- Multi-layer GEM effects
- **Conclusion:** GEM alone is ~10⁻¹⁶% effective.

## Model Validation

The SVS model reproduces the Podkletnov 2% signal at baseline parameters:
- Podkletnov params: ω=524 rad/s, P_RF=100 W/m², f=16 GHz, T=77K
- Model output: Δg/g ≈ 1.1% (reported: 2%, order of magnitude agreement)

## Citation

If you use these models, cite:
Wen Tian (2026). GitHub: https://github.com/wenti-research/anti-gravity-svs
