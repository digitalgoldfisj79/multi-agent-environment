#!/usr/bin/env python3
"""Symbolic genericity certificate for the oriented cubic incidence theorem.

Requires SymPy. The audit works at the exact characteristic-zero point

    a = 1, b = 0, W0 = 2*i,

which lies on W0^2 + 27 b^2 + 4 = 0. It verifies:

1. the oriented-plane discriminant relation;
2. irreducibility of the shifted root-incidence surface;
3. nonsquareness of every plane character weight needed for the unsigned
   and signed cubic incidence sums, using the exact line y=1;
4. coprimality of the local triple-root equations.

One good point proves that the corresponding conditions hold on a nonempty
Zariski-open subset of the base conic. The complement is finite.
"""

from __future__ import annotations

import sympy as sp


I = sp.I
x, y, z = sp.symbols("x y z")
a, b, w = sp.symbols("a b w", nonzero=True)
u, v, V = sp.symbols("u v V", nonzero=True)

half = sp.Rational(1, 2)
Q = x**2 - x * y + y**2
R = x**3 + y**3 - sp.Rational(3, 2) * x * y * (x + y)
S = x * y * (x - y)

u_plane = Q
v_plane = sp.expand(b * R + w * half * S)
V_plane = sp.expand(w * R - sp.Rational(27, 2) * b * S)

# Exact invariant relation modulo the base conic.
relation = V_plane**2 + 4 * u_plane**3 + 27 * v_plane**2
remainder = sp.rem(
    sp.Poly(relation, w),
    sp.Poly(w**2 + 27 * b**2 + 4, w),
).as_expr()
assert sp.expand(remainder) == 0

c = a * u + (V + 9 * v) / (2 * V) - 3 * u**2 / (a * V**2)
d = (
    a * v
    - u**2 / V
    + 3 * u / (2 * a * V)
    + 9 * u * v / (2 * a * V**2)
    - 2 * u**3 / (a**2 * V**3)
)

u_local = (c + 1) / a
v_local = d / a
Delta_local = -4 * u_local**3 - 27 * v_local**2
Delta_num, _ = sp.together(Delta_local).as_numer_denom()

P = 3 * a * d**2 + c + sp.Rational(4, 9) * c**3
T = sp.Rational(4, 3) * c**2
Fplus_num, _ = sp.together(P + T).as_numer_denom()
Fminus_num, _ = sp.together(P - T).as_numer_denom()
c_num, _ = sp.together(c).as_numer_denom()
c1_num, _ = sp.together(c + 1).as_numer_denom()
d_num, _ = sp.together(d).as_numer_denom()

special = {u: u_plane, v: v_plane, V: V_plane, a: 1, b: 0, w: 2 * I}

# Shifted root-incidence surface.
G = sp.expand(
    2 * a * V_plane * (z**3 + u_plane * z + v_plane)
    - 6 * u_plane * z**2
    + (3 * V_plane + 9 * v_plane) * z
    - 4 * u_plane**2
)
G0 = sp.expand(G.subs({a: 1, b: 0, w: 2 * I}))
G_factors = sp.factor_list(G0, extension=I)[1]
assert len(G_factors) == 1
assert G_factors[0][1] == 1
assert sp.total_degree(G_factors[0][0]) == 6

# A square polynomial remains square after every nonzero specialization.
# The line y=1 therefore gives an exact nonsquareness certificate.
raw = {
    "c": c_num,
    "DeltaH": Delta_num,
    "Fplus": Fplus_num,
    "Fminus": Fminus_num,
}
line_polys: dict[str, sp.Poly] = {}
for name, expression in raw.items():
    value = sp.expand(expression.subs(special).subs(y, 1))
    line_polys[name] = sp.Poly(value, x, extension=I)

# c is a distinct nonsquare factor.
c_factor_meta = [
    (sp.degree(f, x), exponent)
    for f, exponent in sp.factor_list(line_polys["c"].as_expr(), x, extension=I)[1]
]
assert any(exponent % 2 for _, exponent in c_factor_meta)

# DeltaH and F+/- have a common square boundary factor and distinct
# degree-18 factors of odd multiplicity.
for name in ("DeltaH", "Fplus", "Fminus"):
    meta = [
        (sp.degree(f, x), exponent)
        for f, exponent in sp.factor_list(line_polys[name].as_expr(), x, extension=I)[1]
    ]
    assert (18, 1) in meta

assert sp.degree(sp.gcd(line_polys["c"], line_polys["DeltaH"])) == 0
assert sp.degree(sp.gcd(line_polys["c"], line_polys["Fplus"])) == 0
assert sp.degree(sp.gcd(line_polys["c"], line_polys["Fminus"])) == 0

for left, right in (("DeltaH", "Fplus"), ("DeltaH", "Fminus"), ("Fplus", "Fminus")):
    common = sp.gcd(line_polys[left], line_polys[right])
    # Only the three doubled boundary roots are common.
    assert sp.degree(common) == 6
    common_meta = [
        (sp.degree(f, x), exponent)
        for f, exponent in sp.factor_list(common.as_expr(), x, extension=I)[1]
    ]
    assert common_meta == [(1, 2), (1, 2), (1, 2)]

# Therefore all raw weights
# F+-, cF+-, DeltaH F+-, c DeltaH F+-
# are nonsquares at this specialization.
for f_name in ("Fplus", "Fminus"):
    for use_c in (False, True):
        for use_delta in (False, True):
            poly = line_polys[f_name]
            if use_c:
                poly *= line_polys["c"]
            if use_delta:
                poly *= line_polys["DeltaH"]
            factors = sp.factor_list(poly.as_expr(), x, extension=I)[1]
            assert any(exponent % 2 for _, exponent in factors)

# The triple-root equations c+1=0 and d=0 have no common component.
C1 = sp.Poly(sp.expand(c1_num.subs(special)), x, y, extension=I)
D0 = sp.Poly(sp.expand(d_num.subs(special)), x, y, extension=I)
assert sp.gcd(C1, D0).total_degree() == 0

print("PASS: oriented cubic genericity certificate")
print("root surface degree:", sp.total_degree(G0))
print("c line factors:", c_factor_meta)
for name in ("DeltaH", "Fplus", "Fminus"):
    print(
        name,
        [
            (sp.degree(f, x), exponent)
            for f, exponent in sp.factor_list(line_polys[name].as_expr(), x, extension=I)[1]
        ],
    )
