# Adversarial mathematical audit

## Decision

**Gate result: PROVISIONAL PASS TO EXTERNAL REVIEW.**

The main random-order theorem has a continuous proof under the explicit frame-admissibility hypothesis. A clean-room implementation reproduced every finite structural identity used in the proof. No fatal logical or normalisation gap was found. This is not yet a submission recommendation because novelty and field significance still require human specialist assessment.

## Frozen source basis

- `RQM_PROOF.md`, blob `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`.
- `PAPER2_ADDENDUM.md`, blob `71a9ad70c7164bcd94b92743fff3d8088c9a158b`.
- `CONDITIONAL_HL_BLOCK.md`, blob `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`.
- Archived Paper II reciprocal-frame definitions, blob `79da1c81b57b051cf8527889e84a6fe1161eb3fe`.

All source files were read from branch `gpt56/d1-gate-bridge-terminal-20260724`, except archived Paper II, which was read from `archive/fortune-paper2-20260720`.

## Load-bearing proof chain

1. Frame admissibility gives `D_X>0`, a lower bound for `D_X`, and diagonal control.
2. Pair-index differences have coefficient patterns of length two to four.
3. Conditioning on ranks gives an exact ordered set-partition law.
4. Multivariate Cauchy gives decay controlled by ratio-character deficits.
5. Gauss inversion converts each additive slot into a character slot with exact norm bounds.
6. Sixth-moment orthogonality and unique factorisation bound the number of bad characters by `O(X log^3 X)`.
7. Ratio coordinates form a tree, permitting an outer-to-inner matching sum.
8. The all-bad pattern dominates every pattern containing good coordinates.
9. The configuration ledger closes; the binding class is the four-endpoint, one-interior-micro-cell case.
10. Diagonal and harmonic-tail estimates assemble the fixed-harmonic, aggregate, and Frobenius conclusions.

## Issues found and resolved

### Indexing conflict

The source addendum used `N` for the number of block primes, whereas the RQM proof used `K` block primes and `N=K+1` path vertices. The manuscript now uses `K=|L_X|` and `N=K+1` consistently.

### Reliance on Paper II

The original proof referred repeatedly to Paper II equations. All definitions and load-bearing inequalities have been restated. Only the motivating interpretation remains companion-paper context.

### Meaning of unconditional

The theorem is unconditional with respect to prime-distribution conjectures, but is proved under the stated smoothing-function admissibility condition. The abstract and theorem now say this explicitly.

### Exact sixth moment

The exact polynomial was obtained through finite exact enumeration plus polynomial determination. It is now labelled computer-assisted and is not used in the main proof.

### Novelty language

The unverified phrase “first unconditional PGD2-type estimate” has been removed. The paper makes only the precise theorem claim and reports that a targeted search found no exact predecessor.

### Boundary cases

The empty initial cell, empty tail, orphan slots, binding exponent, and large-harmonic tail are now treated explicitly and independently checked.

## Clean-room results

Nine independent checks passed:

1. `N`-or-`1` difference dichotomy;
2. complete coefficient taxonomy;
3. exact ordered set-partition identity;
4. ratio-character contour inequality;
5. Gauss/CRT coefficient norms;
6. full end-to-end slot-character expansion;
7. sixth-moment exceptional-character count;
8. moment and exact-sixth-moment checks; and
9. every configuration-ledger exponent.

The binding classes C2a, C2b, and C2d reproduce `X^2 log^7 X = M log^9 X`.

## Residual risks

1. A referee may prefer a more invariant formulation of the smoothing class.
2. The C2 configuration ledger should be independently reconstructed by a human reader without code.
3. Absence from the literature cannot be certified by search alone.
4. The theorem is a model theorem and must not be presented as direct control of the increasing primorial order.

## Submission gate

Send the manuscript for targeted external review now. Do not yet submit it to a journal or publish it as a final Zenodo preprint. A positive response from an analytic/probabilistic number theorist and a character-sum specialist is the remaining publication gate.
