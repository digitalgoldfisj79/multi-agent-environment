# Claim ledger — Fortune formal discovery programme

**Date:** 4 August 2026  
**Current gate:** F4 quadratic emptiness certificate reconstruction  
**Formal proof status:** P7-IFA1, P7-BDD1, P7-BDD2 and P7-STRIP KERNEL-CHECKED; ONE PAPER VII AXIOM REMAINS

## Kernel-checked claims

| Lean declaration | Paper claim | Gate | Evidence |
|---|---|---|---|
| `FortuneFormal.Bilateral.p7_ifa1_concrete` | P7-IFA1 inverse-free equivalence and scalar-witness uniqueness | F2 | Clean-room Lean 4.32.0 build and post-build trust audit |
| `FortuneFormal.Bilateral.p7_bdd1_concrete` | P7-BDD1 common-defect existence, uniqueness and degree bound | F3 | Clean-room Lean 4.32.0 build and post-build trust audit |
| `FortuneFormal.Bilateral.p7_bdd2_concrete` | P7-BDD2 zero-defect reflection/translation classification | F3 | Clean-room Lean 4.32.0 build of 8,676 jobs and post-build trust audit |
| `FortuneFormal.Bilateral.p7_strip_concrete` | P7-STRIP intermediate-strip emptiness | F3 | Same clean-room Lean 4.32.0 build and post-build trust audit |

The F3 theorem chain includes a direct formal proof that `X^q - X - a` is irreducible over a prime field when `a ≠ 0`, the zero-defect normal form, factor ordering, explicit reconstruction of the reflection and translation families, and a non-truncated degree contradiction for the strip.

The formal audit corrected the manuscript interface in two places:

- BDD1 requires the literal prime-Frobenius base `L = X^q - X`, prime-field scope and `k < q`;
- BDD2 and strip require odd prime characteristic because the factor classification distinguishes `L - λ` from `L + λ`.

No characteristic-two or over-scoped version is claimed.

## Kernel-checked infrastructure

- Lean 4.32.0, mathlib v4.32.0 and Comparator v4.32.0 are pinned.
- Literal finite-field polynomial, endpoint, quotient, Frobenius-base and defect definitions compile.
- Temporary assumptions are confined to one file and machine-ledgered.
- Prohibited proof holes, unsafe declarations and unledgered axioms are rejected by the static verifier.

## ASSUMED pending formalization

| Lean declaration | Paper claim | Removal gate |
|---|---|---|
| `FortuneFormal.p7_k2_empty` | P7-K2 quadratic emptiness over odd prime powers | F4 |

The quadratic theorem is proved by the Paper VII computer-assisted certificate package, but remains a formal assumption until the incidence-to-model bridge, localization certificates and discriminant contradiction are reconstructed in Lean.

## OPEN proof engineering

- faithful normalization from a genuine `k = 2` incidence to the q-free four-equation model;
- proof that every genuine incidence lies in one of the two valid localization charts;
- Lean checking of characteristic-zero lift identities after denominator clearing;
- direct exceptional-characteristic certificate checking;
- final discriminant-square contradiction;
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

- that the remaining Lean axiom certifies its own mathematical truth;
- that all of Paper VII has been formalized;
- that Comparator has accepted a completed Paper VII package;
- the cubic true-Frobenius theorem;
- endpoint `FFPR`;
- direct function-field `d=1`;
- any function-field-to-integer transfer;
- Fortune's conjecture.
