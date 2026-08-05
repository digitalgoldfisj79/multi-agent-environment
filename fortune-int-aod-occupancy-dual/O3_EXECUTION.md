# O3 — detector degree and coefficient-cost execution

**Status:** PASSED WITH REDUCTION

## Parameter freedom

For every `0<q<=q_A`, where `q_A=1-exp(-tau_A)`,

\[
\sum_j(1-q)^{Z_j}<1
\]

is a stronger sufficient condition than the issue-#54 detector because `1-q_A<=1-q` and `Z_j>=0`.

Let `L_X` be a deterministic preregistered scale and choose

\[
q_X=\frac{(1+3\varepsilon)\log N}{L_X},
\qquad 0<q_X\le q_A.
\]

If `L_X<=kappa_1=E[Z_J]`, the first connected term satisfies

\[
q_X\kappa_1\ge(1+3\varepsilon)\log N.
\]

Thus it suffices to bound the absolute connected remainder by `2 epsilon log N`.

## Degree ledger

At the registered scale,

\[
M_X\asymp X^2/\log X.
\]

- inherited constant-`q_A` detector: `K_A=q_A M_X=Theta(X^2/log X)`;
- adaptive small-`q` detector with `L_X asymp X`:
  \[
  K_X=q_XM_X=\Theta(X).
  \]

This remains a growing-order object, but removes a full factor `X/log X` from the exact-cover degree and places the connected expansion at `q_X=Theta(log X/X)`.

## Coefficient ruling

Raw Bonferroni truncation still requires growing order and is not opened as the primary lane. The factorial coefficients `q_X^k/k!` are instead paired with connected cumulants before absolute values are taken.

The programme therefore replaces constant-parameter `INT-CCB` by its stronger adaptive form:

> **INT-SQCCB — small-q connected-cumulant bound.** There are deterministic `L_X` and `q_X` as above such that:
> 1. `L_X<=kappa_1`;
> 2. the connected expansion is justified at `q_X`;
> 3. the aggregate higher connected contribution is at most `2 epsilon log N`.

Then `INT-SQCCB => INT-AOD => eventual Fortune`.

## Honesty boundary

The required lower bound `L_X<=kappa_1` is not assumed proved. It is an explicit part of the successor theorem. Selecting `L_X` after observing the occupancies is prohibited.
