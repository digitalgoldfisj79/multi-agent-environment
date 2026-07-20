#!/usr/bin/env python3
"""Validate the exact pair-sum fourth-moment formula by integer counting."""
from collections import Counter
from sympy import primerange

def primorial_prefixes(n: int) -> list[int]:
    ps = list(primerange(2, 1000))[:n-1]
    out = [1]
    x = 1
    for p in ps:
        x *= p
        out.append(x)
    return out

def observed(n: int) -> int:
    P = primorial_prefixes(n)
    pair_sums = [P[i] + P[j] for i in range(n) for j in range(i, n)]
    counts = Counter(a+b for a in pair_sums for b in pair_sums)
    return sum(v*v for v in counts.values())

def expected(n: int) -> int:
    return n * (3*n**3 - 2*n**2 + 2*n - 1) // 2

def main() -> None:
    for n in range(2, 13):
        got, want = observed(n), expected(n)
        assert got == want, (n, got, want)
        print(f"N={n:2d} exact={got}")
    n = 55
    print(f"N=55 formula={expected(n)}")
    assert expected(n) == 13_562_560
    print("PAIR_SUM_FOURTH_MOMENT_PASS")

if __name__ == "__main__":
    main()
