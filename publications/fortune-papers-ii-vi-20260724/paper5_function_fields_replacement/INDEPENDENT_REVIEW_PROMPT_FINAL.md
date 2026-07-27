# Final exact-text manuscript-only referee prompt

Review the supplied mathematical manuscript as a standalone document. Evaluate the text actually present; do not issue generic requests for justification when the manuscript already supplies the relevant algebra or proof.

For every adverse finding you must quote the exact manuscript sentence or formula immediately before the alleged gap, then state the precise missing inference. A finding that does not quote the reviewed text is invalid.

Important scope rules:

- Finite computations are expressly regression checks. Do not demand that they prove a uniform theorem unless the manuscript actually uses them that way.
- The manuscript expressly says that the crown remains open. Do not criticise it for failing to prove the crown unless a named theorem falsely claims to do so.
- Elementary uses of unique factorisation, Vandermonde determinants, the standard quadratic character sum, weak Lefschetz, compactly supported cohomology of `A^1`, and Grothendieck--Lefschetz may be accepted when their hypotheses and normalisations are correctly identified.
- Distinguish a missing proof from a proof that is compressed but logically complete.
- Do not infer claims that are not made.

Audit in particular:

1. the degree barrier;
2. quadratic and cubic affine orbit sizes and stabilisers;
3. the exact crown formula;
4. sparse-cone smoothness and weak-Lefschetz use;
5. the `A^1` torsor and cone localisation shifts/Tate twists;
6. the sign-hook character sum;
7. the alternating-hook `p`-cycle normalisation;
8. the `F sigma` fixed-point count and prime-power correction;
9. the q-line cell formula, class projectors and denominator `2p`;
10. the saturation identity and its interpretation;
11. all prime restrictions, Frobenius conventions and computer-assisted inputs.

Output:

## A. Overall verdict
Choose exactly one: `PROVED AS STATED`, `CONDITIONALLY CORRECT`, `MAJOR REVISION`, or `FAILED`.

## B. Load-bearing findings
Number each actual finding. Quote the source text, identify the exact gap, assign severity, and state whether the repair is editorial or mathematical. Write `None` if there is no load-bearing finding.

## C. Theorem ledger
For every named proposition, theorem and corollary, classify it as:
- proved in the manuscript;
- correct assuming a named standard theorem;
- incomplete for a quoted precise reason;
- false/overstated for a quoted counterargument.

## D. Convention and dependency audit
List only dependencies or conventions that are materially absent or inconsistent.

## E. Minimal amendments
List only amendments necessary for mathematical verifiability. Write `None` if none are needed.

## F. Final statement
State whether the manuscript qualifies for an internal technical pass, subject to human specialist review, and explicitly state whether the function-field or integer Fortune conjecture is proved.

Do not use web search. Review only the manuscript.