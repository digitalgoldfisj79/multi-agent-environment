# video2cua: running findings log

## Retracted / corrected

- **2026-10-29 — first frame-change detector retracted.** Fraction-of-changed-pixels on a
  320-px thumbnail (threshold 1%) missed a typed value entirely in the synthetic test
  (kept t = [0, 6, 9, 11.5]; expected a frame near t = 3). Typed text is ~0.2% of the
  thumbnail. Replaced with changed-tile counting at ≤1280 px width. Test:
  `test_extract_keeps_one_frame_per_ui_state`, `test_small_typed_text_counts_as_a_change`.

## Platform facts (checked 2026-10-29 against platform.claude.com docs)

| Fact | Source | Status |
|---|---|---|
| On Microsoft Foundry, Claude computer use is only via earlier beta tool versions (`computer_20251124` + `computer-use-2025-11-24`); `computer_toolset_20260801` is not available there | Claude-in-Foundry page, "features not supported"; computer-use page, "Earlier tool versions" | verified (docs) |
| Foundry models listed for `computer_20251124`: Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5, Sonnet 5, Opus 4.8 (+ Opus 4.7/4.6/4.5, Sonnet 4.6) | computer-use page, Availability table | verified (docs) |
| Opus 5.5 / Sonnet 5.5 / Haiku 5.5 take `computer_20251124` only on Bedrock, not Foundry | same | verified (docs) |
| Hosted on Azure: Opus 5.5, Opus 5, Opus 4.8, Sonnet 5.5, Sonnet 5, Haiku 5.5, Haiku 4.5 | Claude-in-Foundry model table | verified (docs) |
| Foundry has no server-side `fallbacks`; use SDK `BetaRefusalFallbackMiddleware` | claude-api skill reference | verified (docs); **not tested against Foundry** |
| Foundry Agent Service Computer Use tool uses OpenAI `computer-use-preview`, preview, registration required | web search snippets; learn.microsoft.com blocked from this session | **unverified** — check Learn page |
| Azure Content Understanding video analyzer GA API `2025-11-01` | web search snippet | **unverified** |
| `computer_20251124` action names/params | Anthropic computer-use-demo `tools/computer.py` | verified (reference code) |

## GPT-6.1 Terra backend (added 2026-10-29)

| Fact | Source | Status |
|---|---|---|
| GPT-6.1 Terra released 2026-10-26; API id `gpt-6.1-terra` | press coverage (InfoWorld, BleepingComputer) via search | verified (secondary sources) |
| GA in Foundry catalog; input text + image (no video); 1050k context, 128k output | ai.azure.com catalog via search snippet | snippet only — catalog page not fetched |
| Computer tool is `{"type": "computer"}` (no display size); `computer_call` carries `actions` (batched) or legacy `action`; reply `computer_call_output` with `computer_screenshot`; `pending_safety_checks` → `acknowledged_safety_checks` | `openai` 3.41.0 SDK type definitions | verified (SDK types) |
| `gpt-6.1-terra` is in the SDK's model list | `openai` 3.41.0 `ChatModel` | verified |
| Azure v1 URL `https://<res>.openai.azure.com/openai/v1/`; key sent as Bearer | SDK request capture (mock transport); Azure accepting it is **unverified** | partly verified |
| Entra scope `https://cognitiveservices.azure.com/.default` | memory | **unverified** |
| developers.openai.com, techcommunity.microsoft.com, learn.microsoft.com | blocked in this session | not read |

## Test results (offline, 2026-10-29)

| Test | Result |
|---|---|
| Full suite `pytest tests/` (after Terra backend) | 20 passed |
| SDK request shape, Terra: both calls POST `/openai/v1/responses`; agent tools = `computer` + 4 strict functions | built OK |
| SDK request shape (mock transport): synthesis = beta stream, `output_config.format` json_schema, `claude-opus-5-5` | built OK |
| SDK request shape: agent = `computer_20251124`, betas `computer-use-2025-11-24,context-management-2025-06-27` (+ middleware adds `fallback-credit-2026-07-01`) | built OK |
| 1080p synthetic recording, 6.5 s, 13 sampled frames | 5 kept: t = 0.0, 3.5, 5.0, 5.5, 6.0 |

## Packaging (2026-10-29)

| Check | Result |
|---|---|
| `python -m build` | `video2cua-0.1.0-py3-none-any.whl` and `video2cua-0.1.0.tar.gz` built |
| Fresh venv, wheel with `[openai]` only | installs without `anthropic`; `video2cua --help` and `analyze --extract-only` work; all modules import |
| Docker image, full Dockerfile | **not built here**: Docker Hub rate-limited (429) and deb.debian.org is blocked by this session's network policy |
| Docker image, variant without apt/ffmpeg and without the browser download | builds; entrypoint prints help; runs as `v2c` in `/data`; `openai` and `anthropic` import |

## Open uncertainties (not yet tested against a live Foundry resource)

1. Whether Foundry accepts the `fallback-credit-2026-07-01` header the middleware adds. If not, every call 400s → set `V2C_FALLBACK_DEPLOYMENT=""`.
2. Whether `context-management-2025-06-27` (`clear_tool_uses_20250919`) is accepted together with computer use on Foundry (platform table says context editing is beta on Foundry; the combination is untested).
3. Real-world frame selection: only synthetic video tested. Real screen recordings (video compression, animations, cursor blink, smooth scrolling) may keep too many or too few frames.
4. Runbook quality from real recordings: not measured. Needs an eval set of recorded tasks with hand-written reference runbooks.
5. Whisper `api_version` default `2024-06-01` and endpoint format: from memory, unverified.
6. Terra: whether computer use on Azure needs an access request (the older `computer-use-preview` did), and whether `previous_response_id` + `truncation="auto"` is the recommended loop for the GA tool — not read from docs.
7. Terra: how its key names look in `keypress` (e.g. `CTRL` vs `Control`); the translator lower-cases and maps common names, but unusual names may fail.
8. Terra: image count / payload limits per Responses request for synthesis (60 high-detail frames) — unknown.
9. Docker: the ffmpeg apt step and `playwright install --with-deps chromium` were not exercised in a build; first real build should be watched.
