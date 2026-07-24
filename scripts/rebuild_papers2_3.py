#!/usr/bin/env python3
import json
import pathlib
import subprocess

ROOT = pathlib.Path('publications/fortune-papers-ii-vi-20260724')
P2 = ROOT / 'paper2_revised'
P3 = ROOT / 'paper3_pair_sum'
P2.mkdir(parents=True, exist_ok=True)
P3.mkdir(parents=True, exist_ok=True)


def show(ref: str, path: str) -> str:
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], text=True)


ref2 = 'origin/archive/fortune-paper2-20260720'
base2 = 'fortune-conjecture/paper2-prime-detection-20260720/manuscript'
parts = [
    show(ref2, f'{base2}/part_1_front_matter_to_reciprocal_frame.md'),
    show(ref2, f'{base2}/part_2_moments_mobius_and_density_obstruction.md'),
    show(ref2, f'{base2}/part_3_fourier_density_one_and_harmonic_scale.md'),
    show(ref2, f'{base2}/part_4_methods_reproducibility_and_boundary.md'),
]
p2 = '\n\n'.join(x.rstrip() for x in parts) + '\n'
p2 = p2.replace('date: "20 July 2026"', 'date: "24 July 2026"', 1)
p2 = p2.replace(
    'Moreover, the classical individual factorial bounds are non-saving at the critical length '
    '\\(N\\asymp q^{1/2}/\\log q\\). This analogy therefore identifies the missing structure rather than supplying a theorem.',
    'The available factorial technology exploits that bounded-degree shift structure, which is absent for primorial prefixes. This analogy therefore identifies the missing structure rather than supplying a theorem.'
)
disclosure = '''\n# AI-assistance disclosure\n\nThe research programme used large language models for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical claim presented as a theorem is tied to an explicit proof or an independently reproducible exact computation. Conjectural, conditional, computational, diagnostic, and negative results are labelled separately. The named author takes responsibility for the content, citations, code, and final presentation.\n\n'''
p2 = p2.replace('\n# References\n', disclosure + '# References\n', 1)
P2.joinpath('manuscript.md').write_text(p2, encoding='utf-8')
P2.joinpath('references.bib').write_text(
    show(ref2, 'fortune-conjecture/paper2-prime-detection-20260720/references.bib'), encoding='utf-8'
)

ref3 = 'origin/claude/experimental-branch-review-am0zpg'
current = P3.joinpath('manuscript.md').read_text(encoding='utf-8')
if '# Appendix A. Complete kernel-theory proof' in current:
    current = current.split('# Appendix A. Complete kernel-theory proof', 1)[0].rstrip() + '\n'
main, refs = current.split('# References', 1) if '# References' in current else (current, '')

addendum = show(ref3, 'PAPER2_ADDENDUM.md')
addendum_body = addendum[addendum.index('## A.1 Notation and the rigidity lemma'):]

ms = json.loads(show(ref3, 'frontier/workbench/msLemma.develop.json'))['writeup']
ms_body = '## B.1 The truncated singular series' + ms.split('## 1. The truncated singular series', 1)[1]
for marker in ('\n## 4.', '\n## 4 '):
    if marker in ms_body:
        ms_body = ms_body.split(marker, 1)[0].rstrip() + '\n'
        break
ms_body = (ms_body
    .replace('## 2. Exact second-moment identity', '## B.2 Exact second-moment identity')
    .replace('## 3. The second-moment asymptotic', '## B.3 The second-moment bound')
    .replace('**Lemma 1.**', '**Lemma B.1.**')
    .replace('**Lemma 2 (exact divisor identity).**', '**Lemma B.2 (exact divisor identity).**')
    .replace('**Lemma 3 (proved part).**', '**Lemma B.3 (proved bound).**')
    .replace("**Lemma 3' (sharp constant — provable-sketch).**", "**Remark B.4 (sharp constant — non-load-bearing sketch).**"))

cond = show(ref3, 'CONDITIONAL_HL_BLOCK.md')
cond_body = cond[cond.index('## Theorem (block-averaged conditional criterion)'):]
cond_body = (cond_body
    .replace('## Theorem (block-averaged conditional criterion)', '## C.1 Block-averaged conditional criterion', 1)
    .replace('## Proof', '### Proof', 1)
    .replace('## Remarks', '## C.2 Remarks', 1))

appendices = '''\n# Appendix A. Complete kernel-theory proof\n\nThis appendix reproduces the frozen proof source formerly issued as the Paper II addendum. Its `A.*` numbering is retained deliberately so that the circulation manuscript can be checked line by line against frozen blob `71a9ad70c7164bcd94b92743fff3d8088c9a158b`.\n\n''' + addendum_body.rstrip() + '''\n\n# Appendix B. Truncated singular-series proof\n\nThe sharp Dickman constant discussed below is explicitly a non-load-bearing sketch. The exact divisor identity and the bound `|T_j(H)| <= 2H log X` are the proved inputs used by the conditional theorem.\n\n''' + ms_body.rstrip() + '''\n\n# Appendix C. Corrected conditional Hardy--Littlewood theorem\n\nThis appendix reproduces the corrected block-averaged theorem from frozen blob `41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef`. It supersedes the earlier pointwise formulation, which was vacuously strong.\n\n''' + cond_body.rstrip() + '\n'
P3.joinpath('manuscript.md').write_text(main.rstrip() + '\n\n' + appendices + '\n\n# References' + refs, encoding='utf-8')

rows = [
    ('II', 'archived manuscript part 1', 'archive/fortune-paper2-20260720', f'{base2}/part_1_front_matter_to_reciprocal_frame.md', '79da1c81b57b051cf8527889e84a6fe1161eb3fe'),
    ('II', 'archived manuscript part 2', 'archive/fortune-paper2-20260720', f'{base2}/part_2_moments_mobius_and_density_obstruction.md', '9fcaf35daded3706bc632751e25c634fca93e747'),
    ('II', 'archived manuscript part 3', 'archive/fortune-paper2-20260720', f'{base2}/part_3_fourier_density_one_and_harmonic_scale.md', '83fd9649e0481549753d82789f7014c346aa3013'),
    ('II', 'archived manuscript part 4', 'archive/fortune-paper2-20260720', f'{base2}/part_4_methods_reproducibility_and_boundary.md', 'ea2a6736509996e5f7d8a564349635d082829789'),
    ('III', 'kernel proof', 'claude/experimental-branch-review-am0zpg', 'PAPER2_ADDENDUM.md', '71a9ad70c7164bcd94b92743fff3d8088c9a158b'),
    ('III', 'singular-series proof', 'claude/experimental-branch-review-am0zpg', 'frontier/workbench/msLemma.develop.json', 'abe5cbb0577e35bf05db2302de6a7d73afd991bc'),
    ('III', 'conditional theorem', 'claude/experimental-branch-review-am0zpg', 'CONDITIONAL_HL_BLOCK.md', '41d6f8e9df068bfed2f55fe9c2fd926a2b1423ef'),
]
ROOT.joinpath('PAPERS_II_III_FROZEN_SOURCE_MANIFEST.tsv').write_text(
    'paper\trole\tref\tpath\tblob\n' + ''.join('\t'.join(r) + '\n' for r in rows), encoding='utf-8'
)
