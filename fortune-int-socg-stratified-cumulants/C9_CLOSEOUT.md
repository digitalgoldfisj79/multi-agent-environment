# C9 — closeout

## Required validation

1. `scripts/verify_programme.py` passes from a fresh clone.
2. All exact rational regressions pass.
3. Parent occupancy-dual and integer-mainline verifiers pass.
4. Any new Lean module passes targeted build before import.
5. Full `lake build FortuneFormal` passes in a clean room.
6. Claim matrix, exponent ledger and gate statuses agree.
7. Every programme compute job is completed or cancelled.
8. Unrelated jobs are inspected and left untouched.

## Required terminal record

- exact final status from the preregistered set;
- smallest surviving theorem;
- explicit implication to eventual Fortune;
- exact obstructions for every closed lane;
- hashes, job IDs and failure counts;
- explicit non-claims.

The programme does not close merely because a method appears difficult.