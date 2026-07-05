# Gate-driven falsification campaign — RESULTS (v2, post-verification)

**Concept under test (fixed, from Step 1):** government-anchored derelict-characterization
tours (12–16U inspectors, differential-J2 plane drift, standoff characterization of
high-priority derelicts; retroreflector tagging as an optional enhancement).
Primary product: capture-grade characterization + value-of-information.

**Campaign outcome (after adversarial verification, §9):**

- **Gate 2 (tour economics): PASS.** The initial FAIL was a model artifact: all
  three original tour formulations excluded the cheapest physically valid
  strategy (co-orbital loitering on the targets' own sma/inc differences, per-leg
  drift purchases, single plane change per leg) and two contained outright bugs.
  The corrected search, reproduced by executed code in this repo, schedules
  **9 rendezvous-costed encounters in 729 days for 196.7 m/s** in the SL-8
  82.9° cluster (threshold: ≥8 in 730 d / 200 m/s).
- **Gate 1 (value of information): passes by the letter, but the pre-registered
  metric is evidentially vacuous** — a zero-information null instrument
  reproduces it (P=0.997 vs 0.999): the top-10 is a degenerate near-tie set and
  flips under any noise. The corrected value measurement (informed-vs-baseline
  selection scored against drawn truth, null-differenced) brackets the dossier
  product's worth at **+0.75% to +5.9% of top-10 campaign risk-per-dollar**,
  where the upper end requires spin state to be material to capture cost and is
  then attributable ~entirely to the spin measurement.
- **Stop rule:** engaged mid-campaign on the (then) Gate-2 FAIL, so Phases 3–4
  were not built; with both gates now formally passing, **Phases 3–4 are
  warranted as the next step** and remain NOT EVALUATED here.

Every number below is labeled **measured** (produced by executed code in this
repo), **assumption** (stated, unverified), or **sourced/external** (URL in
SOURCES.md). Python 3.11.9, pinned deps, master seed 20260705, catalog epoch
2026-07-05.

---

## 1. Gate verdict table

| Gate (as pasted from Step 1) | Threshold | Measured value | Verdict |
|---|---|---|---|
| **Gate 0** (Phase-0 redundancy) | cite instead if ≥80% covered | coverage 45–60% across the four studies | **BUILD** (all four) |
| **Gate 1** (value of information) | dossier dead if P(≥2 of top-10 flip) < 0.20 | P(flips≥2) = 0.9985 [measured] — **but null control = 0.997**, evidential weight ≈ 0; corrected value metric: +0.75% / +5.9% (detumble branches), spin-attributable at the upper end | **PASS by letter; metric shown vacuous — see §3** |
| **Gate 2** (tour economics) | kill if < 8 characterization encounters / vehicle / 24 months / 200 m/s | **9 encounters, 196.7 m/s, 729.2 d** (corrected model, SL-8 82.9° cluster) [measured] | **PASS — does not trip** |
| Gate 3 (taggable population ≥8) | — | — | **NOT EVALUATED** (not built this pass) |
| Gate 4 (tag efficacy) | — | — | **NOT EVALUATED** |
| Gate 5 (ground-sensor erosion) | — | — | **NOT EVALUATED** — §6 argues it is now the decisive open gate |
| Gate 6 (anchor-buyer arithmetic ≥70%) | — | feeding arithmetic in §5 [assumption-heavy] | **NOT EVALUATED** |
| Gate 7 (red-alert value ≥5/yr) | — | — | **NOT EVALUATED** |
| Gate 8 (ODMSP applicator compliance) | — | — | **NOT EVALUATED** |

---

## 2. Phase 0 — prior-art and redundancy check (Gate 0)

Method: 6 web-research agents, 2026-07-05; every cited URL was fetched and
content-verified before being reported. Verdicts: **BUILD** for all four
studies (no published work answers any gate to ≥80%).

- **Study 2 (VoI): 45% covered.** No published Monte-Carlo propagation of
  per-object knowledge uncertainty through removal rankings. Closest: McKnight
  et al.'s own 2025 update (SDC9-paper4: only 20–22 of the 2020 top-50 survive
  to 2025 interim lists, unattributed between environment/method/knowledge);
  Rusconi et al. 2025 (EUCASS-614, index-configuration sensitivity); NASA OTPS
  Phase 2 ($1.5B/30 yr for 10× orbit-uncertainty reduction — conjunction
  screening, not ranking).
- **Study 1 (tour): 60% covered.** GTOC9 corpus brackets the physics (JPL
  winner ~222 m/s/leg at ~25-day legs; DLR 21.7 m/s/leg time-unconstrained;
  Cerf 2013: 5 SSO derelicts/12 months via drift orbits) but does not answer
  ≥8-in-24-months-in-200 m/s on the real catalog. Used as cross-checks (§4).
- **Study 3: 60% covered** (ESA DRAMA/ARES parametric alert-rate tooling; NASA
  CARA reference Foster-Pc; Sang & Bennett single-station SLR accuracy).
  Missing: red-alerts-retired on a specific tagged portfolio. Not built.
- **Study 4: 55% covered** (MMT rotation-state population splits; all three
  observed H-2A stages gravity-gradient stable <0.2°/s; MMT excludes Russian
  objects; no per-family sub-2-min fractions). Not built.

Bonus retrieval: the actual published 2021 top-50 table (rank/name/orbit/mass;
NORAD IDs were never published) via its verbatim reproduction in
arXiv:2510.07708, plus the 2025 interim list. Provenance: SOURCES.md.

---

## 3. Phase 1 — Study 2: value-of-information ranking-flip (Gate 1)

**Population [measured]:** published 2021 top-50 orbit-matched to current
catalog objects — 49/49 matched (median |Δalt| 0.8 km, |Δinc| 0.019°;
`shared/match_top50.py`). Owners: 42 CIS, 4 JPN, 1 each ESA/PRC/FR. Published
per-object masses used. (Known imperfections, adversarially audited: rank-27
row lost to a source-table typo; 6/49 rows matched DEB stand-ins of the right
family — verified immaterial to the experiment, §9.)

**v1 experiment (superseded).** Drew class mass ±50% and area ±20% **iid per
object** and reported P(flips≥2)=0.9995, +12.2% value gain, "spin-only" +8.3%.
Adversarial review (§9) showed all three numbers were artifacts: class-
documentation uncertainty is common-mode across the ~21 SL-16 clones (it cannot
distinguish them); the top-10 is a near-tie set that flips under pure noise
(null instrument: P=0.9975, gain −0.29%); and the "spin-only" variant leaked
the area update (true spin-only: P=0.020).

**v2 experiment (current, `study2_voi/run.py`) [measured, 2,000 draws]:**
class errors common-mode per family; per-object idiosyncratic mass ±5% /
area ±2% [assumption]; documented payload masses ±10% [assumption]; real
per-object spin priors (SL-16 median 200 s, σ_ln 1.4 [sourced, n=4]); a
zero-information **null control**; a **true spin-only** variant; and both
branches of the unvalidatable detumble-cost constant.

| Metric | detumble = 0.004 $M/kN·m·s (spin negligible) | detumble = 1.0 (spin material) |
|---|---|---|
| P(flips≥2), primary | 0.9985 | 0.9975 |
| P(flips≥2), **null control** | 0.997 | 0.9995 |
| evidential weight (P − P_null) | **+0.0015** | **−0.002** |
| value gain vs truth, primary | +0.45% | +5.74% |
| value gain, null control | −0.29% | −0.11% |
| **evidential value gain** | **+0.75%** | **+5.85%** |
| value gain, TRUE spin-only | +0.02% | +5.75% |

**Reading.** The pasted Gate-1 metric passes (0.9985 ≥ 0.20) — but it would
pass for a coin-flipping instrument; it measures ranking degeneracy, not
information. What survives measurement: characterization is worth **+0.75%**
of top-10 campaign risk-per-dollar if spin does not drive capture cost, and
**+5.9%** if it does — in which case the value is delivered almost entirely by
the spin measurement, and the mass/area channels (the original "±50% mass"
premise of the gate) contribute ≈ nothing once class uncertainty is treated as
common-mode. On a $500M removal pipeline, the bracket is roughly **$4M–$30M**
of value [derived], versus Step 1's claimed 20:1 re-ranking leverage.

The decisive unknown is no longer statistical but engineering-economic: *does
target spin state materially change capture-mission cost?* That is answerable
from real mission engineering (e.g., ADRAS-J2 detumble requirements), not from
this simulator.

Outputs: `study2_voi/out/{summary.json, flips.csv, movers.csv, flips_hist.png}`.

---

## 4. Phase 2 — Study 1: differential-J2 tour feasibility (Gate 2)

**Population [measured]:** 449 rocket bodies (+Envisat) with current GP
elements at 600–1000 km, 9 inclination clusters ≥6 members (SL-8 82.9°
n=201; SL-8-like 74.0° n=63; SL-16 71.0° n=20; CZ-4 98.5° n=74; …).

**v1 models (superseded).** Three formulations (fixed-offset MILP; static-gap
water-filling "upper bound"; beam search) all pinned the vehicle to a drift
orbit at cluster-median ±80 km, charged double plane changes to the median
inclination, and two contained bugs (beam leg cost omitted the Hohmann to the
target's actual sma; beam tie-break sign rewarded time-wasting prefixes). They
reported best feasible 5–6 at 200 m/s and "8 needs ~700 m/s" — **wrong**, and
the "upper bound" of 8 was not an upper bound (§9).

**v2 model (current, `study1_tour/run.py` beam) [measured]:** per-leg drift
sma chosen from a grid spanning both endpoints ±80 km *including free
co-orbital loitering at the current target's own sma/inc* (the vehicle inherits
each visited object's plane; targets' own sma/inc spread supplies free
differential nodal drift), exact two-burn Hohmann per leg, ONE plane change
|Δi| per leg, 5 m/s proximity margin, 14-day dwell, time-consistent secular-J2
kinematics throughout.

**Headline [measured]:** in the SL-8 82.9° cluster (201 objects), whose epoch
RAANs include a ~4.3°-wide 9-object micro-window (NORADs 11321, 8874, 21088,
7769, 25893, 9510, 10142, 24773, 22208 — real SL-8 R/Bs at 968–985 km):
**9 encounters, 196.7 m/s, 729.2 days** at the 200 m/s budget. Independent
convergence: two adversarial reviewers hand-constructed 9-encounter schedules
over the same objects (192–195 m/s) before the corrected search reproduced the
result (§9).

**Corrected-model results [measured]:**

| Δv budget (24 mo) | Beam v2 (char) | Beam v2 (tag) | v1 beam (superseded) | v1 "700 m/s" claim |
|---|---|---|---|---|
| 150 m/s | **8** | 6 | 5 | — |
| 200 m/s | **9** (196.7 m/s, 729.2 d) | 7 | 6 | retracted |
| 250 m/s | 9 | 8 | 6 | — |

Sweeps [measured, `sensitivity.csv`]: horizons now help (36 mo → 10, 48 mo →
11 encounters at 200 m/s, SL-8 82.9° cluster); budget at 24 mo: 300 m/s → 10,
700 m/s → 11; beam-500 confirms 9 at 200. The SL-16 71° cluster: 5 (24 mo) /
6 (36–48 mo). Full tables: `study1_tour/out/tours.csv`, `gate2.json`.

**External consistency [sourced]:** corrected per-leg costs (~20–25 m/s at
~80–120-day legs) remain on the published GTOC9 time-Δv frontier (DLR
21.7 m/s/leg time-unconstrained).

**Gate 2: PASS** (9 ≥ 8 within 200 m/s and 24 months, rendezvous costing).
Caveats that temper, but do not overturn, the pass: the enabling micro-window
is a property of the *current epoch geometry* of one cluster (its persistence
over launch delays is untested — differential drift both creates and destroys
such windows); impulsive-transfer and no-drag assumptions stand; and the
top-50-relevant SL-16 cluster still maxes at ~5–6, i.e. the pass is carried by
SL-8s, not by the highest-consequence objects.

---

## 5. Per-object cost arithmetic (feeds Gate 6 — itself NOT EVALUATED)

All cost inputs **[assumption]** unless noted.

- Envelope (all assumptions): 16U-class, ~24 kg dry / ~30 kg wet (green
  monoprop Isp 220 s → 200 m/s ≈ 9% propellant fraction); ~40 W OAP; visible
  imager + photometer; tens of GB downlink. Consistency-checked only.
- Marginal mission: bus+payload $3.0M + launch (30 kg × $7,000/kg [sourced] ≈
  $0.25M w/ integration) + 24-month ops $1.4M ≈ **$4.7M/vehicle**.
- Per-object, marginal: $4.7M / 9 = **$0.52M** (SL-8 window) to /5–6 ≈
  **$0.8–0.9M** (other clusters).
- Per-object, NRE-loaded (+$8–12M NRE): single vehicle **$1.4–1.9M** (9 enc);
  two-vehicle $20M program at 14–18 encounters **$1.1–1.4M**.
- Comparables: NASA SSPICY $15M/3 yr "multiple" targets [sourced; count not
  public → $3–5M/object assumed]; dedicated ADRAS-J-class inspection
  $15–25M/object [external_validation_required]. Advantage: ~8–18× vs the
  dedicated-mission comparable, ~2–4× vs SSPICY — versus Step 1's claimed
  25–50×.

---

## 6. What the campaign established (corrected bottom line)

1. **Feasibility survives; the value thesis is what wobbles.** The vehicle can
   collect ≥8 rendezvous-grade characterizations per 24 months within 200 m/s
   (Gate 2 PASS, measured) — but the measured worth of those characterizations
   to a removal campaign is +0.75%…+5.9% of risk-per-dollar, hinging entirely
   on whether spin state drives capture cost.
2. **The pre-registered Gate-1 metric was mis-designed in Step 1.** It cannot
   fail on this population (null instrument passes it). Any successor campaign
   must gate on null-differenced value, not on rank flips.
3. **The spin measurement is the product.** In the only branch where the
   dossier is worth real money, ~100% of the value is the spin/attitude state
   (+5.75% of +5.74%). This sharpens unevaluated **Gate 5 into the decisive
   question**: if ground photometry/SLR can deliver spin states at <$100k per
   object (erosion gate), the flight mission loses its primary value channel
   regardless of Gate 2's pass. The cheapest next falsification is a
   ground-photometry capability study, not more orbit mechanics.
4. **Cluster geometry, not average geometry, carries the feasibility.** The
   pass rides one dense 9-object SL-8 RAAN window at the current epoch; the
   SL-16s that dominate the published top-50 max out at 5 per vehicle in 24
   months (6 at 36–48 months). A real program must either accept SL-8-class
   targets (lower consequence per object) or budget ≥2 vehicles / 36-month
   missions for SL-16 coverage. Tag-mode tours reach 7 at 200 m/s — just
   under the characterization threshold, relevant if Phases 3–4 revive
   tagging.
5. **Next steps (in falsification order):** (a) detumble-cost engineering
   anchor — does spin drive capture cost by >$5M/object at ADRAS-J2-class
   missions? [kills or crowns the value thesis]; (b) Gate 5 ground-photometry
   erosion study; (c) Phases 3–4 as pre-registered (conjunction/red-alert value;
   taggability census); (d) window-persistence Monte Carlo for the SL-8
   micro-window under launch-date dispersion.

**Limitations (unchanged in kind):** tag adhesion physics (never designed);
bus reliability; impulsive transfers (electric propulsion changes both
budgets); no drag makeup below ~650 km; procurement reality; Studies 3–4 not
built; window persistence untested.

---

## 7. Evidence matrix

| Claim | Evidence type | Module / source | Confidence | What would invalidate |
|---|---|---|---|---|
| Real top-50 matched 49/49 (6 DEB stand-ins, immaterial) | measured + audited | shared/match_top50.py, §9 | high | published NORAD IDs contradicting matches |
| Gate 2 PASS: 9 enc / 196.7 m/s / 729 d | measured (corrected beam) + independent reviewer reconstruction | study1_tour/run.py, §9 | high within model | drag/low-thrust/phasing costs breaking the ~3 m/s margin; window dispersal by launch delay |
| v1 tour models understated feasibility | measured (v1 vs v2 on same data) | §9 | high | — |
| Gate-1 letter metric vacuous | measured (null control) | study2_voi/run.py v2 | high | a population where baseline ranking is not near-tie |
| Dossier value +0.75%…+5.9%, spin-attributable at top | measured on assumed cost model | study2_voi/run.py v2 | medium | validated detumble-cost data; different risk index |
| Class-common-mode prior is the right structure | reviewer analysis + physics | §9 | medium-high | evidence of large per-object mass spread within families |
| Marginal $0.5–0.9M/object | assumption arithmetic on measured counts | §5 | low | any real vehicle/ops quote |
| GTOC9 consistency | sourced cross-check | SOURCES.md | high | — |

---

## 8. Assumptions register (cumulative)

Study 2 v2: class common-mode mass U(0.5,1.5)/area U(0.8,1.2) per family;
idiosyncratic mass ±5%, area ±2%; documented payload mass ±10%; spin lognormal
(family medians, σ_ln 1.4); posterior mass ±15%/±30%, area ±5%, spin ±5%;
flux kinetic-theory v_rel 10 km/s, 20-km shells (binning sensitivity audited,
§9); cost model $40M + $10M/(t·km/s) + {0.004, 1.0} $M/(kN·m·s).
Study 1 v2: rideshare injection co-planar/co-orbital with first target;
14/30-day dwells; 5/15 m/s prox margins; impulsive transfers; drift sma within
endpoints ±80 km; no drag; phase angle ignored; epoch GP elements.
§5: all cost figures.

---

## 9. Adversarial verification log (what changed and why)

Three independent skeptical reviewers (tour physics; VoI design; data
pipeline) were tasked to refute the initial verdicts. All three returned
**fatal** findings. Dispositions:

**Study 1 (initial verdict FAIL — overturned):**
- All three v1 models excluded co-orbital loitering / per-leg-adaptive drift
  and double-charged plane changes → ACCEPTED; corrected model built; two
  reviewers' hand-built 9-encounter schedules over NORADs {11321, 8874, 21088,
  7769, 25893, 9510, 10142, 24773, 22208} (192–195 m/s claimed) reproduced by
  the corrected search at 196.7 m/s. (A pure-loiter-only validator shows free
  drift alone is NOT sufficient — waits of 10³–10⁶ days between same-altitude
  SL-8s; the schedules work because of *purchased* per-leg drift over a dense
  4.3° RAAN window. `study1_tour/validate_schedule.py`.)
- Beam leg cost omitted Hohmann to target sma; tie-break sign rewarded
  time-wasting → ACCEPTED, fixed.
- "adaptive_upper_bound is not an upper bound" → ACCEPTED (contiguity, static
  gaps and double plane costing are not uniformly optimistic); demoted to a
  diagnostic, verdict now rests on the constructive search.
- "~700 m/s needed for 8" → RETRACTED (artifact of the above).
- Stale gate2.json vs run_log discrepancy mid-rerun → ACCEPTED; all outputs
  regenerated from the current code in the final run.
- R/B-only population excludes co-located dead payloads (Tselina-2 etc.) →
  ACCEPTED as a further *pessimistic* bias on v1; not needed for the v2 pass;
  noted for Phase-3/4 population work.

**Study 2 (initial verdict PASS — retained by letter, gutted in substance):**
- Null-instrument reproduces the gate statistic (0.9975 vs 0.9995) → ACCEPTED;
  null control now built into the study; verdict annotated as vacuous.
- iid class-uncertainty across identical SL-16s manufactured the +12.2% gain
  (collapses to ~0.06% fully correlated) → ACCEPTED; v2 uses common-mode class
  + idiosyncratic structure; corrected value bracket +0.75%…+5.9%.
- "spin-only" leaked the area update (true spin-only P=0.020 at negligible
  detumble cost) → ACCEPTED; true spin-only implemented; spin value now
  correctly shown to be entirely contingent on the detumble-cost branch.
- Detumble constant 0.004 makes spin economically irrelevant → ACCEPTED; both
  branches (0.004 / 1.0) now reported; the constant is flagged as the decisive
  unvalidated number in the whole campaign.
- Flux-shell binning (10/20/40 km) shifts the supplementary cross-family
  metric but never the letter verdict (P = 0.996/0.9995/0.981) → ACCEPTED as a
  fragility note; primary metrics unaffected.
- Top-50 match audit: rank-27 typo row lost; 6 DEB stand-ins; Cauchy area
  formula and GP/SATCAT join verified clean → ACCEPTED; documented in §3;
  measured effect on the experiment nil (same-family exchangeability).

Verification cost: 3 reviewer agents, 285k tokens, ~19 min; both initial gate
verdicts were materially wrong or hollow. The campaign's honest deliverable is
this corrected report.
