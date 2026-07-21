# General Cartier cofactor theorem in prime degree

**Date:** 2026-07-21  
**Status:** exact unconditional theorem.

## 1. Setup

Let `p` be prime and let

`F(X)=X^p+sum_(j=0)^(p-1) f_j X^j`

be monic over `F_p`. Define the full `p x p` Cartier coefficient matrix

`H(F)_(u,v)=[X^(pu-v)]F(X)^(p-1)`, `1<=u,v<=p`.

For `1<=j<=p-1`, let `C_j(F)` be the cofactor of `I-H(F)` obtained by deleting row p and column j.

Exclude only the pure inseparable family `F=X^p-s`; this exception is necessary because it has one distinct factor but is not irreducible, and its selected cofactors need not vanish.

## 2. Statement

### Theorem GCC.1

If `F` is not of the form `X^p-s`, then for every `1<=j<=p-1`,

`boxed(C_j(F)=j f_j * 1_(F irreducible).)`

All identities are in `F_p`.

## 3. Proof on the squarefree locus

Use the differential basis

`omega_v=X^(v-1)dX/F(X)`, `1<=v<=p`.

Cartier has matrix H in this basis. If the roots are `alpha_i`, the residue matrix

`E_(i,u)=alpha_i^(u-1)/F'(alpha_i)`

conjugates H to the Frobenius permutation P on the roots.

Put

`r=(f_1,2f_2,...,(p-1)f_(p-1),0)^T`.

Lagrange interpolation gives

`Er=1`, `1^T E=e_p^T`.

If F is irreducible, P is one p-cycle and

`adj(I-P)=1 1^T`.

Therefore

`adj(I-H)=r e_p^T`.

Its `(j,p)` entry is `j f_j`, which is exactly the cofactor deleting row p and column j.

If squarefree F is reducible, Frobenius has at least two root orbits. Hence `I-P`, and therefore `I-H`, has corank at least two, so every `(p-1)`-cofactor is zero.

## 4. Singular members

Write

`F=product_i h_i^(e_i)`

with distinct monic irreducibles `h_i`. Each logarithmic differential

`d h_i/h_i`

belongs to the displayed p-dimensional Cartier space and is fixed by Cartier. Distinct factors give linearly independent fixed differentials. Thus if F has at least two distinct factors, `I-H` has corank at least two and every selected cofactor vanishes.

Because p is prime, a nonirreducible degree-p polynomial with only one distinct factor must be `(X-r)^p=X^p-r^p`. These are exactly the excluded pure inseparable polynomials.

This proves the theorem.

## 5. Cubic-slice consequences

For

`F_(a,c,d)=X^p+aX^3+cX+d`, `a!=0`,

the pure inseparable exception is impossible. The only nonzero interior coefficient vectors are

`f_1=c`, `f_3=a`.

Hence pointwise on the complete coefficient plane,

`boxed(C_1(F)=c * 1_(F irreducible),)`

`boxed(C_3(F)=3a * 1_(F irreducible).)`

The second identity is the ordinary Hasse--Witt crown indicator. The first gives the exact weighted coefficient identity

`sum_(c,d) C_1(F)=sum_(F irreducible) c`.

Equivalently, if `C_3(a;c,d)` denotes the canonical polynomial function of the constant cofactor indicator, finite-field orthogonality gives

`[c^(p-2)d^(p-1)] C_3^can = 3a sum_(F irreducible)c`.

Thus any nonvanishing theorem for the first coefficient moment also proves existence, while potentially involving a less extreme canonical coefficient than the unweighted count.

## 6. Full cubic family and translation

For the full family

`X^p+aX^3+bX^2+cX+d`,

Theorem GCC.1 also gives

`C_2(F)=2b * 1_(F irreducible)`.

Translation `X->X+t` acts freely on b by `b->b+3at`, and every translation orbit has a unique depressed representative `b=0`. Consequently

`N_a(p)=-sum_(b,c,d) b^(p-1) 1_(F irreducible) mod p`

and, using the column-two cofactor,

`N_a(p)=-(1/2)sum_(b,c,d) b^(p-2) C_2(F) mod p`.

This three-variable weighted cofactor is exactly equivalent to the depressed-slice crown. It may be useful because complete orthogonality in all lower cubic coefficients is available, although no simplification is asserted yet.
