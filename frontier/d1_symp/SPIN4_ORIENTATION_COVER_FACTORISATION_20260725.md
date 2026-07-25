# Spin(4) factorisation on the geometric orientation cover

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** exceptional rank-four Laurent--Airy family in the function-field `d=1` analytic programme.  
**Status:** the geometric Spin-lift and rank-two tensor factorisation are **PROVED**.  They reduce the standard Adams complexity from cubic to quadratic growth, but do not by themselves prove the terminal estimate.

## 1. Orientation cover

Let

\[
B=\mathbf A^1_u\times\mathbf G_{m,s}
\]

and let

\[
\mathscr H_B(u,s)
=H_c^1\!\left(
\mathbf G_m,
\mathcal L_{\chi_2}(x)
\otimes
\mathcal L_\psi(x^3+ux+s/x)
\right).
\]

The family is geometrically orthogonally self-dual of rank four and has geometric determinant `L_(chi_2)(s)`.  Pass to the quadratic orientation cover

\[
\pi:B'=\mathbf A^1_u\times\mathbf G_{m,r}
\longrightarrow B,
\qquad
s=r^2.
\]

Then

\[
\det(\pi^*\mathscr H_B)=1
\]

geometrically, so the geometric monodromy representation lands in `SO_4`.

## 2. Vanishing of the Spin obstruction

The central extension

\[
1\longrightarrow\mu_2
\longrightarrow\operatorname{Spin}_4
\longrightarrow\operatorname{SO}_4
\longrightarrow1
\]

has lifting obstruction in

\[
H^2_{\mathrm{et}}(B'_{\overline{\mathbf F}_p},\mu_2).
\]

Homotopy invariance reduces this group to

\[
H^2_{\mathrm{et}}(\mathbf G_m,\mu_2).
\]

It vanishes.  Equivalently, the Kummer sequence gives

\[
0\to\operatorname{Pic}(\mathbf G_m)/2
\to H^2(\mathbf G_m,\mu_2)
\to\operatorname{Br}(\mathbf G_m)[2]\to0,
\]

and both outer groups are zero over an algebraically closed field:

- `Pic(G_m)=0`;
- `Br(G_m)=0` for a smooth affine curve over an algebraically closed field.

Therefore the `SO_4` local system lifts to a `Spin_4` local system.

## 3. Rank-two factors

Use the exceptional isomorphism

\[
\operatorname{Spin}_4\cong
\operatorname{SL}_2\times\operatorname{SL}_2.
\]

Let `A` and `C` be the two rank-two local systems obtained from the two standard representations of the `SL_2` factors.  The four-dimensional vector representation of `SO_4` pulls back to the external tensor product of those standard representations.  Hence

\[
\boxed{
\pi^*\mathscr H_B
\cong
\mathscr A\otimes\mathscr C
}
\]

geometrically on `B'`.

The lift is not unique: it may be modified by a quadratic central character.  This replaces

\[
(\mathscr A,\mathscr C)
\quad\text{by}\quad
(\mathscr A\otimes\mathscr L,
 \mathscr C\otimes\mathscr L^{-1}),
\]

and leaves `A tensor C` unchanged.

## 4. Deck involution

Let

\[
\tau(u,r)=(u,-r)
\]

be the deck involution.  The original determinant character is the orientation character.  Thus the descent action of `tau` on the `SO_4` local system is induced by an element of `O_4\setminus SO_4`.

Conjugation by such an element realizes the nontrivial outer automorphism of

\[
\operatorname{Spin}_4
\cong
\operatorname{SL}_2\times\operatorname{SL}_2,
\]

which exchanges the two factors.  Consequently, after a permissible central rank-one adjustment,

\[
\boxed{
\tau^*\mathscr A\cong\mathscr C,
\qquad
\tau^*\mathscr C\cong\mathscr A.
}
\]

This is the geometric meaning of the exceptional rank-four determinant cover.

## 5. Adams factorisation

Adams operations are multiplicative in the representation ring.  Therefore

\[
\boxed{
\Psi^p(\pi^*\mathscr H_B)
=
\Psi^p(\mathscr A)
\otimes
\Psi^p(\mathscr C).
}
\]

For a rank-two local system `V`,

\[
\Psi^p(V)
=
\operatorname{Sym}^p(V)
-\det(V)\otimes\operatorname{Sym}^{p-2}(V).
\]

The two actual terms have ranks `p+1` and `p-1`, so the total termwise rank is `2p`.  Applying this to both factors gives an actual four-term realization of the pulled-back rank-four Adams class with total termwise rank

\[
\boxed{4p^2.}
\]

This improves the direct rank-four hook-Schur realization

\[
\frac{4p(p^2+2)}3
\]

from cubic growth to quadratic growth.

## 6. Why this is not yet the terminal bound

The Hayes irreducible coefficient includes the divided trace

\[
I_p=-\frac1p\operatorname{Tr}(F^p\mid\mathscr H_B).
\]

After the Spin factorisation, the standard actual realization therefore still has effective termwise rank of order

\[
\frac{4p^2}{p}=4p.
\]

Thus the factorisation removes two powers of `p` relative to the original unnormalised rank-four Schur bound, but one factor `p` remains.  This is exactly the factor missing from the desired parameter-plane estimate.

The arithmetic orientation calculation explains why no further pointwise reduction occurs: the Kummer projector retains nonsquare `s`, but those rational fibres are arithmetic orientation-preserving.  On them the two Spin factors are preserved rather than exchanged, so the `p`-th trace is a product of two rank-two Adams traces, not a single rank-two trace.

## 7. Revised exact wall

The first analytic boulder is now reduced to:

> **Spin-factor correlation theorem.**  Prove square-root cancellation, with an absolute constant, for the Kummer-odd descent of
> \[
> \frac1p
> \Psi^p(\mathscr A)\otimes\Psi^p(\mathscr C)
> \]
> on the orientation cover, exploiting `tau^*A=C` and the exact local wild cancellation.

A termwise Deligne bound on the four tensor-product Schur terms loses one factor `p`.  A successful proof must obtain that factor from:

1. cancellation between the four terms before absolute values;
2. additive orthogonality in the `u` parameter;
3. a clean pushforward reducing the two-dimensional trace to a one-dimensional rank-`O(p)` complex.

## 8. Ruling

### Proved

- the geometric orientation cover has zero Spin obstruction;
- the rank-four family factors geometrically as `A tensor C` with rank-two factors;
- the deck involution exchanges the factors;
- the pulled-back `p`-th Adams class has a four-term realization of total rank `4p^2`.

### Closed

- a direct pointwise reduction to a single rank-two Adams trace on the selected nonsquare fibres;
- obtaining the terminal estimate from the Spin factorisation plus termwise Deligne alone.

### Open

The final factor-`p` cancellation in the Spin-factor correlation.