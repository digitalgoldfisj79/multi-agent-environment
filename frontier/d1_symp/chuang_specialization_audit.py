#!/usr/bin/env python3
"""
End-to-end specialization audit for Chuang arXiv:2607.05757 at
(k,p)=(p,p) and (p-2,p), p == 2 mod 3.

This is a focused exact check. It:
  * computes the A' and A'' correction index sets in Theorems 4.18, 4.21, 4.22;
  * computes the dimensions of the two mu_3-invariant Airy trace spaces;
  * computes exact first symmetric-power traces in Z[zeta_p] for selected small primes.

No numerical floating point or broad prime sweep is used.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction


def vp(n: int, p: int) -> int:
    out = 0
    while n and n % p == 0:
        n //= p
        out += 1
    return out


def odd_correction_indices(k: int, p: int) -> list[int]:
    return [a for a in range(1, k // p + 1) if a % 2 == 1]


def odd_inertia_invariant_indices(k: int, p: int) -> list[int]:
    return [a for a in odd_correction_indices(k, p) if vp(a, p) % 6 == 5]


def motive_prime_dim(k: int) -> int:
    return (k + 1) // 2


def boundary_dim(k: int) -> int:
    # floor(k/3)+1-delta_{k == 1 mod 3}
    return k // 3 + 1 - int(k % 3 == 1)


def special_motive_prime_dim(k: int, p: int) -> int:
    # Theorem 4.18: subtract one Tate line for every odd a in [1,k/p].
    return motive_prime_dim(k) - len(odd_correction_indices(k, p))


def mu3_invariant_airy_dim(k: int, p: int) -> int:
    return special_motive_prime_dim(k, p) - boundary_dim(k)


def add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b)]


def sub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def scale(a: list[int], c: int) -> list[int]:
    return [c * x for x in a]


def mul_cyclic(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * p
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % p] += x * y
    return out


def cubic_sum_group_ring(p: int, u: int) -> list[int]:
    out = [0] * p
    for x in range(p):
        out[(x**3 + u * x) % p] += 1
    return out


def symmetric_trace(t: list[int], q: int, k: int, p: int) -> list[int]:
    one = [1] + [0] * (p - 1)
    if k == 0:
        return one
    if k == 1:
        return t
    hm2, hm1 = one, t
    for _ in range(2, k + 1):
        hm2, hm1 = hm1, sub(mul_cyclic(t, hm1, p), scale(hm2, q))
    return hm1


def cyclotomic_integer(v: list[int]) -> int:
    c = v[1]
    if any(x != c for x in v[1:]):
        raise ArithmeticError("result is not rational in Q(zeta_p)")
    return v[0] - c


def first_trace(p: int, k: int) -> int:
    total = [0] * p
    for u in range(p):
        # Airy local trace is minus the cubic exponential sum.
        t = scale(cubic_sum_group_ring(p, u), -1)
        total = add(total, symmetric_trace(t, p, k, p))
    return cyclotomic_integer(total)


@dataclass(frozen=True)
class Audit:
    p: int
    rank: int
    trace_p: int
    trace_pm2: int

    @property
    def twisted_trace_pm2(self) -> int:
        return self.p * self.trace_pm2

    @property
    def virtual_trace(self) -> int:
        return self.trace_p - self.twisted_trace_pm2

    @property
    def weight_scale(self) -> int:
        return self.p ** ((self.p + 1) // 2)


def audit(p: int) -> Audit:
    if p < 5 or p % 3 != 2:
        raise ValueError("p must be a prime-like integer >=5 with p == 2 mod 3")
    rank_p = mu3_invariant_airy_dim(p, p)
    rank_pm2 = mu3_invariant_airy_dim(p - 2, p)
    if rank_p != rank_pm2 or rank_p != (p - 5) // 6:
        raise AssertionError((p, rank_p, rank_pm2))
    if odd_correction_indices(p, p) != [1]:
        raise AssertionError("k=p must have exactly the a=1 correction")
    if odd_correction_indices(p - 2, p):
        raise AssertionError("k=p-2 must have no correction")
    if odd_inertia_invariant_indices(p, p):
        raise AssertionError("the a=1 A'' correction is not inertia invariant")
    return Audit(
        p=p,
        rank=rank_p,
        trace_p=first_trace(p, p),
        trace_pm2=first_trace(p, p - 2),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="*", type=int, default=[11, 17, 23, 29])
    args = parser.parse_args()
    for p in args.primes:
        result = audit(p)
        w = result.weight_scale
        print(
            f"p={p} rank={result.rank} "
            f"A'_corr(k=p)={odd_correction_indices(p,p)} "
            f"E'_inv(k=p)={odd_inertia_invariant_indices(p,p)}"
        )
        print(
            f"  tr_p={result.trace_p} "
            f"p*tr_pm2={result.twisted_trace_pm2} "
            f"virtual={result.virtual_trace}"
        )
        print(
            "  normalized="
            f"({Fraction(result.trace_p,w)}, "
            f"{Fraction(result.twisted_trace_pm2,w)}, "
            f"{Fraction(result.virtual_trace,w)})"
        )


if __name__ == "__main__":
    main()
