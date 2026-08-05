# Successor target — INT-SCME

`INT-SCME` is the sole primary integer frontier after the INT-SOCG execution and is tracked in issue #58.

For each deterministic terminal-prime stratum `B_b`, with common restricted candidate-prime universe

\[
\mathcal M_b=\{m:U_b<m\le H,\ m\text{ prime}\},
\]

prove that a fixed `kappa>0` satisfies

\[
\boxed{
\frac1{n_b}
\sum_{j\in B_b}
\sum_{m\in\mathcal M_b}
\log m\,\Lambda(P_j+m)
\ge \kappa X^2\log X.
}
\]

Proper output prime powers contribute only `O(X(log X)^2)` per row, so `INT-SCME` implies

\[
c_{1,b}\ge c_0X.
\]

This supplies the missing first-cumulant input to `INT-SOCG`.

Secondary higher-order targets `INT-LCSK` and the composite-modulus extension of `INT-PWOC` remain open, but neither is rationally prior to `INT-SCME`.
