# Paper III frozen-source fidelity matrix

## Reviewed manuscript

- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Path: `publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md`
- Git blob: `06fe9116d42fd056bf9727dfbaa63ccb7398562d`
- SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`

## Frozen basis

| Role | Frozen blob |
|---|---|
| Complete kernel theory and exact finite moments | `71a9ad70c7164bcd94b92743fff3d8088c9a158b` |
| Singular-series local factors, divisor identity and bound | `abe5cbb0577e35bf05db2302de6a7d73afd991bc` |
| Corrected block-averaged conditional theorem | `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef` |

The concise standalone paper remains the main narrative. The complete frozen proof sources are appended so that no load-bearing theorem rests only on a synopsis.

## Load-bearing map

| Component | Classification |
|---|---|
| Bounded-coefficient rigidity | Reproduced with proof |
| Exact `N`-or-`1` difference multiplicity, including repeated endpoints | Reproduced with proof |
| Two-scale energy decomposition | Reproduced with proof |
| High-moment upper bound | Reproduced with proof |
| Sub-Weibull tail and full stated range | Reproduced with proof |
| Fixed-level limiting moment law | Reproduced with argument |
| Exact sixth and centred third moments | Exact computer-assisted theorems, with degree bound and validators |
| Exceptional-set transfer corollary | Reproduced with its atom-count and atom-mass conditions |
| Truncated singular-series local factors | Rewritten in publication notation from the frozen proof |
| Exact divisor identity | Rewritten with a continuous proof and exact rational checks |
| Uniform `|T_j(H)| <= 2H log X` input | Reproduced with full cancellation, tail, error and beta estimates |
| Sign of `T_j(H)` | Not claimed; the unsupported frozen-source inference was removed |
| Dickman constant | Explicitly non-load-bearing sketch with standard references |
| Infinite Euler-product tail beyond the truncation | Unsupported claim removed; not used |
| Block-averaged first and pair hypotheses | Reproduced as assumptions |
| Conditional variance assembly | Reproduced with proof |
| Earlier pointwise Hardy--Littlewood formulation | Excluded as vacuously strong |

## Final source repairs

The initial assembled manuscript retained an orphan sentence claiming that the omitted infinite Euler-product tail was `1+O(1/X)` and citing a later lemma that had not been included. The conditional theorem uses only the finite truncated singular series, so the unsupported and unused claim was removed.

Page-level QA then exposed that Appendix B still used machine-write-up pseudo-code rather than publication mathematics. Appendix B was rebuilt line by line from the same frozen proof, with proper definitions of `A_j`, `C_j`, `varphi_2`, the local factors, the exact finite Euler expansion, `W_H`, the divisor identity, the cancellation identity, the tail estimate, the `E_H` estimate and the beta bound.

The frozen machine write-up also inferred `T_j(H)<0` from `T_j(H)=-beta_j(H)H+O(H)` without controlling the absolute error constant. That sign statement was unsupported and unnecessary. It was removed. The proved absolute estimate used by the conditional theorem is preserved.

Finally, one unsupported set-difference glyph was replaced by equivalent prose, and the final Appendix B subscript and convolution notation were normalised. These last changes are typesetting-only.

## Dependency on Paper II

Paper III imports the deterministic variance-to-prime-detection criterion from Paper II. It does not import or assume the open reciprocal transference target. The Hardy--Littlewood conclusion is explicitly conditional on its two block-averaged hypotheses.

## Gate result

Frozen-source fidelity and claim-status audit: **passed**.

This does not constitute external peer review. The block-averaged Hardy--Littlewood hypotheses and the exceptional-set transference theorem remain open.
