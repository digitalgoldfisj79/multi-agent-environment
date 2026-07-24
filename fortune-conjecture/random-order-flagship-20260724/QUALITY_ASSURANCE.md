# Quality assurance and package integrity

## Canonical branch artifacts

The canonical clean-room result artifact in this branch is:

- `independent_audit_results.json`

No file named `independent_audit_results.txt` is currently canonical. A generated package must not reference that filename unless a text export is generated and included in the same archive.

## Scope of the result artifact

`independent_audit_results.json` records finite exact or numerical checks of selected identities and exponent calculations. Its `PASS` status means that those declared checks completed successfully. It does not certify:

- the completeness of the circulation manuscript;
- fidelity to frozen proof blobs;
- exhaustiveness of the configuration classification;
- novelty;
- asymptotic correctness beyond the proved reductions; or
- suitability for journal submission.

## Required pre-circulation QA

Before any package is sent externally:

1. close the fidelity and fresh-review gates in `FIDELITY_AND_EXTERNAL_REVIEW_GATES.md`;
2. regenerate the manuscript PDF and DOCX from the cleared source;
3. extract text from both binaries and compare all theorem statements, hypotheses, displayed formulae, section ordering, and caveats with the cleared source;
4. regenerate the archive manifest from the actual files included;
5. verify that every filename referenced by `README`, review memo, metadata, and QA documents exists exactly once in the archive;
6. compute SHA-256 hashes for the source, PDF, DOCX, review memo, validation code, result JSON, and ZIP;
7. run the validator from a clean environment against the exact archived inputs; and
8. record the validator command, dependency versions, exit status, and unedited output.

## Gate status at this revision

- Frozen-source proof audit: substantive but authored within the same LLM-assisted programme.
- Finite clean-room checks: passed for the declared cases.
- Manuscript fidelity: open.
- Fresh manuscript-only hostile review: open until a successful archived run exists.
- Human specialist review: not started.
- Journal submission or final Zenodo release: not cleared.

## Failure rule

Any missing referenced file, hash mismatch, binary/source discrepancy, stale gate statement, or unarchived manuscript edit reopens package integrity and blocks circulation.
