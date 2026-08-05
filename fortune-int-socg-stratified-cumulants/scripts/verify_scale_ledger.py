#!/usr/bin/env python3
"""Numerical sanity check for the preregistered asymptotic scale ledger."""
import math
sigma=0.5
delta=0.25
epsilon=0.1
c_mean=0.25
previous=None
for exponent in (8,12,16,24,32,48,64):
    x=math.exp(exponent)
    logx=math.log(x)
    width=x/(logx**(1+sigma))
    rows=width/logx
    strata=logx**(1+sigma)
    lower_mean=c_mean*x
    tau=(1+3*epsilon)*math.log(rows*strata)/lower_mean
    dependence=x/(logx**(1+delta))
    tau_d=tau*dependence
    assert width>0 and rows>0 and strata>0 and 0<tau<1
    if previous is not None:
        assert tau_d<previous
    previous=tau_d
    print(f"logX={exponent} width_over_X={width/x:.8g} rows={rows:.8g} tau={tau:.8g} tauD={tau_d:.8g}")
print("FORTUNE_INT_SOCG_SCALE_LEDGER_PASS")
