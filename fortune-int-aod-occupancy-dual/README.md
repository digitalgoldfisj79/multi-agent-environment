# INT-AOD occupancy–dual programme

**Programme:** `FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1`  
**Date:** 5 August 2026  
**Base:** `831184e1ceb519803591eda441de2672dc8a9939`  
**Parent:** PR #53  
**Primary issue:** #54  
**State:** BUILT; NOT YET EXECUTED

## Single objective

Starting from the adaptive occupancy detector

\[
\mathcal O_X=\sum_{j<N}e^{-\tau_X Z_j},
\qquad
\tau_X=\frac{2\log N}{\gamma_{\min}},
\]

determine whether its all-orders information can be compressed into either:

1. a connected-cumulant estimate whose total remainder is smaller than the first-order prime-pair mass; or
2. a row-uniform parity-breaking dual certificate on the actual increasing primorial centres.

The programme must not reopen fixed-order moments, independent factor bands, ordinary lower sieves, Paper VII, direct function-field `d=1`, random-order derandomisation, reciprocal frames, or the superseded four-prime covariance campaign.

## Governing observation

A failed row has `Z_j=0` and contributes exactly one to `O_X`. Thus `O_X<1` excludes every failure. The expected prime-pair count is of order `X`, while `log N` is only of order `log X`; under a genuinely Poisson-like or cluster-controlled law the target would have an exponential margin. The difficulty is not scale but proving a selected-centre lower-tail statement without replacing it by an inaccessible list of raw moments.

## Primary route

Let `J` be uniform on the registered rows and write

\[
G_X(s)=\frac1N\sum_{j<N}s^{Z_j}.
\]

Then `O_X=N G_X(e^{-tau_X})`. The main lane seeks a direct connected expansion or zero-free cluster bound for `log G_X(s)` in which disconnected prime-tuple contributions cancel before estimates are taken.

## Secondary route

If the connected expansion cannot be made convergent at `s=e^{-tau_X}`, derive the exact rowwise Type I/II or bilinear hypothesis needed by a parity-breaking asymptotic sieve, and test that hypothesis at its true post-level ranges.

## Permitted terminal outcomes

- `PROVED_INT_AOD`;
- `REDUCED_TO_CONNECTED_CUMULANT_BOUND`;
- `REDUCED_TO_ROWWISE_PARITY_BREAKING_BILINEAR`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

No conditional or numerical result may be promoted to an unconditional theorem.