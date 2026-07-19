#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def main() -> None:
    fc = json.loads((DATA / "failure_certificate_audit.json").read_text())
    rows = fc["rows"]
    assert rows[-1]["envelope_over_h"] < rows[0]["envelope_over_h"]
    assert rows[-1]["envelope_over_h"] < 0.01

    zk = json.loads((DATA / "primorial_zero_kernel_audit.json").read_text())
    panels = zk["panels"]
    assert panels[-1]["actual_zero_gap_summary"]["observed_limit_correlation"] > 0.99
    assert panels[-1]["actual_zero_gap_summary"]["kernel_abs_over_N_median"] > 0.1
    assert panels[-1]["actual_zero_gap_summary"]["kernel_abs_over_N_median"] * panels[-1]["N"] > 10 * panels[-1]["sqrt_N"]
    for row in panels[-1]["cutoff_migration"][-3:]:
        assert 0.8 < row["ratio_over_p_n_plus_1"] < 1.01

    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
