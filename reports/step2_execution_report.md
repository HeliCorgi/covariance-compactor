全フェーズ完了です。最終報告をまとめます。

結論を先に(日本語): コード実行環境で4研究のうち2つを実際に構築・実行し、敵対的検証を経て当初の両ゲート判定が反転・修正されました。Gate 2(ツアー実現性)はPASS(9エンカウンター/196.7 m/s/729日、実カタログで実測)、Gate 1は事前登録指標そのものが「合格しかできない」欠陥設計と判明(ヌル計測器が再現)し、修正後の真の情報価値は**+0.75%〜+5.9%**(ほぼ全てスピン測定由来)。以下が正式報告(英語)です。 

Gate-Driven Falsification Campaign — Execution Report (Phases 0–2 + adversarial verification) 
Execution mode: code execution was available. Every number below was produced by executed code in C:\Users\corgi\covariance-compactor (Python 3.11.9, pinned requirements.txt, master seed 20260705) or is explicitly labeled assumption/sourced. Inputs A and B were taken verbatim from Step 1 §8 and §5 of this conversation. 

Phase 0 — Prior-art and redundancy check (Gate 0) 
Method: 6 web-research agents (2026-07-05), every cited URL fetched and content-verified. 

Gate 0 verdicts: BUILD for all four studies (coverage: Study 1 60%, Study 2 45%, Study 3 60%, Study 4 55% — none ≥80%): 

Study 2: no published Monte-Carlo propagation of object-knowledge uncertainty through removal rankings exists. Closest: McKnight's own 2025 update (SDC9-paper4: only 20–22 of the 2020 top-50 survive to 2025, unattributed), Rusconi et al. 2025 (index-config sensitivity only), NASA OTPS Phase 2 (VoI for conjunction screening, not ranking). 
Study 1: GTOC9 corpus brackets the physics (JPL winner ~222 m/s/leg; DLR 21.7 m/s/leg time-unconstrained) but nobody has answered ≥8-real-derelicts/24-months/200 m/s. Used as external cross-checks. 
Studies 3/4: ESA DRAMA/ARES + NASA CARA cover tooling; MMT spin surveys give population splits (~25% rotator/37% slow/38% stable) and the decisive fact that all 3 observed H-2A stages are gravity-gradient stable (<0.2°/s) — but MMT excludes Russian objects. (Not built — see stop-rule note.) 
Bonus: the actual published 2021 top-50 table (rank/name/orbit/mass; NORAD IDs were never published) retrieved via its verbatim reproduction in arXiv:2510.07708, plus the 2025 interim list. Recorded in SOURCES.md. 
Data acquired (real, cached in data/raw/, provenance in SOURCES.md): Celestrak SATCAT (69,679 objects) + 33 GP name-queries → 449 rocket bodies (+Envisat) with current elements at 600–1,000 km; the top-50 orbit-matched to the current catalog 49/49 (median |Δalt| 0.8 km, |Δinc| 0.019°). 

Phase 1 — Study 2: VoI ranking-flip experiment (Gate 1) 
Commands: python -m shared.match_top50 …, python -m study2_voi.run (2,000 draws; v1 then v2). 

v1 result (superseded): P(flips≥2)=0.9995, +12.2% value gain → nominal PASS. Adversarial review found it fatally defective: (a) a zero-information null instrument reproduces the statistic (P=0.9975) — the baseline top-10 is a degenerate near-tie set (rank-10/11 margin 0.126%) that flips under any noise; (b) drawing class mass ±50% iid across ~21 identical SL-16s manufactures information (class-documentation uncertainty is common-mode; fully correlated, the gain collapses 12.2%→0.06%); (c) the "spin-only" variant silently leaked the area update (true spin-only: P=0.020). 

v2 result (corrected priors: class common-mode + per-object idiosyncratic ±5% mass/±2% area [assumption]; null control; true spin-only; both detumble-cost branches) [measured]: 

Metric	detumble 0.004 $M/kN·m·s	detumble 1.0 
P(flips≥2) primary / null	0.9985 / 0.997	0.9975 / 0.9995 
value gain vs truth, primary / null	+0.45% / −0.29%	+5.74% / −0.11% 
evidential value gain	+0.75%	+5.85% 
true spin-only gain	+0.02%	+5.75% 
Gate 1 verdict: PASS by the pasted letter (0.9985 ≥ 0.20) — but the metric is evidentially vacuous (null control passes it too; threshold not softened, defect reported). The corrected measurement brackets the dossier product's worth at +0.75%…+5.9% of top-10 campaign risk-per-dollar (~$4–30M on a $500M pipeline), with the upper end contingent on one unvalidated constant — whether spin state materially drives capture cost — and then attributable ~entirely to the spin measurement. Step 1's "±50% mass uncertainty" premise contributes ≈ nothing once treated as common-mode. 

Outputs: study2_voi/out/{summary.json, flips.csv, movers.csv, flips_hist.png}. 

The one modeling decision to review (corrected prior structure): 


def truth_draw():   # class documentation error is COMMON-MODE per family 
    cm_m = rng.uniform(0.5, 1.5, len(fam_list))[fam_idx]      # class mass 
    cm_a = rng.uniform(0.8, 1.2, len(fam_list))[fam_idx]      # class area 
    m_t = m_hat * np.where(documented,                        # payloads: own mass 
        rng.uniform(0.9, 1.1, n), 
        cm_m * rng.uniform(0.95, 1.05, n))                    # idio: resid. propellant 
    a_t = a_hat * np.where(documented, 1.0, cm_a) * rng.uniform(0.98, 1.02, n) 
    s_t = spin_med * rng.lognormal(0.0, 1.4, n)               # spin: truly per-object 

Phase 2 — Study 1: differential-J2 tour feasibility (Gate 2) 
Commands: python -m study1_tour.run, python -m study1_tour.sensitivity, python -m study1_tour.validate_schedule <norads>. 

v1 result (superseded): three formulations (fixed-offset MILP, static-gap water-filling bound, beam search) reported best feasible 5–6 @ 200 m/s → FAIL, and I engaged the stop rule. Adversarial review overturned it: all three models structurally excluded co-orbital loitering and per-leg-adaptive drift purchases, double-charged plane changes, and the beam had two bugs (leg cost omitted the Hohmann to the target's actual sma; a tie-break sign error rewarded time-wasting prefixes). Two reviewers independently hand-built 9-encounter schedules over a real ~4.3°-wide RAAN micro-window of nine SL-8 R/Bs (NORADs 11321, 8874, 21088, 7769, 25893, 9510, 10142, 24773, 22208 at 968–985 km). 

v2 result (corrected leg model, my executed code) [measured]: 

Δv budget (24 mo, rendezvous costing, 14-d dwell)	char encounters	tag encounters 
150 m/s	8	6 
200 m/s	9 (196.7 m/s, 729.2 d, SL-8 82.9° cluster)	7 
250 m/s	9	8 
Sensitivity [measured]: 36 mo → 10, 48 mo → 11 @ 200 m/s; 300 m/s → 10 @ 24 mo; beam-500 confirms 9; the top-50-relevant SL-16 cluster maxes at 5 (24 mo)/6 (36–48 mo). External consistency: corrected per-leg costs sit on the published GTOC9 time-Δv frontier. The v1 "8 needs ~700 m/s" claim is retracted. 

Gate 2 verdict: PASS (9 ≥ 8 within 200 m/s / 24 months). Caveats: the pass rides one dense SL-8 RAAN window at the current epoch (persistence under launch delay untested); impulsive transfers, no drag; the pass is carried by SL-8s, not the highest-consequence SL-16s. 

Per-object arithmetic feeding (unevaluated) Gate 6: marginal $0.52M/object (9 enc, $4.7M vehicle [assumption]); NRE-loaded $1.1–1.9M — ~8–18× under the ADRAS-J-class dedicated-inspection comparable [external_validation_required], ~2–4× under SSPICY — not Step 1's 25–50×. 

The corrected leg model (the decision that flipped the gate): 


def leg(j, k, t_now): 
    a_j, a_k = a_arr[j], a_arr[k] 
    grid = {a_j, a_k, 0.5*(a_j+a_k)}          # incl. FREE co-orbital loiter at a_j 
    for dd in (20.0, 50.0, 80.0): 
        grid |= {a_j+dd, a_j-dd, a_k+dd, a_k-dd} 
    dv_plane = 1e3*plane_change(max(a_j,a_k), inc[k]-inc[j])   # ONE plane change 
    for a_d in grid:                           # per-leg drift sma, exact rates 
        rho = raan_rate(a_d, 0, inc[j]) - rate[k] 
        tau = wrapped_angle(ang0, rho) / abs(rho) 
        dv  = 1e3*(hohmann(a_j,a_d) + hohmann(a_d,a_k)) + dv_plane + prox 

Adversarial verification (added instrument, decisive) 
Three independent skeptical review agents were tasked to refute the initial verdicts before I finalized them. All three returned fatal findings; both initial gate verdicts were wrong or hollow (Study 1 FAIL → PASS; Study 2 PASS → vacuous-with-corrected-value). Every defect, its disposition, and the retractions are logged in RESULTS.md §9. One reviewer claim was itself corrected by my validator: pure co-orbital loitering alone is not sufficient (waits of 10³–10⁶ days between same-altitude SL-8s) — the feasible schedules require purchased per-leg drift over the dense window (validate_schedule.py). 

Stop rule and campaign status 
The stop rule was engaged mid-campaign on the then-measured Gate-2 FAIL; Phases 3–4 (conjunction/red-alert Monte Carlo, taggability census) were therefore not built. After correction, neither Gate 1 (by letter) nor Gate 2 trips, so the stop rule no longer applies: Phases 3–4 are warranted and remain NOT EVALUATED (as are Gates 3–8). Say the word and I'll proceed with Phase 3. 

Honest bottom line 
The vehicle can collect the data (Gate 2 PASS, robustly — even at 150 m/s); what wobbles is what the data is worth. The campaign's own pre-registered VoI metric turned out to be unfalsifiable on this population — the corrected measurement says the characterization dossier is worth +0.75%…+5.9% of campaign risk-per-dollar, and essentially all of the upper end is the spin measurement. The two cheapest next falsifications are therefore not orbit mechanics: (1) an engineering anchor for detumble cost (does spin add >$5M/object to an ADRAS-J2-class capture?), and (2) the Gate-5 erosion study (can ground photometry deliver spin states at <$100k/object, killing the flight mission's main value channel?). 

Repository 
C:\Users\corgi\covariance-compactor — RESULTS.md (verdict table, evidence matrix, assumptions register, verification log §9), SOURCES.md (all data/literature URLs + retrieval dates), README.md (regeneration: python run_all.py), 987 lines of code across shared/, study1_tour/, study2_voi/. Studies 3–4 directories carry explicit not-built markers. 

日本語で要点: 当初「Gate 2不合格→中止」まで行きましたが、敵対的検証で私のツアーモデル3種すべてに構造的欠陥(共軌道待機の排除+2件のバグ)が見つかり、修正後は200 m/s・24ヶ月で9機=合格が私自身の実行コードで確定しました。一方Gate 1は「指標が合格しかできない設計だった」ことがヌル対照で証明され、修正後の実測価値はスピン測定にほぼ全依存(+0.75%〜+5.9%)。次の一手はシミュレーションではなく、①デタンブル費用の工学的アンカー、②地上測光によるスピン取得コスト(Gate 5)の検証です。Phase 3以降の続行指示があればすぐ着手できます。
