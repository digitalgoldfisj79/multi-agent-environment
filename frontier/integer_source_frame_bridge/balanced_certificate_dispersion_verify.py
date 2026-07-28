#!/usr/bin/env python3
"""Verify the exact balanced-certificate second-moment identities."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, primerange


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def certificates(z: int, H: int) -> list[dict]:
    P = primorial(z)
    out: list[dict] = []
    for p0 in primerange(z + 1, H + 1):
        p = int(p0)
        n = P + p
        fs = factorint(n)
        if len(fs) == 1 and next(iter(fs.values())) == 1:
            continue
        q = min(map(int, fs))
        k = n // q
        if q <= H:
            continue
        assert q <= k
        assert min(map(int, factorint(k))) >= q
        q2 = math.isqrt(n)
        assert H < q <= q2
        routed_k = (P + q - 1) // q
        routed_p = q * routed_k - P
        assert routed_k == k and routed_p == p
        weight = math.log(p)
        out.append({"p": p, "q": q, "k": k, "weight": weight})
    return out


def main() -> None:
    H = 150
    centres = [(11, primorial(11)), (13, primorial(13))]
    rows = []
    direct_second = 0.0
    diagonal = 0.0
    off_diagonal = 0.0
    shifted_off_diagonal = 0.0
    centred_direct = 0.0
    centred_expanded = 0.0

    for index, (z, P) in enumerate(centres):
        certs = certificates(z, H)
        C = sum(item["weight"] for item in certs)
        D = sum(item["weight"] ** 2 for item in certs)
        O = 0.0
        shifted = 0.0
        for a in certs:
            for b in certs:
                if a is b:
                    continue
                assert a["q"] != b["q"]
                h = a["p"] - b["p"]
                assert 0 < abs(h) < H
                assert a["q"] * a["k"] - b["q"] * b["k"] == h
                assert a["q"] * a["k"] - a["p"] == P
                assert b["q"] * b["k"] - b["p"] == P
                term = a["weight"] * b["weight"]
                O += term
                shifted += term
        assert abs(C * C - D - O) < 2e-10
        beta = 0.25 * H / math.log(H) + index
        lhs = (C - beta) ** 2
        rhs = D + O - 2 * beta * C + beta * beta
        assert abs(lhs - rhs) < 2e-10
        rows.append({
            "z": z,
            "P": P,
            "H": H,
            "balanced_certificate_count": len(certs),
            "C": C,
            "diagonal": D,
            "off_diagonal": O,
            "shifted_off_diagonal": shifted,
            "second_moment": C * C,
            "centred_beta": beta,
            "centred_identity_error": abs(lhs - rhs),
            "maximum_weight": max((c["weight"] for c in certs), default=0.0),
        })
        direct_second += C * C
        diagonal += D
        off_diagonal += O
        shifted_off_diagonal += shifted
        centred_direct += lhs
        centred_expanded += rhs

    B = max(row["maximum_weight"] for row in rows)
    candidate_count = sum(len(list(primerange(z + 1, H + 1))) for z, _ in centres)
    diagonal_combinatorial_bound = B * B * candidate_count
    assert diagonal <= diagonal_combinatorial_bound + 1e-10

    payload = {
        "status": "PASS",
        "scope": "balanced-certificate diagonal/off-diagonal and shifted-product identities",
        "parameters": {"H": H, "centres": [z for z, _ in centres]},
        "rows": rows,
        "aggregate": {
            "direct_second_moment": direct_second,
            "diagonal": diagonal,
            "off_diagonal": off_diagonal,
            "shifted_off_diagonal": shifted_off_diagonal,
            "second_moment_error": abs(direct_second - diagonal - off_diagonal),
            "shifted_identity_error": abs(off_diagonal - shifted_off_diagonal),
            "centred_identity_error": abs(centred_direct - centred_expanded),
            "diagonal_combinatorial_bound": diagonal_combinatorial_bound,
        },
        "boundary": "Exact finite identities only; the asymptotic off-diagonal covariance estimate remains open.",
    }
    Path(__file__).with_name("balanced_certificate_dispersion_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
