"""Step 3 Task 3 — value coverage of tours + launch-slip robustness.

(i) F(budget,horizon): fraction of pre-registered per-object VoI weight
collectible by a value-restricted tour (beam over top-50 members only, per
inclination cluster); best-1-vehicle and best-2-vehicle reported.
(ii) Slip test: SL-8 82.9-deg full-cluster tour at 200 m/s / 24 months with
all epoch RAANs advanced by each object's own secular rate, +6/+12/+24 months.

Usage: python -m step3_value.tour_value
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
    t = cfg["tour"]
    w = pd.read_csv(OUT / "voi_weights.csv")
    wcol = [c for c in w.columns if c.startswith("w_")]

    # --- (i) value-restricted tours over the 49 matched top-50 objects ------
    vb = w.rename(columns={"norad": "norad"}).copy()
    vb = inclination_clusters(vb, t["inc_cluster_deg"], min_size=2)
    rows = []
    for budget in (150.0, 200.0, 250.0):
        for horizon in (730.0, 1095.0, 1460.0):
            c2 = copy.deepcopy(cfg)
            c2["tour"]["horizon_days"] = horizon
            per_cluster = []
            for _, cl in vb.groupby("cluster"):
                cl = cl.reset_index(drop=True)
                r = beam_search_tour(cl, c2, budget, t["dwell_char_days"],
                                     t["prox_margin_char_m_s"])
                got = w[w["norad"].isin(r.get("targets", []))]
                per_cluster.append({
                    "cluster": f"{cl['family'].mode().iat[0]} i={cl['inc_deg'].median():.1f} n={len(cl)}",
                    "count": r["count"],
                    **{c: float(got[c].sum()) for c in wcol}})
            per_cluster.sort(key=lambda x: -x[wcol[-1]])
            best1, best2 = per_cluster[0], per_cluster[:2]
            rows.append({"budget": budget, "horizon": horizon,
                         "best1_cluster": best1["cluster"], "best1_count": best1["count"],
                         **{f"F1_{c}": round(best1[c], 3) for c in wcol},
                         **{f"F2_{c}": round(sum(x[c] for x in best2), 3) for c in wcol},
                         "best2_count": sum(x["count"] for x in best2)})
    cov = pd.DataFrame(rows)
    cov.to_csv(OUT / "value_coverage.csv", index=False)
    print(cov.to_string(index=False))

    # --- (ii) launch-slip robustness on the SL-8 82.9-deg full cluster ------
    from shared import astro
    band = pop.band_filter(pop.build_derelicts(cfg), cfg)
    clustered = inclination_clusters(band, t["inc_cluster_deg"], t["min_cluster_size"])
    slip_rows = []
    for _, cl in clustered.groupby("cluster"):
        if not (82.5 < cl["inc_deg"].median() < 83.3):
            continue
        cl = cl.reset_index(drop=True)
        rate = astro.raan_rate_deg_day(cl["a_km"].values, cl["ecc"].values,
                                       cl["inc_deg"].values)
        for slip_d in (0.0, 183.0, 365.0, 730.0):
            cl2 = cl.copy()
            cl2["raan_deg"] = (cl["raan_deg"].values + rate * slip_d) % 360.0
            r = beam_search_tour(cl2, cfg, 200.0, t["dwell_char_days"],
                                 t["prox_margin_char_m_s"])
            slip_rows.append({"slip_months": round(slip_d / 30.4, 0),
                              "count": r["count"], "dv_m_s": r.get("dv_total_m_s"),
                              "t_days": r.get("t_end_days")})
    slip = pd.DataFrame(slip_rows)
    slip.to_csv(OUT / "slip_test.csv", index=False)
    print(slip.to_string(index=False))


if __name__ == "__main__":
    main()
