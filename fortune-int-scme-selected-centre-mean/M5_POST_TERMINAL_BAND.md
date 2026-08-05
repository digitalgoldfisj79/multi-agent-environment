# M5 — first post-terminal divisor-band theorem

**Status:** `PROVED_USING_CLASSICAL_BDH`

For a deterministic microblock `C`, define

\[
\mathcal D_C(Q)=
\frac1{|C|}
\sum_{j\in C}
\sum_{m\in M_b}\log m
\sum_{\substack{2X<q\le Q\\q\text{ prime}\\q\mid P_j+m}}
\log q.
\]

The main term in M4 is

\[
(\vartheta(H)-\vartheta(U_b))
\sum_{2X<q\le Q}\frac{\log q}{q-1}.
\]

By the prime number theorem and Mertens partial summation,

\[
\vartheta(H)-\vartheta(U_b)=(1+o(1))H
\]

and, for `Q=X^(1+delta)`,

\[
\sum_{2X<q\le Q}\frac{\log q}{q-1}
=(\delta+o(1))\log X.
\]

Combining these estimates with M4 proves

\[
\boxed{
\mathcal D_C(X^{1+\delta})
=(\delta+o(1))H\log X
}
\]

uniformly for every deterministic microblock whenever

\[
2\delta<\rho<1-\delta.
\]

The largest admissible `delta` for this BDH-plus-collision mechanism is `1/3`. Indeed, existence of `rho` requires `2 delta < 1-delta`. The symmetric optimum is

\[
\rho=2/3,
\qquad
Q=X^{4/3-\varepsilon}
\]

for any fixed `epsilon>0`, giving

\[
\mathcal D_C(Q)=
(1/3-\varepsilon+o(1))H\log X.
\]

## Interpretation boundary

`mathcal D_C(Q)` is weighted prime-divisor incidence, not prime-output mass. Composite outputs contribute positively to this band. The theorem is a genuine unconditional post-terminal distribution result, but it does not prove `INT-SCME`.