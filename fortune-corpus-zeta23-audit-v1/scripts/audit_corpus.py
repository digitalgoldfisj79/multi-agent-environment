#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[2]
PBASE = ROOT / 'publications/fortune-papers-ii-vi-20260724'
PAPERS = {
  'I': PBASE / 'paper1_collision_geometry/manuscript.md',
  'II': PBASE / 'paper2_revised/manuscript.md',
  'III': PBASE / 'paper3_pair_sum/manuscript.md',
  'IV': PBASE / 'paper4_random_order/manuscript.md',
  'V': PBASE / 'paper5_function_fields_replacement/manuscript.md',
  'VI': PBASE / 'paper6_secondary_quotients_replacement/manuscript.md',
}
CLAIM_STATUS = {
  'V': PBASE / 'paper5_function_fields_replacement/CLAIM_STATUS.md',
  'VI': PBASE / 'paper6_secondary_quotients_replacement/CLAIM_STATUS.md',
}
FROOT = ROOT / 'fortune-formal/FortuneFormal'

report = {'papers': {}, 'formal': {}}
for k, p in PAPERS.items():
    if not p.exists():
        raise SystemExit(f'missing manuscript {p}')
    t = p.read_text(encoding='utf-8')
    headings = re.findall(r'(?m)^#{1,3}\s+(?:Theorem|Proposition|Lemma|Corollary)\b', t)
    comp = len(re.findall(r'(?i)computer-assisted|finite verification|finite census|exact computation', t))
    open_hits = len(re.findall(r'(?i)\bopen\b|remains open|not prove|not claimed', t))
    report['papers'][k] = {
        'path': str(p.relative_to(ROOT)),
        'statement_headings': len(headings),
        'computational_markers': comp,
        'open_boundary_markers': open_hits,
    }
    cs = CLAIM_STATUS.get(k)
    if cs and cs.exists():
        cst = cs.read_text(encoding='utf-8')
        report['papers'][k]['claim_status_open_rows'] = len(re.findall(r'(?mi)^\|.*\bOPEN\b.*\|', cst))
        report['papers'][k]['claim_status_computer_rows'] = len(re.findall(r'(?mi)^\|.*COMPUTER-ASSISTED.*\|', cst))

lean_files = sorted(FROOT.rglob('*.lean'))
axioms = []
decls = 0
sorries = []
for p in lean_files:
    t = p.read_text(encoding='utf-8')
    decls += len(re.findall(r'(?m)^\s*(?:theorem|lemma)\s+', t))
    for m in re.finditer(r'(?m)^\s*axiom\s+([A-Za-z0-9_\.]+)', t):
        axioms.append({'file': str(p.relative_to(ROOT)), 'name': m.group(1)})
    if re.search(r'(?m)\bsorry\b|\badmit\b', t):
        sorries.append(str(p.relative_to(ROOT)))

report['formal'] = {
    'lean_files': len(lean_files),
    'theorem_lemma_declarations': decls,
    'axioms': axioms,
    'files_with_sorry_or_admit': sorries,
    'integer_challenge_exists': (FROOT / 'Comparator/IntegerBlockChallenge.lean').exists(),
    'integer_bridge_exists': (FROOT / 'Comparator/IntegerBlockBridge.lean').exists(),
    'p7_challenge_exists': (FROOT / 'Comparator/P7Challenge.lean').exists(),
}

# Hard trust gates.
if len(axioms) != 1 or axioms[0]['name'] != 'p7_k2_certified_normalization':
    print(json.dumps(report, indent=2))
    raise SystemExit(f'unexpected project axiom inventory: {axioms}')
if sorries:
    print(json.dumps(report, indent=2))
    raise SystemExit(f'sorry/admit found: {sorries}')
if not report['formal']['integer_challenge_exists'] or not report['formal']['integer_bridge_exists']:
    raise SystemExit('integer comparator layer missing')

out = ROOT / 'fortune-corpus-zeta23-audit-v1/AUDIT_SCAN.json'
out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, indent=2))
print('CORPUS_SCAN_PASS')
