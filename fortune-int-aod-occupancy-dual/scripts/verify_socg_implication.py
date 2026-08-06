#!/usr/bin/env python3
"""Exact algebraic budget check for INT-SOCG => stratum occupancy."""

from __future__ import annotations

from fractions import Fraction

# If r=tau*D <= eps/(1+eps), then r/(1-r)<=eps. With
# tau*L=(1+3eps)log(nB) and c1>=L, the retained connected gap is at least
# (1+3eps)(1-eps)log(nB), which exceeds log(nB) for 0<eps<2/3.
for eps in (Fraction(1, 100), Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(1, 2)):
    r = eps / (1 + eps)
    remainder_ratio = r / (1 - r)
    assert remainder_ratio == eps
    retained_factor = (1 + 3 * eps) * (1 - eps)
    assert retained_factor > 1
    print(
        f"epsilon={float(eps):.8g} max_tauD={float(r):.8g} "
        f"remainder_ratio={float(remainder_ratio):.8g} "
        f"retained_log_factor={float(retained_factor):.8g}"
    )

print("FORTUNE_INT_AOD_O5_INT_SOCG_IMPLICATION_PASS")
