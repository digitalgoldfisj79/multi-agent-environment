#!/usr/bin/env python3
"""Arithmetic regression for the sparse surface canonical class.

The smooth surface Y_p is the complete intersection of degrees 2,...,p-4 in
P^(p-3). Adjunction gives

    K_Y = O(sum(2,...,p-4) - (p-2))
        = O((p-7)(p-2)/2).

Thus p=5 is Fano, p=7 is Calabi--Yau type, and every admitted p>=11 is in the
ample-canonical/general-type range. This checks only the canonical ledger; it is
not a classification of a quotient compactification.
"""
from __future__ import annotations

import json
from pathlib import Path


def row(p: int) -> dict[str, object]:
    ambient_dimension = p - 3
    degrees = list(range(2, p - 3))
    degree_sum = sum(degrees)
    canonical_coefficient = degree_sum - (ambient_dimension + 1)
    assert canonical_coefficient == (p - 7) * (p - 2) // 2
    return {
        "p": p,
        "ambient_projective_dimension": ambient_dimension,
        "complete_intersection_degrees": degrees,
        "canonical_coefficient": canonical_coefficient,
        "classification": (
            "Fano" if canonical_coefficient < 0
            else "trivial-canonical" if canonical_coefficient == 0
            else "ample-canonical"
        ),
    }


def main() -> None:
    rows = [row(p) for p in (5, 7, 11, 17, 23, 29)]
    assert rows[0]["classification"] == "Fano"
    assert rows[1]["classification"] == "trivial-canonical"
    assert all(entry["classification"] == "ample-canonical" for entry in rows[2:])
    output = {
        "classification": "proved adjunction ledger; rational-point theorem not supplied",
        "formula": "K_Y=O((p-7)(p-2)/2)",
        "rows": rows,
        "ruling": {
            "admitted_p_at_least_11_is_fano": False,
            "admitted_p_at_least_11_is_rationally_connected_by_standard_CI_criterion": False,
            "standard_Fano_Esnault_shortcut_applies": False,
            "quotient_compactification_still_requires_separate_analysis": True,
        },
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "sparse_surface_canonical_class_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("SPARSE_SURFACE_CANONICAL_CLASS_VERIFY: PASS")


if __name__ == "__main__":
    main()
