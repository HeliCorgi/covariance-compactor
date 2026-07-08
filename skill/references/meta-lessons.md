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

## 8. "Structurally doomed" is not "doomed on your timeline"
A real structural flaw does not tell you *when* it bites. A survival artist with
no near-term forcing event (no imminent debt maturity, a cash runway, a
finite-but-unexhausted dilution or bailout engine) can defer the reckoning for
years — and your dated kill thesis can be right about the disease and wrong about
the date.
- *Example (live call, 2026):* a pre-registered "distress by end-2027" thesis on
  AMC Entertainment was **refuted for that window** by the evidence — the
  near-term maturities had already been refinanced out to 2029, 2028 was clean,
  and box office was recovering — even though the structural thesis (cash interest
  > EBITDA, survival only via value-destructive dilution, attendance structurally
  below pre-COVID) was sound. The binding event is the 2029 maturity wall, not
  2027. See `../examples/predictions-ledger.md` (entry 001).
- *Guard:* pre-register the **timing** against the actual forcing events (the debt
  maturity ladder, the cash runway, the subsidy expiry date), not a vibe. Separate
  two verdicts explicitly: *is the structure broken?* and *is there a forcing event
  inside the horizon?* A broken structure with no near-term trigger is "survives
  the window, re-date the thesis," not a kill.

## 9. Specify *whose* death — enterprise vs equity
"Will it die?" is ambiguous until you say *which* death: a Chapter 11 / insolvency
of the **enterprise**, or a permanent wipe of the **common equity** (via dilution
or a distressed take-under). A dilution- or bailout-financed survivor can keep the
enterprise alive for years while destroying its shareholders.
- *Examples (2026 live calls):* AMC and Plug Power both look far more likely to
  **wipe their equity** (relentless dilution — AMC's share count; Plug's authorized
  shares doubled to 3.0B) than to file Chapter 11 in the window; scoring "bankruptcy"
  alone would miss the real, higher-probability outcome. GoPro instead faces acute
  **enterprise** distress (going concern, ~1-quarter cash, a live sale process).
- *Guard:* pre-register the outcome variable explicitly — enterprise insolvency,
  equity wipe (>90% permanent loss), delisting, or distressed sale — and give a
  **separate probability for each**. A company can "survive" and still be a correct
  kill *on the equity*. Also verify the assumed trigger actually happened: Plug's
  45V subsidy did **not** get repealed (it survived, window-compressed), so a
  "subsidy is cut" kill leg must be checked against current policy, not assumed.

## 10. Date the tail, and read the counterparty's direction
A **real** structural single-point-of-failure (customer / supplier / platform
concentration) is not automatically a *near-term* one. Separate the 3-year
probability from the 10-year probability, and weigh the most recent signal from
the critical counterparty: are they **deepening** the relationship (new contracts,
investment, co-development) or quietly building the capability to **exit**?
- *Example (2026 live call):* Cirrus Logic's ~91%-of-revenue dependence on Apple is
  a genuine existential concentration, and Apple has a proven in-sourcing playbook —
  yet in 2026 Apple was *deepening* it (a ~$400M investment through 2030,
  co-developing next-gen Face ID silicon), and the latest teardown still showed
  Cirrus parts. That pushes the existential in-sourcing risk mostly **beyond** the
  3-year window (~6–10%) into a fatter 5–10-year tail — so the honest call is
  "survives the window, monitor the counterparty," not a near-term kill. First-pass
  15–25% was too high once the tail was dated and the counter-signal weighed.
- *Guard:* for a concentration/dependency thesis, pre-register the horizon
  explicitly, give separate near- and long-tail probabilities, and update on the
  counterparty's *direction*, not just the static concentration number.

## 11. Check the metric's definition; a de-rating is not a wipe
Two adjacent traps that a distress thesis routinely conflates:
- **Adjusted / go-forward ≠ realized GAAP.** A "we're profitable now" headline is
  often *adjusted* (excludes stock comp, one-offs) and *projected* ("on a 12-month
  go-forward basis"), not a realized GAAP quarter. Verify which. *Example:*
  Opendoor's "adjusted EBITDA positive on a go-forward basis" sat on top of a Q1
  GAAP net loss of −$173M and excluded ~$120M/quarter of SBC.
- **A big drawdown is not a kill.** A permanent equity *de-rating* (say −50% to
  −80% from an inflated level) is a different outcome from an equity *wipe*
  (>90%). *Example:* Opendoor's real bear case is a de-rating (coin-flip-to-likely)
  — but the corporate entity runs net cash with non-recourse debt, so an actual
  wipe/insolvency is ~15–20%. Scoring "kill" would mislabel a likely de-rating as a
  low-probability wipe.
- *Guard:* pin the exact metric definition (adjusted vs GAAP, realized vs
  projected), and pre-register the *magnitude* of the outcome you mean (insolvency
  / >90% wipe / a specific % drawdown), not a vague "distress."

## 12. Turn the method on itself — a tool's value is marginal over its *true* null
The most reflexive trap: over-claiming the value of the falsification method
itself, using exactly the fallacies (#1 and #3) it exists to catch. On 2026-07-09
this skill was quick-killed on itself; two of its own claims did not survive and
were narrowed.
- **"The disciplines/lessons beat baseline Claude" — confounded (a #1 trap on the
  tool).** The headline evidence — *"all 6 first-pass probabilities moved under
  the deep-dive"* — does not isolate skill-vs-prompt: the first-pass *and* the
  deep-dive were both produced by the same agent, same day, **both with the
  skill**. It shows *thorough research beats a gut read*, not *the skill beats a
  good prompt*. A competent one-off skeptical prompt also says "deep-dive, don't
  trust your first impression," so the **zero-information null moves the
  probabilities too** — the metric is vacuous for the claim under test. The tool's
  TRUE null is *a good skeptical prompt*, not *no method*. Marginal value survives
  only where it is **prompt-irreducible**: runnable deterministic scripts, a fixed
  cross-session cause-code/label enum (a fresh prompt has no memory of prior
  sessions' vocabulary), longitudinal tracking scaffolding (.ics / CI / scheduled
  agent), and **checklist recall** of low-frequency high-impact checks (a capable
  model *knows* each item but doesn't reliably *retrieve* all of them under load).
  Not the prose disciplines a capable model already has.
- **"The predictions ledger is a calibration instrument" — unearned (a #1 trap on
  the ledger).** With `n_resolved = 0`, every calibration statistic is undefined
  and the ledger is **identical to a random-probability null** (Brier over 0 pairs
  = 0/0). Even fully resolved, the design tops out at ~6 calls with ~4 sharing one
  rate/capital-cycle factor, so the 95% CI on the hit-rate spans **chance to
  perfection** — it can never reject "uninformative" on its own. "Calibration" was
  carrying weight the evidence cannot bear; the honest label is a **pre-registered,
  dated, falsifiable prediction log that is calibration-READY**, not a calibration
  measurement. Executed proof: `../scripts/calibration_power.py`.
- *Guard:* measure a method's value as the marginal over its **cheapest real
  alternative** (a good one-off prompt — its true null), not over "nothing"; when
  the claim matters, run the actual A/B (skill vs good-prompt on the same idea,
  blind-graded by a third agent) and report *skill-minus-prompt*. Never call a
  tiny / unresolved / correlated / self-graded prediction set "calibration."
  **Freeze the original (date, event, probability) triple** so that re-dating (#8)
  and enterprise-vs-equity splits (#9) cannot silently become unfalsifiability
  escape hatches. Score Brier only on exogenous binary events, and only once enough
  **independent, fast-resolving** calls exist to make the number mean something.
  Downgrade "compounding asset" to *aspirational until an outcome resolves from the
  world* — same-day distillation is not the resolved-outcome→banked-lesson loop.
- *Update (the A/B this lesson demanded was run, 2026-07-09):* on a blind, 8-item
  A/B, the loaded skill did **not** beat a strong inline prompt built from its own
  disciplines on one-shot pre-mortem quality — it **won only 1 of 8** (D = −0.54,
  sign test p≈0.02; CI grazes 0). The disciplines work (the winning prompt *is*
  them); the file-bundle's real advantage is the prompt-irreducible axes, not
  one-shot prose. Two consequences: ship the disciplines as a tight paste-ready
  prompt for one-shot use ([`../references/one-shot-prompt.md`](../references/one-shot-prompt.md)),
  and the loss surfaced **#13**. See [`../examples/ab-test-2026-07-results.md`](../examples/ab-test-2026-07-results.md).

## 13. Lock the load-bearing number against the primary source before you theorize
A pre-mortem's verdict usually turns on **one** quantity — the debt maturity
ladder, the cash runway, the contribution margin. Build the thesis first and pull
that number loosely (from memory, a secondary source, or a half-read filing) and a
confident, well-reasoned analysis can rest on a fact that is simply wrong —
everything downstream inherits the error, and the reasoning *looks* rigorous.
- *Example (A/B self-test, 2026-07-09):* the skill arm reached the right verdicts
  but lost 6 of 8 items almost entirely by mis-stating the load-bearing capital
  structure while theorizing — a **~23× overstatement** of Snap's Aug-2026 maturity
  (~$1.06B claimed vs **$47M** actual) plus an omitted **$1.5B 2033 tranche**; Beyond
  Meat's term loans dropped; **~$1B of Hims 2030 converts missed on the very 8-K it
  cited**; a fabricated "$60 peak" labelled `measured, web-verified`. It spent
  **~1.5× the tokens** and was still less accurate — the failure was
  theorize-before-verify, not research-less. See
  [`../examples/ab-test-2026-07-results.md`](../examples/ab-test-2026-07-results.md).
- *Guard:* **first**, pull the single decision-driving quantity directly from the
  primary source (the actual 10-K / 10-Q / dataset), **reconcile it** (does the
  maturity ladder sum to the stated total? does the balance sheet show debt you
  didn't list?), and label it `measured` **only** once verified against that primary
  doc — **then** build the thesis. A number that decides the verdict must be locked
  *before* the argument, not sourced *during* it.
