import itertools, cmath, math
from itertools import product as prod

p = 5

def polmulmod(a, b, f, p):
    res = [0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                res[i+j] = (res[i+j] + ai*bj) % p
    d = len(f)-1
    while len(res) > d:
        c = res.pop()
        if c:
            for k in range(d):
                res[len(res)-d+k] = (res[len(res)-d+k] - c*f[k]) % p
    while len(res) < d: res.append(0)
    return tuple(res)

def is_irred(coeffs, p):
    d = len(coeffs)-1
    f = coeffs
    x = tuple([0,1]+[0]*(d-2))
    def fpow(a,e):
        r = tuple([1]+[0]*(d-1)); base=a
        while e:
            if e&1: r = polmulmod(list(r), list(base), f, p)
            base = polmulmod(list(base), list(base), f, p)
            e >>= 1
        return r
    t = x
    for k in range(1, d):
        t = fpow(t, p)
        if t == x: return False
    return fpow(t, p) == x

# N(5) brute force
N5 = [d for d in range(5) if is_irred([d,0,1,0,0,1],5)]
print("N(5) witnesses:", N5, "N(5) =", len(N5))

# field F_{5^5}
f = None
for cand in prod(range(5), repeat=5):
    c = list(cand)+[1]
    if is_irred(c,5):
        f = c; break
print("field poly:", f)
d = 5; Q = 5**5
elts = list(prod(range(5), repeat=5))
zero = (0,)*5; one = (1,0,0,0,0)

def mul(a,b): return polmulmod(list(a),list(b),f,5)
def power(a,e):
    r = one; base = a
    while e:
        if e&1: r = mul(r,base)
        base = mul(base,base)
        e >>= 1
    return r
def tr(a):
    s=[0]*5; t=a
    for k in range(5):
        for i in range(5): s[i]=(s[i]+t[i])%5
        t = power(t,5)
    assert all(c==0 for c in s[1:]), (a,s)
    return s[0]
half = (Q-1)//2
def eta(a): return 1 if power(a,half)==one else -1
e5 = lambda k: cmath.exp(2j*math.pi*(k%5)/5)
inv4 = pow(4,-1,5)

# S(5)
S = 0; ker = 0
for a in elts:
    if a==zero or tr(a)!=0: continue
    ker += 1
    S += eta(a)*e5((-inv4*tr(power(a,Q-1-3)))%5)
print("ker Tr nonzero size:", ker)
print("S(5) =", S, " |S| vs 5^2.5 =", 5**2.5)

# Gauss sum G_5: eta_p quadratic residue char of F_5
sq = {pow(s,2,5) for s in range(1,5)}
G5 = sum((1 if t in sq else -1)*e5(t) for t in range(1,5))
GQ = G5**5
m1 = (4,0,0,0,0)
print("G_5 =", G5, "G_Q =", GQ, "eta(-1) =", eta(m1))
print("S vs eta(-1)*GQ*N:", eta(m1)*GQ*len(N5))
print("N vs p^-p GQ S:", 5**-5*GQ*S)

# T_u and R(u)
def Ru(u):
    cnt=0
    for a in elts:
        v = power(a,5); v2 = mul(a,a)
        s = tuple((v[i]+v2[i]+(u if i==0 else 0))%5 for i in range(5))
        if s==zero: cnt+=1
    return cnt
Rs=[]
for u in range(5):
    T=0
    for a in elts:
        if a==zero: continue
        val = (tr(tuple((u*x)%5 for x in a)) - inv4*tr(power(a,Q-1-3))) % 5
        T += eta(a)*e5(val)
    R = Ru(u); Rs.append(R)
    pred = eta(m1)*GQ*(R-1)
    print(f"u={u}: T_u={T:.6f} pred={pred:.6f} R={R} diff={abs(T-pred):.2e}")
print("R values:", Rs, "sum(R-1) =", sum(r-1 for r in Rs), "= p*N?", 5*len(N5))

# Newton identity equivalence check: e_1..e_K all 0 <=> p_1..p_K all 0 mod p, K=p-3, k<p
import random
def check_newton(pp, K):
    random.seed(2)
    for trial in range(2000):
        e = [0]+[random.randrange(pp) for _ in range(K)]
        # Newton: p_k = e1 p_{k-1} - e2 p_{k-2} + ... + (-1)^{k-1} k e_k  (mod pp), k <= n
        P=[0]*(K+1)
        for k in range(1,K+1):
            s = sum((-1)**(i-1)*e[i]*P[k-i] for i in range(1,k)) + (-1)**(k-1)*k*e[k]
            P[k]=s%pp
        ez = all(x==0 for x in e[1:]); pz = all(x==0 for x in P[1:])
        if ez!=pz: return False
        # also check partial: e_1..e_j = 0 iff p_1..p_j = 0 (triangular, k invertible since k<pp)
        for j in range(1,K+1):
            if all(x==0 for x in e[1:j+1]) != all(x==0 for x in P[1:j+1]): return False
    return True
for pp in (5,7,11,13):
    print(f"Newton triangular equivalence p={pp}, K={pp-3}:", check_newton(pp, pp-3))

# Moisio Cor 6.2 verification q=p=5, m=5: k_n(c) = sum over n vars x_i in F_q^*: e_q(x1+..+xn + c/(x1..xn))
def kln(n, c, q=5):
    tot=0
    for xs in prod(range(1,q), repeat=n):
        pr=1
        for x in xs: pr=pr*x%q
        tot += e5(sum(xs) + c*pow(pr,-1,q))
    return tot
def brute_P(a,b):
    cnt=0
    for cs in prod(range(5), repeat=5):
        c0,c1,c2,c3,c4 = cs
        # p(x) = x^5 - a x^4 + ... + (-1)^5 b => coeff x^4 = -a, const = -b
        if (-c4)%5 != a%5: continue
        if (-c0)%5 != b%5: continue
        if is_irred([c0,c1,c2,c3,c4,1],5): cnt+=1
    return cnt
for (a,b) in [(1,1),(2,3),(4,2)]:
    P = brute_P(a,b)
    c = b*pow(pow(a,5,5),-1,5)%5
    rhs = (5**4-1)//4 + (-1)**4*kln(3,c)
    print(f"(a,b)=({a},{b}): m*P={5*P}, rhs={rhs.real:.6f}+{rhs.imag:.2e}i")
