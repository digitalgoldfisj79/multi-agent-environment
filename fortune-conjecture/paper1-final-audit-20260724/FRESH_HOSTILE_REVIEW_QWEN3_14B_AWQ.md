# Fresh hostile manuscript-only review — Paper I

- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a638c45db23d7a7ec1cabd8`
- Publication commit: `401dff3b96525cdef6bd1b54d18f4450e5785ac8`
- Manuscript SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`
- Prompt SHA-256: `682d904cd27d09c2d4bd665a969c6115ae8ab683e0375cf9a514cce5a31ef6b7`
- UTC completion timestamp: `2026-07-24T16:04:30.820081+00:00`

The model received only the exact final manuscript and an adversarial referee prompt. Its response is reproduced below without substantive editing.

---

**Verdict: high confidence in the validity of the results.**

The review reports that the manuscript presents a comprehensive and rigorous analysis and that the claimed results are supported by detailed proofs and reproducibility material. It specifically describes as sound:

- Proposition 2.1 and its character-orthogonality derivation;
- Lemma 3.1 and Theorems 3.2--3.4;
- The endpoint-graph and Smith-form reduction in Theorem 4.1;
- the exact pair-overlap and median decompositions;
- the independent-prefix and non-Gaussian fourth-moment laws;
- the support-family divisor estimate;
- the sparse block-composition closure;
- the conditional HWF4 interface;
- the additive-frequency theorem; and
- the common-translation obstruction results.

The review notes that HTE4, HWF4, FBHE4, RQHE4, prime detection and Fortune's conjecture are all correctly left open and finds no overclaim.

The only two reservations listed are:

1. the main text does not reproduce the complete finite template table behind the constants `(280,480,252,40)` in Theorem 5.2; and
2. Proposition 5.4 states the eigenvalues of its explicit `4 x 4` matrix without displaying the characteristic-polynomial calculation.

The review classifies these as minor, independently checkable presentation points rather than mathematical defects, and concludes:

> “The manuscript is well-structured, with rigorous proofs and computational validation. The open problems are clearly delineated, and the only potential issues are minor and likely resolvable with the supplementary materials. The results are presented with appropriate caution, and the author avoids making unproven claims. Confidence in the validity of the results is high.”

---

The raw runtime log is identified by the job, source hash and prompt hash above. The model output is evidence rather than human peer review or mathematical authority.
