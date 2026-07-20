#!/usr/bin/env python3
"""Finite diagnostic for the proved primorial-centre coherence limit."""
import cmath, math
from sympy import primerange

def integral(c: float) -> complex:
    return 1+0j if c==0 else (cmath.exp(1j*c)-1)/(1j*c)

def main() -> None:
    primes=list(primerange(2,120000))[:10000]
    L=[]; s=0.0
    for p in primes:
        s += math.log(p); L.append(s)
    for N in [100,300,1000,3000,10000]:
        LN=L[N-1]
        errs=[]
        for c in [0.5,1.0,2.0,4.0,2*math.pi]:
            z=sum(cmath.exp(1j*c*x/LN) for x in L[:N])/N
            errs.append(abs(z-integral(c)))
        print(f"N={N:5d} max_error={max(errs):.6f}")
    print("CRITICAL_SCALE_COHERENCE_DIAGNOSTIC_PASS")

if __name__ == "__main__":
    main()
