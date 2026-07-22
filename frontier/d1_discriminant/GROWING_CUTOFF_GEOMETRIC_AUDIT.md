# Geometric audit of the growing-cutoff sieve

**Date:** 2026-07-22  
**Status:** audit passed after clarifying the equivariant model used for finite-field twists.

## 1. Issue audited

`GROWING_CUTOFF_BONFERRONI.md` bounds the degree of every mixed marked
period cover by

`3^(sum k j_k)`

before the fixed local, sign and open-locus corrections.  It then uses the
fact that finite-field twists have the same degree over the algebraic
closure.

A single-root equation

`Phi_k(c,d;x)=0`

is a valid low-degree model of the marked root cover.  However, the cyclic
automorphism

`x -> g(x)`

is nonlinear in that embedding.  Degree preservation under twisting should
therefore not be justified by claiming that this particular embedding is
already equivariant and linear.

## 2. Correct cycle-coordinate model

For one marked exact k-cycle use coordinates

`x_0,...,x_(k-1)`

and equations

`x_(i+1)=g(x_i)`, `0<=i<k-1`,

`x_0=g(x_(k-1))`.

Each equation has total degree three.  The variety has dimension two over
the coefficient plane, and Bezout gives degree at most

`3^k`.

Remove the loci where coordinates repeat with a proper divisor of k.  This
is precisely the exact-period open subvariety.

The cyclic automorphism is now the linear coordinate permutation

`(x_0,x_1,...,x_(k-1))`

` -> (x_1,...,x_(k-1),x_0).`

The canonical finite-field twist selecting Frobenius k-cycles is therefore a
twist in a projective-linear equivariant embedding.  Meagher's twist lemma
applies directly, and the twist has the same dimension and degree.

For `j_k` ordered distinct k-cycles, take the product of `j_k` such blocks
and remove all cross-block coordinate diagonals.  The twisting group is
`C_k^(j_k)` acting by coordinate permutations.  No `S_(j_k)` twist is
needed because the cycles are ordered before dividing the point count by
`j_k!`.

## 3. Mixed degree bound

For a tuple `j=(j_2,...,j_K)`, the cycle-coordinate model has

`sum_(k=2)^K k j_k`

cycle coordinates and the same number of cubic equations.  Hence

`deg <=3^[sum k j_k] <=3^(K sum j_k).`

This is exactly the degree used in the Bonferroni note.

The local cubic splitting cover can likewise be represented by three root
coordinates with linear `S_3` permutation action.  The quadratic
Discriminant cover has its standard linear involution.  Thus their twists
contribute only the fixed factor already included in

`Delta_(K,L)=12(L^2K+1)3^[K(L+1)].`

The distinctness, branch and exact-period exclusions are products of
coordinate differences and fixed Jacobian/branch equations.  Their total
degree is smaller than the deliberately conservative

`(L^2K+1)3^K`

factor used there.

## 4. Counting normalization

An ordered tuple of selected irreducible factors contributes

`product k^(j_k)`

points to the cycle-coordinate twists, according to the choice of initial
root in each Frobenius cycle.  Forgetting the ordering contributes the
additional divisor

`product j_k!`.

The local 3-cycle and quadratic sign twists contribute the expected density
factors `1/3` and `1/2`.  Therefore the normalized tuple main term is

`p^2/[6 product j_k! k^(j_k)]`,

as used in the global factorial-moment calculation.

The Lang--Weil error is divided by the same centralizer and ordering factors.
Ignoring those divisors, as the Bonferroni note does in its upper bound, is
conservative.

## 5. Other audit checks

The following points were independently re-derived.

1. For odd L,

   `sum_(j=0)^L (-1)^j binom(n,j)<=1_(n=0)`.

2. With L the least odd integer at least `6lambda`, `lambda>=1/2`,

   `sum_(j=0)^L (-lambda)^j/j! >= exp(-lambda)/2`.

3. The multinomial identity gives the global order-j main term

   `p^2 lambda_K^j/(6j!)`.

4. `exp(-(H_K-1))>=1/K`.

5. The two explicit error inequalities in the Bonferroni note imply a total
   error at most `p^2/(24K)`.

6. The standard-library estimator verified the Taylor inequality for every
   `2<=K<=10000`.

## 6. Verdict

The theorem and its degree exponent survive the audit.  The correct geometric
statement is:

> use the cycle-coordinate complete-intersection model to make cyclic
> rotation linear before twisting.

The single-root dynatomic model remains useful for degree intuition, but it
should not be cited by itself as the equivariant embedding underlying the
twist-degree assertion.
