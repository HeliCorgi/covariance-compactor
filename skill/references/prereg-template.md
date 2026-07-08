# Pre-registration template (one per kill-test / gate)

Fill this in **before** gathering any evidence for the test. Copy one block per
gate. Once you start gathering evidence for a gate, its threshold is frozen.

```
GATE / KILL-TEST: <short name>

Idea under test (1 paragraph):
  <what is being proposed, in plain terms>

Load-bearing assumption this gate attacks:
  <the claim that, if false, kills or badly wounds the idea>

Decision metric (exact definition):
  <a formula or procedure precise enough that two people compute the same number>

Kill threshold (number + direction):
  <e.g. "kill if realizable value < $X" / "kill if <N encounters in budget">
  <state which side of the threshold kills>

Null / counterfactual (what a baseline yields):
  <zero-information baseline: what does a random / do-nothing / prior-only
   estimator score on this metric?>
  <cheapest existing alternative: what already delivers this for free / cheaper,
   and what does the idea add ON TOP of it?>

Falsifiability demonstration (REQUIRED):
  Kill-world:    <a plausible world in which this metric trips / the idea fails>
  Survive-world: <a plausible world in which it passes>
  If you cannot write a credible kill-world, the metric is defective — redesign
  it before continuing.

Data / method to compute it (cheapest that can trip the gate):
  <real dataset or sources; first-order model; ~lines of code or # of fetches>
  <label plan: which inputs are measured / assumption / external_validation_required>

Freeze statement:
  Threshold and metric locked as of <date>. No post-hoc changes once evidence
  gathering begins. Any later change is recorded as a metric-design defect, not a
  threshold revision.
```

## Notes

- **One metric, one number, one threshold** per gate. If a gate needs several
  numbers to decide, it is really several gates — split it.
- Prefer **kill thresholds you expect might trip.** A threshold set so lax that
  nothing could ever fail it is theatre, not a test.
- Write the null/counterfactual **before** the metric feels final — it often
  reveals that the metric measures degeneracy or re-measures a free alternative.
- Keep the pre-registrations in a committed file (e.g. `PREREG.md`) so the
  adversarial reviewer can check for post-hoc drift.

## Resolution & scoring (fix these before evidence, too)

For a **live** prediction, also freeze the scoring fields up front, per
[scoring-taxonomy.md](scoring-taxonomy.md), so it can't rot into a zombie:

```
Resolution horizon:  <date by which killed/survived should be clear>
Review checkpoints:  <calendar: +30d/+90d/+1yr>  AND  <event: next earnings /
                     next raise / debt maturity / policy decision / sale outcome>
Outcome variable:    <enterprise insolvency | equity wipe >90% | delisting |
                     distressed sale>  (specify WHICH death — meta-lesson #9)
Pre-declared labels: killed / wounded / survived / inconclusive / too-early
Expected cause code: <one of the fixed enum; optional secondary>
Consensus-at-call:   <price / analyst posture / prevailing narrative TODAY>
                     (so lead time — the edge — is measurable at resolution)
```

At each checkpoint, assign a label (even `too-early`) and never leave the
prediction without a next date. The goal is speed and resolution, not hit-rate:
did we find the load-bearing weakness *before the market*? (Calibration proper is
a later, pooled goal — see meta-lesson #12.)
