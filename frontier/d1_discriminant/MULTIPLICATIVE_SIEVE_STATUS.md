# Multiplicative parity-sieve status

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`

## Closed single-factor levels

The locally admissible quadratic and cubic incidence levels are proved:

`L_(a,2) = p^2/6 + O(p)`

`L_(a,2)^chi = O(p^(3/2))`

`L_(a,3) = p^2/9 + O(p^(3/2))`

`L_(a,3)^chi = O(p^(3/2))`.

Thus both discriminant-parity sectors carry the expected first-order density of degree-two and degree-three factors.

## Closed quadratic multiplicative level

For a fixed family member, traces of irreducible quadratic factors satisfy

`a s^3 - (2-c)s - d = 0`.

Hence there are at most three such factors. Their complete and locally admissible factorial moments are now controlled through order three, including signed versions.

Exact finite inclusion-exclusion gives

`N_(a,no2) = 29p^2/144 + O(p^(3/2))`

and

`M_(a,no2) = O(p^(3/2))`,

where `N_(a,no2)` counts locally admissible members with no irreducible quadratic factor and `M_(a,no2)` is their discriminant-character mass.

Consequently

`N_(a,no2,+) = 29p^2/288 + O(p^(3/2))`

and

`N_(a,no2,-) = 29p^2/288 + O(p^(3/2))`.

This is the first exact multiplicative deletion in the parity sieve. It removes all quadratic factors, including simultaneous pairs and triples.

## What remains

The full d=1 theorem still requires removal of every factor degree from three through `floor(p/3)` inside the positive-discriminant sector.

There are two viable continuations:

1. Prove a uniform finite-degree description of the cubic-factor map and close its complete factorial sieve, including mixed moments with the quadratic deletion weight.
2. Prove the top-coefficient nonvanishing of the exact Frobenius determinant indicator, which would bypass all factor-by-factor sieving.

The determinant route remains shorter if its top coefficient can be evaluated. The multiplicative route is now demonstrably finite at degree two and provides a rigorous fallback architecture.
