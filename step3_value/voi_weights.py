"""Step 3 Task 3 — per-object VoI weights (pre-registered in STEP3_PREREG.md).

w_i = E_draws[ p_true_i * 1(i in informed top-10) - p_true_i * 1(i in baseline
top-10) ], clipped at 0, normalized over the 49 matched objects. Reuses the
Study-2 v2 model verbatim (same seed 20260705, both detumble branches).

Usage: python -m step3_value.voi_weights
"""
import pathlib

import numpy as np
import pandas as pd

from shared import population as pop
from study2_voi.run import removal_cost_musd, risk_score, top_k

OUT = pathlib.Path(__file__).resolve().parent / "out"


def main():
    OUT.mkdir(exist_ok=True)
    cfg = pop.load_config()
    v = cfg["voi"]
    dens = pop.catalog_spatial_density(v["shell_km"])
    sel = pd.read_csv("data/processed/top50_match.csv")
    sel = sel[sel["norad"].notna()].reset_index(drop=True)
    sel["mass_kg"] = sel["mass_pub_kg"].fillna(sel["family"].map(
        lambda k: cfg["families"][k]["mass_kg"]))
    sel["flux_yr"] = pop.flux_at_alt(sel["alt_km"], dens, v["flux_vrel_km_s"])
    n = len(sel)
    med = v["spin_period_median_s"]
    spin_med = sel["family"].map(lambda f: med.get(f, med["default"])).values
    m_hat, a_hat = sel["mass_kg"].values, sel["area_m2"].values
    f_hat, sma, L = sel["flux_yr"].values, sel["a_km"].values, sel["length_m"].values
    families = sel["family"].values
    fam_list = sorted(set(families))
    fam_idx = np.array([fam_list.index(f) for f in families])
    documented = np.isin(families, ["PAY", "ENVISAT", "OTHER"])

    out = sel[["norad", "name", "family", "alt_km", "inc_deg", "raan_deg",
               "a_km", "ecc", "mass_kg"]].copy()
    for c_dt in v["detumble_branches_musd_per_kNms"]:
        rng = np.random.default_rng(cfg["master_seed"])   # same seed per branch
        base10 = top_k(risk_score(f_hat, a_hat, m_hat)
                       / removal_cost_musd(cfg, m_hat, L, spin_med, sma, c_dt),
                       v["top_k"])
        contrib = np.zeros(n)
        for _ in range(v["n_draws"]):
            cm_m = rng.uniform(v["prior_mass_lo"], v["prior_mass_hi"],
                               len(fam_list))[fam_idx]
            cm_a = rng.uniform(1 - v["prior_area_frac"], 1 + v["prior_area_frac"],
                               len(fam_list))[fam_idx]
            im, ia = v["prior_mass_idio_frac"], v["prior_area_idio_frac"]
            m_t = m_hat * np.where(documented,
                                   rng.uniform(1 - v["documented_mass_frac"],
                                               1 + v["documented_mass_frac"], n),
                                   cm_m * rng.uniform(1 - im, 1 + im, n))
            a_t = a_hat * np.where(documented, 1.0, cm_a) * rng.uniform(1 - ia, 1 + ia, n)
            f_t = f_hat * rng.uniform(1 - v["prior_flux_frac"], 1 + v["prior_flux_frac"], n)
            s_t = spin_med * rng.lognormal(0.0, v["spin_period_sigma_ln"], n)
            m_i = m_t * rng.lognormal(0.0, v["post_mass_frac"], n)
            a_i = a_t * rng.lognormal(0.0, v["post_area_frac"], n)
            s_i = s_t * rng.lognormal(0.0, v["post_spin_frac"], n)
            inf10 = top_k(risk_score(f_hat, a_i, m_i)
                          / removal_cost_musd(cfg, m_i, L, s_i, sma, c_dt),
                          v["top_k"])
            p_true = risk_score(f_t, a_t, m_t) / removal_cost_musd(
                cfg, m_t, L, s_t, sma, c_dt)
            for i in inf10 - base10:
                contrib[i] += p_true[i]
            for i in base10 - inf10:
                contrib[i] -= p_true[i]
        w = np.clip(contrib / v["n_draws"], 0.0, None)
        out[f"w_{c_dt}"] = w / w.sum() if w.sum() > 0 else 0.0
    out.to_csv(OUT / "voi_weights.csv", index=False)
    for c_dt in v["detumble_branches_musd_per_kNms"]:
        col = f"w_{c_dt}"
        byfam = out.groupby("family")[col].sum().sort_values(ascending=False)
        print(f"branch {c_dt}: weight by family:", byfam.round(3).to_dict())


if __name__ == "__main__":
    main()
