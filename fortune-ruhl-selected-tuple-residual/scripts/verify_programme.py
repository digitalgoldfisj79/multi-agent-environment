#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    x = n
    p = 2
    parity = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def von_mangoldt(n: int) -> float:
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, int(math.isqrt(p)) + 1)):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return math.log(p)
    return 0.0


def convolution(f: list[float], g: list[float], N: int) -> list[float]:
    h = [0.0] * (N + 1)
    for n in range(1, N + 1):
        h[n] = sum(f[d] * g[n // d] for d in divisors(n))
    return h


def heath_brown_values(N: int, J: int, z: int) -> list[float]:
    mu = [0.0] * (N + 1)
    one = [0.0] + [1.0] * N
    logarithm = [0.0] + [math.log(n) for n in range(1, N + 1)]
    for n in range(1, N + 1):
        mu[n] = float(mobius(n)) if n <= z else 0.0
    delta = [0.0] * (N + 1)
    delta[1] = 1.0
    mu_powers: dict[int, list[float]] = {1: mu}
    one_powers: dict[int, list[float]] = {0: delta}
    for j in range(2, J + 1):
        mu_powers[j] = convolution(mu_powers[j - 1], mu, N)
    for j in range(1, J):
        one_powers[j] = convolution(one_powers[j - 1], one, N)
    answer = [0.0] * (N + 1)
    for j in range(1, J + 1):
        term = convolution(mu_powers[j], one_powers[j - 1], N)
        term = convolution(term, logarithm, N)
        coefficient = (-1) ** (j - 1) * math.comb(J, j)
        for n in range(1, N + 1):
            answer[n] += coefficient * term[n]
    return answer


def falling(z: int, k: int) -> int:
    out = 1
    for i in range(k):
        out *= z - i
    return out


def bonferroni_polynomial(z: int, q: Fraction, K: int) -> Fraction:
    return sum(((-q) ** k) * falling(z, k) / math.factorial(k) for k in range(K + 1))


def model_taylor(lam: Fraction, q: Fraction, K: int) -> Fraction:
    return sum(((-q * lam) ** k) / math.factorial(k) for k in range(K + 1))


@dataclass(frozen=True)
class MarginPanel:
    X: int
    M: float
    K: int
    margin: float
    first_order_allowance: float
    hb_order_for_z_le_H: int
    hb_order_ratio: float
    log10_coefficient_mass: float


def margin_panel(X: int, epsilon: float = 0.10, rho: float = 1.10, beta: float = 5.0) -> MarginPanel:
    M = X / math.log(X)
    L = float(X)
    U = rho * L
    q = (1.0 + 3.0 * epsilon) * math.log(M) / L
    K = math.ceil(beta * math.log(M))
    if K % 2:
        K += 1
    log_tail = (K + 1) * math.log(q * U) - math.lgamma(K + 2)
    tail = math.exp(log_tail)
    margin = 1.0 / M - math.exp(-q * L) - tail
    allowance = margin / q
    J_min = math.ceil(X / (2.0 * math.log(X)))
    return MarginPanel(X, M, K, margin, allowance, J_min, J_min / K, J_min * math.log10(2.0))


def verify_heath_brown_identity() -> None:
    for J, z in [(2, 7), (3, 5), (4, 4)]:
        N = min(z**J, 180)
        values = heath_brown_values(N, J, z)
        for n in range(2, N + 1):
            assert abs(values[n] - von_mangoldt(n)) < 1e-8, (J, z, n)


def verify_signed_discrepancy_identity() -> None:
    occupancies = [0, 1, 3, 4]
    lambdas = [Fraction(2), Fraction(2), Fraction(3), Fraction(3)]
    q = Fraction(1, 5)
    K = 4
    n = len(occupancies)
    moments = [sum(Fraction(falling(z, k)) for z in occupancies) / n for k in range(K + 1)]
    model_moments = [sum(lam**k for lam in lambdas) / n for k in range(K + 1)]
    signed_error = sum(((-q) ** k) * (moments[k] - model_moments[k]) / math.factorial(k) for k in range(K + 1))
    direct = sum(bonferroni_polynomial(z, q, K) for z in occupancies) / n - sum(model_taylor(lam, q, K) for lam in lambdas) / n
    assert signed_error == direct


def verify_first_order_embedding() -> None:
    for X in [100, 300, 1_000, 3_000, 10_000, 30_000, 100_000, 1_000_000]:
        panel = margin_panel(X)
        assert panel.margin > 0
        assert panel.first_order_allowance < 1.0
        if X >= 300:
            assert panel.hb_order_for_z_le_H > panel.K
        if X >= 1_000:
            assert panel.log10_coefficient_mass > 20


def verify_coefficient_mass() -> None:
    for J in range(1, 40):
        assert sum(math.comb(J, j) for j in range(1, J + 1)) == 2**J - 1


def main() -> None:
    verify_heath_brown_identity()
    verify_signed_discrepancy_identity()
    verify_first_order_embedding()
    verify_coefficient_mass()
    print("X,M,K,margin,first_order_allowance,J_min,J_min_over_K,log10_HB_mass")
    for X in [100, 300, 1_000, 3_000, 10_000, 30_000, 100_000, 1_000_000]:
        p = margin_panel(X)
        print(f"{p.X},{p.M:.8f},{p.K},{p.margin:.12g},{p.first_order_allowance:.12g},{p.hb_order_for_z_le_H},{p.hb_order_ratio:.8f},{p.log10_coefficient_mass:.8f}")
    print("FORTUNE_RUHL_SELECTED_TUPLE_RESIDUAL_EXACT_PASS")


if __name__ == "__main__":
    main()
