# Consolidated Fortune proof ledger

**Date:** 2026-07-22  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant,
dynamics, Cartier and dynatomic-sieve programmes.

## 1. Scope

The repository contains two mathematically separate programmes.

`RQM_PROOF.md` proves a reciprocal-frame estimate for uniformly random
orderings of integer block primes. It does not transfer to the increasing
primorial order and does not prove the integer Fortune conjecture.

The function-field d=1 programme studies

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a!=0`,

and seeks one irreducible member in every characteristic. Results below
concern this function-field crown unless stated otherwise.

## 2. Exact parity reduction

Put

`H_(a,c,d)(X)=aX^3+(c+1)X+d`.

Local admissibility means H is rootless over F_p. Every locally admissible F
is squarefree and has no linear factor.

If F has r irreducible factors, Pellet gives

`chi(Disc F)=(-1)^(r+1)`.

A positive-discriminant reducible member therefore has at least three
factors, and its smallest factor has degree at most `p/3`. Hence

> F is irreducible if and only if it is locally admissible, has positive
> discriminant, and has no factor degree from 2 through `floor(p/3)`.

This is the exact parity-breaking sieve target.

## 3. Closed algebraic layer

The following are proved or independently machine-certified in
`frontier/d1_discriminant/`:

1. exact degree-p discriminant formula;
2. exact complete discriminant mass and zero count;
3. local admissibility implies squarefreeness;
4. exact locally admissible family size `(p^2-1)/3`;
5. exact restricted discriminant-mass decomposition and `O(p^(3/2))` parity
   bound;
6. exact low-degree compatibility formulae;
7. exact reduced Frobenius determinant indicator
   `J_a(c,d)=3a 1_(F irreducible)`;
8. exact ordinary Cartier cofactor indicator
   `Cofactor_(p,3)(I-H_Cartier)=3a 1_(F irreducible)`;
9. general prime-degree Cartier theorem
   `Cofactor_(p,j)(I-H_Cartier)=j f_j 1_(F irreducible)`;
10. exact top-coefficient reformulation
    `sum_(c,d)J_a(c,d)=[c^(p-1)d^(p-1)]J_a^can`.

The complete determinant/cofactor coefficient remains unevaluated.

## 4. Complete quadratic deletion

The compatible quadratic traces satisfy

`a s^3-(2-c)s-d=0`,

so `nu_2(F)<=3`.

The first unsigned and signed incidences are

`L_(a,2)=p^2/6+O(p)`,

`L_(a,2)^chi=O(p^(3/2))`.

Exact factorial moments through order three give

`N_(a,no2)=29p^2/144+O(p^(3/2))`,

`M_(a,no2)=O(p^(3/2))`.

Thus each discriminant-parity sector with no quadratic factor has size

`29p^2/288+O(p^(3/2))`.

## 5. Cubic compatibility and complete deletion

The trace-zero plane gives a universal parameterization of oriented
irreducible depressed cubics. Eliminating the cubic invariants gives a monic
degree-eight orientation polynomial, and every fibre has at most 24
compatible cubic factors.

The generic marked group is

`C_3^8 semidirect S_8`.

For `0<=j<=8`,

`Q_(a,3,j)=p^2/[j!3^(j+1)]+O(p^(3/2))`,

`Q_(a,3,j)^chi=O(p^(3/2))`.

Orders `9<=j<=24` lie on a fixed exceptional divisor and are `O(p)`. Exact
finite inclusion--exclusion gives

`N_(a,no3)=C_3p^2+O(p^(3/2))`,

`M_(a,no3)=O(p^(3/2))`,

where

`C_3=(1/3)sum_(j=0)^8(-1/3)^j/j!`

`   =189550849/793618560`.

## 6. Complete mixed quadratic-cubic deletion

The quadratic marked group is

`C_2^3 semidirect S_3`,

and is linearly disjoint from the cubic marked field and the local cubic
field. The raw degree-p discriminant Kummer classes remain nontrivial on
every mixed fibre power.

For `0<=i<=3`, `0<=j<=8`,

`Q_(a;i,j)=p^2/[3i!2^i j!3^j]+O(p^(3/2))`,

`Q_(a;i,j)^chi=O(p^(3/2))`.

Exact mixed inclusion--exclusion yields

`N_(a,no23)`

` =(5496974621/38093690880)p^2+O(p^(3/2))`,

`M_(a,no23)=O(p^(3/2))`.

Each parity sector with neither quadratic nor cubic factors has density

`0.07215072225891911...`.

## 7. Complete periods four and five

A degree-k factor is an exact period-k cycle of

`g(X)=-aX^3-cX-d`.

The generic marked groups are

`G_4=C_4 wr S_18`,

`G_5=C_5 wr S_48`.

The local cubic field and all degree-p discriminant Kummer fields are
independent of these marked fields. All quartic and quintic factorial moments
are proved, signed and unsigned.

The period fields for `2,3,4,5` have full direct-product monodromy. Exact
simultaneous inclusion--exclusion gives

`N_(a,no2to5,+)`

` =(1/6)product_(k=2)^5 E_k p^2+O(p^(3/2))`,

where

`E_k=sum_(j=0)^(r_k)(-1/k)^j/j!`,

`r_k=(1/k)sum_(m|k)mu(k/m)3^m`.

The positive and negative rough-through-five sectors both have density

`0.04600533167213053...`.

## 8. Every fixed factor cutoff is closed

`FIXED_CUTOFF_DYNATOMIC_SIEVE.md` extends the construction to every fixed
finite cutoff K.

Morton's full wreath-product theorem and linear disjointness force generic
direct-product monodromy

`product_(k=2)^K(C_k wr S_(r_k))`.

The local cubic and raw discriminant Kummer fields are independent of every
finite dynatomic product. Therefore, for each fixed `K>=2`, outside a finite
set of primes depending on K,

`N_(a,no[2,K],+)`

` =(1/6)product_(k=2)^K E_k p^2+O_K(p^(3/2))`,

with the same formula for the negative sector.

The product has the dimension-one asymptotic

`product_(k=2)^K E_k~C_0/K`,

`C_0=1.5202566273133043...`.

The positive rough-sector density is asymptotic to

`0.2533761045522174.../K`.

## 9. Cartier--Krylov transfer theorem and no-go result

Let Q be Frobenius on `F_p[X]/(F)` in the signed power basis and let H be the
full Cartier matrix. The residue Gram matrix is

`G_(m,v)=(-1)^m(`

` 1_(m+v=p)-a1_(m+v=2p-3)-c1_(m+v=2p-1))`,

with `det G=1`.

Frobenius--Cartier adjunction gives

`H=G^(-1)QG`,

`I-H=G^(-1)(I-Q)G`.

The associated principal-part Krylov matrix is `K=QG`, and the sparse
boundary matrix is `G^(-1)`, so `H=G^(-1)K`.

Thus the natural p-dimensional Cartier transfer is exactly the
Berlekamp/Frobenius operator in residue-dual coordinates. It does not provide
an independent lower-dimensional evaluator of the complete cofactor sum.

Files:

- `CARTIER_KRYLOV_TRANSFER.md`;
- `cartier_krylov_transfer_check.py`.

## 10. Growing-cutoff Bonferroni theorem

Complete inclusion--exclusion through K uses the full splitting compositum,
whose size is roughly `exp(O(K3^K))`. The global Bonferroni sieve instead puts

`nu_[2,K](F)=sum_(k=2)^K nu_k(F)`

and truncates

`1_(nu_[2,K]=0)`

at one odd total factorial order L.

Put

`lambda_K=H_K-1`

and let L be the least odd integer at least `6lambda_K`. The alternating
Taylor bound gives

`sum_(j=0)^L(-lambda_K)^j/j!`

` >=(1/2)e^(-lambda_K)>=1/(2K)`.

Only mixed covers selecting at most `L=O(log K)` factors are needed. In the
linear cycle-coordinate model their degree is bounded by

`Delta_(K,L)=12(L^2K+1)3^[K(L+1)]`.

There are

`N_(K,L)=binom(K-1+L,L)`

mixed tuples. Cafure--Matera point counting yields an explicit threshold

`P_geom(K)=max {`

` 6Delta^2,`

` (192KNDelta^3)^2,`

` 960KNDelta^(13/3) }`.

### Good-reduction theorem

If p is a good-reduction prime for all required mixed twists and
`p>=P_geom(K)`, then, uniformly for every nonzero a,

`boxed(N_(a,no[2,K],+)>=p^2/(24K)>0.)`

The geometric threshold satisfies

`log P_geom(K)=(36log3+o(1))KlogK`.

Thus, along primes having the required moving good reduction, one may take

`K(p) asymp log p/log log p`.

### Unconditional diagonal theorem

For each fixed K, include all exceptional reduction primes and the geometric
threshold in an increasing number `P_K`. Define

`K_*(p)=max{K:P_K<=p}`.

Then `K_*(p)->infinity`, and for every sufficiently large prime p and every
nonzero a,

`boxed(N_(a,no[2,K_*(p)],+)>=p^2/[24K_*(p)]>0.)`

This is the first unconditional theorem in the programme with a factor cutoff
proved to tend to infinity. It is non-quantitative because no practical
uniform bound for moving-period exceptional reduction primes is known.

The geometric audit uses k-cycle coordinates

`x_(i+1)=g(x_i)`

so cyclic twisting acts by linear coordinate permutation. This preserves the
`3^k` degree bound and removes an ambiguity in the single-root presentation.

Files:

- `GROWING_CUTOFF_BONFERRONI.md`;
- `GROWING_CUTOFF_GEOMETRIC_AUDIT.md`;
- `growing_cutoff_bonferroni.py`;
- `GROWING_CUTOFF_NUMERICS.md`.

The explicit constants are structural, not practical: the current sufficient
threshold is already about `10^177` at K=5.

## 11. Current distance to the function-field crown

The crown is not yet proved.

Closed:

- linear factors and local admissibility;
- exact parity reduction;
- every fixed factor degree;
- every fixed finite collection of factor degrees and all mixed moments;
- an unconditional factor cutoff tending to infinity;
- an explicit `log p/log log p` distribution scale on moving good reductions;
- exact Frobenius and Cartier irreducibility indicators;
- the natural p-dimensional Cartier/Krylov transfer, shown Frobenius-conjugate;
- bounded-degree constructive semiconjugacies, ruled out by the `p/4` barrier.

Open:

1. control moving-period exceptional reduction primes quantitatively;
2. increase the factor-distribution level from `log p/log log p` to `p/3`;
3. find a genuinely compressed quotient of the Frobenius/Cartier module;
4. evaluate the complete determinant/cofactor sum directly;
5. prove the full-family character-sum Lemma L without returning to the
   growing-dimension square-root-cancellation wall.

The multiplicative sieve has the correct dimension-one main term. The gap is
now a distribution-level problem, not an unresolved individual period.

## 12. Ranked next routes

1. **Moving-period reduction.** Bound the reduction discriminants or Noether
   forms of the marked cycle-coordinate models and obtain an explicit
   all-prime lower bound for `K_*(p)`.
2. **Lower-bound Frobenius sieve.** Seek distribution for mixed products
   beyond the current `O(log K)` factorial level without constructing the
   full compositum.
3. **High-period tail.** Bound the number of positive-parity members having a
   factor in `(K,p/3]` after choosing the growing rough cutoff.
4. **Direct determinant coefficient.** Find a quotient or recurrence that is
   not Gram-conjugate to Frobenius.
5. **Integer Fortune.** The increasing-order transfer remains a separate
   major obstruction.
