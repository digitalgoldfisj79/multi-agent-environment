#!/usr/bin/env python3
"""Fingerprint N_square,N_nonsquare deviations against small elliptic traces.

The square-class sum and difference separate invariant and quadratic-twist
motivic components. The script reads the committed exact count ledger, accepts
additional rows, enumerates y^2=x^3+A*x+B over a configurable coefficient box,
and reports correlations plus train/holdout sparse least-squares diagnostics.
This is a discovery audit, not a proof of a motive decomposition.
"""
from __future__ import annotations
import argparse,csv,json,math
import numpy as np

def chi(v,p):
    v%=p
    if not v:return 0
    return 1 if pow(v,(p-1)//2,p)==1 else -1

def main():
    ap=argparse.ArgumentParser();ap.add_argument('csv');ap.add_argument('--box',type=int,default=20);ap.add_argument('--extra',default='');a=ap.parse_args()
    rows=[]
    with open(a.csv) as f:
        for r in csv.DictReader(f):rows.append((int(r['prime']),int(r['N_square']),int(r['N_nonsquare'])))
    if a.extra:
        for item in a.extra.split(';'):
            p,x,y=map(int,item.split(','));rows.append((p,x,y))
    rows=sorted(dict((p,(p,x,y)) for p,x,y in rows).values())
    curves=[]
    for A in range(-a.box,a.box+1):
      for B in range(-a.box,a.box+1):
        if 4*A*A*A+27*B*B:curves.append((A,B))
    traces={}
    for A,B in curves:
      traces[(A,B)]=np.array([-sum(chi(x*x%p*x+A*x+B,p) for x in range(p)) for p,_,_ in rows],float)
    targets={
      'sum':np.array([ns+nn-2*p for p,ns,nn in rows],float),
      'difference':np.array([ns-nn for p,ns,nn in rows],float),
      'square':np.array([ns-p for p,ns,nn in rows],float),
      'nonsquare':np.array([nn-p for p,ns,nn in rows],float),
    }
    result={}
    for name,y in targets.items():
      cor=[]
      for key,x in traces.items():
        if np.std(x):cor.append((abs(float(np.corrcoef(x,y)[0,1])),float(np.corrcoef(x,y)[0,1]),key))
      cor.sort(reverse=True);top=cor[:20];selected=[]
      for _,_,k in top:
        # remove exact duplicate trace vectors
        if not any(np.array_equal(traces[k],traces[j]) for j in selected):selected.append(k)
        if len(selected)==10:break
      X=np.column_stack([np.ones(len(rows))]+[traces[k] for k in selected])
      train=np.array([p<=199 for p,_,_ in rows]);coef=np.linalg.lstsq(X[train],y[train],rcond=None)[0];pred=X@coef;hold=~train
      result[name]={
        'max_abs_over_sqrt_p':max(abs(v)/math.sqrt(p) for v,(p,_,_) in zip(y,rows)),
        'top_correlations':[{'curve':list(k),'correlation':c} for _,c,k in top],
        'selected_curves':[list(k) for k in selected],
        'rounded_coefficients':[int(round(v)) for v in coef],
        'train_MAE':float(np.mean(abs(pred[train]-y[train]))),
        'holdout_MAE':float(np.mean(abs(pred[hold]-y[hold]))),
        'holdout_max_error':float(np.max(abs(pred[hold]-y[hold]))),
        'exact_rounded_fit':bool(np.all(np.rint(X@np.rint(coef))==y)),
      }
    print(json.dumps({'status':'PASS','row_count':len(rows),'prime_max':max(p for p,_,_ in rows),'curve_count':len(curves),'analysis':result},indent=2))
if __name__=='__main__':main()
