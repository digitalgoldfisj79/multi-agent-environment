# M6 — parity-tail identity

**Status:** `EQUIVALENT_TO_INT_SCME_GIVEN_INT_SCVAR`

Define

\[
D_Q(n)=\sum_{2X<q\le Q,\ q\mid n}\log q,
\qquad R_Q(n)=\Lambda(n)-D_Q(n).
\]

For each microblock,

\[
T_C=\mathcal D_C(Q)+\mathcal R_C(Q)
\]

is an exact identity. Since `D_Q` vanishes on every prime output, `mathcal D_C` is entirely composite divisor-band mass.

If `INT-SCVAR` gives

\[
\mathcal D_C(Q)=(1/3-\varepsilon+o(1))H\log X,
\]

then the pointwise trivial inequality `R_Q(n)>=-D_Q(n)` yields

\[
\mathcal R_C(Q)\ge-(1/3-\varepsilon+o(1))H\log X.
\]

Improving this by `\kappa H\log X` is exactly equivalent to proving

\[
T_C\ge\kappa H\log X.
\]

Therefore the former `INT-SCPT` target is not a parity-breaking reduction or an independent theorem. It is `INT-SCME` rewritten after subtracting a conditionally evaluated composite band.
