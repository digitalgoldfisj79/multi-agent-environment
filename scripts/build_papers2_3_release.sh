#!/usr/bin/env bash
set -euo pipefail

ROOT='publications/fortune-papers-ii-vi-20260724'
DIST="$ROOT/papers2-3-dist"
P2SRC="$ROOT/paper2_revised/manuscript.md"
P3SRC="$ROOT/paper3_pair_sum/manuscript.md"

P2_SHA='0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a'
P3_SHA='7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675'

test "$(sha256sum "$P2SRC" | awk '{print $1}')" = "$P2_SHA"
test "$(sha256sum "$P3SRC" | awk '{print $1}')" = "$P3_SHA"
! grep -nE 'TODO|TBD|PLACEHOLDER|\setminus' "$P2SRC" "$P3SRC"

rm -rf "$DIST"
mkdir -p "$DIST/paper2_release" "$DIST/paper3_release" "$DIST/combined_release" "$DIST/build_logs"
cp "$P2SRC" "$DIST/paper2_release/manuscript.md"
cp "$ROOT/paper2_revised/references.bib" "$DIST/paper2_release/references.bib"
cp "$P3SRC" "$DIST/paper3_release/manuscript.md"

cat > "$DIST/xurl-header.tex" <<'EOF'
\usepackage{xurl}
\urlstyle{same}
EOF
cat > "$DIST/url-wrap.lua" <<'EOF'
function Code(el)
  if string.match(el.text, '^https?://') then
    return pandoc.RawInline('latex', '\\url{' .. el.text .. '}')
  end
end
EOF

python3 - <<'PY'
from pathlib import Path
import re
root=Path('publications/fortune-papers-ii-vi-20260724')
dist=root/'papers2-3-dist'
rows=[]
for srcdir,key in [('paper2_revised','paper2'),('paper3_pair_sum','paper3')]:
    source=(root/srcdir/'manuscript.md').read_text(encoding='utf-8')
    rendered=source.replace('\\Bigl','\\left').replace('\\Bigr','\\right')
    rendered,tags=re.subn(r'\\tag\{([^}]+)\}',r'\\qquad \\text{(\1)}',rendered)
    (dist/f'{key}_docx_source.md').write_text(rendered,encoding='utf-8')
    rows.append((key,source.count('\\Bigl'),source.count('\\Bigr'),tags))
with (dist/'TYPESETTING_COUNTS.tsv').open('w',encoding='utf-8') as f:
    f.write('paper\tBigl\tBigr\ttags\n')
    for row in rows: f.write('\t'.join(map(str,row))+'\n')
PY

pandoc "$DIST/paper2_docx_source.md" \
  --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex \
  --to=docx --standalone --citeproc \
  --bibliography="$ROOT/paper2_revised/references.bib" \
  -o "$DIST/paper2_release/Paper_II_Prime_Detection_at_Primorial_Centres.docx"
pandoc "$DIST/paper3_docx_source.md" \
  --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex \
  --to=docx --standalone \
  -o "$DIST/paper3_release/Paper_III_Pair_Sum_Rigidity.docx"

python3 - <<'PY'
from datetime import datetime, timezone
from docx import Document
from docx.shared import Mm, Pt
from pathlib import Path
fixed=datetime(2026,7,24,12,0,0,tzinfo=timezone.utc)
for path in Path('publications/fortune-papers-ii-vi-20260724/papers2-3-dist').glob('paper*_release/*.docx'):
    doc=Document(path)
    for sec in doc.sections:
        sec.page_width=Mm(210); sec.page_height=Mm(297)
        sec.top_margin=Mm(23); sec.bottom_margin=Mm(23)
        sec.left_margin=Mm(24); sec.right_margin=Mm(24)
    doc.styles['Normal'].font.size=Pt(10.5)
    doc.core_properties.created=fixed
    doc.core_properties.modified=fixed
    doc.save(path)
PY

set +e
pandoc "$P2SRC" \
  --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex \
  --standalone --citeproc --bibliography="$ROOT/paper2_revised/references.bib" \
  --lua-filter="$DIST/url-wrap.lua" --include-in-header="$DIST/xurl-header.tex" \
  --pdf-engine=xelatex -V geometry:margin=24mm -V papersize:a4 \
  -o "$DIST/paper2_release/Paper_II_Prime_Detection_at_Primorial_Centres.pdf" \
  2>"$DIST/build_logs/paper2_xelatex.stderr"
R2=$?
pandoc "$P3SRC" \
  --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex \
  --standalone --lua-filter="$DIST/url-wrap.lua" --include-in-header="$DIST/xurl-header.tex" \
  --pdf-engine=xelatex -V geometry:margin=24mm -V papersize:a4 \
  -o "$DIST/paper3_release/Paper_III_Pair_Sum_Rigidity.pdf" \
  2>"$DIST/build_logs/paper3_xelatex.stderr"
R3=$?
set -e
test "$R2" -eq 0 && test "$R3" -eq 0
! grep -q 'Missing character' "$DIST/build_logs/paper2_xelatex.stderr"
! grep -q 'Missing character' "$DIST/build_logs/paper3_xelatex.stderr"

# Add exact audit records from the audit branch.
git fetch origin gpt56/papers2-3-final-audit-20260724
REF='origin/gpt56/papers2-3-final-audit-20260724'
BASE='fortune-conjecture/papers2-3-final-audit-20260724'
for f in INDEPENDENT_CHECKS.md PAPER_II_FIDELITY_MATRIX.md PAPER_III_FIDELITY_MATRIX.md AUDIT_REPORT.md FRESH_HOSTILE_REVIEW_PAPER_II_QWEN3_14B_AWQ.md FRESH_HOSTILE_REVIEW_PAPER_III_QWEN3_14B_AWQ.md HOSTILE_REVIEW_DISPOSITION.md FIDELITY_AND_EXTERNAL_REVIEW_GATES.md; do
  git show "$REF:$BASE/$f" > "$DIST/combined_release/$f"
done
if git cat-file -e "$REF:$BASE/VISUAL_QA_REPORT.md" 2>/dev/null; then
  git show "$REF:$BASE/VISUAL_QA_REPORT.md" > "$DIST/combined_release/VISUAL_QA_REPORT.md"
fi
cp "$DIST/combined_release/"*.md "$DIST/paper2_release/"
cp "$DIST/combined_release/"*.md "$DIST/paper3_release/"

{
  echo '# Canonical build manifest'
  echo
  echo '- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`'
  echo "- Paper II source SHA-256: \`$P2_SHA\`"
  echo "- Paper III source SHA-256: \`$P3_SHA\`"
  echo '- Long-URL wrapping: inline-code URLs are converted to `\url{...}` for PDF typesetting; `xurl` is enabled.'
  echo "- Pandoc: \`$(pandoc --version | head -1)\`"
  echo "- XeTeX: \`$(xelatex --version | head -1)\`"
  echo "- LibreOffice: \`$(libreoffice --version)\`"
} > "$DIST/combined_release/BUILD_MANIFEST.md"
cp "$DIST/combined_release/BUILD_MANIFEST.md" "$DIST/paper2_release/"
cp "$DIST/combined_release/BUILD_MANIFEST.md" "$DIST/paper3_release/"

P2="$DIST/paper2_release"
P3="$DIST/paper3_release"
pandoc "$P2/Paper_II_Prime_Detection_at_Primorial_Centres.docx" -t plain -o "$P2/docx_extracted.txt" 2>"$DIST/build_logs/paper2_docx_extract.stderr"
pdftotext -layout "$P2/Paper_II_Prime_Detection_at_Primorial_Centres.pdf" "$P2/pdf_extracted.txt"
pandoc "$P3/Paper_III_Pair_Sum_Rigidity.docx" -t plain -o "$P3/docx_extracted.txt" 2>"$DIST/build_logs/paper3_docx_extract.stderr"
pdftotext -layout "$P3/Paper_III_Pair_Sum_Rigidity.pdf" "$P3/pdf_extracted.txt"

python3 - "$P2/docx_extracted.txt" "$P2/pdf_extracted.txt" "$P3/docx_extracted.txt" "$P3/pdf_extracted.txt" <<'PY'
import re,sys,unicodedata
def norm(path):
    s=open(path,encoding='utf-8',errors='replace').read()
    s=unicodedata.normalize('NFKD',s).lower()
    return ' '.join(re.sub(r'[^a-z0-9]+',' ',s).split())
checks={
  1:[('block','variance','criterion'),('weighted','harmonic','reduction'),('truncation'),('fortune','conjecture','not','proved'),('ai','assistance','disclosure')],
  2:[('block','variance','criterion'),('weighted','harmonic','reduction'),('truncation'),('fortune','conjecture','not','proved'),('ai','assistance','disclosure')],
  3:[('difference','multiplicity','dichotomy'),('sub','weibull'),('appendix','b','truncated','singular','series'),('block','averaged','conditional','criterion'),('ai','assistance','disclosure')],
  4:[('difference','multiplicity','dichotomy'),('sub','weibull'),('appendix','b','truncated','singular','series'),('block','averaged','conditional','criterion'),('ai','assistance','disclosure')],
}
for i,path in enumerate(sys.argv[1:],1):
    text=norm(path)
    assert len(text)>12000,(path,len(text))
    for words in checks[i]: assert all(w in text for w in words),(path,words)
    assert not any(x in text for x in ('delta p d sum u','phi2 u','consequently t j h 0'))
PY

pdfinfo "$P2/Paper_II_Prime_Detection_at_Primorial_Centres.pdf" > "$P2/pdfinfo.txt"
pdfinfo "$P3/Paper_III_Pair_Sum_Rigidity.pdf" > "$P3/pdfinfo.txt"
pdffonts "$P2/Paper_II_Prime_Detection_at_Primorial_Centres.pdf" > "$P2/pdffonts.txt"
pdffonts "$P3/Paper_III_Pair_Sum_Rigidity.pdf" > "$P3/pdffonts.txt"
grep -Fq '(A4)' "$P2/pdfinfo.txt"
grep -Fq '(A4)' "$P3/pdfinfo.txt"
! grep -q ' no ' "$P2/pdffonts.txt"
! grep -q ' no ' "$P3/pdffonts.txt"

python3 - <<'PY'
from docx import Document
from pathlib import Path
for path in Path('publications/fortune-papers-ii-vi-20260724/papers2-3-dist').glob('paper*_release/*.docx'):
    doc=Document(path)
    headings=[p for p in doc.paragraphs if p.style and p.style.name.startswith('Heading')]
    assert len(headings)>=18,(path,len(headings))
    assert all(p.text.strip() for p in headings),path
    texts='\n'.join(p.text for p in doc.paragraphs)
    assert 'AI-assistance disclosure' in texts,path
PY

cat > "$P2/TYPESETTING_NORMALISATIONS.md" <<'EOF'
# Typesetting normalisations

Each PDF is generated directly from the exact reviewed Markdown with Pandoc and XeLaTeX. For PDF layout only, inline-code strings beginning with `http://` or `https://` are converted to `\url{...}` and typeset with `xurl`, preventing right-margin clipping without changing their visible content. For editable DOCX/OMML output only, TeX `\tag{...}` commands become appended mathematical labels and `\Bigl`/`\Bigr` become `\left`/`\right`. These conversions preserve notation and equation numbering but not right-margin tag alignment in Word. No mathematical statement, hypothesis, exponent or symbol is changed.
EOF
cp "$P2/TYPESETTING_NORMALISATIONS.md" "$P3/TYPESETTING_NORMALISATIONS.md"

cp -r "$DIST/build_logs" "$DIST/combined_release/build_logs"
for D in "$P2" "$P3"; do
  (cd "$D" && find . -maxdepth 1 -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)
done
cp -r "$P2" "$DIST/combined_release/paper2_release"
cp -r "$P3" "$DIST/combined_release/paper3_release"
(cd "$DIST/combined_release" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)
(cd "$DIST" && zip -X -r -9 Paper_II_release.zip paper2_release >/dev/null && zip -X -r -9 Paper_III_release.zip paper3_release >/dev/null && zip -X -r -9 Papers_II_III_combined_release.zip combined_release >/dev/null)
(cd "$DIST" && sha256sum Paper_II_release.zip Paper_III_release.zip Papers_II_III_combined_release.zip > RELEASE_ZIP_SHA256SUMS.txt)
