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
| 23 | 43932462742641 = 3·11·17·23⁸ | +1.0605     | −23.3           |
| 29 | 27522246495265849219 = 65419·29¹⁰ | +2.6823 | −75.1           |

**Correction:** an earlier version printed `23^7` in the p=23 factorization. The exact exponent is `23^8`.

## Findings

1. **Constancy: CONFIRMED** (the entire nonzero-fibre nonuniformity for
   p ≡ 2 mod 3 is one number per prime, exactly as WTCK.4 predicts).
2. **No closed form / no fixed ledger line.** The constants have
   oscillating signs and normalized values −2, −1.71, +1.06, +2.68.
   The value −2.0000 at p=11 is exactly extremal for a single weight-3
   Frobenius pair, while +2.68 at p=29 exceeds 2, so the constant sector
   is not a single eigenvalue pair.
3. **New p-adic pattern, verified later through p=53.** With
   `T_p=-pD_b`, every nonzero calibrated value satisfies

   \[
   v_p(T_p)=\frac{p+4}{3},
   \qquad
   v_p(D_b)=\frac{p+1}{3}.
   \]

   This is evidence for a Dwork-boundary divisibility theorem, not a
   proof and not an archimedean estimate.
4. **Consequence — the earlier assessment was too optimistic.** A
   genuine estimate remains: prove a uniform absolute bound for
   `|D_{b≠0}|/p^{(p−3)/2}`.
5. **The punctual b=0 term** is now known from the collapse lemma to be
   exactly `-(p-1)D_b` numerically. The categorical nearby-cycle ledger
   still has to verify that this identity supplies the required
   subtraction in the original application.

## Verdict

The half-theorem does **not** close for free, but the probe replaces a
vague hope with a precise, minimal target: prove one uniform weight-3
bound for a single constant, per prime p ≡ 2 mod 3.

Boundary as always: FF sibling only; integer Fortune untouched.
