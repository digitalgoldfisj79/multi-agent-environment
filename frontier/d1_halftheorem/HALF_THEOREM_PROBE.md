# Half-theorem probe: the p ≡ 2 (mod 3) sector of the wild cubic trace

**Date:** 2026-07-23. **Scope:** lean inline probe (no agent fan-out).
**Target:** test whether the FF d=1 crown for p ≡ 2 mod 3 closes with
"bookkeeping only" (steps 1 and 4 of the WTCK phase plan), as my
completion of the phase analysis suggested it might.

## Independent confirmation of the WTCK computational layer

`halftheorem_probe.py` reimplements WTCK §5 from scratch (exact
Z[ζ_p] arithmetic, degree-two L-function recurrence, fields of size p
and p² only) and **exactly reproduces** the committed examples:
p=5 all-zero; p=7 normalized deviations {12; −1, −7, 2}; p=11
{20; −2}. Cube-class constancy (WTCK.4) verified for all p ≤ 29 with
zero violations. New exact values computed at p = 13, 19, 23, 29.

## New data: the p ≡ 2 (mod 3) constant sector

For p ≡ 2 mod 3 all nonzero-fibre deviations D_b (b ≠ 0) are equal
(confirmed exactly through p = 29). The constant, two normalizations:

| p  | D_{b≠0} (raw)              | D/p^{(p−3)/2} | D_0/p^{(p−3)/2} |
|----|----------------------------|---------------|-----------------|
| 5  | 0                          | 0             | 0               |
| 11 | −29282 = −2·11⁴            | **−2.0000**   | +20.0           |
| 17 | −699989501 = −29·17⁶       | −1.7059       | +27.3           |
| 23 | 43932462742641 = 3·11·17·23⁷ | +1.0605     | −23.3           |
| 29 | 27522246495265849219 = 65419·29¹⁰ | +2.6823 | −75.1           |

## Findings

1. **Constancy: CONFIRMED** (the entire nonzero-fibre nonuniformity for
   p ≡ 2 mod 3 is one number per prime, exactly as WTCK.4 predicts).
2. **No closed form / no fixed ledger line.** The constants have
   *irregular* p-adic structure (integral in units p^{(p−7)/2} through
   p=23, non-integral at p=29), oscillating sign, and normalized values
   −2, −1.71, +1.06, +2.68. The value −2.0000 at p=11 is *exactly
   extremal* for a single weight-3 Frobenius pair (|2cos θ| ≤ 2), while
   +2.68 at p=29 **exceeds 2** — so the constant sector is not a single
   eigenvalue pair; it behaves like a trace of Frobenius on a sector of
   rank ≈ 2 (bound 4), with no match to any fixed small motive visible
   in four data points.
3. **Consequence — my earlier assessment was too optimistic.** The
   phase plan's step 1 ("identify and subtract the constant line
   already present in the main/Tate or Artin–Schreier ledger") is *not*
   mere bookkeeping: the data shows no fixed ledger line to subtract.
   Even in the p ≡ 2 mod 3 sector a genuine estimate remains — namely a
   **uniform absolute bound for the normalized constant**
   |D_{b≠0}|/p^{(p−3)/2} ≤ C (empirically C ≤ 2.7 through 29;
   conjecturally C = 4 from the rank-2 profile). The good news: for
   half of all primes the *entire* remaining analytic content is this
   single bounded-rank constant — still strictly smaller than the
   p ≡ 1 mod 3 problem (constant + two cubic-character coefficients).
4. **The punctual b=0 term** grows and oscillates (+20, +27, −23, −75
   normalized), confirming the phase report's warning that it must be
   separated from the nearby fibre (step 4) — that separation is also
   still genuine work, not bookkeeping.

## Verdict

The half-theorem does **not** close for free, but the probe replaces a
vague hope with a precise, minimal target: *prove one uniform weight-3
bound for a single constant of apparent rank ≤ 2, per prime
p ≡ 2 mod 3.* That is now the cheapest well-posed route to the first
infinite Fortune-type theorem. By-product: exact deviation tables at
p = 13, 19 for the p ≡ 1 mod 3 sector are in the script output.

Boundary as always: FF sibling only; integer Fortune untouched.
