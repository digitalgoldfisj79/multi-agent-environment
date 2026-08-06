# Programme protocol

## Gate P0 — source and theorem freeze

Freeze:

- the RUHL-FM parent head;
- the proved prime-modulus C5 theorem;
- one terminal-prime stratum geometry;
- the exact modulus range `Q_X`;
- one nonnegative squarefree weight family `beta_X(q)` before collision data are inspected.

The weight family must arise from one named local-factor or source block, or be explicitly labelled a diagnostic surrogate.

**Kill rule:** no result for a hand-chosen weight family may be promoted as `INT-PWOC` unless a proved coefficient comparison transfers the actual source weights to it.

## Gate P1 — exact character and kernel identity

For arbitrary complex coefficients `a_j`, verify

\[
\mathcal E_\beta(a)
=
\sum_{j,k}a_j\overline{a_k}K_\beta(j,k),
\]

where

\[
K_\beta(j,k)=
\sum_{\substack{q\in\mathcal Q_X\\q\mid P_j-P_k}}
\beta(q)q.
\]

Separate the diagonal

\[
D_\beta=\sum_{q\in\mathcal Q_X}\beta(q)q
\]

from the off-diagonal collision kernel.

**Pass condition:** exact arithmetic regression against direct additive-character summation on finite panels.

## Gate P2 — Lean deterministic bridge

Formalise, without analytic axioms:

1. rowwise collision bounds imply the aggregate collision bound;
2. pointwise diagonal-plus-collision estimates imply the global weighted energy estimate.

The Lean module may take the analytic row budget and pointwise decomposition as assumptions, but every assumption must be visible in the theorem signature.

**Required validation:** targeted build, root import, full package build, and static trust scan.

## Gate P3 — squarefree collision combinatorics

For `j<k`, put

\[
\Delta_{j,k}=
\prod_{r=j+1}^{k}\ell_r-1.
\]

Every supported collision modulus divides `Delta_{j,k}`. Since `Delta_{j,k}<(2X)^{k-j}`, it has fewer than `k-j` distinct prime factors above `2X`.

Derive exact bounds for

\[
K_\beta(j,k)
=
\sum_{\substack{q\mid\Delta_{j,k}\\q\in\mathcal Q_X}}
\beta(q)q
\]

under each registered coefficient contract. Keep the divisor-subset growth explicit; do not replace it by `X^{o(1)}` unless the uniform range proves that claim.

## Gate P4 — source-compatible weight contracts

Test, in order:

- `W0`: unrestricted nonnegative squarefree weights, as a falsification baseline;
- `W1`: fixed-order support `omega(q)<=r` with multiplicative prime-factor majorants;
- `W2`: the frozen actual local/source coefficient family;
- `W3`: a proved majorant of `W2`, if available.

Ledger for each contract:

- support range;
- coefficient `l1` and `l2` masses;
- diagonal mass `D_beta`;
- maximal collision row sum `R_beta`;
- ratio `R_beta/D_beta`;
- exact transfer to the RUHL-FM or SOCG arithmetic budget.

## Gate P5 — fixed-order and multiplicative bounds

For `omega(q)=r`, compare the exact divisor sum with

\[
\binom{\omega_{>2X}(\Delta_{j,k})}{r}
\max_{q\mid\Delta_{j,k}}\beta(q)q.
\]

For multiplicative majorants `beta(q)q<=prod_{p|q}u_p`, compare with

\[
\prod_{\substack{p\mid\Delta_{j,k}\\p>2X}}(1+u_p)-1.
\]

Determine the strongest row-sum exponent available without source cancellation.

**Stop rule:** if every source-compatible absolute majorant has collision row sum at or above the diagonal scale, close the absolute-value lane explicitly rather than invoking cancellation heuristically.

## Gate P6 — signed and dyadic refinements

Only after P5, test whether the actual source coefficients provide:

- Möbius signs;
- dyadic cancellation across modulus factors;
- tensor or convolution structure;
- a bilinear factorisation that preserves the selected-centre row variable.

Any signed theorem must state its norm and its implication to the exact weighted energy. A numerical cancellation pattern is diagnostic only.

## Gate P7 — finite panels and adversarial tests

Run exact panels for several `X`, `Q_X`, support orders and weight profiles. Include adversarial profiles concentrated on actual divisors of one large gap `Delta_{j,k}`.

Reject any proposed inequality that fails under an admissible adversarial profile or whose constant grows faster than its stated asymptotic ledger.

## Gate P8 — arithmetic transfer

Quantify the contribution of the proved squarefree energy estimate to:

- the selected-centre prime-tuple residual `A_{b,k}` in RUHL-FM; and/or
- the composite-modulus connected coefficient in INT-SOCG.

**Pass condition:** a displayed inequality with no hidden source decomposition, Cauchy--Schwarz loss or conductor range.

## Gate P9 — closeout and clean room

Run static, exact-regression, targeted Lean and full-package validation. Inspect all external jobs before cancellation.

Allowed terminal outcomes:

- `SQUAREFREE_COMPOSITE_ENERGY_PROVED`;
- `FIXED_ORDER_COMPOSITE_EXTENSION_PROVED`;
- `REDUCED_TO_WEIGHTED_DIVISOR_ROW_SUM`;
- `ABSOLUTE_MAJORANT_BLOCKED_BY_SUBSET_GROWTH`;
- `SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE`;
- `NO_TRANSFER_TO_RUHL_OR_SOCG`;
- `REFUTED_OR_CORRECTED`.

No closeout may claim `INT-PWOC`, `INT-SOCG`, `RUHL-FM`, `INT-AOD` or Fortune unless the complete corresponding implication is committed and validated.
