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
12. unconditional `O(p^(3/2))` factor-parity estimate;
13. exact degree-2 and degree-3 unconditioned factor-incidence formulas;
14. exact parity-breaking sieve reduction;
15. exact locally admissible quadratic-incidence formula with `O(p)` error;
16. exact reduced Frobenius-determinant criterion for irreducibility;
17. exact signed quadratic-incidence decomposition with an effective `O(p^(3/2))` bound.

The quantized identity's method is classical. Novelty of the exact object and result remains provisional pending manual inspection of the offline sources listed in `NOVELTY_VERDICT.md`.

## 2. Consolidation correction

There is **no direct mathematical interface between Theorem RQM and the function-field odd-reducible sector**. RQM uses entropy from random orderings of integer block primes. The function-field problem has no such ordering variable. Earlier wording suggesting that an “RQM assembly” could combine with the discriminant theorem is withdrawn.

The correct companion to the discriminant theorem is a parity-weighted factor sieve or an equivalent full Frobenius-class trace formula.

## 3. Parity-breaking reduction

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

## 4. First completed sieve level: quadratic factors

Every irreducible quadratic

`h_(s,n)(X) = X^2 - sX + n`

divides exactly one member of the cubic slice, with

`c = 1 - a(s^2 - n)`,

`d = s(an - 1)`.

The associated local cubic satisfies the exact identity

`H_(s,n)(X) = a(X + s)h_(s,n)(X) + (2X - s)`.

This makes the total local-root incidence exactly `p(p - 1)/2`, equal to the number of irreducible quadratics.

Let `L_(a,2)` be the number of compatible irreducible quadratics whose local cubic is rootless. Then

`L_(a,2) = p(p - 1)/6 + [1 + chi(a)(p chi(-1) - K_p) - 2T_a]/6`,

where `T_a` is an explicit correction with at most three terms and

`K_p = sum_(D,S) chi(D S P(D,S))`

for the fixed polynomial

`P(D,S) = D^3 - 18D^2S - 24D^2 + 81DS^2 - 360DS + 192D + 144S - 512`.

The double cover `Z^2 = D S P(D,S)` compactifies to a `(4,4)` double cover of `P^1 x P^1` with only ADE singularities; its minimal resolution is a K3 surface. Hence

`K_p = O(p)`

and therefore

`L_(a,2) = p^2/6 + O(p)`.

For the signed incidence

`L_(a,2)^chi = sum_(locally admissible F) chi(Disc F) nu_2(F)`,

an exact four-term decomposition separates two complete `(D,S)` sums, one root-incidence `(w,t)` sum, and a triple-root correction. After expanding the character projectors, every raw term is a one-variable quadratic-character sum of degree at most 6 or 8. The complete and root families have at most 23 and 28 exceptional fibres, respectively. Therefore

`|L_(a,2)^chi| <= 30 p^(3/2) + 131p + 1`.

Consequently the positive- and negative-discriminant sectors each carry

`p^2/12 + O(p^(3/2))`

quadratic-factor incidence. This completes the first signed sieve level.

## 5. Full-cycle determinant

Let B be the matrix of `Phi - I`, where `Phi(z) = z^p` on

`F_p[X]/(F_(a,c,d))`

in the basis `1,X,...,X^(p-1)`.

Delete the constant column and the `X^(p-3)` row. The resulting determinant `J_a(c,d)` satisfies, for every squarefree member,

`J_a(c,d) != 0 if and only if F_(a,c,d) is irreducible`.

The row choice is canonical: the trace row is a left nullvector and Newton's identities give

`Tr(X^(p-3)) = 3a != 0`,

whereas `Tr(1) = p = 0`, so deleting the constant row would fail.

The determinant criterion has been exhaustively checked against an independent Rabin test for both square classes at `p = 5,7,11,13`. It packages every factor degree simultaneously and is the cleanest direct alternative to the parity sieve.

## 6. Representation-theoretic form

For squarefree degree-p `F`, let `sigma_F` be Frobenius on its roots and `Std` the standard `(p - 1)`-dimensional representation. Then

`p * 1_(F irreducible) = det(1 - sigma_F | Std)`

and

`det(1 - sigma_F | Std) = sum_(j=0)^(p-1) (-1)^j chi_(exterior^j Std)(sigma_F)`.

The discriminant character is only the top exterior-power term. The reduced Frobenius determinant is the linear-algebraic realization of the complete full-cycle detector.

## 7. Ranked open fronts after the signed quadratic theorem

1. **Sharpen signed quadratic incidence.** The observed values are `O(p)`. Proving this requires an irregularity and singularity audit of the finite list of fixed double-cover surfaces in `SIGNED_QUADRATIC_INCIDENCE.md`.
2. **Locally admissible cubic incidence.** Repeat the quadratic programme on the oriented cubic surface; target `p^2/9 + O(p)` and its signed analogue.
3. **Frobenius-determinant structure.** Search for a basis giving block triangularity, low displacement rank, a norm/resultant formula, or an explicit nonvanishing coefficient family. Small-prime canonical polynomials have no stable factorisation yet.
4. **Multiplicative parity sieve.** Extend the degree-2 and degree-3 incidence control to squarefree products only after the signed single-factor layers are understood. A term-by-term attack through degree `p/3` is not currently justified.
5. **Increasing-order transfer from RQM.** This remains the integer Fortune wall. A variance theorem over random orderings would strengthen genericity but still would not select the increasing order without an additional deterministic transfer principle.

## 8. Immediate next action

The next controlled decision is between two fixed-complexity tasks: audit the signed quadratic double covers to remove the possible weight-3 cohomology and obtain `O(p)`, or move to the unsigned cubic-incidence surface where a new `p^2/9` main term is available. The signed quadratic audit has priority because it would fully close both halves of the first parity-sieve level.