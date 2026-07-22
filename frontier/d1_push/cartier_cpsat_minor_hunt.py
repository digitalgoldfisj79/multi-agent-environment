#!/usr/bin/env python3
"""Targeted exact search for a CT1-w1 counterexample.

CP-SAT enumerates only torus-graded support matchings of the inverse
substitution minor with beta >= gamma+4.  Each distinct (E,R) is then tested
by exact modular determinant evaluation:

  det(P^-1)[R,E union {0}] * det(U)[R,E union {p-3}] mod p.

A nonzero product is a genuine counterexample to CT1-w1.  A zero product is
excluded by a no-good cut and enumeration continues.  A finite clean run is
not a proof, but it targets the actual cancellation locus far more efficiently
than unconstrained random subset sampling.
"""
from __future__ import annotations

import argparse
import json
from math import comb, factorial
from ortools.sat.python import cp_model


def invmod(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    out = 1
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out % p
        pv = a[c][c]
        out = out * pv % p
        ipv = invmod(pv, p)
        for r in range(c + 1, n):
            if not a[r][c]:
                continue
            factor = a[r][c] * ipv % p
            for j in range(c, n):
                a[r][j] = (a[r][j] - factor * a[c][j]) % p
    return out


def p_inverse_entry(r: int, s: int, p: int) -> int:
    if r < s:
        return 0
    value = invmod(factorial(s) * factorial(r - s), p)
    return -value % p if (r - s) & 1 else value


def u_entry(r: int, s: int, p: int) -> int:
    if s == 0:
        return int(r == 0)
    if r < s or (r - s) & 1:
        return 0
    h = (r - s) // 2
    if 3 * r - s > 2 * p:
        return 0
    value = s * invmod(r, p) % p
    value = value * (comb(r + h - 1, h) % p) % p
    return -value % p if h & 1 else value


def evaluate(p: int, E: list[int], R: list[int]) -> tuple[int, int]:
    c0 = sorted(E + [0])
    c1 = sorted(E + [p - 3])
    pm = [[p_inverse_entry(r, s, p) for s in c0] for r in R]
    um = [[u_entry(r, s, p) for s in c1] for r in R]
    return det_mod(pm, p), det_mod(um, p)


def build_model(p: int, gamma: int, beta: int):
    sum_e = gamma * (p - 1) // 2 - 1
    target_r = sum_e + beta * (p - 1)
    model = cp_model.CpModel()
    mandatory = p - 3
    optional_columns = [s for s in range(1, p) if s != mandatory]
    columns = optional_columns + [mandatory]

    edges = {}
    by_col = {s: [] for s in columns}
    by_row = {r: [] for r in range(p)}
    for s in columns:
        for r in range(s, p):
            if (r - s) % 2 == 0 and 3 * r - s <= 2 * p:
                x = model.NewBoolVar(f"x_{s}_{r}")
                edges[s, r] = x
                by_col[s].append(x)
                by_row[r].append(x)

    e = {}
    for s in optional_columns:
        y = model.NewBoolVar(f"e_{s}")
        e[s] = y
        model.Add(sum(by_col[s]) == y)
    model.Add(sum(by_col[mandatory]) == 1)

    rsel = {}
    for r in range(p):
        y = model.NewBoolVar(f"r_{r}")
        rsel[r] = y
        model.Add(sum(by_row[r]) == y)

    model.Add(sum(s * e[s] for s in optional_columns) == sum_e)
    model.Add(sum(r * rsel[r] for r in range(p)) == target_r)
    model.Add(sum(e.values()) + 1 == sum(rsel.values()))
    return model, e, rsel


def hunt_pair(
    p: int,
    gamma: int,
    beta: int,
    max_solutions: int,
    time_limit: float,
) -> dict:
    model, e, rsel = build_model(p, gamma, beta)
    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 8
    solver.parameters.cp_model_presolve = True
    solver.parameters.max_time_in_seconds = time_limit

    tested = detp_nonzero = detu_nonzero = 0
    first_zero_examples = []
    total_wall = 0.0
    terminal_status = "LIMIT"

    while tested < max_solutions and total_wall < time_limit:
        solver.parameters.max_time_in_seconds = max(0.01, time_limit - total_wall)
        status = solver.Solve(model)
        total_wall += solver.WallTime()
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            terminal_status = solver.StatusName(status)
            break

        E = sorted(s for s, y in e.items() if solver.Value(y))
        R = sorted(r for r, y in rsel.items() if solver.Value(y))
        dp, du = evaluate(p, E, R)
        tested += 1
        detp_nonzero += bool(dp)
        detu_nonzero += bool(du)

        if len(first_zero_examples) < 3:
            first_zero_examples.append(
                {"E": E, "R": R, "detP": dp, "detU": du}
            )

        if dp and du:
            return {
                "p": p,
                "gamma": gamma,
                "beta": beta,
                "status": "COUNTEREXAMPLE",
                "tested": tested,
                "detP_nonzero": detp_nonzero,
                "detU_nonzero": detu_nonzero,
                "wall_seconds": total_wall,
                "E": E,
                "R": R,
                "detP": dp,
                "detU": du,
            }

        # Exclude this exact (E,R) assignment while allowing other matchings.
        literals = []
        set_e, set_r = set(E), set(R)
        for s, y in e.items():
            literals.append(y.Not() if s in set_e else y)
        for r, y in rsel.items():
            literals.append(y.Not() if r in set_r else y)
        model.AddBoolOr(literals)

    return {
        "p": p,
        "gamma": gamma,
        "beta": beta,
        "status": terminal_status if tested < max_solutions else "SOLUTION_LIMIT",
        "tested": tested,
        "detP_nonzero": detp_nonzero,
        "detU_nonzero": detu_nonzero,
        "wall_seconds": total_wall,
        "examples": first_zero_examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--max-solutions", type=int, default=2000)
    parser.add_argument("--time-limit", type=float, default=300.0)
    args = parser.parse_args()

    rows = []
    for gamma in range(1, (args.p - 11) // 4 + 1):
        beta_max = (args.p + 1 - gamma) // 3
        for beta in range(gamma + 4, beta_max + 1, 2):
            row = hunt_pair(
                args.p,
                gamma,
                beta,
                args.max_solutions,
                args.time_limit,
            )
            rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
            if row["status"] == "COUNTEREXAMPLE":
                print(
                    json.dumps(
                        {"p": args.p, "status": "COUNTEREXAMPLE"},
                        sort_keys=True,
                    )
                )
                return

    print(
        json.dumps(
            {
                "p": args.p,
                "status": "NO_COUNTEREXAMPLE",
                "pairs": len(rows),
                "tested": sum(r["tested"] for r in rows),
                "detP_nonzero": sum(r["detP_nonzero"] for r in rows),
                "detU_nonzero": sum(r["detU_nonzero"] for r in rows),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
