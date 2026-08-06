# INT-PSLT Buchstab–factor-band programme

**Programme:** `FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1`  
**Date:** 4 August 2026  
**Base:** `cc8c00c30a436b8ced65bbd4703326145d129de3`  
**Parent:** PR #49  
**Primary issue:** #50  
**State:** CLOSED  
**Outcome:** `REDUCED_TO_CRITICAL_FACTOR_INCIDENCE`

## Result

Starting from `INT-PSLT`, the programme proved an explicit failed-centre prime-power cap of order `X log X`, ruled out natural defect propagation, derived the exact least-factor partition, and proved that the first admissible factor already lies beyond the classical lower-sieve `s=2` boundary.

The exact successor is `INT-PFLI`, the signed selected-centre post-level factor-incidence theorem recorded in `B5_CRITICAL_FACTOR_INCIDENCE.md`.

No work on Paper VII, direct function-field `d=1`, random-order derandomisation, reciprocal frames, or the superseded four-prime target entered the programme.

## Frozen source

For increasing primorial centres

\[
P_j=A_XQ_j,\qquad H=\eta X^2,\qquad 0<\eta<1,
\]

define

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

At a failed centre this source is supported only on proper prime powers. The compressed deterministic threshold is

\[
B_j=2\log(P_j+H)
\sum_{k=2}^{\lfloor\log_2(P_j+H)\rfloor}\frac1k
\asymp X\log X.
\]

## Governing obstruction

If `[P_j+2,P_j+H]` contains no prime, every admissible offset is covered by a composite output whose least prime factor satisfies

\[
r>\ell_j>\sqrt H.
\]

Even an idealized sieve level `D=H` gives

\[
\log D/\log r<2,
\]

so a classical positive lower sieve cannot enter any post-primorial factor band. The remaining input must preserve signed cancellation across the full post-level factor incidence.

`INT-PFLI`, `INT-PSLT`, and Fortune remain open.
