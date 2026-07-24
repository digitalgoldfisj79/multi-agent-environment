# Adversarial mathematical audit

## Revised decision

**Gate result: INTERNAL HOLD — FRESH HOSTILE REVIEW FAILED; FIDELITY GATE OPEN.**

The frozen source `RQM_PROOF.md` contains a continuous proof under its explicit frame-admissibility hypothesis, and the clean-room implementation reproduced the finite structural identities selected for checking. Those facts do **not** by themselves establish that the auditor-edited manuscript is a faithful, complete rendering of the frozen proof. The earlier label “provisional pass to external review” therefore overstated what had been verified.

A fresh manuscript-only hostile review has now been completed. It returned **not proved** for the manuscript as supplied. No specialist should receive the manuscript until:

1. the manuscript has been rebuilt as a faithful, self-contained rendering of the frozen proof;
2. a claim-by-claim and dependency-level fidelity comparison has been completed against the exact revised manuscript; and
3. a new fresh hostile review of that revised manuscript closes with no unresolved fatal issue and every major issue repaired or rebutted line by line.

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

## Fresh hostile manuscript-only review

The exact circulation manuscript was supplied without the proof source, audit report, validator output, prior reviews, or a desired verdict to `Qwen/Qwen3-14B` in Hugging Face job `6a6315847ef3c084649671bb`.

- Manuscript SHA-256: `0c28bc000a8b4ff35f2f47ab53572c3d4e8e5649f7b35cda1d7971818d730be6`.
- Prompt SHA-256: `0bfd60eb4e8d4f2f1f2e0ab17c2c31465998744b4504b305b62ef5735da6464c`.
- UTC completion: `2026-07-24T07:39:06.448438+00:00`.
- Archived output: `FRESH_HOSTILE_REVIEW_QWEN3_14B.md`.
- Verdict: **not proved**.

The load-bearing findings are valid and independently visible in the manuscript: decisive definitions are imported only by vague reference; the contour estimate, exceptional-character argument, complete ledger, and dual-row assembly are asserted rather than proved; and the supporting checks are not substitutes for the missing asymptotic proof.

The model output is evidence, not authority. Three points require qualification in the disposition:

1. its description of the configuration identity as comparing a “simple quadratic” with a higher-order expression is algebraically mistaken, because `M(M-1)` is itself quartic in `N`; the valid criticism is that the manuscript does not derive the identity;
2. failure to define the dependence of `C(eta,rho)` is a presentation/quantifier defect, but not independently a fatal mathematical error if the full proof supplies uniform control; and
3. the manuscript does not need a separate proof that a random-order theorem fails to imply Fortune’s conjecture; the scope limitation is logically clear once the models are defined.

Those overstatements do not affect the review gate. The omitted proof chain is sufficient to make the manuscript fail as a standalone theorem paper.

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

1. Replace the extended synopsis with a faithful full-proof manuscript.
2. Complete and archive the frozen-source-to-manuscript fidelity matrix for that revised manuscript.
3. Reconstruct the C2 ledger independently, without relying on the existing audit code.
4. Run a new fresh hostile review on the revised hashed manuscript and dispose of every issue.
5. Resolve every package-manifest mismatch, including any reference to a missing `independent_audit_results.txt`.
6. Only then approach an analytic/probabilistic number theorist and a character-sum specialist.

## External-review sequence

The RQM manuscript should lead the consultation sequence because its frozen source claims a closed theorem and its human review question is sharply bounded. The Airy line should not be sent to the same small specialist pool in the same week; it remains a separate, higher-specialisation consultation after the RQM package has cleared its internal gates.
