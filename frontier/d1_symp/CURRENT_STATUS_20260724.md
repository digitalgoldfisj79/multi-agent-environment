# Function-field \(d=1\) Fortune programme — current status

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-gate-bridge-terminal-20260724`  
**Base commit:** `f376dd54df2cabe0ca323d7609b9eaef02afdd4e`  
**Scope:** function-field sibling only; integer Fortune is untouched.

## Read this first

This file supersedes the dated terminal summaries for the current branch.
Historical notes remain intact because they record the sequence of
corrections and failure certificates.

## New in this branch

1. Claude's PREREG-8 prediction and independent \(F^3\) measurement package
   has been preserved under `prereg8/`, including exact source files,
   human-readable JSON, base64 copies of the original pickle bytes and
   SHA-256 provenance.
2. The six third-power traces at \(p=17,23,29\) all reproduce exactly.
3. The Gaussian maximum correction was independently recomputed:
   \(E\max|Z|=3.8418853\) for \(n=4806\), and the observed maximum is at the
   \(5.33\) percentile. The sweep gives no directional evidence on boundedness.
4. `Gate 0'` has been completed: the repository lacks the exact transport
   coefficient from \(T_p\) into the irreducibility ledger, so the crown's
   tolerance for logarithmic slack is presently unknowable.
5. A cold bridge audit classifies the object-level comparison and punctual
   transport as theorem-hard. The other ledger tasks are finite assembly once
   that comparison exists.
6. A consultation package and a terminal research-note draft have been added.

## Proved

- the exact \(d=1\) sparse-family and incidence reductions;
- the cubic trace-zero collapse for \(p\equiv2\pmod3\);
- the Airy Adams trace identity, with corrected global sign;
- zero local Swan conductor for the \(p\)-th Adams virtual sheaf;
- equal rank \((p-5)/6\) of the two \(\mu_3\)-invariant trace spaces;
- the odd-power trace-extraction lemma;
- self-duality/reciprocity of the odd symmetric-power invariant spaces;
- all stated route-failure certificates;
- the \(O(\sqrt p)\)-coefficient unconditional bound.

## Exact computer-assisted theorems

- certification of the Fortune sibling for every odd prime \(p<1200\);
- exact first traces and \(F^3\) traces at the committed primes;
- low-rank characteristic polynomials through rank four;
- independent PREREG-8 reproduction of all six \(F^3\) traces;
- exact common-factor and Newton-slope rulings.

## Open

### Analytic theorem
\[
 |T_p|\le C p^{(p-1)/2}
\]
with absolute \(C\), equivalently the characteristic-boundary correlation
between \(U_p\) and \(U_{p-2}(-1)\).

### Application theorem
An object-level comparison transporting the Airy boundary complex into the
exact irreducibility hook/nearby-cycle ledger, with all subtractions, twists
and boundary cells explicit.

The full function-field Fortune crown is not proved until both packages are
closed.

## Stop rule

Further prime sweeps or autonomous route generation are not decision-useful.
Computation should resume only to test a concrete structural identity or an
expert-proposed formula. The next productive action is targeted external
consultation using `CONSULTATION_PACKAGE_20260724.md`.

## Read order

1. `CURRENT_STATUS_20260724.md`
2. `F3_PREREG8_INDEPENDENT_VERIFICATION_20260724.md`
3. `GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md`
4. `BRIDGE_ASSESSMENT_20260724.md`
5. `CONSULTATION_PACKAGE_20260724.md`
6. `TERMINAL_RESEARCH_NOTE_DRAFT_20260724.md`
7. prior theorem and failure-certificate notes
