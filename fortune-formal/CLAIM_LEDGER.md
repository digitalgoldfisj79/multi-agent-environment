# Claim ledger — Fortune formal discovery programme

**Date:** 4 August 2026  
**Current gate:** F3 zero-defect classification and strip  
**Formal proof status:** P7-IFA1 KERNEL-CHECKED; P7-BDD1 KERNEL-CHECKED; THREE PAPER VII AXIOMS REMAIN

## Kernel-checked claims

| Lean declaration | Paper claim | Gate | Evidence |
|---|---|---|---|
| `FortuneFormal.Bilateral.p7_ifa1_concrete` | P7-IFA1 inverse-free equivalence and scalar-witness uniqueness | F2 | Clean-room Lean 4.32.0 build and post-build trust audit |
| `FortuneFormal.Bilateral.p7_bdd1_concrete` | P7-BDD1 common-defect existence, uniqueness and degree bound | F3 | Clean-room Lean 4.32.0 build and post-build trust audit |

The BDD1 formalization proves, from a literal inverse-free incidence, existence of the four quotient polynomials; the two exact transfer identities; divisibility by both modulus pairs; existence and uniqueness of one common defect; and the bound `deg h ≤ q - 2k`.

The formal audit corrected the theorem interface to its manuscript scope: prime field, literal Frobenius base `L = X^q - X`, and `k < q`. The earlier abstract F0 statement omitted these hypotheses and was too broad. No over-scoped theorem is claimed.

## Kernel-checked infrastructure

- Lean 4.32.0, mathlib v4.32.0 and Comparator v4.32.0 are pinned.
- Literal finite-field polynomial, endpoint, quotient, Frobenius-base and defect definitions compile.
- Temporary assumptions are confined to one file and machine-ledgered.
- Prohibited proof holes, unsafe declarations and unledgered axioms are rejected by the static verifier.

## ASSUMED pending formalization

| Lean declaration | Paper claim | Removal gate |
|---|---|---|
| `FortuneFormal.p7_bdd2` | P7-BDD2 zero-defect reflection/translation classification | F3 |
| `FortuneFormal.p7_strip` | P7-STRIP intermediate-strip emptiness | F3 |
| `FortuneFormal.p7_k2_empty` | P7-K2 quadratic emptiness over odd prime powers | F4 |

These claims are proved or certificate-backed in the Paper VII manuscript package, but remain formal assumptions until the corresponding Lean theorem replaces each declaration.

## OPEN proof engineering

- Artin–Schreier irreducibility over the prime field for `X^q - X ± λ`, `λ ≠ 0`;
- zero-defect reduction to the factorization `(L - λ)(L + λ)`;
- reflection/translation reconstruction from the two factor orderings;
- intermediate-strip deduction;
- certificate import/checking architecture for the quadratic theorem;
- true Frobenius orientation predicate;
- cubic faithful saturation and sign-torsor interfaces.

## Future single research frontier

After F4, the programme must isolate one assumption only:

`FortuneFormal.cubic_true_frobenius_point_theorem`.

That declaration does not yet exist. Its exact type will be frozen at F5 after the faithful cubic definitions and weakest sufficient application statement are established.

## Empirical or computational material excluded from theorem status

- cubic orbit-count trends;
- tangent-dimension and formal-jet evidence on the q-free relaxation;
- finite-panel `O(1)` or positive-density interpretations;
- amplitude trends;
- extrapolation from finite panels.

## Explicitly not claimed

- that the three remaining Lean axioms certify their own mathematical truth;
- that all of Paper VII has been formalized;
- that Comparator has accepted a completed Paper VII package;
- the cubic true-Frobenius theorem;
- endpoint `FFPR`;
- direct function-field `d=1`;
- any function-field-to-integer transfer;
- Fortune's conjecture.
