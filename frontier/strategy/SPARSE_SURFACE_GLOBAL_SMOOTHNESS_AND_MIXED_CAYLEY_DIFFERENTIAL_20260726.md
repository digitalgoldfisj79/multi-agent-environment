# Global smoothness of the sparse surface and the mixed Cayley differential

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** aggregate `h=4` Betti programme for function-field Fortune at `d=1`.  
**Status:** the global smoothness theorem, Lefschetz concentration and tensor-product no-go below are **PROVED**. The identification of the full equivariant Dwork/Jacobian complex with Sawin's Betti complexes uses the standard Cayley trick and remains the active comparison theorem.

## 0. Setup

Let `p>=11` be prime and work over an algebraic closure `k` of `F_p`. Put

\[
s_m(x)=\sum_{i=1}^p x_i^m,
\qquad
H=\{s_1=0\}\subset\mathbf A^p,
\qquad
L=k(1,\ldots,1)\subset H,
\]

and

\[
W=H/L.
\]

The projective sparse ordered-root surface is

\[
Y_p=
\{s_2=s_3=\cdots=s_{p-4}=0\}
\subset\mathbf P(W).
\]

It is a complete intersection of multidegree

\[
(2,3,\ldots,p-4)
\]

in

\[
\mathbf P(W)\cong\mathbf P^{p-3},
\]

so its expected dimension is two.

## 1. The affine singular locus is exactly the diagonal

Consider the affine cone

\[
\widetilde Y_p
=
\{s_1=s_2=\cdots=s_{p-4}=0\}
\subset\mathbf A^p.
\]

At a point `x=(x_1,...,x_p)`, the Jacobian of the displayed equations is, after multiplying rows by units,

\[
J(x)=\left(x_i^{m-1}\right)_{
1\le m\le p-4,\ 1\le i\le p}.
\]

Let

\[
\alpha_1,\ldots,\alpha_r
\]

be the distinct coordinate values of `x`, with positive multiplicities

\[
n_1,\ldots,n_r,
\qquad
\sum_j n_j=p.
\]

The truncated Vandermonde matrix has rank

\[
\min(r,p-4).
\]

Hence a Jacobian-rank failure can occur only if

\[
r\le p-5.
\]

Since `x` lies on the sparse cone,

\[
\sum_{j=1}^r n_j\alpha_j^m=0
\qquad(1\le m\le p-4).
\]

The equation for `m=0` also holds in `F_p`:

\[
\sum_j n_j=p=0.
\]

Use the first `r` moment equations `m=0,...,r-1`. Their coefficient matrix is the invertible Vandermonde matrix

\[
(\alpha_j^m)_{
0\le m\le r-1,\ 1\le j\le r}.
\]

Therefore

\[
n_j=0\quad\text{in }\mathbf F_p
\]

for every `j`.

If `r>=2`, every multiplicity satisfies `1<=n_j<p`, a contradiction. Thus `r=1`, and then the sole multiplicity is `p`. Hence every coordinate is equal.

Conversely, the diagonal line `L` lies in the cone and the Jacobian has rank one there. Therefore:

### Theorem 1.1

\[
\boxed{
\operatorname{Sing}(\widetilde Y_p)=L.
}
\]

No collision pattern with at least two distinct root values is singular.

## 2. The projective sparse surface is smooth everywhere

The power sums descend through the translation quotient by `L`. The affine quotient cone in `W` has singular locus only at its vertex, the image of `L`. Projectivization removes that vertex.

### Theorem 2.1

\[
\boxed{
Y_p\subset\mathbf P^{p-3}
\text{ is a smooth complete-intersection surface.}
}
\]

This strengthens the previous Jacobian audit, which only asserted transversality on the separable locus. In particular, collision points on `Y_p` are smooth points of the complete intersection.

The discriminant remains a boundary divisor for the ordered-root torsor, but it is not a singular locus of the ambient sparse surface.

## 3. Lefschetz concentration

Weak Lefschetz for a smooth complete-intersection surface gives

\[
H^1(Y_p,\mathbf Q_\ell)=H^3(Y_p,\mathbf Q_\ell)=0,
\]

and

\[
H^2(Y_p,\mathbf Q_\ell)
=
\mathbf Q_\ell(-1)\oplus H^2_{\mathrm{prim}}(Y_p,\mathbf Q_\ell).
\]

The symmetric group acts trivially on

\[
H^0,
\quad
\mathbf Q_\ell(-1)\subset H^2,
\quad
H^4.
\]

Therefore:

### Corollary 3.1

For every nontrivial irreducible characteristic-zero representation `rho` of `S_p`,

\[
\boxed{
\operatorname{Hom}_{S_p}
\left(\rho,H^*(Y_p,\mathbf Q_\ell)\right)
=
\operatorname{Hom}_{S_p}
\left(\rho,H^2_{\mathrm{prim}}(Y_p,\mathbf Q_\ell)\right)[-2].
}
\]

Thus there is no cancellation between different projective cohomological degrees in any nontrivial hook sector. The relevant compactified hook multiplicities are concentrated in one primitive middle group.

## 4. The exact mixed Cayley differential

Introduce one multiplier `lambda_m` for every equation `s_m`, and define the Cayley phase

\[
\mathscr F(x,\lambda)
=
\sum_{m=2}^{p-4}\lambda_m s_m(x).
\]

Its Jacobian equations are

\[
\boxed{
\frac{\partial\mathscr F}{\partial\lambda_m}
=s_m(x)
}
\]

and

\[
\boxed{
\frac{\partial\mathscr F}{\partial x_i}
=
\sum_{m=2}^{p-4}m\lambda_mx_i^{m-1}.
}
\]

The first family is the regular-sequence restriction. The second family is the **mixed root--frequency differential**. It couples the coefficient/Jordan filtration to the root configuration and has no analogue in the raw full-configuration-space quantum-bar complex.

The standard Cayley trick and the Adolphson--Sperber Jacobian/Dwork complex compute primitive complete-intersection cohomology from the Koszul complex of these two families. In the present programme, the exact comparison still to be constructed is the `S_p`-equivariant, parity-separated identification of that cohomology with the appropriate non-top pieces of Sawin's interval complexes.

## 5. Why the scalar oscillator cannot be an external tensor factor

Let `B` be any finite complex carrying the raw hook/bar multiplicity data, and let `O` be the scalar terminal oscillator complex with two one-dimensional homology groups in adjacent degrees.

If the proposed sparse associated graded were the external tensor product

\[
B\otimes O
\]

with differential

\[
d_B\otimes1+1\otimes d_O,
\]

then Kunneth gives

\[
H^*(B\otimes O)
\cong
H^*(B)\otimes H^*(O).
\]

Consequently

\[
\boxed{
\sum_i\dim H^i(B\otimes O)
=2\sum_i\dim H^i(B).
}
\]

It cannot reduce unsigned Betti mass.

At `p=13`, hook degrees `3,4,5,6` already supply `17` multiplicity-one non-sign terminal classes. An external oscillator factor would produce at least `34`, whereas the multiplicity-one Sawin budget is `12`.

### Theorem 5.1 — tensor-product oscillator no-go

\[
\boxed{
\text{The sparse Betti comparison cannot be a scalar Pascal oscillator}
\text{ tensored independently with the raw hook/bar complex.}
}
\]

Any successful Rees/Dwork model must retain the mixed derivatives

\[
\sum_m m\lambda_mx_i^{m-1}
\]

and use them to create genuine differentials inside the hook multiplicity complexes.

## 6. Exact support of the missing cancellation

The following are already proved:

1. the sparse section is smooth, now globally;
2. local vanishing cycles of the regular sequence vanish on the smooth section;
3. the global Fourier delta identity imposes the equations exactly;
4. every nonzero Fourier phase has no finite critical point on the degree-`p` root locus;
5. the ordered-root map is finite flat;
6. modular Smith contraction alone does not control characteristic-zero unsigned mass.

Therefore the mixed Cayley differential can contribute to the load-bearing hook cancellation only through the compactified critical locus:

- root infinity in the nonzero-frequency family;
- the discriminant/open-boundary complex;
- the exceptional coefficient charts `q=0,2,infinity` and their quotient cones.

The `p=13` exact bar classes provide a hard regression: the boundary mixed complex must kill at least five non-sign multiplicity-one classes from hook degrees `3` through `6`.

## 7. Revised active theorem

> **Equivariant mixed-Cayley cancellation theorem.** Construct the `S_p`-equivariant Dwork/Jacobian complex of the Cayley phase `mathscr F`, compactify it at root and frequency infinity, and separate the even and odd hook multiplicity complexes before taking Euler classes. Prove that the mixed root--frequency differential and boundary maps reduce the surviving non-top multiplicity-one hook mass to at most `p-1` for primes `p congruent 5 mod 6`. The construction must reproduce the exact sign trace, pass the `p=11` sign regression, and kill at least five known non-sign classes in the `p=13` regression.

This is narrower than the former wild Rees statement: the algebraic differential is now explicit. The open work is its compactified cohomology and Frobenius action.

## 8. Verification

`global_sparse_smoothness_verify.py` checks:

1. the multiplicity/Vandermonde singularity argument for every prime through `499`;
2. exhaustive Jacobian ranks over `F_p` at the feasible primes `p=5,7`;
3. the complete-intersection dimension and Chern-class arithmetic;
4. the tensor-product dimension no-go against the exact `p=13` profile.
