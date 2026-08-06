# INT-PFLI signed-duality and occupancy programme

**Programme:** `FORTUNE_INT_PFLI_SIGNED_DUALITY_V0_1`  
**Date:** 4 August 2026  
**Base:** `46e42dedb83dd92c7154258e6ea58b1001ae6bd0`  
**Parent:** PR #51  
**Primary issue:** #52  
**State:** EXECUTING

## Single objective

Determine whether `INT-PFLI` contains exploitable signed factor-incidence structure beyond the prime-pair count itself. If it does not, replace it by the weakest tractable soft detector found, quantify the correlation order required to control that detector, and close every fixed-order moment or direct asymptotic-sieve lane at an exact obstruction.

No work on Paper VII, direct function-field `d=1`, random-order derandomisation, reciprocal frames, the superseded four-prime target, or finite-panel asymptotic promotion is permitted.

## Frozen quantities

For the registered primorial centres and prime candidate offsets, let

\[
Z_j=\#\{m\in\mathcal A_j:P_j+m\text{ is prime}\},
\qquad
C_j=\#\{m\in\mathcal A_j:P_j+m\text{ is composite}\}.
\]

The exact partition is

\[
|\mathcal A_j|=Z_j+C_j.
\]

The inherited `INT-PFLI` excess therefore satisfies

\[
(C_j-|\mathcal A_j|+\gamma_j)_+=(\gamma_j-Z_j)_+.
\]

The programme first formalizes this collapse. It then studies the adaptive occupancy detector

\[
\mathcal O_X(\tau_X)=\sum_{j<N}e^{-\tau_X Z_j},
\qquad
\tau_X=\frac{2\log N}{\gamma_{\min}},
\qquad
\gamma_{\min}=\min_j\gamma_j.
\]

A failed row contributes exactly `1`, so `O_X(tau_X)<1` excludes every failure. The inherited lower-tail theorem would force `O_X(tau_X)=o(1)`, but the occupancy condition allows positive rows far below `gamma_j` and is strictly softer.

## Governing question

Can the adaptive occupancy detector be proved by a signed Buchstab, asymptotic-sieve, bilinear, or factorial-moment argument without importing correlations of growing order?
