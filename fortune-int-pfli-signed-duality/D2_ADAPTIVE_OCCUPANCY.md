# D2 — adaptive occupancy detector

Let

\[
\gamma_{\min}=\min_{j<N}\gamma_j,
\qquad
\tau_X=\frac{2\log N}{\gamma_{\min}},
\]

and define

\[
\mathcal O_X=
\sum_{j<N}e^{-\tau_XZ_j}.
\]

## Failure exclusion

Every summand is nonnegative. If row `j` fails, then `Z_j=0` and its summand is

\[
e^{-\tau_XZ_j}=1.
\]

Thus

\[
\boxed{\mathcal O_X<1\implies Z_j>0\text{ for every }j.}
\]

This implication is finite and exact; no asymptotic estimate is used.

## INT-PFLI implies vanishing occupancy

Write

\[
\Delta_X^2=
\sum_{j<N}(\gamma_j-Z_j)_+^2.
\]

If `INT-PFLI` holds, then

\[
\Delta_X=o(\gamma_{\min}).
\]

Pointwise,

\[
(\gamma_j-Z_j)_+\le\Delta_X,
\]

so

\[
Z_j\ge\gamma_j-\Delta_X
\ge(1-o(1))\gamma_{\min}.
\]

Consequently

\[
e^{-\tau_XZ_j}
\le
\exp(-(2-o(1))\log N)
=N^{-2+o(1)},
\]

and hence

\[
\mathcal O_X\le N^{-1+o(1)}=o(1).
\]

## Strict softening

The occupancy condition does not require every row to reach `gamma_j`. For example, with fixed `N>=2`, one row may have `Z=1<gamma_min` while all remaining rows have sufficiently large counts; the occupancy sum can still be below `1`. The squared lower-tail condition, by contrast, records the full deficit of that row.

The new target is therefore:

> **INT-AOD — adaptive occupancy detector.** For all sufficiently large registered blocks,
> \[
> \boxed{
> \sum_{j<N}
> \exp\!\left(-\frac{2\log N}{\gamma_{\min}}Z_j\right)<1.
> }
> \]

`INT-AOD` is sufficient for eventual Fortune and is strictly softer than `INT-PFLI`. It remains open.
