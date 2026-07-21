# Exact Sage audit for local disjointness at dynatomic periods 2 and 3.

T.<t> = PolynomialRing(QQ)
K.<s> = NumberField(t^2+3)
R.<x> = PolynomialRing(K)

d = 2*s/9
g = x^3+d

def compose(f,h):
    return R(f(x=h))

g2 = compose(g,g)
g3 = compose(g2,g)

Phi2,rem2 = (g2-x).quo_rem(g-x)
Phi3,rem3 = (g3-x).quo_rem(g-x)
assert rem2 == 0
assert rem3 == 0
assert Phi2.degree() == 6
assert Phi3.degree() == 24
assert gcd(Phi2,Phi2.derivative()).degree() == 0
assert gcd(Phi3,Phi3.derivative()).degree() == 0
assert 4+27*d^2 == 0

print('period 2 degree/gcd:',Phi2.degree(),gcd(Phi2,Phi2.derivative()).degree())
print('period 3 degree/gcd:',Phi3.degree(),gcd(Phi3,Phi3.derivative()).degree())
print('PASS: local divisor is unramified at periods 2 and 3')
