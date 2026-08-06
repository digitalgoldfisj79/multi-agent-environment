# Execution runbook

## Order

1. Run `scripts/verify_programme.py` locally or in a short CPU sentinel.
2. Execute C0 and record the exact parent hashes.
3. Freeze C1 geometry before any panel or output-prime inspection.
4. Run C2 and C3 in parallel only after C1 passes.
5. Open C4 before C5; the orbit theorem must use the renormalized local kernel, not raw tuple counts.
6. Open C6 only when C2, C3, C4 and C5 have explicit quantitative outputs.
7. Use C7 only against the C6 norm.
8. Run C8 diagnostics throughout, but never promote them.
9. Close with C9 clean-room validation.

## Compute policy

Every external job command must print

`PROGRAMME=FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1 GATE=<gate> LANE=<lane>`.

- sentinel timeout: 10 minutes;
- ordinary CPU timeout: 45 minutes;
- absolute timeout: 120 minutes unless the runbook is amended before launch;
- GPU is prohibited unless a written gate note demonstrates a GPU-specific need;
- inspect all running jobs before cancellation;
- cancel every orphaned or stale programme job immediately after a branch change;
- do not cancel unrelated jobs.

## Evidence discipline

Each gate produces an execution file containing:

- exact statement tested;
- identities separated from estimates;
- exponent and logarithmic losses;
- job IDs and hashes;
- pass, reduction or obstruction ruling;
- explicit non-claims.

## Closeout validation

- static programme sentinel;
- exact rational combinatorial regressions;
- inherited occupancy-dual verifier;
- inherited integer mainline verifier;
- targeted Lean only after targeted success;
- full clean-room `lake build FortuneFormal`;
- provider sweep with zero active programme jobs.