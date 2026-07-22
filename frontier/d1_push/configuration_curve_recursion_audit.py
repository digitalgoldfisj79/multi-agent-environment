#!/usr/bin/env python3
"""Exact representation audit for CONFIGURATION_CURVE_RECURSION.md.

Checks dimensions and characters of
  exterior^k Perm_p = exterior^k Std_p + exterior^(k-1) Std_p,
the recursive inversion, total alternating coefficient formula, and complement
sign duality for all conjugacy classes (integer partitions) at selected primes.
No random sampling or floating point is used.
"""
from __future__ import annotations
import argparse,json
from math import comb
from pathlib import Path
import sympy as sp

def partitions(n,mx=None):
    if n==0:
        yield (); return
    if mx is None or mx>n: mx=n
    for a in range(mx,0,-1):
        for rest in partitions(n-a,a): yield (a,)+rest

def coeffs_perm_exterior(cyc,p):
    t=sp.symbols('t')
    F=1
    for d in cyc: F*=1-(-t)**d
    P=sp.Poly(sp.expand(F),t)
    return [int(P.coeff_monomial(t**k)) for k in range(p+1)]

def coeffs_std_exterior(cyc,p):
    t=sp.symbols('t')
    F=1
    for d in cyc: F*=1-(-t)**d
    Q,R=sp.div(sp.Poly(sp.expand(F),t),sp.Poly(1+t,t))
    assert R.is_zero
    return [int(Q.coeff_monomial(t**k)) for k in range(p)]

def audit_prime(p):
    bad=[]
    for cyc in partitions(p):
        C=coeffs_perm_exterior(cyc,p)
        H=coeffs_std_exterior(cyc,p)
        for k in range(p+1):
            rhs=(H[k] if k<p else 0)+(H[k-1] if k>=1 else 0)
            if C[k]!=rhs: bad.append((cyc,k,'two_step',C[k],rhs))
        for i in range(p):
            rhs=sum((-1)**(i-k)*C[k] for k in range(0,i+1))
            if H[i]!=rhs: bad.append((cyc,i,'recursion',H[i],rhs))
        lhs=sum((-1)**i*H[i] for i in range(p))
        rhs=sum((p-k)*(-1)**k*C[k] for k in range(p))
        if lhs!=rhs: bad.append((cyc,-1,'total',lhs,rhs))
        sign=(-1)**(p-len(cyc))
        for k in range(p+1):
            if C[p-k]!=sign*C[k]: bad.append((cyc,k,'complement',C[p-k],sign*C[k]))
    dim_checks=all(comb(p,k)==comb(p-1,k)+(comb(p-1,k-1) if k else 0)
                   for k in range(p+1))
    return {'p':p,'cycle_types_checked':sum(1 for _ in partitions(p)),
            'dimension_checks':dim_checks,'failures':bad[:20],
            'failure_count':len(bad),'all_checks_pass':dim_checks and not bad}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--primes',nargs='*',type=int,default=[5,7,11,13,17])
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); rows=[audit_prime(p) for p in a.primes]
    out={'status':'PASS' if all(r['all_checks_pass'] for r in rows) else 'FAIL',
         'method':'Exact character-polynomial arithmetic over every conjugacy class; no sampling or floating point.',
         'results':rows}
    text=json.dumps(out,indent=2); print(text)
    if a.output:a.output.write_text(text+'\n')
if __name__=='__main__':main()
