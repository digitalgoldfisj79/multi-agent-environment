#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')
assert hashlib.sha256(text.encode()).hexdigest() == '8b9aeac471774f86080cc5e444179d9533bf8f492dedc99a4647f87987b6bae1'
old_author = '  - "Edward Stewart Anthony Bozzard"'
new_author = '  - "Edward Stewart Anthony Bozzard (ORCID 0009-0002-4052-0994)"'
assert text.count(old_author) == 1
text = text.replace(old_author, new_author)
old_refs = '# References\n'
new_refs = '''# References

1. E. S. A. Bozzard, *Prime Detection at Primorial Centres: Reciprocal Frames, Exact Moments, and Structural Obstructions*, companion manuscript, 2026.
2. G. H. Hardy and J. E. Littlewood, “Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes”, *Acta Mathematica* **44** (1923), 1–70.
3. N. G. de Bruijn, “On the number of positive integers $\\le x$ and free of prime factors $>y$”, *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, Series A* **54** (1951), 50–60.
4. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., Graduate Studies in Mathematics 163, American Mathematical Society, 2015.
'''
assert text.count(old_refs) == 1 and text.endswith(old_refs)
text = text[:-len(old_refs)] + new_refs
path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
