# Final status — INT-LCSK tree graph

**Programme:** `FORTUNE_INT_LCSK_TREE_GRAPH_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-lcsk-tree-graph-v01-20260806`  
**State:** `EXECUTED_AND_VALIDATED`

## Terminal outcomes

- `PAIR_TREE_MAJORANT_REFUTED`
- `ABSOLUTE_HYPEREDGE_RADIUS_INSUFFICIENT`
- `REDUCED_TO_SIGNED_HIGHER_BODY_CLUSTER_THEOREM`

## Decisive result

The inherited pair-scale estimate cannot be lifted to all connected orders by an absolute spanning-tree inequality. A same-residue triple at one post-terminal prime has connected coefficient of order `1/p`, while every pair-tree term is order `1/p^2`.

The ratio against a tree majorant with fixed edge constant `C` is exactly

\[
(p-2)/(3C^2),
\]

which is unbounded.

## All-orders consequence

Replacing trees by absolute same-prime hyperedges does not restore the frozen `INT-LCSK` radius. The Brun--Titchmarsh absolute ledger permits only

\[
D_r\asymp X/(\log X)^{1+1/(r-1)}.
\]

The extra exponent tends to zero at logarithmic order, whereas `INT-LCSK` requires one fixed positive `delta`.

## Surviving frontier

The next local theorem must preserve signed higher-body collision clusters and primewise Euler-product recombination before absolute values. It cannot be a pair-only dependency graph theorem.

## Validation

Workflow run `31081057533` at head `692278db18b389490104ebc8ddd2889efed17316` passed:

- static claim audit and exact execution regressions;
- targeted build of `LocalConnectedTreeObstruction`;
- full `FortuneFormal` package build;
- scan for `sorry`, `admit`, `axiom` and `unsafe`;
- Lean `4.32.0`.

## Explicit nonclaims

No proof or disproof of `INT-LCSK` is claimed.  
No proof of `INT-SOCG`, `INT-AOD` or Fortune is claimed.
