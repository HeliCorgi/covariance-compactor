# Covariance Compactor — a reusable falsification method (Claude Skill) + a live predictions ledger, and the debris campaign that produced them

This repository grew, in that order, into **three** things:

1. **`falsifying-concepts` — a Claude Agent Skill** ([`skill/`](skill/)). A reusable,
   pre-registered, adversarially-reviewed method for **killing weak, over-ambitious, or
   hard-to-reverse ideas early**, before real effort is spent. Two modes (a fast
   *quick-kill* triage and a *full-campaign*), a growing set of **13 meta-lessons**, a
   scoring taxonomy, and deterministic helper scripts. Start at
   [`skill/README.md`](skill/README.md).
2. **A live predictions ledger** ([`skill/examples/predictions-ledger.md`](skill/examples/predictions-ledger.md)).
   The skill applied as a *pre-mortem* to real, currently-alive companies: dated,
   falsifiable, probability-tagged forward calls with resolution labels
   (`killed / wounded / survived / inconclusive / too-early`), fixed cause codes, and
   **automated review that never zombies** — a calendar file, a GitHub Action, and a
   Claude scheduled agent open a review PR when a call comes due. *Methodology
   demonstration — **not** investment advice.*
3. **The origin campaign** (everything else). The full clean-sheet falsification that
   *produced* the method — an orbital-debris-remediation concept, *"Covariance
   Compactor,"* that was **killed by its own pre-registered kill tests** (a defensible
   negative result). This is the worked example the method is distilled from.

---

## 1. The method (the reusable core)

`falsifying-concepts` turns "I have a gut feeling this won't work" into a **disciplined,
falsifiable, adversarially-checked verdict**. Its non-negotiable disciplines: pre-register
the metric + kill threshold + null/counterfactual *before* gathering evidence; **null-control
every metric** (would a coin flip also pass it?); measure value as the **marginal over the
cheapest existing alternative**, not "vs nothing"; keep one coherent world per calculation;
run an **independent adversarial review before any verdict is final**; and, for live calls,
fix dates / resolution labels / cause codes and **score lead time, not hit-rate**.

The **13 meta-lessons** ([`skill/references/meta-lessons.md`](skill/references/meta-lessons.md))
are the self-deception failure modes it exists to catch — e.g. *a metric a zero-information
instrument also passes*, *"structurally doomed ≠ doomed on your timeline,"* *specify **whose**
death (enterprise vs equity)*, *adjusted/go-forward ≠ realized GAAP; a de-rating is not a wipe*,
*#12: turn the method on itself; a tool's value is marginal over its true null (a good prompt)*,
and *#13: lock the load-bearing number against the primary source before you theorize.*

**Honest scope (self-kill + A/B, 2026-07-09).** The skill's durable marginal value over simply
prompting a capable model to be skeptical is concentrated in what a one-off prompt *cannot*
provide: runnable deterministic scripts, a fixed cross-session cause-code / label taxonomy, the
anti-zombie review scaffolding, and checklist recall. The prose disciplines themselves are ones a
capable model already largely has — and a **blind A/B confirmed it**: a tight inline prompt built
from these disciplines actually *beat* the full multi-file skill on one-shot pre-mortem quality
(skill won 1 of 8; D = −0.54), so for a **single** analysis the recommended delivery is the
paste-ready [`skill/references/one-shot-prompt.md`](skill/references/one-shot-prompt.md), and the
full skill earns its keep on the prompt-irreducible axes above. Value is largest for a user who
*lacks* the methodology. Established by running the skill on itself —
[`skill/examples/self-kill-2026-07.md`](skill/examples/self-kill-2026-07.md) and the A/B
[`skill/examples/ab-test-2026-07-results.md`](skill/examples/ab-test-2026-07-results.md).

**Install:** copy [`skill/`](skill/) to `~/.claude/skills/falsifying-concepts/` (Claude Code),
or use it on claude.ai / the API — see [`skill/README.md`](skill/README.md).

## 2. Live predictions ledger (a calibration-*ready* prediction log, not tips)

Six dated, pre-registered forward calls, one per failure-mode archetype, each **deep-dived
and scored**. One honest finding: **every first-pass gut probability moved** under the
deep-dive — three down, one up, two split into *enterprise-survives-but-equity-dies*. Note
what that does and does not show: *a disciplined deep-dive beats a gut read* — **not** that
this skill beats a good skeptical prompt (both passes were run with the skill). The ledger is
the skill's own **eval set**, but a calibration-*ready* one, **not a calibration
*measurement***: **no call has resolved yet** (`n_resolved = 0`), the set is small and ~4 of 6
are cycle-correlated, so today it is indistinguishable from a random-probability ledger on any
calibration metric (executed proof:
[`skill/scripts/calibration_power.py`](skill/scripts/calibration_power.py)). The
resolved-outcome→banked-lesson loop is **aspirational until a call resolves**. This very claim
was narrowed by running the skill on itself — see
[`skill/examples/self-kill-2026-07.md`](skill/examples/self-kill-2026-07.md).

- Full ledger + scoring summary: [`skill/examples/predictions-ledger.md`](skill/examples/predictions-ledger.md)
- Scoring taxonomy (labels / cause codes / dates / edge): [`skill/references/scoring-taxonomy.md`](skill/references/scoring-taxonomy.md)
- A resolved "prophecy" (frozen at 23andMe's 2021 IPO, confirmed by its 2025 bankruptcy):
  [`skill/examples/23andme-premortem-2021.md`](skill/examples/23andme-premortem-2021.md)
- Reviews never zombie: [`review-schedule.tsv`](skill/examples/review-schedule.tsv) drives a
  calendar file ([`prediction-reviews.ics`](skill/examples/prediction-reviews.ics)), the
  monthly GitHub Action in [`.github/workflows/`](.github/workflows/), and a Claude routine
  that opens a `Ledger review <month>` PR when a call comes due.

> **Not financial advice.** These are public-information, falsifiable methodology
> demonstrations with review dates — the point is disciplined, pre-registered prediction
> logging and learning, not stock tips (calibration is a future, pooled goal — see §2).

## 3. The origin campaign — a debris concept, killed (negative result)

The method was distilled from a real, three-step campaign (Claude, July 2026) on a
clean-sheet orbital-debris-remediation concept — one or two ~24 kg smallsats touring LEO
derelicts to sell capture-grade characterization and value-of-information. **It was killed by
its own pre-registered kill tests, on *value*, not feasibility.** Numbers carry their original
labels (**measured** = executed code in this repo; **assumption**; **external_validation_required**):

- **Tour feasibility (Gate 2): PASS** — 9 encounters / 196.7 m/s / 729.2 d on the SL-8
  cluster [measured]; robust to +24 months launch slip.
- **Value-of-information (Gate 1):** the pre-registered ranking-flip metric is *evidentially
  vacuous* — a zero-information null control passes it. Corrected value: **+0.75% … +1.116%**
  [measured], almost entirely the spin measurement.
- **Kill (Step 3):** realizable dossier value **$0–2M** [assumption-laden] vs a **$15M**
  threshold and **$13–20M** loaded cost — the characterization line is dead.
- **Value coverage:** VoI weights ~96% on SL-16s, SL-8 exactly **0.000** [measured] — the
  *feasible* tour is value-empty.

The campaign **twice reversed its own initial gate verdicts under adversarial review** (Study 1
FAIL→PASS, Study 2 PASS→"vacuous"), and the final kill's D1 objection (three readings:
actual-funding $0–2M / consent-unlocked $3–20M / prereg-literal ~$36M) is disclosed
side-by-side. Read [`RESULTS.md`](RESULTS.md) (§9) and [`STEP3_RESULTS.md`](STEP3_RESULTS.md)
(§6, D1–D13) before drawing conclusions. Reproduce: `python run_all.py` (seed `20260705`; see
[`REPRODUCING.md`](REPRODUCING.md)). Phases 3–4 and Gates 3/4/6/7/8 are **NOT EVALUATED**;
cost figures are assumption-laden.

## Repository map

```
README.md            this file (the repo's current identity)
skill/               ── the reusable method ──────────────────────────
  README.md            what it's for + how to install (Claude Code / claude.ai / API)
  SKILL.md             the method, modes, disciplines, verdict logic (the entrypoint)
  references/          prereg template, gate/verdict format, adversarial rubric,
                       evidence labeling, scoring taxonomy, one-shot-prompt, 13 meta-lessons
  scripts/             null_control.py, verdict_table.py, calibration_power.py
  examples/            predictions-ledger.md (6 live calls), 23andme-premortem-2021.md,
                       self-kill-2026-07.md + ab-test-2026-07-{prereg,results}.md
                       (the skill tested on itself), review-schedule.tsv, prediction-reviews.ics
.github/workflows/     prediction-review-reminder.yml (opens a review issue when due)

RESULTS.md           ── the origin campaign ─────────────────────────
STEP3_PREREG.md        Step 3 pre-registration (before evidence)
STEP3_RESULTS.md       Step 3 kill tests, D1–D13 adversarial log, final verdict
SOURCES.md             data + literature sources (URLs, retrieval dates)
REPRODUCING.md         how to regenerate the studies (python run_all.py)
prompts/  reports/     the three verbatim step prompts and execution reports
shared/  study2_voi/  study1_tour/  step3_value/   executed studies
study3_conjunction/  study4_taggability/           not built (markers)
config.yaml  requirements.txt  run_all.py  data/   parameters, deps, outputs
```

## Method & provenance notes

- **AI-executed (Claude).** Evidence was gathered by multiple agents with per-source URL
  verification (basis: web-verified / training-data / not-found), archived in `SOURCES.md`.
  The exact step prompts are in `prompts/`; the verbatim run reports (including their original
  Japanese framing) in `reports/`.
- **Analysis artifacts are byte-identical to the campaign's final state** (SHA-256 manifest
  verified). The one authorized change is an append-only provenance appendix in `SOURCES.md`.
  `README.md` was renamed to `REPRODUCING.md` (byte-identical) during packaging; the current
  `README.md` is scaffolding that reflects the repo's evolution.
- **Excluded from git:** CelesTrak raw catalog dumps (redistribution terms silent — regenerated
  by `run_all.py`) and two raw evidence JSONs (embedded a local session path — their citations
  are preserved in the `SOURCES.md` appendix). See `.gitignore` and `SOURCES.md`.
- **License:** MIT (`LICENSE`).
