# Exact Sage audit for QUARTIC_FACTORIAL_SIEVE.md

R.<d,x> = PolynomialRing(QQ,2,order='degrevlex')
g = x^3+d

def compose(f,h):
    return R(f(x=h))

g2 = compose(g,g)
g4 = compose(g2,g2)
quotient, remainder = (g4-x).quo_rem(g2-x)
assert remainder == 0
Phi4 = R(quotient)
assert Phi4.degree(x) == 72
assert Phi4.degree(d) == 24

D = Phi4.discriminant(x)
fac = D.factor()
meta = [(factor.degree(d), exponent) for factor, exponent in fac]
assert meta == [(4,2),(4,3),(16,4),(24,4)]

A4 = 729*d^4 + 1620*d^2 + 1000
B4 = 729*d^4 - 324*d^2 + 100
P16 = (
    282429536481*d^16 + 1757339338104*d^14 + 4642459719687*d^12
    + 6806074010589*d^10 + 6891783220746*d^8 + 5994132959232*d^6
    + 4118269132800*d^4 + 1739461754880*d^2 + 1073741824000
)
P24 = (
    150094635296999121*d^24 + 1200757082375992968*d^22
    + 4203267461712259335*d^20 + 8399740516065395253*d^18
    + 10909964351274746418*d^16 + 10526401881511556976*d^14
    + 8522156414444085612*d^12 + 5544611719418268000*d^10
    + 2750472027922567500*d^8 + 1314354779366400000*d^6
    + 459901255680000000*d^4 + 167772160000000000
)

assert D == A4^2 * B4^3 * P16^4 * P24^4

local = 4+27*d^2
for factor in (A4,B4,P16,P24):
    assert gcd(local,factor) == 1

# At the origin, the dynatomic and local discriminants are nonzero.
assert D(d=0) != 0
assert local(d=0) != 0

print('Phi4 degrees:',Phi4.degree(x),Phi4.degree(d))
print('discriminant factor metadata:',meta)
print('rotation-parity square class:',B4)
print('gcd(local,Disc Phi4)=',gcd(local,D))
print('PASS: quartic factorial ramification audit')
