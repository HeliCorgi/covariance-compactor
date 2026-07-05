# Covariance Compactor — a pre-registered, adversarially-reviewed falsification campaign (negative result)

This repository is the complete, verbatim record of a clean-sheet, pre-registered,
adversarially-reviewed **falsification campaign** for an orbital-debris-remediation
concept — *"Covariance Compactor"*: one or two ~24 kg smallsats touring high-priority
LEO derelicts via differential-J2 plane drift to sell capture-grade characterization
and value-of-information, with optional retroreflector tagging as an experimental
enhancement. It was executed with Claude across three steps in July 2026. **Outcome:
negative — the concept was killed by its own pre-registered kill tests.** No further
development is planned.

The point of publishing a dead concept is the method and the receipts: the campaign
twice reversed its own initial gate verdicts under adversarial review, and it kills the
concept on *value*, not feasibility.

## Headline results

Every number below is copied from the execution reports with its original label
(**measured** = produced by executed code in this repo; **assumption**;
**external_validation_required**).

- **Tour feasibility (Gate 2): PASS** — 9 characterization encounters / 196.7 m/s /
  729.2 d on the SL-8 cluster [measured]; robust to +24 months launch slip.
- **Value-of-information (Gate 1):** the pre-registered ranking-flip metric is
  *evidentially vacuous* — a zero-information null control passes it. Corrected,
  evidence-anchored information value: **+0.75% … +1.116%** evidential gain [measured],
  carried almost entirely by the spin measurement.
- **Kill (Step 3, Task 1):** realizable dossier value in the actual funding world
  **$0–2M** [assumption-laden] versus a **$15M** kill threshold and a **$13–20M** loaded
  campaign cost — the characterization line is dead.
- **Ground-erosion (Step 3, Task 2): NOT tripped** — G = 0.21–0.66 < 0.80 [measured /
  assumption].
- **Value coverage (Step 3, Task 3):** per-object VoI weights ~96% on SL-16s, SL-8 weight
  exactly **0.000** [measured] — the *feasible* tour is value-empty; value coverage
  F1 = 0.19–0.32 [measured].

## Disputed verdict, disclosed

The Task 1 kill depends on **which world is priced**. An adversarial reviewer's objection
(logged as **D1**) is that the joint-defensibility constraint that carries the kill was not
encoded in the pre-registered formula, under which a literal reading would *not* trip.
All three readings — actual-funding ($0–2M), consent-unlocked ($3–20M, corner ~$30M), and
prereg-literal (~$36M) — are published side-by-side in `STEP3_RESULTS.md` §1 and §6.
The verdict is reported as tripped **in the decision-relevant (actual-funding) world**,
with the alternates disclosed. Read `STEP3_RESULTS.md` before drawing conclusions.

## What is reusable

- The corrected **differential-J2 tour leg model** (co-orbital loiter + per-leg drift
  purchase; per-leg costs sit on the published GTOC9 time-Δv frontier) — `study1_tour/`.
- The **null-control methodology** for ranking-based value-of-information metrics — the
  Step-2 verdict flip turned on a metric that a zero-information instrument could pass —
  `study2_voi/`.
- The **pre-registration + adversarial-review workflow** (`STEP3_PREREG.md`, the §9 / §6
  defect logs) and the **measured / assumption / external_validation_required**
  evidence-labeling scheme used throughout.

The method has been packaged as a ready-to-install **Claude Agent Skill** in
[`skill/`](skill/) — see [`skill/README.md`](skill/README.md) for what it's for
(killing big, expensive, or hard-to-reverse ideas early) and how to install it in
Claude Code / claude.ai / the API.

## What was never evaluated

- **Phases 3–4 were not built:** the conjunction Monte Carlo and the taggability census.
- **Gates 3, 4, 7, 8 and the final Gate 6 are NOT EVALUATED.**
- **Cost figures are assumption-laden** (per-object and program-level dollar values carry
  the *assumption* label; the dedicated-inspection comparable is
  *external_validation_required*). Treat them accordingly.

## Method note

AI-executed (Claude). Evidence was gathered by multiple agents with per-source URL
verification (basis labels: web-verified / training-data / not-found), archived in
`data/raw/step3_evidence.json` and `SOURCES.md`. Two initial gate verdicts were reversed
under adversarial review — Study 1 FAIL→PASS and Study 2 PASS→"vacuous, corrected value" —
with every defect and its disposition logged in `RESULTS.md` §9 and `STEP3_RESULTS.md` §6
(13 dispositions, D1–D13). The **exact prompts** that drove each step are in `prompts/`;
the **verbatim run reports** (including their original Japanese framing text) are in
`reports/`.

## Repository map

```
README.md            this file
REPRODUCING.md       original repo README — how to regenerate everything
RESULTS.md           Steps 1–2 results: gate table, evidence matrix, verification log §9
STEP3_PREREG.md      Step 3 pre-registration (written before evidence gathering)
STEP3_RESULTS.md     Step 3 kill-test results, D1–D13 adversarial log, final verdict
SOURCES.md           data + literature sources with URLs and retrieval dates
config.yaml          all parameters, labeled measured / assumption / sourced
requirements.txt     pinned dependencies (Python 3.11)
run_all.py           regenerates the executed studies in order
prompts/             the three verbatim step prompts (Steps 1–3)
reports/             the three verbatim execution reports (Steps 1–3)
shared/              propagation, population loading, catalog fetch, top-50 matching
study2_voi/          Phase 1 — value-of-information ranking-flip experiment (Gate 1)
study1_tour/         Phase 2 — differential-J2 tour feasibility (Gate 2) + slip test
step3_value/         Step 3 — VoI weights, value coverage, launch-slip robustness
study3_conjunction/  not built (Phase 3) — carries a not-built marker
study4_taggability/  not built (Phase 4) — carries a not-built marker
data/                processed products + study outputs (raw evidence JSONs excluded, see below)
```

Reproduction details and exact commands are in **`REPRODUCING.md`**
(regeneration: `python run_all.py`; master seed `20260705`).

## Provenance note

- **Renames/moves during packaging:** the campaign's original `README.md` was renamed to
  `REPRODUCING.md` (content byte-identical); the three prompt files and three report files
  were copied into `prompts/` and `reports/` from their verbatim sources. No other file
  was moved.
- **All analysis artifacts are byte-identical to the campaign's final state**, verified by
  a SHA-256 manifest taken before packaging and re-verified after (79 pre-existing files,
  0 mismatches).
- **CelesTrak raw catalog dumps** (`data/raw/satcat.csv`, `data/raw/gp_*.csv`) are **not
  committed**: CelesTrak's usage policy covers download frequency and is silent on
  redistribution, so the bulk dumps are excluded and regenerated on demand by
  `python run_all.py` (see `.gitignore` and `SOURCES.md`). All derived/processed products
  and study outputs are included.
- **Two raw evidence files excluded for privacy:** `data/raw/step3_evidence.json` and
  `data/raw/top50_mcknight.json` embedded a local session path, so they are not committed.
  Their citations are preserved in full: the Step-3 evidence file's complete cited-source
  list is appended to `SOURCES.md` (the "Step 3 evidence — full source list" provenance
  appendix, added under an explicit append-only waiver), and the top-50 list's origin is
  documented in the "Published top-50 list" section of `SOURCES.md`. They are regenerable
  by fetching those documented URLs.
