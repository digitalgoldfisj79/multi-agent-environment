# M6 — selected-centre variance and parity-tail reduction

**Status:** `CONDITIONAL_REDUCTION_TO_INT_SCVAR_PLUS_INT_SCPT`

Fix `epsilon>0`, put

\[
Q=X^{4/3-\varepsilon}
\]

and define

\[
D_Q(n)=
\sum_{\substack{2X<q\le Q\\q\text{ prime}\\q\mid n}}
\log q,
\qquad
R_Q(n)=\Lambda(n)-D_Q(n).
\]

The identity

\[
\Lambda(n)=D_Q(n)+R_Q(n)
\]

is exact. For a deterministic microblock `C`, let `mathcal D_C(Q)` and `mathcal R_C(Q)` be the corresponding weighted averages. Then

\[
T_C=\mathcal D_C(Q)+\mathcal R_C(Q).
\]

## Analytic inputs

`INT-SCVAR` is the post-terminal variance estimate from M4. It implies

\[
\mathcal D_C(Q)=
(1/3-\varepsilon+o(1))H\log X.
\]

`INT-SCPT` is the signed tail bound

\[
\boxed{
\mathcal R_C(Q)
\ge
-(1/3-\varepsilon-\kappa)H\log X
}
\]

for some fixed `kappa>0`.

Together they imply

\[
T_C\ge(\kappa+o(1))H\log X,
\]

hence `INT-SCME` after deterministic microblock aggregation.

## Terminal interpretation

The programme has not reduced `INT-SCME` to one established or one open theorem. It has separated two independent missing inputs:

1. post-terminal selected-residue variance at `Q=H^(2/3-o(1))`;
2. signed prime-versus-composite parity cancellation after that band is extracted.

A GRH-strength variance theorem can supply the first input conditionally, leaving `INT-SCPT`; unconditionally, both inputs remain open. Therefore the honest programme outcome is an explicit two-wall method obstruction, not an unconditional `INT-SCPT` reduction.