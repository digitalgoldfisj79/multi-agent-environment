# Exact theorem ladder

## PWOC-SF0 — deterministic weighted energy criterion

Let `mathcal Q_X` be a finite modulus family and let `beta(q)>=0`. Suppose the exact energy decomposition has diagonal mass

\[
D_\beta=\sum_{q\in\mathcal Q_X}\beta(q)q
\]

and nonnegative off-diagonal collision kernel

\[
K_\beta(j,k)=
\sum_{\substack{q\in\mathcal Q_X\\q\mid P_j-P_k}}
\beta(q)q.
\]

If

\[
R_\beta=\max_j\sum_{k\ne j}K_\beta(j,k),
\]

then the Schur/AM-GM estimate gives

\[
\mathcal E_\beta(a)
\le
(D_\beta+R_\beta)
\sum_j|a_j|^2.
\tag{SF0}
\]

The deterministic assembly from a row collision budget to a total energy budget is the Lean target. The additive-character identity and the arithmetic estimate for `R_beta` remain analytic obligations.

## PWOC-SF1 — fixed-order squarefree extension

For a fixed integer `r>=1`, let

\[
\mathcal Q_{X,r}=
\{q\le Q_X:\mu^2(q)=1,\ \omega(q)=r,
\ p\mid q\Rightarrow p>2X\}.
\]

For one frozen weight family `beta_r(q)`, prove an explicit bound

\[
R_{\beta_r}
\le \mathfrak R_r(X,Q_X,n_b)
\tag{SF1}
\]

with a coefficient-uniform expression `mathfrak R_r`. A result is useful only if the resulting norm contributes below a displayed RUHL-FM or SOCG budget.

## PWOC-SF2 — finite squarefree source block

For a registered maximal support order `r_X` and actual source weights `beta_X(q)`, prove

\[
R_{\beta_X}
=o(D_{\beta_X})
\quad\text{or another explicitly sufficient transfer bound.}
\tag{SF2}
\]

This is the first target that may be labelled a genuine composite-modulus primorial-walk theorem for the frozen source block.

## Full INT-PWOC

The programme does not identify `SF2` with full `INT-PWOC`. Full `INT-PWOC` additionally requires all conductor ranges, coefficient families and products arising in the complete source or connected-correlation decomposition.

## Baseline divisor-subset bound

For `d=k-j`, the gap integer

\[
\Delta_{j,k}=\prod_{r=j+1}^{k}\ell_r-1
\]

has fewer than `d` prime divisors above `2X`. Therefore an order-`r` collision family contains fewer than

\[
\binom{d}{r}
\]

supported divisors before the conductor cutoff and coefficient weights are applied.

This combinatorial fact is a starting bound, not a success criterion. Its row sum may be too large at the registered stratum length.

## Required falsifier

For every admitted weight contract, construct a profile concentrated on squarefree divisors of a single `Delta_{j,k}`. If that admissible profile makes `R_beta` comparable to or larger than `D_beta`, then no absolute-value theorem for that contract can establish the desired square-root energy scale.
