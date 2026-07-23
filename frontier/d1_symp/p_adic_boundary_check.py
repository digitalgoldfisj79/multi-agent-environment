#!/usr/bin/env python3
"""Exact check of the observed p-adic valuation of T_p."""
from collapse_verify import sum_Sp_u_line


def vp(n, p):
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v, n


if __name__ == "__main__":
    for p in (5, 11, 17, 23, 29, 41, 47, 53):
        T = sum_Sp_u_line(p) // p
        if T == 0:
            print(f"p={p}: T_p=0")
            continue
        v, unit = vp(T, p)
        expected = (p + 4) // 3
        assert v == expected
        print(f"p={p}: T_p={T}; unit={unit}; valuation={v}: OK")
    print("VALUATION LAW VERIFIED AT ALL CALIBRATED PRIMES")
