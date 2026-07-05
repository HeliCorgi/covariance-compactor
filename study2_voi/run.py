"""Study 2 — value-of-information ranking-flip experiment (Gate 1). v2.

v1 was found FATALLY DEFECTIVE by adversarial review (RESULTS.md section 9):
it drew class-documentation mass/area uncertainty iid per object across ~21
statistically identical SL-16s, manufacturing "information value" out of a
degenerate near-tie ranking; a zero-information null instrument reproduced
the gate statistic (P=0.9975 vs 0.9995); and the "spin-only" variant leaked
the area update.

v2 corrections:
  * class-documentation uncertainty is COMMON-MODE per family; objects are
    distinguished only by idiosyncratic terms (residual propellant ~5%,
    surface ~2% [assumption]) and by their real per-object spin states;
  * a null-instrument control (posterior noise around prior points, zero
    truth content) is run alongside every branch — the gate's evidential
    weight is (P_primary - P_null) and (gain_primary - gain_null);
  * a TRUE spin-only variant freezes both mass and area;
  * the unvalidatable detumble-cost constant is run at both branch values
    (0.004 = spin economically negligible; 1.0 = spin material).

Per Monte Carlo draw: truth ~ corrected prior; baseline decision = top-10 by
priority(prior points) [fixed]; informed decision = top-10 by
priority(truth x posterior noise); flips = |informed \\ baseline|; value =
true-risk-per-dollar of the informed vs baseline selection.

Gate 1 (pasted, unchanged): dossier product dead if P(flips>=2) < 0.20.

Usage: python -m study2_voi.run [run_index]
"""
import json
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from shared import astro, population as pop

OUT = pathlib.Path(__file__).resolve().parent / "out"


def removal_cost_musd(cfg, mass_kg, length_m, spin_period_s, a_km, c_dt):
    v = cfg["voi"]
    dv = astro.deorbit_dv_km_s(a_km, v["deorbit_perigee_km"])          # km/s
    inertia = mass_kg * length_m**2 / 12.0                              # kg m^2
    omega = 2.0 * np.pi / spin_period_s                                 # rad/s
    h_knms = inertia * omega / 1e3                                      # kN m s
    return (v["cost_fixed_musd"]
            + v["cost_dv_musd_per_tkm_s"] * (mass_kg / 1e3) * dv
            + c_dt * h_knms)


def risk_score(flux_yr, area_m2, mass_kg):
    """Expected catastrophic-fragment generation rate, up to a constant:
    collision rate (flux x area) times NASA-SBM consequence scaling M^0.75."""
    return flux_yr * area_m2 * (mass_kg ** 0.75)


def top_k(scores, k):
    return set(np.argsort(-scores)[:k])


def main(run_index: int = 0):
    OUT.mkdir(exist_ok=True)
    cfg = pop.load_config()
    v = cfg["voi"]
    rng = np.random.default_rng(cfg["master_seed"] + run_index)

    dens = pop.catalog_spatial_density(v["shell_km"])
    real_list = pathlib.Path("data/processed/top50_match.csv")
    if real_list.exists():
        sel = pd.read_csv(real_list)
        sel = sel[sel["norad"].notna()].copy()
        sel["mass_kg"] = sel["mass_pub_kg"].fillna(sel["family"].map(
            lambda k: cfg["families"][k]["mass_kg"]))
        pop_label = (f"REAL-TOP50 (McKnight 2021 published table, {len(sel)}/50 "
                     "orbit-matched to current catalog, published masses)")
    else:
        band = pop.band_filter(pop.build_derelicts(cfg), cfg)
        band["flux_yr"] = pop.flux_at_alt(band["alt_km"], dens, v["flux_vrel_km_s"])
        band["risk_pt"] = risk_score(band["flux_yr"], band["area_m2"], band["mass_kg"])
        sel = band.sort_values("risk_pt", ascending=False).head(v["n_top"]).copy()
        pop_label = "PROXY-TOP50 (catalog-derived, class masses; SYNTHETIC-RANKING)"
    sel["flux_yr"] = pop.flux_at_alt(sel["alt_km"], dens, v["flux_vrel_km_s"])
    sel = sel.reset_index(drop=True)
    n = len(sel)

    med = v["spin_period_median_s"]
    spin_med = sel["family"].map(lambda f: med.get(f, med["default"])).values
    m_hat, a_hat = sel["mass_kg"].values, sel["area_m2"].values
    f_hat, sma = sel["flux_yr"].values, sel["a_km"].values
    L = sel["length_m"].values
    families = sel["family"].values
    fam_list = sorted(set(families))
    fam_idx = np.array([fam_list.index(f) for f in families])
    # payloads carry published per-object masses -> no class common-mode term
    documented = np.isin(families, ["PAY", "ENVISAT", "OTHER"])

    def truth_draw():
        cm_m = rng.uniform(v["prior_mass_lo"], v["prior_mass_hi"], len(fam_list))[fam_idx]
        cm_a = rng.uniform(1 - v["prior_area_frac"], 1 + v["prior_area_frac"],
                           len(fam_list))[fam_idx]
        im, ia = v["prior_mass_idio_frac"], v["prior_area_idio_frac"]
        m_t = m_hat * np.where(
            documented,
            rng.uniform(1 - v["documented_mass_frac"], 1 + v["documented_mass_frac"], n),
            cm_m * rng.uniform(1 - im, 1 + im, n))
        a_t = a_hat * np.where(documented, 1.0, cm_a) * rng.uniform(1 - ia, 1 + ia, n)
        f_t = f_hat * rng.uniform(1 - v["prior_flux_frac"], 1 + v["prior_flux_frac"], n)
        s_t = spin_med * rng.lognormal(0.0, v["spin_period_sigma_ln"], n)
        return m_t, a_t, f_t, s_t

    def experiment(c_dt, post_mass_frac, variant="primary"):
        """variant: primary | spin_only (mass AND area frozen at prior points)
        | null (posterior noise around prior points, ZERO truth content)."""
        base10 = top_k(risk_score(f_hat, a_hat, m_hat)
                       / removal_cost_musd(cfg, m_hat, L, spin_med, sma, c_dt),
                       v["top_k"])
        nd = v["n_draws"]
        flips = np.zeros(nd, dtype=int)
        regret_gain = np.zeros(nd)
        enter_counts = np.zeros(n, dtype=int)
        for d in range(nd):
            m_t, a_t, f_t, s_t = truth_draw()
            if variant == "null":
                m_i = m_hat * rng.lognormal(0.0, post_mass_frac, n)
                a_i = a_hat * rng.lognormal(0.0, v["post_area_frac"], n)
                s_i = spin_med * rng.lognormal(0.0, v["post_spin_frac"], n)
            elif variant == "spin_only":
                m_i, a_i = m_hat, a_hat
                s_i = s_t * rng.lognormal(0.0, v["post_spin_frac"], n)
            else:
                m_i = m_t * rng.lognormal(0.0, post_mass_frac, n)
                a_i = a_t * rng.lognormal(0.0, v["post_area_frac"], n)
                s_i = s_t * rng.lognormal(0.0, v["post_spin_frac"], n)
            p_inf = risk_score(f_hat, a_i, m_i) / removal_cost_musd(
                cfg, m_i, L, s_i, sma, c_dt)
            inf10 = top_k(p_inf, v["top_k"])
            new = inf10 - base10
            flips[d] = len(new)
            for j in new:
                enter_counts[j] += 1
            p_true = risk_score(f_t, a_t, m_t) / removal_cost_musd(
                cfg, m_t, L, s_t, sma, c_dt)
            v_base, v_inf = sum(p_true[list(base10)]), sum(p_true[list(inf10)])
            regret_gain[d] = (v_inf - v_base) / v_base
        return {"P_flips_ge_2": float(np.mean(flips >= 2)),
                "mean_flips": float(np.mean(flips)),
                "mean_value_gain_pct": float(100 * np.mean(regret_gain)),
                "_flips": flips, "_gain": regret_gain, "_enters": enter_counts,
                "_base10": base10}

    pub = lambda r: {k: vv for k, vv in r.items() if not k.startswith("_")}
    branches, keep = {}, None
    for c_dt in v["detumble_branches_musd_per_kNms"]:
        primary = experiment(c_dt, v["post_mass_frac"])
        null = experiment(c_dt, v["post_mass_frac"], variant="null")
        spin = experiment(c_dt, v["post_mass_frac"], variant="spin_only")
        sens = experiment(c_dt, v["post_mass_frac_sens"])
        branches[f"detumble_{c_dt}"] = {
            "primary": pub(primary),
            "null_control_zero_information": pub(null),
            "spin_only_true": pub(spin),
            "sensitivity_post_mass_30pct": pub(sens),
            "evidential_weight": {
                "P_flips_ge_2_minus_null": round(
                    primary["P_flips_ge_2"] - null["P_flips_ge_2"], 4),
                "value_gain_pct_minus_null": round(
                    primary["mean_value_gain_pct"] - null["mean_value_gain_pct"], 3)},
        }
        if keep is None:
            keep = primary

    flips, gain = keep["_flips"], keep["_gain"]
    enters, base10 = keep["_enters"], keep["_base10"]
    frac2 = float(np.mean(flips >= 2))
    summary = {
        "population": pop_label,
        "n_objects": int(n), "n_draws": int(v["n_draws"]),
        "prior_model": "v2 CORRECTED: class common-mode + idiosyncratic (see config)",
        "gate1_threshold": "P(flips>=2) >= 0.20 required, else dossier product dead",
        "gate1_letter_verdict": "PASS (does not trip)" if frac2 >= 0.20
                                else "FAIL (trips: dossier product dead)",
        "gate1_evidential_note": ("the pasted metric must be read against the "
                                  "null control: evidential weight is "
                                  "P_primary - P_null and gain - gain_null"),
        "branches": branches,
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))
    pd.DataFrame({"draw": np.arange(v["n_draws"]), "flips": flips,
                  "value_gain": gain}).to_csv(OUT / "flips.csv", index=False)
    movers = sel[["norad", "name", "family", "alt_km", "inc_deg", "mass_kg"]].copy()
    movers["enter_top10_freq"] = enters / v["n_draws"]
    movers["in_baseline_top10"] = [i in base10 for i in range(n)]
    movers.sort_values("enter_top10_freq", ascending=False).to_csv(
        OUT / "movers.csv", index=False)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(flips, bins=np.arange(-0.5, flips.max() + 1.5), color="#4477aa")
    ax.axvline(2, color="#cc3311", ls="--", label="gate: 2 flips")
    ax.set_xlabel("objects entering informed top-10 (per draw)")
    ax.set_ylabel(f"draws (of {v['n_draws']})")
    ax.set_title(f"Gate 1 v2: P(flips>=2) = {frac2:.3f} (first branch)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "flips_hist.png", dpi=120)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
