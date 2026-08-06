# Autonomous run protocol

Each research round is one committed unit and must contain:

1. **Frozen question.** One theorem, estimate or obstruction only.
2. **Why it is load-bearing.** Exact dependency on the current primary target.
3. **Exponent budget.** Input scale, output scale and every loss.
4. **Sentinel.** Smallest calculation capable of invalidating the approach.
5. **Main execution.** Only after the sentinel passes.
6. **Independent check.** Separate derivation, implementation or formal verification.
7. **Ruling.** `PROMOTE`, `REFINE`, `KILL` or `CLOSEOUT`.
8. **Compute sweep.** Record all programme job IDs and leave zero programme jobs running.

## Required round files

- `ROUND_<NN>_QUESTION.md`
- `ROUND_<NN>_EXPONENTS.json`
- `ROUND_<NN>_RESULT.md`
- `ROUND_<NN>_JOBS.json`

## Promotion rules

A round is promoted only if it does at least one of:

- proves a new implication in the frozen dependency graph;
- improves a registered exponent or logarithmic loss;
- reduces the target to a strictly smaller theorem;
- supplies a rigorous countermodel or lower bound killing a method.

Equivalent notation, additional numerical range, a larger finite panel, another quotient, or another moment formula is not a promotion.

## Compute rules

- Sentinel timeout: 10 minutes.
- Ordinary job timeout: 45 minutes.
- Absolute timeout: 120 minutes, requiring a committed justification before launch.
- Jobs invalidated by a failed sentinel are cancelled immediately.
- At round close, inspect all provider jobs. Cancel only jobs tagged to this programme; leave unrelated jobs untouched.
- A round cannot close while a programme job remains running.

## Reporting rule

Progress reports must state which dependency edge or exponent changed. They must not use “nearly proved”, “one lemma away” or similar language unless the remaining lemma is frozen, strictly smaller and sufficient.