# Manuscript-only independent mathematical referee prompt

Review the supplied manuscript as a standalone, sceptical mathematical referee. You have no access to internal source notes. Your expertise should cover modular representation theory, cyclic group cohomology, Hattori--Stallings traces, arithmetic geometry, Artin--Schreier and Kummer descent, and finite-field point counting.

Do not summarise or encourage. Determine whether every result is proved at its stated scope.

Required checks:

1. Audit every named theorem and proposition separately.
2. Check the Cartier first-moment definitions and distinguish sufficient nonvanishing from unproved uniform nonvanishing.
3. Check the translation projector and reciprocal q-line weight, including signs and boundary contributions.
4. Check the cyclotomic expansion, coefficient ring, valuation of `p`, tangent extension, Tate maps and Bockstein.
5. Check whether the family of Frobenius lifts really proves the claimed Smith/Tate blindness.
6. Check the root-cycle hook character, its fractional Fourier multiplicities and the conclusion that no ordinary divided-hook perfect complex exists.
7. Check the Hattori--Stallings coefficient extraction and every factor of `p`.
8. Check freeness of the root-cycle action, the cyclic transfer, the sign in `y`, and the Artin--Schreier equation.
9. Check the Frobenius-shift interpretation and the exact bijection between nonzero levels and irreducible fibres.
10. Check the logarithmic-derivative no-split theorem and its exceptional-prime boundary.
11. Check the Kummer cohomology classification, the exact sign-twist criterion and the factors of two in the common quotient counts.
12. Check the unique projective fixed point, the isolated wild quotient assertion and whether any unproved singularity property is used.
13. Check the compactified point-count formula, boundary decomposition and the claim that a standard congruence cannot prove the crown.
14. Identify hidden dependencies, circularity, missing assumptions, unmarked computer-assisted inputs, Frobenius conventions, Tate twists and exceptional cases.
15. Distinguish mathematical errors from exposition defects.

Output format:

## A. Overall verdict
Choose exactly one: `PROVED AS STATED`, `CONDITIONALLY CORRECT`, `MAJOR REVISION`, or `FAILED`.

## B. Load-bearing findings
For each numbered finding give severity, exact section/formula, issue, and whether it is editorial or requires new mathematics.

## C. Theorem-by-theorem ledger
For every named theorem/proposition give: proved from manuscript; correct assuming identified standard theorem; incomplete; or false/overstated.

## D. Hidden dependencies and convention audit
List all external theorems, computer inputs, sign conventions, Frobenius conventions, Tate twists and prime restrictions needing explicit treatment.

## E. Required amendments
Give the minimal exact amendment list.

## F. Final referee statement
State whether internal technical pass is justified after amendments and whether either the function-field or integer Fortune conjecture is proved.

Do not use web search or infer missing arguments from likely author intent. Review only the supplied manuscript.