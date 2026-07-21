#!/usr/bin/env python3
"""Step 2: verify the cubic-ledger identities at p = 3, 5 (C-count also p=7).

(A) master identity: p * #irred_4 = C - p^4,
    C = #{(theta,a,b,c) in F_Q x F_p^3 : theta^p + a theta^3 + b theta^2 + c theta in F_p}
(B) reduced character identity: #irred_4 = p^{3-p} * S_3,
    S_3 = sum_{t in kerTr\0} sum_{theta: Tr(t th)=Tr(t th^2)=Tr(t th^3)=0} e_p(Tr(t^{1/p} th))
(C) W-definition spot checks: W(ut,vt,wt+t^{1/p}) = sum_th e_p(Tr(t*(th^p+u th^3+v th^2+w th)))
(D) full quadruple-sum identity at p=3: C = p^4 + p^{1-p} sum_{t!=0,u,v,w} W(...)
(E) strata: u=v=0 stratum = p-1 (t in F_p^*, w=-1 only);
    u=0,v!=0 stratum = #irred_2-(p-1), and closed Gauss form
      = chi(-1)^{(p+3)/2} p^{(3-p)/2} A',  A' = sum_t eta(t) chi(Tr(t^{2-p}))
(F) slice decomposition: #irred_a = p^2 - p^{3-p} + p^{2-p} R_a, R_a computed directly
(G) second moment at p=5: sum_{t in kerTr} |W(ut,vt,wt+t^{1/p})|^2
      = p^{p-1} #{(th1,th2): g(th1)-g(th2) in F_p}
      = p^{p-1} [(p+1)Q - p + E],  E = sum_{lam} sum_{del!=0} eta(disc),
      disc = -12u del^{p+1} - 3u^2 del^4 + (4v^2-12uw) del^2 + 12u lam del
"""
import numpy as np, sys, time
from itertools import product
sys.path.insert(0, '/tmp/claude-0/-home-user-multi-agent-environment/53da20a7-5af0-58c9-b6a4-3bdefd3e2c90/scratchpad')
from fqlib import FQ, irred_mask_family, brute_counts_p3

def legendre(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1

def run(p, do_full_W=False, do_C=True):
    print(f"\n===== p = {p} =====")
    K = FQ(p)
    Q = K.Q
    Th = K.all_elements()                     # theta coords
    Th2 = K.bmul(Th, Th)
    Th3 = K.bmul(Th2, Th)
    Thp = K.frob(Th)
    idx = K.encode(Th)                        # = arange(Q)
    in_Fp = np.all(Th[:, 1:] == 0, axis=1)    # theta in F_p mask

    # brute force #irred_4 and slices
    if p == 3:
        tot4, slices, _ = brute_counts_p3()
        slices = {a: slices[a] for a in range(3)}
    else:
        quads = np.array(list(product(range(p), repeat=4)), dtype=np.int64)
        mask = irred_mask_family(p, quads)
        tot4 = int(mask.sum())
        slices = {a: int(mask[quads[:, 0] == a].sum()) for a in range(p)}
    irred2 = slices[0]
    print(f"#irred_4 = {tot4}, slices = {slices}")

    # ---- (A) master identity via direct C count ----
    if do_C:
        t0 = time.time()
        C = 0
        for a in range(p):
            ta = (a * Th3) % p
            for b in range(p):
                tb = (ta + b * Th2) % p
                for c in range(p):
                    g = (Thp + tb + c * Th) % p
                    C += int(np.all(g[:, 1:] == 0, axis=1).sum())
        print(f"(A) C = {C}; C - p^4 = {C - p**4}; p*#irred_4 = {p * tot4}; "
              f"match = {C - p**4 == p * tot4}  ({time.time()-t0:.1f}s)")

    # ---- kernel of trace, excluding 0 ----
    tr_all = K.tr(Th)
    ker_mask = (tr_all == 0) & (idx != 0)
    Tker = Th[ker_mask]                        # (p^{p-1}-1, p)
    nker = Tker.shape[0]
    assert nker == p ** (p - 1) - 1

    # ---- (B) reduced identity S_3 ----
    t0 = time.time()
    S3 = 0.0 + 0.0j
    om = np.exp(2j * np.pi / p)
    Bmat = K.B
    T1p_all = K.invfrob(Tker)                  # t^{1/p} for each t
    for i in range(nker):
        t = Tker[i]
        w1 = (t @ Bmat) % p
        q1 = (Th @ w1) % p
        q2 = (Th2 @ w1) % p
        q3 = (Th3 @ w1) % p
        mask = (q1 == 0) & (q2 == 0) & (q3 == 0)
        ph = ((Th[mask] @ ((T1p_all[i] @ Bmat) % p)) % p)
        S3 += (om ** ph).sum()
    pred4 = S3 * p ** (3 - p)
    print(f"(B) p^(3-p) S_3 = {pred4.real:.6f} (imag {abs(pred4.imag):.1e}); "
          f"#irred_4 = {tot4}; match = {abs(pred4 - tot4) < 1e-6}  ({time.time()-t0:.1f}s)")

    # ---- (C) W-definition spot checks ----
    rng = np.random.default_rng(0)
    def W_direct(alpha, beta, gamma):
        # sum_th e_p(Tr(alpha th^3 + beta th^2 + gamma th))
        wa = (alpha @ Bmat) % p; wb = (beta @ Bmat) % p; wc = (gamma @ Bmat) % p
        ph = ((Th3 @ wa) + (Th2 @ wb) + (Th @ wc)) % p
        return (om ** ph).sum()
    okC = True
    for _ in range(5):
        i = rng.integers(0, nker)
        u, v, w = (int(x) for x in rng.integers(0, p, 3))
        t = Tker[i]; t1p = T1p_all[i]
        alpha = (u * t) % p; beta = (v * t) % p; gamma = (w * t + t1p) % p
        Wd = W_direct(alpha, beta, gamma)
        # linearized version: sum_th e_p(Tr(t*(th^p + u th^3 + v th^2 + w th)))
        g = (Thp + u * Th3 + v * Th2 + w * Th) % p
        ph2 = (g @ ((t @ Bmat) % p)) % p
        Wl = (om ** ph2).sum()
        okC &= abs(Wd - Wl) < 1e-6
    print(f"(C) W-def linearization spot checks (5 random): {okC}")

    # ---- (D) full quadruple sum at p=3 ----
    if do_full_W:
        tot = 0.0 + 0.0j
        for i in range(nker):
            t = Tker[i]; t1p = T1p_all[i]
            for u in range(p):
                for v in range(p):
                    for w in range(p):
                        alpha = (u * t) % p; beta = (v * t) % p
                        gamma = (w * t + t1p) % p
                        tot += W_direct(alpha, beta, gamma)
        Cpred = p ** 4 + p ** (1 - p) * tot
        print(f"(D) C from full W sum = {Cpred.real:.6f} (imag {abs(Cpred.imag):.1e}); "
              f"direct C = {C}; match = {abs(Cpred - C) < 1e-4}")

    # ---- (E) strata ----
    # u=v=0: count solutions of w t + t^{1/p} = 0
    cnt = 0
    for w in range(p):
        z = (w * Tker + T1p_all) % p
        cnt += int(np.all(z == 0, axis=1).sum())
    print(f"(E1) u=v=0 stratum: #(t,w) with wt+t^(1/p)=0 = {cnt} "
          f"(pred p-1 = {p-1}); contribution = {cnt} (= p^-p * cnt * p^p)")

    # u=0, v!=0 stratum direct
    t0 = time.time()
    strat2 = 0.0 + 0.0j
    for i in range(nker):
        t = Tker[i]; t1p = T1p_all[i]
        w1 = (t @ Bmat) % p
        q2 = (Th2 @ w1) % p
        q1 = (Th @ w1) % p
        q1p = (Th @ ((t1p @ Bmat) % p)) % p
        for v in range(1, p):
            for w in range(p):
                ph = (v * q2 + w * q1 + q1p) % p
                strat2 += (om ** ph).sum()
    strat2 *= p ** (-p)
    print(f"(E2) u=0,v!=0 stratum direct = {strat2.real:.6f} (imag {abs(strat2.imag):.1e}); "
          f"#irred_2-(p-1) = {irred2 - (p-1)}  ({time.time()-t0:.1f}s)")

    # closed Gauss form
    eta = K.eta_table()
    e_exp = Q - 1 - (p - 2)          # t^{2-p} = t^e, e = Q-1+2-p
    Tpow = K.bpow(Tker, e_exp)
    kappa = K.tr(Tpow)               # Tr(t^{2-p}) in F_p
    eta_t = eta[K.encode(Tker)]
    chi_kappa = np.array([legendre(int(k), p) for k in kappa])
    Aprime = int((eta_t * chi_kappa).sum())
    sgn = legendre(-1, p) ** ((p + 3) // 2)
    closed = sgn * p ** ((3 - p) / 2) * Aprime
    print(f"(E3) A' = {Aprime}; closed form chi(-1)^((p+3)/2) p^((3-p)/2) A' = {closed:.6f}; "
          f"matches direct stratum: {abs(closed - strat2.real) < 1e-6}")

    # ---- (F) slice decomposition ----
    t0 = time.time()
    print("(F) slice decomposition  #irred_a = p^2 - p^(3-p) + p^(2-p) R_a:")
    for a in range(p):
        Ra = 0.0 + 0.0j
        for i in range(nker):
            t = Tker[i]; t1p = T1p_all[i]
            w1 = (t @ Bmat) % p
            q1 = (Th @ w1) % p
            q2 = (Th2 @ w1) % p
            mask = (q1 == 0) & (q2 == 0) & (~in_Fp)
            ph = ((a * Th3[mask] + 0) @ w1 + Th[mask] @ ((t1p @ Bmat) % p)) % p
            Ra += (om ** ph).sum()
        pred = p ** 2 - p ** (3 - p) + p ** (2 - p) * Ra
        status = "OK" if abs(pred - slices[a]) < 1e-6 else "MISMATCH"
        print(f"   a={a}: R_a = {Ra.real:+10.3f} (imag {abs(Ra.imag):.0e}), "
              f"R_a/p^p = {Ra.real/p**p:+.4f}, pred #irred_a = {pred.real:.4f}, "
              f"actual = {slices[a]}  [{status}]")
    print(f"   ({time.time()-t0:.1f}s)")

    return K, Th, Th2, Th3, Thp, Tker, T1p_all, tot4, slices


def second_moment(p, K, Th, Th2, Th3, Thp, Tker, T1p_all, triples):
    print(f"\n----- second moment checks, p = {p} -----")
    Q = K.Q
    om = np.exp(2j * np.pi / p)
    Bmat = K.B
    eta = K.eta_table()
    nker = Tker.shape[0]
    for (u, v, w) in triples:
        # LHS: sum over t in kerTr (including t=0 -> W = Q)
        t0 = time.time()
        lhs = float(Q) ** 2
        for i in range(nker):
            t = Tker[i]; t1p = T1p_all[i]
            w1 = (t @ Bmat) % p
            ph = (u * (Th3 @ w1) + v * (Th2 @ w1) + w * (Th @ w1)
                  + Th @ ((t1p @ Bmat) % p)) % p
            Wv = (om ** ph).sum()
            lhs += abs(Wv) ** 2
        # RHS: p^{p-1} * #{(th1,th2): g(th1)-g(th2) in F_p}
        g = (Thp + u * Th3 + v * Th2 + w * Th) % p
        gi = K.encode(g)
        Ng = np.bincount(gi, minlength=Q)
        corr = 0
        for lam in range(p):
            # index of y - lam: digit-0 arithmetic
            y = np.arange(Q, dtype=np.int64)
            y0 = y % p
            yml = y - y0 + ((y0 - lam) % p)
            corr += int((Ng * Ng[yml]).sum())
        rhs = p ** (p - 1) * corr
        # closed form: (p+1)Q - p + E
        delta = Th[1:]     # delta != 0
        dp1 = K.bpow(delta, p + 1)
        d4 = K.bpow(delta, 4)
        d2 = K.bmul(delta, delta)
        c1 = (-12 * u) % p
        c2 = (-3 * u * u) % p
        c3 = (4 * v * v - 12 * u * w) % p
        Etot = 0
        for lam in range(p):
            c4 = (12 * u * lam) % p
            disc = (c1 * dp1 + c2 * d4 + c3 * d2 + c4 * delta) % p
            Etot += int(eta[K.encode(disc)].sum())
        corr_closed = (p + 1) * Q - p + Etot
        print(f"(u,v,w)=({u},{v},{w}): LHS = {lhs:.1f}, RHS = {rhs}, "
              f"match = {abs(lhs - rhs) < 1e-3 * rhs}")
        print(f"    corr count = {corr}, closed = {corr_closed}, "
              f"E = {Etot} (Weil cap p^2 sqrt(Q) = {p**2 * Q**0.5:.0f}), "
              f"match = {corr == corr_closed}  ({time.time()-t0:.1f}s)")


if __name__ == '__main__':
    out3 = run(3, do_full_W=True, do_C=True)
    out5 = run(5, do_full_W=False, do_C=True)
    K, Th, Th2, Th3, Thp, Tker, T1p, tot4, slices = out5
    second_moment(5, K, Th, Th2, Th3, Thp, Tker, T1p,
                  [(1, 0, 0), (1, 2, 3), (2, 4, 1), (4, 4, 4), (3, 0, 2)])
