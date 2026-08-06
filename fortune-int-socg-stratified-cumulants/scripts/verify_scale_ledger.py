#!/usr/bin/env python3
"""Log-scale sanity check for the preregistered asymptotic ledger."""
import math

sigma=0.5
delta=0.25
epsilon=0.1
c_mean=0.25
previous=None

# Write L=log X.  Then n_b B has logarithm L-log L at the registered
# stratum scale, and tau_b D_b is computed without constructing exp(L).
for logx in (8,16,64,256,1024,4096,16384,65536):
    width_over_x=1/(logx**(1+sigma))
    log_rows_times_strata=logx-math.log(logx)
    tau_d=((1+3*epsilon)/c_mean)*log_rows_times_strata/(logx**(1+delta))
    log_tau=(
        math.log(1+3*epsilon)
        + math.log(log_rows_times_strata)
        - math.log(c_mean)
        - logx
    )
    assert width_over_x>0
    assert log_tau<0
    if previous is not None:
        assert tau_d<previous
    previous=tau_d
    print(
        f"logX={logx} width_over_X={width_over_x:.8g} "
        f"log_tau={log_tau:.8g} tauD={tau_d:.8g}"
    )

assert previous<0.5
print("FORTUNE_INT_SOCG_SCALE_LEDGER_PASS")
