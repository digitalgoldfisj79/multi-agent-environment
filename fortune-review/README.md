# fortune-review

End-to-end review of the Fortune's-conjecture paper sequence (Papers I–VI, E. S. A.
Bozzard, 2026) and proposed new proof mechanisms.

- `REVIEW.md` — full technical review: paper-by-paper assessment, 30-check independent
  verification (all pass), load-bearing analysis of the open targets, honest barrier
  assessment.
- `MECHANISMS.md` — seven proposed mechanisms (M1–M7) with first steps, risks, and a
  prioritised roadmap. Headline: the skew-Frobenius dynamical reframing of the
  function-field crown (M1) and the p-adic slope route (M3); one mechanism (M2′) was
  proposed, census-tested, and refuted during the review itself.
- `scripts/` — self-contained Python (numpy only):
  - `verify_identities.py` — re-verifies exact identities of Papers I, II, III, V.
  - `n2_census.py` — crown census: N₂(p) to p=199, cubic sectors/W_p for small p,
    integrable-map diagnostics. Usage: `python3 n2_census.py [pmax] [cubic_pmax]`.
  - `ordering_experiment.py` — is the increasing prime order extremal for the
    reciprocal frame energy? (Answer at toy scales: no — bulk-typical.)
- `data/` — captured outputs of the runs quoted in the documents.
