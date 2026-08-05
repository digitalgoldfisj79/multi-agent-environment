# O4 — connected-cumulant execution

**Status:** GLOBAL LANE OBSTRUCTED; REDUCED TO STRATIFIED CONNECTED BOUND

## Exact global obstruction

Even under an ideal rowwise Poisson model, a whole-block cumulant expansion need not reach the useful detector parameter.

Take two equally weighted row classes with Poisson means `lambda_-` and `lambda_+`. Their factorial probability generating function is

\[
G(1-q)=\frac12e^{-q\lambda_-}+\frac12e^{-q\lambda_+}.
\]

Its nearest complex zero is at

\[
q=\frac{i\pi}{\lambda_+-\lambda_-},
\]

so the Taylor series of `log G(1-q)` about zero has radius

\[
\rho=\frac{\pi}{|\lambda_+-\lambda_-|}.
\]

Across a full dyadic primorial block, the natural row means vary on scale `Theta(X)`. Hence `rho=Theta(1/X)`, while a useful small detector has

\[
q\asymp\log N/X.
\]

Thus `q/rho=Theta(log X)`: the global connected series lies outside its convergence disk even in the Poisson benchmark. This closes unstratified `INT-CCB` as the main route.

## Stratified detector

Partition the registered rows into deterministic contiguous blocks `B_b`, with sizes `n_b`, and choose preregistered parameters

\[
0<q_b\le q_A.
\]

Put

\[
G_b(1-q_b)=\frac1{n_b}\sum_{j\in B_b}(1-q_b)^{Z_j}.
\]

If there are `B` strata and

\[
-\log G_b(1-q_b)>\log(n_bB)
\]

for every `b`, then

\[
\sum_b n_bG_b(1-q_b)<\sum_b\frac1B=1.
\]

Since `q_b<=q_A`, this implies the issue-#54 uniform detector and excludes every failed row.

## Successor theorem — INT-SCCB

For each stratum, let `kappa_{k,b}` be the factorial cumulants of the row occupancy distribution in that stratum.

> **INT-SCCB — stratified connected-cumulant bound.** There is a deterministic partition with `B=polylog(X)` and preregistered `q_b<=q_A` such that:
> 1. the connected expansion of `log G_b(1-q_b)` is justified for every stratum;
> 2. for every `b`,
>    \[
>    q_b\kappa_{1,b}-
>    \sum_{k\ge2}\frac{q_b^k}{k!}|\kappa_{k,b}|
>    >\log(n_bB).
>    \]

Then `INT-SCCB => INT-AOD => eventual Fortune`.

## Required stratum width

In the two-mean surrogate, convergence at `q_b` requires

\[
q_b\,\Delta\lambda_b<\pi.
\]

With `q_b asymp log X/X`, this requires

\[
\Delta\lambda_b=O(X/\log X)
\]

with a strict constant margin. Because the expected row mean changes at order one per unit change of the terminal prime, a safe programme scale is terminal-prime width

\[
X/(\log X)^{1+\delta},
\]

using `B=O((log X)^{1+delta})` strata. The union cost is only `log B=O(log log X)`.

## Verification

- `verify_poisson_mixture_obstruction.py` checks the exact complex zeros and scale separation;
- `verify_stratified_criterion.py` checks the finite implication and failed-row sentinel.

`INT-SCCB` is not proved.
