# Formalisation plan

## New module

Proposed path:

`fortune-formal/FortuneFormal/Integer/WeightedOccupancyCriterion.lean`

The module is not imported until its targeted build passes.

## Definitions

For finite row type `ι`, finite offset type `κ`, an incidence predicate `hit : ι -> κ -> Prop`, and weights `a : κ -> R`, define

\[
\operatorname{weightedOccupancy}(i)
=\prod_{m\in\kappa}
\begin{cases}
\exp(-a_m),&\text{if }hit(i,m),\\
1,&\text{otherwise}.
\end{cases}
\]

A multiplicative version using factors `r_m in [0,1]` may be formalized first to avoid unnecessary analytic dependencies:

\[
D_i=\prod_m (\text{if }hit(i,m)\text{ then }r_m\text{ else }1).
\]

The exponential specialization sets `r_m=exp(-a_m)`.

## Theorems

1. `weightedOccupancy_nonneg` under `0<=r_m`.
2. `weightedOccupancy_of_failure`: if a row has no hits, its detector equals one.
3. `no_failure_of_weightedOccupancy_sum_lt_one`.
4. `uniformWeightedOccupancy_eq_pow`: if every `r_m=r`, the detector is `r^(hitCount i)`.
5. `uniformWeightedOccupancy_specializes_expDefect` for `r=exp(-tau)`.
6. Optional hypergeometric criterion on finite sets, separated from the independent-product detector.

## Trust boundary

The Lean theorem proves only the deterministic implication. It does not prove that a profile is admissible under the O1 protocol, that the detector sum is below one, or that any prime pair exists.

## Validation

- targeted module build first;
- no `sorry`, `admit`, new axiom, or unsafe declaration;
- import into `FortuneFormal.lean` only after targeted success;
- full clean-room package build at O9.