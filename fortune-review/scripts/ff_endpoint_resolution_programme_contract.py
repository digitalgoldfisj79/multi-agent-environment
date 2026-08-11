#!/usr/bin/env python3
"""Validate the machine-readable FERP-0.1 preregistration contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "FF_ENDPOINT_RESOLUTION_PROGRAMME_V0_1_20260730.json"

REQUIRED_STATUSES = {
    "PROVED EXACTLY",
    "PROVED FROM PUBLISHED INPUT",
    "MACHINE-VERIFIED IDENTITY",
    "EMPIRICAL-EXACT FINITE PANEL",
    "EMPIRICAL",
    "CONDITIONAL",
    "RETRACTED",
    "OPEN",
}


def main() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert data["programme"] == "FERP-0.1"
    assert data["date"] == "2026-07-30"
    assert data["frozen_input_head"] == "05d493078a69587b3e8a3bcd707215a0846a6e7e"
    assert set(data["allowed_statuses"]) == REQUIRED_STATUSES
    assert data["endpoint"]["route_a_threshold"] == "M_samp(theta) << q^(3k) poly(k,m)"
    assert data["endpoint"]["route_b"] == "CBEA_FF"

    gates = data["gates"]
    ids = [gate["id"] for gate in gates]
    assert len(ids) == len(set(ids))
    assert ids == [f"G{i}" for i in range(11)]
    known = set()
    for gate in gates:
        assert gate["status"] in REQUIRED_STATUSES
        for prereq in gate.get("prerequisites", []):
            assert prereq in known, (gate["id"], prereq)
        for alternative in gate.get("prerequisites_any", []):
            for prereq in alternative:
                assert prereq in known, (gate["id"], prereq)
        known.add(gate["id"])

    assert gates[0]["status"] == "PROVED EXACTLY"
    assert all(gate["status"] == "OPEN" for gate in gates[1:])
    assert gates[10]["sequence"] == [
        "all monic degree-R",
        "squarefree products of fixed-degree irreducibles",
        "thin product family",
        "chosen walk",
    ]

    route_ids = {route["id"] for route in data["routes"]}
    assert route_ids == {"A", "B"}
    assert len(data["forbidden_claims"]) >= 6
    assert len(data["stop_outcomes"]) == 5

    output = {
        "programme": data["programme"],
        "contract_valid": True,
        "gate_count": len(gates),
        "route_count": len(data["routes"]),
        "allowed_status_count": len(data["allowed_statuses"]),
        "first_open_gate": gates[1]["id"],
        "final_gate": gates[-1]["id"],
        "route_a_threshold": data["endpoint"]["route_a_threshold"],
        "route_b": data["endpoint"]["route_b"],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
