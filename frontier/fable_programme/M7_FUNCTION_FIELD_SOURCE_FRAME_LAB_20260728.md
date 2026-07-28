# M7 execution: function-field source/frame laboratory

Date: 28 July 2026

## Purpose

The corrected integer Papers II--III reopen the source-to-frame bridge. The old reciprocal pair-sum frame is internally valid, but no theorem currently connects it to the correctly centred prime-pair detector. Mechanism M7 proposed testing the complete architecture in a finite polynomial laboratory before investing further in derandomisation.

This document records that test.

## Exact finite model

Work in `F_3[T]` and fix a degree `d`.

- Let `A_d` be the product of all monic irreducibles of degree less than `d`.
- Let `pi_1,...,pi_K` be the monic irreducibles of degree `d`.
- For a nonempty subset `S`, put

  `P_S = A_d product_{i in S} pi_i`.

- The exact candidate-collapse window consists of monic irreducible offsets of degrees `d,...,2d-1`. Any reducible offset of degree below `2d` that is coprime to `P_S` would require two factors of degree at least `d`, which is impossible.
- Define the true detector

  `Z(S) = #{m monic irreducible : d <= deg m < 2d, P_S+m irreducible}`.

For a permutation `sigma`, its path consists of nested prefix subsets `S_1,...,S_K`. The deterministic rank baseline is

`lambda_s = average_{|S|=s} Z(S)`,

and the exact path detector variance is

`V(sigma) = sum_s (Z(S_s)-lambda_s)^2`.

The reciprocal shell consists of monic irreducibles `Q,R` of degree `2d`. For a polynomial `B`, the additive character at infinity is determined by the coefficient of `T^{-1}` in `B/Q`; this is the coefficient of `T^{2d-1}` in the remainder of `B mod Q`.

The laboratory measures four unweighted quantities:

1. the mean centred pair-sum kernel `|H_2|^2-M`;
2. its squared value;
3. the corresponding single-walk kernel;
4. its squared value.

It also measures the source-weighted energy

`E_src(sigma) = average_{Q != R} |sum_s (Z(S_s)-lambda_s) psi((1/Q-1/R)P_{S_s})|^2`.

The last expression retains the actual detector residuals. It is the finite analogue of a signed source frame rather than the old unweighted geometric frame.

## Complete ordering experiment at q=3, d=3

The model has:

- `K=8` degree-3 irreducibles;
- all `8! = 40,320` orderings;
- `255` nonempty centres;
- `74` irreducible candidate offsets of degrees 3, 4 and 5;
- `116` shell irreducibles of degree 6.

One main run used 2,048 shell pairs sampled without replacement. Four further independent runs used 512 shell pairs each.

### Main 2,048-pair run

Correlation with the exact detector variance:

| statistic | Pearson | Spearman |
|---|---:|---:|
| unweighted pair-frame mean | 0.031825 | 0.049078 |
| unweighted pair-frame squared energy | 0.027316 | 0.049348 |
| unweighted single-walk mean | 0.033957 | 0.049033 |
| unweighted single-walk squared energy | 0.031543 | 0.052995 |
| **source-weighted energy** | **0.999376** | **0.999280** |

### Four independent 512-pair runs

The source-weighted Pearson correlation lay in

`[0.997893, 0.998151]`,

with mean `0.998033`. Its Spearman correlation lay in

`[0.997757, 0.998012]`.

Across the same runs, the mean raw correlations were only:

- pair mean: `0.055990`;
- pair squared energy: `0.036517`;
- single mean: `0.062381`;
- single squared energy: `0.050073`.

The signs and magnitudes of the raw correlations varied with the shell sample; none exceeded `0.103` in absolute value in these four runs.

## Exact interpretation

For a complete additive dual of a finite vector space, character orthogonality gives the Parseval identity

`average_chi |sum_j w_j chi(P_j)|^2 = sum_j |w_j|^2`

when the centres are distinct. The near-perfect correlation of `E_src` with `V` is therefore the expected finite-shell shadow of the canonical weighted Fourier identity.

The old unweighted single-walk and pair-sum frames discard the residual weights `Z-lambda`. In this laboratory they explain less than approximately one percent of the ordering-to-ordering detector variance. The source-weighted frame recovers essentially all of it.

## Ruling

1. **M7 succeeds as a programme decision gate.** The raw unweighted reciprocal frame is not a strong detector proxy in the first nontrivial complete-ordering laboratory.
2. This does **not** prove that no corrected source-to-frame theorem can ever produce the old pair-sum kernel after a deeper expansion. It proves that such a bridge must contain a substantial signed, source-dependent transformation; it cannot be justified by treating the raw frame as intrinsically predictive.
3. The next integer bridge should begin from the residual-weighted source and derive every subsequent kernel with the weights and principal subtraction visible. Derandomising Paper IV before doing this remains incorrectly sequenced.
4. The finite laboratory should next be extended to `q=3,d=4` or to additional prime fields using sampled orderings. That is a robustness extension, not a prerequisite for the present negative result.

## Reproducibility

- `ff_source_frame_lab.cpp` implements finite-field arithmetic, exact irreducibility, all-ordering enumeration and the reciprocal measurements.
- `ff_source_frame_main_results.json` records the 2,048-pair run.
- `ff_source_frame_multiseed_results.json` records the independent 512-pair runs and ranges.

The computation is exact once the shell-pair sample is fixed. No asymptotic claim is inferred from the finite data.
