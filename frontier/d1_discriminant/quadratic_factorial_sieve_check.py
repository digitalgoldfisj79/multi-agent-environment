from math import comb, isqrt


def primes(n):
    return [m for m in range(2, n + 1) if all(m % d for d in range(2, isqrt(m) + 1))]


def inv(x, p):
    return pow(x % p, p - 2, p)


def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def local_rootless(a, c, d, p):
    return all((a * x**3 + (c + 1) * x + d) % p for x in range(p))


def disc_char(a, c, d, p):
    sp = 1 if p % 4 == 1 else -1
    if c % p == 0:
        value = sp * 3 * a * d * d
    else:
        eps = chi(-c * inv(3 * a, p), p)
        term = (eps + 2 * c * inv(3, p)) % p
        value = sp * (3 * a * d * d + c * term * term)
    return chi(value, p)


def quadratic_factors(a, c, d, p):
    out = []
    ia = inv(a, p)
    for s in range(p):
        n = (s * s - (1 - c) * ia) % p
        if (s * (a * n - 1) - d) % p:
            continue
        if chi(s * s - 4 * n, p) == -1:
            out.append((s, n))
    return out


def cd_from_uv(a, u, v, p):
    i3 = inv(3, p)
    i27 = inv(27, p)
    q = (u * u - u * v + v * v) % p
    c = (2 - a * q * i3) % p
    d = (a * (u - 2 * v) * (u + v) * (2 * u - v) * i27) % p
    return c, d


def transformed(a, p, j):
    k = 4 * inv(a, p) % p
    unsigned = signed = total = 0
    divisor = 2 if j == 2 else 6

    for u in range(p):
        for v in range(p):
            A = (u * u - k) % p
            B = (v * v - k) % p
            if chi(A, p) != -1 or chi(B, p) != -1:
                continue

            if j == 2:
                if u == v:
                    continue
            else:
                C = ((u - v) * (u - v) - k) % p
                if chi(C, p) != -1 or u == 0 or v == 0 or u == v:
                    continue

            c, d = cd_from_uv(a, u, v, p)
            total += 1
            if local_rootless(a, c, d, p):
                unsigned += 1
                signed += disc_char(a, c, d, p)

    assert total % divisor == 0
    assert unsigned % divisor == 0
    assert signed % divisor == 0
    return total // divisor, unsigned // divisor, signed // divisor


def direct(a, p):
    totals = [0, 0, 0, 0]
    local = [0, 0, 0, 0]
    signed = [0, 0, 0, 0]
    max_nu = 0

    for c in range(p):
        for d in range(p):
            nu = len(quadratic_factors(a, c, d, p))
            max_nu = max(max_nu, nu)
            for j in (1, 2, 3):
                totals[j] += comb(nu, j)

            if local_rootless(a, c, d, p):
                eta = disc_char(a, c, d, p)
                for j in (1, 2, 3):
                    local[j] += comb(nu, j)
                    signed[j] += eta * comb(nu, j)

    return max_nu, totals, local, signed


def run():
    for p in [q for q in primes(47) if q >= 5]:
        classes = [1, next(z for z in range(2, p) if chi(z, p) < 0)]
        for a in classes:
            max_nu, totals, local, signed = direct(a, p)
            assert max_nu <= 3

            n_a = (p - chi(a, p)) // 2
            assert totals[2] == n_a * (n_a - 1) // 2

            for j in (2, 3):
                transformed_values = transformed(a, p, j)
                direct_values = totals[j], local[j], signed[j]
                assert transformed_values == direct_values, (
                    p,
                    a,
                    j,
                    transformed_values,
                    direct_values,
                )

            print(
                f"p={p}, a={a}: PASS; "
                f"complete={totals[1:]}, local={local[1:]}, signed={signed[1:]}"
            )


if __name__ == "__main__":
    run()
