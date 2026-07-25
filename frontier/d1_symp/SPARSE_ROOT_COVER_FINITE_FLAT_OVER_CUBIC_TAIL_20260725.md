# Sparse ordered-root cover is finite flat over the cubic tail

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** algebraic support of the residual Smith-defect/q-line object.  
**Status:** all finite-flatness and separable-torsor statements below are **PROVED**. The integral Fourier/Smith comparison remains **OPEN**.

## 1. Universal ordered-root map

Let `k` be a field of characteristic `p` and put

\[
R=k[x_1,\ldots,x_p].
\]

Let `e_i` be the elementary symmetric polynomials. The coefficient map for the universal monic polynomial is

\[
\pi:\mathbf A^p_x\longrightarrow\mathbf A^p_e,
\qquad
(x_1,\ldots,x_p)\longmapsto(e_1,\ldots,e_p).
\]

The invariant ring is

\[
R^{S_p}=k[e_1,\ldots,e_p].
\]

## 2. Integral Artin basis

### Theorem 2.1

The polynomial ring `R` is a free module of rank `p!` over `k[e_1,...,e_p]`.

One basis is the Artin monomial set

\[
\boxed{
\mathcal B=
\left\{
 x_2^{a_2}x_3^{a_3}\cdots x_p^{a_p}:
0\le a_i<i
\right\}.
}
\]

Its cardinality is

\[
\prod_{i=2}^{p}i=p!.
\]

### Proof

The classical straightening algorithm for symmetric polynomials is integral: every monomial can be reduced, using the monic relations supplied successively by the elementary symmetric functions, to a unique linear combination of the displayed monomials with coefficients in `Z[e_1,...,e_p]`. Equivalently, the same monomials form the standard integral basis of the coinvariant algebra after setting the positive-degree symmetric functions to zero.

Base change from `Z` to `k` preserves the basis and gives the stated freeness in every characteristic, including characteristic `p` dividing `|S_p|`. \(\square\)

Consequently, the universal coefficient map `pi` is finite flat of degree `p!`. No semisimplicity of the symmetric-group action is used.

## 3. Sparse power sums equal sparse coefficients

Put

\[
s_m=\sum_{i=1}^{p}x_i^m.
\]

For `m<p`, Newton's identities give

\[
m e_m
=
\sum_{j=1}^{m}(-1)^{j-1}e_{m-j}s_j.
\]

Since `1,...,p-4` are units in `k`, induction gives equality of ideals

\[
\boxed{
(s_1,s_2,\ldots,s_{p-4})
=
(e_1,e_2,\ldots,e_{p-4})
\subset R.
}
\]

Therefore

\[
R_{sparse}
:=
R/(s_1,\ldots,s_{p-4})
\cong
R/(e_1,\ldots,e_{p-4}).
\]

## 4. Finite flatness over the cubic-tail space

Tensor the free `k[e_1,...,e_p]`-module `R` with

\[
k[e_1,\ldots,e_p]/(e_1,\ldots,e_{p-4})
\cong
k[e_{p-3},e_{p-2},e_{p-1},e_p].
\]

Freeness is preserved. Hence:

### Theorem 4.1

\[
\boxed{
R_{sparse}
\text{ is finite free of rank }p!
\text{ over }
 k[e_{p-3},e_{p-2},e_{p-1},e_p].
}
\]

Using

\[
A=e_{p-3},
\qquad
B=-e_{p-2},
\qquad
C=e_{p-1},
\qquad
D=-e_p,
\]

the base is exactly the coefficient space of

\[
T^p+AT^3+BT^2+CT+D.
\]

Thus the affine ordered-root scheme of the sparse family is finite flat of degree `p!` over the full four-dimensional cubic-tail coefficient space.

## 5. Separable locus

Let

\[
\Delta=\prod_{i<j}(x_i-x_j)^2
\]

be the discriminant. After inverting `Delta`, the roots are pairwise distinct. The Jacobian determinant of the coefficient map is, up to sign, the Vandermonde product

\[
\prod_{i<j}(x_i-x_j),
\]

which is invertible there. Hence the restricted map is finite étale.

The symmetric group acts freely on the ordered roots and permutes every geometric fibre simply transitively. Therefore:

\[
\boxed{
\operatorname{Spec}R_{sparse}[\Delta^{-1}]
\longrightarrow
\operatorname{Spec}k[A,B,C,D,\Delta^{-1}]
}
\]

is an `S_p`-torsor of degree `p!`.

This remains true although `p` divides `|S_p|`; freeness of the geometric action and invertibility of the Vandermonde, not Maschke semisimplicity, are the relevant facts.

## 6. Consequences for the Smith-defect programme

The sparse restriction introduces no hidden algebraic pathology:

1. there are no embedded components created by the equations `s_1,...,s_(p-4)`;
2. there is no excess or varying fibre dimension over the cubic-tail coefficient space;
3. the ordered-root cover has the expected constant rank `p!` everywhere;
4. all failure of étaleness is confined to the discriminant divisor;
5. on the separable open, the alternating-hook local system is the ordinary representation-theoretic local system of this exact `S_p`-torsor.

Combined with the Pascal-pairing and residual-tail theorems, this proves that the algebraic target after clean Fourier elimination is exactly the existing cubic coefficient/q-line family, not a derived thickening or an auxiliary cover.

## 7. What remains genuinely cohomological

Finite flatness does not imply that the integral Fourier transform through the nonsplit modular Jordan filtration is clean. The remaining obstruction is entirely in:

- wild ramification at infinity;
- extension data in the cyclic Smith filtration;
- Frobenius on the characteristic-zero defect complex;
- the discriminant and quotient boundary cones already isolated in the arithmetic ledger.

There is no remaining flatness or coefficient-space ambiguity.

## 8. Ruling

### PROVED

- `k[x_1,...,x_p]` is free of rank `p!` over the symmetric coefficient ring in characteristic `p`;
- the sparse power-sum ideal equals the first `p-4` coefficient ideal;
- the sparse ordered-root scheme is finite flat of rank `p!` over `(A,B,C,D)`;
- its separable open is an exact `S_p`-torsor.

### OPEN

- clean integral Fourier/Smith elimination;
- wild-infinity Frobenius control;
- the crown.

The residual programme is now purely cohomological and arithmetic. Algebraic non-flatness is ruled out.
