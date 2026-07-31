#!/usr/bin/env python3
"""Exact J=1 q-line census for the direct d=1 normal-form family.

Requires python-flint. For each prime p and q in F_p minus {0,2}, count t in
F_p minus {+1,-1} for which
  q z^p + z^3 - 3z - (q-2)t
is irreducible. Write E_1(q)=p(1-I_1(q)) and sum over the generic q-line.
The output is finite exact data, not an asymptotic theorem.
"""
from __future__ import annotations
import argparse,json
import flint

def prime(n:int)->bool:
    return n>=5 and all(n%d for d in range(2,int(n**0.5)+1))

def census(p:int)->dict:
    if not prime(p): raise ValueError(f"expected prime >=5, got {p}")
    ctx=flint.fq_default_ctx(p,1); pc=flint.fq_default_poly_ctx(ctx)
    rows=[]; total=0; histogram={}
    for q in range(1,p):
        if q==2: continue
        tail=[ctx(-3),ctx(0),ctx(1)]+[ctx(0)]*(p-4)+[ctx(q)]
        count=0
        for t in range(p):
            if t in (1,p-1): continue
            f=pc([ctx(-(q-2)*t)]+tail); _,fac=f.factor()
            if len(fac)==1 and fac[0][0].degree()==p and fac[0][1]==1: count+=1
        e1=p*(1-count); total+=e1; histogram[count]=histogram.get(count,0)+1
        rows.append({"q":q,"I1":count,"E1":e1})
    return {
      "p":p,"generic_q_count":p-2,"sum_E1":total,"sum_E1_over_p":total//p,
      "I1_histogram":histogram,"rows":rows,
      "status":"EXACT_FINITE_PANEL",
      "boundary":"The complete J=1 trace is exact for this p; variation in p is not an asymptotic theorem.",
    }

def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument('primes',nargs='+',type=int);args=parser.parse_args()
    for p in args.primes: print(json.dumps(census(p),sort_keys=True))
if __name__=='__main__':main()
