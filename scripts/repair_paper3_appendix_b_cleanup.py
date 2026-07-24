#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = '520988e8776458d3003cd8c2d7e7ecd0820457d48b30d96b5f46fdd1c0e4701c'
assert hashlib.sha256(text.encode()).hexdigest() == expected

old = '\\sum_{\\substack{u\\ge V\\\\u\\ {\nm odd,\\ squarefree}}}'
new = '\\sum_{\\substack{u\\ge V\\\\u\\text{ odd and squarefree}}}'
assert text.count(old) == 1
text = text.replace(old, new)

old = 'where (B.12) was used after expanding \\(f=1*h\\).'
new = 'where (B.12) was used after expanding \\(f=\\mathbf 1*h\\).'
assert text.count(old) == 1
text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
