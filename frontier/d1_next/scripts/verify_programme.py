#!/usr/bin/env python3
"""Validate the frozen direct d=1 programme package and source blobs."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROGRAMME = ROOT / "frontier" / "d1_next"


def git_blob(path: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"HEAD:{path}"], cwd=ROOT, text=True
    ).strip()


def main() -> None:
    manifest = json.loads((PROGRAMME / "SOURCE_MANIFEST.json").read_text())
    gates = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())

    assert manifest["base_commit"] == "c331f740e06a95e5596639800c931e2629ff9178"
    assert gates["programme"] == "D1_AIRY_HOOK_INTEGRAL_TRANSPORT_V0_1"
    assert gates["governing_issue"] == 41

    for item in manifest["authoritative_files"]:
        path = item["path"]
        actual = git_blob(path)
        expected = item["blob"]
        assert actual == expected, (path, actual, expected)

    gate_rows = gates["gates"]
    ids = [row["id"] for row in gate_rows]
    priorities = [row["priority"] for row in gate_rows]
    assert len(ids) == len(set(ids)), "duplicate gate id"
    assert priorities == sorted(priorities), "gate priorities are not ordered"
    assert gate_rows[0]["id"] == "ABT-0"
    assert gate_rows[0]["status"] == "READY"
    assert gate_rows[0]["remote_compute_allowed"] is False
    assert next(row for row in gate_rows if row["id"] == "ITD-0")["status"] == "CONDITIONAL_ON_FORMAL_ABT_OBSTRUCTION"

    compute = gates["compute"]
    assert compute["max_concurrent_paid_jobs"] == 1
    assert compute["smoke_timeout_minutes"] <= 10
    assert compute["ordinary_timeout_minutes"] <= 30
    assert compute["heavy_timeout_minutes"] <= 60
    assert compute["exceptional_hard_max_minutes"] <= 120
    assert compute["stall_cancel_minutes"] <= 10
    assert compute["terminal_marker"] == "RUNNING_REMOTE_JOBS=0"

    required = [
        "PROGRAMME.md",
        "PREREGISTERED_GATES.json",
        "SOURCE_MANIFEST.json",
        "CLAIM_LEDGER.md",
        "REMOTE_COMPUTE_PROTOCOL.md",
        "CURRENT_STATUS.md",
    ]
    for name in required:
        path = PROGRAMME / name
        assert path.is_file() and path.stat().st_size > 0, name

    print(
        json.dumps(
            {
                "status": "D1_NEXT_PROGRAMME_EXACT_PASS",
                "programme": gates["programme"],
                "parent": manifest["base_commit"],
                "frozen_source_blobs": len(manifest["authoritative_files"]),
                "first_gate": "ABT-0",
                "fallback_gate": "ITD-0",
                "max_paid_jobs": compute["max_concurrent_paid_jobs"],
                "remote_terminal_marker": compute["terminal_marker"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
