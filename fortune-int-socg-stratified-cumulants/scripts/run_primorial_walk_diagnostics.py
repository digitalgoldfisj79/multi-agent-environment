#!/usr/bin/env python3
"""Diagnostic additive-character traces along the selected primorial walk.

This script is method-selection evidence only. It proves no asymptotic estimate.
"""
from __future__ import annotations
import argparse
import cmath
import math

def primes_up_to(limit):
    sieve=bytearray(b"\x01")*(limit+1)
    if limit>=0: sieve[0]=0
    if limit>=1: sieve[1]=0
    for p in range(2,int(limit**0.5)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p]=b"\x00"*(((limit-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=int,default=200)
    parser.add_argument("--probe-count",type=int,default=5)
    args=parser.parse_args()
    primes=primes_up_to(6*args.x)
    rows=[p for p in primes if args.x<=p<2*args.x]
    probes=[p for p in primes if p>2*args.x][:args.probe_count]
    for q in probes:
        primorial=1
        values=[]
        row_set=set(rows)
        for p in primes:
            if p>rows[-1]: break
            primorial=(primorial*p)%q
            if p in row_set: values.append(primorial)
        for frequency in range(1,min(5,q)):
            trace=sum(cmath.exp(2j*math.pi*frequency*v/q) for v in values)/len(values)
            print(f"X={args.x} q={q} a={frequency} rows={len(values)} trace_abs={abs(trace):.8g}")
    print("FORTUNE_INT_SOCG_C5_PRIMORIAL_WALK_DIAGNOSTIC_COMPLETE")
if __name__=="__main__":
    main()
