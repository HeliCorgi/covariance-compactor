# STEP 3 RESULTS — kill-test verdicts (FINAL, post-adversarial-review)

Negative-result report. Pre-registrations: `STEP3_PREREG.md` (written before
evidence gathering; unmodified). Evidence: `data/raw/step3_evidence.json`
(six research tasks; every finding labeled web-verified / training-data /
not-found with URL). Adversarial review: two independent skeptical reviewers;
all defects and dispositions in §6. Seed 20260705 throughout. New code:
`step3_value/` (~175 lines incl. a beam patch; over the ~150 guidance, the
overage is the pre-registered weight computation).

## Verdict summary

| Task | Pre-registered kill threshold | Result | Verdict |
|---|---|---|---|
| **Task 1** (spin-knowledge / dossier value) | defensible upper end of program-level dossier value < $15M (sens. $20M) → line dead | decision-relevant (actual-funding) world: **$0–2M**; hypothetical consent-unlocked $500M-pipeline world: $3–20M (corner ~$30M) — indeterminate there; prereg-literal (coherence-unconstrained) reading: ~$36M, would NOT trip (§1, §6-D1) | **TRIPPED in the decision-relevant world** (alternates disclosed) |
| **Task 2** (Gate 5 erosion) | ground ≥80% of value-weighted dossier at <$100k/object → line dead | G = **0.21–0.66** across the defensible weighting range; only a spin-only weighting trips (0.85), and Task 1's anchor rejects that weighting | **NOT TRIPPED** (robust) |
| Task 3 (value-weighted Gate 2/6) | segment soft-kill: loaded >$3M or advantage <5×; slip criterion ≥8 | value coverage F1 ≤ 0.28 / F2 ≤ 0.32; SL-8 tour = 0.000 of value; SL-16 loaded $2.60–3.40M, advantage 4.4–9.6× (**straddles both clauses** at 24 mo); slip 9/9/10/9 → robust | soft-kill straddle on the value segment; feasibility PASS robust and value-empty |

**Decision: do not build Phases 3–4.** Task 1 trips in the world the campaign
would actually launch into; even the readings under which it does not trip
leave a program whose optimistic corner (~$20–36M) barely exceeds its own
loaded cost ($13–20M) while its realizable value in the current world is
$0–2M, its affordable tour carries zero measured value, and its value-bearing
segment straddles its own pre-registered economic soft-kill. The
characterization line, as scoped in the fixed Step-1 brief (cluster-tour
inspector, VoI-primary), is dead.

---

## 1. Task 1 — detumble / spin-knowledge cost anchor

### Anchored constant [evidence: data/raw/step3_evidence.json]

- e.Deorbit designed its arm to capture Envisat (~8 t) **at the full measured
  tumble rate** (~3°/s) inside a 5°/s any-axis envelope, detumbling the stack
  after capture; the envelope corner (195 vs 176 Nm joint torque) — not the
  measured spin — sized the hardware, and the margin is thin, not comfortable
  [web-verified, frobt.2018.00100]. ADRAS-J2 baselines the benign measured
  motion, with thruster-plume detumble documented as *contingency only*
  [web-verified, SDC9-paper121].
- Detumble impulse arithmetic (reviewer-verified): fastest observed SL-16
  (78 s period) has H ≈ 6.5 kN·m·s → ~3.3 kN·s ≈ 1.5 kg propellant
  [assumption: 2 m arm, Isp 220 s]. The continuous cost is ops time and risk:
  order 0.01–0.1 $M/kN·m·s.
- **Anchored bracket 0.004–0.1 $M/kN·m·s** (upper extended from 0.05 to 0.1
  per review §6-D5). The Step-2 "1.0" branch is a category error — it priced
  the *binary envelope-exceedance risk* as a continuous rate cost; that risk
  is priced separately below.

### Mechanical rerun (`.venv/Scripts/python.exe -m study2_voi.run`, seed
20260705, branches [0.004, 0.05, 0.1, 1.0]) [measured]

| branch | evidential value gain | true spin-only |
|---|---|---|
| 0.004 | +0.745% | +0.02% |
| 0.05 | +0.816% | +0.24% |
| **0.1 (anchored upper)** | **+1.116%** | +0.54% |
| 1.0 (reference, evidence-rejected) | +6.13% | +5.82% |

Model-level term, coverage-scaled (F = 0.19–0.32, $500M pipeline
[assumption]): **$0.7–1.8M**.

### Pre-commitment option value (de-duplicated per review §6-D3)

Per funded capture target: V = P(envelope exceedance) × C(unsalvageable
despite plume contingency alone) × (flight marginal over ground only):

- P(exceedance): pooled 1/19 large R/Bs [web-verified]; family-specific
  **0/3 SL-16 and 0/10 SL-8** (sole exceeder an SL-14), synodic factor-2
  ambiguity would halve true rates — so the 5–15% bracket is generous upward
  [corrected per §6-D7]. Genuine state variability exists (SL-8-07426 flipped
  stable→tumbling in ~3 months [web-verified]).
- C: $85–95M mission [sourced] × P(unsalvageable | exceedance, plume
  contingency only) 0.5–0.7 [assumption] = $43–66M.
- Flight marginal over ground alone: 0.1–0.3 [derived: TIRA ISAR delivered
  per-pass rotation vectors for Envisat (19 passes) and confirmed the CRD2
  H-2A attitudes; photometry delivers rates at $1–5k/object — both
  web-verified precedents on these object classes]. The servicer's own
  approach phase (counterfactual b) is now credited ONCE, inside C.
- V_spin = **$0.2–3.0M per funded capture target**; + design-margin savings
  $0–1M [assumption; quantification verified not-found].
- Interface-condition option, symmetrically discounted (approach-phase
  applies to it too, per §6-D4): **$0.1–2M per funded capture target**
  (down from the draft's $1–7M; the ADRAS-J evidence for its value is itself
  an approach-phase, in-house product).

### Single-world accounting (replaces the draft's mixed bracket, per §6-D2)

- **Actual-funding world** (the decision-relevant one): funded capture
  targets ≤4 through 2030 [carried, Step 2]; none is a tour-reachable top-50
  object; the demonstrated market buys pre-capture characterization in-house
  (ADRAS-J Phase I — JAXA: "too risky to demonstrate at one try"; NASA
  SSPICY) [web-verified]. Value realizable by THIS architecture: model-level
  willingness-to-pay ≈ 0 absent a funded pipeline; option terms not
  deliverable by cluster tours → **$0–2M**. **< $15M → TRIPPED.**
- **Hypothetical consent-unlocked world** ($500M top-50 removal pipeline
  [assumption]): model $0.7–1.8M + spin option on ~6 toured SL-16s
  ($1.3–17.8M) + interface option ($0.6–12M) → **$3–20M typical, ~$30M
  stacking every corner** — straddles $15M; **indeterminate there**.
- **Prereg-literal reading** (no mission-existence discipline; review §6-D1):
  N=9 × (V_obj up to ~$3.0M + $1M margin) ≈ **$36M → would NOT trip**. The
  verdict does not rest on this reading: the registered threshold's word
  "defensible" plus the *carried Step-2 facts* (funded-mission count,
  reachability — established before this pre-registration was written, so
  not post-hoc evidence-driven) exclude pricing avoided waste of nine capture
  missions in a world with at most four. The reviewer's objection and this
  disposition are logged verbatim in §6.

**Task 1 verdict: TRIPPED in the decision-relevant world.** Falsifiability
retained: had evidence shown a low envelope, high family exceedance rates,
and no ground rate-measurement path, V would have exceeded $15M on ≤4 targets
alone (e.g., 4 × 0.3 × $60M × 0.8 ≈ $58M).

## 2. Task 2 — Gate 5 erosion study (corrected per §6-D8..D11)

| Component | Share basis | Share | d_ground | Basis notes |
|---|---|---|---|---|
| Spin period + stability | modeled + option | 0.09–0.20 | 0.9 at $1–5k/object | photometry campaigns [web-verified]; MMT public DB excludes Russian objects [web-verified] |
| Spin pole ~10° | option | ~0.18 | 0.5–0.7, cost-uncertain | TIRA capability/precedent web-verified; **bookability medium (snippet-level); cost not-found; $10–120k fusion estimate training-data-LOW**; one verified multi-sensor campaign recovered full states for only ~2 of 5 targets |
| Mass-property refinement | modeled (gain 0.816→0.306 when posterior widens to ±30% → mass carries ~60% of modeled value) | 0.12–0.23 | 0 | flight capability also weak (±15% [assumption]) |
| Surface/MLI gross condition | mission evidence | split from below | 0.3–0.5 | TIRA imaged Envisat damage-class features; gross-condition spec only (per prereg) |
| Interface/adapter cm-scale | mission evidence [web-verified JAXA quotes; share 0.2–0.6 defensible, not uniquely 0.5] | 0.2–0.6 | ~0.05 | flight-only; ADRAS-J needed 50-m optical imaging to identify the PAF "in detail" |

**G = 0.21–0.66 across the defensible weighting range** (reviewer-computed
extremes: model-faithful shares → 0.23; hostile d_interface=0.7 → 0.66;
algebraic maximum 0.83 requires d_interface→1.0, contradicted by web-verified
evidence). The only weighting that trips (spin-only, G≈0.85) is the one Task
1's anchor rejects. **NOT TRIPPED — and robustly so.** What ground erodes is
the spin value; what survives erosion (cm-scale interface imaging, fine
librations) is flight-only but small in realizable dollars (§1) and owned by
the capture programs' own phased missions.

## 3. Task 3 — value-weighted Gate 2 / Gate 6 [measured]

- Per-object VoI weights (pre-registered definition, seed 20260705): ~96% on
  SL-16s, ~4% H-2A, **SL-8 exactly 0.000** — verified definition-robust by an
  independent reviewer re-run (signed, unclipped, and |·| variants all give
  0; SL-8s were never entrants nor leavers in any draw of any branch).
  Disclosure (§6-D12): family-level *net* signed contribution of SL-16s is
  slightly negative (−0.001); the weights are shares of gross entrant churn —
  consistent with the small measured campaign gain.
- Coverage of value: F1 = 0.19 (200 m/s / 24 mo; 5 SL-16s), 0.28 (36–48 mo);
  F2 ≤ 0.32 (two vehicles, 250 m/s). The Gate-2-feasibility-carrying SL-8
  tour collects 0.000 of measured value.
- SL-16-restricted economics: marginal $0.94M/object; loaded $2.60–3.40M
  (24 mo), $2.17–2.83M (36–48 mo); advantage 4.4–9.6× / 5.3–11.5× vs the
  dedicated-inspection comparable [external_validation_required], 0.9–2.3× vs
  SSPICY. **Pre-registered soft-kill straddled at 24 mo**, cleared at 36–48 mo.
- Launch-slip robustness: 9/9/10/9 encounters at +0/6/12/24 months — the
  feasibility PASS is a persistent structure, not an epoch accident
  [measured, `step3_value/out/slip_test.csv`].

## 4. What this campaign concludes

Feasibility was never the problem: the Gate-2 PASS survives two years of
launch slip. The value is: with the detumble constant anchored to how real
capture systems are actually built (capture at full rate inside an envelope;
plume detumble as contingency), the dossier's model-level value collapses to
~+1% of campaign risk-per-dollar; the binary pre-commitment option value
attaches only to funded capture missions — of which there are at most four,
none tour-reachable, and whose owners demonstrably buy characterization
in-house; the affordable tour visits objects nobody values and the valued
objects straddle their own economic soft-kill. **Do not build Phases 3–4.**

Noted without pursuing (per instruction): the surviving flight-only remnant —
one-off pre-capture inspection (cm-scale interface condition + fine attitude)
sold to funded removal programs — abandons the cluster-tour architecture of
the fixed brief; any rescope inverting the product hierarchy
(tagging-primary, SSA-first) would require explicit approval.

Meta-lesson (flagged for any successor campaign): for the second consecutive
step, a pre-registered metric needed coherence repair at review time (Step 2:
Gate 1 could not fail; Step 3: Task 1's formula priced options on missions
that do not exist). Method Discipline 1 should additionally require a
single-world coherence check and an independent metric review BEFORE evidence
gathering.

## 5. Assumptions introduced in Step 3

Anchored detumble bracket 0.004–0.1 $M/kN·m·s [assumption anchored to
web-verified architecture]; P(exceedance) 5–15% [pooled small sample,
family-specific evidence lower]; P(unsalvageable | exceedance, plume-only)
0.5–0.7; flight-marginal-over-ground 0.1–0.3; interface marginal
symmetrically discounted; design-margin savings $0–1M; $500M hypothetical
pipeline; ground photometry $1–5k/object and pole campaign $10–120k
[training-data, LOW]; interface value share 0.2–0.6; funded-capture count ≤4
[carried]. Step-2 cost inputs keep their labels.

## 6. Adversarial review log (2 reviewers; dispositions)

D1 (MAJOR, would-flip): joint-defensibility constraint not in the registered
formula; literal reading gives ~$22–36M → no trip. **Disposition: partially
accepted.** The constraint is carried Step-2 fact (pre-dates the prereg),
admitted through the registered word "defensible", and the metric remains
falsifiable with it; but the verdict is now reported with all three readings
side by side (§1), the literal no-trip explicitly disclosed, and the
formula's failure to encode mission-existence recorded as a metric-design
defect (§4 meta-lesson).
D2 (major): world-mixing in the $2–10M bracket. **Accepted; replaced** with
single-world accounting: $0–2M actual / $3–20M (corner ~$30M) hypothetical.
D3: counterfactual (b) double-applied (kill-direction). **Accepted;
de-duplicated**, raising the per-target spin option to $0.2–3.0M.
D4: interface option lacked the approach-phase discount (anti-kill).
**Accepted**; $1–7M → $0.1–2M.
D5: anchor upper (0.05) inconsistent with its own derivation (0.1); 0.1
branch unrun. **Accepted; 0.1 branch run** → +1.116% [measured], model term
$0.7–1.8M.
D6: rounding drifts (model low end $0.71M vs $0.8M; G 0.331 vs 0.35; 0.61 vs
0.65). **Accepted; corrected** — no threshold sensitivity.
D7: "78→243 s" mislabeled as rate change (it is synodic/aspect variability);
exceedance pooled across families (SL-16-specific 0/3). **Accepted;
corrected** — both kill-favoring.
D8: pole-row label inflation (bookability medium, cost not-found, fusion
cost training-data-LOW). **Accepted; labels split** (§2); d_pole 0.5–0.7.
D9: component shares not model-faithful (mass ~60% of modeled value, not
12%). **Accepted**; G range recomputed 0.21–0.66; biases ran against our own
verdict — Task 2 NOT-tripped strengthened.
D10: surface/MLI gross-condition vs cm-scale spec drift. **Accepted; split**
(ground d 0.3–0.5 on gross half); G extremes include it.
D11: interface share 0.5 not uniquely supported by JAXA quotes. **Accepted**;
presented as 0.2–0.6 range; verdict insensitive.
D12: SL-8 = 0.000 clipping attack **FAILED** (reviewer's own re-run: exact
zero under all definitions); near-zero SL-16 family net now disclosed (§3).
D13: P(exceedance) numerator is researcher-computed, envelope is e.Deorbit's
(ADRAS-J2's is not public), synodic ambiguity. **Accepted as caveats**; all
kill-favoring; recorded in §1/§5.

## 7. Files and commands (Step 3)

Created/changed: `STEP3_PREREG.md`, `STEP3_RESULTS.md`,
`data/raw/step3_evidence.json`, `step3_value/{voi_weights.py, tour_value.py,
out/*.csv}`, `study1_tour/run.py` (+2-line beam patch: returns visited set),
`config.yaml` (detumble branches). Commands:
`python -m step3_value.voi_weights`; `python -m step3_value.tour_value`;
`python -m study2_voi.run` (twice: anchored branches; then +0.1 branch).
