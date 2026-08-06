# O4 — cumulant-generating-function execution

**Status:** GLOBAL LANE OBSTRUCTED; REDUCED TO A STRATIFIED ORDINARY-CUMULANT BOUND

## Correct connected object

For a uniform row `J` in a deterministic stratum, write

\[
K_b(t)=\log\mathbb E_b e^{tZ_J}
=\sum_{k\ge1}c_{k,b}\frac{t^k}{k!},
\]

where `c_{k,b}` are the **ordinary cumulants** of the row occupancy. The detector uses `t=-tau_b` directly:

\[
G_b(\tau_b)=\mathbb E_b e^{-\tau_bZ_J}.
\]

Factorial cumulants are useful for Bonferroni and Hardy--Littlewood moment formulas, but they do not have the simple common-row joint-column decomposition required at O5. Ordinary cumulants do.

## Exact global obstruction

Even under an ideal rowwise Poisson model, a whole-block cumulant expansion need not reach a useful detector temperature.

Take two equally weighted row classes with Poisson means `lambda_-` and `lambda_+`. Their Laplace transform is

\[
G(\tau)=\frac12e^{-\tau\lambda_-}+\frac12e^{-\tau\lambda_+}.
\]

Its nearest complex zero is at

\[
\tau=\frac{i\pi}{\lambda_+-\lambda_-},
\]

so the Taylor series of `log G(tau)` about zero has radius

\[
\rho=\frac{\pi}{|\lambda_+-\lambda_-|}.
\]

Across a full dyadic primorial block, the natural row means vary on scale `Theta(X)`. Hence `rho=Theta(1/X)`, while a useful adaptive detector has

\[
\tau\asymp\log N/X.
\]

Thus `tau/rho=Theta(log X)`: the global cumulant-generating series can lie outside its convergence disk even when every row is individually Poisson. This closes an unstratified cumulant proof as the main route.

## Stratified detector

Partition the registered rows into deterministic contiguous blocks `B_b`, with sizes `n_b`, and choose preregistered temperatures

\[
0<\tau_b\le\tau_A.
\]

Put

\[
G_b(\tau_b)=\frac1{n_b}\sum_{j\in B_b}e^{-\tau_bZ_j}.
\]

If there are `B` strata and

\[
-\log G_b(\tau_b)>\log(n_bB)
\]

for every `b`, then

\[
\sum_b n_bG_b(\tau_b)<1.
\]

The kernel-checked row-dependent-temperature theorem then implies the frozen issue-#54 detector and excludes every failed row.

## Successor criterion — INT-SOCB

> **INT-SOCB — stratified ordinary-cumulant bound.** There is a deterministic partition with `B=polylog(X)` and preregistered `tau_b<=tau_A` such that:
> 1. the ordinary cumulant expansion of `K_b(-tau_b)` is justified for every stratum;
> 2. for every `b`,
>    \[
>    \tau_b c_{1,b}-
>    \sum_{k\ge2}\frac{\tau_b^k}{k!}|c_{k,b}|
>    >\log(n_bB).
>    \]

Then `INT-SOCB => INT-AOD => eventual Fortune`.

## Required stratum width

In the two-mean surrogate, convergence at `tau_b` requires

\[
\tau_b\Delta\lambda_b<\pi.
\]

With `tau_b asymp log X/X`, this requires

\[
\Delta\lambda_b=O(X/\log X)
\]

with strict constant margin. A safe programme scale is terminal-prime width

\[
X/(\log X)^{1+\delta},
\]

using only `B=O((log X)^{1+delta})` strata. The union cost is `O(log log X)`.

## Verification

- `verify_poisson_mixture_obstruction.py` checks the exact complex zeros and scale separation;
- `verify_stratified_criterion.py` checks the finite detector implication and failed-row sentinel;
- `AdaptiveOccupancyCriterion.lean` kernel-checks the row-dependent-to-uniform implication.

`INT-SOCB` is not proved.
