#!/usr/bin/env python3
"""Convert four known LibreOffice-incompatible Paper V display equations to PNG images.

Input and output are Pandoc JSON on stdin/stdout. The generated images are produced
from the exact TeX expression with pdflatex and pdftocairo. Ordinary inline and
display mathematics remain untouched and therefore become native OMML in DOCX.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

if len(sys.argv) != 2:
    raise SystemExit("usage: pandoc_targeted_display_math_images.py MEDIA_DIR")

MEDIA_DIR = Path(sys.argv[1]).resolve()
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

TARGET_PATTERNS = (
    r"\setminus\{",
    r"\sum_{q\ne0,2}",
    r"\Bigl",
)
EXPECTED_CONVERSIONS = 4

LATEX_PREFIX = r"""\documentclass[11pt,border=1pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools,bm}
\begin{document}
$\displaystyle """
LATEX_SUFFIX = r"""$
\end{document}
"""

converted: list[str] = []


def render_equation(tex: str) -> tuple[Path, float | None]:
    key = hashlib.sha256(tex.encode("utf-8")).hexdigest()[:20]
    png_path = MEDIA_DIR / f"math-{key}.png"
    if png_path.exists():
        return png_path, None

    with tempfile.TemporaryDirectory() as temp_dir_string:
        temp_dir = Path(temp_dir_string)
        tex_path = temp_dir / "equation.tex"
        tex_path.write_text(LATEX_PREFIX + tex + LATEX_SUFFIX, encoding="utf-8")

        compile_result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_path.name,
            ],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if compile_result.returncode:
            print(compile_result.stdout, file=sys.stderr)
            raise SystemExit(f"pdflatex failed for equation: {tex}")

        pdf_path = temp_dir / "equation.pdf"
        pdf_info = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True)
        page_size_match = re.search(
            r"Page size:\s+([0-9.]+) x ([0-9.]+) pts", pdf_info
        )
        natural_width_inches = (
            float(page_size_match.group(1)) / 72.0 if page_size_match else None
        )

        subprocess.run(
            [
                "pdftocairo",
                "-png",
                "-singlefile",
                "-r",
                "300",
                "-transp",
                str(pdf_path),
                str(png_path.with_suffix("")),
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    return png_path, natural_width_inches


def image_node(tex: str) -> dict[str, Any]:
    png_path, natural_width_inches = render_equation(tex)
    attributes: list[list[str]] = []
    if natural_width_inches is not None:
        attributes.append(["width", f"{min(natural_width_inches, 6.25):.3f}in"])
    converted.append(tex)
    return {
        "t": "Image",
        "c": [
            ["", ["math-display-image"], attributes],
            [{"t": "Str", "c": f"Equation: {tex}"}],
            [str(png_path), ""],
        ],
    }


def transform(value: Any) -> Any:
    if isinstance(value, list):
        return [transform(item) for item in value]
    if not isinstance(value, dict):
        return value

    if value.get("t") == "Math":
        math_type, tex = value["c"]
        if math_type.get("t") == "DisplayMath" and any(
            pattern in tex for pattern in TARGET_PATTERNS
        ):
            return image_node(tex)
        return value

    return {key: transform(item) for key, item in value.items()}


document = json.load(sys.stdin)
json.dump(transform(document), sys.stdout)

print(
    f"Converted {len(converted)} targeted display equations to PNG images.",
    file=sys.stderr,
)
if len(converted) != EXPECTED_CONVERSIONS:
    raise SystemExit(
        f"Expected {EXPECTED_CONVERSIONS} targeted equations, converted {len(converted)}"
    )
