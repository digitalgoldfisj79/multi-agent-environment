# Adversarial mathematical audit

## Current decision

**Gate result: INTERNAL TECHNICAL PASS — HUMAN SPECIALIST REVIEW OPEN.**

The original 207-line Paper IV manuscript was a condensed research announcement and failed manuscript-only hostile review because it omitted the load-bearing proof chain. It has been replaced by a 1,051-line proof manuscript faithfully reconstructed from frozen `RQM_PROOF.md`, independently checked at the configuration-ledger level, reviewed alone by a third-party model, and compiled through a reproducible publication workflow whose output has passed extraction, checksum, accessibility, PDF-preflight and page-by-page visual QA.

Final reviewed source:

- path: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`;
- Git blob: `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`;
- SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`;
- source scan: 30,976 characters, 1,051 lines, no control characters or unresolved placeholders.

The gates now close as follows:

1. frozen-source fidelity — **passed**;
2. independent ledger reconstruction — **passed**;
3. fresh manuscript-only hostile review — **passed after disposition**;
4. compiled PDF/DOCX/ZIP integrity — **passed**;
5. human specialist review — **open**.

This is not a claim of human peer review, journal acceptance, or a proof of Fortune's conjecture.

## Frozen source basis

- `RQM_PROOF.md`, blob `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`;
- `PAPER2_ADDENDUM.md`, blob `71a9ad70c7164bcd94b92743fff3d8088c9a158b`;
- `CONDITIONAL_HL_BLOCK.md`, blob `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`;
- archived Paper II reciprocal-frame definitions, blob `79da1c81b57b051cf8527889e84a6fe1161eb3fe`.

The rebuilt manuscript isolates one precise external mathematical dependency: the Paper II Frobenius comparison. Every other load-bearing estimate from the frozen proof is proved in Paper IV.

## Rebuild coverage

The rebuilt manuscript now contains:

1. the quantitative frame-admissibility and effective PNT hypotheses;
2. the exact diagonal/distinct-modulus energy expansion and zero-mass convention;
3. path rigidity, unit multipliers, complete coefficient taxonomy and exact multiplicities;
4. the exact ordered-set-partition coefficient identity;
5. the full multivariate Cauchy-contour estimate with prefactor;
6. Gauss/CRT inversion and one-slot/two-slot coefficient norms;
7. sixth-moment orthogonality, the explicit `X>8/eta^2` largeness condition and the `6K^3` collision count;
8. triangular ratio coordinates, orphan handling and the outer-to-inner matching lemma;
9. pattern domination using positive upper bounds `U(P)`, including the explicit `X^{-23f}` margin and all 15 non-all-bad patterns;
10. the disjoint complete `T1–T3`, `C1`, `C2a–C2d`, `C3`, `C4` ledger;
11. the no-cushion calculation for binding classes `C2a`, `C2b`, `C2d`;
12. fixed-harmonic, aggregate, Schwartz-tail and Frobenius assembly; and
13. scope limitations and LLM-assistance disclosure.

The full dependency map is archived in `REBUILT_MANUSCRIPT_FIDELITY_MATRIX.md`.

## Independent ledger reconstruction

`INDEPENDENT_LEDGER_RECONSTRUCTION.md` was written independently of the original audit implementation. For `N=3,...,10` and three micro-cell thresholds, it enumerates all ordered pairs of two-element multisets and verifies:

- the exact total `M(M-1)`;
- type-S multiplicity exactly `N` and every other multiplicity exactly `1`;
- no unclassified configuration;
- no double assignment under the rebuilt disjoint ledger; and
- the binding exponent arithmetic.

All panels passed. The exact algebraic identity is

`M(M-1) = N(N+1)(N-1)(N+2)/4`

and equals

`N^2(N-1)+N(N-1)+6*C(N,3)+6*C(N,4)`.

## Final hostile manuscript-only review

The exact final source was supplied alone to `Qwen/Qwen3-14B-AWQ` in Hugging Face job `6a6325e7db23d7a7ec1ca14a`.

- manuscript SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`;
- prompt SHA-256: `1bb3ba966a21ee69bd24c589aea778f3b4c326329e924585323ffd1b3bb77b67`;
- archived raw response: `FRESH_HOSTILE_REVIEW_FINAL_QWEN3_14B_AWQ.md`;
- headline verdict: **proved**.

The response also listed three objections. `FINAL_HOSTILE_REVIEW_DISPOSITION.md` rebuts all three against the exact reviewed text:

1. the multiplicity identity is algebraically exact and independently enumerated;
2. Lemma 5.2 explicitly starts with `X>8/eta^2`; and
3. Lemma 6.3 explicitly bounds `C_*K^2`, both edge-group ratios and all 15 non-all-bad patterns.

There is no unresolved fatal or major issue from the fresh hostile review. The model output is evidence, not mathematical authority; the source remains subject to human specialist scrutiny.

## Compiled-artifact QA

The canonical publication build is GitHub Actions workflow run `30085400790`, publication commit `af9350f06e41e94d79f583b2e8fca45b55b92852`, artifact ID `8593522378`, artifact digest `sha256:1875d3965d611cffa0a70afc223caf0e3119d93f79183f3f7a9be214f3486a51`.

All workflow steps passed. The downloaded package then passed independent checksum verification and visual inspection.

- PDF SHA-256: `dc5ff454826f605d5fd4db4ba02f6a35df1013bde1cfe9a9d9e26a6c8fc6f1a3`;
- DOCX SHA-256: `3ecac48465573b9305cafb119779a5e17c65b2bd2fc05f7d376ec55895b3b61b`;
- canonical internal ZIP SHA-256: `19c790caa196cf6374f62f90e4d9da4ea2dfc559a4894fd8e7dfdb4a62b5ec43`.

The PDF is A4, 12 pages, text-native, unencrypted, without XFA or preflight warnings. Every page was rendered at 180 dpi and inspected; no clipping, overlap, raw TeX, malformed equation, missing glyph or page-boundary defect remains. The DOCX is A4 and renders to 15 pages; its accessibility audit has zero findings, its heading hierarchy has no skipped level, all 48 equation labels are present, and every page was inspected. Details are in `COMPILED_ARTIFACT_QA.md`.

The visual gate caught and eliminated an earlier build-only defect in which TeX single-backslash delimiters were rendered literally. The final PDF uses XeLaTeX directly from the reviewed source. The DOCX uses documented notation-only OMML normalisations; the source itself remains unchanged.

## No-cushion warning

The binding classes close at

`X^2 log^7 X = M log^9 X`

up to constants and `M asymp X^2/log^2 X`. There is no positive power-of-`X` cushion. This is why independent multiplicity and exhaustiveness reconstruction was required and why human review should focus on the contour/coordinate/matching/ledger chain.

## Framing correction

“No GRH” is literally correct but incomplete unless paired with the source of cancellation. The theorem obtains cancellation after expectation over a uniformly random ordering. It gives no pointwise theorem for the unique increasing primorial order and does not prove Fortune's conjecture.

## Remaining gate

Send the technically cleared package first to:

1. an analytic/probabilistic number theorist to inspect the ordered-partition and contour mechanism; and
2. a character-sum specialist to inspect Gauss/CRT normalisation, the sixth moment, matching and the no-cushion ledger.

The Airy consultation should remain separate or later because it requires a narrower specialist pool.
