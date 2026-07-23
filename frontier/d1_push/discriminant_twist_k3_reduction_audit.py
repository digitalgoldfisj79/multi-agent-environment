#!/usr/bin/env python3
"""Exact audit of the D_q high-genus trace collapse to a fixed sextic/K3 surface.

For p>=5, kappa=3*(-1)^((p-1)/2), and q in F_p^*\{2}, define
 g_+=q(z-1)^(p-2)+z+2,
 g_-=q(z+1)^(p-2)+z-2.
The normalized D_q trace is
 a_D(q)=-sum_z chi(kappa*q*g_+*g_-)-chi(kappa*q).

Define the sextic virtual trace
 a_C*(q)=-sum_z chi(kappa*q*(z^2-1)
          *(z^4+(2q-5)z^2+(q-2)^2))-chi(kappa*q).
Then exactly
 a_D(q)=a_C*(q)-2 chi((3*kappa/2)q(q-2)).

The q-average is also checked against the complete double character sum.
No floating point or random sampling is used.
"""
from __future__ import annotations
import argparse,json
import sympy as sp


def chi(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def row_for_p(p):
    m=(p-1)//2
    kappa=(3*(-1 if m&1 else 1))%p
    inv2=pow(2,p-2,p)
    direct_total=0
    pointwise=[]
    for q in range(1,p):
        if q==2:continue
        SD=0;SC=0
        for z in range(p):
            gp=(q*pow((z-1)%p,p-2,p)+z+2)%p
            gm=(q*pow((z+1)%p,p-2,p)+z-2)%p
            SD+=chi(kappa*q*gp*gm,p)
            sext=(pow(z,4,p)+(2*q-5)*z*z+(q-2)*(q-2))%p
            SC+=chi(kappa*q*(z*z-1)*sext,p)
        aD=-SD-chi(kappa*q,p)
        aC=-SC-chi(kappa*q,p)
        corr=2*chi(3*kappa*inv2*q*(q-2),p)
        ok=(aD==aC-corr)
        pointwise.append({'q':q,'a_D':aD,'a_C_virtual':aC,'correction':corr,'pass':ok})
        direct_total+=aD
    Tall=0
    for q in range(p):
        for z in range(p):
            sext=(pow(z,4,p)+(2*q-5)*z*z+(q-2)*(q-2))%p
            Tall+=chi(kappa*q*(z*z-1)*sext,p)
    predicted=-Tall+(p-2)*chi(2*kappa,p)+2*chi(3*kappa*inv2,p)
    return {'p':p,'kappa':kappa,'q_count':p-2,'direct_D_trace_sum':direct_total,
            'complete_surface_character_sum':Tall,'predicted_D_trace_sum':predicted,
            'pointwise_pass':all(x['pass'] for x in pointwise),
            'q_average_pass':direct_total==predicted,
            'all_checks_pass':all(x['pass'] for x in pointwise) and direct_total==predicted,
            'pointwise':pointwise}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=199);a=ap.parse_args()
    rows=[]
    for p in sp.primerange(5,a.max_prime+1):
        r=row_for_p(int(p));rows.append(r)
        print(json.dumps({k:v for k,v in r.items() if k!='pointwise'}),flush=True)
    print(json.dumps({'status':'PASS' if all(r['all_checks_pass'] for r in rows) else 'FAIL',
                      'method':'exact exhaustive finite-field character sums','rows':rows},indent=2))

if __name__=='__main__':main()
