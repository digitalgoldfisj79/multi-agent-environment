#!/usr/bin/env python3
"""Independent scan: N_a(p) and c-moment M_a(p) = sum_irr c mod p,
for a = 1 and a = least nonresidue, p in the 30-prime validation table.
Uses the d -> -d involution (irreducibility invariant, d=0 reducible).
Verifies against the context table.
"""
from flint import nmod_poly
import json, sys

TABLE = {5:(4,6),7:(10,8),11:(14,14),13:(10,6),17:(18,14),19:(22,16),23:(12,22),
         29:(36,28),31:(30,38),37:(36,36),41:(50,34),43:(42,36),47:(38,40),
         53:(56,38),59:(46,52),61:(42,54),67:(62,80),71:(72,76),73:(74,66),
         79:(80,64),83:(86,82),89:(64,78),97:(84,82),101:(76,116),103:(88,90),
         107:(90,104),109:(78,112),113:(90,84),127:(156,116),131:(110,122)}

def least_nr(p):
    for n in range(2, p):
        if pow(n, (p - 1) // 2, p) == p - 1:
            return n

def irr(f, p):
    lead, facs = f.factor()
    return len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == p

def scan(p, a):
    N = 0
    M = 0  # sum of c over irreducibles, mod p
    for c in range(p):
        for d in range(1, (p + 1) // 2):
            F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
            if irr(F, p):
                N += 2
                M = (M + 2 * c) % p
    return N, M

out = {}
for p in sorted(TABLE):
    nr = least_nr(p)
    res = {}
    for label, a in (("+", 1), ("-", nr)):
        N, M = scan(p, a)
        res[label] = dict(a=a, N=N, N_mod_p=N % p,
                          N_centered=(N % p) if (N % p) <= p // 2 else (N % p) - p,
                          M=M, S=(3 * a * N) % p)
    exp = TABLE[p]
    match = (res["+"]["N"], res["-"]["N"]) == exp
    out[p] = res
    print(p, res["+"]["N"], res["-"]["N"], "TABLE_MATCH" if match else f"TABLE_MISMATCH exp={exp}",
          "| Nmod:", res["+"]["N_centered"], res["-"]["N_centered"],
          "| M:", res["+"]["M"], res["-"]["M"],
          "| S:", res["+"]["S"], res["-"]["S"])
    sys.stdout.flush()

with open("scan_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("done")
