# Input

## A. Concept brief from Step 1 (paste verbatim)

<<<PASTE THE FINAL ONE-PARAGRAPH CONCEPT BRIEF (Step 1, Section 8) HERE>>>

## B. Pre-registered kill criteria from Step 1 (paste verbatim)

<<<PASTE THE KILL CRITERIA, GATES 1–8 (Step 1, Section 5) HERE>>>

Use the pasted concept brief as the sole fixed baseline. Do not re-litigate concept selection. If the fixed concept fails to beat existing approaches on the selected value metric during implementation or simulation, state that plainly and narrow the implementation scope; do not invent a replacement concept unless explicitly asked.

Treat capture-grade derelict characterization and value-of-information as the primary product. Treat retroreflector tagging as an optional experimental enhancement that must be justified by the simulator. The package must still make sense if tagging is dropped.

Treat this as a clean-sheet project. Ignore any prior conversation context, memories, or user history about past projects. Do not mention, analyze, reuse, or compare against ADSC/ASDC or any other prior project of this user.

# Objective

Build and run a gate-driven falsification campaign for the fixed concept — not a full mission-design document. The deliverable is executed studies with measured gate verdicts, honest enough to justify abandoning the concept.

Deliberately deferred until at least Gates 1 and 2 pass: detailed spacecraft bus design (thermal, power, pointing, comms, reliability models), full CONOPS, detailed cost engineering, and tag hardware design beyond a ground coupon-test plan. In this phase, a one-page system envelope (mass, power, delta-v, data-volume consistency; every number labeled assumption) replaces the architecture chapter.

# Execution Mode

* This prompt assumes a code-execution environment. Create files for real, run them, and fix errors until each study completes end to end.
* Do not paste full source code back into the chat. Instead: list created files with one-line purposes, report the exact commands run, report measured outputs (metrics, CSV excerpts of at most 10 rows, plot filenames), and show code excerpts only where a modeling decision needs review (at most ~30 lines each).
* If code execution is NOT available, stop and say so. Do not emit an unexecuted multi-thousand-line codebase into chat; propose delivering one study's code per turn instead.
* Under no circumstances report a number as a simulation result unless it was produced by actually executed code.

# Data Rules (anti-fabrication)

* Never fabricate the identities, masses, orbits, RCS, or spin states of specific cataloged objects.
* Preferred real sources, if fetchable in this environment: Celestrak GP data; space-track (account may be unavailable); ESA DISCOS (API key may be unavailable); the published top-50 statistically-most-concerning derelict list (McKnight et al.). Cache raw files into `data/raw/` and record URL plus retrieval date in `SOURCES.md`.
* If a real source is not reachable, generate a clearly labeled synthetic population from stated, sourced-or-assumed distributions. Mark every object-level conclusion as SYNTHETIC-POPULATION, and mark gate verdicts computed on synthetic data as PROVISIONAL.
* Historical TLE archives (needed for empirical covariance classes in Study 3) generally require a space-track account. If unavailable, use literature-derived covariance classes and mark them assumption.
* Every external program fact, cost figure, legal claim, or market claim must be either supported by a source URL, marked assumption, or marked external_validation_required. Facts inherited from the Step 1 report count as external_validation_required unless the source URL is carried over.

# Dependency Rules

Do not inherit dependency or AI-method choices blindly from the previous response. You may keep, revise, or reject the proposed stack — including RL, MILP solvers, astropy, skyfield, sgp4, or custom propagation. Justify every choice against the simulator's actual needs in at most two sentences per dependency.

* Defaults requiring no justification: numpy, scipy, pandas, matplotlib, pyyaml.
* Pin all versions in `requirements.txt`. poliastro is archived — do not use it.
* The prior expectation from Step 1 is that MILP plus Monte Carlo suffices and no RL is needed. If you propose RL anyway, first show why the MILP/Monte-Carlo formulation is insufficient and include a non-RL baseline comparator.

# Gate-Driven Build Order

Execute strictly in this order. End each phase with a gate-verdict report before starting the next.

## Phase 0 — Prior-art and redundancy check (Gate 0)

Before writing any simulation code, spend one pass checking whether the wheel already exists:

* published sensitivity or value-of-information analyses of derelict priority rankings (the top-50 list and successors),
* existing open tools or published results covering debris tour scheduling, conjunction Pc screening on derelict populations, or SLR-driven covariance improvement.

If existing published work already answers Gate 1 or Gate 2 to roughly 80% or more, report that with URLs, skip the corresponding study, and cite instead of rebuilding. Gate 0 verdict, per study (1–4): BUILD / CITE-INSTEAD / PARTIAL (state which sub-question still needs building).

## Phase 1 — Study 2: value-of-information ranking-flip experiment (decisive)

Bayesian re-ranking of the top-50 under current uncertainty (mass ±50%, unknown spin state, TLE-class covariance priors) versus simulated post-characterization posteriors, propagated through a collision-expectation model. At least 1,000 Monte Carlo draws. Evaluate Gate 1 exactly as pasted; do not soften thresholds.

## Phase 2 — Study 1: tour feasibility MILP

Differential-J2 tour scheduling over the real (or labeled-synthetic) derelict population in the 600–1,000 km band. Sweep the delta-v budget over at least {150, 200, 250} m/s. Cost tagging targets as full rendezvous per the pasted gate's parameters (label the per-transfer costing as assumption). Evaluate Gate 2, and produce the per-object-cost arithmetic that feeds Gate 6.

**Stop rule.** If Gate 1 or Gate 2 trips: do not build Phases 3–5. Write the negative-result report — what was run, measured verdicts, and what narrower scope (if any) remains defensible — and stop.

## Phase 3 (conditional) — Study 3: covariance and conjunction Monte Carlo

Covariance classes: empirical from TLE differencing if archives are available, otherwise literature-derived and labeled assumption. Run a 1-year conjunction Monte Carlo over the candidate derelict set with at least 100 seeds, using coarse screening plus a Foster-type Pc computation. Count red-alert reclassifications under radar-only versus SLR-grade covariance. Evaluate Gates 4(b) and 7 as pasted.

## Phase 4 (conditional) — Study 4: taggability census

Filter the consent-available population by registry, size, altitude band, delta-v reachability (reuse Study 1 machinery), and spin-period confirmability; model SLR visibility and scheduling with stated oversubscription assumptions. Evaluate Gates 3 and 8.

**Tagging drop rule.** If Gate 3, 4, or 8 trips, drop the tagging line and restate the package as characterization-only. This is scope narrowing, not concept failure.

## Phase 5 — Synthesis

* One-page system envelope, every number labeled assumption.
* Thin economics: a per-object cost model consistent with Study 1 outputs; anchor-buyer arithmetic for Gate 6; a sensitivity table over rideshare/launch cost, encounters per vehicle, and per-object price. Every number labeled measured / assumption / external_validation_required.
* Evidence matrix: Claim | Evidence type | Module or source | Confidence | What would invalidate it.
* Gate verdict table covering every gate touched: PASS / FAIL / PROVISIONAL (synthetic data) / NOT EVALUATED, each with the measured number against the pasted threshold.
* Limitations: what this campaign cannot show (tag adhesion physics — ground coupon plan only; bus reliability; procurement reality; anything requiring hardware or high-fidelity simulation).
* Consolidate all of the above into `RESULTS.md`.

# Repository Requirements

* Layout: `data/raw/`, `data/processed/`, `shared/` (propagation, population loading, config, seeding), `study1_tour/`, `study2_voi/`, `study3_conjunction/`, `study4_taggability/`, `run_all.py`, `RESULTS.md`, `SOURCES.md`, `requirements.txt` (pinned), `README.md` with exact regeneration commands.
* Each study must run standalone (e.g., `python -m study2_voi.run`) and write its own CSV outputs and plots.
* Determinism: one master seed in config; per-run seeds derived as `master_seed + run_index` so results reproduce run by run.
* Total code budget: roughly 2,000 lines across all studies. Prefer the simplest physics that can trip a gate (secular J2 and drag rates) over full numerical propagation unless a specific gate genuinely requires more fidelity.

# Reporting Format (every phase)

1. Files created or changed (paths, one line each).
2. Exact commands executed.
3. Measured outputs: key metrics, CSV excerpts (≤10 rows), plot filenames.
4. Gate verdict(s): measured value versus pasted threshold.
5. Assumptions introduced in this phase.
6. Code excerpts (≤30 lines) only where a modeling decision needs review.

# Output Rules

* No fabricated metrics: every reported number must trace to executed code, a labeled assumption, or a source URL.
* No fabricated citations.
* If a gate verdict is PROVISIONAL (synthetic data), state exactly which real dataset would confirm or overturn it.
* If the concept fails its gates, say so plainly and narrow the scope; do not pivot to a new concept unless explicitly asked.
* If a phase cannot fit in one response, complete the phase's execution first, then report; continue in the next turn when prompted.
