# Sparse root surface and exact hook extraction

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the sparse-root construction, hook extraction and Airy hook-multiplicity identity below are **PROVED**. The iterated vanishing-cycle comparison from the ambient complete intersection to the sparse surface remains **OPEN**.

## 0. Result

The source and target of the application theorem can now be placed in one explicit geometric diagram.

- The Airy virtual module is the alternating hook multiplicity in the primitive cohomology of the smooth cyclic `(2,3)` complete intersection.
- The irreducibility hook complex is the alternating hook-isotypic compactly supported cohomology of the sparse ordered-root surface inside that complete intersection.
- The sparse surface is obtained by imposing the remaining power-sum equations

\[
s_4=s_5=\cdots=s_{p-4}=0.
\]

There are `p-7` additional equations. Since `p=5 mod 6`, this number is even. The only admissible geometric comparison is therefore an iterated vanishing-cycle or equivalent middle-dimensional comparison across this nested complete intersection, with the forced Tate twist

\[
\frac{p-7}{2}.
\]

The missing map is no longer undefined.

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

It is the smooth `(2,3)` complete intersection already used in the Airy--primitive bridge.

## 2. Successive power sums descend through translation

For a diagonal translation `x_i -> x_i+c`,

\[
s_m(x+c)
=
\sum_{j=0}^m
\binom mj c^{m-j}s_j(x).
\]

In characteristic `p`,

\[
s_0=p=0.
\]

Consequently, on the nested locus

\[
s_1=s_2=\cdots=s_{m-1}=0,
\]

the function `s_m` is invariant under diagonal translation. Therefore each equation `s_m=0` descends successively to the quotient by `L`.

Define

\[
X_p^{(m)}
=
\{s_2=s_3=\cdots=s_m=0\}
\subset\mathbf P(W),
\qquad
3\le m\le p-4.
\]

Thus

\[
X_p=X_p^{(3)}
\supset X_p^{(4)}
\supset\cdots\supset X_p^{(p-4)}.
\]

Put

\[
Y_p=X_p^{(p-4)}.
\]

It is cut out inside `X_p` by the `p-7` additional power sums `s_4,...,s_{p-4}` and has pure dimension two.

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

Every integer `1<=m<=p-4` is invertible in `kbar`. Induction gives

\[
s_1=\cdots=s_{p-4}=0
\quad\Longleftrightarrow\quad
e_1=\cdots=e_{p-4}=0.
\]

Hence the ordered root tuples on the affine cone over `Y_p` are exactly the ordered roots of polynomials

\[
\boxed{
Z^p+A Z^3+B Z^2+C Z+D.
}
\]

Diagonal translation of the roots corresponds to `Z -> Z+c`; in characteristic `p` it preserves this sparse family. Projective scaling of the root tuple gives the usual weighted scaling of `(A,B,C,D)`. Thus `Y_p/S_p`, with these translation and scaling identifications, is the geometric coefficient surface underlying the full degree-three-offset family.

## 4. Generic normal-form chart

On the open set `A C !=0`, translation uniquely removes `B`, since the new quadratic coefficient is `B+3Ac`. After depression, a scalar change of root variable normalizes the cubic and linear coefficients to `1` and `-3`. Over the base field this change has two quadratic forms according to whether the required square root exists.

The resulting generic chart is

\[
P_{q,t}(Z)
=qZ^p+Z^3-3Z-(q-2)t,
\]

with the split and nonsplit quadratic readings recorded by the hook audit.

The omitted loci are exactly the kinds of cells already present in the application ledger:

- `C=0`, the `q=infinity` boundary;
- the colliding-critical-value cell `q=2`;
- the discriminant fibres `t=+1,-1`;
- the loci where the depression or quadratic normalization degenerates;
- the arithmetic quadratic descent of the chosen square root.

No new boundary family is introduced by the present construction.

## 5. Separable ordered-root torsor

Let

\[
Y_p^{sep}\subset Y_p
\]

be the open locus where the coordinates `x_i` are pairwise distinct. The symmetric group `S_p` acts freely on this locus. Put

\[
\mathcal U_p=Y_p^{sep}/S_p.
\]

Then

\[
Y_p^{sep}\longrightarrow\mathcal U_p
\]

is the finite etale ordered-root `S_p`-torsor of the separable sparse polynomial family modulo translation and scaling.

For

\[
V_i=\bigwedge^i\mathrm{Std},
\qquad0\le i\le p-1,
\]

let `L_i` be the associated local system on `U_p`.

## 6. Exact irreducibility character

Define the virtual hook representation

\[
\Lambda_p
=
\sum_{i=0}^{p-1}(-1)^iV_i.
\]

For a permutation `g in S_p`,

\[
\operatorname{Tr}(g|\Lambda_p)
=
\det(1-g|\mathrm{Std}).
\]

If `g` has more than one cycle, `Std` contains a nonzero fixed vector and the determinant is zero. If `g` is one `p`-cycle, its eigenvalues on `Std` are the nontrivial `p`-th roots of unity, so

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

At a finite-field point of `U_p`, Frobenius is a `p`-cycle on the roots exactly when the associated degree-`p` polynomial is irreducible. Hence the trace function of

\[
\mathcal L_{hook}
=
\sum_i(-1)^i\mathcal L_i
\]

is exactly `p` times the irreducibility indicator.

The global hook complex is

\[
\boxed{
\mathcal K_{sparse}
=R\Gamma_c(\mathcal U_p,\mathcal L_{hook}).
}
\]

Equivalently, because `Y_p^{sep}->U_p` is an `S_p`-torsor,

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

The fixed-`q` hook pushforward followed by the `q`-line assembly is a Leray presentation of this single global complex on the generic normal-form chart. The separately computed `q=2`, `q=infinity` and discriminant cells are its compactification cones.

## 7. Airy primitive cohomology is also an alternating hook multiplicity

Let

\[
H_p=H^{p-5}_{prim}(X_p,\mathbf Q_\ell).
\]

Define

\[
\mathcal K_{ambient}
=
\sum_{i=0}^{p-1}(-1)^i
\operatorname{Hom}_{S_p}(V_i,H_p).
\]

For an irreducible `S_p` representation indexed by a partition `lambda`, the Murnaghan--Nakayama rule gives

\[
\chi_\lambda(\text{a }p\text{-cycle})=0
\]

unless `lambda` is a hook `(p-i,1^i)`, in which case the value is `(-1)^i`. Therefore, for every Frobenius power,

\[
\operatorname{Tr}(F^r|\mathcal K_{ambient})
=
\operatorname{Tr}(\sigma F^r|H_p).
\]

The cyclic two-block theorem gives the right side as

\[
\operatorname{Tr}(F^r|\mathcal D_p).
\]

Thus, in the semisimple virtual Weil category,

\[
\boxed{
\mathcal K_{ambient}^{ss}
=
\mathcal D_p^{ss}.
}
\]

Combining with the full Kummer bridge gives

\[
\boxed{
\mathcal R_p^{ss}
=
\mathcal K_{ambient}(-3)^{ss}.
}
\]

This is the exact hook-theoretic form of the Airy--primitive identity.

## 8. Forced normalization of the sparse comparison

The ambient primitive module has weight `p-5`. The load-bearing global cohomology of the sparse surface has middle weight two before boundary and mixed-weight corrections. Therefore the only Tate normalization compatible with the pure middle pieces is

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

Equivalently, on the Airy side the forced normalization is

\[
\boxed{
\mathcal R_p
\left(\frac{p-1}{2}\right),
}
\]

since

\[
\mathcal R_p
=
\mathcal K_{ambient}(-3).
\]

This determines the previously missing power of `p` in any valid application formula. It does not determine the boundary signs or prove the comparison.

## 9. Exact remaining application theorem

There are `p-7` successive equations

\[
s_4,\ldots,s_{p-4}.
\]

The required degree change from ambient middle degree `p-5` to surface middle degree `2` is also `p-7`. Ordinary restriction cannot make this change. The natural candidate is the iterated vanishing-cycle functor along this sequence, or an equivalent perverse complete-intersection construction.

Write schematically

\[
\Phi_{sp}
=
\phi_{s_{p-4}}\cdots\phi_{s_4}.
\]

The minimal application theorem is now:

> After alternating hook extraction, the load-bearing pure part of the iterated vanishing-cycle complex `Phi_sp(Q_l)` is the ambient hook multiplicity `K_ambient((p-7)/2)`, and its remaining cones are exactly the main/Tate/Artin--Schreier, punctual, arithmetic-quadratic, `q=2`, `q=infinity` and discriminant boundary terms already listed in the hook ledger.

In virtual notation, the desired identity has the form

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

where `B_p` must be written explicitly from the known boundary cells.

Equivalently,

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

## 10. What is closed and what remains

### PROVED

1. The sparse ordered-root surface is the nested power-sum section `Y_p` of `X_p`.
2. Its separable quotient carries the exact alternating hook irreducibility local system.
3. The post-pushforward hook construction is a Leray presentation of its global alternating hook cohomology.
4. The Airy virtual module is the alternating hook multiplicity in ambient primitive cohomology.
5. The Tate normalization of any pure middle comparison is forced.

### OPEN

1. The iterated vanishing-cycle comparison.
2. Identification of its boundary cones with exact signs and twists.
3. The final positivity/certificate implication.
4. Independently, the absolute Airy trace constant.

The application problem is now one specific nested-complete-intersection theorem, not a search for an unspecified source-to-target morphism.
