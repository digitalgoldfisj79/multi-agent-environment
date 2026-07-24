# Twisted descent and the exact primitive-trace identity for `T_p`

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the descent isomorphism, point-count identity and primitive cohomology trace formula below are **PROVED**. The absolute trace bound and the hook/irreducibility transport remain **OPEN**.

## 0. Main result

Let

\[
k=\mathbf F_p,
\qquad
K=\mathbf F_{p^p},
\qquad
H=\ker(\operatorname{Tr}_{K/k}),
\qquad
W=H/k.
\]

The constant line lies in `H` because `Tr(c)=pc=0` in characteristic `p`.

On `H`, put

\[
Q(x)=\operatorname{Tr}(x^2),
\qquad
C(x)=\operatorname{Tr}(x^3).
\]

The quadratic form descends to `W`. The cubic changes by a multiple of `Q` under translation by constants, so the projective complete intersection

\[
X_p^{\mathrm{AS}}:=\{Q=C=0\}\subset\mathbf P(W)
\]

is well-defined independently of the chosen section of `H\to W`.

For every prime `p>=5`, `X_p^{AS}` is the smooth `(2,3)` complete intersection already proved in `SMOOTH_QUADRIC_CUBIC_REDUCTION.md`, of dimension

\[
m=p-5.
\]

For `p=2 mod 3`, the collapse sum satisfies the exact identities

\[
\boxed{
\#X_p^{\mathrm{AS}}(\mathbf F_p)
=
\#\mathbf P^{p-5}(\mathbf F_p)+\frac{T_p}{p^2}
}
\]

and

\[
\boxed{
T_p
=
p^2\operatorname{Tr}
\left(
\operatorname{Frob}_p
\mid
H^{p-5}_{\mathrm{prim}}
(X_{p,\overline{\mathbf F}_p}^{\mathrm{AS}},\mathbf Q_\ell)
\right).
}
\]

The same geometric variety has a split coordinate model over `Fbar_p`:

\[
X_p^{\mathrm{perm}}
=
\left\{
\sum_i x_i=\sum_i x_i^2=\sum_i x_i^3=0
\right\}
\bigg/
\overline{\mathbf F}_p(1,\ldots,1).
\]

Under the canonical splitting of the Weil restriction, the arithmetic Frobenius of the Artin--Schreier form becomes, up to the harmless cyclic-orientation convention,

\[
\Phi=\sigma\circ\operatorname{Frob}_p
\]

on the permutation model. Therefore

\[
\boxed{
T_p
=
p^2\operatorname{Tr}
\left(
\sigma\operatorname{Frob}_p
\mid
H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{perm}},\mathbf Q_\ell)
\right).
}
\]

This supplies the exact object-level descent and the exact main/Tate subtraction for the smooth linear-section model. It does **not** yet identify this primitive motive with the post-pushforward hook complex controlling irreducible fibres.

## 1. The quotient complete intersection is well-defined

For `x in H` and `c in k`, characteristic `p` gives

\[
Q(x+c)=Q(x)
\]

and

\[
C(x+c)=C(x)+3cQ(x).
\]

Hence `Q` descends as a quadratic form on `W=H/k`. The cubic itself depends on a section, but changing the section replaces `C` by `C+LQ` for a linear form `L`. Thus the homogeneous ideal `(Q,C)` and the complete intersection `X_p^{AS}` are intrinsic.

The descended quadratic form is nondegenerate and `dim W=p-2`. Smoothness of `X_p^{AS}` was proved separately by the trace-pairing/Jacobian argument.

## 2. PROVED: scheme-level twisted descent

Let `kbar` be an algebraic closure of `k`. The finite etale algebra splitting gives the canonical `kbar`-algebra isomorphism

\[
\iota:
K\otimes_k\overline k
\longrightarrow
\overline k^p,
\qquad
z\longmapsto
\bigl(z,z^p,z^{p^2},\ldots,z^{p^{p-1}}\bigr)
\]

on `K`-valued points, extended `kbar`-linearly.

For `r=1,2,3`,

\[
\operatorname{Tr}_{K/k}(z^r)
\longmapsto
\sum_{i=0}^{p-1}x_i^r.
\]

Thus `iota` identifies the base change of the trace-zero hyperplane with

\[
\left\{\sum_i x_i=0\right\}\subset\overline k^p,
\]

identifies the constant line with the diagonal line, and induces an isomorphism

\[
X_p^{\mathrm{AS}}\times_k\overline k
\cong
X_p^{\mathrm{perm}}.
\]

The descent datum is cyclic. If `F` denotes coordinatewise `p`-power Frobenius and `sigma` is the cyclic shift, the splitting map intertwines ordinary Frobenius on the Artin--Schreier form with `sigma F` or `sigma^{-1}F`, according to the ordering of the embeddings. Reversing the coordinate order conjugates `sigma` to `sigma^{-1}` and preserves all three power-sum equations, so the trace is independent of this orientation choice.

This is an isomorphism of descended schemes, not merely an equality of their first fixed-point counts. In particular, for every `r>=1`, the zeta traces of the Artin--Schreier form are the traces of `(sigma F)^r` on the split permutation model.

## 3. PROVED: affine fibre calculation

For `b in k`, define

\[
M_b=
\#\{w\in W(k):Q(w)=0,\ C(w)=b\}.
\]

Translation along the constant line gives the already proved identity

\[
T_p
=
p\sum_{w\in W(k),\ Q(w)=0}
\psi(C(w)).
\]

Assume now `p=2 mod 3`. Cubing is a bijection on `k^*`, and scaling `w\mapsto sw` gives

\[
M_b=M_*
\qquad(b\ne0).
\]

Because `Q` is nondegenerate on the odd-dimensional space `W`, with

\[
\dim W=p-2,
\]

its affine null cone has exactly

\[
\sum_{b\in k}M_b
=
\#\{Q=0\}
=p^{p-3}
\]

points.

The additive character sum is

\[
T_p
=p\left(M_0+M_*\sum_{b\ne0}\psi(b)\right)
=p(M_0-M_*).
\]

Solving

\[
M_0+(p-1)M_*=p^{p-3},
\qquad
M_0-M_*=T_p/p,
\]

gives

\[
\boxed{
M_0=p^{p-4}+\frac{p-1}{p^2}T_p
}
\]

and

\[
\boxed{
M_*=p^{p-4}-\frac1{p^2}T_p.
}
\]

## 4. PROVED: projective point-count identity

The equations are homogeneous. The affine zero solution contributes one point, and each projective point has exactly `p-1` nonzero scalar representatives. Therefore

\[
M_0=1+(p-1)\#X_p^{\mathrm{AS}}(k).
\]

Substitution gives

\[
\#X_p^{\mathrm{AS}}(k)
=
\frac{p^{p-4}-1}{p-1}+\frac{T_p}{p^2}.
\]

Since

\[
\frac{p^{p-4}-1}{p-1}
=
1+p+\cdots+p^{p-5}
=
\#\mathbf P^{p-5}(k),
\]

one obtains

\[
\boxed{
\#X_p^{\mathrm{AS}}(k)-\#\mathbf P^{p-5}(k)
=
\frac{T_p}{p^2}.
}
\]

A first arithmetic consequence is the exact divisibility

\[
\boxed{p^2\mid T_p}
\]

for every `p>=5` with `p=2 mod 3`.

## 5. PROVED: primitive cohomology trace

The dimension

\[
m=p-5
\]

is even. For the smooth complete intersection `X_p^{AS}` of dimension `m`, weak Lefschetz and Poincare duality identify all non-middle cohomology with that of `P^m`. Splitting the middle cohomology into its ambient Tate line and primitive part, the Grothendieck--Lefschetz trace formula gives

\[
\#X_p^{\mathrm{AS}}(k)
-
\#\mathbf P^m(k)
=
\operatorname{Tr}
\left(
\operatorname{Frob}_p
\mid H^m_{\mathrm{prim}}(X_p^{\mathrm{AS}})
\right),
\]

because `(-1)^m=+1`.

Combining with the point-count identity proves

\[
\boxed{
T_p
=
p^2\operatorname{Tr}
\left(
\operatorname{Frob}_p
\mid H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{AS}})
\right).
}
\]

Under twisted descent this is exactly the `sigma Frob_p` primitive trace on the split permutation complete intersection.

## 6. Consequences for the main analytic branch

The target

\[
|T_p|\le C p^{(p-1)/2}
\]

is now exactly equivalent to

\[
\boxed{
\left|
\operatorname{Tr}
\left(
\sigma\operatorname{Frob}_p
\mid H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{perm}})
\right)
\right|
\le C p^{(p-5)/2}.
}
\]

This is a pure weight-`p-5` trace estimate with no hidden main term, Tate line or punctual scalar left to subtract. The factor `p^2` in the Airy sum is exactly the Tate normalization converting the projective primitive trace to `T_p`.

This theorem also makes precise why the bare cyclic fixed scheme is irrelevant: the actual Frobenius of the descended form is the semilinear operator `sigma Frob_p`, whose fixed points are transverse and reconstruct the extension-field trace locus.

## 7. What this closes and what remains

### CLOSED

1. The scheme-level identification between the Artin--Schreier trace model and the cyclic-permutation model.
2. The arithmetic/geometric Frobenius convention, up to conjugate cyclic orientation.
3. The exact projective-space/Tate subtraction.
4. The exact normalization between `T_p` and primitive middle cohomology.
5. The concern that the linear-section model was supported only by a first-trace coincidence.

### STILL OPEN — analytic main branch

Prove the absolute normalized trace bound on the primitive cohomology of this twisted `(2,3)` complete intersection. Its ordinary primitive Betti number grows rapidly with `p`; the theorem must exploit the cyclic descent structure, not a generic complete-intersection estimate.

### STILL OPEN — application main branch

Construct the separate map from this primitive cyclic-Frobenius motive into the zero-frequency/post-pushforward hook complex controlling irreducible fibres, including:

- the `q=2` and `q=infinity` cells;
- the arithmetic quadratic twist at infinity;
- the exact Artin--Schreier and endpoint subtractions;
- the final positivity/certificate implication.

The present theorem closes the Airy-to-linear-section object identification. It does not close the linear-section-to-hook ledger.

## 8. Verification

`twisted_descent_trace_verify.py` checks independently:

1. the explicit Artin--Schreier coordinate formulas for `Q` and `C` at `p=5`;
2. the affine fibre counts `M_b=(5,5,5,5,5)`;
3. the direct projective count `#X_5(F_5)=1`;
4. the formula `#X_p=#P^(p-5)+T_p/p^2` against all committed exact `T_p` values with `p=2 mod 3`;
5. the resulting `p^2` divisibility.

The higher-prime checks verify exact arithmetic consequences of committed exact traces. The scheme-level descent and cohomological formula are proved above and do not rely on the regression script.
