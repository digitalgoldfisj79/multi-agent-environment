#!/usr/bin/env python3
"""Exact finite probe of the primitive middle-configuration residual.

For each prime and square class A=chi(a), this script:
  1. computes the selected generic split/nonsplit irreducible-fibre counts;
  2. forms the complete selected virtual trace E_total = sum_q (p-p*n(q));
  3. subtracts the exact Kummer, pair and D extremal ledger from
     QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md;
  4. records E_middle = E_total-E_extremal.

The result is an exact finite diagnostic, not a general-p bound.
Requires python-flint.
"""
from __future__ import annotations
import argparse, json
from math import isqrt
from flint import nmod_poly


def primes_upto(n):
    s=[True]*(n+1); s[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def chi(x,p):
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def least_nr(p):
    for x in range(2,p):
        if chi(x,p)==-1:return x
    raise AssertionError

def eps(p): return chi(((-1)**((p-1)//2))*3,p)

def inv(x,p): return pow(x%p,p-2,p)

def irreducible_count(p,a3,a1):
    n=0
    for d in range(p):
        f=nmod_poly([d,a1%p,0,a3%p]+[0]*(p-4)+[1],p)
        _,fac=f.factor()
        if len(fac)==1 and fac[0][0].degree()==p and fac[0][1]==1:n+=1
    return n

def cell_counts(p):
    eta=least_nr(p); plus={}; minus={}
    for q in range(1,p):
        if q==2:continue
        plus[q]=irreducible_count(p,inv(q,p),-3*inv(q,p))
        minus[q]=irreducible_count(p,-inv(eta*q,p),3*inv(q,p))
    return plus,minus

def ap24(p):
    if chi(-6,p)==-1:return 0
    for x in range(isqrt(p)+1):
        for y in range(isqrt(p//3)+2):
            if x*x+6*y*y==p:return 2*(x*x-6*y*y)
            if 2*x*x+3*y*y==p:return -2*(2*x*x-3*y*y)
    raise AssertionError(p)

def Fqr(p,q,r):return (r*(r-q-3)**2-(q-2)**2)%p

def U1(p):return sum(chi(r*q*Fqr(p,q,r),p) for q in range(p) for r in range(p))

def B0(p):
    if p==5:return 0
    if chi(-1,p)==1:return chi(3,p)*(chi(5,p)-5)//2
    return chi(3,p)*((3+chi(5,p))//2-chi(2,p))

def Bc(p):
    if p==5:return -4
    if chi(-1,p)==1:return -p+chi(2,p)*chi(3,p)*(chi(5,p)-3)//2
    return chi(3,p)*p-chi(3,p)+chi(2,p)*chi(3,p)*(chi(5,p)+1)//2

def ledger(p):
    e=eps(p); delta=chi(-1,p)
    Kp0=-e*chi(2,p); Kpc=e*(p-2); Km0=-Kp0; Kmc=-Kpc
    bp0=B0(p); bpc=Bc(p); bm0=bp0; bmc=bpc
    dp0=e*(-chi(-6,p)*p-ap24(p)-delta-2*chi(2,p)+2*chi(6,p))
    dpc=e*(-delta*p-3)
    if p==5:
        dm0, dmc=-4,4
    else:
        dm0=e*(U1(p)-chi(2,p)*(3*p-1+chi(5,p))-1)
        dmc=e*((p-1)*chi(5,p)-p*(1+delta)+2)
    return {'K':(Kp0,Kpc,Km0,Kmc),'B':(bp0,bpc,bm0,bmc),'D':(dp0,dpc,dm0,dmc)}

def select(A,delta,quad):
    xp0,xpc,xm0,xmc=quad
    return (xp0+A*xpc+xm0-delta*A*xmc)//2

def audit_prime(p):
    plus,minus=cell_counts(p); delta=chi(-1,p); L=ledger(p)
    rows=[]
    for A in (1,-1):
        qp=[q for q in plus if chi(q,p)==A]
        qm=[q for q in minus if chi(q,p)==-delta*A]
        ncells=len(qp)+len(qm)
        nir=sum(plus[q] for q in qp)+sum(minus[q] for q in qm)
        Etotal=p*ncells-p*nir
        EK=select(A,delta,L['K']); EB=select(A,delta,L['B']); ED=select(A,delta,L['D'])
        Eext=EK+EB-ED
        rows.append({'A':A,'generic_cells':ncells,'generic_irreducibles':nir,
                     'E_total':Etotal,'E_extremal':Eext,
                     'E_middle':Etotal-Eext,'E_middle_over_p':(Etotal-Eext)/p})
    return {'p':p,'rows':rows}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=31);ap.add_argument('--output')
    a=ap.parse_args(); rows=[audit_prime(p) for p in primes_upto(a.max_prime) if p>=5]
    out={'status':'PASS','scope':'exact finite diagnostic; no general bound claimed',
         'max_prime':a.max_prime,'results':rows}
    txt=json.dumps(out,indent=2);print(txt)
    if a.output:open(a.output,'w').write(txt+'\n')
if __name__=='__main__':main()
