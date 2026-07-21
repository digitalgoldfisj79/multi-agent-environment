# Exact characteristic-zero audit for QUARTIC_LOCAL_INCIDENCE.md
# Run with SageMath.

# 1. Base ordered-cycle surface.
R.<x0,x1,x2,x3,c,d> = PolynomialRing(QQ, order='degrevlex')
xs = [x0,x1,x2,x3]
eqs = [xs[(i+1)%4] + xs[i]^3 + c*xs[i] + d for i in range(4)]
vdm = prod(xs[i]-xs[j] for i in range(4) for j in range(i+1,4))
I = ideal(eqs).saturation(ideal(vdm))[0]
assert I.dimension() == 2
assert I.is_prime()
assert len(I.associated_primes()) == 1
print('BASE_DIM', I.dimension())
print('BASE_PRIME', I.is_prime())
print('BASE_ASS', len(I.associated_primes()))

# 2. Local-root cover.
S.<x0,x1,x2,x3,c,d,z> = PolynomialRing(QQ, order='degrevlex')
xs = [x0,x1,x2,x3]
eqs = [xs[(i+1)%4] + xs[i]^3 + c*xs[i] + d for i in range(4)]
vdm = prod(xs[i]-xs[j] for i in range(4) for j in range(i+1,4))
root = z^3 + (c+1)*z + d
J = ideal(eqs + [root]).saturation(ideal(vdm))[0]
assert J.dimension() == 2
assert J.is_prime()
assert len(J.associated_primes()) == 1
print('ROOT_DIM', J.dimension())
print('ROOT_PRIME', J.is_prime())
print('ROOT_ASS', len(J.associated_primes()))

# 3. Triple-root locus.
T.<x0,x1,x2,x3,c,d> = PolynomialRing(QQ, order='degrevlex')
xs = [x0,x1,x2,x3]
eqs = [xs[(i+1)%4] + xs[i]^3 + c*xs[i] + d for i in range(4)]
vdm = prod(xs[i]-xs[j] for i in range(4) for j in range(i+1,4))
K = ideal(eqs + [c+1,d]).saturation(ideal(vdm))[0]
assert K.dimension() == 0
print('TRIPLE_DIM', K.dimension())
print('TRIPLE_ASS', len(K.associated_primes()))

# 4. Cyclic Fourier elimination and square-class specialisation.
P.<B> = PolynomialRing(QQ)
h = 32*B^4 - 76*B^2 + 33
assert h.is_irreducible()
N.<bb> = NumberField(h)
B = bb
C = QQ(2)
A = -(4*B^3*C - B*C^3 - B*C + 2*B - C^3 - C^2 + C - 1) / (
    3*C*(2*B-C-1)*(2*B+C-1)
)
x0 = A+B+C
x1 = A-B+1
x2 = A+B-C
c = -((x2+x1^3) - (x1+x0^3))/(x1-x0)
d = -(x1+x0^3) - c*x0

Delta = -4*(c+1)^3 - 27*d^2
Fplus = 4*c^3 + 12*c^2 + 9*c + 27*d^2
Fminus = 4*c^3 - 12*c^2 + 9*c + 27*d^2
weights = [
    ('Delta', Delta),
    ('Fplus', Fplus),
    ('Fminus', Fminus),
    ('cFplus', c*Fplus),
    ('cFminus', c*Fminus),
    ('DeltaFplus', Delta*Fplus),
    ('DeltaFminus', Delta*Fminus),
    ('cDeltaFplus', c*Delta*Fplus),
    ('cDeltaFminus', c*Delta*Fminus),
]
for name, weight in weights:
    assert not weight.is_square()
    print(name, 'SQUARE', weight.is_square())

print('PASS: quartic cycle geometry audit')
