#!/usr/bin/env python3
"""Scale regression for the selected-centre weighted mean reduction."""
from __future__ import annotations
import math
for X in (32,64,128,256,512,1024,4096,16384):
    H=0.5*X*X
    A=max(2,int(X/math.log(2)))
    harmonic=sum(1/a for a in range(2,A+1))
    proper_power_cap=math.log(H)*X*harmonic
    target=X*X*math.log(X)
    ratio=proper_power_cap/target
    assert ratio>0
    if X>=128:
        assert ratio<1
    print(f"X={X} output_prime_power_cap_over_target={ratio:.8g}")
print("FORTUNE_INT_SOCG_C2_WEIGHTED_MEAN_SCALE_PASS")
