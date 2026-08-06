# O4 — cumulant-generating-function compression

Let `J` be uniform on a deterministic row stratum and define

\[
G_b(\tau)=\mathbb E_b[e^{-\tau Z_J}].
\]

The correct coefficients for the exponential detector are the ordinary cumulants `c_{k,b}`:

\[
\log G_b(\tau)=\sum_{k\ge1}c_{k,b}\frac{(-\tau)^k}{k!}.
\]

Factorial moments remain useful for Bonferroni expansions, but factorial cumulants do not have the simple common-row joint-column decomposition required at O5.

## Convergence requirement

A formal power series is insufficient. The programme must establish a zero-free disk, absolute coefficient bound, direct finite identity with remainder, or real-variable representation at the selected temperature.

## Executed reduction

Whole-block expansion is obstructed by macroscopic mixing of row means. The execution therefore uses deterministic terminal-prime strata and defines:

> **INT-SOCB — stratified ordinary-cumulant bound.** For preregistered `tau_b<=tau_A`, the ordinary cumulant expansion converges and
> \[
> \tau_bc_{1,b}-\sum_{k\ge2}\frac{\tau_b^k}{k!}|c_{k,b}|>\log(n_bB)
> \]
> in every stratum.

Then the total row-dependent detector is below one and the kernel-checked monotonicity theorem implies frozen `INT-AOD`.

The quantitative primary successor `INT-SOCG` is recorded in `O5_EXECUTION.md`.
