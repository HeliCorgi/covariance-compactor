"""calibration_power.py -- the null control, EXECUTED (not just described).

The skill's own discipline (meta-lesson #1) says: null-control every metric with
a real number, and if a zero-information baseline also passes it, the metric is
vacuous. This script applies that test to the skill's OWN "the predictions ledger
is a calibration instrument" claim.

Two questions, both answered by executed numbers:

  Q1 (now): with n_resolved = 0, can any calibration statistic distinguish the
     real ledger from a ledger of random probabilities?
  Q2 (best case, fully resolved): even if all 6 calls resolve AND the informed
     probabilities are perfectly calibrated, can this 6-entry design reject the
     random null (Brier of a coin flip) with any confidence?

Deterministic: fixed seed, numpy only. ASCII output (cp932-safe console).

Run:  python calibration_power.py
"""

import numpy as np

SEED = 20260705  # repo-standard seed (see REPRODUCING.md)

# The six deep-dive headline probabilities, for the primary scored binary event
# per entry (the FROZEN original call -- e.g. AMC = P(distress by end-2027), the
# call to be scored, not its re-dated 2029 successor). Midpoints of the ranges.
LEDGER = {
    "AMC  (distress by end-2027)":            0.175,
    "LCID (equity wipe/take-under <=2yr)":     0.500,
    "GPRO (distress/sale/delist <=18mo)":      0.875,
    "PLUG (equity-wiping dilution <=2yr)":     0.500,
    "CRUS (Apple in-sourcing shock <=3yr)":    0.080,
    "OPEN (>90% equity wipe <=2-3yr)":         0.175,
}
P = np.array(list(LEDGER.values()))
N = len(P)

# Correlation structure the skeptic flagged: AMC/LCID/PLUG/OPEN (indices 0,1,3,5)
# share ONE rate/capital-cycle latent factor; GPRO and CRUS are idiosyncratic.
CLUSTER = [0, 1, 3, 5]
IDIO = [2, 4]


def brier(probs, outcomes):
    return float(np.mean((probs - outcomes) ** 2))


def draw_independent(rng, probs, trials):
    u = rng.random((trials, len(probs)))
    return (u < probs).astype(float)


def draw_correlated(rng, probs, trials):
    """4 of 6 outcomes driven by one shared macro path; 2 idiosyncratic."""
    out = np.zeros((trials, len(probs)))
    macro = rng.random((trials, 1))               # one shared uniform per world
    idio_noise = rng.random((trials, len(probs)))
    for j in range(len(probs)):
        if j in CLUSTER:
            # blend the shared macro draw with a little idiosyncratic noise
            u = 0.8 * macro[:, 0] + 0.2 * idio_noise[:, j]
        else:
            u = idio_noise[:, j]
        out[:, j] = (u < probs[j]).astype(float)
    return out


def main():
    print("=" * 70)
    print("NULL CONTROL, EXECUTED: is the predictions ledger a calibration")
    print("instrument?  (applying meta-lesson #1 to the skill itself)")
    print("=" * 70)
    print(f"seed={SEED}   n_entries={N}")
    print()

    # ---- Q1: right now (n_resolved = 0) --------------------------------------
    n_resolved = 0
    print("-" * 70)
    print("Q1  NOW  (n_resolved = 0)")
    print("-" * 70)
    print(f"  resolved (probability, outcome) pairs available : {n_resolved}")
    print("  Brier score over 0 pairs                        : UNDEFINED (0/0)")
    print("  reliability curve over 0 pairs                  : EMPTY")
    print("  => the real ledger and a RANDOM-probability ledger produce")
    print("     IDENTICAL calibration output (nothing). Indistinguishable.")
    print("  VERDICT: 'calibration instrument' is vacuous today.")
    print()

    # ---- Q2: analytic CI at full resolution ----------------------------------
    print("-" * 70)
    print("Q2  BEST CASE  (all 6 resolved, informed probs perfectly calibrated)")
    print("-" * 70)
    phat = 0.7  # an illustrative observed hit-rate
    for n in (N, 3):  # nominal n=6, and effective independent n~3 (correlation)
        se = np.sqrt(phat * (1 - phat) / n)
        lo, hi = max(0.0, phat - 1.96 * se), min(1.0, phat + 1.96 * se)
        tag = "nominal" if n == N else "effective (4/6 correlated)"
        print(f"  n={n} ({tag}): observed hit-rate {phat:.2f} "
              f"+/- SE {se:.3f} -> 95% CI [{lo:.2f}, {hi:.2f}]")
    print("  Both CIs CONTAIN the random null (0.50) AND perfection (1.00):")
    print("  the instrument cannot reject 'uninformative' on its own. EVER,")
    print("  at this sample size.")
    print()

    # ---- Q2b: Monte-Carlo power vs the coin-flip null ------------------------
    print("-" * 70)
    print("Q2b MONTE CARLO  power to beat the null Brier (coin flip = 0.25)")
    print("-" * 70)
    rng = np.random.default_rng(SEED)
    trials = 200_000
    null_probs = np.full(N, 0.5)  # zero-information ledger

    for label, draw in (("independent outcomes", draw_independent),
                        ("correlated (4/6 share macro)", draw_correlated)):
        truth = draw(rng, P, trials)  # assume LEDGER is the true DGP (best case)
        b_informed = np.mean((P - truth) ** 2, axis=1)
        b_null = np.mean((null_probs - truth) ** 2, axis=1)
        beats = float(np.mean(b_informed < b_null))
        mean_gain = float(np.mean(b_null - b_informed))
        print(f"  [{label}]")
        print(f"    P(informed Brier < null Brier) : {beats:.3f}  "
              f"(1.00 would be certainty; 0.50 is a toss-up)")
        print(f"    mean Brier advantage over null : {mean_gain:+.4f}")
    print()
    print("  Even granting the ledger the BEST possible case (its own probs are")
    print("  the true data-generating process), at n=6 a single realized world")
    print("  frequently fails to separate the ledger from a coin flip. One")
    print("  realized draw -- which is all we will ever get -- is not a")
    print("  calibration measurement.")
    print()
    print("=" * 70)
    print("CONCLUSION: the ledger is a pre-registered, dated, falsifiable")
    print("prediction log (real, valuable) and is calibration-READY, but it is")
    print("NOT a calibration MEASUREMENT and this 6-entry design cannot become")
    print("one. Relabel accordingly.")
    print("=" * 70)


if __name__ == "__main__":
    main()
