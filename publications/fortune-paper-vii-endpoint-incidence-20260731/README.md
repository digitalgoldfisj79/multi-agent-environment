# Fortune Paper VII publication package

**Working title:** *Bilateral Endpoint Incidences over Finite Fields: Defect Rigidity, Frobenius Orientation, and Quadratic Emptiness*

This package consolidates the stable endpoint-incidence theorem sequence and freezes the proof-search boundary before further cubic work.

The canonical manuscript source is stored as four ordered files under `manuscript_parts/` and is assembled deterministically with:

```sh
cat manuscript_parts/*.md > manuscript.md
```

The canonical assembled SHA-256 is:

```text
4c95d04b5c055dd4e97b0bdc75db8ed50c61ff2c2cbf23009f830ca25484819b
```

`paper7_verify.py` and the dedicated build workflow enforce that hash before running the symbolic audit, exact Singular certificates and publication build.

Required release files include the manuscript parts, references, Paper VI lineage audit, claim and source-fidelity ledgers, exact certificates, independent-review records, build status, source manifest, release checklist and metadata.

**FROZEN INTERNAL THEOREM PACKAGE — EXACT CERTIFICATES, FRESH-CHECKOUT BUILD AND CANONICAL HOSTILE REVIEW PASSED; HUMAN SPECIALIST REVIEW OPEN**

The paper does not claim the function-field crown, endpoint `FFPR`, the cubic twisted-Frobenius theorem or Fortune's conjecture.