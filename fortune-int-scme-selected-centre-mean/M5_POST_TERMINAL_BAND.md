# M5 — first post-terminal divisor-band theorem

**Status:** `CONDITIONAL_ON_INT_SCVAR; UNCONDITIONAL_ROUTE_OBSTRUCTED`

For a deterministic microblock `C`, define

\[
\mathcal D_C(Q)=
\frac1{|C|}
\sum_{j\in C}
\sum_{m\in M_b}\log m
\sum_{\substack{2X<q\le Q\\q\text{ prime}\\q\mid P_j+m}}
\log q.
\]

The expected main term is

\[
(\vartheta(H)-\vartheta(U_b))
\sum_{2X<q\le Q}\frac{\log q}{q-1}.
\]

By the prime number theorem and Mertens partial summation, for `Q=X^(1+delta)`, this is

\[
(\delta+o(1))H\log X.
\]

Under `INT-SCVAR` from M4, Cauchy–Schwarz and the exact collision multiplicity prove

\[
\boxed{
\mathcal D_C(X^{1+\delta})
=(\delta+o(1))H\log X
}
\]

uniformly whenever `2 delta < rho < 1-delta`. The optimized conditional choice is

\[
\rho=2/3,
\qquad
Q=X^{4/3-\varepsilon},
\]

giving coefficient `1/3-epsilon`.

A GRH-strength variance theorem in the range `Q>=H^(1/2+epsilon)` supplies a conditional literature benchmark for `INT-SCVAR`. The programme does not promote that conditional bridge to an unconditional integer result.

## Unconditional ruling

The standard large-sieve variance bound is too large for every `delta>0`, even under a fictitious collision-free selected residue set. Therefore no unconditional post-terminal divisor-band asymptotic is proved by this programme.

## Interpretation boundary

Even conditionally, `mathcal D_C(Q)` is weighted prime-divisor incidence, not prime-output mass. Composite outputs contribute positively to this band.