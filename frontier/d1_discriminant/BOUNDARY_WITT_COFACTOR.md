# Boundary-Witt cofactor formula

**Date:** 2026-07-21  
**Status:** exact algebraic reduction proved; aggregate cofactor evaluation remains open.

## 1. Universal fixed vector

Let

`F(X)=sum_(j=0)^p f_j X^j`, with `f_p=1`,

and define

`r=(r_1,...,r_(p-1))^T`, `r_j=j f_j`.

For

`B_m(u,v)=[X^(mu-v)]F^(m-1)`, `1<=u,v<=p-1`,

coefficient convolution gives the exact integer identity

`(B_m r)_u = u [X^(mu)]F^m - p [X^(mu-p)]F^(m-1)`.

Indeed, the complete Euler numerator is

`X F'(X)=sum_(j=1)^(p-1) j f_j X^j + p X^p`.

The first term on the right comes from

`X F' F^(m-1)=(1/m)X(F^m)'`,

while the omitted leading term contributes the displayed boundary correction.

For `m=p`, reduction modulo p gives

`B_p r=r mod p`.

Thus r is a universal right fixed vector of the ordinary Hasse--Witt matrix.

For the cubic slice

`F=X^p+aX^3+cX+d`,

this vector is exceptionally sparse:

`r=(c,0,3a,0,...,0)^T`.

In particular, its third coordinate is always nonzero because `a!=0` and `p>=5`.

## 2. The boundary-Witt forcing vector

Put

`D=Beta_p-Beta_(p^2)` modulo `p^2`.

Since `D mod p=B(I-B)` and `Br=r mod p`, one has `Dr=0 mod p`. Define

`w=(Dr)/p mod p`.

Applying the exact Euler identity at `m=p` and `m=p^2` gives

`w_u = (u/p)([X^(pu)]F^p-[X^(p^2u)]F^(p^2))`
`      -[X^(p(u-1))]F^(p-1)`
`      +[X^(p^2u-p)]F^(p^2-1) mod p`.

The first line vanishes modulo p. The required coefficient congruence is

`[X^(p^2u)]F^(p^2) = [X^(pu)]F^p mod p^2`.

It follows from the multinomial Jacobsthal congruence: terms of p-adic valuation below two have all occupation numbers divisible by p; the corresponding multinomial coefficients reduce from level `p^2` to level p modulo `p^2`, while the coefficient powers agree to the required precision. All other occupation patterns are divisible by `p^2`.

Therefore

`boxed(w_u=[X^(p^2u-p)]F^(p^2-1)-[X^(p(u-1))]F^(p-1) mod p).`

The forcing vector is exactly the difference between the missing boundary columns `v=p` of the two higher Hasse--Witt levels. No full first-Witt matrix Gamma is required to compute `Dr/p`.

## 3. One-row adjugate indicator

Let

`D0=D mod p=B(I-B)`.

The adjugate identity over `Z/p^2 Z` gives

`adj(D) D r=det(D)r`.

Reducing the adjugate modulo p and dividing by p yields

`adj(D0) w=K_a(c,d) r`,

where

`K_a(c,d)=det(D)/p mod p`.

Since `r_3=3a!=0`, the entire determinant indicator is recovered from one coordinate:

`boxed(K_a(c,d)=(3a)^(-1)(adj(D0)w)_3).`

Equivalently,

`K_a(c,d)=(3a)^(-1) sum_(u=1)^(p-1) Cofactor_(u,3)(D0) w_u`.

This is exact for every `d!=0`; by the singular completion both sides vanish on singular members and equal the irreducibility indicator on squarefree members.

## 4. Structural significance

The higher Hasse--Witt crown is no longer a full `(p-1)x(p-1)` determinant expansion. It is a single cofactor row paired with a boundary-Witt vector. Three features are now explicit:

1. the kernel vector has only the c-column and a-column coordinates;
2. the p-adic forcing comes only from the omitted leading-coefficient boundary column;
3. finite-field summation can be applied to one cofactor row before expanding the remaining coefficients.

The crown target becomes

`sum_(c in F_p,d in F_p^*) sum_u Cofactor_(u,3)(D0) w_u !=0 mod p`

for at least one square class of a.

The next calculation should attack this paired sum by Cauchy--Binet/constant-term methods. Expanding the complete determinant first would discard the boundary sparsity proved here.
