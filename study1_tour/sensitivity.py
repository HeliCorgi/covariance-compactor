"""Study 1 sensitivity: horizon, beam width, and budget sweep.

Regenerates the sweep numbers quoted in RESULTS.md for the CORRECTED
(co-orbital, per-leg-adaptive) tour model. Earlier claims produced by the
defective v1 model (e.g., "8 encounters requires ~700 m/s") are superseded;
see RESULTS.md section 9.

Usage: python -m study1_tour.sensitivity
"""
import copy
import pathlib

import pandas as pd

from shared import population as pop
from study1_tour.run import beam_search_tour, inclination_clusters

OUT = pathlib.Path(__file__).resolve().parent / "out"


def main():
    OUT.mkdir(exist_ok=True)
    cfg = pop.load_config()
    band = pop.band_filter(pop.build_derelicts(cfg), cfg)
    clustered = inclination_clusters(band, cfg["tour"]["inc_cluster_deg"],
                                     cfg["tour"]["min_cluster_size"])
    cls = {f"{cl['family'].mode().iat[0]} i={cl['inc_deg'].median():.1f} n={len(cl)}":
           cl.reset_index(drop=True) for _, cl in clustered.groupby("cluster")}
    rows = []
    for horizon in (730.0, 1095.0, 1460.0):
        c2 = copy.deepcopy(cfg)
        c2["tour"]["horizon_days"] = horizon
        for name, cl in cls.items():
            r = beam_search_tour(cl, c2, 200.0, c2["tour"]["dwell_char_days"],
                                 c2["tour"]["prox_margin_char_m_s"])
            rows.append({"sweep": "horizon", "value": horizon, "cluster": name,
                         "count": r["count"], "dv_m_s": r.get("dv_total_m_s"),
                         "t_days": r.get("t_end_days")})
    for name in ("SL-16 i=71.0 n=20", "SL-8 i=74.0 n=63", "SL-8 i=82.9 n=201"):
        r = beam_search_tour(cls[name], cfg, 200.0, 14.0, 5.0, beam_width=500)
        rows.append({"sweep": "beam500", "value": 200.0, "cluster": name,
                     "count": r["count"], "dv_m_s": r.get("dv_total_m_s"),
                     "t_days": r.get("t_end_days")})
    for budget in (300.0, 500.0, 700.0):
        best_n, best_name = max((beam_search_tour(cl, cfg, budget, 14.0, 5.0)["count"], n)
                                for n, cl in cls.items())
        rows.append({"sweep": "budget", "value": budget, "cluster": best_name,
                     "count": best_n, "dv_m_s": None, "t_days": None})
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "sensitivity.csv", index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
