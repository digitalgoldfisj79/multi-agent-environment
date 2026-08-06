#!/usr/bin/env python3
"""Finite diagnostic for the post-terminal-prime local edge kernel.

This is method-selection evidence only and proves no asymptotic estimate.
"""
from __future__ import annotations
import math

def primes_upto(limit):
    sieve=bytearray(b"\x01")*(limit+1)
    if limit>=0: sieve[0]=0
    if limit>=1: sieve[1]=0
    for p in range(2,int(limit**0.5)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p]=b"\x00"*(((limit-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]
for X in (40,60,80,100,150):
    H=X*X//2
    ps=primes_upto(H)
    candidates=[p for p in ps if 2*X<p<=H]
    post=candidates
    tail=sum(1/(p*p) for p in post)
    collision=[0.0]*(H+1)
    for p in post:
        for d in range(p,H+1,p):
            collision[d]+=1/p
    max_row=0.0
    total=0.0
    base=tail*max(0,len(candidates)-1)
    for m in candidates:
        row=base+sum(collision[abs(m-n)] for n in candidates if n!=m)
        max_row=max(max_row,row)
        total+=row
    mean_row=total/max(1,len(candidates))
    scale=X/(math.log(X)**2)
    print(f"X={X} columns={len(candidates)} max_edge_row={max_row:.8g} mean_edge_row={mean_row:.8g} ratio_to_X_log2={max_row/scale:.8g}")
print("FORTUNE_INT_SOCG_C4_LOCAL_EDGE_DIAGNOSTIC_COMPLETE")
