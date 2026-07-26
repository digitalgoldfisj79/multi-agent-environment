# d=1 boulders-first execution programme

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Target:** prove FF-Fortune `(p,1)` for every prime `p`, equivalently produce an irreducible

\[
T^p+aT^3+bT^2+cT+d,
\qquad (a,b)\ne(0,0),
\]

over `F_p` for every `p>=3`.

## 1. Frozen dependency graph

The proof is separated into two load-bearing theorems.

### Analytic boulder

For the Hayes prime-degree coefficients

\[
I_p(u,w,v)
=-\frac1p\sum_j\alpha_j(u,w,v)^p,
\qquad d(u,w,v)\le4,
\]

prove

\[
\boxed{
\left|
\chi(-1)\sum_{u,w}I_p(u,w,1)
+
\chi(3)\sum_{u,v}I_p(u,1,v)
\right|
\ll p^{p/2}
}
\]

with an absolute constant.

This is exactly equivalent to the required Airy estimate.

### Application boulder

Inside the already reduced cubic-tail root complex, identify the Airy constituent and all Tate, affine, discriminant, `q=2`, `q=infinity`, invariant and quadratic boundary constituents at the level of Weil objects and all Frobenius powers.

The global Fourier-delta theorem has already eliminated the first `p-4` coefficient directions on the full derived complex. No further pre-elimination configuration or oscillator construction is part of the programme.

## 2. Execution order

### Phase A: analytic kill gate

1. Construct the universal rank-four Hayes sheaf
   \[
   \mathscr H=R^1\pi_!
   \left(
   \mathcal L_\chi(x)\otimes
   \mathcal L_\psi(wx^3+ux+v/x)
   \right).
   \]
2. Express the two parameter-plane families as `v=1` and `w=1` restrictions.
3. Use root scaling to reduce their signed combination to one `w=1` family with a quadratic projector in `v`, plus explicit one-dimensional boundary terms.
4. Compute the generic rank, degree-drop locus, discriminant, inertia and Swan ledger of the combined `p`-th Adams object.
5. **Pass:** bounded compactly supported Betti sum independent of `p`; then apply Deligne.
6. **Fail:** prove an `Omega(p)` uncancelled conductor contribution and close the Hayes route. Move immediately to the equivalent projective reciprocal-trace theorem.

### Phase B: application comparison, run in parallel at lower allocation

1. Build the global cubic-tail coefficient-space localization diagram.
2. Apply the cyclic trivial-minus-nontrivial and arithmetic square-class projectors.
3. Track the exact cubic-origin Airy object through the generic chart and every boundary.
4. Require all-power identities and the existing `p=5,7,11,53,71` regressions.

### Phase C: assembly

Only after both boulders pass:

1. convert the Airy estimate into bounds for `S_0 plus/minus S_chi`;
2. insert them into the exact class-count formula;
3. use positivity or the parity certificate;
4. derive an explicit finite cutoff;
5. machine-certify only the finite remainder.

## 3. Work explicitly stopped

No effort is to be spent on:

- broad prime sweeps;
- boundary-only witness searches;
- new canonical face complexes;
- further compatible oscillator models detached from the actual cubic-tail complex;
- affine-normalizer fixed-locus searches;
- cyclotomic subfield compression;
- paper polishing before theorem closure.

## 4. Immediate theorem gates

The first theorem gate is the universal Hayes sheaf and the exact scaling/projector reduction. The second is the complete ramification ledger of its signed `p`-th Adams object.

The programme stops only at:

- proof of the correlation theorem;
- a theorem-level conductor obstruction closing the Hayes route;
- proof of the application comparison;
- or a precisely isolated new theorem not reducible by the committed methods.
