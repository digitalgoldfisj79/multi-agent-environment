# M6 — selected-centre parity-tail reduction

**Status:** `REDUCED_TO_INT_SCPT`

Fix `epsilon>0`, put

\[
Q=X^{4/3-\varepsilon}
\]

and define for each output integer

\[
D_Q(n)=
\sum_{\substack{2X<q\le Q\\q\text{ prime}\\q\mid n}}
\log q,
\qquad
R_Q(n)=\Lambda(n)-D_Q(n).
\]

This is an exact identity:

\[
\Lambda(n)=D_Q(n)+R_Q(n).
\]

For a deterministic microblock `C`, let

\[
\mathcal R_C(Q)=
\frac1{|C|}\sum_{j\in C}\sum_{m\in M_b}
\log m\,R_Q(P_j+m).
\]

M5 gives

\[
\mathcal D_C(Q)=
(1/3-\varepsilon+o(1))H\log X.
\]

Therefore

\[
T_C=\mathcal D_C(Q)+\mathcal R_C(Q).
\]

## Successor theorem — INT-SCPT

Prove that there are fixed `epsilon,kappa>0` such that every sufficiently large deterministic `X^(2/3)`-row microblock satisfies

\[
\boxed{
\mathcal R_C(X^{4/3-\varepsilon})
\ge
-(1/3-\varepsilon-\kappa)H\log X.
}
\]

Then

\[
T_C\ge (\kappa+o(1))H\log X,
\]

and deterministic aggregation over microblocks proves `INT-SCME` for every parent stratum.

## Meaning of the tail

- prime outputs contribute positively through `Lambda(n)` and have `D_Q(n)=0`;
- composite outputs carrying a band prime contribute negatively through `-D_Q(n)`;
- proper prime powers are already negligible at the target scale;
- composite outputs whose prime factors all exceed `Q` enter with zero in this particular tail.

Thus `INT-SCPT` is a precise parity-breaking statement. It is strictly downstream of an established positive divisor-band main term, but it remains open.