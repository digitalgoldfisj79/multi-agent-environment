#!/usr/bin/env python3
"""Translate one exact Singular power-lift column into a Lean MvPolynomial Z certificate.

The generated Lean theorem contains the literal q-free model equations and a
cleared-denominator ideal-membership identity. Mathlib's reflective `ring`
normalizer checks the resulting polynomial equality. The generator is
untrusted; the generated Lean theorem is the auditable kernel-checked object.
"""
from __future__ import annotations

import argparse
import math
import re
from fractions import Fraction
from pathlib import Path


def parse_matrix(path: Path, chart: str):
    txt = path.read_text()
    seg = txt.split(f"{chart}_LIFT_BEGIN", 1)[1].split(f"{chart}_LIFT_END", 1)[0]
    out = {}
    pat = re.compile(r"_\[(\d+),(\d+)\]=([^_]+?)(?=_\[|$)", re.S)
    for m in pat.finditer(seg):
        raw = m.group(3).strip().replace("\n", "")
        terms = []
        for tok in re.findall(r"[+-]?[^+-]+", raw):
            mm = re.fullmatch(r"([+-]?)(\d+(?:/\d+)?)?((?:[ABCU]\d*)*)", tok)
            if mm is None:
                raise ValueError(f"cannot parse token {tok!r}")
            sign = -1 if mm.group(1) == "-" else 1
            coeff = Fraction(mm.group(2)) if mm.group(2) else Fraction(1)
            exps = {v: 0 for v in "ABCU"}
            for vm in re.finditer(r"([ABCU])(\d*)", mm.group(3) or ""):
                exps[vm.group(1)] += int(vm.group(2)) if vm.group(2) else 1
            terms.append((sign * coeff, tuple(exps[v] for v in "ABCU")))
        out[(int(m.group(1)), int(m.group(2)))] = terms
    return out


def lint_matrix(M):
    expected = {(i, j) for i in range(1, 5) for j in range(1, 4)}
    if set(M) != expected:
        raise ValueError(f"unexpected lift matrix coordinates: {sorted(set(M) ^ expected)}")


def lean_int(n: int) -> str:
    return str(n) if n >= 0 else f"({n})"


def list_def(name: str, terms, denom: int) -> str:
    lines = [f"def {name} : List Term := ["]
    for coeff, exps in terms:
        z = coeff * denom
        if z.denominator != 1:
            raise AssertionError("denominator clearing failed")
        lines.append(
            f"  ⟨{lean_int(z.numerator)}, {exps[0]}, {exps[1]}, {exps[2]}, {exps[3]}⟩,"
        )
    lines.append("]")
    return "\n".join(lines)


HEADER = r'''import Mathlib

set_option autoImplicit false
set_option maxRecDepth 1000000
set_option maxHeartbeats 0

noncomputable section

namespace FortuneFormal
namespace Quadratic
namespace GeneratedPowerLift

open MvPolynomial

abbrev P := MvPolynomial (Fin 4) ℤ

def a : P := X 0
def b : P := X 1
def c : P := X 2
def u : P := X 3

structure Term where
  coeff : ℤ
  eA : ℕ
  eB : ℕ
  eC : ℕ
  eU : ℕ

def term (t : Term) : P :=
  C t.coeff * a ^ t.eA * b ^ t.eB * c ^ t.eC * u ^ t.eU

def poly (ts : List Term) : P :=
  ts.foldl (fun acc t => acc + term t) 0

def f0 : P :=
  -4*a^2*b*u + 6*a^2*b - 2*a^2*u + 4*a^2 +
  4*a*b^3 + 4*a*b^2*u + 2*a*b^2 +
  4*a*b*c*u - 8*a*b*c - 4*a*c +
  2*b*c^2 + 2*c^2*u

def f1 : P :=
  -4*a^2*u + 4*a^2 + 2*a*b^2 + 6*a*b*u -
  2*a*b + 8*a*c*u - 8*a*c - 2*b^2*c -
  2*b*c*u - 2*b*c - 4*c^2*u + 4*c^2

def f2 : P :=
  -2*a^2*b - 2*a^2*u - 2*a*b^3*u - a*b^3 -
  2*a*b^2*u^2 - 2*a*b^2*u + 4*a*b*c*u +
  4*a*c*u^2 - b^3*c - 2*b^2*c*u -
  4*b*c^2*u + 2*b*c^2 - 4*c^2*u^2 + 2*c^2*u

def f3 : P :=
  4*a^2*u - 4*a^2 + 2*a*b^2*u - 4*a*b^2 -
  2*a*b*u^2 - 2*a*b*u - 8*a*c*u + 8*a*c -
  b^4 - 2*b^3*u - 2*b^2*c*u + 4*b^2*c -
  2*b*c*u^2 + 6*b*c*u + 4*c^2*u - 4*c^2
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("--chart", choices=["B", "X"], required=True)
    ap.add_argument("--target", type=int, choices=[1, 2, 3], required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    M = parse_matrix(args.input, args.chart)
    lint_matrix(M)
    j = args.target
    denom = 1
    for i in range(1, 5):
        for coeff, _ in M[(i, j)]:
            denom = math.lcm(denom, coeff.denominator)

    chart_expr = {
        "B": ("u * a * (b^2 - 4*c) * b", [3, 3, 3]),
        "X": ("u * a * (b^2 - 4*c) * (a-c)", [2, 4, 4]),
    }
    gexpr, powers = chart_expr[args.chart]
    target_expr = ["u - 1", "b + 2", "(a-c)^2 + 4*a"][j - 1]

    pieces = [HEADER, f"\ndef g : P := {gexpr}\n"]
    for i in range(1, 5):
        pieces.append(list_def(f"m{i}", M[(i, j)], denom))
    pieces.append(
        f'''\ndef denominator : ℤ := {denom}

def target : P := {target_expr}

/-- Exact cleared-denominator {args.chart}-chart target-{j} power-lift identity. -/
theorem certificate :
    C denominator * g^{powers[j-1]} * target =
      f0 * poly m1 + f1 * poly m2 + f2 * poly m3 + f3 * poly m4 := by
  simp [poly, m1, m2, m3, m4, term, denominator, target, g,
    f0, f1, f2, f3, a, b, c, u]
  ring

end GeneratedPowerLift
end Quadratic
end FortuneFormal
'''
    )
    text = "\n\n".join(pieces)
    args.output.write_text(text)
    term_count = sum(len(M[(i, j)]) for i in range(1, 5))
    print(
        f"GENERATED chart={args.chart} target={j} denominator={denom} "
        f"terms={term_count} bytes={len(text)}"
    )


if __name__ == "__main__":
    main()
