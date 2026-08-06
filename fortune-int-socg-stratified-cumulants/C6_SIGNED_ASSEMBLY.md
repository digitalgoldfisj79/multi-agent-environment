# C6 — signed ordinary-cumulant assembly

C6 combines:

- C2 first-cumulant mass;
- C3 exact equality-pattern decomposition;
- C4 local connected kernel;
- C5 selected primorial-walk cancellation.

Disconnected terms must cancel through partition Möbius inversion before absolute values.

## Target

For every retained stratum and all `k>=2`, prove

\[
|c_{k,b}|\le c_{1,b}k!D_b^{k-1},
\qquad
D_b\ll X/(\log X)^{1+\delta}.
\]

The exact geometric budget is

\[
\sum_{k\ge2}\frac{\tau_b^k}{k!}|c_{k,b}|
\le
\tau_bc_{1,b}\frac{\tau_bD_b}{1-\tau_bD_b}.
\]

## Pass condition

Prove `INT-SOCG` or isolate one strictly smaller signed connected-correlation theorem with a checked implication.

## Kill gate

If the recombined radius is `\gg X/log X`, record the precise equality pattern, local factor or orbit mode causing it.