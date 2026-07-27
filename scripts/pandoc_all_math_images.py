#!/usr/bin/env python3
"""Render every Pandoc Math node as a transparent TeX image for robust DOCX export.

Input and output are Pandoc JSON on stdin/stdout. Unique TeX expressions are
compiled in one preview document, converted in one pdftocairo call and reused.
Both inline and display equations carry exact TeX alt text. This route is used
only for the editable-prose DOCX publication artefact; the reviewed Markdown
and canonical XeLaTeX PDF remain authoritative and unchanged.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from pypdf import PdfReader

if len(sys.argv) != 2:
    raise SystemExit("usage: pandoc_all_math_images.py MEDIA_DIR")

MEDIA_DIR = Path(sys.argv[1]).resolve()
MEDIA_DIR.mkdir(parents=True, exist_ok=True)


def walk_math(value: Any, output: list[tuple[str, str]]) -> None:
    if isinstance(value, list):
        for item in value:
            walk_math(item, output)
    elif isinstance(value, dict):
        if value.get("t") == "Math":
            math_type, tex = value["c"]
            output.append((math_type["t"], tex))
        else:
            for item in value.values():
                walk_math(item, output)


def render_all(
    items: list[tuple[str, str]],
) -> dict[tuple[str, str], tuple[Path, float, float]]:
    unique: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    tex_path = MEDIA_DIR / "all-equations.tex"
    pdf_path = MEDIA_DIR / "all-equations.pdf"
    preamble = r"""\documentclass[11pt]{article}
\usepackage[active,tightpage]{preview}
\PreviewEnvironment{preview}
\setlength\PreviewBorder{1pt}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools,bm,mathrsfs}
\usepackage{xcolor}
\pagestyle{empty}
\begin{document}
"""
    chunks = [preamble]
    for index, (kind, tex) in enumerate(unique, 1):
        digest = hashlib.sha256(tex.encode()).hexdigest()[:12]
        chunks.append(f"% EQ {index} {kind} {digest}\n")
        chunks.append("\\begin{preview}\n")
        if kind == "InlineMath":
            chunks.append("\\(\\mathstrut " + tex + "\\)\n")
        else:
            chunks.append("\\[\\displaystyle " + tex + "\\]\n")
        chunks.append("\\end{preview}\n")
    chunks.append("\\end{document}\n")
    tex_path.write_text("".join(chunks), encoding="utf-8")

    process = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_path.name,
        ],
        cwd=MEDIA_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if process.returncode:
        (MEDIA_DIR / "pdflatex.log.txt").write_text(
            process.stdout, encoding="utf-8"
        )
        print(process.stdout[-6000:], file=sys.stderr)
        raise SystemExit("pdflatex failed while rendering equations")

    reader = PdfReader(str(pdf_path))
    if len(reader.pages) != len(unique):
        raise SystemExit(
            f"equation page mismatch: {len(reader.pages)} != {len(unique)}"
        )

    prefix = MEDIA_DIR / "eq"
    subprocess.run(
        [
            "pdftocairo",
            "-png",
            "-r",
            "300",
            "-transp",
            str(pdf_path),
            str(prefix),
        ],
        check=True,
    )

    result: dict[tuple[str, str], tuple[Path, float, float]] = {}
    for index, item in enumerate(unique, 1):
        page = reader.pages[index - 1]
        width = float(page.mediabox.width) / 72.0
        height = float(page.mediabox.height) / 72.0
        candidates = list(
            dict.fromkeys(
                list(MEDIA_DIR.glob(f"eq-{index}.png"))
                + list(MEDIA_DIR.glob(f"eq-{index:03d}.png"))
                + list(MEDIA_DIR.glob(f"eq-{index:04d}.png"))
            )
        )
        if not candidates:
            pattern = re.compile(rf"eq-0*{index}\.png$")
            candidates = [
                path for path in MEDIA_DIR.glob("eq-*.png") if pattern.search(path.name)
            ]
        if len(candidates) != 1:
            raise SystemExit(f"equation PNG for page {index}: {candidates}")

        key = hashlib.sha256((item[0] + "\0" + item[1]).encode()).hexdigest()[:20]
        final = MEDIA_DIR / f"math-{key}.png"
        candidates[0].replace(final)
        result[item] = (final, width, height)

    for path in MEDIA_DIR.glob("eq-*.png"):
        path.unlink()
    return result


def alt_text(tex: str) -> list[dict[str, Any]]:
    return [{"t": "Str", "c": "Equation: " + tex}]


document = json.load(sys.stdin)
math_items: list[tuple[str, str]] = []
walk_math(document, math_items)
print(
    f"Found {len(math_items)} math nodes ({len(set(math_items))} unique).",
    file=sys.stderr,
)
rendered = render_all(math_items)
counts = {"InlineMath": 0, "DisplayMath": 0}


def transform(value: Any) -> Any:
    if isinstance(value, list):
        return [transform(item) for item in value]
    if not isinstance(value, dict):
        return value
    if value.get("t") == "Math":
        math_type, tex = value["c"]
        kind = math_type["t"]
        path, width, _height = rendered[(kind, tex)]
        counts[kind] += 1
        css_class = (
            "math-inline-image" if kind == "InlineMath" else "math-display-image"
        )
        physical_width = min(width, 6.20) if kind == "DisplayMath" else width
        return {
            "t": "Image",
            "c": [
                ["", [css_class], [["width", f"{physical_width:.4f}in"]]],
                alt_text(tex),
                [str(path), ""],
            ],
        }
    return {key: transform(item) for key, item in value.items()}


json.dump(transform(document), sys.stdout)
print(
    f"Converted {counts['InlineMath']} inline and "
    f"{counts['DisplayMath']} display math nodes.",
    file=sys.stderr,
)
