# Maximal monodromy of the quartic dynatomic cover

**Date:** 2026-07-21  
**Status:** the generic arithmetic and geometric period-four Galois groups are proved to be `C_4 wr S_18`.

## 1. Setup

Over characteristic zero, consider the centered cubic family

`g_(a,c,d)(X)=-aX^3-cX-d`, `a != 0`.

After adjoining a square root and scaling X, the leading coefficient may be normalized. The geometric monodromy is therefore equivalent to that of

`g_(c,d)(X)=X^3+cX+d`.

Its fourth dynatomic polynomial is

`Phi_4(X)=[g^4(X)-X]/[g^2(X)-X]`

and has degree

`3^4-3^2=72=4*18`.

The 72 roots are arranged in 18 dynamical cycles of length four. Hence every Galois automorphism must commute with the cycle permutation, and the generic Galois group is a subgroup of the centralizer

`C_4 wr S_18 = C_4^18 semidirect S_18`.

## 2. Unicritical specialization

Set the linear coefficient c equal to zero. Up to a nonzero geometric scaling, the resulting one-parameter family is the unicritical family

`f_t(X)=X^3+t`.

Morton's generic periodic-point theorem, as restated in Bridy--Garton, proves that for

`f_t(X)=X^k+t`

the arithmetic and geometric Galois groups of the nth dynatomic polynomial are

`C_n wr S_(r_k(n))`,

where

`r_k(n)=(1/n) sum_(m|n) k^m mu(n/m)`.

For `k=3`, `n=4`,

`r_3(4)=(3^4-3^2)/4=18`.

Thus the specialized c=0 family has arithmetic and geometric group

`C_4 wr S_18`.

References:

- P. Morton, *Galois Groups of Periodic Points*, J. Algebra 201 (1998), Theorems B and 9;
- A. Bridy and D. Garton, *Dynamically Distinguishing Polynomials*, Res. Math. Sci. 4 (2017), Corollary 2.4 and the discussion following Theorem 2.3.

## 3. Generic group

For a separable specialization, the specialized Galois group embeds into the generic Galois group. The specialized c=0 group is already the full universal upper bound `C_4 wr S_18`.

Therefore the generic group cannot be smaller.

### Theorem QM.1

For the centered two-parameter cubic family, the generic arithmetic and geometric Galois groups of the fourth dynatomic polynomial are

`G_arith = G_geom = C_4 wr S_18`.

## 4. Consequences

The group acts transitively on:

- ordered j-tuples of distinct period-four cycles, for every `0 <= j <= 18`;
- such a j-tuple together with one marked point in every selected cycle.

The marked action has stabilizer index

`j! 4^j`.

Consequently every ordered distinct j-cycle marked fibre power is geometrically integral.

For the complete coefficient slice, Lang--Weil gives the unconditioned quartic factorial moments

`M_(a,4,j)=p^2/(j!4^j)+O(p^(3/2))`

for `0 <= j <= 18`.

To impose local admissibility and degree-p discriminant parity, one must still determine the intersections of the quartic dynatomic splitting field with the local cubic and Kummer quadratic extensions. The maximal dynatomic monodromy itself is now closed.