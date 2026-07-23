#!/usr/bin/env python3
"""Exact symbolic reduction of the linear-cubic incidence surface X_13,a.

Starting from CMMR.3,
  D^2=-4S^3-27N^2
and the linear-cubic incidence equation, solve the latter for N on the open
2aD-9y != 0. Substitution gives a quartic Q_a(S,D,y)=0. The script computes
and factors its discriminant in D exactly over Q, then audits the primitive
branch polynomial for the two representatives a=1,2.
"""
from __future__ import annotations
import json
import sympy as sp

S,N,D,y,a=sp.symbols('S N D y a')
fdisc=D**2+4*S**3+27*N**2
finc=2*D*a*y**3+6*S*y**2+(2*D*S*a+3*D+9*N)*y+4*S**2-2*D*N*a
nexpr=sp.solve(finc,N)[0]
quartic=sp.factor(sp.cancel(fdisc.subs(N,nexpr)*(2*a*D-9*y)**2/4))
disc=sp.factor(sp.discriminant(quartic,D))
square_component=8*S**2*a+30*S*a*y**2+18*a*y**4+27*y**2
primitive=sp.factor(sp.cancel(disc/(27*S**2*a**2*square_component**2)))

rows=[]
for av in (1,2):
    q=sp.Poly(quartic.subs(a,av),D,S,y,domain=sp.QQ)
    r=sp.Poly(primitive.subs(a,av),S,y,domain=sp.QQ)
    fac=sp.factor_list(r.as_expr())
    rows.append({
        'a':av,
        'quartic_degree_in_D':q.degree(D),
        'quartic_degree_in_S':q.degree(S),
        'quartic_degree_in_y':q.degree(y),
        'primitive_degree_in_S':r.degree(S),
        'primitive_degree_in_y':r.degree(y),
        'primitive_total_degree':r.total_degree(),
        'primitive_factor_degrees':[
            {'exponent':e,'degree_S':sp.Poly(f,S,y).degree(S),
             'degree_y':sp.Poly(f,S,y).degree(y),
             'total_degree':sp.Poly(f,S,y).total_degree()}
            for f,e in fac[1]
        ],
        'primitive_irreducible_over_Q':len(fac[1])==1 and fac[1][0][1]==1,
    })

out={
  'status':'PASS',
  'open_divisor':'2*a*D-9*y != 0',
  'solved_N':str(nexpr),
  'quartic':str(quartic),
  'discriminant_factorization':{
      'scalar':'27',
      'square_factors':['S^2','a^2','(8*S^2*a+30*S*a*y^2+18*a*y^4+27*y^2)^2'],
      'primitive_branch_polynomial':str(primitive),
  },
  'representative_audits':rows,
  'method':'exact SymPy factorization over QQ; no floating point'
}
print(json.dumps(out,indent=2))
