# Consolidated Fortune proof ledger

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant and dynamics head `b2d0e266...`.

## 1. Closed theorem fronts

### RQM: random-order reciprocal-frame model

`RQM_PROOF.md` proves, under its stated frame-nondegeneracy and effective prime-count hypotheses,

`E_sigma E_a^sigma <= C(eta,rho) M (log X)^9`

uniformly for `1 <= |a| < H`, together with the weighted aggregate and Frobenius-energy bounds. The load-bearing arithmetic input is the exact sixth-moment count of characters with block-prime correlation at least `3/4`; the finite configuration and matching ledger closes with a polylogarithmic margin.

**Scope:** this is a theorem about uniformly random orderings of the block primes. It does not imply the estimate for the increasing primorial order and does not prove Fortune's conjecture.

### Exact moment, tail, and singular-series layers

The difference-multiplicity dichotomy, partition moment formula, sixth moment, centred third moment, stretched-exponential upper tail, explicit variance constant, and truncated singular-series identity remain proved as recorded in the addendum and frontier files. The corrected conditional route must use block-averaged Hardy-Littlewood hypotheses; the earlier pointwise first-moment hypothesis was logically stronger than its conclusion.

### Function-field d=1: exact algebraic layer

The following are proved or machine-certified as labelled in `D1_ATTACK.md` and `frontier/d1_discriminant/`:

1. reduction to the sparse cubic family;
2. master root-incidence identity;
3. affine orbit structure;
4. quantized Kloosterman and root-count identity;
5. exact four-slice ledger and Lemma-L reduction;
6. machine certification through the stated finite range;
7. exact degree-p discriminant formula;
8. exact complete-slice Mobius mass and zero-discriminant count;
9. local admissibility implies squarefreeness;
10. exact count `(p^2 - 1)/3` of locally admissible members per nonzero cubic slice;
11. exact restricted discriminant-mass decomposition;
12. unconditional `O(p^(3/2))` factor-parity estimate.

The quantized identity's method is classical. Novelty of the exact object and result remains provisional pending manual inspection of the offline sources listed in `NOVELTY_VERDICT.md`.

## 2. Consolidation correction

There is **no direct mathematical interface between Theorem RQM and the function-field odd-reducible sector**. RQM uses entropy from random orderings of integer block primes. The function-field problem has no such ordering variable. Earlier wording suggesting that an “RQM assembly” could combine with the discriminant theorem is withdrawn.

The correct companion to the discriminant theorem is a parity-weighted factor sieve or an equivalent full Frobenius-class trace formula.

## 3. New exact reduction

For

`F_(a,c,d)(X) = X^p + a X^3 + c X + d`

and

`H_(a,c,d)(X) = a X^3 + (c + 1) X + d`,

let `A_a` be the coefficient pairs for which `H_(a,c,d)` is rootless over `F_p`. Every `F` in `A_a` is squarefree and has no linear factor.

Write `F = product_i P_i` as a product of `r` distinct monic irreducibles. Pellet gives

`chi(Disc F) = (-1)^(r+1)`.

Hence positive discriminant means that `r` is odd. If such an `F` is reducible then `r >= 3`, so its smallest factor has degree at most `p/3`. Therefore:

> `F` is irreducible if and only if it is locally admissible, has positive discriminant character, and has no factor of degree from `2` through `floor(p/3)`.

The full proof and exact inclusion-exclusion form are in `frontier/d1_discriminant/PARITY_SIEVE_REDUCTION.md`.

This is the correct parity-breaking use of the discriminant theorem. It reduces the open crown to a lower-bound sieve over only the positive-parity locally admissible sector.

## 4. Representation-theoretic form

For squarefree degree-p `F`, let `sigma_F` be Frobenius on its roots and `Std` the standard `(p - 1)`-dimensional representation. Then

`p * 1_(F irreducible) = det(1 - sigma_F | Std)`

and

`det(1 - sigma_F | Std) = sum_(j=0)^(p-1) (-1)^j chi_(exterior^j Std)(sigma_F)`.

The discriminant character is only the top exterior-power term. A complete irreducibility count requires either the full alternating hook-character sum or an equivalent parity-weighted sieve. This explains exactly why the discriminant mass alone cannot finish the theorem.

## 5. Ranked open fronts after consolidation

1. **Parity-weighted factor sieve for FF-Fortune `(p,1)`.** Establish a positive lower bound after removing factor degrees through `p/3`, using the exact parity weight. This is the nearest route to a full infinite-family theorem.
2. **Hook-trace or geometric collapse.** Seek a fixed-complexity realization of the full alternating exterior-power trace rather than bounding the `p` hook terms separately.
3. **Constructive dynamics.** The period-p equivalence is exact, but affine maps and global rational semiconjugacies are eliminated. Exact small-prime interpolation shows no stable sparse fibre-semiconjugacy pattern so far.
4. **Increasing-order transfer from RQM.** This remains the integer Fortune wall. A variance theorem over random orderings would strengthen genericity but still would not select the increasing order without an additional deterministic transfer principle.

## 6. Immediate programme

The next work targets the parity sieve, beginning with the exact divisor-incidence functions

`A_a(D) = number of locally admissible F divisible by D`

and

`B_a(D) = sum of chi(Disc F) over locally admissible F divisible by D`,

for squarefree products `D` of irreducibles of degrees `2` through `floor(p/3)`. For every fixed `D` of degree at least two, at most one coefficient pair `(c,d)` is possible. The remaining problem is therefore an incidence-distribution theorem, not a multiplicity problem.
