# Evidence labeling and anti-fabrication

Every number and claim carries a label so a reader (and the adversarial
reviewer) knows how much weight it bears. Two orthogonal label sets:

## Value provenance
- **measured** — produced by executed code / analysis in this campaign. Cite the
  command and (if stochastic) the seed. A number is *not* measured unless code
  actually produced it.
- **assumption** — a stated engineering/business assumption with no verified
  source. Give the value and a one-line rationale; the reviewer will attack it.
- **external_validation_required** — a fact carried from elsewhere that has not
  been independently verified here (e.g. inherited from a prior report). Must be
  confirmed before it can bear real weight.

## Source basis (for external facts)
- **web-verified** — a real URL that was fetched and content-checked. Record the
  URL and retrieval date.
- **training-data** — recalled without fetching. Treat as low confidence; flag
  for verification.
- **not-found** — looked for, could not confirm. Say so explicitly rather than
  inventing.

## Hard rules
1. **No fabricated metrics.** Never report a number as a result unless executed
   code, a labeled assumption, or a fetched source produced it.
2. **No fabricated citations.** Never invent a URL, DOI, identifier, or dataset
   row. If unverifiable, mark not-found.
3. **Real object identities only.** Never invent the properties of specific
   named entities (people, objects, records); use real data or clearly-labeled
   synthetic data, and mark verdicts on synthetic data PROVISIONAL.
4. **Cache and cite.** Save fetched sources with URL + retrieval date so results
   are reproducible and the provenance survives if a file is later excluded.
5. **Determinism.** Fix a master seed for any stochastic study and record it, so
   reruns reproduce the reported numbers.
