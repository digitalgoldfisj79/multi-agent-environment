#!/usr/bin/env python3
"""Exact finite-field audit for QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md.

Checks pair weighted averages, ordinary/twisted D averages, the U0 rational
surface formula, and all weighted formulas. Integer modular arithmetic only.
"""
from __future__ import annotations
import argparse, json
from math import isqrt


def primes_upto(n):
    s=[True]*(n+1); s[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def chi(x,p):
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def eps(p): return chi(((-1)**((p-1)//2))*3,p)

def ap24(p):
    if chi(-6,p)==-1:return 0
    for x in range(isqrt(p)+1):
        for y in range(isqrt(p//3)+2):
            if x*x+6*y*y==p:return 2*(x*x-6*y*y)
            if 2*x*x+3*y*y==p:return -2*(2*x*x-3*y*y)
    raise AssertionError(p)

def btrace(p,q):
    inv3=pow(3,p-2,p); m=(p-1)//2
    NB=sum(1+chi((12-d*d-4*q*pow(d,p-1,p))*inv3,p) for d in range(p))
    NB+=1+chi(-4*q*inv3,p)
    NQ=sum(1+chi((12-r-4*q*pow(r,m,p))*inv3,p) for r in range(p))
    NQ+=(1+chi(-4*q*inv3,p)) if m%2==0 else 1
    return NQ-NB

def B0pred(p):
    if p==5:return 0
    if chi(-1,p)==1:return chi(3,p)*(chi(5,p)-5)//2
    return chi(3,p)*((3+chi(5,p))//2-chi(2,p))

def Bcpred(p):
    if p==5:return -4
    if chi(-1,p)==1:
        return -p+chi(2,p)*chi(3,p)*(chi(5,p)-3)//2
    return chi(3,p)*p-chi(3,p)+chi(2,p)*chi(3,p)*(chi(5,p)+1)//2

def Fqr(p,q,r): return (r*(r-q-3)**2-(q-2)**2)%p

def Hval(p,q,r):
    if r==1:return 3*(q-2)*pow(2,p-2,p)%p
    return (Fqr(p,q,r)*pow((r-1)%p,p-3,p))%p

def Dparts(p,q):
    u=(((-1)**((p-1)//2))*3*q)%p
    ap=-sum(chi(u*Hval(p,q,r),p) for r in range(p))
    am=-chi(u,p)-sum(chi(u*r*Hval(p,q,r),p) for r in range(p))
    return ap,am

def U0(p): return sum(chi(q*Fqr(p,q,r),p) for q in range(p) for r in range(p))
def U1(p): return sum(chi(r*q*Fqr(p,q,r),p) for q in range(p) for r in range(p))

def audit(p):
    Q=[q for q in range(1,p) if q!=2]
    b0=sum(btrace(p,q) for q in Q); bc=sum(chi(q,p)*btrace(p,q) for q in Q)
    dp0=sum(sum(Dparts(p,q)) for q in Q)
    dpc=sum(chi(q,p)*sum(Dparts(p,q)) for q in Q)
    dm0=sum(Dparts(p,q)[0]-Dparts(p,q)[1] for q in Q)
    dmc=sum(chi(q,p)*(Dparts(p,q)[0]-Dparts(p,q)[1]) for q in Q)
    if p==5:
        dm0pred,dmcpred=-4,4
    else:
        dm0pred=eps(p)*(U1(p)-chi(2,p)*(3*p-1+chi(5,p))-1)
        dmcpred=eps(p)*((p-1)*chi(5,p)-p*(1+chi(-1,p))+2)
    checks={
      'B0':b0==B0pred(p), 'Bchi':bc==Bcpred(p),
      'Dplus0':dp0==eps(p)*(-chi(-6,p)*p-ap24(p)-chi(-1,p)-2*chi(2,p)+2*chi(6,p)),
      'Dpluschi':dpc==eps(p)*(-chi(-1,p)*p-3),
      'Dminus0':dm0==dm0pred, 'Dminuschi':dmc==dmcpred,
      'U0':U0(p)==2*chi(2,p)*p+1,
    }
    return {'p':p,'pass':all(checks.values()),'checks':checks,
            'B0':b0,'Bchi':bc,'Dplus0':dp0,'Dpluschi':dpc,
            'Dminus0':dm0,'Dminuschi':dmc,'U0':U0(p),'U1':U1(p)}

def main():
    pa=argparse.ArgumentParser(); pa.add_argument('--max-prime',type=int,default=199);pa.add_argument('--output')
    a=pa.parse_args(); rows=[audit(p) for p in primes_upto(a.max_prime) if p>=5]
    out={'status':'PASS' if all(r['pass'] for r in rows) else 'FAIL',
         'method':'Exact exhaustive F_p character sums; no floating point.',
         'prime_count':len(rows),'max_prime':a.max_prime,'results':rows}
    txt=json.dumps(out,indent=2);print(txt)
    if a.output:open(a.output,'w').write(txt+'\n')
if __name__=='__main__':main()
