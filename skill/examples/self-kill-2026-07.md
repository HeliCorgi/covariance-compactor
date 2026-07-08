# Self-kill — running `falsifying-concepts` on itself (quick-kill, 2026-07-09)

The most honest test of a falsification method is to point it at **itself**. This
is the `falsifying-concepts` skill run in **quick-kill mode** on the claim that it
is worth existing. Two of its own claims were narrowed by its own disciplines —
which is the intended behaviour, not a failure of it.

> **TL;DR verdict.** The skill **survives, narrowed** (verdict: `narrow`, not
> `kill`). Its durable value is real but **prompt-irreducible tooling +
> cross-session consistency + recall**, not the prose disciplines a capable model
> already has. The **"predictions ledger is a calibration instrument"** claim was
> **killed as written** (`n_resolved = 0`; indistinguishable from a random-probability
> null; a ≤6-entry, ~4-correlated design can never reject "uninformative") and
> **relabelled** to a *calibration-ready prediction log*. Banked as **meta-lesson #12**.

---

## 1. Pre-registration (frozen 2026-07-09, before looking at any evidence)

**Idea under test.** "`falsifying-concepts` is a genuinely reusable Claude Skill
that adds real *marginal value over baseline Claude*, and its predictions ledger
is a *genuine calibration instrument*."

**Two load-bearing assumptions → two gates.**
- **A (skill value).** The skill's disciplines + meta-lessons produce materially
  better / more-honest falsification than baseline Claude *without* the skill.
- **B (ledger = calibration).** The predictions ledger is a genuine *calibration*
  instrument, not a vacuous or mislabelled record.

**Kill test A — null control = a competent one-off skeptical prompt.** Baseline
Claude given the same idea + a good prompt (pre-register, null-control,
counterfactual, adversarial review) but *without* this skill's bundled
lessons/scripts/taxonomy. **Kill if** the skill adds no reliable marginal value
over that null (i.e. it is a glorified saved prompt).

**Kill test B — null control = a ledger of random probabilities.** **Kill the
"calibration" claim if** the current ledger cannot be distinguished from the
random-probability null within a reasonable horizon, *or* the design can never
reach a calibration-relevant, independent sample size.

**Counterfactual.** For A, "just prompt Claude well." For B, "a qualitative /
pre-registered *learning log*" (a weaker but honest claim than *calibration*).

**Falsifiability.** A fails if baseline-Claude-with-a-good-prompt matches the
skill's quality. B fails if the ledger is provably indistinguishable from the
random null / cannot reach calibration size. **Frozen.**

---

## 2. Cheap evidence (gathered after freezing)

- **Ledger state:** 6 entries, **0 resolved** — all `ACTIVE`, `Outcome: TBD`; the
  ledger itself says "none has reached its horizon." Earliest resolving trigger is
  2026-09; most are 2027–2029.
- **Correlation:** entries 001/002/004/006 (AMC/LCID/PLUG/OPEN) share one
  **rate/capital-cycle** factor → ~4 of 6 resolve along a single macro path;
  effective independent *n* ≈ 3 themes.
- **Self-grading:** the reviewer (a Claude routine) is the same system that made
  the calls; the narrative labels (`wounded` / `survived-so-far`) are elastic.
- **Skill-value evidence in the repo:** the headline "all 6 first-pass gut
  probabilities moved under the deep-dive." But **both** the first-pass and the
  deep-dive were produced by the same agent, same day, **both with the skill** —
  so it shows *thorough beats gut*, not *skill beats a good prompt*.

## 3. Null control, **executed** (not just described)

Per the skill's own discipline (meta-lesson #1: null-control with a real number),
`../scripts/calibration_power.py` (seed 20260705) computes:

- **Q1 — now (`n_resolved = 0`):** Brier over 0 pairs is **undefined**; the
  reliability curve is **empty**. The real ledger and a random-probability ledger
  produce **identical** calibration output (nothing). *Indistinguishable.*
- **Q2 — best case (all 6 resolved, probs perfectly calibrated):** at an
  illustrative hit-rate 0.70, the 95% CI is **[0.33, 1.00]** at n=6 and **[0.18,
  1.00]** at effective n=3. Both **contain the random null (0.50) and perfection
  (1.00)** — the instrument can never reject "uninformative" on its own.
- **Q2b — Monte Carlo (200k worlds):** granting the ledger the *best* case (its own
  probabilities are the true data-generating process), P(informed Brier < coin-flip
  Brier) ≈ **0.91**, mean Brier advantage ≈ **+0.09–0.11**. So the ledger's
  probabilities *do* carry information (**resolution/sharpness**) — but a single
  realized world (all we will ever get) is **not a calibration measurement**. This
  is why the verdict is *narrow* (keep the log) rather than *kill* (discard it).

## 4. Independent adversarial review (two fresh skeptics, not the author)

Run as a parallel workflow; each was told to refute, not defer.

**Skeptic A (skill value) — `kill_survives: true`, verdict `narrow`.**
> The headline "6 probabilities moved" does not isolate skill-vs-prompt and is,
> by the skill's own null-control test, **vacuous** for the claim under test — a
> good skeptical prompt also says "deep-dive, don't trust your gut," so the null
> moves the probabilities too. The prose disciplines (#1–7) are general critical
> thinking; the finance lessons (#8–11) are standard distressed-investing
> distinctions largely retrievable from a good prompt. The skill is distinguishable
> from the null **only** on four prompt-irreducible axes: (1) runnable deterministic
> scripts, (2) a fixed cross-session cause-code/label enum, (3) longitudinal
> tracking scaffolding (.ics / CI / scheduled agent), (4) checklist recall of
> low-frequency checks (the Gawande argument). *Honest read:* ~0.70 that durable
> marginal value exists at all; only ~0.35–0.40 that the margin is *large* over a
> competent prompter. Value is large for a user who lacks the methodology (~0.85),
> modest and artifact-concentrated otherwise.

**Skeptic B (ledger = calibration) — `kill_survives: true`, verdict `narrow`.**
> `n_resolved = 0`, so every calibration statistic is undefined and the ledger is
> **definitionally indistinguishable** from the random null today. Fully resolved
> the design tops out at ~6, with ~4 sharing one rate/capital-cycle factor, so the
> CI spans chance-to-perfection — it can never reject "uninformative." Death is
> rare/slow, so hit-rate is near-uninformative and soft self-assigned labels end up
> doing the work. *Honest read:* P(genuine calibration instrument **now**) ≈ 0;
> P(this 6-entry design ever yields a meaningful calibration curve) ≈ 5–10%;
> P(genuine pre-registered, dated, falsifiable **prediction log**) ≈ 85%.

## 5. Verdict (honest)

| Gate | Claim | Verdict | Why |
|---|---|---|---|
| **A** | "The disciplines/lessons beat baseline Claude" | **NARROW** (overclaim killed) | Confounded (thorough≠skill); prose value ≈ a good prompt. Real margin = scripts + cross-session taxonomy + tracking + recall. |
| **B** | "The ledger is a calibration instrument" | **NARROW** (claim killed, relabelled) | n=0 → identical to random null; ≤6, ~4 correlated → can never reject chance. It is a *calibration-ready prediction log*. |

**The skill as a whole SURVIVES — narrowed.** It is genuinely more than a saved
prompt (the four prompt-irreducible axes are real and map onto Anthropic's stated
skill-over-prompt criteria), and it just demonstrated its core value by **killing
two of its own overclaims**. But the README's *implied* margin ("the method/lessons
catch mistakes a good prompt wouldn't") and the ledger's *"calibration"* label were
both unearned and have been narrowed.

## 6. Actions taken (acting on the kill)

1. **Meta-lesson #12** added — *turn the method on itself; value is marginal over
   the true null (a good prompt); "calibration" needs resolved, independent
   outcomes.* [`../references/meta-lessons.md`](../references/meta-lessons.md)
2. **Ledger relabelled** — a *calibration-**ready** prediction log*, not a
   calibration *measurement*; added a Calibration-status banner and a **frozen
   scored-calls** rule (AMC's scored call = P(distress by end-2027) ≈ 15–20%; the
   2029 thesis is a *new* call, not a replacement — closing the re-dating escape
   hatch). [`predictions-ledger.md`](predictions-ledger.md)
3. **Scoring taxonomy** — "calibration" reframed as a future, pooled goal, not a
   present property. [`../references/scoring-taxonomy.md`](../references/scoring-taxonomy.md)
4. **README** — §2 relabelled ("calibration-ready prediction log"); an **honest
   scope** note added to §1 (value largest for users without the methodology);
   "compounding asset" downgraded to *aspirational until a call resolves*.
5. **Executed null control** shipped as [`../scripts/calibration_power.py`](../scripts/calibration_power.py).

## 7. Limits of this self-test (stated, not hidden)

- **Self-grading.** The author (Claude) ran the skill *and* wrote this record. The
  two adversarial skeptics are the independent check, but a genuinely independent
  human / third-party review would be stronger. Treat the probability reads as
  self-assessed.
- **No A/B was run.** The clean test of gate A — same idea, *skill-Claude* vs
  *good-prompt-Claude*, blind-graded by a third agent — has **not** been executed.
  Until it is, the marginal-value-over-a-good-prompt claim is argued, not measured.
  This is the next honest step if the claim needs to be load-bearing.
