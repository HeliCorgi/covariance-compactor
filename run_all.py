"""Regenerate the full campaign in order. See README.md for details.

Phases 3-4 (conjunction Monte Carlo, taggability census) were not built in
this pass (see RESULTS.md sections 1 and 9); run_all reproduces everything
that was actually executed.
"""
import subprocess
import sys

STEPS = [
    [sys.executable, "shared/fetch_data.py"],
    [sys.executable, "-m", "shared.match_top50", "data/raw/top50_mcknight.json"],
    [sys.executable, "-m", "study2_voi.run"],
    [sys.executable, "-m", "study1_tour.run"],
    [sys.executable, "-m", "study1_tour.sensitivity"],
]

for step in STEPS:
    print("==>", " ".join(step))
    subprocess.run(step, check=True)
