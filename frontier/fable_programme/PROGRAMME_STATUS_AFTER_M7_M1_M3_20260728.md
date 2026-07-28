# Programme status after executing M7, M1 and M3

Date: 28 July 2026

## Completed

### M7: function-field source/frame laboratory

A complete-ordering laboratory was built over `F_3[T]` at `d=3`.

- All 40,320 orderings were evaluated.
- The true irreducible-offset detector was computed exactly at all 255 nonempty centres.
- Raw unweighted single-walk and pair-sum reciprocal energies had only weak correlation with detector variance.
- The correctly residual-weighted source energy had Pearson and Spearman correlations above `0.997` in every independent run, and above `0.999` in the main 2,048-shell-pair run.

Ruling: the old raw frame is not a strong detector proxy in this laboratory. A corrected bridge must retain the detector residual weights and principal subtraction through the harmonic transformation.

### M1: skew-Frobenius theorem package

The arithmetic-dynamical correspondence is now proved cleanly:

- Frobenius equals the explicit low-degree map on the root set;
- factor degrees equal dynamical cycle lengths;
- irreducibility is equivalent to a single `p`-cycle;
- bounded-period gcd tests give an exact criterion;
- `F_p`-affine conjugacy preserves the cycle partition;
- rational fixed points exclude power and Dickson/Chebyshev conjugacy classes.

Ruling: this yields a structural exclusion theorem, not yet a universal positivity mechanism. The crown lies on the non-special cubic locus.

### M3: p-adic implication audit

A new exact theorem was obtained:

`W_p=0  <=>  #Q_p(F_p) congruent 1 mod p^2`.

The proof uses the exact compactified count and the unconditional bound `0<=W_p<=p^2-1`.

Ruling: length-two Witt or rigid-cohomology information is sufficient in principle. Newton polygons or nonzero unit-root rank alone are insufficient because slopes do not determine trace coefficients.

## Updated priority

1. **Depth-two quotient trace:** construct a cohomological formula for `#Q_p(F_p) mod p^2`, with explicit treatment of the isolated wild quotient point.
2. **Source-weighted transference:** on the integer side, start from the correctly centred detector residuals and derive the harmonic kernel without discarding the weights. Do not begin from the old unweighted pair-sum frame.
3. **Non-special dynamical locus:** formulate and test monodromy/cycle statistics for cubic maps after removing affine power and Dickson/Chebyshev conjugacy classes.
4. **Robustness extensions:** repeat the M7 laboratory at a second field/degree and reproduce the reported `N_2` census from committed code.

## Closed or demoted

- universal quadratic witness `N_2(p)>=1`;
- raw-frame derandomisation as a direct route to Fortune;
- sorted-order extremality;
- generic ordinarity or slope nondegeneracy without a trace comparison;
- power/Chebyshev integrable witnesses.

## Current theorem boundary

The strongest new route is now precise:

> Prove that the compactified Kummer/root-cycle quotient satisfies
> `#Q_p(F_p) != 1 mod p^2` for every admitted prime.

Equivalently, compute a depth-two compactly supported Frobenius coefficient that excludes the zero-count residue.

The integer conjecture remains open, and no theorem currently connects the old unweighted reciprocal frame to the corrected prime-pair detector.
