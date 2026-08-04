#!/usr/bin/env python3
"""Static integrity checks for the Fortune formal discovery programme."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "README.md",
    "PROGRAMME.md",
    "PREREGISTERED_GATES.json",
    "CLAIM_LEDGER.md",
    "AXIOM_LEDGER.json",
    "lean-toolchain",
    "lakefile.toml",
    "FortuneFormal.lean",
    "FortuneFormal/Specification.lean",
    "FortuneFormal/Bilateral/Definitions.lean",
    "FortuneFormal/Bilateral/InverseFree.lean",
    "FortuneFormal/Bilateral/F3Closure.lean",
    "FortuneFormal/Quadratic/Model.lean",
    "FortuneFormal/Quadratic/DiscriminantContradiction.lean",
    "FortuneFormal/Quadratic/ReductionInterface.lean",
    "FortuneFormal/Integer/BlockCriterion.lean",
    "FortuneFormal/Frontier/Assumptions.lean",
    "cross-paper/CLAIM_MATRIX.json",
    "cross-paper/AUDIT_REPORT.md",
    "cross-paper/DEPENDENCY_GRAPH.md",
    "scripts/verify_cross_paper_audit.py",
    "scripts/verify_programme.py",
}

BANNED_LEAN_TOKENS = (
    r"\bsorry\b",
    r"\badmit\b",
    r"\bunsafe\b",
)

AXIOM_RE = re.compile(r"^\s*axiom\s+([A-Za-z0-9_']+)", re.MULTILINE)
THEOREM_RE = re.compile(r"^\s*theorem\s+([A-Za-z0-9_']+)", re.MULTILINE)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {relative}: {exc}")


def programme_lean_files() -> list[Path]:
    files = [ROOT / "FortuneFormal.lean"]
    files.extend(sorted((ROOT / "FortuneFormal").rglob("*.lean")))
    return files


def main() -> int:
    missing = sorted(path for path in REQUIRED if not (ROOT / path).is_file())
    if missing:
        fail(f"missing required files: {missing}")

    toolchain = (ROOT / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != "leanprover/lean4:v4.32.0":
        fail(f"unexpected Lean toolchain: {toolchain!r}")

    lakefile = (ROOT / "lakefile.toml").read_text(encoding="utf-8")
    for required_text in (
        'rev = "v4.32.0"',
        'name = "mathlib"',
        'name = "Comparator"',
        'name = "FortuneFormal"',
    ):
        if required_text not in lakefile:
            fail(f"lakefile missing {required_text!r}")

    gates = load_json("PREREGISTERED_GATES.json")
    if gates.get("programme") != "FORTUNE_TEN_PROOFS_FORMAL_V0_1":
        fail("wrong programme identifier")
    if gates.get("base_commit") != "069f47724a3581dc40cfbc9efa3fafd14181ba3e":
        fail("base commit drift")
    gate_ids = [gate.get("id") for gate in gates.get("gates", [])]
    if gate_ids != ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7"]:
        fail(f"unexpected gate sequence: {gate_ids}")

    ledger = load_json("AXIOM_LEDGER.json")
    allowed_rel = ledger.get("allowed_axiom_file")
    if allowed_rel != "FortuneFormal/Frontier/Assumptions.lean":
        fail("allowed axiom file changed")

    expected_full = [entry["name"] for entry in ledger.get("axioms", [])]
    expected_local = [name.rsplit(".", 1)[-1] for name in expected_full]
    if len(expected_local) != len(set(expected_local)):
        fail("duplicate axiom names in ledger")

    found_by_file: dict[str, list[str]] = {}
    all_theorems: set[str] = set()
    for lean_path in programme_lean_files():
        rel = lean_path.relative_to(ROOT).as_posix()
        text = lean_path.read_text(encoding="utf-8")
        for token in BANNED_LEAN_TOKENS:
            if re.search(token, text):
                fail(f"banned Lean token {token!r} in {rel}")
        axioms = AXIOM_RE.findall(text)
        all_theorems.update(THEOREM_RE.findall(text))
        if axioms:
            found_by_file[rel] = axioms

    expected_axiom_files = {allowed_rel} if expected_local else set()
    if set(found_by_file) != expected_axiom_files:
        fail(f"axiom file set differs from ledger: {found_by_file}")
    found_local = found_by_file.get(allowed_rel, [])
    if found_local != expected_local:
        fail(f"axiom declaration order/content differs from ledger: {found_local}")

    formalized_local = [
        entry["name"].rsplit(".", 1)[-1]
        for entry in ledger.get("formalized_claims", [])
    ]
    for name in formalized_local:
        if name not in all_theorems:
            fail(f"formalized ledger theorem not declared: {name}")

    claim_ledger = (ROOT / "CLAIM_LEDGER.md").read_text(encoding="utf-8")
    required_boundary_phrases = (
        "ONE PAPER VII AXIOM REMAINS",
        "ASSUMED pending formalization",
        "Explicitly not claimed",
    )
    for phrase in required_boundary_phrases:
        if phrase not in claim_ledger:
            fail(f"claim ledger missing boundary phrase {phrase!r}")

    assumptions = (ROOT / allowed_rel).read_text(encoding="utf-8")
    for name in expected_local:
        if not re.search(rf"^\s*axiom\s+{re.escape(name)}\b", assumptions, re.MULTILINE):
            fail(f"ledgered axiom not declared: {name}")

    cross = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_cross_paper_audit.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if cross.returncode:
        fail("cross-paper audit failed: " + (cross.stdout + cross.stderr).strip())

    print(cross.stdout.strip())
    print("FORTUNE_FORMAL_PROGRAMME_STATIC_PASS")
    print(f"ledgered_axioms={len(expected_local)}")
    print(f"formalized_claims={len(formalized_local)}")
    print(f"gate_sequence={','.join(gate_ids)}")
    print(f"programme_lean_files={len(programme_lean_files())}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("FAIL: interrupted", file=sys.stderr)
        raise SystemExit(130)
