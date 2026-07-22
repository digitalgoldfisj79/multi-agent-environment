# Consolidated Fortune proof ledger

**Date:** 2026-07-22  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant and dynamics programme.

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
8. exact ordinary Cartier cofactor indicator
   `Cofactor_(p,3)(I-H_Cartier)=3a 1_(F irreducible)`;
9. general prime-degree Cartier theorem
   `Cofactor_(p,j)(I-H_Cartier)=j f_j 1_(F irreducible)`;
10. exact top-coefficient reformulation
    `sum_(c,d)J_a(c,d)=[c^(p-1)d^(p-1)]J_a^can`.

The determinant/cofactor coefficient remains unevaluated.

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

## 5. Cubic compatibility and complete deletion

The trace-zero plane gives a universal parameterization of oriented irreducible depressed cubics. Frobenius acts by

`tau(x,y)=(-y,x-y)`.

Eliminating the cubic invariants gives a monic degree-eight orientation polynomial. Every fibre has at most 24 compatible cubic factors:

`nu_3(F) <= 24`.

The generic orientation group is `S_8`; after marking roots inside the eight blocks, the full geometric monodromy is

`C_3^8 semidirect S_8`.

For `0 <= j <= 8`, marked monodromy, independence of the local `S_3` field, and Lang--Weil give

`Q_(a,3,j)=p^2/[j! 3^(j+1)]+O(p^(3/2))`,

`Q_(a,3,j)^chi=O(p^(3/2))`.

Orders `9 <= j <= 24` lie on a fixed exceptional divisor and are `O(p)`, signed and unsigned. Exact finite inclusion--exclusion gives

`N_(a,no3)=C_3 p^2+O(p^(3/2))`,

`M_(a,no3)=O(p^(3/2))`,

where

`C_3=(1/3)sum_(j=0)^8 (-1/3)^j/j!`

`   =189550849/793618560`.

## 6. Complete mixed quadratic-cubic deletion

The full quadratic marked monodromy is

`C_2^3 semidirect S_3`,

and it is linearly disjoint from the cubic marked field and the local cubic field. The raw degree-p discriminant Kummer classes remain nontrivial on every mixed fibre power.

For `0 <= i <= 3`, `0 <= j <= 8`,

`Q_(a;i,j)=p^2/[3 i!2^i j!3^j]+O(p^(3/2))`,

`Q_(a;i,j)^chi=O(p^(3/2))`.

Orders `j>8` are `O(p)`. Exact mixed inclusion--exclusion yields

`N_(a,no23)`

` =(5496974621/38093690880)p^2+O(p^(3/2))`,

`M_(a,no23)=O(p^(3/2))`.

Each parity sector with neither quadratic nor cubic factors has density

`5496974621/76187381760`

`=0.07215072225891911...`.

## 7. Complete periods four and five

A degree-k factor is an exact period-k cycle of

`g(X)=-aX^3-cX-d`.

The generic marked cycle groups are

`G_4=C_4 wr S_18`,

`G_5=C_5 wr S_48`.

The local cubic field and all degree-p discriminant Kummer fields are independent of these marked dynatomic fields. Consequently all quartic and quintic factorial moments are proved, signed and unsigned:

`Q_(a,4,j)=p^2/[3 j!4^j]+O(p^(3/2))`, `0<=j<=18`,

`Q_(a,5,j)=p^2/[3 j!5^j]+O(p^(3/2))`, `0<=j<=48`,

with signed versions `O(p^(3/2))`.

The period fields for `2,3,4,5` have full direct-product monodromy. Exact simultaneous inclusion--exclusion gives

`N_(a,no2to5,+)`

` = (1/6) product_(k=2)^5 E_k * p^2+O(p^(3/2))`,

where

`E_k=sum_(j=0)^(r_k)(-1/k)^j/j!`,

`r_k=(1/k)sum_(m|k)mu(k/m)3^m`.

The positive and negative rough-through-five sectors both have density

`0.04600533167213053...`.

## 8. Every fixed factor cutoff is closed

`FIXED_CUTOFF_DYNATOMIC_SIEVE.md` extends the preceding construction from periods `2,...,5` to every fixed finite cutoff K.

Morton's full wreath-product theorem and linear disjointness on the unicritical line force full direct-product monodromy

`product_(k=2)^K (C_k wr S_(r_k))`

for the generic centered family.

The independence of the local cubic is uniform in the period. On the local-discriminant divisor, specialize to the map

`f(Z)=(Z^3+2)/3`.

Its unique finite critical orbit converges to its parabolic fixed point `Z=1`; it has no other finite root-of-unity multiplier cycle. Hence every exact dynatomic polynomial of period at least two is squarefree there, so the local discriminant is not a branch component of any higher-period field.

At the origin the map is `-X^3`, whose exact dynatomic polynomials are squarefree in every period. This proves the required independence of all raw discriminant Kummer classes from every finite dynatomic/local compositum.

For each fixed `K>=2`, outside a finite set of primes depending on K,

`N_(a,no[2,K],+)`

` = (1/6) product_(k=2)^K E_k * p^2+O_K(p^(3/2))`,

with the same formula for the negative sector.

Thus every fixed factor cutoff is now removed simultaneously, including all mixed factorial configurations.

The product has the dimension-one asymptotic

`product_(k=2)^K E_k ~ C_0/K`,

`C_0=1.5202566273133043...`.

The positive rough-sector density is therefore asymptotic to

`0.2533761045522174.../K`.

This identifies the remaining multiplicative obstruction exactly: uniformity when K grows linearly with p.

## 9. Cartier--Krylov transfer theorem and no-go result

Let `Q` be Frobenius on `F_p[X]/(F)` in the signed power basis and let H be the full Cartier matrix. Define the residue Gram matrix

`G_(m,v)=ell((-1)^m X^(m+v-1))`.

For the cubic slice,

`G_(m,v)=(-1)^m(`

` 1_(m+v=p)-a1_(m+v=2p-3)-c1_(m+v=2p-1))`,

and

`det G=1`.

Frobenius--Cartier adjunction gives the exact similarity

`H=G^(-1)QG`,

`I-H=G^(-1)(I-Q)G`.

The associated principal-part Krylov matrix is `K=QG`, and the sparse boundary matrix is `G^(-1)`, so `H=G^(-1)K`.

Therefore the natural Cartier transfer operator is exactly the Berlekamp/Frobenius operator in the residue-dual basis. It does not provide an independent lower-dimensional evaluator of the complete cofactor sum. This closes the obvious transfer route rigorously.

Files:

- `CARTIER_KRYLOV_TRANSFER.md`;
- `cartier_krylov_transfer_check.py`.

## 10. Current distance to the function-field crown

The theorem is not yet proved.

Closed:

- linear factors and local admissibility;
- exact parity reduction;
- every fixed factor degree;
- every fixed finite collection of factor degrees, including all mixed factorial moments;
- exact Frobenius and Cartier irreducibility indicators;
- the natural p-dimensional Cartier/Krylov transfer, shown to be Frobenius-conjugate;
- bounded-degree constructive semiconjugacies, ruled out by the `p/4` degree barrier.

Open:

1. uniform dynatomic/Chebotarev estimates for a cutoff K growing to `p/3`;
2. a genuinely compressed quotient of the Frobenius/Cartier module;
3. or a direct nonvanishing evaluation of the complete determinant/cofactor sum;
4. the full-family character-sum Lemma L, whose current formulations still face growing-dimension square-root cancellation.

The fixed-cutoff theorem shows that the multiplicative sieve itself has the correct main term and sieve dimension. The obstruction is not any individual period; it is uniformity across a linearly growing set of periods.

## 11. Ranked next routes

1. **Uniform fixed-cutoff constants.** Quantify the K-dependence of the effective Lang--Weil/Chebotarev constants and determine the largest provable growing cutoff `K(p)`. Even `K(p)->infinity` would be a new theorem, although it would not alone prove the crown.
2. **Large-sieve dynatomic compression.** Replace the full fibre product by a Frobenius large sieve over separate period covers, seeking uniform roughness without constructing the exponentially large compositum.
3. **Direct determinant coefficient.** Find a quotient, constant-term identity, or recurrence that is not Gram-conjugate to Frobenius and evaluates the two square-class modes.
4. **Character-sum Lemma L.** Seek a non-projective, non-Plancherel transform that preserves finer a-data before aggregation.
5. **Integer Fortune.** The increasing-order transfer remains a separate major obstruction.
