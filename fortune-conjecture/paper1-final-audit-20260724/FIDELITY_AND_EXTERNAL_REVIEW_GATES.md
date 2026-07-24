# Fidelity and external-review gates — Paper I

## Exact object

- Publication commit: `401dff3b96525cdef6bd1b54d18f4450e5785ac8`
- Source SHA-256: `0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`
- Original reproducibility archive: `10.5281/zenodo.21426465`

## F1 — live Zenodo integrity: passed

The exact public archive was downloaded from the Zenodo API and verified against its deposited checksum. All 61 manifest-listed files passed.

## F2 — frozen-source fidelity: passed

The final circulation source is generated deterministically from the anonymous reviewed Markdown in the Zenodo archive. Only author/date metadata, data availability and AI disclosure are changed. The mathematical body is identical.

## F3 — complete reproducibility suite: passed

The full shipped Python suite and both C++ production drivers completed in a fresh environment with `ALL REQUESTED CHECKS PASSED`.

## F4 — independent finite reconstruction: passed

A separate implementation reproduced the exact character identity, transport formula, second-factorial polynomial, Smith forms, finite-group occupancy, overlap counts, median matrix, covariance law, spectral coefficients, packing identities and multiplier asymptotic.

## F5 — fresh exact-hash hostile review: passed after disposition

`Qwen/Qwen3-14B-AWQ` reviewed the exact final manuscript in job `6a638c45db23d7a7ec1cabd8`, found no fatal or major defect and reported high confidence. Its two minor reservations are resolved by the exact independent validator panels.

## F6 — compiled package integrity: passed

GitHub Actions run `30108438561` built the immutable source and produced artifact `8602624235`, digest `sha256:2ecb9ded8ce3e99d579470d9cfde286c10b5df4c63049a9e5474e1ac4effbdd5`.

Closed sub-gates:

1. direct XeLaTeX PDF build from the exact Markdown — passed;
2. editable A4 DOCX with native Office Math — passed;
3. PDF and DOCX text extraction and claim-boundary checks — passed;
4. A4, embedded-font and zero-missing-glyph checks — passed;
5. DOCX hierarchy and structural checks — passed;
6. page-by-page inspection of 28 PDF and 29 DOCX-render pages — passed;
7. per-file, release-ZIP, Zenodo-package and artifact checksums — passed; and
8. circulation and Zenodo-new-version packages — produced and verified.

Canonical visual-QA binary hashes:

- PDF: `35b505c809afc178ced84060d7c67d04239552d42bff4c9a204cb06612757bd4`;
- DOCX: `05577ce07d092e1b7113c51c470bdaac4ff36eb74df621dc76c4d0452d14e6ae`;
- hardened release ZIP: `c267ee0cdbcc30ddffdb478b866767bb8bdd5141bb36ad657b8ca6b37b68dbb7`;
- Zenodo new-version package: `4d9cd4ca9572e103f36b401da7b58d2ad667b4c5a3fa8f5262ae3995195e3016`.

Any source change reopens F1 through F6.

## F7 — external human review: open

The appropriate external readers are:

- an analytic or combinatorial number theorist able to assess divisor incidence and additive-energy arguments; and
- a matroid/gain-graph or integer-linear-algebra specialist able to assess the interval-specific Smith-form theorem and its novelty boundary.

## Claim boundary

- HTE4 is open.
- HWF4 is open.
- FBHE4 and RQHE4 are open.
- The prime-detection bridge is absent.
- No prime-offset theorem or proof of Fortune's conjecture is claimed.
- Internal technical audit and model review are not peer review.
