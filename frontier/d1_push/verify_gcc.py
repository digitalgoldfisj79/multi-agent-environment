#!/usr/bin/env python3
"""Independent re-verification of GCC.1 at p=5,7.

For every (a,c,d) with a != 0: build H(F)_{u,v} = [X^{pu-v}] F^{p-1},
compute cofactor C_j(I-H) (delete row p, column j) for j in {1,2,3},
compare against j*f_j*1_irr with f_1=c, f_2=0, f_3=a.
Irreducibility decided independently by flint factorisation.
Written from scratch (matrix built as full p x p, minor via row/col delete).
"""
from flint import nmod_poly, nmod_mat

def irr(f, p):
    lead, facs = f.factor()
    return len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == p

def run(p):
    mismatches = 0
    checked = 0
    for a in range(1, p):
        for c in range(p):
            for d in range(p):
                F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
                G = F**(p-1)
                deg = G.degree()
                # full I-H
                IH = [[0]*p for _ in range(p)]
                for u in range(1, p+1):
                    for v in range(1, p+1):
                        e = p*u - v
                        h = int(G[e]) if 0 <= e <= deg else 0
                        IH[u-1][v-1] = ((1 if u == v else 0) - h) % p
                t = int(irr(F, p))
                fj = {1: c, 2: 0, 3: a}
                for j in (1, 2, 3):
                    # delete row p (index p-1) and column j (index j-1)
                    minor = [[IH[r][cc] for cc in range(p) if cc != j-1]
                             for r in range(p-1)]
                    cof = int(nmod_mat(minor, p).det()) % p
                    # cofactor sign: deleting row p, col j -> sign (-1)^(p+j)
                    sign = (-1)**(p + j)
                    cof = (sign * cof) % p
                    expect = (j * fj[j] * t) % p
                    checked += 1
                    if cof != expect:
                        mismatches += 1
                        if mismatches < 10:
                            print("MISMATCH", p, a, c, d, j, cof, expect)
    print(f"p={p}: checked {checked} cofactor evaluations, mismatches={mismatches}")
    return mismatches

tot = 0
for p in (5, 7):
    tot += run(p)
print("ALL PASS" if tot == 0 else "FAILURES PRESENT")
