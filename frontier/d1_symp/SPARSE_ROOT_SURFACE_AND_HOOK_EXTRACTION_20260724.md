# Sparse root surface and exact hook extraction

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling; the nested-section theorem below assumes `p=5 mod 6` and `p>=11`. The already proved prime `p=5` is a separate exceptional base case.  
**Status:** the sparse-root construction, irreducibility hook extraction and ambient hook-multiplicity identity below are **PROVED**. The iterated vanishing-cycle comparison from the ambient complete intersection to the sparse surface remains **OPEN**.

## 0. Result

For every half-theorem prime `p>=11`, the source and target of the application theorem lie in one explicit geometric diagram.

- The Airy virtual module is the alternating hook multiplicity in the primitive cohomology of the smooth cyclic `(2,3)` complete intersection.
- The sparse ordered-root surface is obtained inside that complete intersection by imposing

\[
s_4=s_5=\cdots=s_{p-4}=0.
\]

- Its separable quotient carries the exact alternating hook local system whose trace is `p` times the irreducibility indicator.

There are `p-7` additional equations. The required comparison is therefore an iterated vanishing-cycle, or equivalent perverse complete-intersection, theorem across this explicit nested section. Weight compatibility forces the Tate twist `(p-7)/2` on the pure middle term.

At `p=5`, the sparse family only imposes `s_1=0`; it contains the Airy section rather than being cut out inside it. That prime is already proved directly and is excluded from the general nested-section statement.

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

In characteristic `p`, `s_0=p=0`. Consequently, on

\[
s_1=s_2=\cdots=s_{m-1}=0,
\]

the function `s_m` is invariant under diagonal translation. Each next equation therefore descends successively through the quotient by `L`.

For `3<=m<=p-4`, define

\[
X_p^{(m)}
=
\{s_2=s_3=\cdots=s_m=0\}
\subset\mathbf P(W).
\]

For `p>=11`, this gives the nested sequence

\[
X_p=X_p^{(3)}
\supset X_p^{(4)}
\supset\cdots\supset X_p^{(p-4)}.
\]

Put

\[
Y_p=X_p^{(p-4)}.
\]

The additional equations are `s_4,...,s_{p-4}`, exactly `p-7` equations.

## 3. Newton identities identify the sparse polynomial family

Let

\[
P_x(Z)=\prod_{i=1}^p(Z-x_i)
=Z^p-e_1Z^{p-1}+e_2Z^{p-2}-\cdots+(-1)^pe_p.
\]

For `m<p`, Newton's identity is

\[
m e_m
=
\sum_{j=1}^m(-1)^{j-1}e_{m-j}s_j.
\]

Every `1<=m<=p-4` is invertible in the field. Induction gives

\[
s_1=\cdots=s_{p-4}=0
\quad\Longleftrightarrow\quad
e_1=\cdots=e_{p-4}=0.
\]

Hence the affine ordered-root locus above `Y_p` consists exactly of ordered roots of

\[
\boxed{
Z^p+A Z^3+B Z^2+C Z+D.
}
\]

Conversely, every ordered root tuple of such a polynomial satisfies the displayed power-sum equations.

The coefficient map from ordered roots to `(A,B,C,D)` is finite. Before translation and projective scaling, the sparse coefficient locus has dimension four; quotienting the diagonal translation and root scaling directions gives pure dimension two. Thus `Y_p` is the two-dimensional ordered-root model of the degree-three-offset family for `p>=11`.

## 4. Generic normal-form chart and boundaries

On `A C !=0`, translation uniquely removes `B`, because the new quadratic coefficient is `B+3Ac`. A scalar root change then normalizes the cubic and linear terms to `1` and `-3`. Over the base field the required square root produces the split and nonsplit quadratic readings.

The resulting generic chart is

\[
P_{q,t}(Z)
=qZ^p+Z^3-3Z-(q-2)t.
\]

The normalization omits precisely the boundary types already present in the hook ledger:

- `C=0`, corresponding to `q=infinity`;
- the colliding-critical-value cell `q=2`;
- the discriminant fibres `t=+1,-1`;
- degeneration of depression or scaling;
- the arithmetic quadratic descent of the chosen square root.

The chart identifies the existing fixed-`q` root covers with pullbacks of the generic separable ordered-root cover below. Recovering the raw coefficient counts also requires the finite orbit multiplicities and boundary cells already recorded in the ledger.

## 5. Separable ordered-root torsor

Let

\[
Y_p^{sep}\subset Y_p
\]

be the open locus where the coordinates are pairwise distinct, and let

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

If `g` has more than one cycle, the determinant vanishes. If `g` is one `p`-cycle, the eigenvalues on `Std` are the nontrivial `p`-th roots of unity and

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

At a finite-field point of `U_p`, Frobenius is a `p`-cycle on the roots exactly when the degree-`p` polynomial is irreducible. Hence the virtual local system

\[
\mathcal L_{hook}
=
\sum_i(-1)^i\mathcal L_i
\]

has trace function exactly `p` times the irreducibility indicator.

Define the geometric sparse hook complex

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

On the generic normal-form chart, the fixed-`q` pushforward and subsequent `q`-line cohomology are a Leray presentation of the pullback of this object. The finite normalization factors and compactification cones must still be assembled to obtain the exact raw Fortune count.

## 7. Ambient Airy cohomology is an alternating hook multiplicity

Let

\[
H_p=H^{p-5}_{prim}(X_p,\mathbf Q_\ell)
\]

and define

\[
\mathcal K_{ambient}
=
\sum_{i=0}^{p-1}(-1)^i
\operatorname{Hom}_{S_p}(V_i,H_p).
\]

By the Murnaghan--Nakayama rule, an irreducible `S_p` character is zero on a `p`-cycle unless its partition is the hook `(p-i,1^i)`, in which case its value is `(-1)^i`. Therefore, for every Frobenius power,

\[
\operatorname{Tr}(F^r|\mathcal K_{ambient})
=
\operatorname{Tr}(\sigma F^r|H_p).
\]

The cyclic two-block theorem identifies the right side with

\[
\operatorname{Tr}(F^r|\mathcal D_p).
\]

Thus

\[
\boxed{
\mathcal K_{ambient}^{ss}
=
\mathcal D_p^{ss}
}
\]

in the semisimple virtual Weil category. The full Kummer bridge then gives

\[
\boxed{
\mathcal R_p^{ss}
=
\mathcal K_{ambient}(-3)^{ss}.
}
\]

This is the exact hook-theoretic form of the Airy--primitive identity.

## 8. Forced normalization of a pure middle comparison

The ambient primitive module has weight `p-5`. The pure middle contribution of a smooth two-dimensional sparse-root stratum has weight two. A comparison of these pure middle terms therefore requires

\[
\boxed{
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
}
\]

because

\[
(p-5)-2\left(\frac{p-7}{2}\right)=2.
\]

Equivalently, using `R_p=K_ambient(-3)`, the Airy normalization is

\[
\boxed{
\mathcal R_p
\left(\frac{p-1}{2}\right).
}
\]

This determines the only possible Tate power for the pure middle comparison. It does not prove that the load-bearing hook constituent is pure, nor determine boundary signs.

## 9. Exact remaining application theorem

The number of successive equations

\[
s_4,\ldots,s_{p-4}
\]

is `p-7`, equal to the required degree change from ambient middle degree `p-5` to surface middle degree `2`. Ordinary restriction does not produce that degree change. The natural main-branch object is the iterated vanishing-cycle, or equivalent perverse complete-intersection, construction along this sequence.

Write schematically

\[
\Phi_{sp}
=
\phi_{s_{p-4}}\cdots\phi_{s_4}.
\]

The minimal application theorem is:

> After alternating hook extraction, the load-bearing pure part of the iterated vanishing-cycle complex is `K_ambient((p-7)/2)`, while the remaining terms are the explicitly listed main/Tate/Artin--Schreier, punctual, arithmetic-quadratic, discriminant, `q=2` and `q=infinity` cones.

In virtual notation the desired identity has the form

\[
\boxed{
\mathcal K_{sparse}^{load}
=
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
+
\mathcal B_p,
}
\]

or equivalently

\[
\boxed{
\mathcal K_{sparse}^{load}
=
\mathcal R_p
\left(\frac{p-1}{2}\right)
+
\mathcal B_p.
}
\]

Here `B_p` must be written from the known boundary cells and normalization multiplicities.

## 10. What is closed and what remains

### PROVED

1. For `p>=11`, the sparse ordered-root surface is the nested power-sum section `Y_p` of `X_p`.
2. Its separable quotient carries the exact alternating hook irreducibility local system.
3. The generic fixed-`q` hook covers are pullbacks of this global ordered-root torsor.
4. The Airy virtual module is the alternating hook multiplicity in ambient primitive cohomology.
5. The Tate power of any pure middle comparison is forced.

### OPEN

1. The iterated vanishing-cycle comparison.
2. The exact finite normalization from the quotient surface to the two arithmetic coefficient classes.
3. Identification of all boundary cones with exact signs and twists.
4. The final positivity/certificate implication.
5. Independently, the absolute Airy trace constant.

The application problem is now one specific nested-complete-intersection theorem plus a finite boundary ledger. It is no longer a search for an unspecified source-to-target object.
