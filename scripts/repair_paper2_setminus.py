#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = '632bb8f4fd89a51020069327a11fe57f8ae882e57bd4ae1a9ed0829030c32ce1'
assert hashlib.sha256(text.encode()).hexdigest() == expected

old = '\\(q\\in\\mathcal Q_X\\) and \\(a\\in\\mathbb Z\\setminus\\{0\\}\\)'
new = '\\(q\\in\\mathcal Q_X\\) and \\(a\\in\\mathbb Z\\) with \\(a\\ne0\\)'
assert text.count(old) == 1
text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
