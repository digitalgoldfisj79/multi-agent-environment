# Exact Salié evaluation and cancellation of the full main term

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, primes `p congruent 5 mod 6`.  
**Status:** **PROVED**.

## 1. The projective all-line sum

Retain the notation

\[
E=\mathbf F_{p^p},
\qquad
H=\ker\operatorname{Tr}_{E/\mathbf F_p},
\]

and

\[
\mathcal R_{\mathrm{all}}(p)
=
\sum_{\substack{[h]\in\mathbf P(H)\\
\operatorname{Tr}(h^{-1})\ne0}}
\chi_E(h)\chi(\operatorname{Tr}(h^{-1})).
\]

The summand is invariant under multiplication by `F_p^*`.

## 2. Finite-field Salié identity

Let `F_q` be a finite field of odd cardinality, let `psi_q` be a nontrivial additive character, let `chi_q` be the quadratic character, and put

\[
G_q=\sum_{x\in\mathbf F_q}\psi_q(x^2).
\]

### Lemma 2.1

For `b!=0`,

\[
\boxed{
\sum_{x\ne0}\chi_q(x)\psi_q(ax+b/x)
=
G_q\chi_q(b)
\sum_{y^2=4ab}\psi_q(y).
}
\]

### Proof

Take the additive Fourier transform in the variable `a`. For the left side, at frequency `t`, orthogonality gives

\[
q\chi_q(t)\psi_q(b/t)
\]

when `t!=0`, and zero at `t=0`.

For the right side, summing first over `a` is equivalent to summing over all `y` with `a=y^2/(4b)`. Its Fourier transform is

\[
G_q\chi_q(b)
\sum_y\psi_q\left(y-rac{t}{4b}y^2\right).
\]

For `t!=0`, completing the square gives

\[
G_q^2\chi_q(b)\chi_q\left(-\frac{t}{4b}\right)
\psi_q(b/t)
=q\chi_q(t)\psi_q(b/t),
\]

using `G_q^2=chi_q(-1)q`. At `t=0` both transforms vanish. Fourier inversion proves the identity.

## 3. Exact evaluation of R_all

Let

\[
G_E=\sum_{x\in E}\Psi(x^2),
\qquad
G_p=\sum_{c\in\mathbf F_p}\psi(c^2).
\]

### Theorem 3.1

\[
\boxed{
\mathcal R_{\mathrm{all}}(p)
=
\frac{G_E}{G_p}
=
G_p^{p-1}
=
\chi(-1)^{(p-1)/2}p^{(p-1)/2}.
}
\]

### Proof

Let

\[
A_p
=
\sum_{\substack{h\in H^*}}
\chi_E(h)\chi(\operatorname{Tr}(h^{-1})).
\]

Since the summand is scalar-invariant,

\[
A_p=(p-1)\mathcal R_{\mathrm{all}}(p).
\]

Expand the trace-zero indicator and the quadratic character:

\[
A_p
=
\frac1{pG_p}
\sum_{u\in\mathbf F_p}
\sum_{v\in\mathbf F_p^*}
\chi(v)
\sum_{h\in E^*}
\chi_E(h)\Psi(uh+v/h).
\]

Apply Lemma 2.1 over `E`. Because the extension degree `p` is odd,

\[
\chi_E(v)=\chi(v).
\]

For `u=0`, the inner Salié sum is `G_E chi(v)`. Its total contribution is

\[
(p-1)G_E.
\]

For `u!=0`, the equation

\[
y^2=4uv
\]

has two roots exactly when `uv` is a square. Such roots lie in `F_p`, and their extension trace is zero because the extension degree is `p`. Hence each root contributes one to `Psi(y)`. For each fixed nonzero `u`, exactly `(p-1)/2` values of `v` qualify, and the outer and inner quadratic characters cancel. The contribution is

\[
(p-1)G_E
\]

for each `u!=0`, hence `(p-1)^2G_E` in total.

Therefore

\[
A_p=(p-1)G_E/G_p.
\]

Hasse--Davenport gives

\[
G_E=G_p^p
\]

because the extension degree is the odd integer `p`. This proves the theorem.

## 4. Exact cancellation in the Airy second moment

The projective Salié identity is

\[
\begin{aligned}
T_p^2
={}&p^{p-1}
+\chi(-1)p^{(p-1)/2}
\left(p\mathcal R_0(p)-\mathcal R_{\mathrm{all}}(p)\right)\\
&+\chi(3)p^{(p+1)/2}\mathcal D(p).
\end{aligned}
\]

But

\[
\chi(-1)p^{(p-1)/2}\mathcal R_{\mathrm{all}}(p)
=p^{p-1},
\]

because

\[
\chi(-1)^{(p+1)/2}=1
\]

for every odd prime. The diagonal term cancels exactly.

### Theorem 4.1

\[
\boxed{
T_p^2
=
p^{(p+1)/2}
\left(
\chi(-1)\mathcal R_0(p)
+
\chi(3)\mathcal D(p)
\right).
}
\]

In particular,

\[
\boxed{
\mathcal K_p
:=
\chi(-1)\mathcal R_0(p)+\chi(3)\mathcal D(p)
=
\frac{T_p^2}{p^{(p+1)/2}}
\in\mathbf Z_{\ge0}.
}
\]

## 5. Exact terminal reformulation

The desired estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

is equivalent to

\[
\boxed{
0\le\mathcal K_p
\le C^2p^{(p-3)/2}.
}
\]

Thus only one combined projective character sum remains:

\[
\boxed{
\left|
\chi(-1)\mathcal R_0(p)
+
\chi(3)\mathcal D(p)
\right|
\ll p^{(p-3)/2}.
}
\]

The potentially larger all-line sum and the raw diagonal contribution are now removed exactly.

## 6. Relation to the Hasse theorem

For `p=6r+5`, the proved valuation

\[
v_p(T_p)=\frac{p+4}{3}
\]

when the Hasse coefficient is nonzero implies

\[
\boxed{
 v_p(\mathcal K_p)=\frac{p+13}{6}=r+3.
}
\]

The projective character sum therefore carries the same explicit characteristic-boundary divisibility in squared form.

## 7. New analytic wall

> **Combined projective character theorem.** Prove
> \[
> \mathcal K_p
> =\chi(-1)\mathcal R_0(p)+\chi(3)\mathcal D(p)
> \ll p^{(p-3)/2}
> \]
> with an absolute implied constant.

This single theorem is sufficient for the Airy bound. It is strictly sharper than separately bounding `R_all`, `R_0`, and `D`.

## 8. Verification

`projective_salie_collapse_verify.py` checks at `p=5` that

\[
\mathcal R_{\mathrm{all}}=25,
\qquad
\mathcal R_0=-5,
\qquad
\mathcal D=-5,
\]

and hence both sides of Theorem 4.1 vanish, as required by `T_5=0`.
