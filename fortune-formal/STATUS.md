# Current status — Fortune formal discovery programme

**Date:** 4 August 2026  
**Gate:** F4 quadratic emptiness certificate reconstruction  
**Status:** F0–F3 PASSED; ONE PAPER VII AXIOM REMAINS

## Kernel-checked package

- F1 literal finite-field polynomial and endpoint-incidence definitions;
- F2 inverse-free algebraisation and scalar-witness uniqueness;
- F3 common-defect existence, uniqueness and degree bound;
- direct prime-field Artin–Schreier irreducibility;
- zero-defect reflection/translation classification;
- intermediate-strip emptiness by a non-truncated degree contradiction.

The F3 promotion build completed all 8,676 Lean jobs under Lean 4.32.0 and passed the post-build static trust audit.

## Scope corrections found by formalization

- BDD1 requires prime-field scope, the literal base `L = X^q - X`, and `k < q`.
- BDD2 and strip require odd prime characteristic.
- The strip theorem cannot be justified by interpreting `q - 2k` as a negative natural number; it now has a direct degree contradiction.

## Current F4 state

Implemented:

- literal four-equation q-free quadratic model in `FortuneFormal/Quadratic/Model.lean`;
- exact interface for the certified component `U=1`, `B=-2`, `(A-C)^2+4A=0`.

Still required:

1. normalize every genuine `k=2` incidence to the q-free model;
2. prove the two localization charts cover the genuine open locus;
3. import and Lean-check the characteristic-zero lift identities after denominator clearing;
4. check the exceptional-characteristic certificates;
5. prove the final discriminant-square contradiction;
6. delete `FortuneFormal.p7_k2_empty`.

## Exact boundary

No cubic true-Frobenius theorem, endpoint `FFPR`, direct function-field `d=1`, function-field-to-integer transfer, or Fortune theorem is claimed.
