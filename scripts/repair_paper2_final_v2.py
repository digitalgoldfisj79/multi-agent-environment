#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md')
text = path.read_text(encoding='utf-8')
assert hashlib.sha256(text.encode()).hexdigest() == '56e0774dca0f7f2fb561712a867e3bf6a3ee49837345a378afbb431966028b92'
old = r'''Fix a nonnegative even Schwartz function \(\rho\), and let \(\mathcal Q_X\) be the primes in \([H,2H)\), with \(H\asymp X^2\).'''
new = r'''Fix a nonnegative even Schwartz function \(\rho\) such that
\[
\inf_{1/2\le |t|\le1}\rho(t)>0,
\]
and let \(\mathcal Q_X\) be the primes in \([H,2H)\), with \(H\asymp X^2\). This admissibility condition guarantees \(D_X>0\) and the comparison \(D_X\asymp_\rho|\mathcal Q_X|\) used below.'''
assert text.count(old) == 1
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
