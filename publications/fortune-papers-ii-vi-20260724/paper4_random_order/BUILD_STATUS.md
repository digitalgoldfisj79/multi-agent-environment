# Paper IV build status

## Current gate

**Internal technical pass; external human specialist review open.**

The reviewed source, mathematical audit, independent ledger reconstruction, manuscript-only hostile review and compiled-artifact QA are complete. This status is not human peer review or publication acceptance.

## Reviewed source

- Git blob: `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`.
- SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`.

## Canonical build

- GitHub Actions workflow: `Build Paper IV release artifacts`.
- Run: `30085400790`.
- Publication commit: `af9350f06e41e94d79f583b2e8fca45b55b92852`.
- Artifact ID: `8593522378`.
- Artifact digest: `sha256:1875d3965d611cffa0a70afc223caf0e3119d93f79183f3f7a9be214f3486a51`.
- Workflow result: passed.

## Canonical hashes

- PDF: `dc5ff454826f605d5fd4db4ba02f6a35df1013bde1cfe9a9d9e26a6c8fc6f1a3`.
- DOCX: `3ecac48465573b9305cafb119779a5e17c65b2bd2fc05f7d376ec55895b3b61b`.
- Internal release ZIP: `19c790caa196cf6374f62f90e4d9da4ea2dfc559a4894fd8e7dfdb4a62b5ec43`.

The PDF is generated directly from the reviewed source using XeLaTeX. The editable DOCX applies only the notation-preserving conversions documented in `TYPESETTING_NORMALISATIONS.md` inside the release package.

## QA result

- DOCX and PDF extraction checks: passed.
- PDF preflight: passed; 12 pages, unencrypted, text-native, no XFA or warnings.
- DOCX accessibility: zero findings.
- Page-by-page visual inspection: passed for 12 PDF pages and 15 rendered DOCX pages.
- Per-file and archive checksums: passed.

The audit-branch record is `fortune-conjecture/random-order-flagship-20260724/COMPILED_ARTIFACT_QA.md`.
