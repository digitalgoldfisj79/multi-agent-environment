# Consolidated Fortune proof ledger

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant and dynamics head `b2d0e266...`.

## 1. Closed theorem fronts

### RQM: random-order reciprocal-frame model

`RQM_PROOF.md` proves, under its stated frame-nondegeneracy and effective prime-count hypotheses,

`E_sigma E_a^sigma <= C(eta,rho) M (log X)^9`

uniformly for `1 <= |a| < H`, together with the weighted aggregate and Frobenius-energy bounds.

**Scope:** this is a theorem about uniformly random orderings of the block primes. It does not imply the estimate for the increasing primorial order and does not prove Fortune's conjecture.

### Function-field d=1: exact algebraic and sieve layers

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
16. exact signed quadratic-incidence decomposition with an effective `O(p^(3/2))` bound;
17. universal oriented-cubic parameterization by the trace-zero plane;
18. unsigned locally admissible cubic incidence `p^2/9 + O(p^(3/2))`;
19. signed cubic incidence `O(p^(3/2))`;
20. exact reduced Frobenius determinant indicator `J_a(c,d)=3a 1_irred`;
21. exact quadratic factorial sieve through order three and complete quadratic deletion;
22. uniform cubic-factor multiplicity bound `nu_3 <= 24` from a degree-eight orientation eliminant;
23. unsigned quartic incidence `p^2/12 + O(p^(3/2))` and signed quartic incidence `O(p^(3/2))`;
24. a positive-parity sector of size `p^2/288 + O(p^(3/2))` with no factors of degrees 2, 3, or 4.

Novelty of the exact objects and results remains provisional pending manual inspection of the offline sources listed in `NOVELTY_VERDICT.md`.

## 2. Consolidation correction

There is no direct mathematical interface between Theorem RQM and the function-field odd-reducible sector. RQM uses entropy from random orderings of integer block primes. The function-field problem has no such ordering variable.

The correct function-field companions are the parity-weighted factor sieve and the exact Frobenius determinant indicator.

## 3. Parity-breaking reduction

For

`F_(a,c,d)(X) = X^p + aX^3 + cX + d`

and

`H_(a,c,d)(X) = aX^3 + (c+1)X + d`,

let `A_a` be the coefficient pairs for which H is rootless. Every such F is squarefree and has no linear factor.

Pellet gives

`chi(Disc F)=(-1)^(r+1)`,

where r is the number of irreducible factors. Hence a positive-discriminant reducible member has at least three factors and therefore a factor of degree at most `p/3`. Thus

> F is irreducible if and only if it is locally admissible, has positive discriminant character, and has no factor of degree from 2 through `floor(p/3)`.

## 4. Completed quadratic multiplicative level

Every irreducible quadratic

`h_(s,n)(X)=X^2-sX+n`

divides exactly one member of the cubic slice, with

`c=1-a(s^2-n)`, `d=s(an-1)`.

The first signed and unsigned incidences satisfy

`L_(a,2)=p^2/6+O(p)`,

`L_(a,2)^chi=O(p^(3/2))`.

Eliminating n gives the trace equation

`a s^3-(2-c)s-d=0`.

Therefore every member has at most three irreducible quadratic factors. Exact factorial moments through order three give

`N_(a,no2)=29p^2/144+O(p^(3/2))`,

`M_(a,no2)=O(p^(3/2))`.

Consequently

`N_(a,no2,+)=29p^2/288+O(p^(3/2))`,

`N_(a,no2,-)=29p^2/288+O(p^(3/2))`.

This removes all quadratic factors, including simultaneous pairs and triples.

## 5. Completed cubic single-factor level and bounded fibres

Choose an irreducible base cubic `X^3+X+b` and identify its trace-zero plane with `F_p^2`. Frobenius acts universally by

`tau(x,y)=(-y,x-y)`.

The invariant forms parameterize oriented irreducible depressed cubics, three plane points per cubic. Fixed-degree geometry gives

`L_(a,3)=p^2/9+O(p^(3/2))`,

`L_(a,3)^chi=O(p^(3/2))`.

The compatible coefficient map has a monic degree-eight eliminant in the orientation V. For each V, a cubic equation determines the remaining invariant. Hence

`nu_3(F) <= 24`

uniformly for every member. Cubic deletion is therefore an exact finite factorial-moment problem through order 24, not an inclusion-exclusion problem with a p-dependent tail.

## 6. Completed quartic single-factor level

For a Frobenius-ordered quartic orbit `x_0,x_1,x_2,x_3`, compatibility is the fixed system

`x_(i+1)+a x_i^3+c x_i+d=0`

for i modulo four.

After scaling to a=1 and saturating by the Vandermonde, the characteristic-zero ordered-cycle ideal is prime of dimension two. Adding a local root produces another prime dimension-two cover. The local triple-root locus is zero-dimensional.

The local discriminant and all eight raw degree-p discriminant Kummer weights are nonsquares; this is certified by a transverse quartic number-field specialization.

Lang-Weil therefore gives

`L_(a,4)=p^2/12+O(p^(3/2))`,

`L_(a,4)^chi=O(p^(3/2))`,

and hence

`L_(a,4,+)=p^2/24+O(p^(3/2))`,

`L_(a,4,-)=p^2/24+O(p^(3/2))`.

## 7. Roughness through degree four

Let `N_(a,rough4,+)` count locally admissible positive-discriminant members with no factor of degree 2, 3, or 4. A union bound after the exact quadratic deletion gives

`N_(a,rough4,+)`
` >= N_(a,no2,+)-L_(a,3,+)-L_(a,4,+)`
` = [29/288-1/18-1/24]p^2+O(p^(3/2))`
` = p^2/288+O(p^(3/2))`.

Thus every sufficiently large cubic slice contains positive-parity members rough through degree four.

This is the final degree at which first-moment subtraction can work. The next expected positive degree-five incidence is `p^2/30`, which exceeds the remaining `p^2/288` margin. Further progress must use multiplicative correlations or the determinant indicator.

## 8. Exact full-cycle determinant indicator

Let B be the matrix of `Phi-I`, where `Phi(z)=z^p` on

`F_p[X]/(F_(a,c,d))`

in the basis `1,X,...,X^(p-1)`. Delete the constant column and the row indexed by `X^(p-3)`, and call the determinant `J_a(c,d)`.

For every coefficient pair,

`J_a(c,d)=3a * 1_(F irreducible)`.

Therefore, in `F_p`,

`sum_(c,d)J_a(c,d)=3a N_a(p)`.

Equivalently, if `J_a^can` is the canonical polynomial function,

`sum_(c,d)J_a(c,d)=[c^(p-1)d^(p-1)]J_a^can`.

A nonzero formula for this coefficient would prove the function-field crown directly. Initial small-prime determinant factorizations do not yet exhibit a stable coefficient recurrence.

## 9. Ranked open fronts

1. **Determinant top coefficient.** Find a constant-term, resultant, recurrence, or divided-hook formula for `[c^(p-1)d^(p-1)]J_a^can`.
2. **Finite cubic factorial sieve.** Determine the generic monodromy and top-dimensional components of the fibre powers of the degree-eight cubic map, then combine them with the quadratic deletion weight.
3. **Mixed roughness sieve.** Use exact mixed factorial moments rather than first-moment union bounds to pass degree five and beyond.
4. **O(p) geometric sharpening.** Remove weight-three cohomology from the completed degree-2, 3, and 4 surfaces; this improves constants but does not alone reach irreducibility.
5. **Increasing-order transfer from RQM.** This remains the original integer Fortune wall.

## 10. Immediate next action

The next controlled task is the generic monodromy of the degree-eight cubic orientation eliminant. If its geometric Galois group is S_8 or another explicitly transitive group, the cubic factorial moments become a finite Chebotarev calculation and exact cubic deletion can be completed. In parallel, the determinant coefficient remains the higher-upside direct route.