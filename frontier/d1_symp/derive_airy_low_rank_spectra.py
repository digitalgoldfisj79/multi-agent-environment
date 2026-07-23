#!/usr/bin/env python3
"""Derive low-rank characteristic polynomials from exact F and F^3 traces.

Uses self-duality/purity constraints described in
AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

FIRST_TRACES = {
    11: {11: 11**6, 9: -11**5},
    17: {17: 202296965789, 15: 0},
    23: {23: -9735230135207515, 21: 587175767636938},
    29: {29: -17221580757743000101634, 27: 204297536026744106605},
}


def derive() -> dict[str, object]:
    third=json.loads(Path("frontier/d1_symp/airy_odd_power_spectra_results.json").read_text())
    output: dict[str, object]={}
    for p in (11, 17, 23, 29):
        rank=(p-5)//6
        output[str(p)]={}
        for k in (p, p-2):
            s1=FIRST_TRACES[p][k]
            s3=int(third[str(p)][f"TrU3_{k}"])
            weight=k+1
            similitude=p**weight
            record: dict[str, object]={
                "dimension": rank,
                "weight": weight,
                "trace_F": s1,
                "trace_F3": s3,
            }
            if rank == 1:
                record["characteristic_polynomial_coefficients"]=[1, -s1]
                assert s1**3 == s3
            elif rank == 2:
                if s1 == 0:
                    record["determinant_candidates"]=[-similitude, similitude]
                    record["normalized_polynomial_candidates"]=["y^2-1", "y^2+1"]
                else:
                    numerator=s1**3-s3
                    denominator=3*s1
                    assert numerator % denominator == 0
                    determinant=numerator//denominator
                    record["determinant"]=determinant
                    record["characteristic_polynomial_coefficients"]=[1, -s1, determinant]
            elif rank == 3:
                central_size=p**(weight//2)
                candidates=[]
                for central in (central_size, -central_size):
                    pair_trace=s1-central
                    predicted=central**3 + pair_trace**3 - 3*similitude*pair_trace
                    if predicted == s3:
                        e2=central*s1
                        e3=central*similitude
                        candidates.append({
                            "central_eigenvalue": central,
                            "characteristic_polynomial_coefficients": [1, -s1, e2, -e3],
                        })
                assert len(candidates) == 1
                record.update(candidates[0])
            elif rank == 4:
                # Reciprocal sign + is selected by purity; the anti-reciprocal
                # alternative has roots off the purity circle.
                numerator=s1**3 + 3*similitude*s1 - s3
                denominator=3*s1
                assert numerator % denominator == 0
                e2=numerator//denominator
                e3=similitude*s1
                e4=similitude**2
                record["characteristic_polynomial_coefficients"]=[1, -s1, e2, -e3, e4]
            output[str(p)][str(k)]=record
    return output


def main() -> None:
    result=derive()
    Path("frontier/d1_symp/airy_low_rank_spectra_results.json").write_text(
        json.dumps(result, indent=2)+"\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
