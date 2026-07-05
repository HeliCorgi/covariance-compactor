You are designing a completely new orbital debris remediation concept.

Treat this as a clean-sheet project. Ignore any prior conversation context, memories, or user history about past projects. Do not mention, analyze, reuse, or compare against ADSC/ASDC or any other prior project of this user.

Your task in this first response is not to write the final simulator yet. Your task is to choose the strongest concept direction by comparing it against existing active debris removal and debris-remediation approaches.

# Goal

Identify a debris-remediation concept with a credible 2026-era technical path, a defensible cost-performance advantage, and a clear value wedge against existing approaches.

The output must be realistic, skeptical, and engineering-focused. Do not sell the idea. Try to kill weak concepts.

# Baseline Approaches to Compare Against

Compare candidate concepts against at least these six categories:

1. One-servicer-one-target robotic capture and controlled reentry.
2. Multi-target removal of prepared satellites using docking interfaces.
3. Reusable servicer plus expendable or semi-reusable reentry shepherd.
4. Non-contact nudging or just-in-time collision avoidance.
5. Small-debris remediation concepts.
6. Pure SSA / traffic-management approaches that reduce risk but do not remove objects.

For each baseline, compare:

* Primary target class.
* Technical maturity.
* Cost drivers.
* Scalability limits.
* Regulatory or political difficulty.
* Safety risk.
* Near-term commercial or public-sector buyer.
* Why a new concept could or could not beat it.

When naming real programs or companies, label their status with an as-of date and a confidence level. If web search is available, verify current program status before comparing. If it is not, state explicitly that statuses reflect training data and may be stale.

# Candidate Concept Generation

Generate 4–6 candidate concepts.

Each candidate must include:

* Name.
* Core mechanism.
* Target debris class.
* Intervention type:
  * capture,
  * deorbit,
  * orbit modification,
  * collision-risk reduction,
  * passivation,
  * inspection plus risk scoring,
  * or another clearly defined mechanism.
* Required technologies.
* Main cost driver.
* Main failure mode.
* Why it may beat existing approaches.
* Why it probably fails.
* Minimum simulation needed to test the thesis.

Do not assume magical propulsion, perfect autonomy, perfect sensing, zero launch cost, unlimited onboard compute, or unconstrained legal permission.

# Value Metric

Do not default to "kg removed" unless it is genuinely the right metric.

Evaluate these possible metrics:

* cost per kg removed,
* cost per high-risk object stabilized,
* cost per expected collision avoided,
* cost per risk-reduction unit,
* annual risk-reduction capacity,
* operator willingness to pay,
* public-sector justification,
* atmospheric impact avoided,
* controlled-reentry safety value.

Choose the metric that best fits the selected concept.

# Technology Freedom

You may use any 2026-era simulation stack if justified, including plain numpy/scipy, sgp4, skyfield, astropy, scipy optimization, RL libraries, PyTorch, JAX, or simpler custom models.

Note: poliastro is archived (development ceased around 2023; hapsira is a community fork). If you propose it anyway, justify the choice and pin exact versions.

Do not ban RL. Do not force RL.

If RL is used, explain why a rule-based or optimization-based planner is insufficient. If RL is not used, explain why.

If heavyweight dependencies are used, justify them and state the reproducibility cost.

# Selection Criteria

Score each candidate from 1 to 5 on:

* technical plausibility,
* cost-performance advantage,
* scalability,
* safety,
* regulatory feasibility,
* simulation tractability,
* differentiation from existing ADR,
* evidence quality achievable in 3–6 months.

Then choose exactly one concept. If none of the candidate concepts has a credible advantage over existing approaches, say so clearly and propose a narrower, more defensible concept instead of forcing a winner.

# Required Output

Produce the following sections:

## 1. Competitive Landscape

A sober comparison of existing ADR/remediation categories.

## 2. Candidate Concepts

A table of 4–6 concepts with strengths and weaknesses.

## 3. Scoring Matrix

A scored matrix with brief justification for each score.

## 4. Selected Concept

Choose one concept and explain why it is the best available bet — or state plainly that no candidate survives the scoring, and present the narrower, more defensible fallback concept here with the same rigor.

## 5. Kill Criteria

List the conditions under which this concept should be abandoned.

## 6. Value Thesis

Explain the core economic and operational value compared to traditional ADR.

## 7. Simulation Thesis

Define what the first simulator must prove or disprove.

## 8. Final One-Paragraph Concept Brief

End with a concise concept brief, written so it can be pasted verbatim as the input to the next prompt.

Tone: ruthless, skeptical, technical. No hype.
