# Wild-infinity residue interpretation of the sparse symplectic form

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** local wild-infinity geometry of the sparse frequency quotient.  
**Status:** **PROVED**. This identifies the symplectic form geometrically; it does not yet compute the vanishing-cycle complex.

## 1. Principal parts at infinity

Let

\[
\mathcal V_p=k[T]_{\le p-4}/k[T]_{\le3}
\]

and use the local coordinate

\[
z=T^{-1}
\]

at root infinity. For a polynomial phase `f(T)`, write its principal part

\[
F(z)=f(z^{-1}).
\]

For two classes represented by `f,g`, define

\[
\Omega_p(F,G)
=
\operatorname{Res}_{z=0}
\left[
 z^p(F\,dG-G\,dF)
\right].
\]

## 2. Equality with the Wronskian pairing

For monomials

\[
f(T)=T^a,
\qquad
g(T)=T^b,
\]

one has

\[
F=z^{-a},
\qquad G=z^{-b},
\]

and therefore

\[
F\,dG-G\,dF
=(a-b)z^{-a-b-1}dz.
\]

Multiplication by `z^p` has a residue exactly when `a+b=p`. Hence

\[
\Omega_p(z^{-a},z^{-b})
=(a-b)\mathbf1_{a+b=p}.
\]

This is the monomial formula for the previously proved Wronskian form

\[
\omega_p(f,g)
=[T^{p-1}](f'g-fg').
\]

Thus

\[
\boxed{
\omega_p(f,g)
=
\operatorname{Res}_{z=0}
 z^p(F\,dG-G\,dF).
}
\]

## 3. Why the characteristic boundary is essential

The factor

\[
z^p
\]

is Frobenius-flat in characteristic `p`:

\[
d(z^p)=0.
\]

This is the local characteristic-boundary feature behind the pairing. Complementary pole orders `a` and `p-a` pair because their total wild order is exactly `p`.

The cubic multiplier subspace has pole order at most three. It is in the radical because a pole of order at most three cannot pair with the largest sparse pole order `p-4` to total `p`. Quotienting by the cubic multipliers therefore leaves the nondegenerate sparse form.

## 4. Lagrangian slope cutoff

The intrinsic Lagrangian

\[
\mathcal L_p
=
\operatorname{span}
\{T^4,\ldots,T^{(p-1)/2}\}
\]

is the subspace of principal parts with pole order at most `(p-1)/2`. Two such pole orders cannot sum to `p`, so the residue pairing vanishes on it. Every higher pole order `p-a` is paired with one lower pole order `a`.

Thus the half-codimension cutoff in the target Airy twist is exactly the midpoint of the wild pole-order pairing.

## 5. Compatibility with affine root changes

Translation of roots

\[
T\mapsto T+b
\]

induces a triangular change of principal parts at infinity. The residue form is unchanged. Equivalently, in polynomial coordinates, possible changes to the coefficient of `T^(p-1)` involve binomial coefficients

\[
\binom n{p-1},
\qquad p\le n\le2p-9,
\]

which vanish modulo `p` by Lucas' theorem.

Root scaling acts conformally with the value character `a^p`, as already proved for the Wronskian presentation.

## 6. Consequence

The symplectic polarization is now tied directly to the wild-infinity principal-part geometry of the Smith-defect phase. It is not merely an abstract form placed on a vector space of the correct dimension.

The remaining statement is still nontrivial:

> identify the integral cyclic trivial-minus-nontrivial vanishing-cycle complex of this residue-paired principal-part space with the oscillator complex induced from the lower-pole Lagrangian.

The residue theorem supplies the canonical symplectic input for that calculation but does not replace it.

## 7. Verification

The monomial residue formula, nondegeneracy, affine invariance and Lagrangian cutoff are verified by

`frontier/d1_symp/sparse_frequency_symplectic_verify.py`.
