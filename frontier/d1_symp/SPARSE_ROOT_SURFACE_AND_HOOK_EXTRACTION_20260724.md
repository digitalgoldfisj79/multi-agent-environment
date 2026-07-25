# Sparse root surface and exact hook extraction

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling; the nested-section theorem assumes `p=5 mod 6` and `p>=11`. The prime `p=5` is a separate proved base case.  
**Status:** the sparse-root construction, irreducibility hook extraction and ambient hook-multiplicity identity below are **PROVED**. The correct remaining comparison is the global Fourier--Cayley theorem in `SPARSE_JACOBIAN_AND_FOURIER_CAYLEY_CORRECTION_20260724.md`. A local iterated-vanishing-cycle bridge at the smooth sparse zero section is **CLOSED**.

## 0. Exact geometric diagram

For every half-theorem prime `p>=11`:

- the Airy virtual module is an alternating hook multiplicity in the primitive cohomology of the smooth cyclic `(2,3)` complete intersection;
- the sparse ordered-root surface is obtained inside that complete intersection by imposing

\[
s_4=s_5=\cdots=s_{p-4}=0;
\]

- its separable quotient carries the alternating hook local system whose trace is exactly `p` times the irreducibility indicator.

The source and target of the application theorem are therefore explicit alternating-hook objects in one power-sum geometry.

## 1. Ambient ordered-root complete intersection

Over `kbar=Fbar_p`, let

\[
H=\{(x_1,\ldots,x_p):s_1=0\},
\qquad
L=kbar(1,\ldots,1),
\qquad
W=H/L,
\]

where

\[
s_j=\sum_{i=1}^p x_i^j.
\]

The ambient projective variety is

\[
X_p=\{s_2=s_3=0\}\subset\mathbf P(W).
\]

It is the smooth `(2,3)` complete intersection used in the full Airy--primitive Weil bridge.

## 2. Successive power sums descend through translation

For a diagonal translation `x_i -> x_i+c`,

\[
s_m(x+c)
=
\sum_{j=0}^m
\binom mj c^{m-j}s_j(x).
\]

In characteristic `p`, `s_0=p=0`. On

\[
s_1=s_2=\cdots=s_{m-1}=0,
\]

the function `s_m` is therefore invariant under diagonal translation and descends successively through the quotient by `L`.

For `3<=m<=p-4`, define

\[
X_p^{(m)}
=
\{s_2=s_3=\cdots=s_m=0\}
\subset\mathbf P(W).
\]

For `p>=11`,

\[
X_p=X_p^{(3)}
\supset X_p^{(4)}
\supset\cdots\supset X_p^{(p-4)}.
\]

Put

\[
Y_p=X_p^{(p-4)}.
\]

It is cut out inside `X_p` by the `p-7` additional power sums `s_4,...,s_{p-4}`.

## 3. Newton identities identify the sparse family

Let

\[
P_x(Z)=\prod_{i=1}^p(Z-x_i)
=Z^p-e_1Z^{p-1}+e_2Z^{p-2}-\cdots+(-1)^pe_p.
\]

For `m<p`,

\[
m e_m
=
\sum_{j=1}^m(-1)^{j-1}e_{m-j}s_j.
\]

Since `1,...,p-4` are invertible,

\[
s_1=\cdots=s_{p-4}=0
\quad\Longleftrightarrow\quad
e_1=\cdots=e_{p-4}=0.
\]

Thus the affine ordered-root locus above `Y_p` consists exactly of ordered roots of

\[
\boxed{
Z^p+A Z^3+B Z^2+C Z+D.
}
\]

The coefficient map is finite. The sparse coefficient locus has dimension four before diagonal translation and root scaling; the quotient has pure dimension two. Hence `Y_p` is the two-dimensional ordered-root model of the degree-three-offset family.

At `p=5`, the sparse family imposes only `s_1=0`; it contains `X_5` rather than being a deeper section. This explains the exceptional base-case treatment.

## 4. Generic normal form and boundaries

On `A C !=0`, translation removes `B`, and a scalar root change normalizes the cubic and linear terms. The generic split chart is

\[
P_{q,t}(Z)
=qZ^p+Z^3-3Z-(q-2)t.
\]

The square root required by this normalization gives the split and nonsplit arithmetic readings. The omitted loci are exactly:

- `C=0`, or `q=infinity`;
- `q=2`;
- the discriminant fibres `t=+1,-1`;
- degeneration of depression or scaling;
- the arithmetic quadratic descent of the square root.

The exact coefficient and arithmetic-class normalization is proved in `NORMAL_FORM_CELL_LEDGER_20260724.md`.

## 5. Separable ordered-root torsor

Let

\[
Y_p^{sep}\subset Y_p
\]

be the open locus of pairwise distinct roots, and put

\[
\mathcal U_p=Y_p^{sep}/S_p.
\]

The action is free, so

\[
Y_p^{sep}\longrightarrow\mathcal U_p
\]

is the finite etale ordered-root `S_p`-torsor of the separable sparse family modulo translation and scaling.

For

\[
V_i=\bigwedge^i\mathrm{Std},
\qquad0\le i\le p-1,
\]

let `L_i` be the associated local system on `U_p`.

## 6. Exact irreducibility character

Define

\[
\Lambda_p
=
\sum_{i=0}^{p-1}(-1)^iV_i.
\]

For `g in S_p`,

\[
\operatorname{Tr}(g|\Lambda_p)
=
\det(1-g|\mathrm{Std}).
\]

The determinant is zero if `g` has more than one cycle. For one `p`-cycle,

\[
\det(1-g|\mathrm{Std})
=
\prod_{j=1}^{p-1}(1-\zeta_p^j)
=p.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(g|\Lambda_p)
=
\begin{cases}
p,&g\text{ is a }p\text{-cycle},\\0,&\text{otherwise}.
\end{cases}
}
\]

At a finite-field point, Frobenius is a `p`-cycle on the roots exactly when the polynomial is irreducible. The virtual local system

\[
\mathcal L_{hook}
=
\sum_i(-1)^i\mathcal L_i
\]

therefore has trace exactly `p` times the irreducibility indicator.

The geometric sparse hook complex is

\[
\boxed{
\mathcal K_{sparse}
=R\Gamma_c(\mathcal U_p,\mathcal L_{hook}).
}
\]

Equivalently,

\[
\boxed{
\mathcal K_{sparse}
=
\sum_i(-1)^i
R\operatorname{Hom}_{S_p}
\left(
V_i,R\Gamma_c(Y_p^{sep},\mathbf Q_\ell)
\right).
}
\]

The fixed-`q` hook pushforward and q-line assembly are a Leray presentation on the generic normal-form chart. The exact class projector and boundary ledger are given in `HOOK_Q_LINE_CLASS_PROJECTORS_20260724.md`.

## 7. Ambient Airy cohomology is an alternating hook multiplicity

Let

\[
H_p=H^{p-5}_{prim}(X_p,\mathbf Q_\ell)
\]

and

\[
\mathcal K_{ambient}
=
\sum_{i=0}^{p-1}(-1)^i
\operatorname{Hom}_{S_p}(V_i,H_p).
\]

By Murnaghan--Nakayama, an irreducible `S_p` character is zero on a `p`-cycle unless it is the hook `(p-i,1^i)`, when its value is `(-1)^i`. Hence for every `r`,

\[
\operatorname{Tr}(F^r|\mathcal K_{ambient})
=
\operatorname{Tr}(\sigma F^r|H_p)
=
\operatorname{Tr}(F^r|\mathcal D_p).
\]

Thus

\[
\boxed{
\mathcal K_{ambient}^{ss}=\mathcal D_p^{ss}
}
\]

and the full Kummer bridge gives

\[
\boxed{
\mathcal R_p^{ss}
=
\mathcal K_{ambient}(-3)^{ss}.
}
\]

## 8. Smoothness correction

The Jacobian of `s_1,...,s_m` is a truncated Vandermonde matrix. It has rank `m` whenever the tuple has at least `m` distinct coordinates. Therefore every stage of the nested sparse section is transverse on `Y_p^{sep}`.

Local vanishing cycles at the zero section vanish throughout the separable locus. They are supported only on the discriminant boundary and cannot equal the load-bearing interior hook complex.

Accordingly, the former local iterated-vanishing-cycle proposal is withdrawn.

## 9. Correct remaining application object

Collect the additional power sums into

\[
S=(s_4,\ldots,s_{p-4})
\]

and introduce dual variables `lambda_m`. Additive orthogonality gives

\[
\mathbf1_{S=0}
=
Q^{-(p-7)}
\sum_\lambda
\psi\left(\sum_m\lambda_m s_m\right).
\]

Sheaf-theoretically, integration of the Artin--Schreier phase over the dual variables is the delta sheaf of the sparse zero section, with the exact Tate and cohomological shifts proved in `SPARSE_JACOBIAN_AND_FOURIER_CAYLEY_CORRECTION_20260724.md`.

Thus the correct application theorem is a global `S_p`-equivariant Fourier--Cayley decomposition. It must isolate

\[
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
=
\mathcal R_p
\left(\frac{p-1}{2}\right)
\]

as the load-bearing pure constituent and identify the complementary Fourier strata with the invariant/quadratic q-line projectors and explicit boundaries.

## 10. Boundary of the result

### PROVED

1. The sparse ordered-root surface and its exact polynomial interpretation.
2. The exact hook irreducibility local system.
3. The ambient Airy module as an alternating hook multiplicity.
4. Smoothness of the sparse section on the separable locus.
5. Closure of the naïve local vanishing-cycle mechanism.
6. Identification of the correct global Fourier--Cayley target.

### OPEN

1. Isolation of the ambient hook constituent inside the Fourier--Cayley complex.
2. Decomposition of complementary Fourier strata into `S_0`, `S_chi`, `q=2`, `q=infinity`, discriminant and punctual terms.
3. The final parity certificate.
4. The separate absolute Airy trace bound.
