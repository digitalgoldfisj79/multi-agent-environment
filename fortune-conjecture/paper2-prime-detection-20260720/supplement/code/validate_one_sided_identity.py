#!/usr/bin/env python3
"""Validate E_a = M(M-1) kappa_2 + R_a in random finite systems."""
import cmath, random

def h2(theta: float, P: list[int]) -> complex:
    return sum(cmath.exp(2j*cmath.pi*theta*(P[i]+P[j]))
               for i in range(len(P)) for j in range(i, len(P)))

def trial(seed: int) -> float:
    rng = random.Random(seed)
    n = rng.randint(4, 9)
    P=[1]
    for _ in range(1,n):
        P.append(P[-1]*rng.choice([5,7,11,13]))
    S=[P[i]+P[j] for i in range(n) for j in range(i,n)]
    M=len(S)
    qs=rng.sample([101,103,107,109,113,127,131,137],rng.randint(3,6))
    raw=[rng.random()+0.05 for _ in qs]
    z=sum(raw); weights=[x/z for x in raw]
    a=rng.randint(1,4)
    E=0.0
    for u,su in enumerate(S):
        for v,sv in enumerate(S):
            if u==v: continue
            psi=sum(w*cmath.exp(2j*cmath.pi*a*(su-sv)/q) for q,w in zip(qs,weights))
            E += abs(psi)**2
    R=0.0
    for iq,q in enumerate(qs):
        for ir,r in enumerate(qs):
            if iq==ir: continue
            R += weights[iq]*weights[ir]*(abs(h2(a*(1/q-1/r),P))**2-M)
    rhs=M*(M-1)*sum(w*w for w in weights)+R
    return abs(E-rhs)

def main() -> None:
    residuals=[trial(s) for s in range(80)]
    mx=max(residuals)
    print(f"trials={len(residuals)} max_residual={mx:.3e}")
    assert mx < 2e-8
    print("ONE_SIDED_IDENTITY_PASS")

if __name__ == "__main__":
    main()
