# Exact finite Delta panel on the primorial-resonant component

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Programme:** `FERP-0.1`, Gate 3

## Result

For the characteristic-three resonant family from `FF_PRIMORIAL_RESONANT_COMPONENT_20260730.md`, define for an ordered prime pair `a=(P,S)`

`X_a=Ahat_P(mu_PS) Ahat_S(nu_SP)`,

`B_a=X_a-Delta_PS`.

Let `b=(P',S')` be its partner under

`P'=LQ-P`, `S'=LQ-S`, with `L=t^3-t`.

Exact cyclotomic computation for every resonant prime point at `k=3,4,5`, source degree `m=2k-1`, and scalar `theta=1` gives

`X_a=X_b`,

`Delta_a=Delta_b`,

`B_a=B_b`.

Consequently the literal corrected cross term is

`B_a conjugate(B_b)=|B_a|^2 >= 0`.

Thus `Delta_PS` does not cancel the resonant involution on these panels. It changes the amplitude substantially but preserves the coherent pairing.

This is an **EMPIRICAL-EXACT FINITE PANEL** result. It is not promoted to a theorem for general `k`.

## Exact aggregate decomposition

Summing over all resonant ordered pair-of-pairs gives:

| `k` | rows | `XX` | `-XD` | `-DX` | `DD` | corrected `BB` | `BB / 3^(2m+3k)` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 1,062,882 | 214,326 | 214,326 | 43,218 | 1,534,752 | 0.00132049 |
| 4 | 12 | 71,384,652 | 55,931,148 | 55,931,148 | 43,823,052 | 227,070,000 | 0.0000893320 |
| 5 | 72 | 308,039,038,452 | 92,518,064,244 | 92,518,064,244 | 35,233,974,972 | 528,309,141,912 | 0.0000950357 |

Here

`BB=XX-XD-DX+DD`.

All displayed values are exact rational cyclotomic totals in `Z[zeta_3]`; the nonconstant cyclotomic coordinates vanish identically.

## Interpretation

The resonant component is not removed by transpose, Galois, affine or `Delta` pairing in the audited range. It behaves as a coherent positive component of the corrected pair-of-pairs expansion.

The finite ratios are small, consistent with the parameter-dimension saving proved for the raw Gram incidence. They do not prove an asymptotic bound for `B_a`, because such a bound would require uniform control of the special local prime transforms at fixed field size and growing conductor.

Accordingly:

- the component must be retained explicitly in the centered bilateral identity;
- it need not be assigned an additional oscillatory cancellation mechanism on the evidence available;
- the remaining theorem is to bound its corrected amplitude uniformly, or show that the final centered identity attaches a stronger coefficient than the literal pair cross term computed here.

## Verification

Verifier:

`fortune-review/scripts/ff_primorial_resonant_delta_panel.py`

Frozen output:

`fortune-review/data/ff_primorial_resonant_delta_panel.json`

The verifier independently reconstructs `Ahat`, `Delta_PS`, the corrected pair value and every cross term. No floating-point arithmetic enters the exact totals.

## Status

### EMPIRICAL-EXACT FINITE PANEL

- involution invariance of `X`, `Delta` and `B` through `k=5`;
- positivity and the displayed exact aggregate totals.

### PROVED EXACTLY ELSEWHERE

- the resonant incidence construction and constant completion numerators;
- the raw Gram parameter-dimension bound.

### OPEN

- a general proof of involution invariance for `X` and `Delta`;
- a fixed-`q`, growing-`k` bound for the corrected amplitudes;
- insertion of this component into `CBI_FF`;
- complete bilateral component classification and endpoint `FFPR`.
