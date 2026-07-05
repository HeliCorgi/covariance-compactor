"""Load the real derelict population: Celestrak GP elements x SATCAT metadata.

Object identities, orbits, owners, and object types are measured (fetched
catalog data). Masses and dimensions are CLASS-LEVEL config values labeled
assumption — never object-specific fabrications.
"""
import pathlib

import numpy as np
import pandas as pd
import yaml

from shared import astro

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

FAMILY_KEYS = [
    "SL-16", "SL-8", "SL-12", "SL-14", "SL-3", "CZ-2", "CZ-3", "CZ-4",
    "CZ-6", "DELTA", "TITAN", "AGENA", "THORAD", "ATLAS", "SCOUT", "ARIANE",
    "H-2A", "H-2", "H-1", "ENVISAT",
]


def load_config():
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def classify_family(name: str) -> str:
    up = str(name).upper()
    if "THORAD" in up:
        return "THORAD"  # before AGENA: 'THORAD AGENA D R/B'
    for key in FAMILY_KEYS:
        if key in up:
            return key
    return "OTHER"


def load_gp() -> pd.DataFrame:
    frames = [pd.read_csv(p) for p in sorted(RAW.glob("gp_*.csv")) if p.stat().st_size > 100]
    gp = pd.concat(frames, ignore_index=True)
    gp["EPOCH"] = pd.to_datetime(gp["EPOCH"])
    gp = gp.sort_values("EPOCH").drop_duplicates("NORAD_CAT_ID", keep="last")
    return gp


def load_satcat() -> pd.DataFrame:
    sc = pd.read_csv(RAW / "satcat.csv", low_memory=False)
    return sc.set_index("NORAD_CAT_ID")


def build_derelicts(cfg=None) -> pd.DataFrame:
    """Rocket bodies (plus Envisat) currently on orbit with GP elements."""
    cfg = cfg or load_config()
    gp, sc = load_gp(), load_satcat()
    df = gp.join(sc[["OBJECT_TYPE", "OWNER", "DECAY_DATE", "RCS", "LAUNCH_DATE"]],
                 on="NORAD_CAT_ID")
    is_rb = df["OBJECT_TYPE"] == "R/B"
    is_envisat = df["OBJECT_NAME"].str.upper().str.contains("ENVISAT", na=False) \
        & (df["OBJECT_TYPE"] == "PAY")
    df = df[(is_rb | is_envisat) & df["DECAY_DATE"].isna()].copy()

    df["a_km"] = astro.sma_from_mean_motion(df["MEAN_MOTION"])
    df["alt_km"] = df["a_km"] - astro.RE
    df["family"] = df["OBJECT_NAME"].map(classify_family)

    fam = cfg["families"]
    df["mass_kg"] = df["family"].map(lambda k: fam[k]["mass_kg"]).astype(float)
    df["length_m"] = df["family"].map(lambda k: fam[k]["length_m"]).astype(float)
    df["diam_m"] = df["family"].map(lambda k: fam[k]["diam_m"]).astype(float)
    df["area_m2"] = astro.mean_projected_area_cylinder(df["length_m"], df["diam_m"])

    keep = ["NORAD_CAT_ID", "OBJECT_NAME", "family", "OWNER", "RCS", "LAUNCH_DATE",
            "a_km", "alt_km", "INCLINATION", "RA_OF_ASC_NODE", "ECCENTRICITY",
            "mass_kg", "length_m", "diam_m", "area_m2", "EPOCH"]
    out = df[keep].rename(columns={
        "NORAD_CAT_ID": "norad", "OBJECT_NAME": "name", "OWNER": "owner",
        "INCLINATION": "inc_deg", "RA_OF_ASC_NODE": "raan_deg",
        "ECCENTRICITY": "ecc"}).reset_index(drop=True)
    return out


def band_filter(df: pd.DataFrame, cfg=None) -> pd.DataFrame:
    cfg = cfg or load_config()
    lo, hi = cfg["band"]["alt_min_km"], cfg["band"]["alt_max_km"]
    return df[(df["alt_km"] >= lo) & (df["alt_km"] <= hi)].copy()


def catalog_spatial_density(shell_km: float = 20.0) -> pd.DataFrame:
    """Spatial density [objects/km^3] per altitude shell from ALL on-orbit
    cataloged objects (SATCAT PERIOD->sma). Measured from fetched data."""
    sc = pd.read_csv(RAW / "satcat.csv", low_memory=False)
    sc = sc[sc["DECAY_DATE"].isna() & (sc["ORBIT_CENTER"] == "EA")]
    sc = sc.dropna(subset=["PERIOD"])
    rev_day = 1440.0 / sc["PERIOD"]
    a = astro.sma_from_mean_motion(rev_day)
    alt = a - astro.RE
    alt = alt[(alt > 200) & (alt < 2500)]
    edges = np.arange(200.0, 2500.0 + shell_km, shell_km)
    counts, _ = np.histogram(alt, bins=edges)
    r_lo, r_hi = astro.RE + edges[:-1], astro.RE + edges[1:]
    vol = 4.0 / 3.0 * np.pi * (r_hi**3 - r_lo**3)  # km^3
    return pd.DataFrame({"alt_lo": edges[:-1], "alt_hi": edges[1:],
                         "count": counts, "density_km3": counts / vol})


def flux_at_alt(alt_km, density_table: pd.DataFrame, vrel_km_s: float):
    """Kinetic-theory flux [1/m^2/yr]: rho * v_rel. rho in km^-3 -> m^-3."""
    idx = np.clip(np.searchsorted(density_table["alt_lo"].values,
                                  np.asarray(alt_km)) - 1, 0,
                  len(density_table) - 1)
    rho_km3 = density_table["density_km3"].values[idx]
    rho_m3 = rho_km3 * 1e-9
    seconds_yr = 86400.0 * 365.25
    return rho_m3 * (vrel_km_s * 1e3) * seconds_yr
