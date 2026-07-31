#!/usr/bin/env python3
"""Exact finite-panel Jacobian and rho-transversality audit for TFP3.

Input is classifier JSONL. This certifies tangent ranks at enumerated points
only; it does not determine global dimension or exclude other components.
"""
from __future__ import annotations
import argparse,collections,json
from pathlib import Path
import sympy as sp
import ff_nonzero_defect_cubic_oriented_coefficient as coefficient
import ff_tfp3_orientation_verify as orientation

def rank_mod(matrix:list[list[int]],q:int)->int:
    a=[[x%q for x in row] for row in matrix]; r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]; inv=pow(a[r][c],-1,q);a[r]=[x*inv%q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c];a[i]=[(a[i][j]-z*a[r][j])%q for j in range(len(a[i]))]
        r+=1
        if r==len(a):break
    return r

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('panel',type=Path);a=ap.parse_args()
    variables,equations,s=coefficient.build_system();dep=variables[:-1]
    full=sp.Matrix(equations).jacobian(variables); fixed=sp.Matrix(equations).jacobian(dep)
    rows=[]
    for line in a.panel.read_text().splitlines():
        if not line.strip():continue
        row=json.loads(line)
        if row['type']!='orbit':continue
        q=int(row['q']);sub={s['rho']:int(row['rho'])%q}
        for name in 'ABCD':
            a2,a1,a0=row[name];f=[a0%q,a1%q,a2%q,1]
            sub[s[name+'2']]=a2;sub[s[name+'1']]=a1;sub[s[name+'0']]=a0
            sub[s['e'+name]]=orientation.eta_frobenius(f,q)
        assert not any(coefficient.modular_rational(e.subs(sub),q) for e in equations)
        rf=rank_mod([[coefficient.modular_rational(x.subs(sub),q) for x in r] for r in full.tolist()],q)
        rd=rank_mod([[coefficient.modular_rational(x.subs(sub),q) for x in r] for r in fixed.tolist()],q)
        rows.append({'q':q,'rho':int(row['rho'])%q,'full_rank':rf,'fixed_rho_rank':rd,'A':row['A'],'B':row['B'],'C':row['C'],'D':row['D']})
    print(json.dumps({
      'status':'EXACT_FINITE_PANEL',
      'orbits':len(rows),
      'full_rank_histogram':dict(collections.Counter(r['full_rank'] for r in rows)),
      'fixed_rho_rank_histogram':dict(collections.Counter(r['fixed_rho_rank'] for r in rows)),
      'rho_one':[r for r in rows if r['rho']==1],
      'fixed_rho_exceptions':[r for r in rows if r['fixed_rho_rank']<16],
      'boundary':'Ranks certify local tangents and rho transversality only at enumerated points; they do not prove global dimension, irreducibility or finite generic fibres.',
    },indent=2,sort_keys=True))
if __name__=='__main__':main()
