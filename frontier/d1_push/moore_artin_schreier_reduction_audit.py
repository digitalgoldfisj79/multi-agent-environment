#!/usr/bin/env sage-python
"""Exact audit of the one-variable Moore/Artin-Schreier reduction.

For K=F_(p^p), u!=0, put v=u^p and w=u^(p^2), and

 Xi_a(u) = [v^2-u*w-a*u*v*(2u^2+3uv+v^2)]/[3a*u*v*(u+v)].

The reduction predicts
 p*N_a(p) = #{u in K^*: Xi_a(u)^p-Xi_a(u)=u}.

The denominator never vanishes for u!=0 because u^p=-u would put u in
F_(p^2) intersect F_(p^p)=F_p and hence u=0.
"""
from __future__ import annotations
import argparse, json, time
from sage.all import GF, is_prime


def nonsquare(p):
    for a in range(2,p):
        if pow(a,(p-1)//2,p)==p-1:
            return a
    raise RuntimeError


def run(p,a_int):
    K=GF(p**p,'z')
    a=K(a_int)
    count=0
    den_zero=0
    t=time.time()
    for u in K:
        if not u:
            continue
        v=u**p
        w=v**p
        den=3*a*u*v*(u+v)
        if not den:
            den_zero+=1
            continue
        xi=(v*v-u*w-a*u*v*(2*u*u+3*u*v+v*v))/den
        if xi**p-xi==u:
            count+=1
    return {'p':p,'a':a_int,'root_count':count,'N_from_recurrence':count//p,
            'divisible_by_p':count%p==0,'denominator_zero_nonzero_u':den_zero,
            'elapsed_seconds':time.time()-t}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('p',type=int);args=ap.parse_args();p=args.p
    if not is_prime(p) or p<5: raise SystemExit('p prime >=5')
    rows=[]
    for a in (1,nonsquare(p)):
        row=run(p,a);rows.append(row);print(json.dumps(row),flush=True)
    print(json.dumps({'status':'PASS','rows':rows},indent=2))

if __name__=='__main__':main()
