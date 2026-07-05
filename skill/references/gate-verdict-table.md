# Verdict reporting format

## Gate verdict table

One row per gate touched. `scripts/verdict_table.py` renders this from a small
JSON/YAML file so the numbers trace to a machine-checkable source.

| Gate | Pre-registered threshold | Measured value (labeled) | Verdict |
|---|---|---|---|
| <name> | <threshold + direction> | <number> [measured/assumption/ext_val] | PASS / TRIP / PROVISIONAL / NOT-EVALUATED |

Verdict vocabulary:
- **PASS** — measured value is on the survive side of the frozen threshold.
- **TRIP** — measured value crosses the kill threshold. A single convincing TRIP
  ends the campaign (write the negative report and stop).
- **PROVISIONAL** — computed on synthetic/assumption-heavy inputs; name the real
  dataset that would confirm or overturn it.
- **NOT-EVALUATED** — gate not built (say why; do not imply it passed).

## Negative-result report skeleton (on a kill)

A kill is only useful if it is honest enough to act on. Include:

1. **Pre-registrations** (verbatim, with freeze dates).
2. **Evidence** — every external fact with a fetched source URL, or labeled
   assumption / external_validation_required.
3. **Measured results** — the actual numbers your executed code / analysis
   produced (command + seed if code).
4. **Adversarial log** — every defect found, its disposition (accepted / rejected
   / retracted-in-place), and whether it changed a verdict.
5. **Verdict vs each threshold** — the table above.
6. **Assumptions register** — every assumption introduced, in one place.
7. **What this cannot show** — the limits (what would need hardware, more data,
   or higher fidelity to settle).
8. **Surviving narrower scope** (optional) — if a *smaller* version survives,
   state it plainly; do NOT invent a replacement concept unless asked.

## On a survive (all gates pass)

Report the surviving value **with every caveat and label intact**, the residual
risks, and the cheapest next test that could still kill it. Recommend proceeding
only after this — and design any next-phase metric with a null control from the
start.
