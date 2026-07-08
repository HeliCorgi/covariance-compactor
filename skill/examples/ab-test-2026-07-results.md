# A/B results — the skill vs a good prompt (run 2026-07-09)

The pre-registered test in [`ab-test-2026-07-prereg.md`](ab-test-2026-07-prereg.md),
executed. **The result went against the skill** — honestly reported here, then
acted on.

## Headline
On one-shot, blind-graded pre-mortem quality, **the loaded skill trailed a strong
inline prompt built from its own disciplines.**

| Metric (frozen) | Result |
|---|---|
| **D** = mean(skill overall − prompt overall), 24 pairs | **−0.542** (skill lower) |
| Win-rate (skill) | **0.25** (6 of 24 pairs; skill won **1 of 8** companies outright) |
| 95% CI on D | **[−1.10, +0.018]** (grazes 0 → magnitude not significant at 5%) |
| Sign test on 6/24 wins | **p ≈ 0.02** (direction *is* significant) |
| Per-dimension (skill − prompt) | load-bearing −0.13, calibration −0.25, decisive −0.48, **rigor −1.04**, overall −0.54 |
| Pre-registered band | **ambiguous**, point estimate in "prompt-wins" territory but CI upper edge > 0 |

**Prediction was "indistinguishable"; the actual result was worse for the skill
than predicted.** Both independent interpretation guards (one pressured against
minimizing the loss, one against over-dismissing the skill) returned
`claude_bias_check: balanced` and agreed on the reading below.

## Why the skill lost — and why it *didn't*
- **Not framework labeling, not a missing null-control.** Graders explicitly
  credited the skill arm with "genuine two-sided null controls," and the rigor gap
  was *not* a uniform offset — the skill *won* rigor on CVNA (+1.50) and RIVN
  (+0.50) and lost it only where it made fact errors. So the deficit tracked
  substance, not the blinding rule.
- **The driver was factual accuracy on the load-bearing number.** The skill arm
  reached the *same verdicts* but mis-stated the crux capital structure while
  theorizing: **SNAP** — Aug-2026 maturity stated ~$1.06B vs **$47M actual (~23×
  overstatement)**, the entire **$1.5B 2033 tranche omitted**, ladder not
  reconciling to its own total; **BYND** — the **$81.7M term loans dropped**;
  **HIMS** — **~$1B of 2030 converts missed on the very 8-K it cited**; **CHWY** —
  a fabricated "~$60 June-2025 peak" labeled `measured, web-verified`. It spent
  **~1.5× the tokens/tool-calls** and was still less accurate → the failure was
  **theorize-before-verify**, not research-less.
- **The skill's one clean win (CVNA) shows what it adds when it works.** On
  identical facts it found the *true* load-bearing vector — the accounting-quality
  / restatement channel, engaging the Gotham short report and its three dated
  falsifiable predictions (all missed), with an arm's-length ABS market-check as
  the counterfactual — while the prompt arm strawmanned the thesis as a
  debt-service question and even carried its own fact error (claimed the 2028 notes
  retired). The disciplines add value when they surface the non-obvious crux; here,
  not reliably enough to overcome the fact misses.

## Fair scope (what this does and does not establish)
- **ESTABLISHES:** loading the multi-file skill in quick-kill mode buys **no
  measurable one-shot-prose advantage** over a tight inline prompt encoding the
  same disciplines, at **~1.5× the cost**, and in these 8 draws was **systematically
  weaker at locking the load-bearing figure**. Directionally clear (sign test
  p≈0.02); the skill lost 18/24 pairs and 6/8 companies.
- **DOES NOT ESTABLISH:** (1) that the disciplines are wrong — **arm B *is* those
  disciplines**, so "prompt beats skill" means *the skill's knowledge, tightened
  into a prompt, delivers at least as well* — a vindication of the content, an
  indictment of the file-bundle **delivery + overhead**. (2) That the skill
  underperforms at its actual job — proactive triggering / when-to-invoke,
  cross-session consistency for users who **can't** hand-craft a 200-word expert
  prompt, and the scripts / scoring taxonomy / tracking scaffolding (the four
  prompt-irreducible axes) were **not tested**. (3) Robust magnitude — n=8,
  correlated graders, CI touches 0, and PTON / WW / one HIMS grader were explicit
  near-ties, so "6/8" overstates the real separation. NET: *"the skill underperforms"*
  is an over-reading; the bounded honest claim is *"for a single blind-graded
  pre-mortem the skill did not beat — and slightly trailed — a strong prompt made
  from its own disciplines, mainly because this arm under-verified the load-bearing
  numbers."*

## Actions taken (acting on the loss)
1. **New meta-lesson #13 — lock the load-bearing number against the primary source
   *before* theorizing.** The exact failure mode the losses exposed.
   [`../references/meta-lessons.md`](../references/meta-lessons.md)
2. **A hard verify-the-crux gate added to the quick-kill procedure** in
   [`../SKILL.md`](../SKILL.md): pull and reconcile the single decision-driving
   quantity from the primary filing, and label it `measured` only once verified,
   *before* building the thesis.
3. **Shipped the winning delivery** — a compact, paste-ready
   [`../references/one-shot-prompt.md`](../references/one-shot-prompt.md) (the
   distilled disciplines that beat the file-bundle), with guidance to use the tight
   prompt for one-shot analysis and reserve the full skill for its prompt-irreducible
   value (scripts, taxonomy, tracking, recall, proactive use).

## Limits
n=8, one draw, Claude graders (same family). Meta-lesson #12 applies to this test
too: it is *one* executed A/B — strictly more than the zero we had, not a final
word. A human grader panel and more, faster-resolving items would strengthen it.
