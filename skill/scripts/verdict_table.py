"""Render a gate verdict table + kill summary from a small JSON/YAML file.

Keeps the campaign's headline verdicts traceable to a machine-checkable source
instead of hand-typed prose. Verdicts are derived from the measured value vs the
frozen threshold when possible, so a typo cannot silently flip a PASS to a TRIP.

Usage:
    python scripts/verdict_table.py gates.json     # or gates.yaml (needs pyyaml)
    python scripts/verdict_table.py                # built-in example

Input: a list of gates, each:
    {"name": "...", "metric": "...", "threshold": 8, "direction": "min",
     "measured": 6, "label": "measured", "note": "..."}
  direction "min" => kill if measured < threshold; "max" => kill if measured > threshold.
  Omit measured (null) => NOT-EVALUATED. Set "verdict" explicitly to override,
  or "provisional": true to mark PROVISIONAL.

Standard library only (JSON). YAML input additionally needs pyyaml.
"""
from __future__ import annotations

import json
import sys


def verdict_for(g: dict) -> str:
    if g.get("verdict"):
        return g["verdict"].upper()
    if g.get("measured") is None:
        return "NOT-EVALUATED"
    if g.get("provisional"):
        return "PROVISIONAL"
    thr, meas, d = g.get("threshold"), g["measured"], g.get("direction", "min")
    if thr is None or not isinstance(meas, (int, float)):
        return "PASS"
    trips = (meas < thr) if d == "min" else (meas > thr)
    return "TRIP" if trips else "PASS"


def render(gates: list) -> str:
    rows = []
    for g in gates:
        v = verdict_for(g)
        meas = g.get("measured")
        mstr = "-" if meas is None else str(meas)
        if g.get("label"):
            mstr += f" [{g['label']}]"
        thr = g.get("threshold")
        tstr = "-" if thr is None else f"{g.get('direction','min')} {thr}"
        rows.append((g.get("name", "?"), g.get("metric", ""), tstr, mstr, v))
    w = [max(len(str(r[i])) for r in rows + [("Gate", "Metric", "Threshold",
         "Measured", "Verdict")]) for i in range(5)]
    def line(cols):
        return "| " + " | ".join(str(c).ljust(w[i]) for i, c in enumerate(cols)) + " |"
    out = [line(("Gate", "Metric", "Threshold", "Measured", "Verdict")),
           "|" + "|".join("-" * (w[i] + 2) for i in range(5)) + "|"]
    out += [line(r) for r in rows]
    trips = sum(1 for r in rows if r[4] == "TRIP")
    ne = sum(1 for r in rows if r[4] == "NOT-EVALUATED")
    prov = sum(1 for r in rows if r[4] == "PROVISIONAL")
    summary = (f"\nSummary: {len(rows)} gates | {trips} TRIP | {prov} PROVISIONAL | "
               f"{ne} NOT-EVALUATED")
    if trips:
        summary += ("\nVERDICT: KILL - at least one gate tripped. Write the "
                    "negative-result report and stop.")
    elif ne:
        summary += ("\nVERDICT: INCONCLUSIVE - gates remain unevaluated; do not "
                    "imply they passed.")
    else:
        summary += ("\nVERDICT: SURVIVES - report residual value with caveats "
                    "before recommending proceed.")
    return "\n".join(out) + "\n" + summary


def _load(path: str) -> list:
    text = open(path, encoding="utf-8").read()
    if path.endswith((".yaml", ".yml")):
        import yaml  # optional dependency
        return yaml.safe_load(text)
    return json.loads(text)


def _example() -> list:
    return [
        {"name": "Gate1-value", "metric": "info gain vs null (%)",
         "threshold": 0.2, "direction": "min", "measured": 1.116,
         "label": "measured", "note": "beats null control"},
        {"name": "Gate2-feasible", "metric": "encounters in budget",
         "threshold": 8, "direction": "min", "measured": 9, "label": "measured"},
        {"name": "Task1-realizable-value", "metric": "$M realizable",
         "threshold": 15, "direction": "min", "measured": 1.5,
         "label": "assumption-laden", "note": "actual-funding world"},
        {"name": "Gate7-red-alerts", "metric": "alerts/yr retired",
         "measured": None, "note": "not built"},
    ]


if __name__ == "__main__":
    gates = _load(sys.argv[1]) if len(sys.argv) > 1 else _example()
    print(render(gates))
