#!/usr/bin/env python3
# Exact symbolic audit of the cubic Frobenius-sign cover.
from __future__ import annotations
import json
import sympy as sp

def main() -> None:
    a,b,c,e,t=sp.symbols("a b c e t")
    cubic=t**3+a*t**2+b*t+c
    disc=sp.discriminant(cubic,t)
    numerator=(
        (a*a-3*b)*t**2
        +(a**3-sp.Rational(7,2)*a*b+sp.Rational(9,2)*c-sp.Rational(3,2)*e)*t
        +sp.Rational(1,2)*a*a*b+sp.Rational(3,2)*a*c-2*b*b-sp.Rational(1,2)*a*e
    )
    norm=sp.factor(sp.resultant(cubic,numerator,t))
    cofactor=sp.factor((norm-e**4)/(e**2-disc))
    expected=-sp.Rational(1,8)*(
        4*a**3*c-2*a**3*e-a**2*b**2-18*a*b*c+9*a*b*e
        +4*b**3+27*c**2-27*c*e+8*e**2
    )
    assert sp.factor(cofactor-expected)==0
    eA,eB,eC,eD,RAB,RAC,RCD,RBD,rho=sp.symbols(
        "eA eB eC eD RAB RAC RCD RBD rho", nonzero=True
    )
    relations=[
        eA*RAB-RAC,
        eC*RCD-RAC,
        eB*RAB-rho**3*RBD,
        eD*RCD-rho**3*RBD,
    ]
    invariant=eA*eD-eB*eC
    groebner=sp.groebner(relations,RAC,RBD,RAB,RCD,eA,eB,eC,eD,rho)
    assert groebner.reduce(invariant*RAB*RCD)[1]==0
    signs=[
        s for s in __import__("itertools").product((-1,1),repeat=4)
        if s[0]*s[3]==s[1]*s[2]
    ]
    assert len(signs)==8 and (1,1,1,1) in signs
    print(json.dumps({
        "status":"TFP3_SIGN_COVER_EXACT_PASS",
        "norm_factorization":str(sp.factor(norm-e**4)),
        "orientation_invariant":"eA*eD=eB*eC",
        "sign_cover_size":len(signs),
        "true_sign_class":[1,1,1,1],
        "boundary":"This proves the eight-class cover, not its componentwise monodromy or point density.",
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
