#!/usr/bin/env python3
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'fortune-corpus-novelty-assurance-v1'

inventory = json.loads((P / 'THEOREM_INVENTORY.json').read_text())['candidates']
matrix = json.loads((P / 'NOVELTY_MATRIX.json').read_text())
rows = matrix['rows']

ids_i = [x['id'] for x in inventory]
ids_m = [x['id'] for x in rows]
assert len(ids_i) == 37, len(ids_i)
assert len(ids_i) == len(set(ids_i))
assert len(ids_m) == len(set(ids_m))
assert set(ids_i) == set(ids_m), (set(ids_i)-set(ids_m), set(ids_m)-set(ids_i))

counts = Counter(r['verdict'] for r in rows)
assert dict(counts) == matrix['counts'], (dict(counts), matrix['counts'])
assert counts['NEW'] == 0
assert counts['STRENGTHENING'] == 0
for r in rows:
    assert r['verdict'] in {'NEW','STRENGTHENING','NEW_SPECIALIZATION','KNOWN_SPECIAL_CASE','ROUTINE_DERIVATION','UNCLEAR'}
    assert r.get('difference')
    if r['verdict'] in {'NEW','STRENGTHENING','NEW_SPECIALIZATION','UNCLEAR'}:
        assert r.get('comparator')

programme = (P / 'PROGRAMME.md').read_text()
status = (P / 'FINAL_STATUS.md').read_text()
assert 'integer Fortune frontier is CLOSED' in programme
assert '`LITERATURE_UNRESOLVED`' in status
assert 'AXIOM_BOUNDARY_IRREDUCIBLE_AT_CURRENT_FORMAL_ABSTRACTION' in status

required = [
    'LITERATURE_COMPARATORS.md','PAPER_IV_AUDIT.md','PAPER_VI_AUDIT.md','PAPER_VII_AUDIT.md',
    'AXIOM_CLOSURE_ASSESSMENT.md','PUBLICATION_PORTFOLIO.md','FINAL_STATUS.md',
    'review_packets/ANALYTIC_NUMBER_THEORY.md',
    'review_packets/ADDITIVE_COMBINATORICS_PROBABILITY.md',
    'review_packets/ARITHMETIC_GEOMETRY_FINITE_FIELDS.md',
    'review_packets/MODULAR_REPRESENTATION_KTHEORY.md'
]
for f in required:
    assert (P / f).is_file(), f

lean_root = ROOT / 'fortune-formal' / 'FortuneFormal'
axioms = []
for f in lean_root.rglob('*.lean'):
    for i,line in enumerate(f.read_text().splitlines(),1):
        if re.match(r'^\s*axiom\s+', line):
            axioms.append((f.relative_to(ROOT).as_posix(), i, line.strip()))
assert len(axioms) == 1, axioms
assert 'p7_k2_certified_normalization' in axioms[0][2]

p6 = (ROOT/'publications/fortune-papers-ii-vi-20260724/paper6_secondary_quotients_replacement/manuscript.md').read_text()
for phrase in [
    'We now justify the\nArtin--Schreier presentation globally rather than only fibrewise.',
    'After cancelling common factors in the logarithmic derivative, write',
    'The $\\mu_n$-action on the\nirreducible $g=1$ locus is free.'
]:
    assert phrase in p6, phrase

print('FORTUNE_ASSURANCE_PROGRAMME_V1_VERIFIED')
print('clusters=37')
print('novelty_counts='+json.dumps(matrix['counts'], sort_keys=True))
print('lean_axioms=1:p7_k2_certified_normalization')
print('terminal=LITERATURE_UNRESOLVED')
print('secondary=AXIOM_BOUNDARY_IRREDUCIBLE_AT_CURRENT_FORMAL_ABSTRACTION')
