# The implementation-kill pipeline

A multi-agent verification pattern for **implementations whose numbers must
match a source of truth** — a design spec, a physics derivation, a dataset, a
prior report, a regulatory filing. Proven in the ADSC campaign
(github.com/HeliCorgi/ADSC), a full engineering execution — WP13 (EDT
physics), WP14 (cost ranges), WP15 (proposal package) — run under this
skill's disciplines, 2026-07-11/12.

## The pipeline

```
implementer  ->  independent numeric cross-checker  ->  adversarial reviewer  ->  CI
```

1. **Implementer** — writes the code/doc from the binding spec, transcribing
   numbers out of the source-of-truth doc.
2. **Independent numeric cross-checker** — a separate pass whose *only* job is
   to **re-derive every transcribed number from the source-of-truth doc**,
   from scratch, without reading the implementer's derivation. Not a re-read
   of the implementer's work — an independent recomputation.
3. **Adversarial reviewer** — attacks pins (numbers that must not silently
   move), compile/test correctness, and the honesty of claims (see
   [`adversarial-review-rubric.md`](adversarial-review-rubric.md)).
4. **CI** — the final, deterministic arbiter. Cannot be argued with; catches
   what every agent pass missed, and catches future drift on every subsequent
   commit.

## Key claim: different roles catch different defect classes

- **Transcription errors** (wrong row, wrong sign, dropped term) — caught by
  the numeric cross-checker's independent re-derivation.
- **Derivation / methodology drift** (a formula that quietly changes what is
  included) — caught by the cross-checker or the adversarial reviewer.
- **Overstatement / honesty issues** (claiming something is stronger or more
  guaranteed than the code actually makes it) — caught by the adversarial
  reviewer.
- **Silent drift over time** (a hand-maintained number slowly diverging from
  its generator) — caught only by CI, because it is the one role that reruns
  on every future commit.

No single role catches all four classes; the pipeline's value is running all
of them, not picking the "best" one.

## Evidence: the ADSC pre-merge kill record

Ten defects this pipeline killed before merge, in one campaign:

1. **Retrograde sign physics bug** — the binding spec specified signed `cos i`
   instead of `|cos i|` for retrograde orbits; the implementer flagged the
   spec-vs-physics conflict rather than silently "fixing" it (meta-lesson #15).
2. **FCC midpoint self-contradiction** — 0.037 was presented as the output of
   the doc's own stated "average the two bounds" rule, which actually
   computes to 0.0375. Caught by the numeric cross-checker.
3. **Anchor-numerator methodology drift** — an anchor number's numerator
   included line items that its own cited method explicitly excluded. Caught
   by the numeric cross-checker.
4. **Launch-cost width narrowing** — a launch-cost range was narrowed against
   the source's explicit do-not-narrow instruction. Caught by the numeric
   cross-checker.
5. **Quote-unaware CSV test parser** — a test's CSV parser split naively on
   commas, silently mis-parsing quoted fields; proven broken by constructing
   a simulated adversarial input row. Caught by the adversarial reviewer.
6. **A 1e-12 floating-point tolerance, falsified** — the pipeline only
   round-trips values to `%.6f` (6 decimal digits), so a tolerance of 1e-12 is
   untestable and meaningless. Caught by the adversarial reviewer.
7. **An "identical by construction" overstatement** — two values claimed
   identical were not actually guaranteed identical by the code that produced
   them. Caught by the adversarial reviewer.
8. **A missing mandatory anchor phrase** — a required phrase was absent from
   the deliverable; caught by a cold-read (reading the doc fresh, as its first
   real reader would, rather than checking it against a mental checklist).
9. **Stale spec self-contradiction** — an older passage in the spec
   contradicted a newer one that superseded it. Caught by the cross-checker.
10. **README hand-maintained number drift** — numbers hand-typed into the
    README had drifted from their generated source; closed permanently by
    adding a generator plus a CI gate that regenerates and fails the build on
    mismatch, rather than re-fixing the number once more by hand.

## When to use

Any implementation whose numbers must reproduce a source of truth: a binding
design spec, a physics derivation, a cost model transcribing a cited source, a
regulatory or dataset-derived figure. Skip it for work with no numeric
fidelity requirement (pure UI polish, prose-only edits) — ordinary code
review is sufficient there.

## The pin-safety rule

Existing numbers — already published, already cited, already relied upon —
move only with a **BEFORE/AFTER disclosure**, never a silent edit. Any pass in
the pipeline (implementer, cross-checker, reviewer) that changes a previously
pinned number must show the old value, the new value, and the reason, in the
same diff. This holds even when the new number is "more correct" — a silent
correction destroys the audit trail and hides how large the past error was.

## Relationship to the rest of the skill

- The numeric cross-checker is a stricter, narrower version of the
  adversarial reviewer's "Arithmetic" surface (see
  [`adversarial-review-rubric.md`](adversarial-review-rubric.md)): it doesn't
  just recompute brackets from the stated inputs, it re-derives every
  transcribed number against the primary doc from scratch.
- Meta-lesson #13 (lock the load-bearing number against the primary source
  before you theorize) is the discipline this pipeline enforces mechanically,
  at implementation scale — see [`meta-lessons.md`](meta-lessons.md).
- Meta-lesson #15 (adversarially review binding specs) is what defect #1 above
  produced.
