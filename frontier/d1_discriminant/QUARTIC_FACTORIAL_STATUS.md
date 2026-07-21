# Finite quartic-factorial reduction

**Date:** 2026-07-21  
**Status:** uniform multiplicity bound and exact finite inclusion-exclusion proved. The quartic factorial moments remain open.

## 1. Dynamical interpretation

Let p >= 5, let a be nonzero in F_p, and put

`F_(a,c,d)(X)=X^p+aX^3+cX+d`.

Define the cubic map

`g_(a,c,d)(X)=-aX^3-cX-d`.

If alpha is a root of F, then

`alpha^p=g(alpha)`.

If alpha lies in an irreducible quartic factor of F, its Frobenius orbit has exact length four. Therefore

`g^4(alpha)=alpha`

and

`g^k(alpha) != alpha`

for `1 <= k < 4`.

Thus every root of every irreducible quartic factor is an exact composition-period-four point of g.

## 2. The period-four dynatomic polynomial

Because two divides four,

`g^2(X)-X`

divides

`g^4(X)-X`.

Define

`Phi_(g,4)(X) = [g^4(X)-X]/[g^2(X)-X]`.

This is the fourth dynatomic polynomial; for the present bound only the displayed quotient identity is needed.

Since g has degree three,

`deg(g^4-X)=3^4=81`,

`deg(g^2-X)=3^2=9`.

Hence

`deg Phi_(g,4)=72`.

Every exact period-four point is a root of `Phi_(g,4)`. The polynomial may acquire repeated roots or lower-period formal roots at exceptional coefficients, but this cannot increase the number of distinct exact period-four points beyond 72.

## 3. Uniform quartic multiplicity bound

Distinct irreducible quartic factors have disjoint root sets, and every such factor contributes four distinct exact period-four points.

### Theorem QFR.1

For every prime p >= 5, every nonzero a in F_p, and every c,d in F_p,

`nu_4(F_(a,c,d)) <= 18`.

### Proof

The union of the roots of all irreducible quartic factors is a subset of the distinct roots of the degree-72 polynomial `Phi_(g,4)`. Therefore

`4 nu_4(F) <= 72`.

QED.

## 4. Exact finite inclusion-exclusion

For every family member,

`1_(nu_4=0) = sum_(j=0)^18 (-1)^j binom(nu_4,j)`.

Consequently quartic deletion requires only the 19 factorial moments

`Q_(a,4,j)=sum_(locally admissible F) binom(nu_4(F),j)`

and their discriminant-weighted analogues

`Q_(a,4,j)^chi=sum_(locally admissible F) chi(Disc F) binom(nu_4(F),j)`.

There is no quartic inclusion-exclusion tail whose length grows with p.

## 5. Expected generic geometry

The generic period-four dynatomic polynomial has degree 72, corresponding to 18 four-cycles. If the generic cycle monodromy on these cycles is `S_18` and the four root markings are independent, the full marked monodromy is the wreath product

`C_4^18 semidirect S_18`.

That would imply the generic factorial main terms

`Q_(a,4,j)=p^2/[3 j! 4^j]+O(p^(3/2))`

for `0 <= j <= 18`, with signed moments `O(p^(3/2))`, after verifying independence from the local cubic and degree-p discriminant Kummer covers.

This paragraph is a programme, not a proved theorem. The unconditional content of this note is Theorem QFR.1 and the exact finite inclusion-exclusion identity.

## 6. Next controlled task

Determine the generic geometric Galois group of `Phi_(g,4)` for the centered cubic family

`g(X)=-aX^3-cX-d`.

There are two acceptable routes:

1. apply a published generic dynatomic monodromy theorem whose hypotheses explicitly cover this two-parameter family; or
2. prove the cycle monodromy and root-marking kernel directly by specialization, branch cycles, and Kummer independence, following the completed cubic-factor programme.
