# Completed cyclic fixed scheme and correction to the localization route

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the completed local-ring calculation is **PROVED**. The proposed use of the unique `sigma`-fixed point to localize the target trace is **INVALID** because the target correspondence is `sigma` composed with Frobenius, not `sigma` alone.

## 1. Setup

Let

\[
V=\overline{\mathbf F}_p^p,
\qquad
H=\{(x_i):\sum_i x_i=0\},
\qquad
W=H/\overline{\mathbf F}_p(1,\ldots,1),
\]

and let `sigma` cyclically permute the coordinates. Put `n=p-2=dim W`. As a module for `N=sigma-1`, `W` is one Jordan block of length `n`.

Let

\[
X_p=\{Q=C=0\}\subset\mathbf P(W),
\qquad
Q=\sum_i x_i^2,
\qquad
C=\sum_i x_i^3.
\]

The unique set-theoretic `sigma`-fixed point is represented by

\[
v=(0,1,2,\ldots,p-1).
\]

## 2. PROVED: the full projective fixed scheme of `sigma`

Choose a Jordan basis `e_0,...,e_{n-1}` with

\[
N e_j=e_{j-1}\quad(j\ge1),\qquad Ne_0=0.
\]

On the affine chart in `P(W)` where the `e_0` coordinate is one, write a point as

\[
e_0+z_1e_1+\cdots+z_{n-1}e_{n-1}.
\]

The equality of projective points `sigma(z)=z` gives

\[
z_{j+1}=z_1z_j\quad(1\le j\le n-2),
\qquad
z_1z_{n-1}=0.
\]

Hence

\[
z_j=z_1^j,
\qquad
z_1^n=0.
\]

Therefore the scheme-theoretic fixed locus is curvilinear and

\[
\boxed{
\widehat{\mathcal O}_{\operatorname{Fix}(\sigma,\mathbf P(W)),[v]}
\cong
\overline{\mathbf F}_p[[t]]/(t^{p-2}).
}
\]

Since `[v]` is the only set-theoretic fixed point, this is the entire fixed scheme.

## 3. Canonical formal eigenvector

In the original coordinate model, the same fixed thickening is represented by

\[
x_i(t)=\frac{(1+t)^i-1}{t}
      =\sum_{r\ge0}\binom{i}{r+1}t^r,
\qquad i\in\mathbf F_p.
\]

Indeed,

\[
x_{i+1}(t)=(1+t)x_i(t)+1,
\]

so modulo the constant line the cyclic shift acts by the projective scalar `1+t`. Moreover,

\[
\sum_{i\in\mathbf F_p}x_i(t)=t^{p-2},
\]

which is zero in `k[[t]]/(t^{p-2})`, so this vector lies in `H` modulo the fixed-scheme relation.

## 4. PROVED: restriction of the quadratic and cubic equations

Let

\[
S_m(t)=\sum_{i=0}^{p-1}(1+t)^{mi}.
\]

In characteristic `p`,

\[
S_m(t)
=
\frac{(1+t)^{mp}-1}{(1+t)^m-1}
=
\frac{(1+t^p)^m-1}{(1+t)^m-1}.
\]

Using

\[
Q(t)=\frac{S_2-2S_1}{t^2},
\qquad
C(t)=\frac{S_3-3S_2+3S_1}{t^3},
\]

and retaining precisely the terms visible modulo `t^(p-2)`, one obtains

\[
\boxed{Q(t)=-t^{p-3}\pmod{t^{p-2}}}
\]

and

\[
\boxed{
C(t)=t^{p-4}\left(1+\frac t2\right)
\pmod{t^{p-2}}.
}
\]

The factor `1+t/2` is a unit. Consequently

\[
\boxed{
\widehat{\mathcal O}_{\operatorname{Fix}(\sigma,X_p),[v]}
\cong
\overline{\mathbf F}_p[[t]]/(t^{p-4}).
}
\]

Thus

\[
\boxed{\operatorname{length}\operatorname{Fix}(\sigma,X_p)=p-4.}
\]

For `p=5` the fixed point is reduced. For every `p>=7` its nilpotent thickness grows linearly with `p`.

The identities are independently checked in exact finite-field arithmetic by `fixed_scheme_verify.py`.

## 5. Consequence for the bare-shift localization idea

The unique fixed point does not have bounded intersection multiplicity. Any local formula attached to the bare automorphism `sigma` must account for `p-4` infinitesimal layers. Therefore even for the wrong correspondence, the argument

> one set-theoretic fixed point implies one bounded local contribution

is false.

A bounded answer would require a signed or oscillatory cancellation across these layers; it cannot follow from the support or length of the fixed scheme.

## 6. CRITICAL CORRECTION: this is not the target correspondence

The restriction-of-scalars description says that the arithmetic operator relevant to `T_p` is

\[
\Phi=\sigma\circ\operatorname{Frob}_p
\]

(up to the harmless inverse convention between arithmetic and geometric Frobenius), not `sigma` alone.

The fixed-point equations for `Phi` are

\[
x_{i+1}=x_i^p
\]

up to cyclic orientation. Hence every fixed point is determined by `x_0` and satisfies

\[
x_i=x_0^{p^i},
\qquad
x_0^{p^p}=x_0.
\]

The equations `sum x_i=0`, `sum x_i^2=0`, `sum x_i^3=0` become exactly

\[
\operatorname{Tr}(x_0)=0,
\qquad
\operatorname{Tr}(x_0^2)=0,
\qquad
\operatorname{Tr}(x_0^3)=0.
\]

Thus `Fix(Phi)` is the original extension-field locus, not the unique point `[v]`.

Moreover, the differential of absolute Frobenius is zero, so

\[
d\Phi=0.
\]

Therefore `1-d\Phi` is invertible on tangent spaces: the graph of `Phi` and the diagonal are transverse at their geometric fixed points. The wild nontransversality of `Fix(sigma)` is not the local obstruction for the target trace.

## 7. Verdict

### PROVED

- `Fix(sigma,P(W))` is curvilinear of length `p-2`;
- `Fix(sigma,X_p)` is curvilinear of length `p-4`;
- the bare-shift fixed multiplicity grows linearly.

### INVALID ROUTE

The proposed reduction of the target trace to a wild local term at the unique `sigma`-fixed point is invalid. It studies `Tr(sigma)` rather than the required `Tr(sigma Frob_p)`.

### OPEN

The linear-section route still requires a genuine decomposition of the `sigma Frob_p` trace, for example an admissible Jacobi-sum/character-orbit decomposition of the `(1,3)` linear section. Ordinary localization at `Fix(sigma)` cannot provide it.

The global Airy cross-symmetric-power trace estimate therefore remains the cleanest exact formulation of the missing theorem.
