# Formalisation plan

## Existing trusted bridge

`FortuneFormal/Integer/AdaptiveOccupancyCriterion.lean` already proves the deterministic row-dependent detector implication. It remains the formal endpoint of this programme.

## No premature analytic formalisation

The build adds no new Lean theorem asserting a cumulant-generating expansion, a singular-series estimate, or a prime correlation. Those statements remain analytic obligations.

## Candidate module after C3/C6

Proposed path:

`fortune-formal/FortuneFormal/Integer/OrdinaryCumulantGrowthCriterion.lean`

Stage A may formalize only the deterministic geometric budget:

\[
|c_k|\le c_1 k!D^{k-1},\quad \tau D<1
\Longrightarrow
\sum_{k=2}^{K}\frac{\tau^k}{k!}|c_k|
\le \tau c_1\frac{\tau D}{1-\tau D}.
\]

Stage B is imported only if the analytic proof supplies a rigorously stated equality between the log-Laplace transform and the convergent ordinary-cumulant series.

## Required validation

- targeted build before import;
- no `sorry`, `admit`, unsafe declaration or new axiom;
- theorem names and assumptions mirrored in the claim matrix;
- full clean-room package build at C9.

The formal module must not hide the first-cumulant lower bound, convergence radius, or selected-centre arithmetic estimate.