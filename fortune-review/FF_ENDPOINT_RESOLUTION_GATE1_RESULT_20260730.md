# FERP-0.1 Gate 1 result — exceptional sampled diagonal route closed

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Gate:** 1 — sampled-diagonal discriminator

This note is the authoritative Gate 1 status update for `FF_ENDPOINT_RESOLUTION_PROGRAMME_V0_1_20260730.md`. Where it conflicts with the two-route wording in the earlier mechanism map, this note supersedes it.

## Decision

`SAD_FF` is **FALSIFIED AS A UNIFORM POINTWISE ROUTE**.

For the endpoint subfamily `k=2`, `m=3`, odd `q`, exact projective occupancy gives

`sum_{theta!=0} M_samp(theta) >= (q-3)/2 M_full`.

Keating--Rudnick's literal fixed-degree, large-field variance theorem gives

`M_full=(1/2+o(1))q^7`.

Therefore

`max_{theta!=0} M_samp(theta) >= (1/4+o(1))q^7`,

which exceeds the Route A allowance `q^(3k)poly(k,m)=q^6 O(1)` by a power of `q`.

This closes the preregistered uniform theorem

`M_samp(theta) << q^(3k) poly(k,m)`

for every nonzero canonical `theta`.

Full proof: `FF_ROUTE_A_CLOSED_BY_PROJECTIVE_OCCUPANCY_20260730.md`.

## What is and is not closed

### CLOSED

- exceptional sampled-diagonal Route A as a uniform pointwise endpoint strategy;
- attempts to obtain endpoint `FFPR` by combining ordinary post-Cauchy class control with a uniformly tiny deterministic sampled mass;
- further generic sampled-variance experiments as a claimed endpoint proof route.

### NOT CLOSED

- corrected endpoint `FFPR`;
- centered bilateral Route B;
- the possibility of special cancellation after theta summation, unless it is retained inside the exact signed endpoint ledger;
- fixed-`q`, growing-`k` sampled-mass asymptotics as an independent question;
- any integer theorem.

## Revised programme state

The endpoint programme now has one main route:

```text
Gate 2: bilateral incidence classification
   -> Gate 3: exact signed component contributions, including Delta_PS
   -> Gate 4: centered bilateral identity before positivity
   -> Gate 5: residual bilinear/sheaf estimate
   -> Gate 6: corrected endpoint FFPR
```

The Route A discriminator remains in CI as a closed-route audit. It is not an active theorem programme.

## Next mandatory tasks

1. enumerate the two exceptional `(q,k)=(3,4)` affine orbits with all scalar completion constants;
2. derive invariant polynomial relations rather than infer structure from orbit size;
3. compute their literal signed contribution, including transpose/Galois/affine pairing and `Delta_PS` interaction;
4. determine whether they are a forced main term, paired main term, degenerate residual or negligible finite-characteristic artifact;
5. use that classification in the first exact centered bilateral identity.

No sheaf construction should begin before Tasks 1--4 are complete.

## Status vocabulary

### PROVED EXACTLY

- the degree-two projective occupancy theorem;
- the exact theta-average lower inequality;
- the algebraic reduction from sampled frequency to irreducible-translate directions.

### PROVED FROM PUBLISHED INPUT

- `M_full=(1/2+o(1))q^7` in the stated degree-two family;
- the consequent lower bound for `max_theta M_samp`;
- failure of uniform `SAD_FF`.

### MACHINE-VERIFIED IDENTITY / EMPIRICAL-EXACT FINITE PANEL

- occupancy histograms and exact sampled-mass ledgers at the committed finite parameters.

### OPEN

- `BIC_FF`, exact exceptional-component contribution, `CBI_FF`, `RBK_FF`, corrected endpoint `FFPR`, and every later transfer/thinning/integer gate.
