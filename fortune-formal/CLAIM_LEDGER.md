# Claim ledger — Fortune formal discovery programme

**Date:** 4 August 2026  
**Current gate:** F3 defect dichotomy and strip  
**Formal proof status:** P7-IFA1 KERNEL-CHECKED; FOUR PAPER VII AXIOMS REMAIN

## Kernel-checked claims

| Lean declaration | Paper claim | Gate | Evidence |
|---|---|---|---|
| `FortuneFormal.Bilateral.p7_ifa1_concrete` | P7-IFA1 inverse-free equivalence and scalar-witness uniqueness | F2 | Clean-room Lean 4.32.0 build and post-build trust audit |

The F2 proof includes both forward polynomial identities and the converse Chinese-remainder/degree argument. It does not rely on finite enumeration or an external algebra certificate.

## Kernel-checked infrastructure

- Lean 4.32.0, mathlib v4.32.0 and Comparator v4.32.0 are pinned.
- Literal finite-field polynomial, endpoint, quotient and defect definitions compile.
- Temporary assumptions are confined to one file and machine-ledgered.
- Prohibited proof holes, unsafe declarations and unledgered axioms are rejected by the static verifier.

## ASSUMED pending formalization

| Lean declaration | Paper claim | Removal gate |
|---|---|---|
| `FortuneFormal.p7_bdd1` | P7-BDD1 common-defect existence, uniqueness and degree bound | F3 |
| `FortuneFormal.p7_bdd2` | P7-BDD2 zero-defect reflection/translation classification | F3 |
| `FortuneFormal.p7_strip` | P7-STRIP intermediate-strip emptiness | F3 |
| `FortuneFormal.p7_k2_empty` | P7-K2 quadratic emptiness over odd prime powers | F4 |

These claims are proved or certificate-backed in the Paper VII manuscript package, but remain formal assumptions until the corresponding Lean theorem replaces each declaration.

## OPEN proof engineering

- common-defect construction and uniqueness;
- defect degree bound;
- zero-defect reflection/translation classification;
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

- that the four remaining Lean axioms certify their own mathematical truth;
- that all of Paper VII has been formalized;
- that Comparator has accepted a completed Paper VII package;
- the cubic true-Frobenius theorem;
- endpoint `FFPR`;
- direct function-field `d=1`;
- any function-field-to-integer transfer;
- Fortune's conjecture.
