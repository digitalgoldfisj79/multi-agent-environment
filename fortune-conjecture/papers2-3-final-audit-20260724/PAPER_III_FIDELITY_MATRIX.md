# Paper III frozen-source fidelity matrix

## Reviewed manuscript

- Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`
- Path: `publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md`
- Git blob: `05463cd60819598045ad41658d6bfd491e572691`
- SHA-256: `1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb`

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
| Exceptional-set transfer corollary | Reproduced with atom-mass hypothesis |
| Truncated singular-series local factors | Reproduced in Appendix B |
| Exact divisor identity | Reproduced with proof |
| Uniform `|T_j(H)| <= 2H log X` input | Reproduced with proof |
| Dickman constant | Explicitly non-load-bearing sketch with standard references |
| Infinite Euler-product tail beyond the truncation | Unsupported claim removed; not used |
| Block-averaged first and pair hypotheses | Reproduced as assumptions |
| Conditional variance assembly | Reproduced with proof |
| Earlier pointwise Hardy--Littlewood formulation | Excluded as vacuously strong |

## Final source repairs

The first assembled manuscript retained an orphan sentence claiming that the omitted infinite Euler-product tail was `1+O(1/X)` and citing a later lemma that had not been included. The conditional theorem uses only the finite truncated singular series, so the unsupported and unused claim was removed rather than reconstructed speculatively. A following non-load-bearing heuristic paragraph was also removed. No proved theorem or hypothesis changed.

The final immutable object adds the author's ORCID and a short bibliography for the companion Paper II, Hardy--Littlewood pair heuristics, de Bruijn smooth-number theory and Tenenbaum's reference text. Those additions are editorial only.

## Dependency on Paper II

Paper III imports the deterministic variance-to-prime-detection criterion from Paper II. It does not import or assume the open reciprocal transference target. The Hardy--Littlewood conclusion is explicitly conditional on its two block-averaged hypotheses.

## Gate result

Frozen-source fidelity and claim-status audit: **passed**.

This does not constitute external peer review. The block-averaged Hardy--Littlewood hypotheses remain open.
