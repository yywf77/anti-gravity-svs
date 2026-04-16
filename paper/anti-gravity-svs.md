# Gravity Reduction via Superconductor-Vacuum Synergy: Theoretical Framework and Experimental Predictions

**Author:** Ask-Ask-Ask (Wen Tian)
**Date:** April 16, 2026
**Contact:** wenti.research@proton.me
**GitHub:** https://github.com/wenti-research/anti-gravity-svs
**arXiv:** (pending — check repository for latest version)

---

## Abstract

We present a theoretical framework for a **Superconductor-Vacuum Synergy (SVS)** effect, in which a rotating superconductor illuminated by radio-frequency (RF) radiation produces a measurable reduction in the apparent gravitational acceleration of nearby test masses. By calibrating against the seminal Podkletnov experiment (1992), which reported a ~2% gravitational reduction, we derive a characteristic SVS acceleration ω_SVS ≈ 0.196 m/s², corresponding to an effective vacuum coupling length ξ_vac ≈ 0.6 m. The SVS force obeys:

```
F_SVS = m_test × ω_SVS × (ξ_eff/ξ₀) × N^γ     [γ ≈ 1.5]
```

Three key predictions are made: (i) RF power in the range 10³–10⁴ W/m² at 10–20 GHz yields detectable enhancement; (ii) the effect scales linearly with test mass, confirming a modification of gravitational mass rather than an external force; (iii) multi-layer stacks amplify the effect as N^γ (γ ≈ 1.5). A minimal-budget (~¥2,000) tabletop experiment using rotating permanent magnets and a precision balance is proposed for independent verification. All simulation code is open-sourced at https://github.com/wenti-research/anti-gravity-svs.

---

## 1. Introduction

The possibility of modifying gravitational attraction has intrigued physicists since Einstein. In 1992, Podkletnov and Nieminen reported a surprising result: a rotating YBa₂Cu₃O₇ (YBCO) disc, when exposed to RF radiation, appeared to reduce the weight of a test mass above it by approximately 2%.

Despite follow-up attempts (Hathaway 2003, Unnikrishnan 2004), no independent lab has reproducibly confirmed the effect. Three considerations motivate a re-examination:

1. The original experiment was never published under truly controlled conditions.
2. Modern precision measurement techniques are far more sensitive than in 1992.
3. High-Tc superconducting films are now commercially available at modest cost.

Here we develop the quantitative SVS theoretical framework and make specific, falsifiable predictions.

---

## 2. Ruling Out Existing Explanations

### 2.1 Pure GEM Gravitomagnetic Field

The GEM equations predict for Podkletnov geometry (M ≈ 0.1 kg, ω = 524 rad/s, r = 0.1 m):

```
B_g ≈ 7 × 10⁻²³ s⁻¹
```

With quantum coherence amplification (κ² ~ 10⁴, Li-Torr-deWit), the induced horizontal gravitational acceleration is ~10⁻¹⁶% — effectively zero.

**Conclusion: Pure GEM is ruled out.**

### 2.2 Pure Casimir Repulsion

The Casimir-Lifshitz force at d = 100 nm is F/A ~ 10⁻⁷ N/m². To levitate a 70 kg person requires 1372 N/m² — eleven orders of magnitude more. Even with:
- Nano-cavity field enhancement: ×10³
- 500-layer stack: ×500
- Total amplification: ~10⁶ — still falls short by 10⁵.

**Conclusion: Pure Casimir repulsion is ruled out.**

---

## 3. The SVS Mechanism

The intersection of two failed routes points to a synergistic coupling. We propose three effects combine:

**S1 — Rotating Cooper pairs generate a GEM field** (weak alone).

**S2 — RF radiation drives the superconductor into a non-equilibrium macroscopic quantum coherent state**, dramatically increasing the effective coherence length ξ_eff ≫ ξ₀.

**S3 — The GEM field couples to the vacuum energy density modified by the coherent superconductor state**, producing a feedback loop that amplifies the effective gravitational modification over a macroscopic spatial scale ξ_vac ~ 0.6 m.

The key calibration from Podkletnov:

```
F_SVS(obs) = 9.8 × 10⁻⁵ N = ω_SVS × m_test
ω_SVS ≈ 0.196 m/s²
```

This implies ξ_vac ~ 0.6 m (for ξ₀ ~ 3 nm, giving χ ~ 10⁸).

---

## 4. The SVS Equation

The SVS force formula:

```
F_SVS = m_test × ω_SVS × (ξ_eff/ξ₀) × N^γ

Where:
• ω_SVS ≈ 0.196 m/s² — calibrated from Podkletnov 2% data
• ξ_eff — RF-enhanced effective coherence length [m]
• ξ₀ — intrinsic superconducting coherence length [m]
• N — number of superconductor layers
• γ ≈ 1.5 — cooperative amplification index (mean-field estimate)
```

The factor (ξ_eff/ξ₀) encodes RF enhancement of coherence length.
The factor N^γ encodes inter-layer cooperative amplification.

---

## 5. Numerical Model

The complete Python simulation is in `simulations/svs_model.py`.

**Baseline YBCO parameters (77 K):**

| Parameter | Value |
|-----------|-------|
| Tc | 93 K |
| n_s | 5.3 × 10²⁷ m⁻³ |
| ξ₀ | 1.5 nm |
| λ_L | 150 nm |
| Disk radius | 25 mm |
| Disk thickness | 5 mm |

**Model results at Podkletnov parameters:**

| Condition | Δg/g (1g mass) |
|-----------|-----------------|
| Podkletnov baseline (ω=524, P_RF=100 W/m², f=16GHz) | **1.10%** |
| RF ×100 (P_RF=10,000 W/m²) | **5.04%** |
| Optimal rotation (ω=5.9×10⁶ rad/s) | **40%** |
| N=10 layers, γ=1.5 | ~13% |
| N=100 layers, optimal params | ~400% |

**Caution:** Predictions for N > 10 are extrapolations beyond the calibration point and require experimental verification.

---

## 6. Experimental Predictions

### P1: RF Frequency Resonance
The SVS signal peaks at **f_RF ≈ 10–20 GHz**, with Q ~ 10².
*Test:* RF frequency scan from 1 MHz to 100 GHz.

### P2: RF Power Threshold
Below P_RF ~ 100 W/m²: Δg/g ∝ P_RF (linear).
Above P_RF ~ 10,000 W/m²: saturation or nonlinearity.
*Test:* RF power scan from 0.1 W to 1 kW.

### P3: Mass Independence
Δg/g is independent of test mass m_test.
*Test:* Compare 1 g vs 10 g test masses. If different % → force, not gravity modification.

### P4: Multi-Layer Amplification
Δg/g ∝ N^γ, γ ≈ 1.5.
*Test:* Measure N = 1, 2, 5, 10, 20 layers.

### P5: Critical Rotation
Non-analytic change near ω ~ 10⁵–10⁶ rad/s.
*Test:* Rotation speed scan from 1,000 to 100,000 rpm.

---

## 7. Minimal Budget Experiment Protocol

**Total budget: ~¥2,000 / ~$300 USD**

### Materials

| Item | Cost | Source |
|------|------|--------|
| NdFeB magnets (50mm×10mm) × 4 | ¥50 | Taobao / Amazon |
| DC motor (12V, 10,000 rpm) | ¥80 | Electronics store |
| Tungsten wire (10 µm, 1m) | ¥10 | Lab supplier |
| Quartz spheres (1–5 g) | ¥50 | Mineral shop |
| Bi₂Sr₂CaCu₂O₈ pellet (10mm×2mm) | ¥200 | Taobao |
| Modified microwave magnetron (RF 2.45 GHz) | ¥30 | Salvaged microwave |
| RF waveguide and coax cable | ¥100 | Electronics store |
| Electronic balance (0.01 g resolution) | ¥500 | Taobao |
| Liquid nitrogen (10 L Dewar) | ¥100 | Gas / university lab |
| Glass bell jar (optional) | ¥100 | Hardware store |
| Draft enclosure (cardboard + foam) | ¥0 | Homemade |
| **Total** | **~¥1,220** | |

### Step 1: Null Baseline (Week 1)
1. Set up torsion balance with quartz mass.
2. Measure baseline oscillation frequency.
3. Rotate magnets (no superconductor, no RF) → record signal.
4. This establishes the null reference.

### Step 2: Superconductor Control (Week 2)
1. Cool Bi-2212 pellet to 77 K (liquid nitrogen).
2. Measure magnetic levitation height (Meissner effect baseline).
3. Rotate at 10,000 rpm without RF.
4. Expected: No anomalous gravity signal.

### Step 3: SVS Measurement (Week 3–4)
1. Illuminate Bi-2212 with RF at 2.45 GHz (magnetron), power ~1–10 W.
2. Measure torsion balance deflection.
3. Expected signal: ~10⁻⁶% (below detection threshold with basic equipment).
4. This is a meaningful null result — it establishes upper bounds.

### Step 4: Upgrade Path
- Replace torsion balance with laser interferometry → sensitivity 10⁻⁹ g.
- Replace Bi-2212 with YBCO film → higher Tc.
- Increase rotation speed → 100,000 rpm.
- Increase RF power → 100 W.

---

## 8. Limitations

1. **Single calibration point:** ω_SVS is derived from Podkletnov's 2% figure. If that measurement contains systematic error, the model is systematically biased.

2. **RF enhancement is phenomenological:** The equation ξ_eff = ξ(T) × f(P_RF) has not been derived from first principles. A microscopic theory of RF-enhanced macroscopic coherence is needed.

3. **Extreme predictions:** The model's prediction of complete levitation for N ~ 100 layers under optimal parameters is an extrapolation ~10²–10³ beyond the calibration range.

4. **Room-temperature requirement:** Achieving significant effects at room temperature requires a room-Tc superconductor — not yet available as of 2026.

---

## 9. Conclusion

The SVS framework provides the first quantitative, falsifiable theoretical structure for Podkletnov-class experiments. We have:

- Ruled out pure GEM and pure Casimir routes.
- Established a self-consistent SVS equation calibrated from experimental data.
- Made 5 specific, falsifiable predictions.
- Designed a ~¥2,000 tabletop verification experiment.
- Open-sourced all code for independent verification.

**Either the SVS effect is real, in which case we have found a new window into quantum gravity — or it is not, in which case this is the most thorough analysis ruling out these routes.**

We invite independent experimental groups to attempt verification.

---

## References

Full bibliography: `refs/references.bib`

Key references:
- Podkletnov & Nieminen, Physica C 203, 441 (1992)
- Li & Torr, Phys. Rev. D 43, 457 (1991); Phys. Rev. B 46, 5489 (1992)
- Harris, arXiv:gr-qc/9904009 (1999)
- Munday et al., Nature 457, 170 (2009)
- Verlinde, JHEP 2011, 029 (2010)
- Hathaway, arXiv:hep-ex/0202014 (2003)
- Geng et al., Nature (2025) [Ni-based superconductors]

---

## How to Cite

```
Wen Tian (2026). Gravity Reduction via Superconductor-Vacuum Synergy: 
Theoretical Framework and Experimental Predictions.
GitHub: https://github.com/wenti-research/anti-gravity-svs
arXiv: [pending]
```

---

*Conducted independently without institutional funding. All results are open and reproducible.*
