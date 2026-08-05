# Formalisation record

## Implemented module

`fortune-formal/FortuneFormal/Integer/AdaptiveOccupancyCriterion.lean`

The module is imported by `FortuneFormal.lean`.

## Kernel-checked theorems

1. `no_failure_of_rowDependentExp_sum_lt_one`

   A row-dependent exponential detector excludes every failed row when its total mass is below one, because a zero-source row contributes exactly one.

2. `uniformExp_le_rowDependentExp`

   For nonnegative source and `tau_j<=tau_A`, the frozen uniform detector term is no larger than the row-dependent term.

3. `uniformExp_sum_lt_one_of_rowDependent`

   A successful preregistered stratified detector with every temperature below the frozen temperature implies the issue-#54 uniform `INT-AOD` detector bound.

## Validation

Targeted Hugging Face job `6a72bab0a00abefd4b2930d2` completed successfully:

- Lean 4.32.0;
- 8,659 jobs;
- zero build failures;
- terminal sentinel `FORTUNE_INT_AOD_ADAPTIVE_OCCUPANCY_LEAN_PASS`.

The failed intermediate jobs exposed only expression-normalization issues and resulted in no theorem-statement change.

## Trust boundary

The Lean module proves deterministic implications only. It does not prove:

- detector admissibility under the no-tautology protocol;
- `INT-SCG` or any connected-cumulant estimate;
- `INT-AOD`;
- Fortune's conjecture.

No `sorry`, `admit`, new axiom, or unsafe declaration is present.
