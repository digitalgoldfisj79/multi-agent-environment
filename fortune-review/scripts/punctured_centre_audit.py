#!/usr/bin/env python3
"""Independent audit computations for the hostile review of the punctured-centre
full-band Fortune reduction (PR #33, branch gpt56/fortune-mesoscopic-cotlar-20260728).

Independent implementation: shares no code with the branch verifiers.

Checks:
  A. Two-level Heath-Brown identity (3.1) and one-small-variable resummation (3.2),
     exactly (formal prime-exponent vectors), for every n <= H on panels X=11,17,23,
     plus the intermediate epsilon-level identity eps = 2A - A^2 + B*B (integer-valued).
  E. Support audit of the one-variable collision collapse (packet claim 8.2 / gate (4.2)):
     - on the verifier's tested range m,m' <= Y the collapse HOLDS (0 violations);
     - on the true cell range m,m' <= H/d it FAILS for every panel (explicit
       counterexamples printed).
  F. The multiplicative-character form of the residue-energy identity (9.1)
     (the committed verifier checks only the weaker centring identity).
  G. Empirical (labelled EMPIRICAL) fixed-modulus energy ratios for Mobius vs
     unweighted coefficients, illustrating that the signs carry the entire
     required factor-p saving.
"""
import cmath, math, sys
from fractions import Fraction

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = b"\x00" * len(s[i * i :: i])
    return [i for i in range(n + 1) if s[i]]

def factorize(n):
    f = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f

def mobius(n):
    f = factorize(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1

def divisors(n):
    ds = [1]
    for p, e in factorize(n).items():
        ds = [d * p ** a for d in ds for a in range(e + 1)]
    return ds

# ---------------------------------------------------------------- A: identities
def expvec_add(target, n, coeff):
    """target += coeff * (prime-exponent vector of log n)."""
    for p, e in factorize(n).items():
        target[p] = target.get(p, 0) + coeff * e
        if target[p] == 0:
            del target[p]

def lambda_vec(n):
    f = factorize(n)
    return {next(iter(f)): 1} if len(f) == 1 else {}

def check_panel_identities(X, eta_num=4, eta_den=5):
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    assert Y < X and H <= Y * Y

    # epsilon-level: eps = 2A - A^2 + B*B  with A = mu_{<=Y}*1, B = mu_{>Y}*1
    def A(n):
        return sum(mobius(d) for d in divisors(n) if d <= Y)
    def B(n):
        return sum(mobius(d) for d in divisors(n) if d > Y)
    ok_eps = True
    for n in range(1, Y * Y + 1):
        a2 = sum(A(u) * A(n // u) for u in divisors(n))
        bb = sum(B(u) * B(n // u) for u in divisors(n))
        eps = 1 if n == 1 else 0
        if 2 * A(n) - a2 + bb != eps:
            ok_eps = False
            break
        if n <= Y * Y and bb != 0 and n <= Y * Y:
            pass
    report(f"eps = 2A - A^2 + B*B on n <= Y^2   (X={X}, Y={Y})", ok_eps)

    # B*B vanishes on n <= Y^2 (support claim used to drop it)
    ok_supp = all(
        sum(B(u) * B(n // u) for u in divisors(n)) == 0 for n in range(1, Y * Y + 1)
    )
    report(f"(mu_>Y * 1)^2 has no support <= Y^2 (X={X})", ok_supp)

    ok31 = ok32 = True
    for n in range(1, H + 1):
        lam = lambda_vec(n)
        # (3.1): 2 mu_<=Y * log - mu_<=Y * mu_<=Y * 1 * log
        v = {}
        for d in divisors(n):
            if d <= Y and mobius(d):
                expvec_add(v, n // d, 2 * mobius(d))
        for d1 in divisors(n):
            if d1 > Y or not mobius(d1):
                continue
            for d2 in divisors(n // d1):
                if d2 > Y or not mobius(d2):
                    continue
                rem = n // (d1 * d2)
                for e in divisors(rem):
                    expvec_add(v, rem // e, -mobius(d1) * mobius(d2))
        if v != lam:
            ok31 = False
        # (3.2): mu_<=Y * log + mu_<=Y * mu_>Y * 1 * log
        w = {}
        for d in divisors(n):
            if d <= Y and mobius(d):
                expvec_add(w, n // d, mobius(d))
        for d in divisors(n):
            if d > Y or not mobius(d):
                continue
            for a in divisors(n // d):
                if a <= Y or not mobius(a):
                    continue
                rem = n // (d * a)
                for e in divisors(rem):
                    expvec_add(w, rem // e, mobius(d) * mobius(a))
        if w != lam:
            ok32 = False
    report(f"(3.1) two-level HB identity, all n <= H={H}  (X={X})", ok31)
    report(f"(3.2) one-small-variable resummation, all n <= H  (X={X})", ok32)
    return H, Y

# ------------------------------------------------- E: collision support audit
def collision_support_audit(X, eta_num=4, eta_den=5):
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    band = [p for p in primes_upto(2 * X) if p > X]
    smalls = [d for d in range(1, Y + 1) if mobius(d)]

    # verifier's range: d,m,m' <= Y  --  the collapse must HOLD here
    viol_bal = 0
    for p in band:
        for d in smalls:
            for m in range(1, Y + 1):
                for mp in range(1, Y + 1):
                    if m != mp and (d * (m - mp)) % p == 0:
                        viol_bal += 1
    report(f"collapse on balanced range m,m'<=Y={Y} (X={X})", viol_bal == 0,
           f"violations={viol_bal}")

    # true cell range: m,m' <= H/d  --  count violations of the unscoped claim
    viol = 0
    example = None
    for p in band:
        for d in smalls:
            top = H // d
            if top <= p:
                continue
            # p | d(m-m'), p coprime to d  <=>  m' = m mod p
            for m in range(1, top + 1):
                k = (top - m) // p
                viol += k          # m' = m + p, m + 2p, ..., all <= top, m' != m
                if k and example is None:
                    example = (p, d, m, m + p, H)
    report(f"UNSCOPED claim 8.2 on true range m,m'<=H/d (X={X})", viol > 0,
           f"one-variable collisions with m!=m': {viol}"
           + (f"; example p={example[0]}, d=d'={example[1]}, m={example[2]}, "
              f"m'={example[3]} <= H/d={example[4]//example[1]}" if example else ""))
    # NB: report() marks this PASS when viol>0: the audit *expects* violations,
    # i.e. the unscoped claim is false on the true range.
    return viol

# ---------------------------------- F: character form of the residue energy (9.1)
def residue_energy_character_check(p, D, M):
    alpha = {d: mobius(d) for d in range(1, D + 1) if mobius(d) and d % p != 0}
    gamma = {m: mobius(m) for m in range(1, M + 1) if mobius(m) and m % p != 0}
    # LHS: sum over units of |r(a) - AC/(p-1)|^2
    r = [0.0] * p
    for d, ad in alpha.items():
        for m, gm in gamma.items():
            r[(d * m) % p] += ad * gm
    A = sum(alpha.values())
    C = sum(gamma.values())
    mean = A * C / (p - 1)
    lhs = sum((r[a] - mean) ** 2 for a in range(1, p))
    # RHS: (1/(p-1)) sum_{chi != chi0} |sum alpha chi|^2 |sum gamma chi|^2
    # characters via a primitive root
    g = next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1
             for q in factorize(p - 1)))
    dlog = {}
    x = 1
    for t in range(p - 1):
        dlog[x] = t
        x = x * g % p
    rhs = 0.0
    for k in range(1, p - 1):                     # chi_k, k=0 is principal
        Msum = sum(ad * cmath.exp(2j * cmath.pi * k * dlog[d % p] / (p - 1))
                   for d, ad in alpha.items())
        Csum = sum(gm * cmath.exp(2j * cmath.pi * k * dlog[m % p] / (p - 1))
                   for m, gm in gamma.items())
        rhs += abs(Msum) ** 2 * abs(Csum) ** 2
    rhs /= (p - 1)
    ok = abs(lhs - rhs) < 1e-6 * max(1.0, abs(lhs))
    report(f"(9.1) character form, p={p}, D={D}, M={M}", ok,
           f"lhs={lhs:.6f} rhs={rhs:.6f}")

# --------------------------------- G: empirical fixed-modulus energy ratios
def empirical_energy(p, D, M, signed=True):
    """Returns (uncentred, centred) residue energy on F_p^x and (A, C)."""
    r = [0.0] * p
    for d in range(1, D + 1):
        ad = mobius(d) if signed else 1
        if not ad or d % p == 0:
            continue
        for m in range(1, M + 1):
            gm = mobius(m) if signed else 1
            if not gm or m % p == 0:
                continue
            r[(d * m) % p] += ad * gm
    if signed:
        A = sum(mobius(d) for d in range(1, D + 1) if mobius(d) and d % p)
        C = sum(mobius(m) for m in range(1, M + 1) if mobius(m) and m % p)
    else:
        A = sum(1 for d in range(1, D + 1) if d % p)
        C = sum(1 for m in range(1, M + 1) if m % p)
    mean = A * C / (p - 1)
    unc = sum(r[a] ** 2 for a in range(1, p))
    cen = sum((r[a] - mean) ** 2 for a in range(1, p))
    return unc, cen, A, C

def main():
    print("== A. Independent identity verification ==")
    for X in (11, 17, 23):
        check_panel_identities(X)

    print("\n== E. Collision-collapse support audit ==")
    for X in (11, 17, 23):
        collision_support_audit(X)

    print("\n== F. Character form of residue-energy identity (9.1) ==")
    residue_energy_character_check(101, 90, 150)
    residue_energy_character_check(199, 180, 260)

    print("\n== G. EMPIRICAL fixed-modulus residue energies / (D*M), D=M~0.55p ==")
    print("   unweighted: uncentred has structured main term ~ (DM)^2/p /(DM) = DM/p,")
    print("   removed exactly by centring (ACZ regime).  Mobius: centring is vacuous")
    print("   (A ~ 0); smallness of the energy = mu-vs-chi non-correlation (unproved")
    print("   at D ~ p; GRH-accessible).  EMPIRICAL ONLY.")
    for p in (101, 199, 307, 401):
        D = M = int(0.55 * p)
        uu, uc, _, _ = empirical_energy(p, D, M, signed=False)
        su, sc, A, C = empirical_energy(p, D, M, signed=True)
        print(f"   p={p:4d} D=M={D}: unsigned unc/cen = {uu/(D*M):7.1f} /{uc/(D*M):7.2f}"
              f"   mu unc/cen = {su/(D*M):6.2f} /{sc/(D*M):6.2f}"
              f"   (A={A}, C={C}, DM/p={(D*M)/p:.1f})")

    sys.exit(FAIL)

if __name__ == "__main__":
    main()
