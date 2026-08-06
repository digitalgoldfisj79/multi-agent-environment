#!/usr/bin/env python3
"""Check the exact geometric budget used by INT-SOCG."""
from fractions import Fraction
for eps in (Fraction(1,100),Fraction(1,20),Fraction(1,10),Fraction(1,5),Fraction(1,2)):
    assert eps<Fraction(2,3)
    max_tau_d=eps/(1+eps)
    remainder_ratio=max_tau_d/(1-max_tau_d)
    assert remainder_ratio==eps
    retained=(1-eps)*(1+3*eps)
    assert retained>1
    print(f"epsilon={float(eps):.8g} max_tauD={float(max_tau_d):.8g} remainder_ratio={float(remainder_ratio):.8g} retained_log_factor={float(retained):.8g}")
print("FORTUNE_INT_SOCG_C6_GEOMETRIC_BUDGET_PASS")
