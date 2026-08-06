#!/usr/bin/env python3
"""Regression for deterministic terminal-prime stratum assignment."""
import math

def stratum_key(terminal_prime,x,sigma):
    width=max(1,int(x/(math.log(x)**(1+sigma))))
    return (terminal_prime-x)//width

for x in (100,1000,10000):
    sigma=0.5
    keys=[stratum_key(p,x,sigma) for p in range(x,2*x)]
    assert keys==sorted(keys)
    fake_occupancies=[(p*p)%17 for p in range(x,2*x)]
    keys_again=[stratum_key(p,x,sigma) for p,_ in zip(range(x,2*x),fake_occupancies)]
    assert keys_again==keys
    print(f"X={x} strata={1+max(keys)} deterministic=1")
print("FORTUNE_INT_SOCG_C1_STRATUM_GEOMETRY_PASS")
