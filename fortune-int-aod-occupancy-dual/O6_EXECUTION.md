# O6 — conditional Poisson and Hardy--Littlewood benchmark execution

**Status:** PASSED AS AN EXPLICIT CONDITIONAL REDUCTION

## Stratified factorial moments

For stratum `b`, put

\[
M_{b,k}=\frac1{n_b}\sum_{j\in B_b}(Z_j)_k.
\]

Let `lambda_j` be deterministic Hardy--Littlewood model means satisfying

\[
L_b\le\lambda_j\le U_b,
\qquad U_b/L_b\le1+o(1).
\]

Choose

\[
q_b=(1+3\varepsilon)\frac{\log(n_bB)}{L_b}
\le q_A
\]

and an even order

\[
K_b=\lceil\beta\log(n_bB)\rceil_{\rm even}.
\]

## RUHL-FM hypothesis

The exact row-uniform growing-tuple hypothesis required by the programme is:

\[
M_{b,k}
=
\frac1{n_b}\sum_{j\in B_b}\lambda_j^k+E_{b,k}
\qquad(0\le k\le K_b),
\]

with weighted aggregate error

\[
\sum_{k=0}^{K_b}
\frac{q_b^k}{k!}|E_{b,k}|
\le(n_bB)^{-1-2\varepsilon}.
\]

The tuple order is only

\[
K_b=\Theta(\log X),
\]

but the estimate must be uniform on the actual sparse primorial centres and its aggregate error must retain one-row resolution.

## Conditional implication

Bonferroni gives, because `K_b` is even,

\[
G_b(1-q_b)
\le
\sum_{k=0}^{K_b}
\frac{(-q_b)^k}{k!}M_{b,k}.
\]

For each model mean, Taylor's theorem gives

\[
0\le
\sum_{k=0}^{K_b}\frac{(-q_b\lambda_j)^k}{k!}
-e^{-q_b\lambda_j}
\le
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}.
\]

Choose the absolute constant `beta` so that

\[
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}
\le(n_bB)^{-1-2\varepsilon}.
\]

Since `q_b lambda_j >=(1+3 epsilon)log(n_bB)`, the Poisson term is at most `(n_bB)^(-1-3epsilon)`. Combining the model term, Taylor remainder, and RUHL error yields

\[
G_b(1-q_b)<\frac1{n_bB}
\]

for sufficiently large `X`. Summing over strata proves `INT-AOD`.

`verify_ruhl_budget.py` confirms that, for example, `beta=10`, `epsilon=0.10`, and `U_b/L_b<=1.10` satisfy the factorial-tail budget across the registered asymptotic scales.

## What existing results do and do not supply

Growing-set singular-series theorems can control averages of the local Hardy--Littlewood constants when `k=O(log X)` and the offset range is sufficiently large. Conditional Poisson-tail results show that strong Hardy--Littlewood uniformity can produce the expected Laplace and tail behaviour. They do not provide the displayed `RUHL-FM` estimates on the selected multiplicative primorial path.

## Ruling

\[
\boxed{\mathrm{RUHL\!-\!FM}(K=\Theta(\log X),\text{ weighted error }<(n_bB)^{-1-2\varepsilon})
\Longrightarrow \mathrm{INT\!-\!AOD}.}
\]

This is a complete conditional implication, not an unconditional theorem. The missing input is now quantified in tuple order, stratum width, and error scale.
