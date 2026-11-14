# Running log: content engine

## Retracted findings
_(none yet; retractions go here, at the top)_

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
