# Ordinary Hasse--Witt cofactor indicator

**Date:** 2026-07-21  
**Status:** exact unconditional theorem over `F_p` for every member with `d!=0`.

## 1. Full ordinary Hasse--Witt matrix

Let

`F(X)=X^p+aX^3+cX+d`,

where `p>=5`, `a!=0`, and `d!=0`. Define the full `p x p` coefficient matrix

`H(F)_(u,v)=[X^(pu-v)]F(X)^(p-1)`, `1<=u,v<=p`.

The last row is

`(0,...,0,1)`

because `deg F^(p-1)=p(p-1)`. Thus

`H = [[B,b],[0,1]]`,

where B is the interior `(p-1)x(p-1)` Hasse--Witt matrix and

`b_u=[X^(p(u-1))]F^(p-1)`.

Consequently

`I-H = [[I-B,-b],[0,0]]`.

## 2. Cartier interpretation

Consider the rational differentials

`omega_v=X^(v-1)dX/F(X)`, `1<=v<=p`.

In characteristic p,

`omega_v=X^(v-1)F^(p-1)dX/F^p`.

The Cartier operator selects exponents congruent to `-1 mod p`. Hence

`C(omega_v)=sum_u H_(u,v) omega_u`.

So H is the Cartier matrix on this p-dimensional simple-pole space.

Assume first that F is squarefree, with nonzero roots `alpha_1,...,alpha_p`. Let

`E_(i,u)=alpha_i^(u-1)/F'(alpha_i)`.

Partial fractions identify E with the residue isomorphism. Cartier permutes the residue coordinates by arithmetic Frobenius, so

`E H=P E`

(up to replacing P by its inverse, which has the same orbit decomposition and adjugate at one), where P is the Frobenius permutation of the roots.

Two exact normalizations follow from Lagrange interpolation. Put

`r_u=u f_u`,

where `F=sum_(u=0)^p f_u X^u`. Then

`E r=1`,

because the numerator is `F'(alpha_i)`. Also

`1^T E=e_p^T`,

because

`sum_i alpha_i^k/F'(alpha_i)=0` for `0<=k<=p-2`,

and equals one for `k=p-1`.

For the cubic slice,

`r=(c,0,3a,0,...,0)^T`

inside `F_p^p`; the last coordinate `p f_p` vanishes.

## 3. The selected cofactor

If F is irreducible, P is one p-cycle. For a directed p-cycle,

`adj(I-P)=1 1^T`.

Conjugating by E gives

`adj(I-H)=r e_p^T`.

Therefore the adjugate entry in row 3, column p is

`adj(I-H)_(3,p)=r_3=3a`.

This adjugate entry is the cofactor obtained by deleting row p and column 3.

If F has at least two distinct irreducible factors, the fixed space of Frobenius has dimension at least two, so `rank(I-H)<=p-2` and every `(p-1)`-cofactor vanishes.

A degree-p polynomial with only one distinct factor but not irreducible would have to be `(X-r)^p`. This cannot occur because `a!=0`.

The same conclusion therefore holds for singular members as well: either F is irreducible, or `I-H` has corank at least two.

## 4. Exact theorem

### Theorem OHC.1

For every prime `p>=5`, every `a!=0`, every `c in F_p`, and every `d in F_p^*`,

`boxed(Cofactor_(p,3)(I-H(F))=3a * 1_(F irreducible).)`

Equivalently, because of the block form of H,

`Cofactor_(p,3)(I-H)=e_3^T adj(I-B)b`.

Thus

`boxed(1_(F irreducible)=(3a)^(-1)e_3^T adj(I-B)b.)`

This is a purely mod-p ordinary Hasse--Witt indicator. It requires neither `Beta_(p^2)` nor a p-adic lift.

## 5. Relation to the higher Hasse--Witt route

The boundary-Witt calculation gave

`adj(B(I-B))w=K r`,

with `w=Bb`. The universal adjugate identity

`adj(B(I-B))B=det(B)adj(I-B)`

then reduces the higher indicator to the selected ordinary cofactor. On an irreducible member `det(B)=1`; on reducible members the cofactor vanishes. Hence the p-adic construction collapses exactly to Theorem OHC.1.

The higher calculation was therefore not wasted: it exposed the correct missing boundary column b and selected cofactor.

## 6. Crown reformulation

Every irreducible member has `d!=0`. Therefore

`3a N_a(p)=sum_(c in F_p,d in F_p^*) Cofactor_(p,3)(I-H(F))`.

The d=1 function-field crown follows from nonvanishing of this one explicit cofactor sum for at least one square class of a.

The matrix entries involve only coefficients of the single four-term power `F^(p-1)`. This is materially simpler than:

- iterating Frobenius modulo F in the Berlekamp determinant;
- expanding all dynatomic periods;
- computing `Beta_(p^2)` or a first-Witt correction.

## 7. Verification

Exhaustive direct calculations at `p=5,7` verify the cofactor pointwise for every `a!=0`, every c, and every `d!=0`, including singular members. The cofactor is always exactly `3a` on irreducibles and zero otherwise.
