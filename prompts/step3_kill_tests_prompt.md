# Input

Continue in the existing repository (`covariance-compactor`, as reported in the Step 2 execution report). `RESULTS.md` and `SOURCES.md` are the source of record for all Step 2 numbers. If the repository is not accessible in this session, stop and say so — do not reconstruct results from memory.

Fixed baseline unchanged: the Step 1 concept brief remains the sole baseline; capture-grade characterization plus value-of-information is the primary product; tagging remains an optional enhancement. Do not re-litigate concept selection. Do not propose replacement concepts; if the characterization line dies here, note — without pursuing it — that any rescope inverting the product hierarchy (tagging-primary, SSA-first) would require explicit approval.

Working state carried from Step 2 (verify against `RESULTS.md` before use):

* Gate 2 PASS: 9 characterization encounters / 196.7 m/s / 729 d on the SL-8 cluster; the SL-16 cluster maxes at 5 (24 mo) / 6 (36–48 mo).
* Gate 1: the pasted metric is evidentially vacuous (the null control passes it); corrected VoI = +0.75%…+5.9% of top-10 campaign risk-per-dollar, the upper end contingent on the detumble-cost constant and carried almost entirely by the spin measurement.
* Cost arithmetic: $0.52M/object marginal, $1.1–1.9M loaded [assumption-laden]; advantage vs SSPICY ~2–4×, not 25–50×.

# Objective

Decide whether Phases 3–4 are worth building by running the two cheapest kill tests plus one integration recalculation. This is a literature/engineering-anchoring step, not a simulation campaign: new code ≤ ~150 lines total, no new dependencies without justification, everything else parameter reruns of existing modules and sourced analysis. Budget: days, not weeks.

# Method Discipline (lessons from Step 2 — both initial gate verdicts flipped under adversarial review)

1. **Pre-registration first.** Before gathering any evidence for a task, write down its decision metric, kill threshold, and null/counterfactual, and demonstrate falsifiability by describing a plausible world in which it fails. If no such world exists, the metric is defective — redesign it before proceeding. Thresholds may not be revised after evidence gathering for that task begins.
2. **Counterfactual discipline.** The comparison class for a flight inspector's data is never "no knowledge." It is: (a) ground photometry/radar, plus (b) the characterization the capture vehicle itself performs during its own mandatory approach phase. The flight inspector's marginal value is only what survives both.
3. **Provisional verdicts.** Every initial verdict is provisional until an adversarial review pass — an independent skeptical read attacking the data, the counterfactual, and the arithmetic — has run. Log every defect and its disposition; retract in place if overturned.
4. **Anti-fabrication unchanged.** Every external figure carries a fetched-and-content-verified source URL, or is marked assumption or external_validation_required. Facts carried from Step 2 keep their existing labels.

# Task 1 — Detumble / spin-knowledge cost anchor

Question: what is pre-commitment spin knowledge actually worth, in dollars per object, to an ADRAS-J2-class capture campaign?

Method:

* Anchor the detumble-cost constant (Study 2 currently brackets it at 0.004 vs 1.0 $M/kN·m·s) from public program evidence: ADRAS-J's measured target spin findings; ADRAS-J2 requirements; ClearSpace-1; e.Deorbit / DEOS and published detumbling and capture-envelope GNC studies.
* Frame the value as pre-commitment option value: P(target uncapturable or materially costlier than assumed | no prior spin data) × cost of a wasted or replanned servicer mission, plus any design-margin savings (propellant, capture-mechanism sizing) attributable to knowing spin before build/launch — minus whatever the servicer's own approach phase would discover in time anyway (counterfactual (b)).
* Deliverable: a sourced bracket for the constant and a $/object bracket for pre-commitment spin knowledge; then mechanically rerun `study2_voi` with the anchored constant (record command and seed) and report the updated program-level dossier value bracket.

Fixed kill threshold: if the defensible upper end of program-level dossier value is below the loaded cost of the characterization campaign (Study 1 loaded $/object × planned object count), the characterization line is dead.

# Task 2 — Gate 5 erosion study (ground-acquisition attack)

Decompose the dossier into components: spin period; spin axis/pole; stability class (tumbling vs gravity-gradient stable); surface/MLI condition; mass-property refinement; interface/adapter imaging. Assign each a value share using Task 1 and Study 2 outputs (expected: value ≈ spin).

For each value-carrying component, establish ground deliverability against the actual target classes (SL-8 / SL-16 at 600–1,000 km):

* photometric surveys — verify actual database coverage of these classes with URLs; do not rely on the Phase-0 coverage claim without rechecking;
* ISAR radar — check the TIRA / Envisat spin-characterization precedent explicitly;
* SLR photometry and commercial optical/radar offerings;

each with per-object cost, achievable precision against the Gate-5 spec (axis ~10°, period ~1 s, gross condition), and population completeness.

Fixed kill threshold (Gate 5 as pasted, value-weighted): if ground assets can deliver ≥80% of the value-weighted dossier content at <$100k/object, the dedicated-inspector premium is unjustified and the characterization line is dead. This threshold is pre-registered from Step 1 and may not be renegotiated.

# Task 3 — Value-weighted Gate 2 / Gate 6 recalculation

Join Study 1 reachability with Study 2 per-object VoI (small code, reuse the repo):

* fraction of measured VoI collectible within {150, 200, 250} m/s at 24 / 36 / 48 months;
* SL-16-restricted per-object cost (marginal and loaded) and advantage multiple vs the SSPICY and dedicated-inspection comparables [existing labels carried];
* evaluate Gate 2's economic clause on the value-bearing set: per-object cost > ~$3M or advantage < 5× → soft-kill on that segment. The SL-8 feasibility PASS stands either way; state plainly whether the affordable tour actually covers the value.
* launch-slip robustness: rerun the tour with the window geometry propagated +6 / +12 / +24 months to test whether the 9-encounter SL-8 pass survives schedule slip (Step 2's own untested caveat).

# Verdict Logic

* If Task 1 or Task 2 trips its kill threshold: write `STEP3_RESULTS.md` as a negative-result report (pre-registrations, evidence with URLs, measured reruns, adversarial log, verdicts), do not build Phases 3–4, and stop.
* If both survive: report the surviving per-object and program-level value brackets and Task 3's coverage-of-value results, and only then recommend proceeding to Phase 3 — with the added requirement that Gate 7's red-alert metric be designed with a null control (per Method Discipline 1) before any conjunction code is written.
* Report in the Step 2 format: files created/changed, exact commands, measured outputs, verdicts vs thresholds, assumptions introduced, code excerpts ≤30 lines. No full source in chat.

# Output Rules

Unchanged from Step 2: no fabricated metrics or citations; measured / assumption / external_validation_required labeling throughout; determinism preserved (same master seed unless a change is justified and recorded); if the characterization line dies, say so plainly.
