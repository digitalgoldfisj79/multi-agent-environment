#!/usr/bin/env python3
"""Exact integer regression for the INT-PFLI algebraic collapse."""

for A in range(0, 25):
    for Z in range(0, A + 1):
        C = A - Z
        for gamma in range(0, 12):
            lhs = max(0, C - A + gamma)
            rhs = max(0, gamma - Z)
            assert lhs == rhs, (A, Z, C, gamma, lhs, rhs)

print("FORTUNE_INT_PFLI_D1_COLLAPSE_PASS")
