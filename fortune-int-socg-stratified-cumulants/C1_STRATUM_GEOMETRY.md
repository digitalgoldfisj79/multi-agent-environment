# C1 — deterministic stratum geometry

Fix one `sigma>0` before inspecting output-prime incidence and partition terminal primes by intervals of width

\[
W_X=\left\lfloor X/(\log X)^{1+\sigma}\right\rfloor.
\]

Every stratum is determined by `X`, `sigma` and `ell_j` alone. Fix endpoint conventions, minimum row count, treatment of boundary strata, and a common candidate-offset universe.

For each retained stratum, preregister `L_b` and

\[
\tau_b=(1+3\varepsilon)\log(n_bB)/L_b.
\]

No `L_b` or `tau_b` may depend on observed `Z_j`.

## Deliverable — INT-SOCG-GEOM

A deterministic partition and comparison ledger proving:

- `0<tau_b<=tau_A`;
- successful stratum detectors sum to less than one;
- the inherited formal detector then excludes all failed rows.

## Kill gate

If every output-independent lower scale makes `tau_b>tau_A` or destroys `tau_bD_b=o(1)`, record the explicit incompatibility.