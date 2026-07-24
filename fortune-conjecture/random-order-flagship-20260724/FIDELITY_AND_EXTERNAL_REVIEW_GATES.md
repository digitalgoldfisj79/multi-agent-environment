# Fidelity and external-review gates

## Purpose

This document separates four questions that had previously been conflated:

1. Is there a continuous proof in the frozen research source?
2. Do the finite clean-room checks reproduce selected identities used by that proof?
3. Does the exact circulation manuscript faithfully and completely reproduce the frozen proof?
4. Has an independent hostile reader found no fatal defect in the circulation manuscript?

The current evidence supports (1) and selected parts of (2). Gate (3) is open. Gate (4) has been tested on the current manuscript and failed: the fresh reviewer returned **not proved**.

## Gate F1 — frozen-source fidelity

The exact DOCX/PDF/Markdown file sent to a reviewer must be checked against these frozen blobs:

- `RQM_PROOF.md`: `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`;
- `PAPER2_ADDENDUM.md`: `71a9ad70c7164bcd94b92743fff3d8088c9a158b`;
- `CONDITIONAL_HL_BLOCK.md`: `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`;
- archived Paper II definitions: `79da1c81b57b051cf8527889e84a6fe1161eb3fe`.

The fidelity matrix must record, for every load-bearing item:

| Item | Frozen source location | Manuscript location | Status | Notes |
|---|---|---|---|---|
| Quantitative frame admissibility and lower bound for `D_X` | RQM §0, `(N1)` | Pending | Open | Shorthand is insufficient unless defined equivalently. |
| PNT block-size bounds and relation between `M`, `N`, and `X` | RQM §0, `(N2)` | Pending | Open | Preserve all uses in diagonal and ledger estimates. |
| Exact theorem quantifiers in `q,r,a,X,eta,rho` | RQM §0 | Pending | Open | No strengthening or loss of uniformity. |
| Configuration taxonomy and multiplicities | RQM §2 | Pending | Open | Must include sliding-family multiplicity `N`. |
| Ordered set-partition identity | RQM §3.1 | Pending | Open | Include empty-cell handling. |
| Contour inequality and prefactor | RQM §3.2 | Pending | Open | Include phase-uniformity and all constants used later. |
| Gauss/CRT expansion and coefficient norms | RQM §4 | Pending | Open | Include principal components and collapsed initial slot. |
| Bad-character count | RQM §5 | Pending | Open | Include the largeness condition turning congruence into equality. |
| Triangular coordinate bijection | RQM §6.1 | Pending | Open | Include front/back orphan definitions. |
| Path matching lemma | RQM §6.2 | Pending | Open | Preserve summation order and group norms. |
| Pattern domination | RQM §6.3 | Pending | Open | Preserve the per-free-coordinate margin. |
| Full `T/C` ledger | RQM §7 | Pending | Open | Every class, count, multiplicity, and exponent. |
| Fixed-harmonic assembly | RQM §8(i) | Pending | Open | Preserve absolute-value and diagonal steps. |
| Aggregate and Frobenius assembly | RQM §8(ii) | Pending | Open | Preserve small/large harmonic split and Paper II dependency. |
| Scope limitation | RQM header and theorem | Pending | Open | Random order is not increasing primorial order. |

### F1 acceptance criterion

Every row is either:

- **verbatim-equivalent**, with only notation or exposition changed; or
- **changed with proof**, where the manuscript supplies a new complete argument and the change is explicitly logged.

A prose assertion that omitted details are “standard,” “checked,” or “in the package” does not close a row.

## Initial F1 finding

The repository manuscript at `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md` does not currently meet the criterion for a self-contained proof paper. It states the decisive contour, expansion, matching, and ledger conclusions at summary level and displays only the binding configuration rather than the complete ledger. It should be classified as an extended synopsis until replaced by a faithful full proof.

## Gate F2 — fresh hostile manuscript-only review

The review input must contain only:

- the exact manuscript file;
- a neutral instruction to find errors and decide whether the theorem is proved.

It must not contain:

- this audit report;
- prior positive verdicts;
- clean-room results;
- a proof dependency graph;
- novelty claims;
- reviewer-targeting language; or
- any statement that the theorem has already passed.

The archive must preserve:

- manuscript SHA-256;
- model or reviewer identity;
- date and session identifier;
- exact prompt;
- unedited output;
- an issue-by-issue disposition written only after the review is frozen.

### F2 acceptance criterion

No unresolved fatal issue, and every major issue has either been repaired in a new hashed manuscript or rebutted with a line-level proof.

### F2 run 1 — completed, acceptance failed

- Model: `Qwen/Qwen3-14B`.
- Hugging Face job: `6a6315847ef3c084649671bb`.
- Manuscript SHA-256: `0c28bc000a8b4ff35f2f47ab53572c3d4e8e5649f7b35cda1d7971818d730be6`.
- Prompt SHA-256: `0bfd60eb4e8d4f2f1f2e0ab17c2c31465998744b4504b305b62ef5735da6464c`.
- Archived response: `FRESH_HOSTILE_REVIEW_QWEN3_14B.md`.
- Verdict: **not proved**.

The review correctly identified that the manuscript does not supply the decisive contour, exceptional-character, complete-ledger, and assembly proofs. Some individual classifications in the raw output are overstated or partially mistaken; those are disposed of in `AUDIT_REPORT.md`. They do not alter the failed gate because the missing load-bearing proof chain is independently visible.

A second F2 run should target the revised full-proof manuscript, not the present synopsis.

## Gate F3 — package integrity

Before circulation:

1. regenerate DOCX, PDF, and ZIP from the cleared manuscript source;
2. compute SHA-256 for every artifact;
3. verify that the text extracted from DOCX/PDF matches the cleared source mathematically;
4. ensure every referenced file is present;
5. ensure every present validation artifact is named consistently; and
6. remove stale claims that the package has passed a gate which remains open.

The canonical clean-room result file in this branch is `independent_audit_results.json`. A reference to `independent_audit_results.txt` is invalid unless that file is actually generated and included.

## Gate F4 — human specialist review

Only after F1–F3 close should the package go to external specialists. The first ask should be narrowly framed:

- verify the contour/coordinate/matching/ledger chain;
- determine whether the theorem is already known;
- assess whether the random-order theorem has independent publication value.

The package must disclose LLM assistance before the specialist begins work.

## Consultation sequencing

RQM should be the first external consultation. It has a purportedly closed theorem in a comparatively standard analytic/probabilistic number-theory register. The Airy package requires a narrower wild-cohomology/characteristic-dependent skill set and should be held until the RQM request is completed or routed to a distinct specialist. Do not send both packages to the same small network in the same week.
