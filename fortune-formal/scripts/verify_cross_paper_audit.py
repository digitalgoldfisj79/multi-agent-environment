#!/usr/bin/env python3
"""Verify the frozen Fortune Papers I–VII source and dependency audit."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "cross-paper" / "CLAIM_MATRIX.json"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    try:
        data = json.loads(MATRIX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load claim matrix: {exc}")

    if data.get("programme") != "FORTUNE_CROSS_PAPER_AUDIT_V0_1":
        fail("wrong audit programme identifier")

    papers = data.get("authoritative_papers", [])
    ids = [paper.get("id") for paper in papers]
    if ids != [f"P{i}" for i in range(1, 8)]:
        fail(f"authoritative paper sequence mismatch: {ids}")

    required_fields = {
        "id", "title", "lane", "source_ref", "path", "git_blob",
        "publication_status", "formalization_priority", "boundary"
    }
    for paper in papers:
        missing = sorted(required_fields - set(paper))
        if missing:
            fail(f"{paper.get('id')} missing fields: {missing}")
        blob = paper["git_blob"]
        if len(blob) != 40 or any(c not in "0123456789abcdef" for c in blob):
            fail(f"{paper['id']} has invalid Git blob: {blob}")
        if "Fortune" not in paper["boundary"] and "fortune" not in paper["boundary"]:
            fail(f"{paper['id']} boundary does not state Fortune scope")

    expected_refs = {
        "P1": "publication/fortune-papers-ii-vi-20260724",
        "P2": "b42da323eccd6f995fc9e2f93373beb1274293ac",
        "P3": "b42da323eccd6f995fc9e2f93373beb1274293ac",
        "P4": "af9350f06e41e94d79f583b2e8fca45b55b92852",
        "P5": "publication/fortune-papers-ii-vi-20260724",
        "P6": "publication/fortune-papers-ii-vi-20260724",
        "P7": "069f47724a3581dc40cfbc9efa3fafd14181ba3e",
    }
    for paper in papers:
        if paper["source_ref"] != expected_refs[paper["id"]]:
            fail(f"{paper['id']} source-ref drift")

    terminal = data.get("terminal_frontiers", [])
    terminal_ids = [entry.get("id") for entry in terminal]
    if terminal_ids != ["INT-SIGNED-TRANSFER", "D1-QLINE-NONSAT", "P7-CUBIC-TF"]:
        fail(f"terminal frontier mismatch: {terminal_ids}")

    lanes = {paper["id"]: paper["lane"] for paper in papers}
    if lanes["P5"] != lanes["P6"] or lanes["P7"] == lanes["P5"]:
        fail("direct d=1 and Paper VII lanes are conflated")
    if lanes["P2"] == lanes["P7"]:
        fail("integer and Paper VII lanes are conflated")

    stale = data.get("stale_or_superseded_records", [])
    stale_paths = {entry.get("path") for entry in stale}
    required_stale = {
        "publications/fortune-papers-ii-vi-20260724/CLAIM_STATUS_ALL.md",
        "publications/fortune-papers-ii-vi-20260724/paper5_function_fields/manuscript.md",
        "publications/fortune-papers-ii-vi-20260724/paper6_airy/manuscript.md",
    }
    if not required_stale.issubset(stale_paths):
        fail("superseded source set is incomplete")

    conflations = data.get("prohibited_conflations", [])
    if len(conflations) < 5:
        fail("insufficient prohibited-conflation rules")

    for required in (
        ROOT / "cross-paper" / "AUDIT_REPORT.md",
        ROOT / "cross-paper" / "DEPENDENCY_GRAPH.md",
    ):
        if not required.is_file():
            fail(f"missing audit document: {required.relative_to(ROOT)}")

    print("FORTUNE_CROSS_PAPER_AUDIT_PASS")
    print("papers=7")
    print("terminal_frontiers=3")
    print("authoritative_refs=" + ",".join(expected_refs[p] for p in ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
