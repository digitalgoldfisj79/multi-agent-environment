#!/usr/bin/env python3
"""Exact CP-SAT test of complementary substitution support for CT1-w1.

For a dominant identity-selected term, Jacobi gives

    det U[R,C1] = sign * det T[Q,M],

where C1=E union {p-3}, Q=Omega\C1, M=Omega\R, and

    T[q,m]=[X^q](X+X^3)^m.

A T entry can be nonzero only if m<=q<=3m and q=m mod 2. This model imposes
full torus grading with beta>=gamma+4 and asks whether the complementary
support graph has a perfect matching. UNSAT proves determinant vanishing
before any modular cancellation.
"""
from __future__ import annotations

import argparse
import json
from ortools.sat.python import cp_model


def solve_case(p: int, gamma: int, time_limit: float) -> dict:
    sum_e = gamma * (p - 1) // 2 - 1
    beta_max = (p + 1 - gamma) // 3
    z_max = (beta_max - (gamma + 4)) // 2
    if z_max < 0:
        return {"p": p, "gamma": gamma, "status": "INFEASIBLE_BY_SIMPLEX"}

    model = cp_model.CpModel()
    omega = range(p)
    mandatory = p - 3

    e = {}
    for s in range(1, p):
        if s == mandatory:
            continue
        e[s] = model.NewBoolVar(f"e_{s}")
    model.Add(sum(s * e[s] for s in e) == sum_e)

    rsel = {r: model.NewBoolVar(f"r_{r}") for r in omega}
    row_sum = sum(r * rsel[r] for r in omega)

    z = model.NewIntVar(0, z_max, "z")
    beta = model.NewIntVar(gamma + 4, beta_max, "beta")
    model.Add(beta == gamma + 4 + 2 * z)
    model.Add(row_sum == sum_e + beta * (p - 1))

    # Q-active rows of T are the complement of C1.
    q_active = {}
    for q in omega:
        if q == 0:
            q_active[q] = 1
        elif q == mandatory:
            q_active[q] = 0
        else:
            q_active[q] = 1 - e[q]

    # M-active columns of T are the complement of R.
    m_active = {m: 1 - rsel[m] for m in omega}

    edges = {}
    by_q = {q: [] for q in omega}
    by_m = {m: [] for m in omega}
    for m in omega:
        for q in range(m, min(p - 1, 3 * m) + 1):
            if (q - m) % 2:
                continue
            x = model.NewBoolVar(f"x_{q}_{m}")
            edges[q, m] = x
            by_q[q].append(x)
            by_m[m].append(x)

    for q in omega:
        model.Add(sum(by_q[q]) == q_active[q])
    for m in omega:
        model.Add(sum(by_m[m]) == m_active[m])

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
        E = sorted(s for s, y in e.items() if solver.Value(y))
        R = sorted(r for r, y in rsel.items() if solver.Value(y))
        matching = sorted((q, m) for (q, m), x in edges.items() if solver.Value(x))
        result.update(
            {
                "beta": solver.Value(beta),
                "E": E,
                "R": R,
                "Q": sorted(set(omega) - set(E) - {mandatory}),
                "M": sorted(set(omega) - set(R)),
                "matching": matching,
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
    for gamma in range(1, (args.p - 11) // 4 + 1):
        row = solve_case(args.p, gamma, args.time_limit)
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
        if row["status"] in {"OPTIMAL", "FEASIBLE"}:
            break

    all_unsat = all(
        row["status"] in {"INFEASIBLE", "INFEASIBLE_BY_SIMPLEX"}
        for row in rows
    )
    print(
        json.dumps(
            {
                "p": args.p,
                "status": (
                    "T_SUPPORT_COUNTEREXAMPLE"
                    if any(row["status"] in {"OPTIMAL", "FEASIBLE"} for row in rows)
                    else "ALL_PROVED_UNSAT"
                    if all_unsat
                    else "INCOMPLETE"
                ),
                "cases": len(rows),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
