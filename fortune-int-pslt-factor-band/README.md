# INT-PSLT Buchstab–factor-band programme

**Programme:** `FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1`  
**Date:** 4 August 2026  
**Base:** `cc8c00c30a436b8ced65bbd4703326145d129de3`  
**Parent:** PR #49  
**Primary issue:** #50  
**State:** EXECUTING

## Single objective

Starting from the reduced shifted-prime lower-tail theorem `INT-PSLT`, determine whether a primorial-specific Buchstab or lower-bound-sieve decomposition can resolve one failed centre. The programme must either prove the theorem, reduce it to one exact post-level factor-incidence theorem, or close the factor-band method at an explicit scale obstruction.

No work on Paper VII, direct function-field `d=1`, random-order derandomisation, reciprocal frames, or the superseded four-prime target is permitted.

## Frozen source

For increasing primorial centres

\[
P_j=A_XQ_j,\qquad H=\eta X^2,\qquad 0<\eta<1,
\]

define

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

At a failed centre this source is supported only on proper prime powers. The first gate replaces the deliberately loose threshold `X(log X)^2` by an explicit deterministic prime-power cap of order `X log X`.

## Governing question

If `[P_j+2,P_j+H]` contains no prime, every admissible offset `m` is covered by a composite output whose least prime factor exceeds `ell_j`. Since `ell_j > sqrt(H)`, the factor decomposition begins at the exact lower-bound-sieve parity boundary.

The programme asks whether any signed Buchstab, divisor-switching, or selected-centre incidence mechanism crosses that boundary.
