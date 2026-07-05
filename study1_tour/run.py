"""Study 1 — differential-J2 tour feasibility MILP (Gate 2).

Model: the vehicle parks at a drift altitude offset da from an
inclination-cluster of derelicts; differential J2 nodal regression sweeps its
RAAN relative to each target. Visiting target k costs a full rendezvous
(descend to the target's sma and return: 2x Hohmann, plus inclination match
to the cluster median, plus a proximity-ops margin) and a dwell during which
sweeping is paused. For each (cluster, drift offset, sweep direction, anchor
start target) a small MILP selects the visit subset maximizing encounters
subject to the 24-month horizon and the delta-v budget.

Conservative choices (all harder to pass, per the pasted Gate 2):
  * every visit costed as a full rendezvous, never a flyby;
  * inclination mismatch paid twice (go and return to cluster median plane);
  * dwell pauses the RAAN sweep.

Usage: python -m study1_tour.run
"""
import json
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pulp

from shared import astro, population as pop

OUT = pathlib.Path(__file__).resolve().parent / "out"


def inclination_clusters(band: pd.DataFrame, link_deg: float, min_size: int):
    df = band.sort_values("inc_deg").reset_index(drop=True)
    breaks = np.where(np.diff(df["inc_deg"].values) > link_deg)[0]
    ids = np.zeros(len(df), dtype=int)
    for b in breaks:
        ids[b + 1:] += 1
    df["cluster"] = ids
    sizes = df.groupby("cluster")["norad"].count()
    keep = sizes[sizes >= min_size].index
    return df[df["cluster"].isin(keep)].copy()


def solve_anchor_milp(t_align, dv_visit, dwell_days, horizon, dv_budget, time_limit):
    """Select visits maximizing count: t_align (days) fixed alignment times,
    additive dwell, additive dv. Returns (count, dv_used, t_used, chosen idx)."""
    n = len(t_align)
    prob = pulp.LpProblem("tour", pulp.LpMaximize)
    x = [pulp.LpVariable(f"x{k}", cat="Binary") for k in range(n)]
    t_end = pulp.LpVariable("t_end", lowBound=0, upBound=horizon)
    prob += pulp.lpSum(x)
    for k in range(n):
        # if selected, the sweep must reach it: alignment time counts toward t_end
        prob += t_align[k] * x[k] <= t_end
    prob += t_end + dwell_days * pulp.lpSum(x) <= horizon
    prob += pulp.lpSum(dv_visit[k] * x[k] for k in range(n)) <= dv_budget
    prob.solve(pulp.PULP_CBC_CMD(msg=0, timeLimit=time_limit))
    if pulp.LpStatus[prob.status] != "Optimal":
        return 0, 0.0, 0.0, []
    chosen = [k for k in range(n) if x[k].value() and x[k].value() > 0.5]
    dv_used = float(sum(dv_visit[k] for k in chosen))
    t_used = float(max([t_align[k] for k in chosen], default=0.0)
                   + dwell_days * len(chosen))
    return len(chosen), dv_used, t_used, chosen


def tour_search(cl: pd.DataFrame, cfg, dv_budget_m_s, dwell_days, prox_m_s):
    """Best tour over drift offsets, directions, anchors for one cluster."""
    t = cfg["tour"]
    a_med = cl["a_km"].median()
    i_med = cl["inc_deg"].median()
    raan = cl["raan_deg"].values
    a_k = cl["a_km"].values
    inc_k = cl["inc_deg"].values
    ecc_k = cl["ecc"].values
    n = len(cl)
    # per-visit dv [m/s]: 2x Hohmann + 2x inc match + prox margin
    dv_alt = 2.0e3 * astro.hohmann_dv_km_s(np.full(n, a_med), a_k)  # placeholder vs a_d below
    best = None
    for off in t["drift_offsets_km"]:
        for sign in (+1.0, -1.0):
            a_d = a_med + sign * off
            rate_v = astro.raan_rate_deg_day(a_d, 0.0, i_med)
            rho = rate_v - astro.raan_rate_deg_day(a_k, ecc_k, inc_k)  # deg/day
            dv_alt = 2.0e3 * astro.hohmann_dv_km_s(np.full(n, a_d), a_k)
            dv_inc = 2.0e3 * astro.plane_change_dv_km_s(a_k, inc_k - i_med)
            dv_visit = dv_alt + dv_inc + prox_m_s
            dv_init = 1.0e3 * astro.hohmann_dv_km_s(a_med, a_d)
            for sweep in (+1.0, -1.0):
                ok = np.where(sweep * rho > 1e-4)[0]
                if len(ok) < 2:
                    continue
                idx = ok[np.argsort((-np.sign(sweep)) * raan[ok])]  # any order; anchor loop below
                for anchor in ok:
                    rel = (sweep * (raan[ok] - raan[anchor])) % 360.0
                    t_align = rel / np.abs(rho[ok])
                    feas = t_align <= t["horizon_days"]
                    if feas.sum() < 2:
                        continue
                    cnt, dvu, tu, chosen = solve_anchor_milp(
                        t_align[feas], dv_visit[ok][feas], dwell_days,
                        t["horizon_days"], dv_budget_m_s - dv_init,
                        t["milp_time_limit_s"])
                    if best is None or cnt > best["count"] or (
                            cnt == best["count"] and dvu < best["dv_visits_m_s"]):
                        sel_global = ok[feas][chosen] if chosen else []
                        best = {"count": cnt, "offset_km": float(sign * off),
                                "sweep": sweep, "anchor_norad": int(cl["norad"].values[anchor]),
                                "dv_init_m_s": float(dv_init),
                                "dv_visits_m_s": dvu,
                                "dv_total_m_s": float(dv_init + dvu),
                                "t_used_days": tu,
                                "rate_deg_day": float(np.median(np.abs(rho))),
                                "targets": [int(x) for x in cl["norad"].values[sel_global]]}
    return best


def adaptive_upper_bound(cl: pd.DataFrame, cfg, dv_budget_m_s, dwell_days,
                         prox_m_s, dmax_km=80.0, flyby=False):
    """Per-leg-adaptive drift-offset optimum (static-gap approximation).

    For a contiguous RAAN window of n targets with gaps g_i, the minimal drift
    delta-v given total drift time T is (2*c1/(k_r*T)) * (sum sqrt(g_i))^2
    (Lagrange water-filling, t_i ~ sqrt(g_i)), with per-leg offsets capped at
    dmax_km via iterative pinning. Optimistic vs the fixed-offset MILP:
    assumes epoch RAAN gaps are static over the tour (intra-cluster
    differential drift ignored) — so this is an UPPER BOUND on encounters.
    flyby=True zeroes the descent cost (vehicle never leaves drift altitude):
    reference-only reproduction of the Step-1 'flyby costing' that the
    adversarial review rejected; data quality at 10-80 km standoff untested.
    """
    t = cfg["tour"]
    horizon = t["horizon_days"]
    a_med, i_med = cl["a_km"].median(), cl["inc_deg"].median()
    c1 = 1.0e3 * astro.hohmann_dv_km_s(a_med, a_med + 1.0)     # m/s per km, one-way
    k_r = 3.5 * abs(astro.raan_rate_deg_day(a_med, 0.0, i_med)) / a_med  # deg/day/km
    order = cl.sort_values("raan_deg").reset_index(drop=True)
    raan = order["raan_deg"].values
    extras_all = (2.0e3 * astro.plane_change_dv_km_s(
        order["a_km"].values, order["inc_deg"].values - i_med) + prox_m_s)
    if flyby:
        extras_all = np.full(len(order), prox_m_s)
    n_obj = len(order)
    gaps = np.diff(np.concatenate([raan, raan[:1] + 360.0]))   # circular
    best = {"count": 0}

    def drift_dv(g, T):
        if flyby:
            # one-time offset acquisition only; sweep covers sum(g) if fast enough
            need = np.sum(g) / (k_r * dmax_km)                 # days at max offset
            return (2.0 * c1 * dmax_km) if need <= T else None
        t_min = g / (k_r * dmax_km)
        if np.sum(t_min) > T:
            return None
        free = np.ones(len(g), bool)
        t_alloc = np.zeros(len(g))
        T_rem = T
        for _ in range(len(g)):
            s = np.sqrt(g[free]).sum()
            t_alloc[free] = T_rem * np.sqrt(g[free]) / s
            viol = free & (t_alloc < t_min - 1e-12)
            if not viol.any():
                break
            t_alloc[viol] = t_min[viol]
            T_rem = T - t_alloc[~free & ~viol].sum() - t_min[viol].sum()
            free = free & ~viol
            if T_rem <= 0:
                return None
        return float(np.sum(2.0 * c1 * g / (k_r * t_alloc)))

    max_n = min(n_obj, int(horizon // dwell_days))
    for n in range(max_n, 1, -1):
        t_avail = horizon - n * dwell_days
        if t_avail <= 0:
            continue
        for s in range(n_obj):
            idx = [(s + j) % n_obj for j in range(n)]
            g = gaps[[(s + j) % n_obj for j in range(n - 1)]]
            if np.sum(g) >= 360.0:
                continue
            extras = extras_all[idx].sum()
            if extras >= dv_budget_m_s:
                continue
            dv_d = drift_dv(g, t_avail)
            if dv_d is not None and dv_d + extras <= dv_budget_m_s:
                best = {"count": n, "start_norad": int(order["norad"].values[s]),
                        "arc_deg": float(np.sum(g)),
                        "dv_drift_m_s": round(dv_d, 1),
                        "dv_extras_m_s": round(float(extras), 1),
                        "dv_total_m_s": round(dv_d + float(extras), 1)}
                break
        if best["count"]:
            break
    return best


def beam_search_tour(cl: pd.DataFrame, cfg, dv_budget_m_s, dwell_days,
                     prox_m_s, dmax_km=80.0, beam_width=300):
    """Time-consistent, per-leg-adaptive tour construction (tie-breaker).

    Exact secular kinematics: every target's RAAN advances at its own J2 rate;
    a leg to target k at drift offset delta reaches alignment after
    tau = wrapped_angle / |rate_v(delta) - rate_k|. Any schedule found is
    FEASIBLE under the model (a constructive lower bound that, unlike the
    fixed-offset MILP, adapts the offset per leg and, unlike the analytic
    upper bound, does not freeze epoch gaps). Beam search over sequences;
    per candidate leg two offset choices are expanded: cheapest-feasible and
    fastest (dmax).
    """
    t = cfg["tour"]
    horizon = t["horizon_days"]
    a_arr = cl["a_km"].values
    inc_arr = cl["inc_deg"].values
    raan0 = cl["raan_deg"].values
    rate = astro.raan_rate_deg_day(a_arr, cl["ecc"].values, inc_arr)
    norads = cl["norad"].values
    n = len(cl)

    def leg(j, k, t_now):
        """(tau_days, dv_m_s) options for leg j->k starting t_now.

        Corrected model (post adversarial review): the vehicle leaves target j
        (sma a_j, inc i_j), coasts at a chosen drift sma a_d (including a_j
        itself — free co-orbital loitering exploiting the targets' OWN sma/inc
        differences), and on node alignment transfers to target k with exact
        Hohmann legs and ONE plane change |i_k - i_j|. The original version
        pinned a_d to the cluster median +/- offset, never charged the Hohmann
        to the target's actual sma, and double-charged plane changes — defects
        that suppressed feasible schedules (see RESULTS.md section 9).
        """
        a_j, a_k = a_arr[j], a_arr[k]
        grid = {a_j, a_k, 0.5 * (a_j + a_k)}
        for dd in (20.0, 50.0, dmax_km):
            grid |= {a_j + dd, a_j - dd, a_k + dd, a_k - dd}
        dv_plane = 1.0e3 * astro.plane_change_dv_km_s(max(a_j, a_k),
                                                      inc_arr[k] - inc_arr[j])
        ang0 = (raan0[k] + rate[k] * t_now) - (raan0[j] + rate[j] * t_now)
        cands = []
        for a_d in grid:
            rho = astro.raan_rate_deg_day(a_d, 0.0, inc_arr[j]) - rate[k]
            if abs(rho) < 1e-7:
                continue
            ang = ang0 % 360.0 if rho > 0 else (-ang0) % 360.0
            tau = ang / abs(rho)
            if t_now + tau + dwell_days > horizon:
                continue
            dv = (1.0e3 * (astro.hohmann_dv_km_s(a_j, a_d)
                           + astro.hohmann_dv_km_s(a_d, a_k))
                  + dv_plane + prox_m_s)
            cands.append((tau, float(dv)))
        if not cands:
            return []
        cheapest = min(cands, key=lambda x: x[1])
        fastest = min(cands, key=lambda x: x[0])
        mid = min(cands, key=lambda x: x[0] * 0.27 + x[1] * 0.0037 * 730.0 / 200.0)
        out = [cheapest]
        for c in (fastest, mid):
            if c not in out:
                out.append(c)
        return out

    # states: (count, -dv, t, current, visited bitmask)
    # first visit: injected co-planar and co-orbital with the start target
    beams = [(1, -prox_m_s, dwell_days, s, 1 << s) for s in range(n)]
    best = max(beams, key=lambda b: b[0]) if beams else None
    while beams:
        nxt = []
        for cnt, negdv, t_now, cur, mask in beams:
            for k in range(n):
                if mask & (1 << k):
                    continue
                for tau, dv_leg in leg(cur, k, t_now):
                    dv_new = -negdv + dv_leg
                    if dv_new > dv_budget_m_s:
                        continue
                    nxt.append((cnt + 1, -dv_new, t_now + tau + dwell_days,
                                k, mask | (1 << k)))
        if not nxt:
            break
        # prefer fewer resources spent: ascending (dv + 0.27*t). The original
        # key had an inverted sign that rewarded time-wasting prefixes.
        nxt.sort(key=lambda b: (-b[0], -b[1] + 0.27 * b[2]))
        seen, dedup = set(), []
        for b in nxt:
            key = (b[3], b[4])
            if key not in seen:
                seen.add(key)
                dedup.append(b)
            if len(dedup) >= beam_width:
                break
        beams = dedup
        cand = max(beams, key=lambda b: (b[0], b[1]))
        if best is None or cand[0] > best[0]:
            best = cand
    if best is None:
        return {"count": 0, "targets": []}
    visited = [int(norads[i]) for i in range(n) if best[4] & (1 << i)]
    return {"count": int(best[0]), "dv_total_m_s": round(-best[1], 1),
            "t_end_days": round(best[2], 1),
            "final_norad": int(norads[best[3]]), "targets": visited}


def main():
    OUT.mkdir(exist_ok=True)
    cfg = pop.load_config()
    t = cfg["tour"]
    band = pop.band_filter(pop.build_derelicts(cfg), cfg)
    clustered = inclination_clusters(band, t["inc_cluster_deg"], t["min_cluster_size"])
    rows, plans = [], {}
    for cid, cl_full in clustered.groupby("cluster"):
        label = (f"{cl_full['family'].mode().iat[0]}-like i={cl_full['inc_deg'].median():.1f} "
                 f"alt={cl_full['alt_km'].median():.0f} n={len(cl_full)}")
        cl_full = cl_full.reset_index(drop=True)
        # cap applies ONLY to the fixed-offset MILP (anchor enumeration cost);
        # beam search and the analytic bound use the full cluster
        cl_milp = (cl_full.sort_values("mass_kg", ascending=False)
                   .head(t["milp_max_nodes"]) if len(cl_full) > t["milp_max_nodes"]
                   else cl_full)
        for budget in t["dv_budgets_m_s"]:
            for mode, dwell, prox in (("char", t["dwell_char_days"], t["prox_margin_char_m_s"]),
                                      ("tag", t["dwell_tag_days"], t["prox_margin_tag_m_s"])):
                best = tour_search(cl_milp, cfg, budget, dwell, prox)
                ub = adaptive_upper_bound(cl_full, cfg, budget, dwell, prox)
                beam = beam_search_tour(cl_full, cfg, budget, dwell, prox)
                fly = adaptive_upper_bound(cl_full, cfg, budget, 2.0, prox, flyby=True) \
                    if mode == "char" else {"count": None}
                if best is None and ub["count"] == 0 and beam["count"] == 0:
                    continue
                rows.append({"cluster": label, "budget_m_s": budget, "mode": mode,
                             "count_beam": beam["count"],
                             "beam_dv_m_s": beam.get("dv_total_m_s"),
                             "beam_t_days": beam.get("t_end_days"),
                             "count_ub_adaptive": ub["count"],
                             "ub_arc_deg": ub.get("arc_deg"),
                             "ub_dv_total_m_s": ub.get("dv_total_m_s"),
                             "count_flyby_ref": fly["count"],
                             **{k: vv for k, vv in (best or {"count": 0}).items()
                                if k != "targets"}})
                if best:
                    plans[f"{label}|{budget}|{mode}"] = best["targets"]
    res = pd.DataFrame(rows).sort_values(["mode", "budget_m_s", "count"],
                                         ascending=[True, True, False])
    res.to_csv(OUT / "tours.csv", index=False)
    (OUT / "plans.json").write_text(json.dumps(plans, indent=1))

    char = res[res["mode"] == "char"]
    beam200 = char[char["budget_m_s"] == 200.0].sort_values("count_beam", ascending=False)
    gate2 = {"gate2_threshold": ">=8 characterization encounters / vehicle / 24 months in 200 m/s (rendezvous costing)",
             "beam_best_at_200": int(beam200["count_beam"].max()) if len(beam200) else 0,
             "beam_best_cluster": beam200.iloc[0]["cluster"] if len(beam200) else None,
             "beam_by_budget": {str(b): int(char[char["budget_m_s"] == b]["count_beam"].max())
                                for b in t["dv_budgets_m_s"]},
             "milp_by_budget": {str(b): int(char[char["budget_m_s"] == b]["count"].max())
                                for b in t["dv_budgets_m_s"]},
             "adaptive_ub_by_budget": {str(b): int(char[char["budget_m_s"] == b]["count_ub_adaptive"].max())
                                       for b in t["dv_budgets_m_s"]},
             "flyby_reference_by_budget": {str(b): int(char[char["budget_m_s"] == b]["count_flyby_ref"].max())
                                           for b in t["dv_budgets_m_s"]},
             "tag_mode_beam_by_budget": {str(b): int(res[(res["mode"] == "tag") & (res["budget_m_s"] == b)]["count_beam"].max())
                                         for b in t["dv_budgets_m_s"]}}
    # primary verdict: beam (time-consistent AND per-leg adaptive — a
    # constructive feasible schedule). The static-gap analytic bound reaches 8
    # only by freezing epoch RAAN gaps, which the time-consistent methods show
    # is unphysical over a ~2-year tour; see sensitivity.py for the beam-500
    # robustness check and the budget sweep (8 encounters needs ~700 m/s).
    feasible = gate2["beam_best_at_200"]
    ub = gate2["adaptive_ub_by_budget"]["200.0"]
    gate2["gate2_verdict"] = ("PASS (does not trip)" if feasible >= 8 else
                              f"FAIL (trips: best feasible schedule={feasible} < 8; "
                              f"static-gap upper bound={ub} shown unphysical)")
    (OUT / "gate2.json").write_text(json.dumps(gate2, indent=2))

    fig, ax = plt.subplots(figsize=(7, 4))
    for label, gr in char.groupby("cluster"):
        gr = gr.sort_values("budget_m_s")
        ax.plot(gr["budget_m_s"], gr["count"], marker="o", label=label)
    ax.axhline(8, color="#cc3311", ls="--", label="gate: 8 encounters")
    ax.set_xlabel("delta-v budget [m/s]")
    ax.set_ylabel("encounters in 24 months")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT / "encounters_vs_budget.png", dpi=120)
    print(json.dumps(gate2, indent=2))
    print(res.head(12).to_string(index=False))


if __name__ == "__main__":
    main()
