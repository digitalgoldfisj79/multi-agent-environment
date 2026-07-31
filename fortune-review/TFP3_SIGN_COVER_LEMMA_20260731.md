# TFP3 orientation identity and corrected sign-torsor statement

**Date:** 31 July 2026  
**Status:** **THEOREM** on the separable cross-distinct cubic open locus; sign-cover consequence corrected after the literature-transfer audit.

## 1. Exact orientation identity

Let `A,B,C,D` be the four ordered cubic root cycles in the normalized
`lambda=1` q-free bilateral system, and let `eta_A,...,eta_D` be the
oriented Vandermondes used in that system. Then

\[
\eta_A\eta_D=\eta_B\eta_C.
\]

Write `R_XY` for the product of all root differences from the roots of `X`
to the roots of `Y`. On the cross-distinct open locus these resultants are
nonzero. Multiplication of the three root equations in each block gives

\[
\eta_A R_{AB}=R_{AC},\qquad
\eta_C R_{CD}=R_{AC},
\]

and

\[
\eta_B R_{AB}=\rho^3R_{BD},\qquad
\eta_D R_{CD}=\rho^3R_{BD}.
\]

Eliminating the nonzero resultants proves the identity. This part of the
original lemma is unchanged.

## 2. Correction: two sign torsors, not one global eight-class cover

For each irreducible cubic, let `eta_X^F` be its actual Frobenius-oriented
Vandermonde and write

\[
\eta_X=\sigma_X\eta_X^F,\qquad \sigma_X\in\{\pm1\}.
\]

Define the base Frobenius invariant

\[
\kappa=
\frac{\eta_A^F\eta_D^F}{\eta_B^F\eta_C^F}
\in\{\pm1\}.
\]

The q-free identity implies

\[
\sigma_A\sigma_D=\kappa\,\sigma_B\sigma_C.
\]

Thus:

- over the base locus `kappa=+1`, the admissible relative signs form the
  eight-element kernel `sigma_A sigma_D=sigma_B sigma_C`;
- over `kappa=-1`, they form the disjoint eight-element coset
  `sigma_A sigma_D=-sigma_B sigma_C`;
- the true arithmetic class `(1,1,1,1)` can occur only over `kappa=+1`.

The earlier wording incorrectly treated the `kappa=+1` kernel as a globally
regular degree-eight cover of the whole q-free relaxation. That conclusion
did not follow, because the actual Frobenius orientations need not themselves
satisfy the q-free endpoint equations.

## 3. Exact symbolic audit

For a monic cubic `F=t^3+a t^2+b t+c` and oriented variable `e`, the
coefficient-cycle numerator `N_e` satisfies

\[
\operatorname{Res}_t(F,N_e)-e^4
=-\frac{(e^2-\operatorname{disc}F)Q(a,b,c,e)}8,
\]

where

\[
Q=4a^3c-2a^3e-a^2b^2-18abc+9abe+4b^3+27c^2-27ce+8e^2.
\]

The companion script verifies this factorization, the resultant elimination,
and the two disjoint eight-element sign torsors exactly.

## 4. Correct Chebotarev gate

A finite-cover argument now requires more than the orientation identity:

1. identify and normalize the faithful true-Frobenius base curve;
2. prove that `kappa` is constant, or classify its divisor, on each component;
3. construct the relative-sign torsor on the `kappa=+1` open locus;
4. prove finite etaleness, geometric connectedness and monodromy there;
5. only then apply effective finite-field Chebotarev to the all-positive class.

No point-density theorem follows from the orientation identity alone.
