# Higher Hasse--Witt indicator for the cubic slice

**Date:** 2026-07-21  
**Status:** exact indicator theorem proved on the squarefree ordinary locus, conditional only on the standard Dwork--Vlasenko congruence identifying the unit-root Frobenius matrix modulo `p^2`. A stronger extension to singular members is computationally supported but not asserted as theorem.

## 1. Setup

Let

`F(X)=X^p+aX^3+cX+d`,

where `p>=5` is prime and `a!=0` in `F_p`. Use the canonical integer lifts of `a,c,d` in `{0,...,p-1}` and regard F as a polynomial over `Z_p`.

For every positive integer m define the `(p-1) x (p-1)` coefficient matrix

`Beta_m(F)_(u,v) = [X^(m u-v)] F(X)^(m-1)`,

with `1<=u,v<=p-1`.

Write

`B=Beta_p(F)`,

`B2=Beta_(p^2)(F)`.

All matrix congruences below are taken over `Z/p^2 Z` unless stated otherwise.

## 2. Dwork approximation

For a squarefree member with `d!=0`, the zero-dimensional hypersurface `F=0` lies in `G_m` and its reduced unit-root crystal has rank `p-1`. The standard higher Hasse--Witt congruence gives its Frobenius matrix `Phi_red` modulo `p^2` as

`Phi_red = B2 B^(-1) mod p^2`.

The orientation may be transposed or inverted under alternative Cartier conventions, but the characteristic polynomial and its value at one are unchanged.

If

`F=product_i h_i`

is squarefree with factor degrees `d_i`, then

`det(1-T Phi_red)=product_i(1-T^(d_i))/(1-T)`.

At `T=1` this equals

- `p` if F is irreducible of degree p;
- `0` if F has at least two factors.

Therefore

`det(I-B2 B^(-1)) = p 1_(F irreducible) mod p^2`.

Multiplying by `det(B)` gives

`det(B-B2)=p det(B) 1_(F irreducible) mod p^2`.

On an irreducible degree-p member, Frobenius is a p-cycle. Since p is odd, its determinant on the reduced permutation representation is `+1`. Hence

`det(B)=1 mod p`

on the irreducible locus. On the reducible locus the right side is zero.

## 3. Exact indicator theorem

### Theorem HHW.1

For every squarefree member with `d!=0`,

`boxed( det(Beta_p(F)-Beta_(p^2)(F))/p = 1_(F irreducible) mod p ).`

The determinant is always divisible by p.

Every locally admissible member is squarefree and has `d!=0`. Consequently the theorem applies on the complete local-admissibility set used by the Fortune programme.

This is a second exact irreducibility indicator, independent in construction from the reduced Berlekamp cofactor

`J_a(c,d)/(3a)=1_(F irreducible)`.

On the locally admissible set,

`J_a(c,d)/(3a) = det(Beta_p-Beta_(p^2))/p mod p`.

### Singular members

Exhaustive computation at `p=5,7` finds the same formula for every non-squarefree member as well: the determinant difference is always `0 mod p^2`. A plausible explanation is that modulo p

`Beta_(p^2)=Beta_p^2`,

and the singular Frobenius has independent zero- and one-eigenspace directions, forcing corank at least two in `Beta_p(I-Beta_p)`. A publication-level extension requires an explicit comparison between the singular Hasse--Witt matrix and Frobenius on the non-etale algebra. Until that comparison is written, the non-squarefree extension is recorded as a verified conjectural strengthening, not part of Theorem HHW.1.

## 4. Sparse first-Witt correction

Put

`E_F(X)=(F(X)^p-F(X^p))/p`.

This is an integral polynomial. It is the first p-typical Witt carry of the four monomials of F, together with the Fermat-quotient terms arising from the chosen coefficient lifts.

Using

`F^(p^2-1)=F^(p-1)(F^p)^(p-1)`

and

`F^p=F(X^p)+p E_F`,

one obtains modulo `p^2`

`F^(p^2-1) = F^(p-1)F(X^p)^(p-1)`
`               +p(p-1)F^(p-1)F(X^p)^(p-2)E_F`.

The first term gives exactly the matrix product `B^2`. Define the matrix Gamma over `F_p` by

`Gamma_(u,v)=(p-1)[X^(p^2 u-v)]`
`             F(X)^(p-1) F(X^p)^(p-2) E_F(X)`.

Then

`boxed( Beta_(p^2)=Beta_p^2+p Gamma mod p^2 ).`

Thus the indicator is determined entirely by:

1. the ordinary Hasse--Witt matrix B, whose entries come from the four-term power `F^(p-1)`;
2. one explicit first-Witt correction Gamma;
3. one `(p-1)x(p-1)` determinant modulo `p^2`.

No extension-field factorisation and no growing-period inclusion--exclusion appears in this formula.

## 5. Crown reformulation

On the locally admissible set define

`K_a(c,d)=det(Beta_p(F)-Beta_(p^2)(F))/p mod p`.

Then

`K_a(c,d)=1_(F irreducible)`

pointwise. Consequently

`N_a(p) = sum_(H_(a,c,d) rootless) K_a(c,d) mod p`,

where

`H_(a,c,d)(X)=aX^3+(c+1)X+d`.

The d=1 function-field crown follows if, for at least one square class of a,

`sum_(H rootless) K_a(c,d) !=0 mod p`.

This is a higher Hasse--Witt version of the determinant top-coefficient target. Its advantage is that every entry is an explicit coefficient of a power of a four-term polynomial, and the only genuinely p-adic information is the first Witt carry `E_F`.

## 6. Verification

The standard-library checker `higher_hasse_witt_indicator_check.py` exhaustively verifies Theorem HHW.1 for every squarefree member with `d!=0` at

- `a!=0`, `c,d in F_5`;
- `a!=0`, `c,d in F_7`.

It independently tests irreducibility using the prime-degree Rabin criterion. It also records, separately, that the same determinant identity holds on every singular member in these two characteristics.

Observed total irreducible counts over all nonzero a are:

- `20` at `p=5`;
- `54` at `p=7`.

For every squarefree tested member the determinant difference is `p mod p^2` on the irreducible locus and `0 mod p^2` elsewhere.

## 7. Next exact target

Expand the determinant only to first order in the Witt correction:

`Beta_p-Beta_(p^2)=B(I-B)-p Gamma`.

The crown-level calculation is now to evaluate

`sum_(H rootless) (1/p) det(B(I-B)-p Gamma) mod p`

without expanding the full determinant polynomial. The plausible mechanisms are:

1. Cauchy--Binet/minor expansion using the sparse coefficient support of B and Gamma;
2. finite-field orthogonality in c and d before the determinant sum;
3. a matrix-tree interpretation of the first-order determinant around the unipotent Frobenius block;
4. a Witt-vector resultant or constant-term formula.

Unlike the earlier scalar character sums, this object genuinely contains the first p-adic Frobenius correction and is not merely a repackaging of the integer count.