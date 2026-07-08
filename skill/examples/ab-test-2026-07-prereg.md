# A/B pre-registration — does the skill beat a *good prompt*? (frozen 2026-07-09)

The self-kill ([`self-kill-2026-07.md`](self-kill-2026-07.md)) narrowed gate A
("the skill's disciplines/lessons beat baseline Claude") to *unproven*, because
the only evidence in the repo was confounded (thorough-vs-gut, both passes run
**with** the skill). This is the missing clean test, **pre-registered before any
result exists** (committed to git before the runs). Per the skill's own discipline:
metric + threshold + null are frozen here, before evidence.

## Claim under test
On the quality of a **single falsification analysis**, does `falsifying-concepts`
(the treatment) produce materially better output than a **competent one-off
skeptical prompt** (the true null)?

> This A/B tests *only* single-analysis prose quality — the one contested axis.
> It does **not** test the four prompt-irreducible axes (deterministic scripts,
> cross-session cause-code/label taxonomy, anti-zombie tracking, checklist recall),
> which are real by construction and need no A/B (meta-lesson #12).

## Design
- **Arm A (skill):** an agent that reads the full skill (`SKILL.md`, all
  `references/`, may run `scripts/`) and applies it in quick-kill mode.
- **Arm B (null = a *strong* prompt):** an agent given a hand-written, genuinely
  competent skeptical prompt that states the *general* forms of every discipline
  (pre-register metric/threshold/null; null-control; counterfactual; single-world
  coherence; whose-death enterprise-vs-equity; date the timing to forcing events;
  adjusted≠GAAP; adversarial self-review) — but **not** the skill's specific 12
  meta-lessons, taxonomy enum, worked examples, or scripts.
  **This is deliberately a *strong* null — it biases the test *against* the skill.**
  If the skill still wins, the result is robust; if it does not, the self-kill's
  narrowing is confirmed.
- **Both arms:** same model/effort, same web access for current data, output in an
  identical neutral structure, and are **forbidden to name any framework / lesson
  number** (so grading is blind).
- **8 fresh targets, none in the ledger, direction-mixed** (to defeat a
  "predict-doom-always" strategy): Beyond Meat (BYND), Carvana (CVNA), Peloton
  (PTON), WW International (WW), Hims & Hers (HIMS), Rivian (RIVN), Snap (SNAP),
  Chewy (CHWY). Intended spread: ~2 kill-leaning, ~2 survive/refute (false-positive
  tests), ~4 genuinely two-sided.
- **Blinding:** for each target the two analyses are presented as "Analysis 1 /
  Analysis 2"; the skill arm is Analysis 1 on even-indexed targets, Analysis 2 on
  odd — a rule the graders do not know. Mapping recorded post-hoc.
- **Graders:** 3 independent blind judges per target (8×3 = 24 paired judgments),
  each scoring both analyses 1–10 on: (a) identifies the true load-bearing
  assumption; (b) calibration & honesty of the probability (penalize *both*
  over-dramatic and wishy-washy; a well-justified *refutation* scores as high as a
  well-justified kill); (c) identifies the decisive weakness / correctly avoids a
  false positive; (d) rigor of null-control & counterfactual; (e) overall. Judge
  substance, not length/format.

## Pre-registered metric & decision rule (frozen)
Primary: **D = mean(skill_overall − prompt_overall)** across all 24 (target×grader)
pairs. Secondary: **W = win-rate** = #(skill_overall > prompt_overall)/24. CI on D
by normal approx / bootstrap.

| Outcome | Rule (frozen) | Meaning |
|---|---|---|
| **Skill materially wins** | D ≥ +1.0 **and** W ≥ 0.65 **and** 95% CI on D excludes 0 | Gate A claim vindicated; would *reverse* the self-kill's narrowing |
| **Modest real edge** | +0.3 ≤ D < 1.0 with CI excluding 0, or W ≥ 0.60 | Skill helps on prose too, but the "modest margin" narrowing stands |
| **Indistinguishable** | \|D\| < 0.3, or CI includes 0 with 0.40 ≤ W ≤ 0.60 | **Self-kill narrowing CONFIRMED** — prose quality ≈ a good prompt |
| **Prompt wins** | D ≤ −0.3 with CI excluding 0 | Strong finding: the bundled lessons *mislead* on a single analysis |

**Predicted (before running):** *Indistinguishable* — because the null is a strong
prompt and a capable model already has the prose disciplines. A clear "skill
materially wins" would surprise me.

## Falsifiability & limits (frozen)
- The claim is falsified (self-kill confirmed) if D is small / CI includes 0.
- **Power is weak** (n=24 paired, graders correlated within target); treat the CI
  as indicative, not definitive — meta-lesson #12 applies to *this* test too. This
  is *one* executed A/B, strictly more than the zero we had, not a final word.
- Grading is by Claude judges (same family as the arms); a human panel would be
  stronger. Stated, not hidden.
