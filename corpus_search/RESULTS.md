# Running results — Upper Rhine corpus search

## RETRACTED FINDINGS
(none)

## Log
### 2026-09-25 — Exa agent run launched
- Run ID: `agent_run_c848f2243c564180b69a63f0769e3a36` (Exa MCP connector, effort=ultra)
- Query + schema: `upper_rhine_corpus.py` (verbatim from user)
- Direct `api.exa.ai` call blocked by container network policy; run made via Exa MCP instead.
- Earlier unwanted run `agent_run_cf446857c5214e6fbec067046dacf498` (founding-designers query) abandoned; could not be cancelled from here.
- Status: superseded by entry below.
- Nature of task: descriptive corpus construction, not a hypothesis test on Voynich data. Every entry the agent returns is UNVERIFIED until its shelfmark/catalogue URL is checked against the primary catalogue.

### 2026-09-25 ~23:00 UTC — Exa run COMPLETED
- Exa-reported cost: **$19.18** (180.1 agent compute units + 233 searches). Earlier founding-designers run cost: unknown.
- Output: `upper_rhine_corpus_output.json` (structured), `upper_rhine_corpus_raw_response.json` (full response), tables `upper_rhine_corpus_table.{csv,md}`.
- Counts (descriptive, as returned by agent): 42 shelfmarks; 16 with >=3 categories (12 x3, 4 x4); 26 with 2. Digitisation: 26 full / 4 partial / 12 catalogue-only. 101 rejected near-misses.
- Internal checks PASSED: all 17 schema fields present; every assigned category has an evidence entry; no duplicate (repository, shelfmark); strict-subset list == entries with >=3 categories.
- Internal checks FLAGGED — date: 15/42 have only broad/quarter-century dates. Weakest date fits: Zürich ZB Ms. C 150 ("15th c", units undated); Stuttgart HB XI 16 (Part II 16th c); Karlsruhe St. Georgen 73 (qualifying unit c.1400, older catalogue 14th c); St. Gallen Cod. Sang. 1164 & 678, Zürich C 101 (broad "15th c"). Four of the 16 strict-subset entries sit on these weak dates (C 150, St. Georgen 73, HB XI 16, and Aarau MsZQ 57 with alt. 3rd-quarter date).
- NOT VERIFIED: no shelfmark, date, provenance or content claim checked against primary catalogues. URL check blocked by container network policy (all 72 URLs: 61 connection failures, 11 x 403) -> see url_check_blocked.txt.
- Agent's own exhaustion assessment: "substantial saturation of readily searchable descriptions, not global exhaustion".
- Epistemic status: descriptive candidate list from a web agent. P(an arbitrary entry survives primary-catalogue check intact, all fields) = unknown; not estimable until a sample is verified.
