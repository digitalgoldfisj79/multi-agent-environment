# Arithmetic orientation dichotomy and no-go for pointwise rank-two collapse

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** Kummer-projected rank-four Laurent--Airy family for the function-field `d=1` analytic wall.  
**Status:** the orthogonal coefficient identities are **PROVED modulo the standard arithmetic determinant normalization**; the normalization and all displayed identities are independently **EXACTLY COMPUTER-CERTIFIED** on the complete `p=5` fibre grid and selected square/nonsquare fibres at `p=11,17`. The resulting pointwise rank-two shortcut is **REFUTED**.

## 1. Fibre polynomial

For

\[
\mathscr H_{u,s}
=
H_c^1\!\left(
\mathbf G_m,
\mathcal L_{\chi_2}(x)
\otimes
\mathcal L_\psi(x^3+ux+s/x)
\right),
\qquad s\ne0,
\]

write

\[
P_{u,s}(T)
=
\det(1-F_{u,s}T\mid\mathscr H_{u,s})
=
1-e_1T+e_2T^2-e_3T^3+e_4T^4.
\]

The family is orthogonally self-dual with similitude multiplier

\[
\boxed{q_0=\chi(-1)p.}
\]

For primes `p congruent 5 mod 6`, its arithmetic orientation character is

\[
\boxed{\delta(s)=-\chi(s).}
\]

Equivalently,

\[
\boxed{
 e_3=-\chi(-1)\chi(s)p\,e_1,
 \qquad
 e_4=-\chi(s)p^2.
}
\]

The geometric determinant is the quadratic Kummer character in `s`; the minus sign is the constant arithmetic determinant normalization.  Since `q_0^2=p^2`, the two displayed coefficient identities are exactly the reciprocal-similitude identities

\[
e_3=\delta q_0 e_1,
\qquad
e_4=\delta q_0^2.
\]

## 2. Orientation-reversing fibres

An orientation-reversing element of a four-dimensional orthogonal similitude group has normalized spectrum

\[
\{1,-1,\lambda,\lambda^{-1}\}.
\]

Consequently its middle elementary symmetric coefficient vanishes.  In the present family this gives

\[
\boxed{
\chi(s)=+1
\quad\Longrightarrow\quad
 e_2=0.
}
\]

Thus the square fibres have the exact form

\[
\boxed{
P_{u,s}(T)
=
1-e_1T
+\chi(-1)p\,e_1T^3
-p^2T^4
\qquad(s\text{ square}).
}
\]

On these fibres the odd `p`-th Adams trace is indeed a rank-two Dickson trace after the standard scalar normalization.

## 3. Why this does not help the terminal projector

The exact two-plane reduction retains the factor

\[
\chi(s)-1.
\]

It vanishes on square `s` and equals `-2` on nonsquare `s`.  Therefore it discards precisely the orientation-reversing fibres on which the rank-two characteristic-polynomial collapse occurs, and retains the orientation-preserving fibres.

For nonsquare `s`, one has

\[
 e_4=+p^2,
 \qquad
 e_3=+\chi(-1)p\,e_1,
\]

but `e_2` is not forced to vanish.  These fibres remain genuinely rank four.

Hence the proposed inference

> the determinant Kummer projector selects orientation-reversing Frobenius, so the `p`-th Adams trace is pointwise rank two

is false.  The constant arithmetic orientation factor reverses the selection: the Kummer projector selects the orientation-preserving arithmetic fibres.

## 4. Exact certification

The verifier constructs `F_(p^n)` for `1<=n<=4`, computes

\[
S_n
=-\sum_{x\in\mathbf F_{p^n}^*}
\chi_n(x)
\psi\!\left(
\operatorname{Tr}(x^3+ux+s/x)
\right),
\]

and reconstructs `e_1,...,e_4` from Newton identities in exact cyclotomic arithmetic.

It checks:

- every one of the `20` fibres `(u,s)` with `u in F_5`, `s in F_5^*`;
- selected square and nonsquare fibres for `u=0,1` at `p=11`;
- selected square and nonsquare fibres for `u=0,1` at `p=17`.

All coefficient identities pass exactly.  No floating-point eigenvalue reconstruction is used.

## 5. Ruling

### Preserved positive result

The generic local-inertia calculation remains valid:

- the `s=infinity` wild block cancels in the Kummer-projected Adams class;
- the `s=0` residual is bounded tame;
- generic `u=infinity` wild inertia becomes tame after Adams;
- there is no interior discriminant conductor.

### Closed

- pointwise rank-two reduction on the nonsquare fibres selected by the terminal projector;
- using the determinant character alone to construct the required bounded-rank global Adams object;
- the naive orientation-cover tensor-induction shortcut in which nonsplit rational fibres are assumed to act by factor exchange.

### Still open

The terminal theorem still requires cancellation across the orientation-preserving nonsquare rank-four fibres, either through an object-level relation among the four hook-Schur terms or through direct two-parameter/projective orthogonality.