# Claim ledger — Fortune formal discovery programme

**Date:** 4 August 2026  
**Current gate:** F0 specification freeze  
**Formal proof status:** NO PAPER VII THEOREM FORMALIZED YET

## Kernel-checked infrastructure

- Lean/mathlib package configuration is pinned.
- The specification module compiles.
- Temporary assumptions are confined to one file and machine-ledgered.
- `sorry`, `admit`, `unsafe`, and unledgered axioms are prohibited by the static verifier.

## ASSUMED pending formalization

| Lean declaration | Paper claim | Removal gate |
|---|---|---|
| `FortuneFormal.p7_ifa1` | P7-IFA1 inverse-free equivalence and witness uniqueness | F2 |
| `FortuneFormal.p7_bdd1` | P7-BDD1 common-defect existence, uniqueness and degree bound | F3 |
| `FortuneFormal.p7_bdd2` | P7-BDD2 zero-defect reflection/translation classification | F3 |
| `FortuneFormal.p7_strip` | P7-STRIP intermediate-strip emptiness | F3 |
| `FortuneFormal.p7_k2_empty` | P7-K2 quadratic emptiness over odd prime powers | F4 |

These claims are proved or certificate-backed in the Paper VII manuscript package, but they remain **formal assumptions** until the corresponding Lean theorem replaces each declaration.

## OPEN definitions and proof engineering

- literal finite-field polynomial model;
- inverse-free incidence and cross-distinct open locus;
- common-defect construction;
- reflection and translation families;
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
- any extrapolation from q=11,13,17,97 or other finite panels.

## Explicitly not claimed

- that Lean axioms certify their own mathematical truth;
- that Paper VII has been formalized;
- that Comparator has run on this package;
- the cubic true-Frobenius theorem;
- endpoint `FFPR`;
- direct function-field `d=1`;
- any function-field-to-integer transfer;
- Fortune's conjecture.
