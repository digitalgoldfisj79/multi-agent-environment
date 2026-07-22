# d=1 crown push — Phase Z interim status

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** first Route 1/2 computation completed; Routes 3/4 remain at structural-design stage.

## 1. Completed work

The Phase Z four-route programme has been frozen in

`D1_PHASE_Z_FOUR_ROUTE_PROGRAMME_20260722.md`.

An exact weight-resolved Cartier ledger has been implemented in

`cartier_weight_resolved_ledger.cpp`.

The first compute run used Hugging Face `cpu-xl`, job

`6a612671d09dc1f57c6c31b6`,

and completed in 58 seconds for `p=23,29,31`, both square classes of `a`, and both the dominant `w=1` matrix and complete `w=1,2,3,4` matrix.

The raw results are committed in

`cartier_weight_resolved_ledger_results_p23_p29_p31.json`.

## 2. Exact method

Set

`c=c0*t, d=d0*t^2`,

with `c0,d0 in F_p` and `t in F_(p^2)^*`.

Summation over `c0,d0` projects exactly onto positive exponents divisible by `p-1`. Multiplicative Fourier inversion in `t` then separates every exact `(1,2)`-filtration weight.

An exact Hungarian assignment calculation gives the maximal possible `t`-degree. In all cases this is below `p^2-1`, so the Fourier transform has no aliasing.

## 3. New structural result

The above-bound tail is sparse and stable under the lower filtration blocks.

### p=23

The old boundary is

`264=12(p-1)`.

For both square classes, the complete tail is zero. This recovers the finite p=23 support theorem.

### p=29

The old boundary is

`420=15(p-1)`.

There is exactly one nonzero tail level:

`448=16(p-1)=((p+3)/2)(p-1).`

Its values are:

- square class: `22 mod 29`;
- nonsquare class: `14 mod 29`.

These values are identical in the `w=1` ledger and complete `w=1,2,3,4` ledger.

### p=31

The old boundary is

`480=16(p-1)`.

There is again exactly one nonzero tail level:

`510=17(p-1)=((p+3)/2)(p-1).`

Its values are:

- square class: `10 mod 31`;
- nonsquare class: `12 mod 31`.

Again these values are identical in the `w=1` ledger and complete `w=1,2,3,4` ledger.

## 4. Consequence for Route 1

The p=29 counterexample does not produce a diffuse uncontrolled tail. In the first two primes where the former bound fails, the complete tail consists of one survivor level exactly one torus step above the old boundary.

The lower blocks `w=2,3,4` substantially rearrange the low-weight coefficients but leave this tail level unchanged.

This suggests a replacement theorem of the following form:

> The complete above-bound Cartier tail is supported on a short terminal band, whose top component is inherited unchanged from the dominant `w=1` block.

This is currently a finite pattern at p=29,31, not a theorem. The next Route 1 computation should test p=37,41,43 and derive the maximal torus-survivor levels from the substitution-minor formula.

## 5. Consequence for Route 2

The complete projected Cartier totals are nonzero in both square classes for all three audited primes:

- p=23: totals `13,8`;
- p=29: totals `21,23`;
- p=31: totals `28,1`.

Under the committed certificate normalisation `S_a=3aN_a mod p`, these imply nonzero residues for `N_a` in both square classes at these primes.

More importantly, the total is not controlled by the tail alone. For example at p=29 the square-class low part is `28` and tail is `22`, summing to total `21`; at p=31 the low and tail pieces are `18+10=28` and `20+12=1`.

Therefore a quantized nonvanishing theorem must control the interaction between the low block and the sparse terminal tail, rather than merely prove the tail nonzero.

## 6. Current route status

1. **Tail-inclusive Cartier assembly:** active and currently the strongest route. Exact ledger machinery is operational; sparse-terminal-tail pattern found at p=29,31.
2. **Quantized nonvanishing:** active. Complete residues are nonzero in the audited cases, but no uniform congruence has yet been identified.
3. **Geometric direct image:** not yet advanced beyond the existing exact extremal decomposition. Next task is a precise definition of the primitive remainder `P_q` and its involutions.
4. **Singular-series/mass formula:** not yet advanced beyond the exact linear-factor/rootless mass. Next task is the exact degree-2 factor incidence ledger.

## 7. Epistemic status

Exact:

- weight-resolved ledger method;
- p=23,29,31 coefficient tables;
- zero p=23 tail;
- single-level p=29 and p=31 tails;
- equality of dominant and full tail values in those cases;
- nonzero complete certificate residues in both square classes for p=23,29,31.

Conjectural:

- terminal-band support for general p;
- invariance of the complete tail under `w=2,3,4` for general p;
- any uniform nonvanishing consequence.

The function-field d=1 crown remains open.
