---
name: falsifying-concepts
description: Runs a pre-registered, gate-driven falsification to kill weak or over-ambitious ideas early, before real effort is committed. Use when deciding whether a big, expensive, or hard-to-reverse concept, project, or hypothesis is worth pursuing. It pre-registers falsifiable kill-metrics with null controls, runs the cheapest kill-tests on real data or sourced literature, and adversarially reviews the arithmetic and counterfactuals before issuing a keep or kill verdict. Defaults to a fast quick-kill triage; escalates to a full multi-gate campaign only for high-stakes decisions. Not for small, cheap, or reversible choices.
---

# Falsifying concepts — kill weak ideas early, cheaply, and defensibly

## What this is for

A falsification campaign exists to **kill an idea as cheaply as possible**. Its
job is not to build the idea or to confirm it — it is to find the fastest honest
reason it will fail, and to make a *survivor* earn its survival. Bias toward
killing. The enemy is motivated reasoning that keeps a doomed idea alive with a
flattering metric, a missing counterfactual, or a goalpost that quietly moves.

Use this when a wrong "go" is expensive: a multi-month build, a large spend, a
public commitment, a hard-to-reverse architecture choice, or a bold hypothesis
someone is attached to. **Skip it** for small, cheap, or reversible decisions
(just do them) and for ideas already validated by prior work.

## Two modes

| Mode | When | Cost | Output |
|---|---|---|---|
| **quick-kill** (default) | First pass on any big idea. Target its single riskiest assumption. | Hours; 1–2 kill-tests, one adversarial pass. | Kill (short negative report) or "survives triage → candidate for full campaign". |
| **full-campaign** | Quick-kill did not land and the cost of a wrong go is large. | Many agent-hours/tokens; confirm scope first. | 4–8 pre-registered gates, executed studies, per-finding adversarial review, negative-result report or a caveated proceed. |

Always start in quick-kill. Escalate only if it survives *and* the stakes justify it.

## The non-negotiable disciplines

These are what make a kill *defensible* (and stop you fooling yourself). Every
mode applies all of them. Details and worked failure examples are in
[references/meta-lessons.md](references/meta-lessons.md).

1. **Pre-register before evidence.** Before gathering anything, write down for
   each kill-test: the decision metric, the kill threshold (a number), the null/
   counterfactual, and a *falsifiability demonstration* — describe a plausible
   world in which the metric fails. If you cannot describe such a world, the
   metric is defective; redesign it before proceeding. **Freeze thresholds** —
   never revise them after evidence-gathering for that test begins. Use
   [references/prereg-template.md](references/prereg-template.md).

2. **Null-control every metric.** Ask: would a zero-information / random / do-
   nothing baseline also pass this metric? If yes, the metric is *vacuous* and
   proves nothing. Report **metric-minus-null**, not the raw metric. Run
   `python scripts/null_control.py` (adapt the four callables) to measure it.

3. **Counterfactual discipline.** A benefit is the *marginal* gain over the
   **cheapest existing alternative** — never over "nothing". List what is
   already done for free, by someone else, or by a simpler method, and subtract
   it. Include the system's own mandatory work (what it would discover anyway).

4. **Single-world coherence.** Do not price benefits in one world and costs in
   another. Pick one consistent set of assumptions per calculation and state it.

5. **Minimal executable kill-tests.** Build the cheapest thing that can trip a
   gate — real data or sourced literature, not vibes. Prefer first-order /
   secular models over full fidelity. Label every number **measured /
   assumption / external_validation_required** (see
   [references/evidence-labeling.md](references/evidence-labeling.md)).

6. **Adversarial review before any verdict is final.** Every initial verdict is
   *provisional*. Spawn an independent skeptic (a fresh subagent) to attack the
   data, the counterfactual, and the arithmetic. Log every defect and its
   disposition; retract in place if overturned. Use
   [references/adversarial-review-rubric.md](references/adversarial-review-rubric.md).
   (In the worked example, *both* initial gate verdicts flipped under review.)

7. **Verdict logic.** If a kill gate trips → write the negative-result report and
   **stop**; do not pivot to a replacement concept unless explicitly asked. If
   all gates survive → report the surviving value with every caveat and *only
   then* recommend proceeding. Format in
   [references/gate-verdict-table.md](references/gate-verdict-table.md).

8. **For a live prediction, score it — and score speed, not hit-rate.** Fix a
   **resolution date + review triggers** (calendar *and* event-based) so it can't
   zombie; pre-declare the label set (**killed / wounded / survived / inconclusive
   / too-early**), a fixed **cause code**, and a **consensus-at-call snapshot** so
   lead time is measurable. The value is finding the load-bearing weakness *before
   the market* — prize lead time and resolution over being "right." (True
   *calibration* is a later, pooled goal that needs many independent, fast-resolving
   calls; a small or correlated set is calibration-*ready*, not calibrated — see
   meta-lesson #12.) See
   [references/scoring-taxonomy.md](references/scoring-taxonomy.md); log calls in a
   predictions ledger and fold each resolution back into meta-lessons.

## Quick-kill procedure (default)

1. **State the idea** in one paragraph. Name its **single load-bearing
   assumption** — the claim that, if false, kills the whole thing.
2. **Pre-register** 1–2 of the cheapest tests that attack that assumption, each
   with a kill threshold, a null control, and the counterfactual
   (prereg-template.md). Freeze the thresholds.
3. **Lock the load-bearing number first, *then* gather the rest.** Before
   theorizing, pull the single decision-driving quantity (the debt maturity ladder
   / cash runway / unit margin) directly from the **primary source** and reconcile
   it (does the ladder sum to the stated total? is there debt on the balance sheet
   you didn't list?); label it `measured` only once verified against that primary
   doc (meta-lesson #13 — theorize-before-verify was the #1 cause of wrong verdicts
   in the A/B self-test). Then do the focused web/literature check (fetch and verify
   real sources) or a <150-line calculation on real data. Label every number.
4. **Adversarial pass:** one fresh skeptic attacks data, counterfactual, and
   arithmetic (adversarial-review-rubric.md). Fix or retract.
5. **Verdict:** kill (write a short negative-result note: pre-reg, evidence with
   URLs, measured result, defect log, verdict) — or "survives triage".
6. **Stop rule:** if the load-bearing assumption fails cheaply, stop there. Do
   not build more to rescue it.

## Full-campaign procedure (high-stakes only)

Confirm scope and rough cost with the user before launching — this can be
expensive.

1. **Landscape / baseline:** what already exists and what it costs (verified,
   with sources). The idea must beat *this*, not a strawman.
2. **Define 4–8 gates** covering both **feasibility** ("can we do it?") and
   **value** ("is the result worth it?"). Pre-register each (metric, threshold,
   null, counterfactual, falsifiable world). Order them cheapest-kill-first.
3. **Minimal executable study per gate** on real data; every number labeled.
   Determinism: fix and record a master seed.
4. **Adversarial review per finding** (fresh skeptics); log defects + dispositions.
5. **Single-world economics** and an **evidence matrix**
   (claim | evidence type | source | confidence | what would invalidate it).
6. **Gate verdict table** + negative-result report on the first convincing trip,
   or a caveated proceed if all survive.

Worked example (a full campaign that ended in a defensible kill):
https://github.com/HeliCorgi/covariance-compactor — read its `STEP3_RESULTS.md`
§6 (13 dispositioned defects) and `RESULTS.md` §9 (two reversed verdicts).

## Running it in this environment

- Use subagents / the Workflow tool for parallel evidence-gathering and for
  *independent* adversarial review (the reviewer must not be the author).
- Use the bundled scripts for the deterministic parts:
  - `scripts/null_control.py` — does a metric beat a zero-information baseline?
  - `scripts/verdict_table.py` — render the gate verdict table + kill summary.
- Anti-fabrication: every external number carries a fetched source URL, or is
  marked assumption, or external_validation_required. Cache sources with
  retrieval dates. Never report a computed number that was not actually computed.

## Meta-check before you gather evidence

Two failure modes recur (see meta-lessons.md): a metric that *cannot fail*, and
options priced on a world that does not exist. Before gathering evidence, run a
**single-world coherence check** and an **independent metric review** — confirm
each pre-registered metric could plausibly fail and is priced in one coherent
world. Cheap to do; it prevents the most common wasted campaign.
