#!/usr/bin/env python3
"""Validate the preregistered NDO-0.1 programme contract."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

EXPECTED_GATES = [f"G{i}" for i in range(14)]
REQUIRED_TARGETS = {"QZD_3", "TFP_k", "QZD_k with effective D_k", "CBI_ND", "OAC_FF", "NDC_FF", "FFPR"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", nargs="?", default="fortune-review/data/ff_nonzero_defect_programme_contract.json")
    args = parser.parse_args()
    path = Path(args.contract)
    data = json.loads(path.read_text(encoding="utf-8"))

    assert data["programme"] == "NDO-0.1"
    assert data["frozen_input_head"] == "170c8aeb2545f9bf164258a01857360cc2d50789"
    assert data["regime"]["range"] == "q>=2k"
    gates = data["gates"]
    assert [gate["id"] for gate in gates] == EXPECTED_GATES
    targets = {gate["target"] for gate in gates}
    assert REQUIRED_TARGETS <= targets
    assert data["first_discriminator"]["pass"].startswith("dimension zero")
    assert "positive-dimensional" in data["first_discriminator"]["fail"]
    assert data["sufficient_counting_theorem"] == "#I_nd(q,k) <= k^4 D_k q(q-1)"
    assert len(data["forbidden_shortcuts"]) >= 5
    assert len(data["stop_conditions"]) == 5
    assert any("twisted Frobenius" in item for item in data["forbidden_shortcuts"])
    assert any("Sawin-Shusterman" in item for item in data["literature_audit"])

    print(json.dumps({
        "status": "PASS",
        "programme": data["programme"],
        "gates": len(gates),
        "first_discriminator": data["first_discriminator"],
        "open_targets": [gate["target"] for gate in gates if gate["status"] == "OPEN"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
