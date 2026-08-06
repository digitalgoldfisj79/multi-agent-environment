# O3 — detector degree and coefficient-cost execution

**Status:** PASSED WITH REDUCTION

## Parameter freedom

For every `0<tau<=tau_A`,

\[
\sum_j e^{-\tau Z_j}<1
\]

is a stronger sufficient condition than the issue-#54 detector, because the frozen terms at `tau_A` are no larger.

Let `L_X` be a deterministic preregistered scale and choose

\[
\tau_X=\frac{(1+3\varepsilon)\log N}{L_X},
\qquad 0<\tau_X\le\tau_A.
\]

If `L_X<=c_1=E[Z_J]`, the first ordinary-cumulant term satisfies

\[
\tau_Xc_1\ge(1+3\varepsilon)\log N.
\]

The associated Bernoulli cover density is

\[
q_X=1-e^{-\tau_X}=\Theta(\log X/X)
\]

when `L_X asymp X`.

## Degree ledger

At the registered scale,

\[
M_X\asymp X^2/\log X.
\]

- inherited constant-density detector: `K_A=q_A M_X=Theta(X^2/log X)`;
- adaptive detector:
  \[
  K_X=q_XM_X=\Theta(X).
  \]

This removes a full factor `X/log X` from the natural exact-cover degree.

## Coefficient ruling

Raw Bonferroni truncation remains a growing-order object and is retained only in the conditional O6 benchmark. The primary route uses the ordinary cumulant generating function

\[
\log E[e^{-\tau_XZ}]
=\sum_{k\ge1}c_k\frac{(-\tau_X)^k}{k!}.
\]

The later O4–O5 gates show that this must be applied after deterministic stratification and reduce it to `INT-SOCG`.

## Honesty boundary

The required lower bound `L_X<=c_1` is not assumed proved. It is an explicit part of the successor theorem. Selecting `L_X` after observing occupancies is prohibited.
