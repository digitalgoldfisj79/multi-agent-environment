#!/usr/bin/env python3
"""Exact small-panel ordinary-cumulant diagnostics using SymPy.

Temperatures or lower scales inferred from these outputs are inadmissible in a proof.
"""
from __future__ import annotations
import argparse
import math
from fractions import Fraction
from sympy import isprime, primerange, primorial
from verify_equality_pattern_decomposition import canonical_partitions

def scalar_cumulant(values,k):
    total=Fraction(0)
    for part in canonical_partitions(k):
        coeff=Fraction(((-1)**(len(part)-1))*math.factorial(len(part)-1))
        product=Fraction(1)
        for block in part:
            power=len(block)
            product*=Fraction(sum(v**power for v in values),len(values))
        total+=coeff*product
    return total

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=int,default=100)
    parser.add_argument("--eta",type=float,default=0.5)
    parser.add_argument("--order",type=int,default=6)
    parser.add_argument("--sigma",type=float,default=0.5)
    args=parser.parse_args()
    h=int(args.eta*args.x*args.x)
    terminal=list(primerange(args.x,2*args.x))
    candidates=list(primerange(2,h+1))
    width=max(1,int(args.x/(math.log(args.x)**(1+args.sigma))))
    groups={}
    for ell in terminal:
        centre=int(primorial(ell,method="primes"))
        z=sum(1 for m in candidates if ell<m<=h and isprime(centre+m))
        groups.setdefault((ell-args.x)//width,[]).append(z)
    for key,zs in sorted(groups.items()):
        cumulants=[scalar_cumulant(zs,k) for k in range(1,min(args.order,len(zs))+1)]
        print(f"stratum={key} rows={len(zs)} minZ={min(zs)} meanZ={sum(zs)/len(zs):.8g} maxZ={max(zs)} cumulants={cumulants}")
    print("FORTUNE_INT_SOCG_C8_SELECTED_CENTRE_DIAGNOSTIC_COMPLETE")
if __name__=="__main__":
    main()
