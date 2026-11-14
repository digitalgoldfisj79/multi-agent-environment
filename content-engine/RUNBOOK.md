# Daily runbook (followed by the scheduled cloud session)

Goal: produce 1 Reel and 1 carousel anchored to a current TikTok/Instagram trend, in the house style, for at most **45 credits (about $2.25)** of Higgsfield spend. Queue them so GitHub Actions posts to Instagram, and pre-fill the TikTok publish form.

The owner raised the cap from 40 to 45 credits on 2026-11-14 to pay for Kling 4.0, the model they approved. A normal day costs 42.75 credits.

Work from the repo checkout on branch **`ccr-8bbf046b-r7dn0e`**. The owner has explicitly authorised the daily session to commit and push to this branch.

```bash
git fetch origin ccr-8bbf046b-r7dn0e && git checkout ccr-8bbf046b-r7dn0e && git pull --ff-only
DAY=$(date -u +%F); cd content-engine
```

## 0. Idempotency and budget (stop early if either fails)
- If `queue/$DAY.json` already exists, stop: today is done.
- `python engine/budget.py check 42.75` must exit 0.
- Cross-check with Higgsfield `transactions` (size 30). Sum today's (UTC) spends minus refunds. If that sum + 42.75 > 45, stop and report.

## 1. Pick today's trend (about 5 minutes, no Higgsfield spend)
- Run 2-3 `WebSearch` (standard) queries in parallel:
  - "TikTok trends this week <Month YYYY>"
  - "Instagram Reels trends this week <Month YYYY>"
  - "viral satisfying / miniature / ASMR video trends this week"
- If `tiktok_accounts` shows an active account, also call `tiktok_music_trending` (7DAY) to read the mood of trending sounds. This is for mood only; tracks are attached by the owner in the publish form.
- Read `state/history.json`. Do not repeat a topic used in the last 14 days.
- **Feedback from past posts.** Run `python engine/ig_insights.py --report`, which is descriptive only. The pre-registered rule, which must not be changed after seeing data:
  - Until there are **14 or more Reels with d7 snapshots**, insights do NOT influence topic choice. Just note them in the log.
  - After that, a category is "favoured" only if its median d7 views exceed the overall median by more than the overall IQR, with at least 4 posts in that category. A favoured category earns +1 on trend strength. Anything weaker counts as "the metric does not resolve this" and has no effect.
  - High `reels_skip_rate` is a hook problem, not a topic problem. If the median skip rate is above 50%, put the motion in frame 1 and keep the subject centred.
- Give each candidate a `category` from: `food-drink`, `nature-weather`, `seasonal-holiday`, `craft-making`, `texture-asmr`, `place-mood`, `miniature`. It goes in the manifest at `trend.category`.
- Turn each trend into a concept that meets all four tests in STYLE_GUIDE.md ("What a concept must have"). Drop any trend you cannot turn into one.
- Score up to 5 concepts out of 5 on each of:
  - **trend strength**: named by 2 or more independent sources this week
  - **hook and payoff**: readable in the first frame, with a visible before and after
  - **feasibility**: one rigid object moving one soft material, nothing cut open or transformed
  - **compliance**: COMPLIANCE.md rule 5. Any brand, person, tragedy or politics means automatic reject.
- Pick the top scorer and write the candidate table and sources into the manifest's `trend` block.

## 2. Start frame (2.75 credits)
- Write the start-frame prompt from the STYLE_GUIDE.md template.
- Preflight with `generate_image` `get_cost:true` for `{model: gpt_image_2_6, aspect_ratio: "9:16", quality: "high", resolution: "2k", output_format: "jpeg"}`. Expect 2.75.
- Generate it, wait with `jobs_wait`, download it and `Read` it.
- Check it: photographic, no text or logos, no people, the moving object centred. Note which way the object actually faces.
- If it fails, regenerate once (2.75 more) and cut the carousel to 3 images, which keeps the day at 42.5 credits. If it fails again, stop for the day and report.
- `python engine/budget.py record "<DAY> start frame gpt_image_2_6 high 2k" 2.75`

## 3. Clip and carousel
- Write the video prompt to match what the start frame actually shows, including the direction the object faces.
- Preflight with `generate_video` `get_cost:true` for `{model: kling4_0, mode: "image-to-video", aspect_ratio: "9:16", duration: 10, resolution: "1080p"}`. Expect 32.5.
- Preflight with `generate_image` `get_cost:true` for `{model: gpt_image_2_6, aspect_ratio: "4:5", quality: "high", output_format: "jpeg"}`. Expect 1.5.
- If prices have changed, recompute against the 45-credit cap. If the day no longer fits, cut the carousel to 3 images first. Never swap Kling 4.0 for a cheaper video model: the owner rejected those. If Kling 4.0 alone no longer fits, stop and report.
- Submit both in parallel:
  - `generate_video` with `medias: [{value: <start frame job_id>, role: "start_image"}]`
  - `generate_image_batch` with the 5 carousel prompts
  - Do not pass a `folder_id`.
- Wait with `jobs_wait` (15 s timeout per call; Kling 4.0 takes about 6-8 minutes).
- Record both spends with `engine/budget.py record`.

## 4. Download and QA (look at every frame)
```bash
mkdir -p output/$DAY && cd output/$DAY
curl -sS -o raw_clip.mp4 "<video result_url>"; curl -sS -o slide_1.jpg "<img1>" ...  # slide_1..5
ffmpeg -y -loglevel error -i raw_clip.mp4 -vf "fps=1,scale=200:-1,tile=10x1" -frames:v 1 frames.jpg
ffmpeg -y -loglevel error -ss 8 -i raw_clip.mp4 -frames:v 1 -vf "scale=600:-1" frame_t8.jpg
python3 -c "from PIL import Image;ims=[Image.open(f'slide_{i}.jpg').resize((216,270)) for i in range(1,6)];c=Image.new('RGB',(1080,270));[c.paste(m,(216*k,0)) for k,m in enumerate(ims)];c.save('contact.jpg')"
```
- `Read` `frames.jpg`, `frame_t8.jpg` and `contact.jpg`.
- The clip FAILS if it shows any of these (criteria fixed on 2026-11-14, before the bake-off was viewed):
  - an object morphing, ghosting or turning translucent
  - background objects moving or deforming
  - the moving object changing shape
  - the material behaving like liquid or fog when it is a powder or solid
  - **wrong cause and effect**, such as a cleared path appearing ahead of the thing doing the clearing
  - text, logos, faces or identifiable people
- **No re-roll.** If the clip fails, do not regenerate it and do not post it. Post the carousel only that day (leave the `reel` block out of the manifest) and say so in the final message.
- A carousel image that fails is dropped. The carousel needs 2 or more images.

## 5. Audio and hosting
- Kling 4.0 clips come with native audio. Confirm with `ffprobe` and keep it: `cp raw_clip.mp4 reel.mp4`. Use the Higgsfield `result_url` as `reel.video_url`.
- Only if the clip is silent: run `python ../../engine/ambient_audio.py raw_clip.mp4 reel.mp4 --seed <day-of-year>`, upload `reel.mp4` via `media_upload`, PUT it with curl, call `media_confirm` (type video), and use the returned `url` as `video_url`.
- Run `python ../../engine/validate.py .`. It must exit 0.

## 6. Queue
- Write `queue/$DAY.json` with the same schema as `queue/2026-11-14.json`, without the `hold` field:
  - trend, reel (if it passed), carousel
  - credits_spent
  - compliance (every check true, `passed: true`)
- Append `{"date": DAY, "topic": ...}` to `state/history.json`.
- Add a dated entry to `RUNNING_LOG.md` (trend, credits, QA notes, whether the clip passed).
- Commit the manifest, state and log only. `output/` is gitignored.
- `git push -u origin ccr-8bbf046b-r7dn0e`, retrying up to 4 times with backoff. The push triggers `.github/workflows/instagram-post.yml`: the Reel goes out immediately and the carousel about 3 hours later.

## 7. TikTok (needs 1 tap from the owner)
- If `tiktok_accounts` has an active account:
  - Call `tiktok_prepare_publish` with mode `DIRECT_POST`, media_type `VIDEO`, `video_url` set to reel.video_url, `title` set to the first caption line, `description` set to the full caption, and `is_aigc: true`. The owner requires AI disclosure on every post.
  - Then call it again for the carousel with media_type `PHOTO` and the image URLs (JPEG, within 1080x1920).
- If no account is connected, say so in the final message. The owner can upload `reel.video_url` manually.

## 8. Final message (this becomes the phone notification)
A short table with:
- trend chosen and why
- credits used today, with the estimated dollar cost
- whether the clip passed the frame check
- Reel URL and image URLs
- Instagram status ("queued: Action will post")
- TikTok status ("tap to publish in this session" or "not connected")
- anything skipped and why

Never exceed the budget, never skip the compliance gate, never post brand or person content, never substitute a cheaper video model.
