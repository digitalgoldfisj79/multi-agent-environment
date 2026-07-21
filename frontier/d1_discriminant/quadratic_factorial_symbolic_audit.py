import sympy as sp


x, y, z = sp.symbols("x y z")
a = sp.symbols("a", nonzero=True)

Q = x * x - x * y + y * y
C = (x - 2 * y) * (x + y) * (2 * x - y)
c = 2 - a * Q / sp.Integer(3)
d = a * C / sp.Integer(27)
U = (c + 1) / a
W = d / a
Delta = sp.factor(-4 * U**3 - 27 * W**2)
P = 3 * a * d**2 + c + sp.Rational(4, 9) * c**3
T = sp.Rational(4, 3) * c**2
Fplus = sp.factor(P + T)
Fminus = sp.factor(P - T)

A = x * x - 4 / a
B = y * y - 4 / a
Cq = (x - y) ** 2 - 4 / a

# The local-root incidence surface is geometrically irreducible at a=1.
Gnum = sp.together(z**3 + U * z + W).as_numer_denom()[0]
G1 = sp.Poly(sp.expand(Gnum.subs(a, 1)), x, y, z)
factors = sp.factor_list(G1.as_expr())[1]
assert len(factors) == 1 and factors[0][1] == 1

# The local triple-root equations have finite intersection.
Unum = sp.Poly(sp.together(U.subs(a, 1)).as_numer_denom()[0], x, y)
Wnum = sp.Poly(sp.together(W).as_numer_denom()[0], x, y)
assert sp.gcd(Unum, Wnum).total_degree() == 0

# One affine line gives exact nonsquareness and coprimality certificates.
substitution = {a: 1, y: 2 * x + 1}
raw = {
    "A": A,
    "B": B,
    "C": Cq,
    "Delta": Delta,
    "Fplus": Fplus,
    "Fminus": Fminus,
    "c": c,
}
polynomials = {}

for name, expression in raw.items():
    numerator = sp.expand(
        sp.together(expression.subs(substitution)).as_numer_denom()[0]
    )
    polynomial = sp.Poly(numerator, x)
    polynomials[name] = polynomial
    line_factors = sp.factor_list(polynomial.as_expr())[1]
    assert line_factors
    assert all(exponent == 1 for _, exponent in line_factors), (
        name,
        line_factors,
    )

names = list(polynomials)
for i, name in enumerate(names):
    for other in names[i + 1 :]:
        assert sp.gcd(polynomials[name], polynomials[other]).degree() == 0, (
            name,
            other,
        )

expected = {
    "A": (x - 2) * (x + 2),
    "B": (2 * x - 1) * (2 * x + 3),
    "C": (x - 1) * (x + 3),
    "Delta": (
        4 * x**6
        + 12 * x**5
        - 23 * x**4
        - 66 * x**3
        + 49 * x**2
        + 84 * x
        - 76
    ),
    "Fplus": -27
    * (
        4 * x**6
        + 12 * x**5
        - 23 * x**4
        - 66 * x**3
        + 46 * x**2
        + 81 * x
        - 67
    ),
    "Fminus": -9
    * (
        12 * x**6
        + 36 * x**5
        + 3 * x**4
        - 54 * x**3
        - 30 * x**2
        + 3 * x
        - 1
    ),
    "c": -(3 * x**2 + 3 * x - 5),
}

for name, expression in expected.items():
    assert sp.rem(polynomials[name], sp.Poly(expression, x)).is_zero
    assert polynomials[name].degree() == sp.degree(expression, x)

print("PASS: quadratic-factorial genericity certificate")
print("root surface:", G1.as_expr())
for name in names:
    print(name, sp.factor(polynomials[name].as_expr()))
