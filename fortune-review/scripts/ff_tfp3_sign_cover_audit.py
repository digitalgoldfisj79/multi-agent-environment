#!/usr/bin/env python3
"""Exact symbolic audit of the cubic orientation identity and sign torsors."""
from __future__ import annotations
import itertools,json
import sympy as sp

def main()->None:
    a,b,c,e,t=sp.symbols('a b c e t')
    cubic=t**3+a*t**2+b*t+c; disc=sp.discriminant(cubic,t)
    numerator=((a*a-3*b)*t**2 +(a**3-sp.Rational(7,2)*a*b+sp.Rational(9,2)*c-sp.Rational(3,2)*e)*t +sp.Rational(1,2)*a*a*b+sp.Rational(3,2)*a*c-2*b*b-sp.Rational(1,2)*a*e)
    norm=sp.factor(sp.resultant(cubic,numerator,t))
    cofactor=sp.factor((norm-e**4)/(e**2-disc))
    expected=-sp.Rational(1,8)*(4*a**3*c-2*a**3*e-a**2*b**2-18*a*b*c+9*a*b*e+4*b**3+27*c**2-27*c*e+8*e**2)
    assert sp.factor(cofactor-expected)==0
    eA,eB,eC,eD,RAB,RAC,RCD,RBD,rho=sp.symbols('eA eB eC eD RAB RAC RCD RBD rho',nonzero=True)
    relations=[eA*RAB-RAC,eC*RCD-RAC,eB*RAB-rho**3*RBD,eD*RCD-rho**3*RBD]
    invariant=eA*eD-eB*eC
    groebner=sp.groebner(relations,RAC,RBD,RAB,RCD,eA,eB,eC,eD,rho)
    assert groebner.reduce(invariant*RAB*RCD)[1]==0
    signs=list(itertools.product((-1,1),repeat=4))
    torsors={k:[s for s in signs if s[0]*s[3]==k*s[1]*s[2]] for k in (-1,1)}
    assert len(torsors[-1])==len(torsors[1])==8
    assert set(torsors[-1]).isdisjoint(torsors[1])
    assert (1,1,1,1) in torsors[1] and (1,1,1,1) not in torsors[-1]
    print(json.dumps({
      'status':'TFP3_ORIENTATION_TORSOR_EXACT_PASS',
      'q_free_orientation_identity':'eA*eD=eB*eC',
      'kernel_size':8,
      'frobenius_base_invariant':'kappa=(etaA_F*etaD_F)/(etaB_F*etaC_F)',
      'relative_sign_equation':'sigmaA*sigmaD=kappa*sigmaB*sigmaC',
      'torsor_sizes':{'kappa_-1':8,'kappa_+1':8},
      'true_class_requirement':'kappa=+1 and sigma=(1,1,1,1)',
      'boundary':'The identity gives two eight-element sign torsors, not a globally regular degree-eight cover. Componentwise kappa, etaleness and monodromy remain open.',
    },indent=2,sort_keys=True))
if __name__=='__main__':main()
