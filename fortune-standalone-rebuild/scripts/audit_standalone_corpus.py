#!/usr/bin/env python3
"""Final corpus-level audit for the 2026-08-11 standalone Fortune manuscripts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "publications/fortune-standalone-20260811"

PAPERS = [
    ("I", "paper1_collision_geometry", 25, "structural collision geometry"),
    ("II", "paper2_prime_pair_detection", 24, "exact prime-pair detector and reciprocal-frame obstructions"),
    ("III", "paper3_pair_sum_rigidity", 11, "superincreasing pair-sum rigidity and covariance application"),
    ("IV", "paper4_random_product_paths", 14, "random-order reciprocal-frame theorem"),
    ("V", "paper5_fortunate_polynomials", 11, "function-field normal forms and crown geometry"),
    ("VI", "paper6_secondary_traces_quotients", 16, "secondary traces and quotient geometry"),
    ("VII", "paper7_bilateral_endpoint_incidence", 7, "bilateral endpoint incidence and quadratic emptiness"),
    ("Synthesis", "synthesis_conditional_and_barriers", 1, "conditional Fortune criterion and obstruction ring"),
]

REQUIRED_FILES = ["manuscript.md", "CLAIM_STATUS.md", "SOURCE_MANIFEST.json", "REFEREE_READ.md", "REPRODUCIBILITY.md"]

# Publication-facing manuscripts must not require internal programme vocabulary or
# another paper merely to make a load-bearing statement intelligible.
FORBIDDEN = [
    "RUHL-FM", "INT-AOD", "INT-ISC", "INT-SCME", "D1-QLINE-NONSAT", "P7-CUBIC-TF",
    "preceding paper", "following paper", "next paper", "input to Paper", "six-paper sequence",
    "this series", "Correction notice", "first circulation edition", "TODO", "TBD",
]


def title_of(text: str) -> str:
    # YAML title first; Markdown H1 fallback.
    m = re.search(r'^title:\s*[|]?\s*\n?\s*"?([^"\n]+)', text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else "Untitled"


def count_labels(key: str, text: str) -> int:
    if key == "I":
        return len(re.findall(r'^#{2,3} (?:Theorem|Proposition|Lemma|Corollary) [0-9]+\.[0-9]+', text, re.M))
    if key in {"II", "III"}:
        return len(re.findall(r'^\*\*(?:Theorem|Proposition|Lemma|Corollary) [0-9]+\.[0-9]+', text, re.M))
    if key in {"IV", "V", "VI", "VII"}:
        return len(re.findall(r'^## (?:Theorem|Proposition|Lemma|Corollary) [0-9]+\.[0-9]+', text, re.M))
    return len(re.findall(r'^### Theorem [0-9]+\.[0-9]+', text, re.M))


def main() -> None:
    records = []
    total_words = 0
    total_statements = 0

    for key, dirname, expected_count, role in PAPERS:
        d = PUB / dirname
        assert d.is_dir(), f"missing publication directory: {d}"
        for filename in REQUIRED_FILES:
            assert (d / filename).is_file(), f"{key}: missing {filename}"

        text = (d / "manuscript.md").read_text(encoding="utf-8")
        status = (d / "CLAIM_STATUS.md").read_text(encoding="utf-8")
        referee = (d / "REFEREE_READ.md").read_text(encoding="utf-8")
        repro = (d / "REPRODUCIBILITY.md").read_text(encoding="utf-8")
        manifest = json.loads((d / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))

        bad = [token for token in FORBIDDEN if token in text]
        assert not bad, f"{key}: forbidden internal/stale tokens {bad}"
        assert manifest.get("logical_cross_paper_dependencies") == 0, f"{key}: cross-paper dependency not zero"
        assert manifest.get("fortune_proved") is False, f"{key}: Fortune status not explicitly false"
        count = count_labels(key, text)
        assert count == expected_count, f"{key}: statement count {count}, expected {expected_count}"
        manifest_count = manifest.get("statement_count", manifest.get("numbered_theorem_count"))
        assert manifest_count == expected_count, f"{key}: manifest count {manifest_count}, expected {expected_count}"
        assert "Disposition:" in referee, f"{key}: missing referee disposition"
        assert "reproduc" in repro.lower() or "computation" in repro.lower() or "finite" in repro.lower(), f"{key}: empty reproducibility boundary"

        # Paper-specific invariants that protect the major repairs/boundaries.
        if key == "II":
            assert "# Open analytic boundary" in text
            assert "No prime-pair asymptotic and no proof of Fortune's conjecture is claimed." in text
        elif key == "III":
            assert r"r(D)\le1" in text
            assert r"otherwise \(r(D)=1\)" not in text
            assert "Proposition 7.1 (exact fourth and centred second moments)" in text
            assert "PASS_AFTER_TWO_SOURCE_REPAIRS" in referee
        elif key == "IV":
            assert "Reciprocal-Frame Bounds Along Random Primorial-Product Paths" in text
            assert "Prime Detection Along Random" not in text
            assert "not by itself a prime-pair theorem" in text
        elif key == "V":
            assert manifest.get("universal_crown_proved") is False
            assert manifest.get("integer_transfer_proved") is False
            assert "strict q-line nonsaturation" in status
        elif key == "VI":
            assert manifest.get("universal_crown_proved") is False
            assert manifest.get("integer_transfer_proved") is False
            assert "Theorem 11.2 multiplied by" not in text
            assert "exactly the second formula of Theorem 11.2" in text
        elif key == "VII":
            assert manifest.get("quadratic_lean_status") == "DERIVED_WITH_LEDGERED_AXIOM"
            assert manifest.get("custom_axiom") == "FortuneFormal.p7_k2_certified_normalization"
            assert "not axiom-free" in text
            assert "p7_k2_certified_normalization" in text
        elif key == "Synthesis":
            assumptions = manifest.get("beta_certificate_assumptions")
            assert assumptions == {"epsilon": 0.1, "U_over_L_max": 1.1, "beta": 5}, assumptions
            assert "Selected-centre signed prime-tuple problem" in text
            assert "Fortune's conjecture remains open." in text

        words = len(text.split())
        total_words += words
        total_statements += count
        records.append({
            "paper": key,
            "directory": dirname,
            "title": title_of(text),
            "role": role,
            "word_count": words,
            "labelled_statement_count": count,
            "logical_cross_paper_dependencies": 0,
            "referee_disposition": re.search(r'`([^`]+)`', referee).group(1),
        })

    corpus = {
        "programme": "FORTUNE_STANDALONE_PAPERS_V1",
        "date": "2026-08-11",
        "terminal": "STANDALONE_CORPUS_AUDIT_PASS",
        "fortune_status": "NOT_PROVED",
        "integer_mainline": "CLOSED",
        "paper_count": 8,
        "total_manuscript_words": total_words,
        "total_labelled_statements": total_statements,
        "papers": records,
        "global_boundaries": {
            "integer": "jointly signed selected-centre prime-tuple/covariance-transference theorem remains open",
            "function_field_d1": "universal q-line/cubic crown nonvanishing remains open",
            "paper_vii": "quadratic theorem exact computer-assisted; Lean derivation still uses one explicit normalization axiom",
        },
    }
    (PUB / "CORPUS_MANIFEST.json").write_text(json.dumps(corpus, indent=2) + "\n", encoding="utf-8")

    rows = [
        "# Fortune standalone manuscript corpus — 11 August 2026",
        "",
        "This directory is the authoritative standalone publication set produced after the cold review, novelty/assurance audit, Zeta23-style trust audit, and paper-by-paper dependency rebuild.",
        "",
        "Each manuscript is intended to be readable independently. Companion Fortune papers may motivate related questions, but no load-bearing definition, theorem, proof, correction, or evidence classification is imported merely by reference to another paper.",
        "",
        "**Global status:** Fortune's conjecture is not proved. The integer mainline remains closed at the selected-centre signed prime-tuple/covariance frontier. The universal function-field d=1 crown is open. Paper VII's quadratic theorem is exact computer-assisted mathematics; the current Lean derivation retains one explicit normalization axiom.",
        "",
        "| Paper | Standalone role | Words | Labelled statements | Referee disposition |",
        "|---|---|---:|---:|---|",
    ]
    for r in records:
        rows.append(f"| {r['paper']} | {r['role']} | {r['word_count']:,} | {r['labelled_statement_count']} | `{r['referee_disposition']}` |")
    rows += [
        "",
        f"Total manuscript words by whitespace count: **{total_words:,}**. Total labelled statements in the rebuilt publication set: **{total_statements}**.",
        "",
        "Every paper directory contains `manuscript.md`, `CLAIM_STATUS.md`, `SOURCE_MANIFEST.json`, `REFEREE_READ.md`, and `REPRODUCIBILITY.md`; papers using BibTeX also contain a local `references.bib`.",
        "",
        "The source manifests record repairs made during standalone reconstruction. In particular, Paper III corrects the source main-text multiplicity overstatement using the already-correct frozen Appendix A theorem and reproves its exact fourth moment locally; Paper VI closes three former Paper-V dependencies and repairs a point-count wording error; Paper VII states its current formal trust boundary explicitly.",
    ]
    (PUB / "README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"STANDALONE_CORPUS_AUDIT_PASS papers=8 words={total_words} statements={total_statements}")


if __name__ == "__main__":
    main()
