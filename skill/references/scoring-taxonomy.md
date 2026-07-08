# Scoring taxonomy — how predictions resolve

Every live prediction is scored with **fixed fields set before the outcome**, so
the portfolio can be cross-analyzed and — *once enough independent calls resolve* —
eventually calibrated, instead of rotting into zombies. Four rules.

> **Calibration is a goal, not a present property.** Fixed fields make a set of
> predictions calibration-*ready*; they do not make any small, unresolved, or
> heavily correlated set a calibration *measurement*. See meta-lesson #12 and
> `../scripts/calibration_power.py`.

## 1. Fixed judgment dates (no zombies)

Each prediction carries, from the moment it is made:
- **Resolution horizon** — a date by which *killed* or *survived* should be clear.
- **Review checkpoints** — both **calendar** (e.g., +30d, +90d, +1yr) **and
  event-triggered**: next earnings, next capital raise / dilution, a debt
  maturity, a subsidy/regulatory decision, a strategic-review outcome.

At every checkpoint you **must** assign a label below — even `too-early` — so a
prediction is never left dangling. *A prediction with no next date is a bug.*

## 2. Resolution labels (pre-decided)

- **killed** — the predicted death occurred. Say which (meta-lesson #9):
  *enterprise* (Chapter 11 / insolvency) or *equity* (>90% permanent loss — wipe,
  distressed take-under, or delisting / forced sale).
- **wounded** — materially impaired toward the thesis (going concern, covenant
  breach, heavy dilution, restructuring, an active distressed-sale process) but
  not a full kill yet. On track.
- **survived** — the thesis is refuted for the window: financed / refinanced /
  healthy, the load-bearing assumption held.
- **inconclusive** — the checkpoint arrived but the evidence is genuinely
  ambiguous; re-date with a reason.
- **too-early** — the resolution horizon is not reached; keep ACTIVE, nothing else.

## 3. Cause codes (fixed enum — one primary, optional secondary)

Fixed so failure modes can be cross-tabbed across many predictions:

- `no-demand` — the market doesn't want it at scale.
- `bad-unit-economics` — per-unit / contribution economics structurally negative.
- `one-time-purchase-decay` — no recurring engine; a saturating one-time TAM.
- `incumbent-wins` — an entrenched player, or the key counterparty, captures or
  **in-sources** it.
- `backer-or-customer-dependency` — survival hinges on ONE backer / customer /
  supplier who can withdraw (single point of failure).
- `subsidy-or-regulatory` — economics hinge on a subsidy or regulation that shifts.
- `capital-structure / dilution-death` — the enterprise survives but the equity is
  destroyed by dilution or a take-under (meta-lesson #9).
- `value-not-realizable` — the asset / information isn't worth the claim (no
  willingness-to-pay, no counterfactual edge).
- `ops-too-hard` — execution / technical / logistics infeasibility.
- `timing-wrong` — right structural thesis, wrong window (meta-lesson #8).

## 4. Score speed, not just accuracy (the edge principle)

The value of this method is **finding the load-bearing weakness before the market
prices it** — not being "right" after everyone already knows. So:

- Record a **consensus-at-call snapshot** when the prediction is made (price,
  analyst posture, the prevailing narrative) so lead time is measurable later.
- The **edge** is: did we name the *specific* failure mode, the *timing*, or the
  *whose-death* earlier or more precisely than consensus? A correct **survived**
  call — refuting a scary-looking thesis and avoiding a false positive — is also
  edge.
- At the portfolio level, prize **lead time to the market** and **resolution**
  (naming the specific failure mode / timing / whose-death) over raw hit-rate.
  Death is a rare event, so hit-rate alone is nearly uninformative. True
  **calibration** (do the 70%s happen ~70% of the time) is the eventual prize, but
  it needs *many more independent, faster-resolving* calls than a handful of
  correlated distress bets — score Brier only on exogenous binary events, and only
  when the sample can actually support it (meta-lesson #12). Until then, the asset
  is a fast, cause-coded, pre-registered record — calibration-ready, not calibrated.
