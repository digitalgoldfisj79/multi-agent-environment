#!/usr/bin/env python3
"""Set every DOCX section to A4 with 25 mm margins."""

from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.shared import Mm

if len(sys.argv) != 2:
    raise SystemExit("usage: set_docx_a4.py DOCX")

path = Path(sys.argv[1])
if not path.is_file():
    raise SystemExit(f"DOCX not found: {path}")

document = Document(path)
for section in document.sections:
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(25)
    section.left_margin = Mm(25)
    section.right_margin = Mm(25)

document.save(path)
print(f"Set {len(document.sections)} DOCX section(s) to A4 with 25 mm margins: {path}")
