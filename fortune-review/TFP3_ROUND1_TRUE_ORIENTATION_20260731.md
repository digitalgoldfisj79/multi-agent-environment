# TFP3 Round 1: faithful classifier and extended true-orbit panel

**Date:** 31 July 2026  
**Research branch:** `gpt56/fortune-tfp3-true-frobenius-20260731`  
**Base:** `69271f1f2d71f10ba68b8d8dc5fb6ce303e382d8`  
**Paper VII freeze:** `069f47724a3581dc40cfbc9efa3fafd14181ba3e`

## Status

This round implements the first executable gate of issue #36. It does not use
the dimension or rational-point count of the q-free relaxation as an arithmetic
surrogate.

The exact classifier starts from the original inverse-free divisibilities,
quotients by the full affine action, and emits the unique gauge
`lambda=1`, `[t^2]P=0`. A second implementation reconstructs the actual
Frobenius cycles of all four irreducible cubics and verifies the
Frobenius--Vandermonde orientation equations.

## Exact checks

For every emitted orbit the verifier checks:

1. all four cubics are irreducible and pairwise distinct;
2. `rho` is nonzero and nonunit;
3. all four original inverse-free divisibilities hold;
4. the ordered-cycle numerator built from
   `eta_F=(x-x^q)(x-x^(q^2))(x^q-x^(q^2))`
   satisfies the four root-orientation equations;
5. restoring the affine orbit gives exactly `q(q-1)` incidences;
6. the normalized `rho` multiset is invariant under `rho -> rho^-1`.

The frozen panel through `q=59` is a regression contract, not evidence for a
uniform theorem.

## Extended exact panel

| q | normalized true orbits | raw incidences |
|---:|---:|---:|
| 61 | 6 | 21,960 |
| 67 | 12 | 53,064 |
| 71 | 10 | 49,700 |
| 73 | 8 | 42,048 |
| 79 | 8 | 49,296 |
| 83 | 14 | 95,284 |
| 89 | 18 | 140,976 |
| 97 | 16 | 148,992 |
| 101 | 24 | 242,400 |

Every raw count is exactly the normalized count times `q(q-1)`.

For the exact panel with `q>=29`, ordinary least squares gives slope
approximately `0.2455643` and `R^2 approximately 0.7951651`. This is an
**exact-finite-panel linear-growth alarm**, not a proof of asymptotic
linearity and not a formal refutation of `O(1)`.

## Frobenius sign cover

On the nondegenerate irreducible points enumerated at `q=11,13,17`, the
component invariant

`eta_A eta_D = eta_B eta_C`

holds, while the actual arithmetic incidence is exactly the sign class in
which all four oriented Vandermondes agree with their Frobenius orientation.
The observed sign patterns lie in the eight-element subgroup cut out by the
displayed relation. Thus the true locus is a single class of an explicit
eight-class sign cover, rather than a Zariski component of the relaxation.

## Decisive next theorem

The original bounded-point target can no longer be pursued by extrapolating
the small `q<=59` panel. The theorem-level discriminator is now:

1. identify the nondegenerate irreducible one-dimensional component or
   components of the oriented coefficient scheme;
2. construct the eight-class Frobenius-sign cover on their normalisations;
3. determine its geometric monodromy and fields of definition;
4. prove either:
   - positive-density Chebotarev growth for the all-positive sign class, which
     would give `delta q + O(sqrt(q))` normalized true points and formally
     refute `O(1)`; or
   - confinement of that sign class to a bounded exceptional locus.

Until that theorem is proved, the correct classification is:

- faithful classifier: **exact and verified**;
- extended counts: **empirical-exact finite panel**;
- linear growth: **strongly suggested, not proved**;
- `TFP3: O(1)`: **open and empirically disfavoured**;
- downstream amplitude, `FFPR`, crown and Fortune gates: **blocked**.
