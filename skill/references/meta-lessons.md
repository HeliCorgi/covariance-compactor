# Meta-lessons — the failure modes this skill exists to catch

These are the recurring ways a falsification campaign fools itself. Each was hit
in the worked example (a real 4-step campaign that ended in a defensible kill:
https://github.com/HeliCorgi/covariance-compactor). Check for all of them.

## 1. The metric that cannot fail
A metric that a **zero-information baseline also passes** measures nothing.
- *Example:* a "ranking-flip" metric read as 99.9% positive — but a null
  instrument (posterior = prior + noise, zero real information) reproduced it,
  because the ranking was a degenerate near-tie that flips under any noise.
- *Guard:* null-control every metric (`scripts/null_control.py`); report
  metric-minus-null. If you cannot describe a plausible world where the metric
  fails, redesign it before gathering evidence.

## 2. The structurally-wrong model
A model that quietly **excludes the cheapest valid strategy** (or has a sign bug)
gives a confident wrong verdict.
- *Example:* a feasibility model reported FAIL because all three formulations
  excluded a free, physically-valid option and double-charged a cost; an
  adversarial reviewer's hand-built counter-example flipped it to PASS.
- *Guard:* adversarial review must include "is there a strategy the model
  structurally cannot represent?" Cross-check against an external benchmark.

## 3. Value priced "vs nothing"
Benefit measured against no-knowledge instead of the **cheapest existing
alternative** inflates the case.
- *Example:* the value of a flight sensor collapsed once you subtracted what
  ground instruments and the mission's own mandatory approach phase already
  deliver for far less.
- *Guard:* counterfactual discipline — list free/cheaper/already-done
  alternatives and subtract them; do not credit the system for what it would
  learn anyway.

## 4. World-mixing
Pricing benefits in one world and costs in another produces an incoherent number.
- *Example:* a value bracket scaled benefits by a hypothetical funded pipeline
  while zeroing option-value using the *opposite* fact (that pipeline is
  unfunded). The same fact was used in both directions.
- *Guard:* single-world coherence — one consistent assumption set per calculation.

## 5. Post-hoc constraint that eases the kill (or the pass)
Adding a constraint after seeing evidence, in a way that moves the verdict, is
goalpost-moving — even when it moves toward the "right" answer.
- *Example:* the decisive kill rested on a joint-defensibility constraint that
  was not in the pre-registered formula; the honest fix was to disclose all
  readings side-by-side, not to quietly bake the constraint in.
- *Guard:* freeze thresholds; the reviewer checks for drift in either direction;
  disclose alternative readings rather than picking the flattering one.

## 6. Options priced on things that do not exist
Assigning value to a capability only useful for missions/customers/markets that
are not funded, reachable, or real.
- *Guard:* existence check — every option's precondition must actually exist
  (funded, reachable, legally permitted); otherwise price it at zero in the
  decision-relevant world and disclose the hypothetical separately.

## 7. The pre-evidence coherence check (the summary lesson)
Twice in the worked example a pre-registered metric needed repair *at review
time* — a metric that could not fail, and options priced on nonexistent missions.
Both were catchable before spending anything.
- *Guard:* before gathering evidence, run a **single-world coherence check** and
  an **independent metric review** on every pre-registered metric. Cheapest
  possible insurance against a wasted campaign.
