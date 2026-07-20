#!/usr/bin/env python3
"""Validate exact reconstruction of a length-H Fourier sum from A translates."""
import cmath

def main() -> None:
    mx=0.0; cases=0
    for H in range(12,121):
        for A in range(2,13):
            if H % A: continue
            h=H//A
            for q in [H+1,2*H+3,3*H+7]:
                for a in range(-7,8):
                    left=sum(sum(cmath.exp(2j*cmath.pi*a*m/q) for m in range(b*h,(b+1)*h)) for b in range(A))
                    right=sum(cmath.exp(2j*cmath.pi*a*m/q) for m in range(H))
                    mx=max(mx,abs(left-right)); cases+=1
    print(f"cases={cases} max_residual={mx:.3e}")
    assert mx < 2e-11
    print("FOURIER_SCALE_CONSERVATION_PASS")

if __name__ == "__main__":
    main()
