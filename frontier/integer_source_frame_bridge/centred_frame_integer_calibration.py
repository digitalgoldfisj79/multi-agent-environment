#!/usr/bin/env python3
"""Finite primorial-block calibration of the centred reciprocal frame.

Uses rho(t)=exp(-pi*t^2), |a|<=6, H=0.8X^2, and the conjectural
Hardy--Littlewood baseline.  No asymptotic conclusion is inferred.
"""
from __future__ import annotations
import cmath, json, math
from pathlib import Path
import mpmath as mp
import numpy as np
from sympy import isprime, perfect_power, prevprime, primerange

TARGETS=(11,17,23,29,37,43,53,61,73,89,101,113,131)
ETA=.8
AMAX=6

def c2(limit=200_000):
    s=mp.mpf("0")
    for p in primerange(3,limit+1):
        s+=mp.log(mp.mpf(p*(p-2))/mp.mpf((p-1)**2))
    return mp.e**s

def singular(pmax,C2):
    z=2*C2
    for p in primerange(3,pmax+1):
        z*=mp.mpf(p-1)/mp.mpf(p-2)
    return z

def mangoldt(n):
    if isprime(n): return math.log(n)
    pp=perfect_power(n)
    if pp and isprime(pp[0]): return math.log(int(pp[0]))
    return 0.0

def kernel_matrix(centres,H):
    qs=[int(q) for q in primerange(H,2*H)]
    D=sum(math.exp(-math.pi*(H*a/q)**2)
          for a in range(-AMAX,AMAX+1) if a
          for q in qs)
    rows={a:[(q,math.exp(-math.pi*(H*a/q)**2)/D) for q in qs]
          for a in range(1,AMAX+1)}
    def K(L):
        z=0.0
        for a,rw in rows.items():
            m=sum(w for _,w in rw)
            t=sum(w*cmath.exp(2j*math.pi*a*(L%q)/q) for q,w in rw)
            z+=2*abs(t)**2/m
        return z
    n=len(centres)
    A=np.array([[K(centres[j]-centres[k]) for k in range(n)]
                for j in range(n)],float)
    tail=2*sum(math.exp(-math.pi*(a/2)**2) for a in range(AMAX+1,100))
    return A,len(qs),tail

def block(X,C2):
    ell=[int(p) for p in primerange(X,2*X)]
    P=1
    for p in primerange(2,X): P*=int(p)
    centres=[]; pmax=[]; prev=int(prevprime(X))
    for j,p in enumerate(ell):
        centres.append(P); pmax.append(prev if j==0 else ell[j-1]); P*=p
    H=int(ETA*X*X)
    c=[]
    for P,r in zip(centres,pmax):
        psi=sum(mangoldt(P+m) for m in range(2,H+1))
        mu=float(singular(r,C2)*(mp.li(H)-mp.li(r)))
        c.append(psi-mu)
    K,qcount,tail=kernel_matrix(centres,H)
    eig=np.linalg.eigvalsh(K); I=np.eye(len(K)); off=K-I
    v=np.asarray(c,float); V=float(v@v)
    return {
      "X":X,"N":len(centres),"H":H,
      "largest_centre_digits":len(str(centres[-1])),
      "q_shell_count":qcount,"gaussian_signed_tail_bound":tail,
      "kernel_min_eigenvalue":float(eig[0]),
      "kernel_max_eigenvalue":float(eig[-1]),
      "operator_norm_K_minus_I":float(max(abs(eig-1))),
      "kernel_total_off_diagonal_mass":float(off.sum()),
      "kernel_max_off_diagonal_row_sum":float(off.sum(axis=1).max()),
      "residual_rayleigh_quotient":float(v@K@v/V)
    }

def main():
    mp.mp.dps=40; C2=c2()
    rows=[block(X,C2) for X in TARGETS]
    for r in rows:
        assert r["kernel_min_eigenvalue"]>0
        assert r["gaussian_signed_tail_bound"]<1e-15
    out={
      "status":"finite calibration; no asymptotic inference",
      "parameters":{"targets":list(TARGETS),"eta":ETA,
                    "harmonic_cutoff":AMAX,
                    "twin_prime_constant_approximation":float(C2)},
      "summary":{
        "minimum_eigenvalue_over_panel":min(r["kernel_min_eigenvalue"] for r in rows),
        "maximum_eigenvalue_over_panel":max(r["kernel_max_eigenvalue"] for r in rows),
        "minimum_residual_rayleigh_quotient":min(r["residual_rayleigh_quotient"] for r in rows),
        "maximum_residual_rayleigh_quotient":max(r["residual_rayleigh_quotient"] for r in rows),
        "minimum_total_off_diagonal_mass":min(r["kernel_total_off_diagonal_mass"] for r in rows),
        "maximum_total_off_diagonal_mass":max(r["kernel_total_off_diagonal_mass"] for r in rows),
        "minimum_max_row_sum":min(r["kernel_max_off_diagonal_row_sum"] for r in rows),
        "maximum_max_row_sum":max(r["kernel_max_off_diagonal_row_sum"] for r in rows)
      },
      "rows":rows,
      "boundary":"Finite positivity and near-one Rayleigh quotients do not prove a uniform lower frame bound."
    }
    path=Path(__file__).with_name("centred_frame_integer_calibration_results.json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
