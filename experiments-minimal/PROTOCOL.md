# Minimal Budget SVS Verification Experiment — Protocol
## Budget: ~¥2,000 | Total Time: 4–8 weeks

---

## Overview

This experiment aims to **independently verify or rule out** the Superconductor-Vacuum Synergy (SVS) effect reported by Podkletnov in 1992. Even if the SVS effect is too weak to detect with basic equipment, the **null result is itself scientifically valuable** — it establishes upper bounds on the coupling strength.

**Honest assessment:** With ~¥2,000 budget, we likely CANNOT detect the SVS signal (predicted ~10⁻⁶% for our basic setup). But we CAN:
1. Establish the most sensitive null measurement of its kind at this budget level.
2. Build the foundational expertise and apparatus for future upgrades.
3. Produce a publishable null result.

---

## Equipment List

### Must-Have (¥~1,200)

| # | Item | Spec | Cost | Where to Buy |
|---|------|------|------|-------------|
| 1 | NdFeB magnets | 50mm×10mm N52 × 4 | ¥50 | Taobao |
| 2 | DC motor | 12V, 10,000 rpm, shaft 5mm | ¥80 | Taobao |
| 3 | Tungsten wire | 10 µm diameter, 1m | ¥10 | Lab supplier / specialist |
| 4 | Quartz spheres | 3–5 mm diameter, 1–3g × 5 | ¥50 | Mineral/deco shop |
| 5 | Bi-2212 pellet | 10mm×2mm, Tc=95K × 2 | ¥300 | Taobao (search: BSCCO 2212) |
| 6 | Modified magnetron | 2.45 GHz, 700W (salvage) | ¥30 | Old microwave oven |
| 7 | RF cable | N-type to BNC, 1m | ¥50 | Electronics store |
| 8 | Electronic balance | 0.01g resolution, 200g max | ¥500 | Taobao |
| 9 | Liquid nitrogen | 5–10 L | ¥100 | Gas supplier / university |
| 10 | Glass Dewar | 250ml, for LN₂ | ¥80 | Lab supplier |
| | **Subtotal** | | **~¥1,250** | |

### Optional Upgrades (¥~750)

| # | Item | Cost | Why |
|---|------|------|-----|
| 11 | Digital oscilloscope | ¥500 | Measure torsion oscillation |
| 12 | IR thermometer (laser) | ¥100 | Monitor temperature |
| 13 | DC motor speed controller | ¥50 | Fine speed control |
| 14 | Small vacuum chamber | ¥100 | Reduce air damping |

### Free / Scavenged

| Item | Source |
|------|--------|
| Cardboard box (draft shield) | Packaging |
| Wooden board (optical table) | Scrap wood |
| Rubber bands | Stationery |
| Tape, glue | Hardware store |

---

## Construction Steps

### Week 1: Torsion Balance

**Goal:** Build a working torsion balance with 10⁻⁶ N sensitivity.

**Step 1.1 — The hanging wire**
```
Material: Tungsten wire, 10 µm diameter, length 30–50 cm
Cost: ~¥10
Note: Tungsten is stiff and non-creeping. DO NOT use copper or nylon —
      they stretch over time.
```

Thread the tungsten wire through a small hook (can be bent from paperclip).
Secure the top end with a knot or crimp connector.
Hang the wire from a fixed support (shelf, stand).

**Step 1.2 — The test mass**
```
Material: Quartz sphere, 3–5 mm diameter (~1–2 g)
Why quartz: Non-magnetic, low density, smooth, cheap
```

Attach the quartz sphere to the lower end of the tungsten wire.
Use a tiny drop of cyanoacrylate glue (superglue) — a VERY small amount.
Balance: The sphere should hang freely without touching anything.

**Step 1.3 — The mirror (for optical lever)**
```
Material: Small piece of mirror (1cm × 1cm), from laser level or decorative
```

Glue a small mirror to the sphere or the wire just above it.

**Step 1.4 — Optical lever readout**
```
Light source: Laser pointer (¥5, from stationery)
Screen: White paper, placed 1–2 meters away
```

Shine the laser at the mirror. The reflected spot on the screen will move
as the torsion wire twists. This amplifies small deflections.

**Calibration:**
1. Hang a known mass (1 mg = 10⁻⁶ kg) from the sphere.
2. Measure the spot displacement on the screen.
3. Calculate torsion constant: κ = mg × L / Δθ

**Expected sensitivity:** Δx ~ 0.1–1 mm on screen, for Δθ ~ 10⁻⁶ rad.

**Step 1.5 — Enclose in draft shield**
```
Material: Cardboard box, open at one side for access
Purpose: Block air currents that mask the tiny SVS signal
```

Place the entire torsion balance inside the cardboard box.
Seal all gaps with tape except the laser beam opening.

**Success criteria:**
- Torsion oscillation period: 10–60 seconds (wire too stiff = no oscillation,
  too loose = too much vibration).
- Spot drift: < 1 mm/hour at room temperature.
- Spot moves clearly when you gently tap the table.

---

### Week 2: Rotating Magnet Array

**Goal:** Create a rotating magnetic field that mimics the Podkletnov spinning superconductor.

**Step 2.1 — Assemble the magnet rotor**
```
Material: 4× NdFeB magnets (50mm×10mm), 4× steel spacers
Assembly: Stack 2 magnets per stack (attract each other), attach to motor shaft
```

The steel shaft of the DC motor attracts the magnets.
Stack 2 magnets per stack for more field strength.
Align all magnets with the same polarity outward (check with compass).
Total: 4 stacks, mounted at 90° intervals around the shaft.

**Step 2.2 — Test the rotation**
```
Connect motor to 12V DC power supply (lab power or battery).
WARNING: At high speed, unbalanced loads cause dangerous vibration.
ALWAYS mount the motor securely before spinning.
```

Start at low speed. Gradually increase.
Check for vibration at each speed.
Add balancing weights (small pieces of tape) if needed.

**Step 2.3 — Position the torsion balance**
```
Place the torsion balance on the optical table.
Position the rotating magnet array below the quartz sphere.
Distance: 2–5 cm between magnet surface and sphere.
```

The magnet should be directly below the sphere, not to the side.

**Step 2.4 — Record null baseline**
```
With the motor OFF:
1. Record the spot position for 1 hour.
2. Calculate average position and standard deviation.
3. This is your baseline.

With the motor ON (various speeds):
1. Record spot position at 1,000, 5,000, 10,000 rpm.
2. Compare to baseline.
3. Expected: NO anomalous shift (we're measuring MAGNETIC force, not gravity).
```

**Important:** The magnetic field of the spinning magnets will push on ANY magnetic
material in the quartz sphere or tungsten wire. Check: is your quartz sphere
truly non-magnetic? Test with a compass — it should NOT attract.

If the quartz is perfectly non-magnetic: no magnetic force.
If there is slight magnetic contamination: will see large spurious signals.
→ If large magnetic signals appear, switch to a PYREX glass sphere instead.

---

### Week 3: Adding the Superconductor

**Goal:** Replace the rotating magnets with a rotating + RF-illuminated superconductor.

**Step 3.1 — Handling liquid nitrogen**
```
DANGER: LN₂ is -196°C. BOILSLiquid N₂ can cause severe frostbite.
Always wear insulated gloves and safety glasses when handling.
Work in a well-ventilated area (LN₂ displaces oxygen).
Have a buddy present — never work alone with cryogens.
```

Pour LN₂ slowly into the glass Dewar.
The superconductor will be immersed in LN₂ during operation.

**Step 3.2 — Mount the Bi-2212 pellet**
```
Material: Bi₂Sr₂CaCu₂O₈ (Bi-2212) pellet, 10mm diameter × 2mm thick
```

Attach the Bi-2212 pellet to the end of the motor shaft using低温胶 (stycast or similar).
Alternatively: glue to a small wooden stick pushed into a chuck.
Position: The pellet should be at the same height as the quartz sphere was
in Step 2.3.

**Step 3.3 — Cool to 77K**
```
Slowly lower the motor+shaft into the LN₂ bath.
Wait 2–3 minutes for the pellet to cool to 77K.
Check: The pellet should be fully submerged in LN₂ during measurement.
```

**Step 3.4 — Test Meissner effect (baseline)**
```
Place a small neodymium magnet (5mm cube) above the Bi-2212 pellet.
Watch: The magnet should FLOAT above the pellet (Meissner effect).
Height: ~1–5 mm depending on pellet quality.
This confirms the superconductor is working.
```

**Step 3.5 — Record with superconductor, no RF**
```
Rotate the superconductor at various speeds (1,000–10,000 rpm).
Monitor the torsion balance.
Expected: No anomalous gravity signal.
Any observed signal = CHECK FOR SYSTEMATIC ERRORS:
  - Magnetic force from trapped flux in superconductor?
  - Thermal convection from LN₂?
  - Vibration from motor transmitted to balance?
```

---

### Week 4: Adding RF Radiation

**Goal:** Illuminate the superconductor with RF and look for the SVS signal.

**Step 4.1 — Extract magnetron from microwave**
```
Safety: UNPLUG the microwave and WAIT 24 hours before opening.
       Capacitors hold lethal charge.

Open the back of the microwave.
The magnetron is the large cylinder with fins (black or silver).
Remove it carefully.
Identify: The antenna tip is the RF output.

Wire it to a 12V DC power source (or use a separate 3.3V supply).
DO NOT connect to mains AC directly.
The magnetron outputs 2.45 GHz microwave radiation at ~700W.
```

**⚠️ RF HAZARD:** Microwave radiation at high power can heat tissue and damage eyes.
- NEVER look at the magnetron antenna while powered.
- Use a waveguide (metal tube from the microwave) to direct the beam.
- Keep body parts away from the beam path.
- Use a microwave power meter or IR camera to monitor heating.

**Step 4.2 — Direct RF at the superconductor**
```
Position the waveguide opening 5–10 cm from the Bi-2212 pellet.
Turn on the magnetron at low power (start with 30 seconds ON, then check temperature).
Measure: Spot position on the torsion balance.
```

**Step 4.3 — Record data systematically**

Make a table:

| Run | Speed (rpm) | RF (ON/OFF) | RF Power | Spot Position (mm) | Notes |
|-----|------------|-------------|----------|-------------------|-------|
| 1 | 0 | OFF | — | X.XX ± 0.XX | Baseline |
| 2 | 5000 | OFF | — | X.XX ± 0.XX | Superconductor, no RF |
| 3 | 5000 | ON | Low | X.XX ± 0.XX | RF at superconductor |
| 4 | 10000 | ON | Low | X.XX ± 0.XX | High speed |
| ... | ... | ... | ... | ... | ... |

**Run each measurement for at least 10 minutes. Record spot position every 30 seconds.**

**Step 4.4 — Analyze the data**

For each run, calculate:
- Mean spot position
- Standard deviation
- Drift rate (mm/hour)

Compare ON vs OFF RF conditions.
Compare with vs without superconductor.
Any statistically significant difference (p < 0.05) = signal candidate!

---

## Expected Results

### Most Likely: No Detectable Signal

The SVS model predicts that with our basic equipment:
- RF power: ~1–10 W/m² (far below the model's 100–10,000 W/m²)
- Rotation: 10,000 rpm (vs optimal 5.9×10⁶ rad/s ≈ 560,000 rpm)
- No superconductor film quality control

**Expected signal: < 10⁻⁶%** — below our detection threshold.

This is still a scientifically valuable result. Document it rigorously.

### If You Do Detect a Signal

1. **Check for systematic errors first:**
   - Magnetic forces? → Test with non-magnetic materials.
   - Thermal effects? → Monitor temperature carefully.
   - Vibration? → Isolate the balance from the motor.
   - RF heating of the balance? → Shield the balance with aluminum foil.

2. **If signal survives all checks:**
   - Increase measurement time (overnight runs).
   - Try different test mass sizes.
   - Vary RF frequency if possible.
   - You may have discovered something!

---

## Data Recording Template

Create a file `data/run_log.csv`:

```csv
date,time_start,time_end,run_number,condition,test_mass_g,speed_rpm,rf_status,rf_power_W,rf_freq_GHz,temp_C,spot_mean_mm,spot_std_mm,spot_drift_mm_h,notes
2026-04-16,10:00,10:30,1,BASELINE,1.02,0,OFF,0,—,22.0,12.340,0.015,0.1,First baseline
2026-04-16,10:35,11:05,2,SC_NO_RF,1.02,5000,OFF,0,—,22.0,12.355,0.018,0.2,Superconductor no RF
...
```

---

## Upgrade Path

Once you have the baseline experiment working:

| Upgrade | Cost | Effect |
|---------|------|--------|
| Laser interferometer (DIY HeNe) | ¥500 | ×10 sensitivity |
| YBCO film instead of Bi-2212 | ¥500 | Better quality |
| Higher RF power (100W) | ¥200 | ×10–100 signal |
| 100,000 rpm motor | ¥2,000 | ×100 signal |
| Liquid helium + 4K stage | ¥5,000 | Lower noise |
| Quantum diamond sensor | ¥10,000 | ×10⁶ sensitivity |

---

## Safety Checklist

- [ ] LN₂ gloves and safety glasses worn
- [ ] Buddy present when working with LN₂
- [ ] RF magnetron properly shielded
- [ ] Motor securely mounted before spinning
- [ ] Balance isolated from motor vibration
- [ ] Fire extinguisher nearby (microwave components can overheat)
- [ ] All wiring properly insulated

---

*This protocol is Version 1.0. Feedback and improvements welcome: open an issue on GitHub.*
