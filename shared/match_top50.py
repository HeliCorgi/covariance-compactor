"""Match the published McKnight 2021 top-50 table to current catalog objects.

The published table (reproduced verbatim in Abdul-Hamid et al., arXiv:2510.07708
Table A1, from McKnight et al. Acta Astronautica 181 (2021)) gives
rank/name/apogee/perigee/inclination/mass but NO NORAD IDs. We match each row
to a real cataloged object by family/name token + orbit proximity
(|dinc| <= 0.7 deg, |dalt| <= 35 km, greedy 1-to-1 on closest orbit).
Within the SL-16 cluster objects are near-identical, so identity assignment
among same-family near-ties is approximate — documented, and irrelevant to the
Study-2 experiment, which treats same-family objects as exchangeable.

Usage: python -m shared.match_top50 <path-to-top50.json>
"""
import json
import pathlib
import shutil
import sys

import numpy as np
import pandas as pd

from shared import astro, population as pop

ROOT = pathlib.Path(__file__).resolve().parents[1]

TOKEN_TO_FAMILY = {
    "SL-16 R/B": "SL-16", "SL-8 R/B": "SL-8", "SL-12 R/B(2)": "SL-12",
    "SL-3 R/B": "SL-3", "CZ-2D R/B": "CZ-2", "CZ-2C R/B": "CZ-2",
    "CZ-4C R/B": "CZ-4", "CZ-4B R/B": "CZ-4", "CZ-4 R/B": "CZ-4",
    "CZ-6A R/B": "CZ-6", "H-2A R/B": "H-2A", "H-2 R/B": "H-2",
    "H-1 R/B": "H-1", "ARIANE 5 R/B": "ARIANE", "ENVISAT": "ENVISAT",
}


def build_all_with_gp(cfg):
    """Like build_derelicts but WITHOUT the R/B type filter (top-50 includes
    payloads)."""
    gp, sc = pop.load_gp(), pop.load_satcat()
    df = gp.join(sc[["OBJECT_TYPE", "OWNER", "DECAY_DATE", "RCS"]],
                 on="NORAD_CAT_ID")
    df = df[df["DECAY_DATE"].isna()].copy()
    df["a_km"] = astro.sma_from_mean_motion(df["MEAN_MOTION"])
    df["alt_km"] = df["a_km"] - astro.RE
    df["family"] = df["OBJECT_NAME"].map(pop.classify_family)
    df.loc[(df["family"] == "OTHER") & (df["OBJECT_TYPE"] == "PAY"),
           "family"] = "PAY"
    fam = cfg["families"]
    for col, key in (("mass_kg", "mass_kg"), ("length_m", "length_m"),
                     ("diam_m", "diam_m")):
        df[col] = df["family"].map(lambda k: fam[k][key]).astype(float)
    df["area_m2"] = astro.mean_projected_area_cylinder(df["length_m"], df["diam_m"])
    return df.reset_index(drop=True)


def main(top50_json: str):
    cfg = pop.load_config()
    src = pathlib.Path(top50_json)
    dest = ROOT / "data" / "raw" / "top50_mcknight.json"
    if not dest.exists():
        shutil.copy(src, dest)
    doc = json.loads(dest.read_text(encoding="utf-8"))
    rows = [o for o in doc["objects"]
            if "2021 Acta Astronautica" in o["name"] and o.get("apogee_km")]
    cat = build_all_with_gp(cfg)
    used, out = set(), []
    # match well-constrained (rarest) tokens first: sort by pool size
    ALIASES = {"ADEOS 2": "ADEOS-II", "METEOR 3M": "METEOR-3M"}

    def pool_for(token):
        if token in TOKEN_TO_FAMILY:
            return cat[cat["family"] == TOKEN_TO_FAMILY[token]]
        pat = ALIASES.get(token, token).upper()
        return cat[cat["OBJECT_NAME"].str.upper().str.contains(pat, na=False, regex=False)]

    parsed = []
    for o in rows:
        token = o["name"].split(" — ")[0].strip()
        alt = 0.5 * (o["apogee_km"] + o["perigee_km"])
        parsed.append((token, alt, o))
    parsed.sort(key=lambda x: len(pool_for(x[0])))

    for token, alt_l, o in parsed:
        cand = pool_for(token)
        cand = cand[~cand["NORAD_CAT_ID"].isin(used)]
        if len(cand) == 0:
            out.append({"rank": o["rank"], "list_name": token, "norad": None})
            continue
        dinc = (cand["INCLINATION"] - o["inc_deg"]).abs()
        dalt = (cand["alt_km"] - alt_l).abs()
        score = dalt + 50.0 * dinc
        feas = (dinc <= 0.7) & (dalt <= 35.0)
        if not feas.any():
            out.append({"rank": o["rank"], "list_name": token, "norad": None})
            continue
        best = cand[feas].loc[score[feas].idxmin()]
        used.add(int(best["NORAD_CAT_ID"]))
        out.append({
            "rank": o["rank"], "list_name": token,
            "norad": int(best["NORAD_CAT_ID"]), "name": best["OBJECT_NAME"],
            "family": best["family"], "owner": best["OWNER"],
            "mass_pub_kg": o.get("mass_kg"),
            "a_km": float(best["a_km"]), "alt_km": float(best["alt_km"]),
            "inc_deg": float(best["INCLINATION"]),
            "raan_deg": float(best["RA_OF_ASC_NODE"]),
            "ecc": float(best["ECCENTRICITY"]),
            "length_m": float(best["length_m"]), "diam_m": float(best["diam_m"]),
            "area_m2": float(best["area_m2"]),
            "dalt_km": float(abs(best["alt_km"] - alt_l)),
            "dinc_deg": float(abs(best["INCLINATION"] - o["inc_deg"]))})
    res = pd.DataFrame(out).sort_values("rank")
    dst = ROOT / "data" / "processed" / "top50_match.csv"
    dst.parent.mkdir(parents=True, exist_ok=True)
    res.to_csv(dst, index=False)
    ok = res["norad"].notna()
    print(f"matched {ok.sum()}/{len(res)}; median |dalt|="
          f"{res.loc[ok,'dalt_km'].median():.1f} km, median |dinc|="
          f"{res.loc[ok,'dinc_deg'].median():.3f} deg")
    print(res[~ok][["rank", "list_name"]].to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1])
