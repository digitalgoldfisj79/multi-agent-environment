# Content engine: daily trend → AI Reel + carousel → Instagram & TikTok

## How it runs (no daily work from you except one TikTok tap)
```
scheduled cloud session (daily)
  └─ RUNBOOK.md:
     trends (web + TikTok music chart)
     → pick 1 on-brand, compliant topic
     → Higgsfield: photoreal start frame (2.75 cr)
       → 10 s Kling 4.0 clip at 1080p animated from it (32.5 cr)
       + 5 × GPT Image 2.6 carousel stills (7.5 cr)
     → frame-by-frame QA + COMPLIANCE.md gate
     → queue/DAY.json → git push
          └─ GitHub Action instagram-post.yml
             → Reel now, carousel +3 h (AI label on)
     → TikTok publish form pre-filled (is_aigc on) → you tap "Post"
```
**Budget:** a hard cap of 45 credits a day (about $2.25 at $0.05/credit), enforced by `engine/budget.py` and cross-checked against Higgsfield's transaction log. A normal day uses 42.75 credits (about $2.14). The owner raised the cap from $2 on 2026-11-14 to pay for Kling 4.0, the only model that passed the quality bake-off. That is about 1,280 credits a month, against the Plus plan's 1,000.

**Quality rule:** if a day's clip fails the frame check, it is not regenerated and not posted. That day posts the carousel only.

## One-time setup

### 1. Instagram (about 30 min, once)
1. In the Instagram app: Settings → Account type → switch to a **Professional** account (Creator or Business).
2. Create an app at <https://developers.facebook.com/apps>. Choose the use case for managing content on Instagram ("Instagram API with Instagram Login"). This setup does **not** need a Facebook Page.
3. In the app's Instagram API setup, add your Instagram account and **generate an access token** with these three permissions:
   - `instagram_business_basic`
   - `instagram_business_content_publish`
   - `instagram_business_manage_insights`, which lets the engine read each post's views, saves and skip rate and learn from them

   Copy the token and the Instagram **user ID** shown next to it.
4. In GitHub, open this repo → Settings → Secrets and variables → Actions → **New repository secret** and add:
   - `IG_USER_ID`
   - `IG_ACCESS_TOKEN`
5. Optionally, on the **Variables** tab:
   - `IG_GRAPH_HOST`: set it to `graph.facebook.com` if you used Facebook Login instead.
   - `CAROUSEL_DELAY_MIN`: defaults to 180.

Until the secrets exist, the Action runs green and posts nothing.

> The token lasts about 60 days. Set a reminder to regenerate it in step 3 and paste it into the secret again. (UNVERIFIED: the exact menu names in Meta's dashboard change often. Meta's own guide is the reference: <https://developers.facebook.com/documentation/instagram-platform/content-publishing>.)

### 2. TikTok (2 min, once)
Connect your TikTok account to Higgsfield. Ask Claude to "connect TikTok to Higgsfield", or use Higgsfield's TikTok connect flow. After that, each day's session pre-fills the publish form with the AI-generated label on. You tap **Post** in the session. TikTok's rules require that a person confirms each post made through this integration.

## Files
| File | Purpose |
|---|---|
| `RUNBOOK.md` | The exact daily procedure the scheduled session follows |
| `STYLE_GUIDE.md` | The fixed look, prompt templates and caption rules that keep posts consistent |
| `COMPLIANCE.md` | Platform-rule gate (AI labels, no real people or brands or copyrighted audio) |
| `engine/budget.py` | $2.25/day (45-credit) cap ledger |
| `engine/validate.py` | Media spec checks (JPEG, 9:16, fps, duration…) |
| `engine/ambient_audio.py` | Original synthesised audio bed for silent clips |
| `engine/ig_post.py` | Instagram Content Publishing API client (stdlib only). It reads back `is_ai_generated` after each post to confirm the label |
| `engine/ig_insights.py` | Per-post metrics at 48 h and 7 days, written to `state/insights.json` |
| `queue/DAY.json` | One manifest per day (also the audit trail) |
| `state/` | Ledger, topic history, posted IDs |
| `RUNNING_LOG.md` | Dated log of every run and decision |

## Change things
- **Style:** edit `STYLE_GUIDE.md`.
- **Budget:** set the env vars `DAILY_USD_CAP` / `USD_PER_CREDIT`, or edit the defaults in `budget.py`.
- **Pause:** disable the scheduled task (ask Claude) or disable the GitHub Action.
