#!/usr/bin/env python3
"""Structural check of the exact split/nonsplit normal-form cell ledger.

Checks p=5,7,11 only. No third-party packages are required.
"""


def add(a, b, p):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sub(a, b, p):
    return add(a, [(-x) % p for x in b], p)


def mulmod(a, b, f, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    n = len(f) - 1
    for k in range(len(out) - 1, n - 1, -1):
        coefficient = out[k] % p
        if coefficient:
            for j in range(n):
                out[k - n + j] = (out[k - n + j] - coefficient * f[j]) % p
    out = out[:n]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def powmod(a, exponent, f, p):
    result = [1]
    while exponent:
        if exponent & 1:
            result = mulmod(result, a, f, p)
        a = mulmod(a, a, f, p)
        exponent >>= 1
    return result


def divmod_poly(a, b, p):
    a = a[:]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    inverse = pow(b[-1], -1, p)
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        degree = len(a) - len(b)
        coefficient = a[-1] * inverse % p
        quotient[degree] = coefficient
        for j in range(len(b)):
            a[degree + j] = (a[degree + j] - coefficient * b[j]) % p
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return quotient, a


def gcd_poly(a, b, p):
    while not (len(b) == 1 and b[0] == 0):
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return [(x * inverse) % p for x in a]


def irreducible_prime_degree(f, p):
    degree = len(f) - 1
    x = [0, 1]
    xp = powmod(x, p, f, p)
    if len(gcd_poly(sub(xp, x, p), f, p)) > 1:
        return False
    current = x
    for _ in range(degree):
        current = powmod(current, p, f, p)
    return sub(current, x, p) == [0]


def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def square_root(x, p):
    for y in range(1, p):
        if y * y % p == x % p:
            return y
    raise AssertionError((x, p))


def least_nonsquare(p):
    for x in range(2, p):
        if chi(x, p) == -1:
            return x
    raise AssertionError(p)


def polynomial(p, cubic, linear, constant):
    return [constant, linear, 0, cubic] + [0] * (p - 4) + [1]


def original_counts(p, a):
    counts = {}
    for c in range(p):
        count = 0
        for d in range(p):
            if irreducible_prime_degree(polynomial(p, a, c, d), p):
                count += 1
        counts[c] = count
    return counts


def normalized_count(p, a, c):
    q = -3 * pow(c, -1, p) % p
    r = pow(a * q % p, -1, p)
    eta = least_nonsquare(p)
    epsilon = chi(r, p)
    if epsilon == 1:
        square_root(r, p)
        cubic = pow(q, -1, p)
    else:
        square_root(r * pow(eta, -1, p) % p, p)
        cubic = pow(eta * q % p, -1, p)
    linear = -3 * pow(q, -1, p) % p
    count = sum(
        irreducible_prime_degree(polynomial(p, cubic, linear, delta), p)
        for delta in range(p)
    )
    return q, epsilon, count


def main():
    committed = {
        5: (4, 6),
        7: (10, 8),
        11: (14, 14),
    }
    for p in (5, 7, 11):
        eta = least_nonsquare(p)
        seen = set()
        totals = []
        for a in (1, eta):
            arithmetic_class = chi(a, p)
            counts = original_counts(p, a)
            totals.append(sum(counts.values()))
            for c in range(1, p):
                q, epsilon, count = normalized_count(p, a, c)
                assert epsilon == arithmetic_class * chi(q, p)
                assert count == counts[c]
                seen.add((q, epsilon))
        assert len(seen) == 2 * (p - 1)
        assert tuple(totals) == committed[p]
        print(f"PASS p={p}: all cells and committed totals agree.")


if __name__ == "__main__":
    main()
