# Paper III frozen-source fidelity matrix

## Reviewed manuscript

- Path: `publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md`
- Git blob: `6ff5adb496be657b4d0e761fe8508ab6f458ac56`
- SHA-256: `908eb40bbdfb1e88905d539bf978bbbebabffa874bdae98e0e7547b13b840e5f`

## Frozen basis

| Role | Frozen blob |
|---|---|
| Complete kernel theory and exact finite moments | `71a9ad70c7164bcd94b92743fff3d8088c9a158b` |
| Singular-series local factors, divisor identity and bound | `abe5cbb0577e35bf05db2302de6a7d73afd991bc` |
| Corrected block-averaged conditional theorem | `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef` |

## Reconstruction map

The concise standalone draft remains the main narrative. The complete frozen proof sources are appended so that no load-bearing result depends only on a synopsis.

| Load-bearing component | Frozen basis | Circulation status |
|---|---|---|
| Bounded-coefficient rigidity | Kernel source | Reproduced in main text and Appendix A |
| Exact `N`-or-`1` difference multiplicity | Kernel source | Reproduced with proof |
| Two-scale energy decomposition | Kernel source | Reproduced with proof |
| High-moment upper bound | Kernel source | Reproduced with proof |
| Sub-Weibull tail and range | Kernel source | Reproduced with proof |
| Exact sixth and centred third moments | Kernel source | Reproduced as exact computer-assisted results |
| Exceptional-set transfer corollary | Kernel source | Reproduced with hypotheses |
| Truncated singular-series local factors | Singular-series source | Reproduced in Appendix B |
| Exact divisor identity | Singular-series source | Reproduced with proof |
| Uniform `|T_j(H)| <= 2H log X` input | Singular-series source | Reproduced with proof |
| Dickman constant | Singular-series source | Explicitly labelled non-load-bearing sketch |
| Block-averaged first and pair hypotheses | Conditional source | Reproduced in Appendix C |
| Conditional variance assembly | Conditional source | Reproduced with proof |
| Earlier pointwise Hardy--Littlewood formulation | Superseded | Excluded and identified as vacuously strong |

## Editorial transformations

Appendix numbering was changed only to avoid collisions between the three frozen sources. Mathematical notation and hypotheses were otherwise retained. The sharp Dickman asymptotic is explicitly separated from the proved bound used by the conditional theorem.

## Dependency on Paper II

Paper III imports only the deterministic variance-to-prime-detection criterion from Paper II. It does not import or assume the open reciprocal transference target.

## Current gate

Frozen-source fidelity: **passed editorially**. Correctness of the exact assembled manuscript remains subject to hostile review and compiled-artifact verification.
