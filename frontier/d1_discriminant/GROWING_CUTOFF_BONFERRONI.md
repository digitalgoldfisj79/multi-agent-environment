# Growing-cutoff Bonferroni sieve

**Date:** 2026-07-22  
**Status:** unconditional non-effective growing-cutoff theorem; explicit
`K << log p/log log p` point-count scale proved away from the finite bad-reduction set of the required marked dynatomic models.

## 1. Purpose

`FIXED_CUTOFF_DYNATOMIC_SIEVE.md` proves, for every fixed K,

`N_(a,no[2,K],+)`

` = (1/6) product_(k=2)^K E_k p^2+O_K(p^(3/2))`,

where `N_(a,no[2,K],+)` counts locally admissible positive-discriminant
members of

`F_(a,c,d)=X^p+aX^3+cX+d`

with no factor degree from 2 through K.

The complete product cover has size roughly

`exp(O(K 3^K))`.

Using it directly therefore conceals all useful dependence on K.  This note
replaces complete inclusion--exclusion by one global odd Bonferroni
truncation.  Only covers marking `O(log K)` factors are then required.

## 2. Global factor count and factorial moments

Fix `p>K` and nonzero a.  On the locally admissible positive-discriminant
sector put

`nu_[2,K](F)=sum_(k=2)^K nu_k(F)`.

For `j>=0`, define the global factorial moment

`M_(K,j)^+=sum_F binom(nu_[2,K](F),j)`.

Expanding the binomial coefficient across factor degrees gives the exact
identity

`M_(K,j)^+`

` = sum_(j_2+...+j_K=j)`

`   sum_F product_(k=2)^K binom(nu_k(F),j_k).`

For a tuple `j=(j_2,...,j_K)`, the ordered marked cover has

`product_(k=2)^K j_k! k^(j_k)`

representatives for each selected factor tuple.  Full direct-product
monodromy makes its appropriate Frobenius twist geometrically integral in
characteristic zero.  The local cubic and discriminant Kummer covers are
independent by `FIXED_CUTOFF_DYNATOMIC_SIEVE.md`.

The expected main term of the tuple is therefore

`p^2/[6 product_(k=2)^K j_k! k^(j_k)].`

Put

`lambda_K=sum_(k=2)^K 1/k=H_K-1`.

The multinomial theorem gives

`sum_(j_2+...+j_K=j)`

` 1/[product j_k! k^(j_k)] = lambda_K^j/j!`.

Hence the combined order-j main term is

`p^2 lambda_K^j/(6j!).`

## 3. Odd Bonferroni lower bound

For every integer n and every odd L,

`1_(n=0) >= sum_(j=0)^L (-1)^j binom(n,j).`

Indeed, for `n>L` the right side equals

`-binom(n-1,L)`,

and for `1<=n<=L` it is zero.

Therefore

`N_(a,no[2,K],+)`

` >= sum_(j=0)^L (-1)^j M_(K,j)^+.`

Choose L to be the least odd integer satisfying

`L>=6 lambda_K`.

Since `lambda_K>=1/2`, the alternating exponential tail and

`n! >= (n/e)^n`

give

`0 <= e^(-lambda_K)`

` -sum_(j=0)^L (-lambda_K)^j/j!`

` <= lambda_K^(L+1)/(L+1)!`

` <= (e/6)^(6lambda_K)`

` <= (1/2)e^(-lambda_K).`

Consequently

`sum_(j=0)^L (-lambda_K)^j/j!`

` >= (1/2)e^(-lambda_K).`

The elementary bound `H_K<=1+log K` gives

`e^(-lambda_K)>=1/K`.

Thus the truncated main term is at least

`boxed(p^2/(12K)).`

This is the lower-bound-sieve step.  It is the reason that the full splitting
compositum is not needed.

## 4. Degree of the required mixed covers

Let

`Phi_k(c,d;X)`

be the exact period-k dynatomic polynomial of

`g(X)=-aX^3-cX-d`.

An induction on iteration gives

`deg_total(g^k(X)-X)<=3^k`.

Since `Phi_k` is a polynomial factor of this monic iterate difference,

`deg_total Phi_k<=3^k`.

A mixed marked cover of tuple order

`j=sum j_k<=L`

is an open subvariety of the complete intersection obtained by adjoining one
marked-root variable for every selected factor and imposing the corresponding
dynatomic equation.  Before removing diagonals and branch divisors, Bezout
gives degree at most

`product_(k=2)^K 3^(k j_k)<=3^(Kj).`

The forbidden orbit diagonals, ramification divisors, local cubic branch
locus and degree-p discriminant branch locus can be combined into one
nonvanishing polynomial.  A conservative degree bound for this polynomial is

`(L^2 K+1)3^K`.

Adjoining one inverse variable turns the open subvariety into an affine
variety.  Including the local cubic and quadratic Kummer twists yields the
uniform degree bound

`boxed(Delta_(K,L)=12(L^2 K+1)3^[K(L+1)].)`

Every finite-field twist is geometrically isomorphic to the original marked
cover over the algebraic closure, so it has the same dimension and degree.

The number of mixed tuples with total order at most L is

`boxed(N_(K,L)=binom(K-1+L,L).)`

## 5. Explicit point-count error on good reductions

Call a prime **(K,L)-good** when all ordered marked twists of total order at
most L, together with the local and discriminant covers used above, have the
geometric integrality supplied by the characteristic-zero monodromy theorem.
For fixed `(K,L)`, only finitely many primes are not `(K,L)`-good.

Cafure--Matera prove that an absolutely irreducible affine variety of
dimension two and degree delta satisfies, when `p>6delta^2`,

`|#V(F_p)-p^2|`

` <= delta(delta-1)(delta-2)p^(3/2)`

`    +5delta^(13/3)p.`

Applying this to the marked twists, absorbing their removed boundary loci,
and summing unsigned and discriminant-twisted counts gives the conservative
total error

`E_(K,L)(p)`

` <= N_(K,L) [`

`      4 Delta_(K,L)^3 p^(3/2)`

`     +20 Delta_(K,L)^(13/3) p ].`

It is sufficient that

`p>6Delta^2`,

`sqrt(p)>=192 K N Delta^3`,

`p>=960 K N Delta^(13/3)`.

Under these inequalities the total error is at most `p^2/(24K)`.  Combining
with the Bonferroni main term proves:

### Theorem GCB.1 -- explicit good-reduction theorem

Let `K>=2`, put `lambda_K=H_K-1`, and let L be the least odd integer at least
`6lambda_K`.  If p is `(K,L)`-good and satisfies

`p >= P_geom(K)`,

where

`P_geom(K)=max {`

` 6Delta^2,`

` (192 K N Delta^3)^2,`

` 960 K N Delta^(13/3) }`,

then, uniformly for every nonzero a,

`boxed(N_(a,no[2,K],+)>=p^2/(24K)>0.)`

In particular, every nonzero cubic slice contains a positive-discriminant,
locally admissible member with no factor degree at most K.

The point-count threshold is explicit.  The good-reduction test is a finite
algebraic computation in the integral marked-cover models.

## 6. Closed-form scale

For `K>=3`,

`L<=6log K+3`,

`log N_(K,L)=O((log K)^2)`,

and

`log Delta_(K,L)=6(log 3)K log K+O(K+log^2 K)`.

Substitution into `P_geom(K)` gives

`log P_geom(K)`

` <= (36log 3+o(1))K log K`

` = (39.550...+o(1))K log K.`

The deliberately rounded inequality

`boxed(log p>=100 K log K)`

is sufficient for every `K>=3` in the implemented bounds.

### Corollary GCB.2 -- good-prime growing scale

Along any sequence of primes p that is `(K(p),L(p))`-good, the choice

`K(p)=floor(log p/[200 log log p])`

satisfies the point-count inequalities for all sufficiently large p.
Consequently the positive sector is rough through

`K(p) asymp log p/log log p`.

This corollary retains the good-reduction qualification.  It is not a theorem
that every prime is good at this moving cutoff.

## 7. Unconditional growing cutoff by diagonalization

For each fixed K, `FIXED_CUTOFF_DYNATOMIC_SIEVE.md` supplies a threshold
`P_K` beyond which:

1. all relevant reductions are good;
2. the fixed-K error is smaller than half its positive main term.

Choose the thresholds increasing and define

`K_*(p)=max {K:P_K<=p}`.

Then `K_*(p)->infinity`.  Applying the fixed-K theorem at `K=K_*(p)` gives:

### Theorem GCB.3 -- unconditional growing roughness

There exists a nondecreasing function `K_*(p)->infinity` such that, for every
sufficiently large prime p and every nonzero a, the slice

`X^p+aX^3+cX+d`

contains locally admissible positive-discriminant members with no factor
degree from 2 through `K_*(p)`.

The function can be made computable by constructing integral models for the
finitely many covers at each K, applying effective generic freeness or
absolute-irreducibility algorithms to determine a localization integer, and
then using the explicit Cafure--Matera threshold.

This is the first unconditional result in the programme with a factor cutoff
proved to tend to infinity.  It remains non-quantitative because no practical
uniform bound for the exceptional reduction primes has been established.

## 8. Why the Frobenius large sieve is not yet a substitute

Kowalski's Frobenius large sieve is designed to upper-bound the set of base
points avoiding prescribed conjugacy subsets.  Here the desired rough set is
precisely such an avoiding set, and an upper-bound sieve does not prove that
it is nonempty.

A lower-bound or beta-sieve implementation would still require distribution
for mixed products up to a level comparable with the Bonferroni order.  The
odd global Bonferroni argument above already uses exactly that information
and makes its geometric complexity explicit.

The large sieve may still become useful for controlling the bad-reduction or
high-period tail, but it does not by itself replace the lower-bound step.

## 9. Remaining gap to the crown

The exact parity reduction requires exclusion of every factor degree through
`floor(p/3)`.

This note proves:

- an unconditional cutoff `K_*(p)->infinity`;
- an explicit `K<<log p/log log p` point-count scale on good reductions.

Neither reaches a linear cutoff.  The remaining gap is therefore now split
into two separate problems:

1. control the exceptional reduction primes uniformly in moving period;
2. improve the distribution level from approximately `log p/log log p` to a
   positive proportion of p.

The first is arithmetic geometry of dynatomic reduction.  The second requires
new cancellation or a true high-dimensional lower-bound sieve; it cannot be
obtained by merely sharpening constants in Lang--Weil.

## 10. Reproducibility and sources

`growing_cutoff_bonferroni.py` computes `lambda_K`, L, the number of mixed
tuples, the degree bound and the explicit point-count threshold.

Primary inputs:

- A. Cafure and G. Matera, *Improved explicit estimates on the number of
  solutions of equations over a finite field*, Finite Fields Appl. 12
  (2006), 155--185;
- S. Meagher, *A simple proof of Chebotarev's density theorem over finite
  fields*, Bull. Aust. Math. Soc. 98 (2018), 196--202;
- E. Kowalski, *The large sieve, monodromy and zeta functions of curves*, J.
  Reine Angew. Math. 601 (2006), 97--133;
- P. Morton, *On certain algebraic curves related to polynomial maps*,
  Compositio Math. 103 (1996), 319--350, together with the 2011 corrigendum;
- J. Doyle et al., *Reduction of dynatomic curves*, Ergodic Theory Dynam.
  Systems 39 (2019), 2717--2768, for the fact that moving-period good
  reduction is a substantive separate issue rather than an automatic
  consequence of characteristic-zero monodromy.
