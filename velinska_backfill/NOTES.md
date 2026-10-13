# Run log
- 2026-10-13: web.archive.org blocked by session network policy (proxy CONNECT 403). No data fetched.
  backfill.py written; offline self-test on a synthetic fixture (scratchpad, not shipped) passed
  for parse / comments / feed / verify / zip. Expected table sums to 184 across 37 months.
- Next: allow web.archive.org, then `python backfill.py all` (resumable; rerun after interruption).
