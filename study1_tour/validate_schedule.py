"""Independent validator for an explicit visit sequence (Gate 2 cross-check).

Strategy validated: after each visit the vehicle LOITERS co-orbital with the
just-visited object (zero dv) while natural differential J2 drift (from the
targets' own sma/inc differences) closes the node gap to the next target;
at node alignment it performs one direct Hohmann plus one plane change.
Costing is strict: exact two-burn Hohmann between the two smas, full plane
change at the higher orbit, +5 m/s proximity margin per visit, 14-day dwell.

Usage: python -m study1_tour.validate_schedule 11321 8874 21088 ...
"""
import sys

import numpy as np

from shared import astro, population as pop


def validate(norads, horizon_days=730.0, dv_budget=200.0, dwell=14.0,
             prox=5.0, verbose=True):
    cfg = pop.load_config()
    d = pop.build_derelicts(cfg).set_index("norad")
    seq = d.loc[norads]
    a = seq["a_km"].values
    inc = seq["inc_deg"].values
    ecc = seq["ecc"].values
    raan0 = seq["raan_deg"].values
    rate = astro.raan_rate_deg_day(a, ecc, inc)
    t = dwell            # first visit: injected co-planar with target 0
    dv = prox            # first-visit proximity margin
    rows = [(norads[0], 0.0, t, dv)]
    for j in range(len(norads) - 1):
        rho = rate[j] - rate[j + 1]
        if abs(rho) < 1e-9:
            return None
        ang = (raan0[j + 1] + rate[j + 1] * t) - (raan0[j] + rate[j] * t)
        wait = (ang % 360.0) / rho if rho > 0 else ((-ang) % 360.0) / (-rho)
        dv_leg = (1e3 * astro.hohmann_dv_km_s(a[j], a[j + 1])
                  + 1e3 * astro.plane_change_dv_km_s(max(a[j], a[j + 1]),
                                                     inc[j + 1] - inc[j])
                  + prox)
        t += wait + dwell
        dv += dv_leg
        rows.append((norads[j + 1], round(wait, 1), round(t, 1), round(dv, 1)))
    ok = t <= horizon_days and dv <= dv_budget
    if verbose:
        print(f"{'norad':>8} {'wait_d':>8} {'t_done_d':>9} {'dv_cum':>7}")
        for r in rows:
            print(f"{r[0]:>8} {r[1]:>8} {r[2]:>9} {r[3]:>7}")
        print(f"visits={len(rows)}  t={t:.1f} d (<=730: {t<=horizon_days})  "
              f"dv={dv:.1f} m/s (<=200: {dv<=dv_budget})  FEASIBLE={ok}")
    return {"visits": len(rows), "t_days": t, "dv_m_s": dv, "feasible": ok}


if __name__ == "__main__":
    validate([int(x) for x in sys.argv[1:]])
