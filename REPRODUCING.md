# Gate-driven falsification campaign — derelict characterization mission

Executed falsification studies for a fixed concept (Step-1 concept brief:
government-anchored derelict-characterization tours with optional
retroreflector tagging). This is **not** a mission-design document; it is the
evidence for gate verdicts. **Outcome after adversarial verification
(RESULTS.md §9): Gate 2 PASSES (9 encounters / 197 m/s / 24 months feasible —
initial FAIL was a model artifact), and Gate 1 passes by the letter but is
evidentially vacuous — a zero-information null instrument reproduces it; the
corrected value-of-information measurement brackets the dossier product's
worth at +0.7% to +5.9% of campaign risk-per-dollar, almost entirely
attributable to spin-state knowledge under the spin-material cost branch.**
Phases 3–4 were not built in this pass (initially stopped by the later-
overturned Gate-2 FAIL); they are warranted next. See `RESULTS.md`.

## Regeneration

```
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt   # pinned, Python 3.11.9
.venv/Scripts/python run_all.py
```

Individual studies run standalone:

```
.venv/Scripts/python -m study2_voi.run          # Gate 1 (value of information)
.venv/Scripts/python -m study1_tour.run         # Gate 2 (tour feasibility)
.venv/Scripts/python -m study1_tour.sensitivity # horizon/beam/budget sweeps
```

Determinism: `master_seed` in `config.yaml`; per-run seeds are
`master_seed + run_index` (pass an integer argv to `study2_voi.run`).

`shared/fetch_data.py` is idempotent (cached files in `data/raw/` are kept;
delete to re-fetch — results will then reflect the new catalog epoch).
Raw-data provenance: `SOURCES.md`.

## Layout

- `config.yaml` — all parameters, each labeled measured / assumption / sourced
- `shared/` — data fetch, population loading, secular-J2 astro, top-50 matching
- `study2_voi/` — Phase 1: Bayesian ranking-flip experiment (Gate 1) — **PASS**
- `study1_tour/` — Phase 2: differential-J2 tour MILP + adaptive bound + beam
  search (Gate 2) — **FAIL**
- `study3_conjunction/`, `study4_taggability/` — not built this pass (see RESULTS.md §1)
- `RESULTS.md` — gate verdict table, evidence matrix, negative-result report
