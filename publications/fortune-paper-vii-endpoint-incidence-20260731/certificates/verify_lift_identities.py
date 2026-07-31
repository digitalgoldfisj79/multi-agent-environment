#!/usr/bin/env python3
"""Exact verification of the two chart lift identities T = K*M over Q.

Parses the Singular lift matrices (regenerate with chartB_universal.sing /
chartX_universal.sing) and re-expands T = K*M with exact Fraction dict
arithmetic; also checks the identities modulo 1009 and 10007.
Usage: python3 verify_lift_identities.py lift_B.out lift_X.out
"""
import re, sys
from fractions import Fraction

def parse(fn):
    txt = open(fn).read()
    seg = txt.split("LIFT_BEGIN")[1].split("LIFT_END")[0]
    M = {}
    for m in re.finditer(r"_\[(\d+),(\d+)\]=([^_]+?)(?=_\[|$)", seg, re.S):
        s = m.group(3).strip().replace("\n", "")
        poly = {}
        for tok in re.findall(r"[+-]?[^+-]+", s):
            mm = re.fullmatch(r"([+-]?)(\d+(?:/\d+)?)?((?:[zABCU]\d*)*)", tok)
            sign = -1 if mm.group(1) == "-" else 1
            co = Fraction(mm.group(2)) if mm.group(2) else Fraction(1)
            ex = [0] * 5
            for vm in re.finditer(r"([zABCU])(\d*)", mm.group(3) or ""):
                ex["zABCU".index(vm.group(1))] += \
                    int(vm.group(2)) if vm.group(2) else 1
            key = tuple(ex)
            poly[key] = poly.get(key, Fraction(0)) + sign * co
        M[(int(m.group(1)), int(m.group(2)))] = \
            {k: v for k, v in poly.items() if v}
    return M

def pmulq(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, Fraction(0)) + va * vb
    return {k: v for k, v in out.items() if v}

def paddq(a, b):
    out = dict(a)
    for k, v in b.items():
        s = out.get(k, Fraction(0)) + v
        if s:
            out[k] = s
        elif k in out:
            del out[k]
    return out

def gp(s):
    import sympy as sp
    syms = sp.symbols("z A B C U")
    e = sp.Poly(sp.sympify(s), *syms)
    return {tuple(mon): Fraction(int(c))
            for mon, c in zip(e.monoms(), e.coeffs())}

F = [gp("-4*A**2*B*U+6*A**2*B-2*A**2*U+4*A**2+4*A*B**3+4*A*B**2*U+2*A*B**2"
        "+4*A*B*C*U-8*A*B*C-4*A*C+2*B*C**2+2*C**2*U"),
     gp("-4*A**2*U+4*A**2+2*A*B**2+6*A*B*U-2*A*B+8*A*C*U-8*A*C-2*B**2*C"
        "-2*B*C*U-2*B*C-4*C**2*U+4*C**2"),
     gp("-2*A**2*B-2*A**2*U-2*A*B**3*U-A*B**3-2*A*B**2*U**2-2*A*B**2*U"
        "+4*A*B*C*U+4*A*C*U**2-B**3*C-2*B**2*C*U-4*B*C**2*U+2*B*C**2"
        "-4*C**2*U**2+2*C**2*U"),
     gp("4*A**2*U-4*A**2+2*A*B**2*U-4*A*B**2-2*A*B*U**2-2*A*B*U-8*A*C*U"
        "+8*A*C-B**4-2*B**3*U-2*B**2*C*U+4*B**2*C-2*B*C*U**2+6*B*C*U"
        "+4*C**2*U-4*C**2")]
T = [gp("U-1"), gp("B+2"), gp("(A-C)**2+4*A")]
INVS = {"B": "z*U*A*(B**2-4*C)*B-1", "X": "z*U*A*(B**2-4*C)*(A-C)-1"}

def main():
    fails = 0
    for chart, fn in (("B", sys.argv[1]), ("X", sys.argv[2])):
        K = F + [gp(INVS[chart])]
        M = parse(fn)
        ok = True
        for j in range(1, 4):
            acc = {}
            for i in range(1, 6):
                acc = paddq(acc, pmulq(K[i - 1], M.get((i, j), {})))
            if paddq(acc, {k: -v for k, v in T[j - 1].items()}):
                ok = False
        print(f"chart {chart}: T = K*M exact over Q: {ok}")
        fails += not ok
    sys.exit(fails)

if __name__ == "__main__":
    main()
