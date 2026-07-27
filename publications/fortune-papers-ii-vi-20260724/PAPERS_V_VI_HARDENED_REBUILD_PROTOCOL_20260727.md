# Replacement Papers V and VI: hardened publication protocol

**Date:** 2026-07-27  
**Branch:** `publication/fortune-papers-ii-vi-20260724`  
**Status:** controlling protocol for the complete replacement of Papers V and VI.

## 0. Governing decision

The existing Paper V and Paper VI manuscripts are superseded working drafts. They are retained for provenance only and must not be line-edited into release candidates.

Replacement Paper V must continue explicitly from Papers III and IV. Replacement Paper VI must take the frozen notation and exact crown reduction from replacement Paper V and continue to the current secondary-trace/Kummer-quotient frontier.

No manuscript may be described as final, submission-ready or proved merely because it compiles or passes model review. The highest pre-human-review status is **INTERNAL TECHNICAL PASS — HUMAN SPECIALIST REVIEW OPEN**.

Any source change after a freeze invalidates all downstream hashes, hostile reviews, compiled artefacts and release manifests.

## 1. Clean-room source intake

For each paper:

1. Create a new manuscript directory; do not overwrite the superseded draft.
2. Record every frozen source file, branch, commit, Git blob and SHA-256 used to support the manuscript.
3. Separate sources into:
   - proved mathematical sources;
   - exact computer-assisted certificates;
   - published external theorems;
   - empirical evidence;
   - heuristics;
   - open claims and failed routes.
4. Build a claim-source matrix before drafting prose.
5. Exclude any result whose latest hostile audit retracted, narrowed or renormalised it.

Paper V sources must include the exact normal-form, sparse-surface, hook-projector and q-line ledgers. Paper VI sources must include the fixed Cartier moment, cyclotomic tangent, divided-hook obstruction, Hattori--Stallings trace, Artin--Schreier quotient, no-split theorem, Kummer correction and projective quotient count.

## 2. Series-continuity gate

Before mathematical drafting:

1. Write the exact dependency map from Papers III and IV into Paper V.
2. State why the function-field problem is a controlled laboratory after the integer derandomisation wall.
3. State explicitly that the function-field results do not imply the integer Fortune conjecture.
4. Freeze Paper V's notation and theorem numbering before Paper VI is finalised.
5. Paper VI must cite and reuse Paper V's definitions of `N_2`, `N_+`, `N_-` and
   \[
   W_p=N_2+\frac{N_++N_-}{2}.
   \]

A reader must not have to infer the bridge between Papers III--IV and V, or between V and VI.

## 3. Claim-status and theorem audit

Every displayed claim must appear in a live claim-status ledger with one of the following labels:

- **PROVED**;
- **PUBLISHED INPUT**;
- **EXACT COMPUTER-ASSISTED THEOREM**;
- **CONDITIONAL THEOREM**;
- **EMPIRICAL EVIDENCE**;
- **HEURISTIC**;
- **OPEN**;
- **CLOSED/REFUTED ROUTE**.

For every theorem labelled PROVED:

1. identify the complete proof source;
2. reconstruct the proof in manuscript notation;
3. audit sign, normalisation, Tate twist, Frobenius convention, boundary terms and exceptional primes;
4. ensure the theorem statement is no stronger than the audited source;
5. record dependencies and any machine-checkable subclaims.

For every exact computation:

1. freeze the code and input data;
2. provide an independent implementation or independent mathematical reconstruction;
3. record environment, command, output and checksums;
4. state clearly that finite verification is not a uniform theorem.

## 4. Independent reconstruction gate

The first four papers did not rely on authorial restatement alone. The replacement papers must likewise receive independent reconstruction of their load-bearing ledgers.

Paper V minimum reconstruction targets:

- affine-orbit and normal-form decomposition;
- exact crown formula and failure certificate;
- smooth sparse-surface Jacobian argument;
- alternating-hook `p`-cycle projector;
- fixed-point and q-line saturation identities.

Paper VI minimum reconstruction targets:

- Cartier cofactor/first-moment identities;
- cyclotomic tangent and precision ledger;
- nonexistence of the ordinary divided-hook character;
- Hattori--Stallings coefficient extraction;
- cyclic transfer and Artin--Schreier coordinate;
- no-split logarithmic-derivative theorem;
- Kummer cocycle classification;
- projective quotient point-count formula.

Independent reconstruction must be committed separately from the prose manuscript and must be reproducible from documented commands.

## 5. Manuscript construction gate

Only audited claims may enter the manuscript.

Each replacement manuscript must be self-contained at theorem level, not a condensed research diary. It must include:

- a precise abstract with no unproved implication;
- a theorem inventory in the introduction;
- full proofs or explicit, correctly scoped citations to prior papers in the series;
- a section separating proved, computed, conditional and open conclusions;
- a reproducibility section;
- an AI-assistance disclosure;
- a terminal boundary statement that does not imply the Fortune crown is proved.

Paper V must terminate at the semisimple/projector/q-line wall. Paper VI must terminate at the genuinely one-sided Frobenius/nonvanishing theorem.

The superseded Airy manuscript is not Paper VI. It may later become a separately audited technical companion.

## 6. Frozen-source fidelity gate

Once a complete manuscript draft exists:

1. freeze its Git blob and SHA-256;
2. create a line-by-line theorem/source fidelity matrix;
3. verify every theorem, equation, numerical table and scope statement against the frozen sources;
4. run searches for `TODO`, `TBD`, placeholders, malformed Unicode, unsupported glyphs and broken cross-references;
5. record manuscript line count, byte count and exact hash.

No hostile review or canonical build begins before this gate closes.

## 7. Manuscript-only hostile review gate

Each frozen manuscript must be reviewed as a standalone document by a third-party model with no access to the internal programme narrative except the manuscript and declared supplements.

Required review outputs:

1. raw prompt and raw response;
2. theorem-by-theorem verdict;
3. identification of hidden assumptions, circular reductions, missing boundary terms, sign/normalisation defects and unsupported novelty claims;
4. line-by-line disposition document;
5. explicit final verdict: proved as stated, conditionally correct, major revision, or failed.

Reviewer pools must be distinct:

- Paper V: finite fields, algebraic geometry, prescribed coefficients and representation-theoretic point counting;
- Paper VI: arithmetic geometry, modular representation theory, integral trace theory, Artin--Schreier/Kummer quotients and wild singularities.

Any substantive amendment creates a new frozen source hash and requires a fresh hostile review.

## 8. Specialist human-review gate

After internal technical pass, the remaining gate is external human review.

Paper V should be reviewed by at least:

- a finite-field/algebraic-geometer specialist;
- an analytic or arithmetic number theorist familiar with irreducible polynomials in coefficient slices.

Paper VI should be reviewed by at least:

- an arithmetic geometer familiar with wild quotient singularities and Artin--Schreier/Kummer descent;
- a representation/cohomology specialist familiar with Hattori--Stallings traces or modular cyclic actions.

Human-review changes reset all downstream gates.

## 9. Canonical build gate

Build directly from the exact reviewed source through a reproducible GitHub Actions workflow.

Required artefacts for each paper:

- reviewed Markdown source;
- LaTeX source;
- text-native A4 PDF built with XeLaTeX;
- editable A4 DOCX;
- references file;
- claim-status ledger;
- source-fidelity matrix;
- source manifest;
- supporting-materials manifest;
- raw hostile review and disposition;
- machine-verification scripts and frozen outputs;
- `CITATION.cff`;
- Zenodo metadata JSON;
- checksums;
- internal release ZIP.

DOCX conversions must be notation-preserving and documented. Silent rewriting during typesetting is prohibited.

## 10. Compiled-artifact QA gate

For every canonical build:

1. extract text independently from PDF and DOCX and compare mathematical content with the reviewed source;
2. run PDF preflight: A4, text-native, unencrypted, embedded fonts, no XFA, no malformed objects or warnings;
3. run DOCX accessibility, heading, equation and metadata audits;
4. render the DOCX independently;
5. inspect every page of the PDF and rendered DOCX;
6. inspect equations, tables, page breaks, headers, references, footnotes, glyphs and hyperlinks;
7. archive the page-level QA record;
8. generate per-file SHA-256 hashes and an archive manifest;
9. download the workflow artefact and re-verify every checksum.

A successful compiler exit is not a visual or semantic pass.

## 11. Release and Zenodo gate

No Zenodo publication occurs merely on internal technical pass.

Prepare upload-ready packages containing all required sources, binaries, code, outputs, manifests and checksums. Metadata must preserve:

- author: Edward Stewart Anthony Bozzard;
- ORCID: `0009-0002-4052-0994`;
- exact paper title and version;
- relation to the preceding paper in the series;
- explicit statement that the function-field crown remains open;
- licence, keywords and repository commit.

After human review is disposed, decide whether each replacement paper receives a new Zenodo record or supersedes a prior unpublished draft package. Do not overwrite an already deposited record without a byte-for-byte and claim-for-claim version decision.

## 12. Execution order

1. Freeze and inventory the complete Paper V proof sources.
2. Build and independently audit replacement Paper V.
3. Freeze Paper V notation and theorem references.
4. Freeze and inventory the complete Paper VI proof sources.
5. Build and independently audit replacement Paper VI.
6. Run separate hostile reviews.
7. Resolve findings and refreeze sources.
8. Build canonical PDF/DOCX/release packages.
9. Perform full binary and visual QA.
10. Mark each paper **INTERNAL TECHNICAL PASS — HUMAN SPECIALIST REVIEW OPEN** only after every internal gate passes.

## 13. Non-negotiable reset rule

A change to any reviewed manuscript source after its hash is frozen requires:

- a new source SHA-256;
- an updated fidelity matrix and claim ledger;
- rerun independent checks affected by the change;
- a fresh manuscript-only hostile review;
- a complete rebuild;
- renewed PDF/DOCX extraction, preflight, accessibility and page-by-page QA;
- regenerated manifests, checksums and release ZIP.

There are no editorial exceptions to this rule.
