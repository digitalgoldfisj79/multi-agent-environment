# Adversarial mathematical audit

## Revised decision

**Gate result: INTERNAL HOLD — FIDELITY AND FRESH-REVIEW GATES OPEN.**

The frozen source `RQM_PROOF.md` contains a continuous proof under its explicit frame-admissibility hypothesis, and the clean-room implementation reproduced the finite structural identities selected for checking. Those facts do **not** by themselves establish that the auditor-edited manuscript is a faithful, complete rendering of the frozen proof. The earlier label “provisional pass to external review” therefore overstated what had been verified.

No specialist should receive the manuscript until both of the following are complete:

1. a claim-by-claim and dependency-level fidelity comparison between the frozen source blobs and the exact manuscript file sent for review; and
2. a genuinely fresh hostile review of that manuscript alone, with no audit report, supportive context, validator output, or prior-session conclusions.

## Frozen source basis

- `RQM_PROOF.md`, blob `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`.
- `PAPER2_ADDENDUM.md`, blob `71a9ad70c7164bcd94b92743fff3d8088c9a158b`.
- `CONDITIONAL_HL_BLOCK.md`, blob `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`.
- Archived Paper II reciprocal-frame definitions, blob `79da1c81b57b051cf8527889e84a6fe1161eb3fe`.

All source files were read from branch `gpt56/d1-gate-bridge-terminal-20260724`, except archived Paper II, which was read from `archive/fortune-paper2-20260720`.

## What the clean-room suite actually verifies

The suite independently checks finite identities and selected normalisations:

1. the `N`-or-`1` difference dichotomy;
2. the coefficient taxonomy;
3. the ordered set-partition identity at finite scale;
4. a numerical instance of the contour inequality;
5. Gauss/CRT coefficient norms;
6. an end-to-end finite slot-character expansion;
7. a finite sixth-moment exceptional-character count;
8. moment and exact-sixth-moment calculations; and
9. symbolic exponent arithmetic for the declared ledger classes.

It does **not** independently verify:

- that every hypothesis and quantifier in the frozen proof appears unchanged in the manuscript;
- that the manuscript proves, rather than merely states, the contour, coordinate, matching, pattern-domination, and ledger steps;
- that the ledger classification is exhaustive at manuscript level;
- that every use of Paper II has been restated or cited correctly;
- that the compiled DOCX/PDF is identical in mathematical content to the repository source; or
- that no claim was strengthened during editorial reconstruction.

## Initial fidelity findings

The repository manuscript currently functions as a condensed research announcement, not a self-contained full proof. In particular:

- the precise frame condition `(N1)` from the frozen source is replaced by undefined shorthand (“nondegenerate” and “admissible”);
- the complete character-slot expansion, triangular coordinate bijection, path matching lemma, and pattern-domination proof are summarized rather than proved;
- the full `T1–T3`, `C1`, `C2a–C2d`, `C3`, `C4` ledger and its multiplicity counts are omitted;
- the binding-class calculation is displayed, but the assertion that all remaining classes are smaller is not established in the manuscript text; and
- several largeness conditions and constants used to turn congruence into equality and control the harmonic tail are absorbed into prose rather than tracked.

These omissions do not refute the frozen theorem. They refute the earlier claim that the reconstructed manuscript itself had already passed a complete proof audit.

## Load-bearing proof chain in the frozen source

1. Frame admissibility gives `D_X>0`, a quantitative lower bound for `D_X`, and diagonal control.
2. Pair-index differences have coefficient patterns of length two to four.
3. Conditioning on ranks gives an exact ordered set-partition law.
4. Multivariate Cauchy gives decay controlled by ratio-character deficits.
5. Gauss inversion converts each additive slot into a character slot with exact norm bounds.
6. Sixth-moment orthogonality and unique factorisation bound the number of bad characters by `O(X log^3 X)`.
7. Ratio coordinates form a tree, permitting an outer-to-inner matching sum.
8. The all-bad pattern dominates every pattern containing good coordinates.
9. The configuration ledger closes.
10. Diagonal and harmonic-tail estimates assemble the fixed-harmonic, aggregate, and Frobenius conclusions.

## No-cushion warning

The binding classes `C2a`, `C2b`, and `C2d` close at exactly

`X^2 log^7 X = M log^9 X`

up to constants and the relation `M asymp X^2/log^2 X`. There is no declared positive power-of-`X` cushion. A missing configuration family, an extra multiplicity factor, or a lost ratio-coordinate saving can therefore break the stated exponent. The clean-room exponent table checks the arithmetic of the declared classes; it does not substitute for an independent reconstruction of class exhaustiveness and multiplicities.

## Framing correction

“No GRH” is literally correct, but incomplete as a summary. The theorem obtains cancellation after expectation over a uniformly random ordering. That permutation average is the principal source of cancellation and has no established analogue for the unique increasing primorial order. External material must state this in the same sentence as the no-GRH claim.

## Residual gates

1. Complete and archive the frozen-source-to-manuscript fidelity matrix.
2. Run a fresh hostile manuscript-only review and preserve the exact input hash, model/session identity, prompt, and unedited output.
3. Reconstruct the C2 ledger independently, without relying on the existing audit code.
4. Resolve every package-manifest mismatch, including any reference to a missing `independent_audit_results.txt`.
5. Only then approach an analytic/probabilistic number theorist and a character-sum specialist.

## External-review sequence

The RQM manuscript should lead the consultation sequence because its frozen source claims a closed theorem and its human review question is sharply bounded. The Airy line should not be sent to the same small specialist pool in the same week; it remains a separate, higher-specialisation consultation after the RQM package has cleared its internal gates.
