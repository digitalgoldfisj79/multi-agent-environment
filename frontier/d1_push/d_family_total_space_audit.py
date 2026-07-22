#!/usr/bin/env python3
"""Exact audit of D_FAMILY_TOTAL_SPACE_THEOREM.md.

Uses only integer modular arithmetic. For every prime in range it compares:
  (1) direct sum of the original prime-field D_q trace formula;
  (2) the fixed-surface compression;
  (3) the bielliptic E1+E2 decomposition;
  (4) the closed CM-newform formula.
"""
from __future__ import annotations
import argparse, json
from math import isqrt


def primes_upto(n: int):
    sieve=[True]*(n+1); sieve[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if sieve[i]:
            sieve[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(sieve) if v]


def chi(x:int,p:int)->int:
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1


def ap_cm24(p:int)->int:
    if chi(-6,p)==-1:return 0
    for x in range(isqrt(p)+1):
        for y in range(isqrt(p//3)+2):
            if x*x+6*y*y==p:
                return 2*(x*x-6*y*y)
            if 2*x*x+3*y*y==p:
                return -2*(2*x*x-3*y*y)
    raise AssertionError(f'no form representation for split prime {p}')


def d_trace_direct(p:int,q:int)->int:
    kap=3*((-1)**((p-1)//2))
    s=0
    for z in range(p):
        gp=(q*pow((z-1)%p,p-2,p)+z+2)%p
        gm=(q*pow((z+1)%p,p-2,p)+z-2)%p
        s+=chi(kap*q*gp*gm,p)
    return -chi(kap*q,p)-s


def surface_sum(p:int)->int:
    return sum(chi((z*z-1)*q*(q+z*z+z-2)*(q+z*z-z-2),p)
               for z in range(p) for q in range(p))


def a1(p:int,q:int)->int:
    return -sum(chi(q*(r-1)*((q+r-2)**2-r),p) for r in range(p))


def a2(p:int,q:int)->int:
    return -chi(q,p)-sum(chi(q*r*(r-1)*((q+r-2)**2-r),p) for r in range(p))


def audit(p:int):
    eps=chi(3*((-1)**((p-1)//2)),p)
    direct=sum(d_trace_direct(p,q) for q in range(1,p) if q!=2)
    S=surface_sum(p)
    compressed=eps*((p-2)*chi(2,p)+2*chi(6,p)-S)
    A1=sum(a1(p,q) for q in range(p))
    A2=sum(a2(p,q) for q in range(p))
    ap=ap_cm24(p)
    predicted=eps*(-chi(-6,p)*p-ap-chi(-1,p)-2*chi(2,p)+2*chi(6,p))
    checks={
      'direct_equals_compressed':direct==compressed,
      'surface_bielliptic':S==-(A1+A2),
      'A1_closed':A1==-chi(-6,p)*p-chi(-1,p),
      'A2_K3':A2==-chi(2,p)*p-ap,
      'D_total_closed':direct==predicted,
    }
    return {'p':p,'checks':checks,'pass':all(checks.values()),
            'D_total':direct,'surface_sum':S,'A1':A1,'A2':A2,
            'a_p_24_3_h_a':ap,'epsilon':eps,'predicted':predicted}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=199);ap.add_argument('--output')
    args=ap.parse_args()
    rows=[audit(p) for p in primes_upto(args.max_prime) if p>=5]
    out={'status':'PASS' if all(r['pass'] for r in rows) else 'FAIL',
         'method':'Exact exhaustive prime-field character sums; no floating point.',
         'prime_count':len(rows),'max_prime':args.max_prime,'results':rows}
    text=json.dumps(out,indent=2)
    print(text)
    if args.output:open(args.output,'w').write(text+'\n')
if __name__=='__main__':main()
