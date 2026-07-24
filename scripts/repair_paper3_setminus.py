#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = 'df7f6f2b70c148715e7adba1ec28b159174f369acd4b1e52c095391cfcb49335'
assert hashlib.sha256(text.encode()).hexdigest() == expected

old = ('and then (A.4) gives '
       '\\(u\'=(\\{i,i,k,t\\})\\setminus\\{k,i\\}=\\{i,t\\}\\).')
new = ('and then (A.4) gives \\(u\'=\\{i,t\\}\\) after removing one '
       'occurrence each of \\(k\\) and \\(i\\) from \\(\\{i,i,k,t\\}\\).')
assert text.count(old) == 1
text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
