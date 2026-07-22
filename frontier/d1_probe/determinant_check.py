#!/usr/bin/env python3
"""Independent verification of the phase-report Cartier determinant theorem.

Claim:  A_p(G)_{n,e} = [X^e] G(X)^n,  G = a X^3 + c X + d,
        rows n = 1..p-1,  cols e in {0,...,p-1} \ {p-3},
        det A_p(G) = - c^{p(p-3)/2} d^{p-3} ((p-3) a d^2 - c^3)  in F_p.

Result: CONFIRMED for p = 5,7,11,13,17,19,23,29 (random a in F_p^*, c,d in F_p).
Also: the (1,2)-weighted degree (wt c=1, d=2, a=0) is exactly (p^2+p-4)/2,
matching the report, sitting (p-3)/2 above (p^2-1)/2.
"""
from sympy import symbols, Poly, Matrix
import random

def det_Ap(p, a, c, d):
    X = symbols('X')
    Gp = Poly(a*X**3 + c*X + d, X)
    cols = [e for e in range(p) if e != p-3]
    Gpow = [Poly(1, X)]
    for _ in range(1, p):
        Gpow.append(Gpow[-1]*Gp)
    rows = [[Gpow[n].as_dict().get((e,), 0) for e in cols] for n in range(1, p)]
    return int(Matrix(rows).det()) % p

def formula(p, a, c, d):
    return (-pow(c, p*(p-3)//2, p) * pow(d, p-3, p)
            * (((p-3)*a*d*d - c**3))) % p

if __name__ == "__main__":
    random.seed(1)
    for p in [5, 7, 11, 13, 17, 19, 23, 29]:
        ok = all(det_Ap(p, a, c, d) == formula(p, a, c, d)
                 for a, c, d in [(random.randint(1, p-1), random.randint(0, p-1),
                                  random.randint(0, p-1)) for _ in range(6)])
        deg = p*(p-3)//2 + 2*(p-3) + 4
        print(f"p={p:>3}: formula {'OK' if ok else 'FAIL'};  "
              f"(1,2)-deg={deg}=(p^2+p-4)/2={(p*p+p-4)//2}, "
              f"excess over (p^2-1)/2 = {deg-(p*p-1)//2}")
