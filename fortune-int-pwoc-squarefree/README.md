# Fortune INT-PWOC-SF

**Programme:** `FORTUNE_INT_PWOC_SQUAREFREE_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-pwoc-sf-v01-20260806`  
**Base:** `2c7c9e11d0af091d69886fd888a90876ba2e1161`  
**Status:** built; execution not yet started

## Purpose

Extend the proved prime-modulus primorial-walk energy estimate to one precisely frozen family of weighted squarefree-composite moduli.

The programme is deliberately narrower than the full output-prime source problem. It asks whether a nontrivial squarefree modulus block can be controlled strongly enough to feed either:

- the selected-centre prime-tuple residual in `fortune-int-ruhl-fm-consolidation/ARITHMETIC_INTERFACE.md`; or
- the composite-modulus input `INT-PWOC` in the `INT-SOCG` lane.

## Trust boundary

Lean formalises only deterministic finite implications:

1. rowwise collision budgets imply aggregate collision budgets;
2. pointwise diagonal-plus-collision energy estimates imply the global weighted energy estimate.

Lean does not assume or assert additive-character orthogonality, a squarefree divisor estimate, a source decomposition, a large-sieve theorem, or a prime-correlation theorem. Those remain explicit analytic obligations.

## Frozen notation

For one terminal-prime stratum, let `P_j` be consecutive primorial centres and let `a_j` be arbitrary coefficients. For a nonnegative modulus weight `beta(q)`, define

\[
\mathcal E_\beta(a)=
\sum_{q\in\mathcal Q_X}\beta(q)
\sum_{c\bmod q}
\left|\sum_j a_j e(cP_j/q)\right|^2.
\]

The squarefree support contract is

\[
q\le Q_X,\qquad \mu^2(q)=1,
\qquad p\mid q\Longrightarrow p>2X.
\]

The exact collision kernel is

\[
K_\beta(j,k)=
\sum_{\substack{q\in\mathcal Q_X\\q\mid P_j-P_k}}
\beta(q)q.
\]

The programme seeks an explicit source-compatible bound on

\[
\max_j\sum_{k\ne j}K_\beta(j,k).
\]

## Required outputs

- a frozen coefficient contract for one squarefree source block;
- an exact orthogonality and kernel ledger;
- upper and lower obstruction bounds for the collision row sum;
- finite exact regressions and adversarial weight profiles;
- a Lean-checked deterministic implication module;
- one honest closeout target if the source-compatible norm remains open.
