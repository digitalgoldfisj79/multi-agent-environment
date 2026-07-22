#!/usr/bin/env python3
"""Exact audit for PAIR_CURVE_Q_AVERAGE_THEOREM.md.

Directly counts the smooth projective hyperelliptic models B_q and Q_q over
F_p for every admissible q and compares their summed anti-invariant trace with
the closed formula. No random sampling or floating point is used.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp

def chi(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def counts(p,q):
    inv3=pow(3,p-2,p)
    NBaff=0
    for d in range(p):
        rhs=(12-d*d-4*q*pow(d,p-1,p))*inv3%p
        NBaff+=1+chi(rhs,p)
    lc=(-4*q*inv3)%p
    NB=NBaff+1+chi(lc,p)

    m=(p-1)//2
    NQaff=0
    for r in range(p):
        rhs=(12-r-4*q*pow(r,m,p))*inv3%p
        NQaff+=1+chi(rhs,p)
    NQ=NQaff+(1 if m%2 else 1+chi(lc,p))
    return NB,NQ,NQ-NB

def predict(p):
    if p==5:return 0
    if p%4==1:
        return chi(3,p)*(chi(5,p)-5)//2
    return chi(3,p)*((3+chi(5,p))//2-chi(2,p))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-prime',type=int,default=199)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); rows=[]
    for p in list(sp.primerange(5,a.max_prime+1)):
        total=0
        for q in range(1,p):
            if q==2:continue
            NB,NQ,b=counts(p,q); total+=b
        pred=predict(p)
        rows.append({'p':p,'q_checked':p-2,'trace_sum':total,'predicted':pred,
                     'absolute_bound_pass':abs(total)<=3,'all_checks_pass':total==pred and abs(total)<=3})
    out={'status':'PASS' if all(r['all_checks_pass'] for r in rows) else 'FAIL',
         'method':'Exact direct F_p point counts for every q and every prime in range; no sampling or floating point.',
         'results':rows}
    text=json.dumps(out,indent=2);print(text)
    if a.output:a.output.write_text(text+'\n')
if __name__=='__main__':main()
