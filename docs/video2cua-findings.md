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

## Test results (offline, 2026-10-29)

| Test | Result |
|---|---|
| Full suite `pytest tests/` | 14 passed |
| SDK request shape (mock transport): synthesis = beta stream, `output_config.format` json_schema, `claude-opus-5-5` | built OK |
| SDK request shape: agent = `computer_20251124`, betas `computer-use-2025-11-24,context-management-2025-06-27` (+ middleware adds `fallback-credit-2026-07-01`) | built OK |
| 1080p synthetic recording, 6.5 s, 13 sampled frames | 5 kept: t = 0.0, 3.5, 5.0, 5.5, 6.0 |

## Open uncertainties (not yet tested against a live Foundry resource)

1. Whether Foundry accepts the `fallback-credit-2026-07-01` header the middleware adds. If not, every call 400s → set `V2C_FALLBACK_DEPLOYMENT=""`.
2. Whether `context-management-2025-06-27` (`clear_tool_uses_20250919`) is accepted together with computer use on Foundry (platform table says context editing is beta on Foundry; the combination is untested).
3. Real-world frame selection: only synthetic video tested. Real screen recordings (video compression, animations, cursor blink, smooth scrolling) may keep too many or too few frames.
4. Runbook quality from real recordings: not measured. Needs an eval set of recorded tasks with hand-written reference runbooks.
5. Whisper `api_version` default `2024-06-01` and endpoint format: from memory, unverified.
