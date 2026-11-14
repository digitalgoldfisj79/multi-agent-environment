# Running log: content engine

## Retracted findings
- **2026-11-14: recipe v1 (Kling 3.0 Turbo, text-to-video, 720p) RETRACTED.** The owner rejected it: generic concept, obviously AI. Its manifest `queue/2026-11-14.json` is on hold and must not be posted.
- **2026-11-14: recipe v2 (Minimax Hailuo 2.3 image-to-video, 768p) RETRACTED.** The owner rejected it: "looks like 2025 AI". The reveal also failed my own frame check. The "proposed new daily mix" built on Hailuo is withdrawn.
- **Root cause of both:** I chose models by lowest credit cost and never priced the current top tier. The owner's own account history (12 Nov) shows Kling 4.0 and GPT Image 2.0, which is the quality bar I should have matched.

---

## 2026-11-14: setup and proof run

### Verified facts (looked up or measured this session)
| Fact | Value | Source |
|---|---|---|
| Higgsfield balance before run | 794.75 credits, Plus plan | `balance` tool |
| Kling 3.0 Turbo, 10 s, 9:16, 720p | 15 credits | `get_cost` preflight |
| Veo 3.1 Lite, 8 s, 9:16 | 12 credits | `get_cost` preflight |
| Seedance 2.5, 10 s, 480p, no audio | 30 credits | `get_cost` preflight |
| GPT Image 2.6, 4:5, jpeg: low / medium / high | 0.25 / 0.5 / 1.5 credits | `get_cost` preflight |
| Today's actual spend | 17.5 credits (15 + 5 × 0.5) | Higgsfield `transactions`, which matches the ledger |
| Kling Turbo output | 720×1280, 24 fps, H.264, AAC audio, 10.04 s | ffprobe |
| Instagram: JPEG only; `is_ai_generated` flag; carousel max 20 | confirmed | Meta content-publishing doc + IG Platform changelog |
| Higgsfield `media_upload` re-host serves `video/mp4` publicly | confirmed (HTTP 200) | curl -I |

### Unverified or assumed
- $ per credit is set to 0.05. It comes from third-party pages quoting about $5 per 100 credits in top-ups, and Plus-plan figures conflict ($39-$59 for 1,000-1,200 credits). It is NOT confirmed on higgsfield.ai.
- Instagram's 24 h API post limit: Meta's own doc says 100 in one place and 50 in another. This doesn't matter at 2 posts a day.
- Whether the GitHub Action fires on a non-default branch push: GitHub's push trigger uses the workflow file in the pushed commit (standard behaviour, but untested in this repo).
- Whether the TikTok publish widget renders in a scheduled cloud session viewed from the Claude app is untested.
- The Instagram token lifetime of about 60 days is from memory and has not been re-checked.

### Proof run
- Trend: cozy holiday cafe / sugar-cookie latte, from 4 trend trackers for 8-13 Nov. Brand variants were excluded.
- Output: 1 Reel and 5 carousel images. All passed `validate.py` and the manual compliance review.
- Spend: 17.5 credits, about $0.88 (estimated).
- Posted: nothing yet. Instagram secrets aren't set and TikTok isn't connected.

### Calibration
| Claim | P(survives 60d) |
|---|---|
| Daily pipeline stays at or under 40 credits per day | 90% |
| Kling Turbo price stays at 15 credits per 10 s | 60% (vendor prices move) |
| Content will "go viral" | not estimable; no engagement data exists yet |

### Post-push checks (2026-11-14, about 07:00 UTC)
- VERIFIED: a push to the non-default branch `ccr-8bbf046b-r7dn0e` triggered `instagram-post` (run 43568905944). With no secrets set, it is expected to post nothing.
- Created scheduled task `trig_019XFhSadowXnQ7ovHP3NVNa`: daily at 11:23 UTC, a fresh session each time, with push notifications.
- BLOCKER: the scheduled task was created without the Higgsfield connector, because this organisation does not allow attaching connectors from a session. Until the owner attaches Higgsfield to the task in the claude.ai scheduled-tasks UI, daily runs will stop at the "Higgsfield tools unavailable" check and report it. They will not spend anything.

## 2026-11-14: insights feedback loop added

The owner supplied Meta's docs for "Instagram API with Instagram Login" and "Media Insights". What those docs confirm:
- The host is `graph.instagram.com` and the latest version is v27.0, which matches the code defaults.
- No Facebook Page is needed.
- The scopes `instagram_business_*` are the right ones.

What was added:
- `engine/ig_insights.py` takes d2 (48 h or more) and d7 snapshots. Metrics are requested one at a time, empty data is stored as null rather than 0, and carousel children are not queried. All of this follows the doc's limitations section.
- `ig_post.verify()` reads `is_ai_generated` back after publishing and raises a warning if it is not true.
- The README now asks for the extra scope `instagram_business_manage_insights`.
- Offline mock test `tests/test_insights_mock.py`: PASSED (idempotent reruns, 48 h gating, null-not-zero, per-metric error isolation, label warning).

PRE-REGISTERED (written before any engagement data exists):
- With fewer than 14 Reels holding d7 snapshots, insights have no effect on topic choice.
- After that, a category is favoured only if its median d7 views exceed the overall median by more than the IQR, with at least 4 posts in the category.
- Anything weaker is logged as "the metric does not resolve this".

Untested against the live API, because there is no token yet. P(insights code works first time against the live API) = 70%. The most likely failure is a metric name or permission error, which is isolated per metric.

## 2026-11-14: quality test v2 (after owner feedback: "ideas poor, video clearly AI")

Diagnosis of v1:
- The concept was generic: a hygge latte with no hook and no payoff.
- It was text-to-video on the cheapest model.
- The prompt used stock-AI descriptors ("film grain, amber bokeh").

Test v2 recipe:
- Concept: "is it cake?" Christmas bauble reveal.
- Start frame: GPT Image 2.6, high quality, 9:16 jpeg, prompted with phone-photo realism (1.5 credits each, 2 frames).
- Video: Minimax Hailuo 2.3 image-to-video, 10 s, 768p (11 credits).
- Higgsfield transactions confirm the spend: 1.5 + 1.5 + 11 = 14 credits.
- Day total: 31.5 credits (about $1.58), under the 40-credit cap.

Result:
- Seconds 0-7 (hand, knife, bauble, marble, window light) are convincingly photographic, which is a large improvement over v1.
- Seconds 7-10, the reveal and payoff, FAIL:
  - The knife turns translucent and floats away.
  - A red glow bleeds onto the marble.
  - The interior mixes vanilla and red-velvet sponge with no consistent structure.
  - There is no audio track.
- Verdict: not postable as is. The weak point is exactly the moment that carries the hook.

Next test, not yet run (the daily cap is reached):
- Supply an END frame as well, a photoreal cut-open bauble cake, so Hailuo interpolates between two fixed frames instead of inventing the interior.
- Expected cost: 2 frames at 1.5 + Hailuo at 11 = 14 credits.

PRE-REGISTERED:
- If the start+end-frame version still shows object morphing or ghosting during the reveal in at least 2 of 4 test clips, the "transformation reveal" format is dropped. The fallback is the simpler physics the models do well: melt, pour, slice of a soft solid, steam.
- n = 1 so far. Nothing here is established.

P(start+end-frame fixes the reveal) = 50%.

## 2026-11-14: top-tier pricing (after second rejection)

All figures are from `get_cost` preflights this session, for 9:16 clips.

| Model | Length, resolution | Credits |
|---|---|---|
| Kling 4.0 | 10 s, 1080p | 32.5 |
| Kling 4.0 | 10 s, 720p | 22.5 |
| Kling 4.0 | 5 s, 1080p | 16.25 |
| Kling 4.0 Flash | 10 s, 720p | 30 |
| Google Veo 3.1 | 8 s | 32 |
| Wan 3.0 | 10 s, 1080p | 35 |
| Gemini Omni Flash 1.2 | 10 s, 1080p | 32.5 |
| Seedance 2.5 Flash | 10 s, 720p | 50 |
| Seedance 2.5 | 5 s, 1080p | 80 |
| Cinema Studio 4.0 | 10 s, 1080p | 160 |

- Candidate recipe v3: 1 high-quality start frame (1.5) + Kling 4.0 10 s 1080p image-to-video (32.5) + 5-image carousel (2.5) = 36.5 credits, under the 40 cap with no retry headroom.
- Not yet run: today has 8.5 credits left.
- The scheduled task is paused until the owner approves a look.
- No quality claim is made for v3. The owner's eye is the test.

## 2026-11-14: bake-off (owner instruction: "optimise for quality, raise the cap to the minimum necessary")

PRE-REGISTERED before viewing any output:
- Same start frame (GPT Image 2.6, high, 2k, 1520x2688) and identical prompt on three models: Kling 4.0 1080p (32.5 cr), Gemini Omni Flash 1.2 1080p (32.5 cr), Seedance 2.5 720p (70 cr). All 10 s, 9:16.
- My frame check FAILS a clip if it shows any of: object morphing or ghosting, the houses moving or deforming, the truck changing shape, sugar behaving like liquid or fog, text or logos appearing.
- The owner's eye is the deciding test. The new daily cap is set by the CHEAPEST model the owner accepts. If the owner accepts none, the cap is not raised and the format question reopens.
- One clip per model is n = 1. A single good or bad render does not establish a model's typical quality.
- One-off bake-off spend: 137.75 credits (about $6.89 at the unconfirmed $0.05/credit). This is authorised test spend, not the new daily level.

### Bake-off result (2026-11-14, frame review at 1 frame per second plus full-size frames at 8 s)

Spend verified against Higgsfield `transactions`: 2.75 + 32.5 + 32.5 + 70 = 137.75 credits. Balance 794.75 at session start, 625.5 now; day total 169.25, which matches.

| Clip | Model | Credits | Output | My frame check |
|---|---|---|---|---|
| A | Kling 4.0, image-to-video | 32.5 | 1080x1912, 24 fps, audio | PASS. The plough pushes sugar forward, the cleared track is behind the truck, sugar dusts the cab. Houses gain chimneys versus the start frame but stay solid. |
| B | Gemini Omni Flash 1.2 | 32.5 | 1080x1920, 24 fps, quiet audio | FAIL on logic. Sharp and photographic, but the cleared track appears in front of the blade, so the truck reads as reversing. |
| C | Seedance 2.5 | 70 | 720x1280, 24 fps, audio | FAIL on logic. Same inverted clearing, with two bare strips ahead of the blade. Lower resolution. |

- Against the pre-registered criteria, only A passes. A is also the cheapest of the three.
- n = 1 per model. This does not establish that Kling 4.0 is typically better, only that it was on this shot.
- I cannot hear audio. Levels were measured (A: mean -23.9 dB), content was not judged.
- Awaiting the owner's verdict on clip A. The daily task stays paused until then.

Candidate recipe v3 if the owner accepts A:
- start frame GPT Image 2.6 high 2k (2.75) + Kling 4.0 10 s 1080p image-to-video (32.5) + 5 carousel images at high quality (7.5) = 42.75 credits a day.
- Proposed cap 45 credits (about $2.25). No re-roll: if the clip fails the frame check, that day posts the carousel only.
- At 42.75 credits a day the month needs about 1,280 credits against the plan's 1,000-credit grant (seen in transactions on 12 Nov).

P(owner accepts clip A) = 55%. P(Kling 4.0 keeps passing my frame check on at least 7 of the next 10 daily clips) = 60%.
