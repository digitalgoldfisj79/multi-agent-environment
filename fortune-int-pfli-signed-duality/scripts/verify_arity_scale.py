#!/usr/bin/env python3
"""Quantify the minimum moment and prime-correlation arity forced by D4."""

import math

for X in (10**2, 10**3, 10**4, 10**5, 10**6, 10**8, 10**10):
    N = max(2, int(X / math.log(X)))
    K_min = math.floor(math.log2(N)) + 1
    assert 2 ** (K_min - 1) <= N < 2**K_min
    prime_arity = 2 * K_min
    ratio = K_min / math.log(X)
    print(
        f"X={X} rows={N} min_factorial_order={K_min} "
        f"min_prime_arity={prime_arity} K_over_logX={ratio:.6f}"
    )

print("FORTUNE_INT_PFLI_D5_ARITY_SCALE_PASS")
