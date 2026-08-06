# Programme protocol

## L0 — source and scale freeze

Freeze the inherited candidate universe

\[
\mathcal M_b=\{m:U_b<m\le H,\ m\text{ prime}\},
\]

the post-terminal prime range `p>2X`, the exact local factor

\[
G_p(S)=\frac{1-\nu_p(S)/p}{(1-1/p)^{|S|}},
\]

and the pair edge scale from C4 before inspecting higher-order output.

## L1 — exact connected recombination

For each residue pattern and order `r`, compute

\[
\kappa_{r,p}
=\sum_{\pi\in\Pi_r}(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{B\in\pi}G_p(B).
\]

Verify the set-partition formula exactly for all order-three residue patterns and finite panels through order eight.

## L2 — pair-edge identification

For two equal residues verify

\[
\kappa_{2,p}=\frac1{p-1}.
\]

Keep the inherited generic `O(1/p^2)` tail separate.

## L3 — spanning-tree gate

Test whether one fixed constant `C` can give

\[
|\kappa_{r,p}|\le
\sum_{T\in\mathcal T_r}\prod_{\{a,b\}\in E(T)}
\frac{C\,1_{m_a\equiv m_b\,(p)}}{p-1}
\]

for every post-terminal prime, residue pattern and `r<=Theta(log X)`.

**Kill rule:** one exact residue pattern whose ratio to the tree budget is unbounded closes the pair-tree lane.

## L4 — actual candidate witness

If L3 fails abstractly, require one finite witness satisfying the frozen candidate-universe restrictions `m_i>U_b`, `m_i<=H`, all `m_i` prime and `p>2X`.

## L5 — absolute hyperedge ledger

For the irreducible same-prime `r`-body cluster, combine the exact local coefficient with the inherited Brun--Titchmarsh row count. Keep the order dependence and logarithmic exponent explicit.

**Pass condition:** a fixed `delta>0` such that the absolute row mass is bounded by

\[
r!\left(X/(\log X)^{1+\delta}\right)^{r-1}
\]

uniformly through `r=Theta(log X)`.

## L6 — signed refinement gate

Open only if L5 fails. Identify whether partition signs, signs across different primes, or Euler-product logarithms furnish an exact cancellation identity. Numerical cancellation alone is not a theorem.

## L7 — Fortune interface

A successful result must enter the frozen factorial-cumulant estimate

\[
|f_{r,b}|\le c_{1,b}r!D_{F,b}^{r-1}
\]

with `D_{F,b}<<X/(log X)^(1+delta)` for one fixed `delta>0` and all registered orders.

## L8 — formal and clean-room validation

Kernel-check the exact order-three algebra, the fixed-constant tree obstruction and the logarithmic exponent gap. Run exact regressions, targeted Lean, full-package Lean and a trust scan.

## Allowed terminal outcomes

- `INT_LCSK_PROVED`
- `PAIR_TREE_MAJORANT_REFUTED`
- `ABSOLUTE_HYPEREDGE_RADIUS_INSUFFICIENT`
- `REDUCED_TO_SIGNED_HIGHER_BODY_CLUSTER_THEOREM`
- `REFUTED_OR_CORRECTED`

No terminal outcome may be promoted to `INT-LCSK`, `INT-SOCG`, `INT-AOD` or Fortune without the complete implication.
