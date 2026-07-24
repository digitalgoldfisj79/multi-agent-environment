# Random-order flagship audit package

This directory records an adversarial audit of the combined random-order integer sequel. The audit edited and reconstructed manuscript material; it is therefore not independent authorship validation and must not be treated as such.

## Current gate

**Internal hold.** The frozen RQM proof source and the selected finite checks remain substantive, but the exact circulation manuscript has not yet passed:

1. a frozen-source-to-manuscript fidelity audit; and
2. a fresh, context-free hostile review of the manuscript alone.

Do not send the manuscript to a specialist, submit it to a journal, or publish it as a final Zenodo preprint until both gates are closed.

## Core result under audit

For a uniformly random ordering of the primes in `[X,2X)`, form the nested prime-prefix products and all unordered pair sums. The frozen source claims that, for the reciprocal Fourier frame with prime moduli of size `X^2`,

`E_sigma E_a <= C M (log X)^9`

uniformly in the natural harmonic range, together with weighted aggregate and Frobenius-energy bounds, under a quantitative frame-admissibility hypothesis.

The result uses no GRH, but its cancellation comes from expectation over a uniformly random ordering. It does not cover the increasing primorial order and does not prove Fortune's conjecture.

## Files

- `AUDIT_REPORT.md`: revised correctness gate, scope of the clean-room checks, and no-cushion warning.
- `FIDELITY_AND_EXTERNAL_REVIEW_GATES.md`: mandatory internal gates and initial source/manuscript findings.
- `FRESH_HOSTILE_REVIEW_PROMPT.md`: fixed prompt for a manuscript-only review in a clean session.
- `NOVELTY_AUDIT.md`: theorem-specific literature comparison.
- `PROOF_DEPENDENCY_GRAPH.md`: load-bearing proof structure.
- `EXTERNAL_REVIEW_MEMO.md`: compact specialist brief with provenance disclosure.
- `CLAIM_STATUS.md`: source-versus-manuscript epistemic ledger.
- `QUALITY_ASSURANCE.md`: canonical package-integrity and verification-artifact record.
- `independent_audit_results.json`: clean-room finite results.

## Package integrity

The canonical machine-readable result file is `independent_audit_results.json`. Any generated archive that references `independent_audit_results.txt` must either include that text export or remove the reference. Binary PDF/DOCX/ZIP artifacts are not considered cleared merely because the repository Markdown has been corrected; their hashes and contents must be revalidated after regeneration.

## Consultation sequence

RQM should lead the external consultation sequence after its internal gates close. The Airy package should be held back from the same small specialist pool until the RQM consultation has been completed or clearly routed elsewhere.
