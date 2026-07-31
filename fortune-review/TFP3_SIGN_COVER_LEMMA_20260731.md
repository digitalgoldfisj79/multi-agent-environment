# TFP3 sign-cover lemma

**Date:** 31 July 2026  
**Status:** **THEOREM** on the separable cross-distinct cubic open locus.

## Statement

Let `A,B,C,D` be the four ordered cubic root cycles in the normalized
`lambda=1` q-free bilateral system, and let `eta_A,...,eta_D` be their
oriented Vandermondes. Then

\[
\eta_A\eta_D=\eta_B\eta_C.
\]

Consequently, after fixing the actual Frobenius orientation of each
irreducible cubic, every q-free oriented point has a sign vector

\[
(\sigma_A,\sigma_B,\sigma_C,\sigma_D)\in\{\pm1\}^4
\]

satisfying

\[
\sigma_A\sigma_D=\sigma_B\sigma_C.
\]

The allowed sign vectors form a group of order eight. The true arithmetic
incidence is the identity class `(1,1,1,1)`.

## Proof

Write `R_XY` for the product of all root differences from the roots of `X`
to the roots of `Y`. All such products are nonzero on the stated open locus.

Multiplying the three root equations in the `A` block gives

\[
\eta_A R_{AB}=R_{AC}.
\]

For the `C` block, the three explicit minus signs cancel the odd-degree
resultant-reversal sign, giving

\[
\eta_C R_{CD}=R_{AC}.
\]

The `B` and `D` blocks similarly give

\[
\eta_B R_{AB}=\rho^3 R_{BD},\qquad
\eta_D R_{CD}=\rho^3 R_{BD}.
\]

Eliminating the nonzero resultants yields

\[
\frac{\eta_A}{\eta_C}=\frac{R_{CD}}{R_{AB}}
=\frac{\eta_B}{\eta_D},
\]

and therefore the claimed identity.

For an irreducible separable cubic the two square roots of its discriminant
are the two orientations of its root cycle. Thus any q-free orientation
differs from the actual Frobenius orientation by one sign. Applying the
identity to both orientations gives the displayed sign relation. Its kernel
inside `{±1}^4` has eight elements, and equality with the actual Frobenius
cycles is precisely the all-positive class. QED.

## Coefficient audit

For a monic cubic `F=t^3+a t^2+b t+c` and oriented variable `e`, the
coefficient-cycle numerator `N_e` satisfies the exact norm factorization

\[
\operatorname{Res}_t(F,N_e)-e^4
=-\frac{(e^2-\operatorname{disc}F)Q(a,b,c,e)}{8},
\]

where

\[
Q=4a^3c-2a^3e-a^2b^2-18abc+9abe+4b^3+27c^2-27ce+8e^2.
\]

The companion script verifies this factorization, the resultant elimination
above, and the eight-element sign kernel exactly.

## Consequence and boundary

This lemma removes the ambiguity between the q-free orientation variety and
the true arithmetic locus: the latter is one class of a finite degree-eight
sign cover.

It does **not** determine whether that class has bounded support or positive
Chebotarev density on any surviving component. Component normalisation,
geometric monodromy and point density remain open.
