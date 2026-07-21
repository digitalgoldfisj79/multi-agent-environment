# Exact Sage audit for QUINTIC_LOCAL_INCIDENCE.md

T.<t> = PolynomialRing(QQ)
K.<s> = NumberField(t^2+3)
R.<x> = PolynomialRing(K)

d = 2*s/9
g = x^3+d

def compose(f,h):
    return R(f(x=h))

g2 = compose(g,g)
g3 = compose(g2,g)
g4 = compose(g3,g)
g5 = compose(g4,g)

Phi5,remainder = (g5-x).quo_rem(g-x)
assert remainder == 0
assert Phi5.degree() == 240
assert gcd(Phi5,Phi5.derivative()).degree() == 0
assert 4+27*d^2 == 0

print('Phi5 degree:',Phi5.degree())
print('gcd degree:',gcd(Phi5,Phi5.derivative()).degree())
print('PASS: local discriminant divisor is not period-five ramification')
