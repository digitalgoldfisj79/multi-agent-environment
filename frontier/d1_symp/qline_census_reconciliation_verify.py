from fractions import Fraction
LED={11:dict(S0=-44,Schi=-66,Bp=0,Bm=6),17:dict(S0=34,Schi=-136,Bp=0,Bm=4),
     23:dict(S0=322,Schi=92,Bp=0,Bm=6),29:dict(S0=-232,Schi=-290,Bp=0,Bm=2),
     53:dict(S0=424,Schi=-954,Bp=0,Bm=0),71:dict(S0=-710,Schi=284,Bp=0,Bm=0)}

def mulcubic(u,phi3,f,p):           # u * phi, phi of degree<=3 -> O(n)
    n=len(f); out=[0]*(n+3)
    for k,ck in phi3:
        if ck:
            for i in range(n):
                if u[i]: out[i+k]=(out[i+k]+u[i]*ck)%p
    for i in range(n+2,n-1,-1):
        c=out[i]
        if c:
            out[i]=0
            for j in range(n):
                if f[j]: out[i-n+j]=(out[i-n+j]-c*f[j])%p
    return out[:n]

def irred(p,a,c,d):
    for x in range(p):
        if (pow(x,p,p)+a*x%p*x%p*x+c*x+d)%p==0: return False
    f=[d%p,c%p,0,a%p]+[0]*(p-4)
    phi3=[(0,(-d)%p),(1,(-c)%p),(3,(-a)%p)]
    X=[0,1]+[0]*(p-2); g=X[:]
    for _ in range(p):
        acc=[0]*p
        for i in range(p-1,-1,-1):
            acc=mulcubic(acc,phi3,f,p); acc[0]=(acc[0]+g[i])%p
        g=acc
    return g==X

def census(p,a): return sum(1 for c in range(p) for d in range(p) if irred(p,a,c,d))

print(f"{'p':>4} {'class':>6} {'census':>7} {'ledger':>7} {'match':>6} {'|dev|':>6} {'d_A':>5} {'ok?':>5}")
for p in (11,17,23,29):
    sq={x*x%p for x in range(1,p)}
    for A,a,B in ((+1,1,LED[p]['Bp']),(-1,next(x for x in range(2,p) if x not in sq),LED[p]['Bm'])):
        S=LED[p]['S0']+A*LED[p]['Schi']; C=p-2+B
        N=Fraction(C)-Fraction(S,2*p); dev=abs(Fraction(S,2*p)); dA=min(C,2*p-C)
        cen=census(p,a)
        print(f"{p:>4} {A:>+6} {cen:>7} {str(N):>7} {'YES' if N==cen else 'NO':>6} "
              f"{str(dev):>6} {dA:>5} {'PASS' if dev<dA else 'FAIL':>5}")
