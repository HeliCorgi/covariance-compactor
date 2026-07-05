"""Null-control harness: is a metric evidential, or would a coin flip pass it?

A metric only carries evidence if an INFORMED estimator beats a NULL
(zero-information) estimator on it. This harness runs both through the same
decision and scores each against the drawn truth, so you can see the
*evidential* gain (informed minus null) rather than a raw number that a
degenerate problem inflates for everyone.

Adapt the four callables to your problem, or run as-is for the built-in demo,
which reproduces the campaign's Gate-1 lesson: a "selection changed" rate can be
~100% for BOTH informed and null (so it proves nothing), while the value gain is
positive only for the informed estimator.

Usage:
    python scripts/null_control.py            # built-in ranking-flip demo
    # or import run_null_control(...) and pass your own callables.

Only depends on the standard library.
"""
from __future__ import annotations

import statistics
from typing import Callable


def run_null_control(
    draw_truth: Callable,
    informed_estimate: Callable,
    null_estimate: Callable,
    decision: Callable,
    value_of: Callable,
    n: int = 2000,
    seed: int = 0,
) -> dict:
    """Compare an informed vs a zero-information decision against the truth.

    draw_truth(rng)            -> a 'truth' object for one Monte Carlo draw.
    informed_estimate(truth,rng) -> estimate that DOES use information about truth.
    null_estimate(rng)         -> estimate that uses NO information about truth
                                   (must not read `truth`).
    decision(estimate)         -> the action/choice made from an estimate.
    value_of(decision, truth)  -> the realized value of that decision under truth.

    Returns means, the evidential gain (informed - null), and how often the two
    decisions differ. If evidential_gain is ~0, the metric is vacuous.
    """
    import random

    rng = random.Random(seed)
    v_inf, v_null, differ = [], [], 0
    for _ in range(n):
        truth = draw_truth(rng)
        d_inf = decision(informed_estimate(truth, rng))
        d_null = decision(null_estimate(rng))
        v_inf.append(value_of(d_inf, truth))
        v_null.append(value_of(d_null, truth))
        if d_inf != d_null:
            differ += 1
    mi, mn = statistics.fmean(v_inf), statistics.fmean(v_null)
    return {
        "n": n,
        "value_informed_mean": mi,
        "value_null_mean": mn,
        "evidential_gain": mi - mn,
        "p_decisions_differ": differ / n,
        "verdict": ("VACUOUS - null matches informed; metric proves nothing"
                    if abs(mi - mn) <= 1e-9 or mi - mn < 0.02 * (abs(mn) + 1e-9)
                    else "EVIDENTIAL - informed beats the zero-information baseline"),
    }


def _demo() -> None:
    """Ranking-flip demo: pick the single best of K near-identical items.

    Truth: K item values, nearly tied (a degenerate ranking). Informed estimate
    sees a noisy-but-real signal about the truth; null sees only prior noise.
    A 'the pick changed vs prior-best' rate is high for both (degeneracy), but
    only the informed pick captures above-baseline true value.
    """
    K = 12

    def draw_truth(rng):
        # near-tied true values around 1.0 (a degenerate near-tie set)
        return [1.0 + 0.02 * rng.gauss(0, 1) for _ in range(K)]

    def informed(truth, rng):
        # real information: truth plus modest observation noise
        return [t + 0.01 * rng.gauss(0, 1) for t in truth]

    def null(rng):
        # zero information about truth: prior point (all equal) plus noise
        return [1.0 + 0.02 * rng.gauss(0, 1) for _ in range(K)]

    def decision(estimate):
        return max(range(len(estimate)), key=lambda i: estimate[i])  # argmax

    def value_of(pick, truth):
        # value captured relative to the average item (baseline = pick at random)
        return truth[pick] - statistics.fmean(truth)

    res = run_null_control(draw_truth, informed, null, decision, value_of,
                           n=4000, seed=20260705)
    print("Null-control demo (ranking flip on a near-tie set)")
    print(f"  value gain, informed decision : {res['value_informed_mean']:+.4f}")
    print(f"  value gain, null decision     : {res['value_null_mean']:+.4f}")
    print(f"  EVIDENTIAL GAIN (inf - null)  : {res['evidential_gain']:+.4f}")
    print(f"  P(pick differs from prior)    : {res['p_decisions_differ']:.3f}  "
          f"<- high for BOTH; a raw 'it changed' metric is vacuous here")
    print(f"  verdict: {res['verdict']}")


if __name__ == "__main__":
    _demo()
