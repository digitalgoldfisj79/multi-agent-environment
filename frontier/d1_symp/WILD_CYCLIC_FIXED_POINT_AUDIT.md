# Wild cyclic fixed-point audit on the smooth (2,3) model

**Date:** 2026-07-23  
**Status:** set-theoretic fixed locus and tangent obstruction are **PROVED**. A wild local-term formula remains **OPEN**.

## 1. The cyclic module

Over `Fbar_p`, let `V` be the `p`-dimensional coordinate permutation module for the cyclic shift `sigma`. Let

\[
H=\{(x_i):\sum_i x_i=0\},\qquad L=\mathbf F_p(1,\ldots,1),\qquad W=H/L.
\]

Because the characteristic is `p`, the constant line lies in `H`. As a module for `N=sigma-1`, the regular permutation module is one Jordan block of length `p`; consequently `W` is one Jordan block of length `p-2`.

In particular,

\[
\dim W^{\sigma}=1.
\]

A representative of the fixed line is

\[
v=(0,1,2,\ldots,p-1),
\]

up to reversing the cyclic convention and adding a constant vector.

## 2. PROVED: unique set-theoretic fixed point

The descended quadratic and cubic forms are

\[
Q=\sum_i x_i^2,\qquad C=\sum_i x_i^3.
\]

For `p>=5`, the standard power-sum identities give

\[
Q(v)=\sum_{i\in\mathbf F_p}i^2=0,
\qquad
C(v)=\sum_{i\in\mathbf F_p}i^3=0.
\]

Therefore the unique projective fixed line `[v]` lies on

\[
X_p=\{Q=C=0\}\subset\mathbf P(W).
\]

Since `W^sigma` is one-dimensional, `[v]` is the only geometric fixed point of `sigma` on `P(W)`, hence also the only set-theoretic fixed point on `X_p`.

## 3. PROVED: the fixed point is non-transverse for p>=7

The tangent space to `P(W)` at `[v]` is `Hom(<v>,W/<v>)`. Since `W` is a single Jordan block, the fixed tangent subspace is one-dimensional. A concrete generalized eigenvector is represented by

\[
y_i=\binom{i}{2},
\]

because its cyclic finite difference is linear in `i`, hence equals `v` modulo the constant line and cyclic-convention sign.

The tangent equations of `X_p` at `v` are

\[
dQ_v(y)=2\sum_i i\binom{i}{2},
\qquad
dC_v(y)=3\sum_i i^2\binom{i}{2}.
\]

The first summand is a polynomial in `i` of degree three. The second is a polynomial of degree four. For `p>=7`, both degrees are strictly below `p-1`, so their sums over `F_p` vanish:

\[
dQ_v(y)=dC_v(y)=0.
\]

Thus the unique fixed point has a nonzero fixed tangent vector on `X_p` for every `p>=7`.

Equivalently, the scheme-theoretic fixed locus is nonreduced at `[v]`; the graph of `sigma` and the diagonal do not meet transversely.

At `p=5`, the degree-four power sum is exceptional and the cubic tangent equation may remove this direction. This small-prime exception is irrelevant to the general obstruction.

## 4. Consequence for Route 2

The tempting argument

> one fixed point implies a bounded Lefschetz local term

is invalid. The automorphism has order equal to the characteristic, is unipotent on the tangent representation, and its unique fixed point is wild and non-transverse. Ordinary semisimple or transverse Lefschetz formulas do not apply.

Any successful fixed-point proof must compute the full wild local term of this thickened fixed point and prove that its Frobenius-weight-normalized contribution is bounded independently of `p`.

## 5. Smallest next theorem

Determine the completed local ring of the fixed scheme of `sigma` on `X_p` at `[v]`, or at least its intersection multiplicity and the induced Artin--Schreier local system. Then apply a wild Lefschetz--Verdier or arithmetic Picard--Lefschetz formula.

The key decision criterion is:

- if the local multiplicity/local term is uniformly bounded after the required cancellation, Route 2 may prove the theorem;
- if it grows with `p` without a further signed cancellation, fixed-point localization alone cannot prove the absolute-constant bound.

This is now the exact local calculation required by the cyclic linear-section route.