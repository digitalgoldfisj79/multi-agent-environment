#!/usr/bin/env python3
"""Centre image-only DOCX paragraphs and require a minimum conversion count."""

from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

if len(sys.argv) not in (2, 3):
    raise SystemExit("usage: centre_docx_equation_images.py DOCX [MINIMUM]")

path = Path(sys.argv[1])
minimum = int(sys.argv[2]) if len(sys.argv) == 3 else 1
if minimum < 0:
    raise SystemExit("MINIMUM must be nonnegative")

if not path.is_file():
    raise SystemExit(f"DOCX not found: {path}")

document = Document(path)
count = 0
for paragraph in document.paragraphs:
    has_drawing = bool(paragraph._p.xpath(".//w:drawing | .//w:pict"))
    if has_drawing and not paragraph.text.strip():
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        count += 1

document.save(path)
print(f"Centred {count} image-only paragraphs in {path}")
if count < minimum:
    raise SystemExit(
        f"Expected at least {minimum} image-only equation paragraphs, found {count}"
    )
