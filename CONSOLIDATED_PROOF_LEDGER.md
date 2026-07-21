# Consolidated Fortune proof ledger

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant and dynamics head `b2d0e266...`.

## 1. Scope

The repository contains two mathematically separate programmes.

`RQM_PROOF.md` proves a reciprocal-frame estimate for uniformly random orderings of integer block primes. It does not transfer to the increasing primorial order and does not prove the integer Fortune conjecture.

The function-field d=1 programme studies

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a != 0`,

and seeks one irreducible member in every characteristic. Results below concern this function-field crown unless stated otherwise.

## 2. Exact parity reduction

Put

`H_(a,c,d)(X)=aX^3+(c+1)X+d`.

Local admissibility means H is rootless over F_p. Every locally admissible F is squarefree and has no linear factor.

If F has r irreducible factors, Pellet gives

`chi(Disc F)=(-1)^(r+1)`.

A positive-discriminant reducible member therefore has at least three factors, and its smallest factor has degree at most `p/3`. Hence

> F is irreducible if and only if it is locally admissible, has positive discriminant, and has no factor of degree from 2 through `floor(p/3)`.

This is the exact parity-breaking sieve target.

## 3. Closed algebraic layer

The following are proved or independently machine-certified in `frontier/d1_discriminant/`:

1. exact degree-p discriminant formula;
2. exact complete discriminant mass and zero count;
3. local admissibility implies squarefreeness;
4. exact locally admissible family size `(p^2-1)/3`;
5. exact restricted discriminant-mass decomposition and `O(p^(3/2))` parity bound;
6. exact degree-2 and degree-3 compatibility formulae;
7. exact reduced Frobenius determinant indicator
   `J_a(c,d)=3a 1_(F irreducible)`;
8. exact top-coefficient reformulation
   `sum_(c,d)J_a(c,d)=[c^(p-1)d^(p-1)]J_a^can`.

The determinant coefficient remains unevaluated.

## 4. Complete quadratic deletion

The compatible quadratic traces satisfy

`a s^3-(2-c)s-d=0`.

Therefore

`nu_2(F) <= 3`.

The first unsigned and signed incidences are

`L_(a,2)=p^2/6+O(p)`,

`L_(a,2)^chi=O(p^(3/2))`.

Exact factorial moments through order three give

`N_(a,no2)=29p^2/144+O(p^(3/2))`,

`M_(a,no2)=O(p^(3/2))`.

Thus each discriminant-parity sector with no quadratic factor has size

`29p^2/288+O(p^(3/2))`.

All simultaneous configurations of quadratic factors are removed exactly.

## 5. Cubic compatibility and monodromy

The trace-zero plane gives a universal parameterization of oriented irreducible depressed cubics. Frobenius acts by

`tau(x,y)=(-y,x-y)`.

Eliminating the cubic invariants gives a monic degree-eight orientation polynomial `E_(c,d)(V)`. Every fibre has at most 24 compatible cubic factors:

`nu_3(F) <= 24`.

The generic arithmetic and geometric Galois groups of E are both `S_8`. This is proved by the specialization `c=d=-2`, whose good-prime cycle types include an 8-cycle, a 7-cycle, and a transposition, together with the nonsquare generic discriminant.

After marking roots inside the eight cubic blocks, the full geometric monodromy is

`C_3^8 semidirect S_8`.

The diagonal C_3 kernel is excluded by a rational specialization containing two distinct cyclic cubic fields of discriminants `13^2` and `7^2`. The sum-zero kernel is excluded by an explicit noncube product of the eight Cardano classes.

## 6. Complete cubic deletion

For the locally admissible family define

`Q_(a,3,j)=sum binom(nu_3(F),j)`.

For `0 <= j <= 8`, full marked monodromy, independence of the local S_3 field, and fixed-degree Lang-Weil estimates give

`Q_(a,3,j)=p^2/[j! 3^(j+1)]+O(p^(3/2))`.

The discriminant-weighted moments satisfy

`Q_(a,3,j)^chi=O(p^(3/2))`.

Orders `9 <= j <= 24` are supported on the fixed exceptional divisor and are `O(p)`, signed and unsigned.

Exact finite inclusion-exclusion therefore gives

`N_(a,no3)=C_3 p^2+O(p^(3/2))`,

`M_(a,no3)=O(p^(3/2))`,

where

`C_3=(1/3)sum_(j=0)^8 (-1/3)^j/j!`

`   =189550849/793618560`.

This removes every cubic factor, including exceptional fibres.

## 7. Complete mixed quadratic-cubic deletion

The full quadratic marked monodromy is

`C_2^3 semidirect S_3`.

At `d=0`, its three nontrivial quadratic classes are

`c-2`, `c-1`, `(c-2)(c-1)`.

The cubic orientation sign class is

`c^2-c+1`,

and the local-cubic sign class is

`c+1`.

These classes are independent. The quadratic, cubic, and local splitting fields are therefore linearly disjoint. The raw degree-p discriminant Kummer classes remain nontrivial on every mixed fibre power.

For `0 <= i <= 3`, `0 <= j <= 8`,

`Q_(a;i,j)=p^2/[3 i!2^i j!3^j]+O(p^(3/2))`,

`Q_(a;i,j)^chi=O(p^(3/2))`.

Orders `j>8` are `O(p)`.

Exact mixed inclusion-exclusion yields

`N_(a,no23)`
` =(5496974621/38093690880)p^2+O(p^(3/2))`,

`M_(a,no23)=O(p^(3/2))`.

Each parity sector with neither quadratic nor cubic factors has density

`5496974621/76187381760`

`=0.07215072225891911...`.

This is the first simultaneous complete deletion across two factor degrees.

## 8. Quartic single-factor theorem

Quartic factors are exact period-four cycles of

`g(X)=-aX^3-cX-d`.

The ordered cycle surface, after removing repeated coordinates, is geometrically integral of dimension two. Its local-root cover is also integral, the triple-root locus is zero-dimensional, and every required local or degree-p Kummer weight is nonsquare.

Therefore

`L_(a,4)=p^2/12+O(p^(3/2))`,

`L_(a,4)^chi=O(p^(3/2))`,

and

`L_(a,4,+)=p^2/24+O(p^(3/2))`.

Combining this with complete mixed quadratic-cubic deletion gives

`N_(a,rough4,+)`
` >= (2322500381/76187381760)p^2+O(p^(3/2))`.

Thus every sufficiently large slice contains a positive-discriminant population of density at least

`0.03048405559225244...`

with no factors of degrees 2, 3, or 4.

## 9. Finite quartic factorial reduction

The period-four dynatomic polynomial is

`Phi_(g,4)=[g^4(X)-X]/[g^2(X)-X]`

and has degree

`3^4-3^2=72`.

Every quartic factor contributes four distinct exact period-four points. Hence

`nu_4(F) <= 18`.

Quartic deletion is therefore finite:

`1_(nu_4=0)=sum_(j=0)^18 (-1)^j binom(nu_4,j)`.

The quartic factorial moments are not yet proved. Published dynatomic work establishes generic irreducibility in broad polynomial families and wreath-product monodromy in important cases, but a primary theorem whose explicit hypotheses directly cover the centered two-parameter cubic family has not yet been verified. No full quartic monodromy theorem is claimed in this ledger.

## 10. Current distance to the function-field crown

The theorem is not yet proved.

Closed:

- linear factors;
- every quadratic factor, including multiplicities;
- every cubic factor, including multiplicities and mixed quadratic-cubic configurations;
- first signed and unsigned quartic incidence;
- a positive rough-through-four sector;
- a finite quartic inclusion-exclusion bound.

Open:

1. complete quartic factorial moments and their mixed moments with degrees two and three;
2. a mechanism extending roughness through all degrees up to `p/3`, rather than one fixed degree at a time;
3. or, preferably, evaluation of the determinant top coefficient, which bypasses the factor sieve entirely.

## 11. Ranked next routes

1. **Direct determinant coefficient.** Find a constant-term, resultant, or recurrence formula for `[c^(p-1)d^(p-1)]J_a^can`.
2. **Quartic monodromy.** Prove that the period-four cycle cover for the centered cubic family has maximal cycle/root monodromy, either by checking a published theorem's hypotheses or by a direct specialization and branch-cycle proof.
3. **Quartic mixed sieve.** Once monodromy is known, compute the finite mixed factorial table and delete quartics exactly.
4. **Growing-degree compression.** Find a uniform cycle-index, trace formula, or determinant identity that controls all degrees through `p/3` without repeating fixed-degree geometry indefinitely.
5. **Integer Fortune.** The increasing-order transfer remains a separate major obstruction.