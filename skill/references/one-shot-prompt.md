# The one-shot prompt (paste-ready)

In a blind A/B ([`../examples/ab-test-2026-07-results.md`](../examples/ab-test-2026-07-results.md)),
a tight inline prompt encoding these disciplines **beat the full multi-file skill**
on one-shot analysis quality — at ~⅔ the cost. So for a **single** falsification /
pre-mortem, paste the prompt below instead of loading the whole skill. Reserve the
full skill for what a prompt cannot give: the executable scripts, the cross-session
scoring taxonomy, the tracking scaffolding, accumulated meta-lessons, and
zero-friction recall (see [`README.md`](../README.md) "why not just a prompt").

---

## Copy from here

> You are a rigorous, skeptical analyst running a **pre-mortem / falsification** of
> the following idea or thesis: **[STATE THE IDEA / COMPANY / HYPOTHESIS]**.
>
> **1 — Lock the load-bearing number first.** Identify the *single* quantity the
> verdict turns on (e.g. the debt maturity ladder / cash runway / unit-contribution
> margin / the key rate). Pull it **directly from the primary source** (the actual
> filing / dataset / paper), **reconcile it** (does it sum to the stated total? is
> there something on the balance sheet you didn't list?), and treat it as fact only
> once verified against that primary doc. Do this **before** you build any argument.
>
> **2 — Pre-register, before gathering the rest of the evidence:** the single
> **load-bearing assumption** whose failure kills the thesis; the **metric +
> threshold** that would confirm or refute distress; and a **null / counterfactual**
> (what a zero-information or base-rate view would say).
>
> **3 — Then research** current primary evidence and apply these disciplines:
> - **Null-control** your key metric — would it also "fire" with zero real
>   information? If a coin flip passes it, it measures nothing.
> - Judge severity **vs the cheapest alternative explanation**, not vs nothing.
> - Keep **one coherent scenario per number** — never mix a bull fact and a bear
>   fact to double-count.
> - Specify **whose** death — enterprise insolvency vs a >90% equity wipe vs a mere
>   de-rating — and give **separate probabilities** for each.
> - Pin the **timing** to actual forcing events (debt maturities, cash runway,
>   subsidy / regulatory dates), not a vibe. A broken structure with no near-term
>   trigger "survives the window; re-date the thesis."
> - Distinguish **adjusted / non-GAAP / go-forward** figures from realized GAAP.
> - Engage the **strongest** form of the bear case, not a strawman.
>
> **4 — Adversarially review your own verdict:** actively try to refute it before
> finalizing. A "survives / refuted" verdict is fine and is **preferred** over a
> forced dramatic call.
>
> **5 — Report:** verdict; the load-bearing assumption; your honest probability
> (with whose-death); the timing / forcing event; the decisive weakness (or the
> reason it's refuted); the null-control / counterfactual; and the key evidence with
> its source. Label each number `measured` (verified against a primary source),
> `assumption`, or `needs external validation`.

## To here

---

**When to use which.** One-shot prompt → a single pre-mortem, fastest and (per the
A/B) at least as good. Full skill → you need the deterministic scripts
(`../scripts/`), a portfolio scored with the fixed cause-code/label taxonomy, the
anti-zombie review scaffolding, the accumulating meta-lessons, or you want it to
trigger without re-deriving this prompt each time.
