# Adversarial review rubric

Every initial verdict is **provisional** until an independent skeptic has tried
to refute it. The reviewer must **not** be the author of the finding (spawn a
fresh subagent with only the artifacts, not the reasoning that produced them).
The reviewer's job is to **flip the verdict**, not to agree.

## Attack these three surfaces

**1. Data**
- Are the sources real and actually fetched — not remembered? Do basis labels
  (web-verified / training-data / not-found) match what was truly verified?
- Silent data loss: dropped rows, stale records, duplicates, wrong-object matches
  in any join or lookup?
- Does a load-bearing number rest on a single unverified or paywalled source?

**2. Counterfactual**
- Is value measured against the **cheapest existing alternative** and the
  system's **own mandatory work** — or sloppily against "nothing"?
- Double-counting: is the same advantage credited twice (e.g. a discount applied
  once in the probability and again in the marginal factor)?
- Is the comparison class a strawman?

**3. Arithmetic**
- Recompute every bracket end-to-end. Do the printed numbers reproduce?
- **Null control:** can the metric be passed by a zero-information baseline? If a
  null instrument reproduces the headline number, the finding is vacuous.
- **Single-world coherence:** are benefits and costs priced in the same world?
- **Threshold drift:** was any threshold, weighting, or constraint added *after*
  evidence gathering in a way that made the verdict easier? Flag it whichever
  direction it pushes.
- **Existence check:** are options/benefits priced on things that actually exist
  (funded, reachable, real), or on hypotheticals treated as real?

## Reviewer output (structured)

```
sound:        true / false
severity:     none / minor / major / fatal
would_flip:   true / false        (could a defect plausibly flip the verdict?)
defects:
  - location:    <file / section / line>
    description: <what is wrong>
    impact:      <direction + rough size on the verdict metric>
```

## Disposition (by the author, in place)

For each defect: **accept** (fix and re-run, record old→new), **reject** (with a
reason the reviewer would accept), or **retract-in-place** (if it overturns the
verdict, change the verdict where it was stated — do not bury it).

Run enough reviewers to cover the surfaces; for high-stakes gates use several
independent skeptics and treat a majority "would_flip" as decisive. Record that
verdicts were provisional until this pass ran.
