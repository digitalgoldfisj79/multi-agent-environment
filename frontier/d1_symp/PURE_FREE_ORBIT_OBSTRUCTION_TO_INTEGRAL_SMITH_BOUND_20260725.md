# Pure free-orbit obstruction to an integral Smith trace bound

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** audit of the proposed passage from modular Smith localization to a characteristic-zero Frobenius bound.  
**Status:** the counterexample and coefficient-category separation below are **PROVED**. They show that the requested absolute trace bound does not follow from the existing Smith/Fourier reductions.

## 1. Purpose

Modular Smith localization kills free `C_p`-modules. The proposed proof would require the following additional implication:

> a free cyclic summand killed by modular Smith contributes no, or uniformly bounded, characteristic-zero trivial-minus-nontrivial Frobenius trace.

That implication is false. It remains false with:

- an integral lattice;
- an action of the full affine normalizer `AGL_1(F_p)`;
- an invertible Frobenius isogeny;
- pure characteristic-zero eigenvalues of one common Weil weight.

## 2. The affine-normalizer lattice

Let `O` be a complete discrete valuation ring of residue characteristic `p`, with fraction field `K`. Let

\[
C=C_p
\]

and let

\[
M=\mathcal O[C]
\]

be the regular permutation lattice, with basis indexed by `F_p`. The affine normalizer

\[
N=C_p\rtimes F_p^*=\operatorname{AGL}_1(F_p)
\]

acts by affine permutations of this basis.

Put

\[
J=\sum_{g\in C}g\in\operatorname{End}_{\mathcal O}(M).
\]

In the permutation basis, `J` is the all-ones operator. It commutes with `N`: translations preserve the sum and every automorphism of `C` permutes its terms.

After extending scalars to a splitting field,

\[
M_K=K_{\bf1}\oplus\bigoplus_{\chi\ne1}K_\chi.
\]

The norm operator acts by

\[
J|K_{\bf1}=p,
\qquad
J|K_\chi=0\quad(\chi\ne1).
\]

Modulo the maximal ideal, `M` remains a free rank-one `k[C]`-module. Hence its Tate/Smith localization is zero.

## 3. A pure integral Frobenius invisible to Smith

Fix an integer `m>=1` and put

\[
Q=p^{2m},
\qquad
b=p^{m-1}.
\]

On

\[
L=M\otimes_{\mathcal O}\mathcal O^2
\]

define

\[
\Phi
=
1_M\otimes
\begin{pmatrix}
0&-Q\\
1&0
\end{pmatrix}
+
J\otimes
\begin{pmatrix}
0&0\\
0&b
\end{pmatrix}.
\]

This is integral and `N`-equivariant. Its determinant on every character block is `Q`, so it is an isogeny and becomes invertible over `K`.

### Nontrivial cyclic character

On `K_chi` with `chi != 1`, `J=0`, so

\[
\Phi_\chi=
\begin{pmatrix}
0&-Q\\
1&0
\end{pmatrix},
\]

with characteristic polynomial

\[
X^2+Q.
\]

Its eigenvalues are

\[
\pm i p^m,
\]

both of complex absolute value `p^m`.

### Trivial cyclic character

On `K_1`, `J=p`, so

\[
\Phi_{\bf1}=
\begin{pmatrix}
0&-Q\\
1&pb
\end{pmatrix}
=
\begin{pmatrix}
0&-p^{2m}\\
1&p^m
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
X^2-p^mX+p^{2m}.
\]

The roots are

\[
p^m\frac{1\pm i\sqrt3}{2},
\]

again algebraic integers whose every complex conjugate has absolute value `p^m`.

Thus all generic eigenvalues on both cyclic sectors are pure of the same weight `2m`.

Nevertheless,

\[
\boxed{
\operatorname{Tr}(\Phi|L^{C})
-
\operatorname{Tr}(\Phi|L_\chi)
=p^m.
}
\]

The modular Smith object is zero, while the characteristic-zero cyclic trace difference is one full Weil-scale eigenvalue.

Taking `r` direct copies gives

\[
\boxed{
\widehat H^*(C,L^{\oplus r}\otimes k)=0,
\qquad
\operatorname{Tr}(\Phi|({L^{\oplus r}})^C)
-
\operatorname{Tr}(\Phi|({L^{\oplus r}})_\chi)
=r p^m.
}
\]

The coefficient can therefore grow arbitrarily with the free-orbit rank.

For the Airy common weight, take

\[
m=\frac{p+1}{2}.
\]

Each invisible free block then contributes exactly the target scale

\[
p^{(p+1)/2}.
\]

Taking

\[
r=\frac{p-5}{6}
\]

reproduces the precise linearly growing loss that the desired theorem must remove.

## 4. Consequence for the proposed proof

The following data do not imply an absolute trace bound:

1. modular Smith/Tate localization is rank two or bounded;
2. the remaining lattice is free over `O[C_p]`;
3. Frobenius commutes with the affine normalizer;
4. Frobenius is integral and invertible after inverting `p`;
5. all generic eigenvalues are pure of the expected weight;
6. the associated-graded coefficient pairing is unimodular.

The counterexample satisfies all six and still has an arbitrarily large normalized cyclic trace difference.

Therefore a proof must control the Frobenius **on the free cyclic part**, not merely prove that this part is killed by Smith localization.

## 5. Exact missing invariant

For an integral `C_p`-equivariant complex `K` with Frobenius `Phi`, define the generic cyclic defect

\[
\delta_\Phi(K)
=
\operatorname{Tr}(\Phi|K^C)
-
\operatorname{Tr}(\Phi|K_\xi).
\]

Equivalently, on a finite free `O[C]` model it is the difference between the trivial and nontrivial character evaluations of the group-ring or Hattori--Stallings trace of `Phi`.

Modular Smith localization determines none of this invariant on free summands. The exact additional theorem required for the Airy bound is therefore one of:

\[
\boxed{
\delta_\Phi(K_{\mathrm{free}})=0,
}
\]

or at minimum

\[
\boxed{
|\delta_\Phi(K_{\mathrm{free}})|
\le C p^{(p+1)/2}
}
\]

with `C` independent of `p` and of the free rank.

This is not a formal property of Smith theory. It is precisely the missing Frobenius-correlation theorem.

## 6. The coefficient-category separation

There are two different integral settings in the programme.

### Characteristic-zero Fourier setting

For `ell != p`, the Artin--Schreier sheaf exists with an integral lattice over `O_ell[zeta_p]`. Here `p` is a unit, the `C_p` character projectors are semisimple direct summands, and the global Fourier-delta identity of `GLOBAL_INTEGRAL_FOURIER_ELIMINATION_TO_CUBIC_TAIL_20260725.md` is exact.

### Modular Smith setting

Smith/Tate localization for a `C_p` action requires residue characteristic `p`, where free `k[C_p]`-modules become invisible. In that setting a `p`-th root of unity reduces to one, so the ordinary integral reduction of an Artin--Schreier character loses its phase. Over a base field of characteristic `p`, ordinary etale `p`-adic coefficients are not the coefficient category used for the Artin--Schreier Fourier transform.

A `p`-adic Dwork or arithmetic-D-module category can encode the exponential phase and Frobenius, but the necessary integral lattice, Smith localization and compatibility with Fourier pushforward at the boundary `k=p` are exactly what has not been constructed. Haessig's effective decomposition applies in the nonresonant range `k<p`; the existing `k=p` residue audit leaves linearly many invariant Laurent classes before cohomological reduction.

Thus one may not splice the `ell`-adic Fourier-delta theorem and the modular Smith rank collapse as though they were statements in one integral six-functor category.

## 7. Ruling

### PROVED

- modular Smith localization can kill an integral free cyclic lattice carrying a nonzero characteristic-zero cyclic trace defect;
- the defect can be arbitrarily large in the free rank;
- this remains true for affine-normalizer-equivariant, integral, invertible and pure Frobenius;
- the `ell`-adic Fourier elimination and residue-characteristic-`p` Smith contraction live in different integral coefficient settings;
- the absolute Airy bound does not follow from the currently proved elimination and modular contraction.

### OPEN

- a geometric theorem forcing cancellation of the group-ring Frobenius trace on the actual Airy free-orbit complex;
- equivalently,
  \[
  |\operatorname{Tr}(F|R_p)|\le C p^{(p+1)/2};
  \]
- the crown.

The requested absolute bound cannot be honestly declared proved without an additional theorem controlling `delta_Phi` on the free cyclic part. The counterexample shows that this control is substantive, not bookkeeping.
