# External review memorandum

## Review status

**Not yet cleared for specialist circulation.** The frozen proof source claims a complete theorem, but the exact manuscript intended for circulation is still undergoing a source-fidelity check and a fresh manuscript-only hostile review.

## Provenance and responsibility

This manuscript was assembled with substantial large-language-model assistance from frozen research notes and proof files. Large language models were also used for adversarial review, literature triage, code generation, finite exact checks, and editorial reconstruction. The computational checks verify specified identities and normalisations; they do not certify manuscript fidelity or replace human proof review. Edward Stewart Anthony Bozzard is the named author and takes responsibility for the mathematical claims, citations, code, disclosures, and final text.

## Result under review

For a uniformly random ordering of the primes in `[X,2X)`, form the nested prefix products and all unordered pair sums of the resulting `N` centres. Sample pair-sum differences through a reciprocal Fourier frame with prime moduli `q,r ~ X^2`. The frozen source claims

`E_sigma E_a <= C M (log X)^9`

uniformly for all natural harmonics `1 <= |a| < eta X^2`, together with weighted aggregate and Frobenius-energy versions, under an explicit quantitative frame-admissibility condition.

## Why it may be interesting

- It reaches the critical reciprocal-energy scale in a random-order model with the same block primes, pair lift, moduli, and harmonic range as the deterministic primorial problem.
- It uses no GRH or pointwise prime-character estimate; instead, expectation over a uniformly random permutation supplies the decisive cancellation.
- Random order is treated through exact ordered set partitions rather than independent-cell or Poisson approximations.
- A sixth-moment count of exceptional characters is claimed to be exactly strong enough to close the binding configurations.

## What it does not prove

The increasing order is one deterministic ordering and receives no permutation entropy. The theorem does not imply Fortune's conjecture, a prime after every primorial, or the reciprocal-frame bound for the increasing order.

## No-cushion risk

The declared binding classes `C2a`, `C2b`, and `C2d` close at the headline order `M(log X)^9`; there is no positive power-of-`X` margin. The most consequential review task is therefore to reconstruct the configuration partition and multiplicities independently and determine whether any omitted or miscounted family loses the estimate.

## Questions for the reviewer

1. Is the main theorem new in substance, or is it subsumed by a known theorem on random permutations, multiplicative walks, or character sums?
2. Is the contour/coordinate/matching/ledger proof complete and uniform in all parameters?
3. Is the configuration ledger exhaustive, with no missing multiplicity or orphan-slot loss at the binding scale?
4. Is the result independently interesting without the Fortune motivation?
5. Which journal level and mathematical framing would be appropriate?

## High-risk proof locations

- Quantitative frame admissibility and every use of the normalising denominator.
- Ratio-character contour decay.
- Full Gauss/CRT slot expansion, including empty initial and tail cells.
- Triangular coordinate bijection and orphan slots.
- Path matching and pattern domination.
- `C2a/C2b/C2d` binding ledger and exhaustiveness of the full `T/C` partition.
- Passage from the fixed-harmonic estimate to the weighted aggregate and harmonic tail.
