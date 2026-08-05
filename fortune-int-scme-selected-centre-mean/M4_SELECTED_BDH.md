# M4 — selected-residue variance reduction

**Status:** `REDUCED_TO_INT_SCVAR; UNCONDITIONAL_LARGE_SIEVE_OBSTRUCTED`

Let `C` be a deterministic microblock with `R asymp X^rho` rows and put

\[
Q=X^{1+\delta},\qquad 0<\delta<1.
\]

For prime `q` with `2X<q<=Q`, every `P_j` is invertible modulo `q`. Define

\[
r_q(a)=\#\{j\in C:-P_j\equiv a\pmod q\},
\qquad
E_q(a)=\vartheta(H;q,a)-\frac{H}{q-1}.
\]

The exact primorial collision argument gives

\[
\sum_{2X<q\le Q}\sum_{a\bmod q}r_q(a)^2
\ll \frac{RQ}{\log Q}+R^3.
\]

## Candidate variance input — INT-SCVAR

Assume at this scale that

\[
\boxed{
V(H,Q):=
\sum_{2X<q\le Q}\sum_{(a,q)=1}|E_q(a)|^2
\ll H Q(\log H)^C.
}
\]

Cauchy–Schwarz then gives a selected-residue error, relative to `H log X`, with diagonal and collision exponents

\[
X^{\delta-\rho/2+o(1)}
\quad\text{and}\quad
X^{(\rho+\delta-1)/2+o(1)}.
\]

Thus `INT-SCVAR` yields the desired selected-band asymptotic exactly when

\[
2\delta<\rho<1-\delta.
\]

The optimized conditional frontier is `rho=2/3`, `delta<1/3`.

## Correction to the initial execution

The classical unconditional Barban–Davenport–Halberstam `HQ log H` estimate is available in its standard form when `Q` is near `H` (for example `Q>=H/(log H)^A`), not at the programme scale

\[
Q=X^{1+\delta}=H^{(1+\delta)/2}.
\]

At this smaller `Q`, the unconditional large-sieve bound is of order

\[
V(H,Q)\ll (H+Q^2)H(\log H)^C.
\]

Since `Q>H^(1/2)` in every post-terminal band, the `Q^2H` term dominates. Even discarding every collision, the resulting selected-residue error relative to `H log X` has exponent

\[
\frac12+\frac{3\delta}{2}-\frac\rho2.
\]

It would require `rho>1+3 delta`, impossible for a microblock contained in `O(X/log X)` rows.

Therefore the unconditional large-sieve/BDH route cannot enter any polynomial post-terminal band. The earlier unconditional M5 promotion is retracted. `INT-SCVAR` is a genuine additional theorem; GRH-level variance results provide a conditional benchmark in the range `Q>=H^(1/2+epsilon)`.