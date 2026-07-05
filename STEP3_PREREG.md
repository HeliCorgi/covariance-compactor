# Step 3 pre-registration (written BEFORE evidence gathering — 2026-07-05)

Master seed unchanged: 20260705. Baseline unchanged: Step-1 concept brief;
characterization + VoI primary, tagging optional. Comparison class for the
flight inspector (Method Discipline 2): (a) ground photometry/radar/SLR, AND
(b) the capture vehicle's own mandatory approach-phase characterization.

## Task 1 — detumble / spin-knowledge cost anchor

- **Decision metric.** Program-level pre-commitment dossier value
  V_prog = N_planned × V_obj, where
  V_obj = P(capture-envelope mismatch not knowable before commitment)
          × C_consequence(wasted or replanned servicer mission)
          + S_margin (design-margin savings from pre-build spin knowledge)
          − D_approach (value recovered anyway by the servicer's own approach
            phase, counterfactual (b)).
  Each term sourced or labeled assumption. In parallel, the Study-2 v2 model
  is mechanically rerun with the anchored detumble constant(s) replacing the
  {0.004, 1.0} bracket (same seed, command recorded) for the model-level value.
- **Kill threshold (fixed now).** If the DEFENSIBLE UPPER END of V_prog is
  below the loaded campaign cost — primary case: $15M (single-vehicle program,
  RESULTS.md §5 midpoint, 9 objects); sensitivity case: $20M (two vehicles,
  14–18 objects) — the characterization line is dead. No revision after
  evidence gathering begins.
- **Null/counterfactual.** Family spin priors from ground data alone, plus
  approach-phase discovery (ADRAS-J precedent: inspection precedes capture
  within the same program).
- **Falsifiability demonstration.** Plausible kill-world: ADRAS-J found its
  target benign; published capture envelopes cover the family spin
  distribution; approach-phase discovery converts would-be losses into cheap
  replans → V_obj ≈ 0 → trip. Plausible survive-world: published evidence that
  target tumble drove major redesign/cancellation (e.g., Envisat rates in
  e.Deorbit) with family P(fast tumbler) ≳ 20% and envelope limits low →
  V_obj ~ $1–5M → V_prog can exceed $15M. Both worlds plausible → metric is
  falsifiable.

## Task 2 — Gate 5 erosion (ground-acquisition attack)

- **Decision metric.** Value-weighted ground-deliverable share
  G = Σ_c w_c · d_c over dossier components
  c ∈ {spin period, spin axis/pole, stability class, surface/MLI condition,
  mass-property refinement, interface/adapter imaging}. w_c from Study-2 v2 +
  Task 1 (expected: concentrated in spin period+pole+stability); components
  the Study-2 model does not price (surface, interface imaging) get
  assumption-labeled shares anchored to mission evidence gathered in Task 1,
  and the adversarial pass must attack them. d_c = 1 only if ground assets
  deliver component c against SL-8/SL-16 at 600–1,000 km to the Gate-5 spec
  (axis ~10°, period ~1 s, gross condition) at < $100k/object with adequate
  population completeness; partial capability → fractional d_c, justified.
- **Kill threshold (pre-registered in Step 1, not renegotiable).**
  G ≥ 0.80 at < $100k/object → dedicated-inspector premium unjustified →
  characterization line dead.
- **Null.** The flight inspector itself: list what it delivers that ground
  provably cannot.
- **Falsifiability demonstration.** Kill-world: TIRA ISAR Envisat precedent
  extends to SL-16/SL-8 sizes; photometric surveys already cover these
  families; pole from photometry+SLR fusion ≤ 10° → G ≥ 0.8 cheap.
  Survive-world: public photometric DBs exclude Russian objects; light-curve
  inversion leaves pole ambiguous; ISAR access is scarce or > $100k/object →
  G < 0.8. Both plausible → falsifiable.

## Task 3 — value-weighted Gate 2 / Gate 6 recalculation

- **Per-object VoI weight (defined now).** From the Study-2 v2 experiment at
  seed 20260705, both detumble branches:
  w_i = E_draws[ p_true,i · 1(i ∈ informed top-10) − p_true,i · 1(i ∈ baseline
  top-10) ] clipped at 0, normalized over the 49 matched objects. (Signed
  decomposition of the measured campaign gain; entrants carry the value.)
- **Metrics.** (i) Coverage F(budget, horizon) = Σ w_i over objects visitable
  by a value-restricted tour (beam search over top-50 members only, per
  inclination cluster, budgets {150,200,250} m/s × horizons {730,1095,1460} d)
  / Σ w_i over all 49. (ii) SL-16-restricted per-object cost (marginal,
  loaded) and advantage multiples vs the ADRAS-J-class dedicated-inspection
  comparable ($15–25M/object [external_validation_required]) — the comparable
  named by the pasted gate — and vs SSPICY ($3–5M/object [sourced contract,
  assumed count]). (iii) Slip robustness: SL-8 82.9° tour at 200 m/s / 24 mo
  with all epoch RAANs advanced by each object's own secular rate for
  Δ ∈ {+6, +12, +24} months.
- **Pre-registered clauses.** Economic soft-kill on a segment (Gate 2 clause
  as pasted): loaded per-object cost > ~$3M OR advantage < 5× (vs the
  dedicated-inspection comparable). Slip criterion: the SL-8 feasibility PASS
  is annotated EPOCH-FRAGILE unless ≥8 encounters at 200 m/s / 24 months
  survive at all of +6/+12/+24 months.
- **Falsifiability demonstration.** Kill-world: VoI weight concentrates on
  SL-16s whose tour maxes at 5 for ≥$3M loaded, and the 9-encounter SL-8
  window contains no top-50 members and disperses under slip → F low +
  soft-kill + fragile. Survive-world: SL-8 top-50 members are RAAN-dense and
  the SL-16 window improves at 36 months → F ≥ 0.5, no soft-kill. Both
  plausible → falsifiable.

## Verdict logic (fixed)

Task 1 OR Task 2 trips → STEP3_RESULTS.md as negative-result report; do not
build Phases 3–4; stop. Both survive → report brackets + Task-3 coverage and
recommend Phase 3 with a null-controlled Gate-7 design requirement.
