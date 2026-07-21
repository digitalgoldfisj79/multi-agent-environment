import itertools, sys
sys.setrecursionlimit(10000)

# polynomials over F_p as tuples of coeffs low->high, normalized (no trailing zeros)
def norm(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return tuple(a)
def add(a,b,p):
    n=max(len(a),len(b)); return norm([( (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) )%p for i in range(n)])
def mul(a,b,p):
    if not a or not b: return ()
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                r[i+j]=(r[i+j]+x*y)%p
    return norm(r)
def divmod_poly(a,b,p):
    a=list(a); db=len(b)-1; lb=b[-1]; inv=pow(lb,p-2,p); q=[0]*(max(len(a)-db,0))
    while len(a)-1>=db and any(a):
        if a[-1]==0: a.pop(); continue
        d=len(a)-1-db; c=(a[-1]*inv)%p; q[d]=c
        for i,y in enumerate(b):
            a[d+i]=(a[d+i]-c*y)%p
        while a and a[-1]==0: a.pop()
    return norm(q), norm(a)
def mod(a,b,p): return divmod_poly(a,b,p)[1]
def gcd(a,b,p):
    while b: a,b=b,mod(a,b,p)
    if a:
        inv=pow(a[-1],p-2,p); a=tuple((c*inv)%p for c in a)
    return a
def powmod(a,e,f,p):
    r=(1,); a=mod(a,f,p)
    while e:
        if e&1: r=mul(r,a,p); r=mod(r,f,p)
        a=mul(a,a,p); a=mod(a,f,p); e>>=1
    return r
def frob_pow(x, k, f, p):
    # x^(p^k) mod f
    for _ in range(k): x=powmod(x,p,f,p)
    return x
def primes_of(n):
    s=set(); d=2; m=n
    while d*d<=m:
        while m%d==0: s.add(d); m//=d
        d+=1
    if m>1: s.add(m)
    return s
def is_irred(f,p):
    n=len(f)-1
    if n<=0: return False
    if n==1: return True
    T=(0,1)
    x=frob_pow(T,n,f,p)
    if add(x,tuple((-c)%p for c in T),p): return False
    for r in primes_of(n):
        y=frob_pow(T,n//r,f,p)
        g=gcd(f, add(y,tuple((-c)%p for c in T),p), p)
        if g!=(1,): return False
    return True

def all_monic_irred(p,d):
    # list monic irreducibles of degree <= d
    out=[]
    for e in range(1,d+1):
        for coeffs in itertools.product(range(p),repeat=e):
            f=tuple(coeffs)+(1,)
            if is_irred(f,p): out.append(f)
    return out

def fortunate(p,d,maxdeg):
    irr=all_monic_irred(p,d)
    P=(1,)
    for f in irr: P=mul(P,f,p)
    n=len(P)-1
    nd=sum((e)*sum(1 for f in irr if len(f)-1==e) for e in range(1,d+1))
    assert n==nd
    for degm in range(1,maxdeg+1):
        for coeffs in itertools.product(range(p),repeat=degm+1):
            if coeffs[-1]==0: continue
            m=tuple(coeffs)
            cand=add(P,m,p)
            if is_irred(cand,p):
                return n, degm, m, is_irred(m,p)
    return n, None, None, None

cases=[(2,3),(2,4),(3,2),(3,3),(5,2),(3,1),(5,1),(7,1),(11,1),(13,1)]
for (p,d) in cases:
    n,degF,m,mirr=fortunate(p,d,2*d+2)
    print(f"p={p} d={d} n={n} degF={degF} bound2d+1={2*d+1} F_irred={mirr} m={m}")
