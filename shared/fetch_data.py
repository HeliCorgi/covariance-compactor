"""Download and cache real catalog data from Celestrak.

Writes raw files to data/raw/ and records provenance in SOURCES.md.
Idempotent: skips files that already exist (delete to re-fetch).
"""
import datetime
import pathlib
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SOURCES = ROOT / "SOURCES.md"
UA = {"User-Agent": "gate-driven-falsification-study/0.1 (research; contact via session)"}

SATCAT_URL = "https://celestrak.org/pub/satcat.csv"
GP_BASE = "https://celestrak.org/NORAD/elements/gp.php"

# Name-substring GP queries: rocket-body families relevant to the 600-1000 km
# band (Soviet/Russian, Chinese, US, Japanese, European) plus Envisat.
GP_NAME_QUERIES = [
    "SL-16", "SL-8", "SL-12", "SL-14", "SL-3",
    "CZ-2", "CZ-3", "CZ-4", "CZ-6",
    "DELTA", "TITAN", "AGENA", "THORAD", "ATLAS", "SCOUT",
    "ARIANE", "H-2", "H-1",
    "ENVISAT",
    # payloads appearing in the published McKnight top-50 tables:
    "COSMOS 2322", "COSMOS 2406", "COSMOS 2278", "COSMOS 1943",
    "COSMOS 1844", "COSMOS 2082", "COSMOS 1275", "COSMOS 2237",
    "COSMOS 2263", "ADEOS", "MIDORI", "METEOR", "SPOT", "ALOS",
    "METOP-A",
]


def fetch(url: str, dest: pathlib.Path, note: str) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        print(f"cached  {dest.name}")
        return False
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"WARN    {dest.name}: HTTP {e.code} (no data for this query)")
        return False
    dest.write_bytes(data)
    stamp = datetime.date.today().isoformat()
    with SOURCES.open("a", encoding="utf-8") as f:
        f.write(f"- `data/raw/{dest.name}` — {note} — {url} — retrieved {stamp}\n")
    print(f"fetched {dest.name} ({len(data):,} bytes)")
    return True


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    if not SOURCES.exists():
        SOURCES.write_text("# Data sources\n\n", encoding="utf-8")
    fetch(SATCAT_URL, RAW / "satcat.csv", "Celestrak SATCAT (object type, owner, status, RCS class, orbit summary)")
    for name in GP_NAME_QUERIES:
        q = urllib.parse.urlencode({"NAME": name, "FORMAT": "CSV"})
        url = f"{GP_BASE}?{q}"
        safe = name.replace("/", "_").replace(" ", "_")
        fetch(url, RAW / f"gp_{safe}.csv", f"Celestrak GP elements, NAME={name}")


if __name__ == "__main__":
    sys.exit(main())
