# Cartier dominant coefficients as complementary inverse minors

**Date:** 2026-07-22  
**Status:** exact algebraic reduction for every prime `p>=5`. It strengthens the substitution-minor formula by replacing each large identity-selected term with two small complementary minors. It reduces the dominant part of the corrected support conjecture to one explicit modular-minor inequality. It does not prove that inequality or the full `w=1,2,3,4` theorem.

## 1. Matrices

Work over `F_p` with index universe

`Omega={0,1,...,p-1}`.

Define the full falling-factorial matrix

`P_(n,m)=(n)_m`

and the ordinary substitution matrix

`T_(q,m)=[X^q](X+X^3)^m.`

Both are lower unitriangular up to the diagonal factorials:

`det P=product_(m=0)^(p-1)m!,`

`det T=1.`

The exponential substitution matrix used in the Cartier grouping is

`B_(q,m)=T_(q,m)/m!`

`       =1/m! [X^q](X+X^3)^m.`

## 2. Identity-selected sets

Let `E` be the set of omitted falling-factorial row parameters coming from identity choices. Row `3` cannot be selected, so

`p-3 notin E.`

Put

`N={1,...,p-1}\E`

and

`Q=(N\{p-3}) union {0}.`

For a Cauchy-Binet degree set `M subset Omega` with

`|M|=|N|=|Q|`,

write

`R=Omega\M.`

The complementary row/column sets are

`N^c=E union {0}=:C_0,`

`Q^c=E union {p-3}=:C_1.`

Thus all complementary minors have size

`|E|+1`,

rather than size `p-1-|E|`.

## 3. Inverse falling-factorial matrix

Newton interpolation gives

`(P^(-1))_(r,s)`

` =(-1)^(r-s)/(s!(r-s)!)` if `r>=s`,

and zero otherwise.

Jacobi's complementary-minor identity yields

`det P_(N,M)`

` =epsilon_P(N,M) det(P) det(P^(-1))_(R,C_0),`

where

`epsilon_P(N,M)=(-1)^(sum N+sum M)`

for the increasing-order convention.

## 4. Inverse substitution matrix

Let `psi(X)` be the compositional inverse of

`phi(X)=X+X^3`

truncated below degree `p`:

`psi+psi^3=X.`

The inverse matrix of `T` is

`U_(r,s)=[X^r]psi(X)^s.`

For `s>=1`, Lagrange inversion gives

`U_(r,s)=0`

unless

`r=s+2h`, `h>=0`,

and in that case

`boxed( U_(r,s)=s/r (-1)^h binom(r+h-1,h). )`

Also `U_(0,0)=1` and `U_(r,0)=0` for `r>0`.

Jacobi gives

`det T_(Q,M)`

` =epsilon_T(Q,M) det U_(R,C_1),`

with

`epsilon_T(Q,M)=(-1)^(sum Q+sum M)`.

Because

`det B_(Q,M)=det T_(Q,M)/product_(m in M)m!`,

the factorials combine with `det P` to leave only the complement:

### Theorem CMR.1 — complementary product formula

For every identity set `E` and degree set `M`,

`boxed( det P_(N,M) det B_(Q,M)`

` =epsilon(E,M)`

`  (product_(r in R)r!)`

`  det(P^(-1))_(R,C_0)`

`  det(U)_(R,C_1). )`

Here `epsilon(E,M)` is the explicit product of the two Jacobi signs. Thus each large grouped Cartier term is exactly a product of two minors of size `|E|+1`.

No assignment enumeration and no large alternant evaluation is required.

## 5. Modular support of the inverse substitution matrix

For `0<=r,s<=p-1`, the Lagrange binomial satisfies a sharp Lucas cutoff.

If `s>=1` and `r=s+2h`, then

`binom(r+h-1,h)`

is nonzero modulo `p` exactly when

`r+h<=p`,

or equivalently

`3r-s<=2p.`

Indeed, if `r+h-1>=p`, Lucas's theorem gives zero because the lower digit `h` exceeds the lower base-p digit `r+h-1-p`; the converse is immediate below `p`.

Hence:

### Corollary CMR.2 — inverse-substitution band

`boxed( U_(r,s)!=0 mod p )`

only if

`r>=s,  r=s mod 2,  3r-s<=2p.`

This converts the substitution cancellation problem into a small banded-minor problem.

## 6. Weight in complementary coordinates

For the dominant `w=1` term, the total cubic-factor count is

`I=(sum Q-sum M)/2.`

Since complements have equal total universe sum,

`boxed( I=(sum R-sum C_1)/2. )`

The `(1,2)`-weight of the corresponding monomial is

`W=p(p-1)/2 + (sum R-3sum E+p-3)/2.`

Therefore the corrected one-extra-level bound

`W<=(p-1)(p+3)/2`

is equivalent to the elementary-looking complement inequality

### Lemma CT1-w1 — exact remaining dominant support lemma

Whenever

`det(P^(-1))_(R,E union {0})`

and

`det(U)_(R,E union {p-3})`

are both nonzero modulo `p`, and the torus-survivor grading holds, then

`boxed( sum R <= 3sum E+2p. )`

This is the precise dominant-`w=1` form of Conjecture CT1.

## 7. The p=29 tail is extremal

For the p=29 counterexample,

`E={1,2,4,5,7,8}`

and one nonzero complementary row set is

`R={11,18,19,20,21,22,28}`.

Then

`sum E=27,  sum R=139,`

and

`3sum E+2p=81+58=139.`

Thus the observed tail does not merely satisfy CT1-w1: it saturates it exactly. The old boundary would demand a strictly smaller complement sum and is therefore incompatible with this nonzero product.

Simple entrywise support is not sufficient to prove CT1-w1: the inverse-substitution band permits matchings with larger total row sum at p=29, but their determinant product vanishes. The remaining content is genuine modular minor cancellation in the small complementary matrices.

## 8. Extension to lower filtration blocks

The complete `w=1,2,3,4` coefficient matrix is a finite sum of shifted substitution matrices. The p=41,43,47 ledgers show that these shifts alter the top-tail coefficient.

A full proof of CT1 therefore requires a block or group-algebra extension of CMR.1 in which the four shifted inverse substitutions are assembled before the complementary determinant is evaluated.

The dominant theorem above is exact and supplies the base case, but a proof for `w=1` alone cannot establish the complete Cartier coefficient.

## 9. Strategic consequence

Route 1 is now reduced to two named algebraic tasks:

1. prove CT1-w1 for the product of the two explicit small minors;
2. derive and prove the shifted four-block analogue for the complete matrix.

If both succeed, the hard support cutoff is replaced by the one-extra-level theorem verified through p=47.

## 10. Epistemic classification

- Inverse falling-factorial formula: exact.
- Lagrange inversion formula for `U`: exact.
- Jacobi complementary-minor reduction: exact.
- Lucas support band: exact.
- Weight formula and equivalence to `sum R<=3sum E+2p`: exact.
- p=29 saturation: exact.
- CT1-w1: open.
- Four-block complementary formula and full CT1: open.
- Cartier nonvanishing and d=1 crown: open.
