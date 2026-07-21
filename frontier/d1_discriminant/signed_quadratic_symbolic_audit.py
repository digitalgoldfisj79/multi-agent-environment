#!/usr/bin/env python3
"""Symbolic nonsquare-fibre audit for SIGNED_QUADRATIC_INCIDENCE.md.

Requires SymPy. It verifies the discriminants, pairwise coprimality, and
exceptional-polynomial degrees used in the one-variable Weil bounds.
"""

import sympy as sp

D, S, w, t = sp.symbols("D S w t")

L = D + 3*S - 4
Up = (
    D**3 - 18*D**2*S - 24*D**2
    + 81*D*S**2 - 360*D*S + 180*D + 108*S - 400
)
Um = (
    D**3 - 18*D**2*S
    + 81*D*S**2 - 216*D*S - 12*D
    + 216*S**2 - 468*S - 16
)
Q = (
    D**3 - 18*D**2*S - 24*D**2
    + 81*D*S**2 - 360*D*S + 192*D + 144*S - 512
)

assert sp.expand(
    sp.discriminant(Up, S) - 1296*(2*D+1)**2*(4*D+9)
) == 0
assert sp.expand(
    sp.discriminant(Um, S) - 432*(2*D+7)**2*(4*D+11)
) == 0
assert sp.expand(
    sp.discriminant(Q, S) - 20736*(D+1)**3
) == 0

complete = {"S": S, "L": L, "Up": Up, "Um": Um, "Q": Q}
for name, f in complete.items():
    assert sp.Poly(f, S).is_sqf, name
for i, (name1, f1) in enumerate(complete.items()):
    for name2, f2 in list(complete.items())[i+1:]:
        assert sp.gcd(f1, f2) == 1, (name1, name2)

E_complete = sp.prod([
    D, 3*D+8, D-4, D-10, D+2, D-8,
    2*D+1, 4*D+9, 2*D+7, 4*D+11, D+1,
    D**3-12*D-20,
    D**3-8*D**2-12*D-4,
    64*D**6-48*D**5-1431*D**4-424*D**3
        +13524*D**2+32220*D+25216,
])
assert sp.degree(E_complete, D) == 23

Lr = t**2 + t*w - 3*t + w**2 - 3*w
A1 = t*w - t - w
A2 = (
    t**3*w - 3*t**3
    + 2*t**2*w**2 - 15*t**2*w + 25*t**2
    + t*w**3 - 9*t*w**2 + 20*t*w
    - w**3 + 4*w**2
)
B = (
    8*t**5 + 3*t**4*w**2 + 4*t**4*w - 39*t**4
    + 6*t**3*w**3 - 30*t**3*w**2 + 33*t**3*w - 3*t**3
    + 3*t**2*w**4 - 20*t**2*w**3
    + 36*t**2*w**2 + 9*t**2*w
    + 2*t*w**4 - 6*t*w**3
    + 3*w**4 - 12*w**3
)

assert sp.expand(sp.discriminant(Lr, t) + 3*(w-3)*(w+1)) == 0
assert sp.expand(
    sp.discriminant(A2, t)
    + w**3*(w-4)*(2*w-7)**2*(4*w**3-37*w**2+122*w-125)
) == 0

H10 = (
    288*w**10-8376*w**9+105068*w**8-740793*w**7
    +3204594*w**6-8696455*w**5+14466060*w**4
    -13610007*w**3+5822658*w**2-378513*w-3564
)
assert sp.expand(
    sp.discriminant(B, t)
    - 27*w**7*(w-5)**2*(2*w-1)**2*(2*w**2-22*w+63)**2*H10
) == 0

root = {"t": t, "A1": A1, "A2": A2, "B": B, "Lr": Lr}
for name, f in root.items():
    assert sp.Poly(f, t).is_sqf, name
for i, (name1, f1) in enumerate(root.items()):
    for name2, f2 in list(root.items())[i+1:]:
        assert sp.gcd(f1, f2) == 1, (name1, name2)

E_root = sp.prod([
    w, w-1, w-3, w+1, w-4, 2*w-7,
    4*w**3-37*w**2+122*w-125,
    w-5, 2*w-1, 2*w**2-22*w+63, H10,
    2*w**2-10*w+9, w-2, w**2-8*w+18,
])
assert sp.degree(E_root, w) == 28

print("COMPLETE exceptional degree:", sp.degree(E_complete, D))
print("ROOT exceptional degree:", sp.degree(E_root, w))
print("SYMBOLIC NONSQUARE-FIBRE AUDIT PASSED")
