#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = '908eb40bbdfb1e88905d539bf978bbbebabffa874bdae98e0e7547b13b840e5f'
assert hashlib.sha256(text.encode()).hexdigest() == expected
old = ('Primes p > ell_j contribute the classical factors '
       '(1 - nu_d(p)/p)(1-1/p)^{-2}; their total product is 1 + O(1/X) '
       'uniformly for 0 < |d| < H (see Lemma 6).')
new = ('For p > ell_j the local factors have the same classical form. '
       'No uniform estimate for the omitted infinite tail is claimed or used; '
       'the conditional theorem is formulated for the finite truncated product S_j(d).')
assert text.count(old) == 1
text = text.replace(old, new)
marker = '\n**Sign and order (the answer to "what actually happens").**'
assert text.count(marker) == 1
start = text.index(marker)
end = text.index('\n---\n\n# Appendix C.', start)
text = text[:start].rstrip() + '\n' + text[end:]
path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
