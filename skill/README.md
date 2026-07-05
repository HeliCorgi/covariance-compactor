# `falsifying-concepts` — a Claude Agent Skill for killing weak ideas early

This folder is a self-contained **[Claude Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)**
distilled from the falsification campaign in this repository. It is published as
an appendix so others can install and reuse the *method*, not just read the
worked example.

## What it's for

Use it to **decide, cheaply and early, whether a big idea is worth pursuing** —
before you sink months of work or real money into it. It turns "I have a gut
feeling this won't work" into a **disciplined, falsifiable, adversarially-checked
verdict** you can act on and defend to others.

Good moments to reach for it:
- "Should we spend the next quarter building X?"
- "Is this startup / product / research thesis actually viable, or does it just
  sound good?"
- "This architecture choice is hard to reverse — is it justified?"
- "Someone is attached to a bold hypothesis. Is it real, or is it surviving on a
  flattering metric?"

It is deliberately **biased toward killing**. Most big ideas that will fail can
be killed with one cheap, well-chosen test — if you have the discipline to run it
honestly instead of accumulating evidence for what you already want to believe.

**Not for** small, cheap, or reversible decisions (just make them), or ideas
already validated by prior work.

## Why a skill (and not just a prompt)

The hard part of killing your own idea isn't intelligence — it's *discipline*.
Four failure modes recur, and this skill encodes guards against each (with real
examples in `references/meta-lessons.md`):

1. **A metric that can't fail** — a "signal" a coin flip would also pass. → every
   metric is checked against a zero-information null control.
2. **Value measured against "nothing"** — instead of against the cheapest thing
   that already works. → counterfactual discipline.
3. **Moving the goalposts** — quietly relaxing a threshold once the data is in. →
   pre-registration: metric, threshold, and null are frozen *before* evidence.
4. **A confident-but-wrong model** — one that silently excludes the obvious
   option. → an independent adversarial review must try to flip every verdict
   before it's final.

In the campaign that produced this skill, **both** initial gate verdicts were
wrong and flipped under adversarial review. That's the point: the method catches
the mistakes a smart, motivated analyst makes by default.

## The method in one breath

**pre-register** (metric + kill threshold + null + counterfactual, frozen) →
**null-control** every metric → measure value as the **marginal over the cheapest
existing alternative** → run the **cheapest kill-test on real data** → **adversarial
review** flips-or-confirms → **verdict**: gate trips → write the negative report
and stop; all gates survive → report the earned value with every caveat.

Two modes:
- **quick-kill (default)** — attack the single riskiest assumption with 1–2 cheap
  tests + a null control + one adversarial pass. Hours, not weeks.
- **full-campaign** — 4–8 pre-registered gates with executed studies and
  per-finding review, for high-stakes, hard-to-reverse decisions.

## Install

The skill follows the Agent Skills open standard, so it works across Claude
surfaces.

**Claude Code** (recommended)
```bash
# personal — available in all your projects:
cp -r skill ~/.claude/skills/falsifying-concepts
# or project-scoped — just this repo:
# cp -r skill .claude/skills/falsifying-concepts
```
Then invoke it with `/falsifying-concepts`, or just describe a big decision and
Claude will offer it. If `~/.claude/skills/` did not exist before, restart Claude
Code once so it registers.

**claude.ai** — enable Skills (Settings → Features / Capabilities, with the code
execution tool), then upload this folder as a custom Skill.

**Claude Developer Platform / Agent SDK** — upload the skill and reference it via
the code execution tool. See the official docs:
https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

## Try the bundled scripts (standard library only)

```bash
python skill/scripts/null_control.py    # shows a "changed 92% of the time" metric
                                        # that a zero-info baseline ALSO passes
                                        # (i.e. proves nothing) vs the real signal
python skill/scripts/verdict_table.py   # renders a gate verdict table + kill call
```

## What's inside

```
SKILL.md                              the method, when-to-use, verdict logic (the entrypoint)
references/prereg-template.md          fill-in pre-registration (metric/threshold/null/counterfactual)
references/gate-verdict-table.md       verdict table + negative-result report format
references/adversarial-review-rubric.md what the skeptic attacks; reviewer output format
references/evidence-labeling.md         measured / assumption / external_validation_required; anti-fabrication
references/meta-lessons.md              the recurring self-deception failure modes, with examples
scripts/null_control.py                 is a metric evidential, or would a coin flip pass it?
scripts/verdict_table.py                render the gate verdict table from a small JSON/YAML file
```

## Worked example

This repository *is* the worked example: a real, pre-registered, adversarially-
reviewed campaign that ended in a defensible **kill** of an orbital-debris
concept. Read `../STEP3_RESULTS.md` (§6: 13 dispositioned review defects) and
`../RESULTS.md` (§9: the two reversed verdicts) to see the disciplines catching
real mistakes.

## License

MIT (see `../LICENSE`). Reuse, adapt, and share it freely.
