#!/usr/bin/env python3
import json

rows = [
    (5, 1, 4, 6),
    (7, 1, 10, 8),
    (11, 1, 14, 14),
    (17, 1, 18, 14),
    (23, 2, 12, 22),
]

out = []
for p, n2, nsq, nns in rows:
    W = n2 + (nsq + nns) // 2
    q_points = 1 + (p - 1) * W
    recovered = ((q_points - 1) * pow(p - 1, -1, p * p)) % (p * p)
    assert 0 <= W < p * p
    assert recovered == W
    assert (q_points % (p * p) == 1) == (W == 0)
    out.append(
        {
            "p": p,
            "N2": n2,
            "N_sq": nsq,
            "N_ns": nns,
            "W": W,
            "Q_points": q_points,
            "Q_mod_p": q_points % p,
            "Q_mod_p2": q_points % (p * p),
            "recovered_W_mod_p2": recovered,
        }
    )

payload = {
    "rows": out,
    "theorem": (
        "Because N2<=p-1 and each N_a<=p(p-1), 0<=W_p<=p^2-1. "
        "Hence #Q_p(F_p)=1+(p-1)W_p is congruent to 1 mod p^2 iff W_p=0."
    ),
}
print(json.dumps(payload, indent=2))
