# Phase Z4 fixed-dimensional motives and sieve status

**Date:** 2026-07-23  
**Job:** `6a619f07d09dc1f57c6c3ce6`  
**Status:** exact large-prime moment sweep complete; simple elliptic decomposition rejected; uniform trace theorem and all-degree sieve remain open.

## Exact sweep

The optimized exact cubic ledger evaluated both square classes for every prime

`503 <= p <= 1999`.

This gives `416` exact cases. The optimization replaces an unnecessary `O(p^3)` rational-root loop by the equivalent `O(p^2)` incidence construction; all quadratic and cubic factor computations and internal mass checks are unchanged.

The largest observed cubic multiplicity remains

`max Q_3 = 8`.

## Centered envelopes

Across this range:

- `|M_13-(p^2-1)/3|/p <= 1.89293`;
- `|M_23-(p^2-1)/6|/p <= 1.67280`;
- `|M_33-(p^2-1)/18|/p <= 1.03094`.

Thus the finite data continue to support the desired `O(p)` primitive-trace scale with moderate constants. This is finite evidence, not a Weil or Betti-number theorem.

## Motive fingerprinting

The three residuals were compared against the Frobenius traces of every nonsingular curve

`y^2=x^3+A*x+B`, `-5<=A,B<=5`,

and the corresponding square-class twists: `240` features in total.

The strongest single-feature absolute correlations were only:

- `0.2023` for the linear-cubic residual;
- `0.1578` for the quadratic-cubic residual;
- `0.1429` for the cubic-pair residual.

Eight-feature least-squares fits trained below `p=1200` failed badly on the held-out primes. No exact or stable low-height elliptic decomposition was found.

## Consequence

Route 4 remains the numerically strongest route because the residual scale is still `O(p)`, but the primitive surfaces are not explained by a small direct sum of obvious elliptic curves. The next useful work is geometric:

1. compactify and desingularize `X_13,a`, `X_23,a` and the off-diagonal cubic-pair surface;
2. calculate boundary and algebraic components exactly;
3. bound the remaining Betti numbers or identify higher-dimensional abelian/K3 factors;
4. use those bounds in the signed cycle-index sieve.

Further prime-range extension without a geometric model has low marginal value. The all-degree sieve and the d=1 crown remain open.
