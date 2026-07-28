# M7 cross-field robustness correction

Date: 28 July 2026

## Why this correction was required

The first complete-ordering laboratory over `F_3[T]` encoded the single-walk phase through the diagonal pair-sum `P+P=2P`. Over `F_3`, multiplication by two merely conjugates the nontrivial additive character, so every absolute-square statistic is unchanged. This is why the original `q=3,d=3` results and their validation were correct.

That implementation is not portable to characteristic two: there `P+P=0`, so the purported single-walk phase collapses. A first `F_2` robustness run exposed this defect immediately.

The corrected laboratory now stores two distinct residues:

- `residue(P_i+P_j mod Q)` for the pair-sum frame;
- `residue(P_i mod Q)` for the single-walk and source-weighted frame.

It also computes additive-character absolute squares using the correct character table for the selected prime field rather than the hard-coded `F_3` formula.

## Complete robustness laboratory over F_2[T]

Parameters:

- field: `F_2`;
- block degree: `d=5`;
- degree-5 block irreducibles: `K=6`;
- all `6!=720` orderings;
- all `63` nonempty centres;
- irreducible candidate offsets of degrees `5,...,9`: `119`;
- shell irreducibles of degree ten: `99`;
- **all** unordered shell pairs: `4,851`.

Correlations with the exact detector variance:

| statistic | Pearson | Spearman |
|---|---:|---:|
| raw pair-frame mean | -0.06135757 | -0.04675073 |
| raw pair-frame squared energy | -0.04591810 | -0.03030591 |
| raw single-walk mean | -0.06240673 | -0.04811530 |
| raw single-walk squared energy | -0.05404695 | -0.03739016 |
| **residual-weighted source energy** | **0.99960557** | **0.99943780** |

The identity ordering is bulk-typical for the true detector variance, at percentile `46.39`.

## Cross-field ruling

The corrected source/frame conclusion now holds in two distinct complete-ordering laboratories:

1. `F_3,d=3`: 40,320 orderings, weighted-source Pearson `0.99937643`;
2. `F_2,d=5`: 720 orderings and the complete shell, weighted-source Pearson `0.99960557`.

In both fields every raw single-walk or pair-frame correlation has magnitude below `0.15`, while the correctly residual-weighted source energy exceeds `0.999`.

This materially strengthens the M7 ruling:

- the raw unweighted frame is not an intrinsic proxy for detector variance in either laboratory;
- the detector residuals are the load-bearing Fourier coefficients;
- any integer source-to-frame theorem must retain those signed weights and its principal subtraction until a proved transformation removes them.

The result remains a finite laboratory statement. It does not prove that a deeper analytic expansion can never produce the old pair-sum kernel, and it does not prove Fortune's conjecture.

## Reproducibility

`generalize_ff_source_frame_lab.py` transforms the original validated `F_3` implementation into a prime-field command-line implementation with separate pair and single residues. CI regenerates the code, reruns the original `F_3,d=3` regression, runs the complete `F_2,d=5` robustness laboratory, and compares both outputs to `ff_source_frame_crossfield_results.json`.
