#!/usr/bin/env python3
"""Exact CP-SAT search for support-level violations of CT1-w1.

For fixed prime p and grading coordinate gamma, the inverse-substitution minor
has columns C_1=E union {p-3}. An entry U_(r,s) can be nonzero only when

    r >= s, r == s (mod 2), 3r-s <= 2p.

The model imposes the full torus grading

    sum(E)=gamma(p-1)/2-1,
    sum(R)-sum(E)=beta(p-1),
    beta=gamma+4+2z,
    3beta+gamma<=p+1.

SAT is an exact support-level counterexample. UNSAT proves that support alone
excludes beta>=gamma+4 for that (p,gamma).
"""
from __future__ import annotations

import argparse
import json
from ortools.sat.python import cp_model


def solve_case(p: int, gamma: int, time_limit: float) -> dict:
    sum_e = gamma * (p - 1) // 2 - 1
    beta_max = (p + 1 - gamma) // 3
    model = cp_model.CpModel()

    mandatory = p - 3
    optional_columns = [s for s in range(1, p) if s != mandatory]
    columns = optional_columns + [mandatory]

    edges: dict[tuple[int, int], cp_model.IntVar] = {}
    by_col: dict[int, list[cp_model.IntVar]] = {s: [] for s in columns}
    by_row: dict[int, list[cp_model.IntVar]] = {r: [] for r in range(p)}

    for s in columns:
        for r in range(s, p):
            if (r - s) % 2 == 0 and 3 * r - s <= 2 * p:
                x = model.NewBoolVar(f"x_{s}_{r}")
                edges[s, r] = x
                by_col[s].append(x)
                by_row[r].append(x)

    selected: dict[int, cp_model.IntVar] = {}
    for s in optional_columns:
        y = model.NewBoolVar(f"y_{s}")
        selected[s] = y
        model.Add(sum(by_col[s]) == y)
    model.Add(sum(by_col[mandatory]) == 1)

    for vars_r in by_row.values():
        if vars_r:
            model.Add(sum(vars_r) <= 1)

    model.Add(sum(s * selected[s] for s in optional_columns) == sum_e)
    row_sum = sum(r * x for (s, r), x in edges.items())

    z_max = (beta_max - (gamma + 4)) // 2
    if z_max < 0:
        return {
            "p": p,
            "gamma": gamma,
            "sum_e": sum_e,
            "status": "INFEASIBLE_BY_SIMPLEX",
            "wall_seconds": 0.0,
        }

    z = model.NewIntVar(0, z_max, "z")
    beta = model.NewIntVar(gamma + 4, beta_max, "beta")
    model.Add(beta == gamma + 4 + 2 * z)
    model.Add(row_sum == sum_e + beta * (p - 1))
    model.Maximize(beta)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    solver.parameters.cp_model_presolve = True
    status = solver.Solve(model)
    status_name = solver.StatusName(status)

    result = {
        "p": p,
        "gamma": gamma,
        "sum_e": sum_e,
        "beta_min": gamma + 4,
        "beta_max": beta_max,
        "status": status_name,
        "wall_seconds": solver.WallTime(),
        "branches": solver.NumBranches(),
        "conflicts": solver.NumConflicts(),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        E = sorted(s for s, y in selected.items() if solver.Value(y))
        pairs = sorted((s, r) for (s, r), x in edges.items() if solver.Value(x))
        R = sorted(r for _, r in pairs)
        result.update(
            {
                "beta": solver.Value(beta),
                "row_sum": sum(R),
                "E": E,
                "R": R,
                "matching": pairs,
                "grading_check": sum(R) - sum(E),
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--time-limit", type=float, default=300.0)
    args = parser.parse_args()

    rows = []
    max_gamma = (args.p - 11) // 4
    for gamma in range(1, max_gamma + 1):
        row = solve_case(args.p, gamma, args.time_limit)
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
        if row["status"] in {"OPTIMAL", "FEASIBLE"}:
            break

    solved_unsat = all(
        r["status"] in {"INFEASIBLE", "INFEASIBLE_BY_SIMPLEX"} for r in rows
    )
    print(
        json.dumps(
            {
                "p": args.p,
                "status": (
                    "SUPPORT_COUNTEREXAMPLE"
                    if any(r["status"] in {"OPTIMAL", "FEASIBLE"} for r in rows)
                    else "ALL_PROVED_UNSAT"
                    if solved_unsat
                    else "INCOMPLETE"
                ),
                "cases": len(rows),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
