# Compliance gate (must pass before anything is queued)

The rules are summarised from platform documentation and reporting checked on 2026-11-14. Re-check them quarterly, because policies change.

## Hard rules
1. **AI disclosure is always on.**
   - Instagram: the uploader sets `is_ai_generated=true`. This is verified in Meta's Instagram Platform changelog (June 2026), and for carousels it goes on the parent container only.
   - TikTok: the AI-generated content toggle (`is_aigc`) is ON in the publish form.
   - The caption also says "(AI-generated visuals)".
2. **No real people.** No celebrities, public figures, creators or anyone's likeness. Generic, non-identifiable hands are OK. Instagram reportedly limits reach for unlabeled profiles built around an AI-generated person; we avoid that category entirely.
3. **No IP.** No brands, logos, trademarked products (for example a named coffee chain's cups), copyrighted characters or artworks "in the style of" a named living artist.
4. **No copyrighted audio.**
   - Use the model's native audio, the code-synthesised pad, or (on TikTok only) a track from TikTok's Commercial Music Library chosen in the publish form.
   - Never upload chart music yourself.
5. **No sensitive or misleading trends.** Skip anything about:
   - tragedies, disasters, war, politics or elections
   - health or medical claims, finance or crypto
   - minors, dangerous challenges, sexual content
   - news events where AI visuals could be mistaken for footage
6. **No deception.** No fake "real footage", fake reviews, fake giveaways or engagement bait.
7. **Rate.** At most 1 Reel and 1 carousel a day. That is far under Instagram's documented API limit, which the docs give as 100 posts per 24 h in one place and 50 in another.

## Daily checklist (recorded in the manifest's `compliance.checks`)
- [ ] `no_real_people_or_likeness`
- [ ] `no_brands_logos_trademarks` (inspect every frame and image, including text that slipped into a render)
- [ ] `no_copyrighted_characters_or_music`
- [ ] `no_sensitive_topics`
- [ ] `no_misleading_claims`
- [ ] `ai_label_set_on_upload`
- [ ] `ai_disclosed_in_caption`
- [ ] `hashtags_le_5`

If any box fails: regenerate if the budget allows, otherwise skip the day. Never queue a failing post. `ig_post.py` refuses to post unless `compliance.passed` is true.
