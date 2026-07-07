# Live predictions ledger

A register of **live, dated, falsifiable** predictions made with the
`falsifying-concepts` skill. Each entry freezes a thesis, a probability, and
dated kill/survive criteria *before* the outcome is known, then records the
resolution and the lesson. This is the skill's own **eval set**: when an entry
resolves — right or wrong — the lesson is folded into
[`../references/meta-lessons.md`](../references/meta-lessons.md).

**Disclaimer.** Methodology demonstration, **not investment advice**. Everything
is public information, labeled and sourced. Predictions are probabilistic and
often wrong; the point is calibration and learning, not stock tips. Nothing here
is a recommendation to buy, sell, or hold any security.

**How to read a verdict.** The skill reports the verdict the evidence supports —
including "the thesis is refuted" — never a forced dramatic call. A structurally
weak company with no near-term forcing event is scored **survives-the-window**,
with the thesis re-dated, not killed.

**Scoring.** Every entry carries fixed fields (resolution date, review triggers,
a pre-declared label, a cause code, and a consensus-at-call snapshot) per
[`../references/scoring-taxonomy.md`](../references/scoring-taxonomy.md). Labels:
**killed / wounded / survived / inconclusive / too-early**. The point is **speed +
calibration, not hit-rate**: did we find the load-bearing weakness before the
market — and did the 70%s happen ~70% of the time?

## Scoring summary (interim labels as of 2026-07-08)

| # | Co. | Resolution horizon | Key review triggers | Current label | Primary cause code | Edge vs consensus |
|---|---|---|---|---|---|---|
| 001 | AMC | 2029 wall (equity: rolling) | each 10-Q; the 2029 refi | **wounded** (FCF−, diluting) | `capital-structure/dilution-death` (2ry `timing-wrong`) | re-dated the crunch to 2029 vs a 2027 death narrative |
| 002 | LCID | ~mid-2028 | each quarter; any PIF take-private | **wounded** | `capital-structure/dilution-death` (2ry `backer-or-customer-dependency`) | flagged take-under as the dominant mode, not bankruptcy |
| 003 | GPRO | ~2027-06 | 2026-12; Sept-2026 covenant test; sale-process outcome | **wounded** (kill-outcomes partly realized) | `one-time-purchase-decay` (2ry `bad-unit-economics`) | mostly consensus now (going concern public); structural read was early |
| 004 | PLUG | ~2028 | each quarter; 45V/2028 window; DOE-loan decision | **wounded** | `subsidy-or-regulatory` (2ry `capital-structure/dilution-death`) | equity-death framing vs the market's bankruptcy-binary |
| 005 | CRUS | 3yr (2029) + 5–10yr tail | each iPhone teardown; any Apple audio-insourcing signal | **survived-so-far** | `incumbent-wins` (tail only) | correctly *down*-rated a scary concentration (avoided a false positive) |
| 006 | OPEN | ~2028 | each quarter; a housing/rate down-cycle | **too-early** (no deep-dive yet) | `bad-unit-economics` (2ry `timing-wrong`) | TBD |

*Labels are interim checkpoints, not resolutions — none has reached its horizon.
Update the label + a next date at every review; record the outcome and the
realized lead time when each resolves.*

---

## Entry 001 — AMC Entertainment (AMC) — pre-registered 2026-07-08

**Surface ("seems safe"):** the largest US cinema chain, a "meme stock" that has
repeatedly survived near-death by issuing dilutive equity — it looks like it
*can't* die because it keeps not dying.

**Pre-registered thesis (frozen 2026-07-08):** distress (Chapter 11 or an
equity-wiping restructuring) **by end-2027**, if all of: FCF-negative through
2026 **and** a 2026/2027 maturity unrefinanced on non-distressed terms **and**
box office stuck below ~$9.5B **and** dilution capacity exhausted.

**Evidence (Q1 2026 10-Q + current, web-verified):**
- Debt ~**$4.02B** principal; net debt ~$3.64B. **Maturity ladder: 2026 $14.9M,
  2027 $545M, 2028 $0, 2029 $3,172M (the wall), 2030 $267M.**
  [SEC 10-Q, amc-20260331]
- **Near-term walls already refinanced:** a July 2025 "transformative" refinancing
  redeemed all 2026 maturities out to 2029; a new $425M Odeon term loan pushed the
  2027 Odeon notes to 2031; June 2026 equity is redeeming the 2027 subordinated
  notes. [investor.amctheatres.com]
- **FCF-negative:** Q1 2026 operating cash flow −$128.5M, FCF −$174.7M; FY2025 net
  loss −$632.4M despite +$387.5M Adjusted EBITDA. **Cash interest ~$480M/yr now
  EXCEEDS EBITDA (~$388M).** [StockTitan 10-Q]
- **Dilution engine still running but value-destructive:** shares ~433M (Mar 2025)
  → ~605M (Mar 2026) → ~850–900M (mid-2026); authorized raised to **1.1B**.
  Liquidity ~$381M (Mar 2026) + ~$350M fresh mid-2026 equity. [SEC 424B5]
- **Box office recovering, but structurally sub-2019:** 2025 ~$8.87B; 2026 YTD
  $4.88B (Jul 7), full-year projected ~$9.9B (best post-COVID) — yet admissions
  ~780M vs 2019's ~1.2B (**−37%**); AMC's own 10-Q says burn is "not sustainable
  long-term" and needs "pre-COVID-19 levels" (~$11.4B). [Box Office Mojo; Comscore]

**Adversarial review verdict: the kill does NOT survive for the end-2027 window.**
Only ~$545M matures before 2029, 2028 is clean, box office is recovering, and Q1
2026 Adjusted EBITDA turned positive (+$38M, best Q1 since 2019). Two of the four
pre-registered kill conditions fail: near maturities *were* refinanced, and box
office is projected *above* the $9.5B line.

**VERDICT (honest): pre-registered end-2027 KILL is REFUTED.**
- P(Chapter 11 / equity-wipe **by end-2027**): **~15–20% — UNLIKELY.** AMC very
  likely survives the window.
- **The structural thesis is validated but re-dated.** Interest > EBITDA,
  survival only via finite value-destructive dilution, and dependence on a
  pre-COVID box office that is not returning — these bite at the **2029 refinancing
  of the ~$3.17B wall at ~10%**, not in 2027.

**Re-dated live thesis (new falsifiable call):** materially elevated distress risk
**concentrated in 2028–2029**, contingent on (a) the 2029 wall being refinanced
only on distressed terms or not at all, (b) domestic box office staying below
~$11B, and (c) FCF remaining negative. A calibrated 2029 probability will be set
on review closer to the date (AMC's refinancing track record keeps even the 2029
outcome genuinely uncertain).

**Review dates:** 2027-01-31 (interim), 2028-07-01 (pre-2029-wall). **Status:
ACTIVE.** **Outcome:** TBD.

**Lesson already banked (meta-lessons #8):** "structurally doomed" ≠ "doomed on
your timeline." Pre-register the *timing* against the actual forcing events (the
maturity ladder), and separate "is the structure broken?" from "is there a
forcing event inside the horizon?" The skill did its job here by refuting a
dramatic-but-mis-timed near-term death call.

---

## Batch — Entries 002–006 (pre-registered 2026-07-08)

One live call per archetype (AMC = archetype 2 above), non-overlapping,
deliberately mixing directions and horizons. **Probabilities are first-pass**,
set from verified current data but *before* a full AMC-style adversarial
deep-dive — which can move them materially (entry 001 shows a first impression
getting refuted). Each is falsifiable with a review date. Not advice.

### Entry 002 — Lucid Group (LCID) — archetype 1 (sovereign-backer burn)
- **Direction:** KILL-leaning (PIF-contingent) · **Horizon:** medium (1–2yr)
- **Seems safe:** a "bottomless" Saudi PIF majority owner, ~$3.2B liquidity, a
  fresh ~$1.05B round (incl. Uber's $300M robotaxi deal), the Gravity SUV.
- **Load-bearing assumption:** PIF keeps writing multi-billion checks **and**
  Lucid reaches positive gross margin before that appetite fades.
- **Structural read:** 2025 net loss $2.7B, cash burn ~$3.8B/yr; **Q1 2026 gross
  margin ≈ −110%** (cost of revenue > 2× revenue); ~3,000 deliveries/quarter;
  18% layoffs. [SEC Q1FY26 8-K; Motley Fool 2026-07-01]
- **Kill if:** PIF funding slows/stops while gross margin stays deeply negative →
  equity wipe or distressed take-private. **Survive if:** PIF keeps funding AND
  Gravity drives gross margin positive.
- **First-pass P(equity-wipe / distressed take-private within ~2yr): ~35–45%.**
- **DEEP-DIVE VERDICT (2026-07-08): SPLIT (a #9 case) — enterprise survives, the
  equity is the risk.** PIF support is **confirmed, not waning**: an April 2026
  $550M Series C preferred within a ~$1.05B raise, the PIF delayed-draw term loan
  raised $500M to ~$2.5B, and a June 2026 fresh PIF + Uber round (~$750M) plus a
  ~$800M Saudi credit draw → pro-forma liquidity ~$4.7B, guided "into H2 2027". No
  near-term debt wall (2026 converts repurchased with new notes due 2031; the DDTL
  is a captive PIF lender). So **P(hard bankruptcy within ~2yr) ~10–15% (UNLIKELY).**
  But unit economics are catastrophic and worsening (Q1 2026 gross margin **−110%**,
  cost of revenue >2× revenue; ~$1.4B/quarter FCF burn; deliveries ~3–4k/quarter,
  2026 guidance **suspended**; shareholders' equity collapsed **$3.87B → $717M**),
  and a **PIF take-private is live chatter** (Apr 2026; mcap ~$2.3B ≈ ¼ of PIF's
  ~$9.5B sunk). So **P(equity wiped OR taken under at a distressed price within
  ~2yr) ~50% (coin-flip, downside-tilted)** — dominant mode a **low-ball PIF
  take-private (~30–35%).** Enterprise ~85% survives; the common equity is the
  thing at risk. First-pass (~35–45%) refined up to ~50% and reframed as a #9 split.
  [Q1 2026 results; PIF injections (AGBI/IR); take-private reporting]
  **Review:** 2027-01, 2027-07. **Alternate:** VinFast (VFS), going-concern-flagged,
  ~−53% gross margin.

### Entry 003 — GoPro (GPRO) — archetype 3 (one-time-purchase decay)
- **Direction:** KILL-leaning · **Horizon:** short (<1yr) *(fast-feedback pick)*
- **Seems safe:** iconic brand, 2.36M paying subscribers (looks like sticky SaaS).
- **Load-bearing assumption:** the subscription/services layer (or a new category,
  or a rescue buyer) scales fast enough to offset a structurally shrinking
  one-time hardware business before liquidity runs out.
- **Structural read:** Q1 2026 revenue $99.1M **−26% YoY**; hardware $72.2M (from
  $107.4M, **−33%**); subscription **flat** at $26.9M; net loss; **board running a
  strategic review** (a distress/sale signal). [10-Q filed 2026-05-11]
- **Kill if:** distressed sale, delisting, or restructuring within ~12–18 months.
  **Survive if:** services/new category stabilize revenue and restore positive FCF
  independently.
- **First-pass P(distress / forced sale / delisting within ~18mo): ~45–60%.**
- **DEEP-DIVE VERDICT (2026-07-08): KILL — confirmed, revised UP to ~85–90%.**
  Near-term forcing events are real and several are already partly realized:
  an auditor **going-concern** opinion (Q1 2026 10-Q, reiterated June 2026);
  **~$40.7M cash ≈ one quarter of runway** (revolver fully drawn); a **covenant
  breach** (asset-coverage 1.05x) waived May 2026 with management **expecting
  future non-compliance** and **cross-default** across all facilities (all debt
  reclassified current); a **live Houlihan Lokey sale process** (open, no deal);
  stock **~$0.75, sub-$1** with renewed Nasdaq delisting risk; hardware −33% while
  subscription is **flat and subscribers −8%**. The first-pass was **too low** —
  the acute near-term triggers moved it up. Most likely resolution: a **distressed
  sale** (rescues assets, minimizes/wipes common equity) or restructuring/
  delisting. Status: **ACTIVE**, several kill-outcomes already partly realized.
  **Review:** 2026-12, 2027-06.

### Entry 004 — Plug Power (PLUG) — archetype 4 (subsidy-dependent)
- **Direction:** KILL-leaning · **Horizon:** short–medium
- **Seems safe:** $802M total cash, revenue +22% YoY, gross margin improving
  (−55% → −13%), a $1.7B DOE loan.
- **Load-bearing assumption:** the Section 45V clean-hydrogen credit (plus 45X/ITC)
  persists **and** Plug places enough capacity in service before the 2028 window
  while raising dilutive capital to bridge ~$150M/quarter burn.
- **Structural read:** Q1 2026 net loss $245.3M; green hydrogen (~$4–6/kg) is
  uneconomic vs grey without 45V; chronic dilution; prior going-concern history.
  [10-Q 2026-05-11]
- **Kill if:** the subsidy is cut/expires or capacity misses the window **and**
  dilution capacity exhausts → distress within ~2yr. **Survive if:** 45V locked +
  capacity in service + margin to positive + financing holds.
- **First-pass P(severe distress / dilution-to-oblivion within ~2yr): ~40–55%.**
- **DEEP-DIVE VERDICT (2026-07-08): SPLIT by definition of "death".** The subsidy
  did NOT get cut — **45V survived** the July 2025 OBBBA law (not repealed), but
  the begin-construction window was compressed to **before 2028**; Plug's three
  operating plants qualify, while its DOE-backed expansion is **suspended** (Nov
  2025 clean-energy pause) and at risk of missing the window. **No near-term debt
  wall** (convertibles due **2033**). Cash **$223M unrestricted + $184M restricted**
  (releasing ~$50M/qtr) vs **~$150M/quarter burn**; authorized shares **doubled to
  3.0B** (Feb 2026) = large remaining dilution runway. So:
  **P(hard insolvency / Ch 11 within ~2yr) ~20–25% (UNLIKELY)**, but
  **P(equity-wiping severe dilution within ~2yr) ~50% (coin-flip-to-likely)** —
  the survival path itself funds 6–8 quarters of burn with equity at a ~$2–3 stock,
  inflicting 30–60%+ dilution on top of the +40% already suffered. **The company
  likely survives; the common equity is the thing at risk** (see meta-lesson #9).
  **Review:** 2027-01, 2027-07. **Alternate:** Sunrun (RUN), ITC-dependent,
  negative cash generation despite GAAP profit.

### Entry 005 — Cirrus Logic (CRUS) — archetype 5 (single-customer) — SURVIVE-call
- **Direction:** SURVIVE (base case) with a **named catastrophic tail** ·
  **Horizon:** long (2–3yr+)
- **Seems safe:** profitable compounder, net cash, active buybacks, rising iPhone
  content — *and it genuinely is healthy today.*
- **Load-bearing assumption:** Apple keeps **outsourcing** its audio/mixed-signal
  silicon to Cirrus rather than in-sourcing it.
- **Structural fragility:** **Apple ≈ 91% of FY2026 net sales, and rising**
  (87% → 89% → 91%); Apple has a proven playbook of in-sourcing suppliers
  (modems, etc.). [FY2026 10-K, ~2026-05-21]
- **The call:** base case **survives and compounds**; the single point of failure
  is an Apple in-sourcing decision, which would existentially threaten ~90% of
  revenue. **First-pass P(existential revenue shock from Apple in-sourcing within
  ~3yr): ~15–25%** (low base rate, high impact). This is the ledger's
  both-directions entry: the value is naming the one thing to monitor, not a death
  call.
- **DEEP-DIVE VERDICT (2026-07-08): SURVIVE-call CONFIRMED; 3-year tail revised
  DOWN to ~6–10%.** The dependency is real and rising (Apple **~91%** of FY2026
  sales, ~94% in peak quarters; a design-out would be existential, and Apple has a
  proven in-sourcing playbook — Intel modem → C1, Dialog PMIC). But there is **no
  near-term catalyst**: the iPhone 17 teardown (Sept 2025) still shows Cirrus audio
  codec + amps, and — decisively — **Apple is DEEPENING the relationship**: a
  ~$400M investment in Cirrus through 2030 and co-development of next-gen
  mixed-signal silicon incl. next-gen Face ID (~$2 ASP, ~$180M potential); content
  per iPhone is rising; Cirrus is diversifying (PC/laptop targeting ~10%; HPMS —
  camera controllers, haptics, battery via Lion Semiconductor). So **P(existential
  >50% revenue loss from Apple in-sourcing within ~3yr) ~6–10%** — first-pass
  (15–25%) was **too high** for the 3-year horizon; the real risk is a **fatter
  5–10-year tail** (~2032–33). Honest call: **survives the window; monitor the
  counterparty's direction** (meta-lesson #10). [FY2026 10-K; iFixit teardown;
  Apple $400M / Face ID reporting]
  **Review:** 2027-06, 2028-06.

### Entry 006 — Opendoor Technologies (OPEN) — archetype 6 (negative unit economics)
- **Direction:** coin-flip · **Horizon:** medium (1–2yr)
- **Seems safe:** a 2025–26 meme rally and a charismatic ex-Shopify CEO declaring
  the "fatal flaw" fixed and the company "adjusted-EBITDA profitable on a
  go-forward basis."
- **Load-bearing assumption:** home prices stay flat-to-rising and rate/spread
  conditions stay benign long enough for the thin gross spread to cover holding +
  financing + opex.
- **Structural read:** Q1 2026 revenue $720M **−37% YoY**; gross margin 10.0% but
  **contribution margin just 4.4%**; adjusted EBITDA **−$31M**; GAAP net loss
  −$173M; rate/housing-sensitive inventory risk (the 2022 failure mode). [Q1 2026
  results]
- **Kill if:** a housing/rate down-cycle craters the thin spread → inventory
  write-downs + liquidity crunch within ~2–3yr. **Survive if:** durable positive
  contribution margin and adjusted-EBITDA profit *through a full cycle*.
- **First-pass P(severe distress / equity wipe within ~2–3yr): ~30–45%** — highly
  contingent on the rate/housing cycle (not company-controllable). **Review:**
  2027-01, 2027-07.

---

**Batch design note (calibration hygiene).** Directions are deliberately mixed —
AMC (survives-window/re-dated), Lucid/GoPro/Plug (kill-leaning), Cirrus
(survive + named tail), Opendoor (coin-flip) — with two short-horizon calls
(GoPro, Plug) for fast feedback. When each resolves, record the outcome here and
fold the lesson into `../references/meta-lessons.md`.

**Deep-dive calibration record (first-pass → deep-dive, 2026-07-08).** Every one
of the five deep-dived first impressions moved — which is the point of the
deep-dive + honest-probability discipline:

| Entry | First-pass | After deep-dive | Move |
|---|---|---|---|
| 001 AMC | near-term death | ~15–20% by end-2027; structure bites 2029 | **↓ refuted / re-dated** |
| 002 Lucid | ~35–45% equity | enterprise ~85% survives; equity ~50% wiped/taken-under | **split (#9)** |
| 003 GoPro | ~45–60% | ~85–90% within ~18mo | **↑ up** |
| 004 Plug | ~40–55% | insolvency ~20–25%; equity-wipe ~50% | **split (#9)** |
| 005 Cirrus | tail 15–25% (3yr) | ~6–10% (3yr); fatter 5–10yr tail | **↓ down** |

Three of five (AMC, Lucid, Plug) resolve to "**enterprise survives, equity dies**"
(meta-lesson #9). Two first-pass numbers were too high (Cirrus, and — for the
near term — AMC), one was too low (GoPro). Gut first-passes are unreliable;
date the trigger (#8), specify whose death (#9), and read the counterparty (#10).

*Add future predictions as further entries. Keep both directions represented,
state a probability, and set a review date so the ledger becomes a calibration
record.*
