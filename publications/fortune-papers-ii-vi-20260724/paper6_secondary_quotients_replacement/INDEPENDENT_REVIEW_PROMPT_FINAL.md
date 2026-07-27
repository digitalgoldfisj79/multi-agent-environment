# Final exact-text manuscript-only referee prompt

Review the supplied mathematical manuscript as a standalone document. Evaluate the proof text actually present. For every adverse finding, quote the exact sentence or display immediately before the alleged gap and identify the precise missing inference. Generic statements such as “a complete proof is required” without a quotation and logical diagnosis are invalid.

Scope rules:

- The implication `M_a != 0 => N_a > 0` is distinct from the expressly open claim that `M_a` is uniformly nonzero.
- Finite computations are regression checks only. Do not demand that they prove a uniform theorem unless the manuscript uses them that way.
- The crown is expressly open. Do not criticise the paper for not proving it unless a named result falsely claims it.
- Standard cyclic Tate complexes, the irreducible-character basis of a finite cyclic group, Artin--Schreier torsor classification, Kummer cohomology and elementary finite-field power sums may be accepted when hypotheses and normalisations are identified.
- Distinguish a compressed but complete proof from an absent proof.

Audit:

1. Cartier moment and translation/q-line projectors;
2. cyclotomic tangent and three-mode dependence;
3. tangent extension, Tate groups, Bockstein and Frobenius blindness;
4. divided-hook character obstruction;
5. Hattori--Stallings coefficient extraction and factors of `p`;
6. cyclic transfer, Artin--Schreier coordinate and irreducibility levels;
7. no-split theorem;
8. Kummer classification, sign criterion and quotient counts;
9. unique projective fixed point and wild-singularity caveat;
10. compactified count and congruence obstruction;
11. prime restrictions, Frobenius conventions and exact-computation scope.

Output:

## A. Overall verdict
Choose exactly one: `PROVED AS STATED`, `CONDITIONALLY CORRECT`, `MAJOR REVISION`, or `FAILED`.

## B. Load-bearing findings
Quote the reviewed text for every actual finding, identify the precise gap, severity and repair. Write `None` if none.

## C. Theorem ledger
Classify every named proposition/theorem as proved in the manuscript; correct assuming an identified standard input; incomplete for a quoted reason; or false/overstated.

## D. Convention and dependency audit
List only materially absent or inconsistent dependencies/conventions.

## E. Minimal amendments
List only mathematically necessary amendments. Write `None` if none.

## F. Final statement
State whether internal technical pass is justified subject to human specialist review, and whether either Fortune conjecture is proved.

Do not use web search. Review only the manuscript.