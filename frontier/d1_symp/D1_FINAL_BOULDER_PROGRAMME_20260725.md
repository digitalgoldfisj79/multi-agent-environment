# Final boulder programme for function-field `d=1`

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Target:** prove FF-Fortune `(p,1)` for every prime `p`, equivalently prove that for every `p>=3` some offset `m` of degree `2` or `3` makes `T^p-T+m` irreducible.

## 1. Authoritative dependency graph

The proof now has two load-bearing inputs.

### Analytic boulder

For the Hayes coefficients

\[
I_p(u,w,v)=\sum_{\deg P=p\atop P\ \mathrm{irreducible}}
\chi(n(P))\psi(us_1(P)+ws_3(P)+vr_1(P)),
\]

put

\[
\mathcal A_p=\sum_{u,w}I_p(u,w,1),\qquad
\mathcal B_p=\sum_{u,v}I_p(u,1,v).
\]

The proved Salié/Hayes reduction gives

\[
T_p^2=
\frac{p^{(p-1)/2}}{G_p}
\left(\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p\right).
\]

The exact analytic target is

\[
\boxed{
|\chi(-1)\mathcal A_p+\chi(3)\mathcal B_p|
\ll p^{p/2}
}
\]

with an absolute constant.

### Application boulder

The full Fourier-delta theorem has already eliminated all first `p-4` coefficient directions on the full derived complex, including the nonsplit Jordan extensions. The residual object is exactly the alternating-hook complex of the cubic-tail root cover

\[
T^p+AT^3+BT^2+CT+D.
\]

The remaining application theorem must identify the distinguished Airy constituent and every Tate, affine, discriminant, `q=2`, `q=infinity`, invariant and quadratic-projector boundary term inside that residual complex, for all Frobenius powers.

## 2. Sequence

1. Construct the universal Hayes sheaf and determine its exact rank and boundary loci.
2. Formulate the signed `p`-th Adams object whose parameter-plane trace is the analytic target.
3. Compute its virtual rank, local inertia and conductor ledger.
4. **Gate:** if a bounded-complexity realization exists, apply Deligne; if complexity is `Omega(p)` after the signed combination, close the simple Hayes-sheaf route and return to the equivalent projective character sum.
5. In parallel, construct the cubic-tail localization/projector diagram, but do not invest in final assembly until the analytic gate passes.
6. Join the analytic estimate to the exact class-count ledger and derive an explicit finite cutoff.
7. Use exact computation only for primes below that cutoff.

## 3. Closed distractions

No further effort without a new theorem should go to:

- broad prime sweeps;
- boundary-only positivity;
- proper cyclotomic subfield descent;
- affine-normalizer fixed-locus searches;
- new configuration face complexes;
- compatible oscillator models not derived from the actual cubic-tail complex;
- manuscript polishing before the two boulders are resolved.

## 4. Stop rules

A route stops only at one of:

- a proof of the required theorem;
- a rigorous no-go theorem for the proposed mechanism;
- an exact reduction to a strictly smaller new theorem;
- a theorem-level obstruction requiring genuinely new mathematics.

This file supersedes earlier programme descriptions that treated clean Fourier elimination through the first `p-4` directions as open.