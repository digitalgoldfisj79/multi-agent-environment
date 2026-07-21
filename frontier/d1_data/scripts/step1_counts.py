#!/usr/bin/env python3
"""Step 1: brute-force irreducible counts.
- quartic family T^p + aT^3 + bT^2 + cT + d for p = 3,5,7,11,13
  (total, per-a slices, fortune-relevant (a,b)!=(0,0))
- cross-check batched Rabin against sympy on random samples
- re-verify the quadratic-family table for p up to 19
"""
import numpy as np, sys, time
from itertools import product
sys.path.insert(0, '/tmp/claude-0/-home-user-multi-agent-environment/53da20a7-5af0-58c9-b6a4-3bdefd3e2c90/scratchpad')
from fqlib import irred_mask_family, brute_counts_p3

# p = 3 special
tot3, slices3, fortune3 = brute_counts_p3()
print(f"p=3 quartic family: total deg-3 irred = {tot3}, per-a slices = {slices3}, "
      f"fortune (a,b)!=(0,0) = {fortune3}")

for p in [5, 7, 11, 13]:
    t0 = time.time()
    quads = np.array(list(product(range(p), repeat=4)), dtype=np.int64)  # (a,b,c,d)
    mask = irred_mask_family(p, quads)
    tot = int(mask.sum())
    a_slice = {a: int(mask[quads[:, 0] == a].sum()) for a in range(p)}
    fortune = int(mask[(quads[:, 0] != 0) | (quads[:, 1] != 0)].sum())
    quad_fam = a_slice[0]   # a=0 slice = quadratic family count
    print(f"p={p}: #irred_4 = {tot} (p^3={p**3}), a=0 slice = {quad_fam}, "
          f"fortune = {fortune}, time {time.time()-t0:.1f}s")
    print(f"   per-a: {a_slice}")

# cross-check vs sympy on random sample at p=7
import sympy
T = sympy.symbols('T')
rng = np.random.default_rng(1)
p = 7
sample = rng.integers(0, p, size=(40, 4))
mask = irred_mask_family(p, sample)
for row, m in zip(sample, mask):
    a, b, c, d = (int(x) for x in row)
    coeffs = [1] + [0] * (p - 4) + [a, b, c, d]
    ok = sympy.Poly(coeffs, T, modulus=p).is_irreducible
    assert ok == bool(m), (row, ok, m)
print("Rabin batch vs sympy: 40/40 agree at p=7")

# quadratic family re-verification
print("\nquadratic family (b,c,d):")
for p in [5, 7, 11, 13, 17, 19]:
    trips = np.array(list(product(range(p), repeat=3)), dtype=np.int64)
    quads = np.column_stack([np.zeros(len(trips), dtype=np.int64), trips])
    mask = irred_mask_family(p, quads)
    tot = int(mask.sum())
    bnz = int(mask[trips[:, 0] != 0].sum())
    N = (tot - (p - 1)) / (p * (p - 1))
    print(f"p={p}: #irred_2 = {tot}, b!=0: {bnz}, N(p) = {N}")
