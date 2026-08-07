# Paper VI proof-interior audit

## Verdict

`INTERNAL_AUDIT_PASS_AFTER_LOCAL_REPAIRS_HUMAN_SPECIALIST_REQUIRED`

The assurance audit found three places where the manuscript compressed necessary arguments too aggressively. All three were locally repairable without changing any theorem statement, numerical result, or later dependency. The repaired manuscript is committed on this branch at `07df4893764cffc50b19df2a21b00c24cd44daa4`.

## Repairs made

### Theorem 9.2 — Artin--Schreier quotient

The original fibrewise phrase that `y` is a coordinate did not by itself justify the global quotient presentation. The proof now uses:

- freeness of the root-cycle `C_p` action;
- finite étale degree `p` of the quotient;
- local freeness of rank `p`;
- the monic equation `T^p-T-g` satisfied by `y`;
- pairwise distinct translates on geometric fibres;
- an equal-rank fibrewise isomorphism argument.

This supplies the missing global algebra step.

### Theorem 10.1 — no-split theorem

The original wording conflated the squarefree product of root factors with the reduced denominator of `f'/f`. The proof now first writes `f'/f=P/R` in lowest terms and observes that the reduced denominator divides the squarefree root product, hence has degree at most three. The degree contradiction is then valid as written.

### Theorem 11.2 — Kummer quotient counts

The original proof used torsor fibre counts without explicitly proving freeness of the `mu_(p-3)` action. The manuscript now proves it: a stabilising dilation fixes the nonzero constant coefficient, hence has cube one; for prime `p>5`, `gcd(3,p-3)=1`, forcing the stabiliser to be trivial.

## Independent finite reconstruction

`paper6_independent_reconstruction.py` reproduces the committed finite checks for:

- tangent dual numbers at `p=5,7,11`;
- divided-hook character nonintegrality;
- Hattori--Stallings random checks at `p=5,7`;
- no-split panels at `p=7,11`;
- Kummer class checks at `p=5,11,17,23,29`;
- compactified quotient-count checks at `p=7,11,17,23`.

These are regression tests, not proofs of the general theorems.

## Cross-disciplinary boundary audit

The following general technologies are established literature and should not be marketed as new machinery:

- Hattori--Stallings traces;
- Artin--Schreier torsors;
- Kummer descent/forms;
- standard modular representation-theoretic extension language.

The possible new content lies in the particular sparse module, the no-divided-hook consequence, the explicit quotient attached to the sparse root-cycle family, the two-form count, and the compactified fixed-point/count identities.

## Remaining specialist risks

1. `VI-TANGENT`: the exact relationship among the cyclotomic tangent, nonsplit extension, and Smith-blindness needs modular-representation review.
2. `VI-DIVIDED-HOOK`: the no-divided-hook theorem needs a specialist priority/correctness audit; Hattori--Stallings extraction itself is classical.
3. `VI-AS-QUOTIENT` through `VI-COMPACT`: the repaired arguments are internally coherent, but a finite-field/arithmetic-geometry specialist should verify that every quotient is taken on the stated open locus and that compactification does not introduce an unaccounted stabiliser or boundary component.

No further model-level contradiction was found after the repairs.
