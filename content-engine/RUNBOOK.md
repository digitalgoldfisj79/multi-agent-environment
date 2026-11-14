# Daily runbook (followed by the scheduled cloud session)

Goal: produce 1 Reel and 1 carousel anchored to a current TikTok/Instagram trend, in the house style, for at most **$2 (40 credits)** of Higgsfield spend. Queue them so GitHub Actions posts to Instagram, and pre-fill the TikTok publish form.

Work from `/home/user/multi-agent-environment` (or wherever this repo is checked out) on branch **`ccr-8bbf046b-r7dn0e`**. The owner has explicitly authorised the daily session to commit and push to this branch.

```bash
git fetch origin ccr-8bbf046b-r7dn0e && git checkout ccr-8bbf046b-r7dn0e && git pull --ff-only
DAY=$(date -u +%F); cd content-engine
```

## 0. Idempotency and budget (stop early if either fails)
- If `queue/$DAY.json` already exists, stop: today is done.
- `python engine/budget.py check 17.5` must exit 0.
- Cross-check with Higgsfield `transactions` (size 30). Sum today's (UTC) spends minus refunds. If that sum + 17.5 > 40, stop and report.

## 1. Pick today's trend (about 5 minutes, no Higgsfield spend)
- Run 2-3 `WebSearch` (standard) queries in parallel:
  - "TikTok trends this week <Month YYYY>"
  - "Instagram Reels trends this week <Month YYYY>"
  - "trending aesthetic / satisfying / cozy content this week"
- If `tiktok_accounts` shows an active account, also call `tiktok_music_trending` (7DAY) to read the mood of trending sounds. This is for mood only; tracks are attached by the owner in the publish form.
- Read `state/history.json`. Do not repeat a topic used in the last 14 days.
- Score up to 5 candidates out of 5 on each of:
  - **trend strength**: named by 2 or more independent sources this week
  - **visual fit** with STYLE_GUIDE.md: can it be a satisfying, people-free macro visual?
  - **compliance**: COMPLIANCE.md rule 5. Any brand, person, tragedy or politics means automatic reject.
- Pick the top scorer and write the candidate table and sources into the manifest's `trend` block.

## 2. Prompts
- Write 1 Reel prompt and 5 carousel prompts from the STYLE_GUIDE.md templates.
- Every prompt ends with the fixed signature, including "No people, no faces, no text, no logos, no brand marks".

## 3. Preflight cost, then generate
- Preflight with `generate_video` `get_cost:true` for `{model: kling3_0_turbo, aspect_ratio: "9:16", duration: 10, resolution: "720p"}`. Expect 15.
- Preflight with `generate_image` `get_cost:true` for `{model: gpt_image_2_6, aspect_ratio: "4:5", quality: "medium", output_format: "jpeg"}`. Expect 0.5.
- If prices have changed, recompute. If the total exceeds the remaining budget, drop to 3 carousel images. If it still exceeds, skip the Reel.
- Submit both in parallel: `generate_video` with the Reel prompt, and `generate_image_batch` with 5 requests. Do not pass a `folder_id`.
- Wait with `jobs_wait` (15 s timeout per call; Kling takes about 3-5 minutes).
- Then run `python engine/budget.py record "<DAY> clip kling3_0_turbo 10s" 15` and `... record "<DAY> carousel 5x gpt_image_2_6 medium" 2.5`.

## 4. Download and QA (look at every frame)
```bash
mkdir -p output/$DAY && cd output/$DAY
curl -sS -o raw_clip.mp4 "<video result_url>"; curl -sS -o slide_1.jpg "<img1>" ...  # slide_1..5
ffmpeg -y -loglevel error -i raw_clip.mp4 -vf "fps=0.6,scale=180:-1,tile=6x1" -frames:v 1 frames.jpg
python3 -c "from PIL import Image;ims=[Image.open(f'slide_{i}.jpg').resize((216,270)) for i in range(1,6)];c=Image.new('RGB',(1080,270));[c.paste(m,(216*k,0)) for k,m in enumerate(ims)];c.save('contact.jpg')"
```
- `Read` both `frames.jpg` and `contact.jpg`, and check them against COMPLIANCE.md: no logos or text, no faces or identifiable people, no warped or anatomically broken objects.
- If an item fails, regenerate only that item, and only if `budget.py check <cost>` passes. Otherwise drop it. Post whatever passed: the carousel needs 2 or more images.

## 5. Audio and hosting
- Check for audio with `ffprobe` on raw_clip.mp4.
  - **Audio present:** `cp raw_clip.mp4 reel.mp4` and use the Higgsfield `result_url` as `reel.video_url`.
  - **Silent:** run `python ../../engine/ambient_audio.py raw_clip.mp4 reel.mp4 --seed <day-of-year>`. Then upload `reel.mp4` via `media_upload`, PUT it with curl, call `media_confirm` (type video), and use the returned `url` as `video_url`. This was verified on 2026-11-14 to serve publicly as `video/mp4`.
- Run `python ../../engine/validate.py .`. It must exit 0.

## 6. Queue
- Write `queue/$DAY.json` with the same schema as `queue/2026-11-14.json`:
  - trend, reel, carousel
  - credits_spent
  - compliance (every check true, `passed: true`)
- Append `{"date": DAY, "topic": ...}` to `state/history.json`.
- Add a dated entry to `RUNNING_LOG.md` (trend, credits, QA notes, P(trend still relevant in 7 days)).
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
- Reel URL and image URLs
- Instagram status ("queued: Action will post")
- TikTok status ("tap to publish in this session" or "not connected")
- anything skipped and why

Never exceed the budget, never skip the compliance gate, never post brand or person content.
