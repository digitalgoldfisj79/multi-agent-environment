#!/usr/bin/env python3
"""Create an O(p^2) large-sweep variant of cubic_mixed_mass_audit.cpp.

The original exact audit computes the rational-root multiplicity array with a
triple loop over (c,d,x).  For each fixed (c,x), exactly one d makes x a root,
so the same array is obtained by incrementing that unique cell.  This patch
changes only that exact construction and leaves all quadratic/cubic arithmetic
and moment checks unchanged.
"""
from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: cubic_mixed_mass_fast_patch.py <input.cpp> <output.cpp>")
src = Path(sys.argv[1]).read_text()
old = '''    // Complete rational-root count.
    for (int c = 0; c < p; ++c) {
        for (int d = 0; d < p; ++d) {
            int count = 0;
            for (int x = 0; x < p; ++x) {
                int value = modp(
                    (long long)a * x % p * x % p * x
                    + (long long)(c + 1) * x + d,
                    p
                );
                if (value == 0) ++count;
            }
            linear[c * p + d] = count;
        }
    }
'''
new = '''    // Complete rational-root count in O(p^2): for fixed (c,x), the unique
    // constant term making x a root is d=-a*x^3-(c+1)*x.
    for (int c = 0; c < p; ++c) {
        for (int x = 0; x < p; ++x) {
            int d = modp(
                -(long long)a * x % p * x % p * x
                - (long long)(c + 1) * x,
                p
            );
            ++linear[c * p + d];
        }
    }
'''
if old not in src:
    raise SystemExit("expected source block not found")
Path(sys.argv[2]).write_text(src.replace(old, new))
