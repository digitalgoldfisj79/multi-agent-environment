# Papers V--VI final compiled-artifact QA

## Disposition

**INTERNAL TECHNICAL PASS — HUMAN SPECIALIST REVIEW OPEN**

This is an internal source, proof-reconstruction, exact-text referee, build and compiled-artifact pass. It is not peer review, journal acceptance or a proof of either Fortune conjecture.

## Frozen mathematical sources

### Paper V

- title: *Fortunate Polynomials over Finite Fields*;
- reviewed source commit: `4869f63e72f4e17078fa3e43fc18e60fcd6ff8ac`;
- manuscript Git blob: `89794e9337eaf328dfb13a627b9616a1e3a9553c`;
- manuscript SHA-256: `2a7df97840babfd4f92007f0fcdc70fe67faada264019cb3f396c1d05237c965`;
- final referee job: `6a6708d47ef3c0846496a42b`;
- final referee verdict: **PROVED AS STATED**.

### Paper VI

- title: *Secondary Traces and Kummer Quotients for the Function-Field Fortune Crown*;
- reviewed source commit: `f8dda702141e85a07d0a20d08ed543bad6c6f270`;
- manuscript Git blob: `6e42cce0331dcf6b532d2c88819303f858ae4fd9`;
- manuscript SHA-256: `12879f46044fa3cc598ebe60c9419b78d8d32cfeb518dbad5a5d8d4589eb88dd`;
- final referee job: `6a671d607ef3c0846496a4d1`;
- final referee verdict: **PROVED AS STATED**.

No mathematical source edit was made during compiled-artifact repair. The build-only normalisations are recorded in each paper's `TYPESETTING_NORMALISATIONS.md`.

## Final canonical build

- GitHub Actions run: `30269702452`;
- source commit: `8d8980ca3f9ca4231111b799ea127a672ee6a1a2`;
- workflow conclusion: **success**;
- artifact ID: `8654346156`;
- artifact name: `fortune-papers-v-vi-internal-release-final`;
- GitHub artifact digest: `sha256:53ddbf83dbdf608959e142be2997ce86ab28a01f35b9a6e33b913b1c7eca7875`;
- independently downloaded outer ZIP SHA-256: `53ddbf83dbdf608959e142be2997ce86ab28a01f35b9a6e33b913b1c7eca7875`;
- inner release ZIP SHA-256: `f808a617a3765632f808d128ce2c8db25648def9e19173c335048eca43f63357`;
- every entry in the packaged `SHA256SUMS` manifest: **verified**.

## Canonical file hashes

### Paper V

- PDF: `66abf33168a9d5e52ac4a1897155aba2ba71a9ce28f949584b8e4d6f843dc77b`;
- DOCX: `9766b48416b03de61b4edade59928fcd3dd45072a859186e64fa20f846ef6207`;
- LaTeX: `df209365198a829fdced7f4dfa2f1250958fdc5603ed2fa986fe60c237854c97`.

### Paper VI

- PDF: `b7e13fd033b6b845bdaa5c403fc5831f7ed253eba6dc115adc0c924e139567a5`;
- DOCX: `3463210ec1d4f035417896e3b02fcafc6d59ab24b11675f250028f99e538e275`;
- LaTeX: `e029ec6dc439498b11aec120792cc3d230a17fbf87d317a4f1eff084a8bc91e2`.

## Automated compiled-artifact gates

All final-run steps passed:

- exact-hash review-gate verification;
- independent mathematical reconstruction scripts and the independent Paper V C++ singular-locus verifier;
- frozen-source hygiene and placeholder checks;
- canonical XeLaTeX A4 PDF, editable-prose DOCX and LaTeX generation;
- PDF `qpdf` integrity, A4 dimensions and embedded-font audit;
- DOCX A4, heading, author/title metadata and package-structure audit;
- exact equation-image counts and exact TeX alternative text;
- independent LibreOffice DOCX-to-PDF rendering;
- rendered end-marker, source-token leakage, blank-page and page-edge checks;
- complete checksum verification and artifact upload.

DOCX equation package:

- Paper V: 359 equation occurrences, 359 exact-TeX alternative texts and 273 unique PNG resources;
- Paper VI: 394 equation occurrences, 394 exact-TeX alternative texts and 272 unique PNG resources;
- no residual OMML objects were accepted because manual QA demonstrated that LibreOffice could silently omit otherwise valid inline OMML;
- prose, headings, citations and lists remain editable; the canonical reviewed Markdown and LaTeX/PDF remain the authoritative mathematical source.

## Manual page-level visual QA

The exact downloaded final artifact was rasterised at 150 dpi and inspected page by page:

- Paper V canonical PDF: 11 pages;
- Paper V independent DOCX render: 16 pages;
- Paper VI canonical PDF: 12 pages;
- Paper VI independent DOCX render: 17 pages;
- total inspected: **56 pages**.

Finding: **no defect**.

Specifically, no page showed a missing inline or display equation, broken glyph box, literal TeX or Markdown leakage, duplicate or blank page, clipped formula, content outside the A4 printable area, broken theorem/proof boundary, or reference overflow. Office-specific line and page wrapping differs from the canonical PDFs but the mathematical content and ordering are intact.

## Open external gates

- human finite-field/algebraic-geometry and prescribed-coefficient review of Paper V;
- human arithmetic-geometry/wild-quotient and integral-trace/modular-representation review of Paper VI;
- disposition of any human findings;
- final Zenodo/versioning decision.

Paper V reduces the function-field crown to the exact nonnegative count `W_p>0`; Paper VI constructs the integral and quotient carriers and isolates the remaining one-sided Frobenius/rational-point theorem. The function-field crown remains open. No implication to the integer Fortune conjecture is claimed.
