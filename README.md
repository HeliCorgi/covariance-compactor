# Covariance Compactor — a reusable falsification method (Claude Skill) + a live predictions ledger, and the debris campaign that produced them

This repository grew, in that order, into **three** things:

1. **`falsifying-concepts` — a Claude Agent Skill** ([`skill/`](skill/)). A reusable,
   pre-registered, adversarially-reviewed method for **killing weak, over-ambitious, or
   hard-to-reverse ideas early**, before real effort is spent. Two modes (a fast
   *quick-kill* triage and a *full-campaign*), a growing set of **11 meta-lessons**, a
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

The **11 meta-lessons** ([`skill/references/meta-lessons.md`](skill/references/meta-lessons.md))
are the self-deception failure modes it exists to catch — each earned from a real reversal,
e.g. *a metric a zero-information instrument also passes*, *"structurally doomed ≠ doomed on
your timeline,"* *specify **whose** death (enterprise vs equity)*, and *adjusted/go-forward ≠
realized GAAP; a de-rating is not a wipe.*

**Install:** copy [`skill/`](skill/) to `~/.claude/skills/falsifying-concepts/` (Claude Code),
or use it on claude.ai / the API — see [`skill/README.md`](skill/README.md).

## 2. Live predictions ledger (calibration, not tips)

Six dated forward calls, one per failure-mode archetype, each **deep-dived and scored**. The
honest headline: **every first-pass gut probability moved** under the deep-dive — three down,
one up, two split into *enterprise-survives-but-equity-dies*. The ledger is the skill's own
**eval set**: when a call resolves, the lesson folds back into the meta-lessons.

- Full ledger + scoring summary: [`skill/examples/predictions-ledger.md`](skill/examples/predictions-ledger.md)
- Scoring taxonomy (labels / cause codes / dates / edge): [`skill/references/scoring-taxonomy.md`](skill/references/scoring-taxonomy.md)
- A resolved "prophecy" (frozen at 23andMe's 2021 IPO, confirmed by its 2025 bankruptcy):
  [`skill/examples/23andme-premortem-2021.md`](skill/examples/23andme-premortem-2021.md)
- Reviews never zombie: [`review-schedule.tsv`](skill/examples/review-schedule.tsv) drives a
  calendar file ([`prediction-reviews.ics`](skill/examples/prediction-reviews.ics)), the
  monthly GitHub Action in [`.github/workflows/`](.github/workflows/), and a Claude routine
  that opens a `Ledger review <month>` PR when a call comes due.

> **Not financial advice.** These are public-information, falsifiable methodology
> demonstrations with review dates — the point is calibration and learning, not stock tips.

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
                       evidence labeling, scoring taxonomy, 11 meta-lessons
  scripts/             null_control.py, verdict_table.py (deterministic helpers)
  examples/            predictions-ledger.md (6 live calls), 23andme-premortem-2021.md,
                       review-schedule.tsv, prediction-reviews.ics
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
