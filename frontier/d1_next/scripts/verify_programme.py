#!/usr/bin/env python3
"""Validate the executed direct d=1 programme package and frozen sources."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROGRAMME = ROOT / "frontier" / "d1_next"


def git_blob(commit: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
    ).strip()


def main() -> None:
    manifest = json.loads((PROGRAMME / "SOURCE_MANIFEST.json").read_text())
    gates = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())

    assert manifest["base_commit"] == "c331f740e06a95e5596639800c931e2629ff9178"
    assert manifest["application_audit_commit"] == "b2fc61d060e7c613d555b3401f3f2f574fe6f8e8"
    assert gates["programme"] == "D1_AIRY_HOOK_INTEGRAL_TRANSPORT_V0_2"
    assert gates["governing_issue"] == 41
    assert gates["execution_round"] == 1

    for item in manifest["authoritative_files"]:
        actual = git_blob(item["commit"], item["path"])
        assert actual == item["blob"], (
            item["commit"], item["path"], actual, item["blob"]
        )

    rows = gates["gates"]
    by_id = {row["id"]: row for row in rows}
    priorities = [row["priority"] for row in rows]
    assert len(by_id) == len(rows), "duplicate gate id"
    assert priorities == sorted(priorities), "gate priorities are not ordered"
    assert by_id["ABT-0"]["status"] == "PASS"
    assert by_id["ABT-0"]["remote_compute_allowed"] is False
    assert by_id["ABT-1"]["status"] == "RAW_INTEGRAL_LANE_CLOSED"
    assert "p-adic" in by_id["ABT-1"]["pivot_certificate"]
    assert by_id["ITD-0"]["status"] == "READY_NEW_THEOREM_REQUIRED"
    assert by_id["ABT-5"]["status"] == "BLOCKED_BY_QLINE_MAIN_TERM_AND_TRANSPORT"

    compute = gates["compute"]
    assert compute["max_concurrent_paid_jobs"] == 1
    assert compute["round_1_paid_jobs"] == 0
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
        "ABT_ROUND1_OBJECT_DICTIONARY_20260801.md",
        "ABT_ROUND1_INVARIANT_PIVOT_20260801.md",
        "ITD_ROUND0_OBJECT_AND_OBSTRUCTION_20260801.md",
    ]
    for name in required:
        path = PROGRAMME / name
        assert path.is_file() and path.stat().st_size > 0, name

    print(json.dumps({
        "status": "D1_NEXT_ROUND1_EXACT_PASS",
        "programme": gates["programme"],
        "parent": manifest["base_commit"],
        "application_audit": manifest["application_audit_commit"],
        "frozen_source_blobs": len(manifest["authoritative_files"]),
        "abt0": by_id["ABT-0"]["status"],
        "abt1": by_id["ABT-1"]["status"],
        "active_gate": "ITD-0",
        "secondary_open_theorem": by_id["ABT-1"]["secondary_open_target"],
        "round_1_paid_jobs": compute["round_1_paid_jobs"],
        "remote_terminal_marker": compute["terminal_marker"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
