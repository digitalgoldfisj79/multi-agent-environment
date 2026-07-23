# Wild cyclic fixed-point audit on the smooth (2,3) model

**Date:** 2026-07-23  
**Corrected status:** the set-theoretic fixed locus, tangent obstruction and completed fixed scheme for the bare cyclic shift `sigma` are **PROVED**. However, localization at this fixed scheme is **NOT A VALID ROUTE TO THE TARGET TRACE**: the relevant operator is `sigma` composed with Frobenius. See `COMPLETED_FIXED_SCHEME_AND_CORRESPONDENCE_CORRECTION.md`.

## 0. Critical distinction

The calculations below concern `Fix(sigma)`. They correctly describe the geometry of the bare cyclic automorphism, but the trace defining the function-field problem is the trace of

\[
\sigma\circ\operatorname{Frob}_p.
\]

The latter has a completely different fixed locus: its fixed-point equations reconstruct the original `F_{p^p}` trace equations. Therefore the earlier proposal to compute one wild local term at the unique `sigma`-fixed point is withdrawn.

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

At `p=5`, the degree-four power sum is exceptional and the cubic tangent equation removes this direction.

## 4. PROVED: completed fixed scheme

The full calculation is in `COMPLETED_FIXED_SCHEME_AND_CORRESPONDENCE_CORRECTION.md`. The result is

\[
\widehat{\mathcal O}_{\operatorname{Fix}(\sigma,\mathbf P(W)),[v]}
\cong \overline{\mathbf F}_p[[t]]/(t^{p-2})
\]

and

\[
\boxed{
\widehat{\mathcal O}_{\operatorname{Fix}(\sigma,X_p),[v]}
\cong \overline{\mathbf F}_p[[t]]/(t^{p-4}).
}
\]

Hence the bare-shift fixed multiplicity is exactly `p-4`, not uniformly bounded.

## 5. CORRECTION: why this does not localize T_p

The relevant arithmetic operator is

\[
\Phi=\sigma\circ\operatorname{Frob}_p,
\]

not `sigma`. Its fixed equations are, up to orientation,

\[
x_{i+1}=x_i^p.
\]

Thus

\[
x_i=x_0^{p^i},\qquad x_0^{p^p}=x_0,
\]

and the defining equations become the original extension-field trace equations. In addition, `dFrob_p=0`, so `1-dPhi` is invertible: the nontransversality of `Fix(sigma)` is not the local obstruction for the target correspondence.

Therefore the earlier statement

> compute the wild local term of the unique thickened `sigma`-fixed point

is not a valid next step for proving the `T_p` estimate.

## 6. Correct remaining target

The linear-section route still needs an exact decomposition of the `sigma Frob_p` trace, such as a Jacobi-sum or character-orbit decomposition valid for the `(1,3)` linear section. The unique bare-shift fixed point does not supply such a decomposition.

The Airy formulation remains the cleanest exact statement of the missing theorem:

\[
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le C p^{(p+1)/2}.
\]

The fixed-scheme result is retained as a correct theorem and a failure certificate, not as a route to the target trace.
