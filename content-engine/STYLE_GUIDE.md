# House style: photoreal, satisfying, one idea per clip

Recipe v3, approved by the owner on 2026-11-14 after a three-model bake-off. Recipes v1 and v2 were rejected as generic and obviously AI. See the retractions at the top of `RUNNING_LOG.md`.

## What a concept must have
A concept is rejected at the idea stage unless it has all four:
1. **A trend anchor.** A topic or format that two or more sources name as rising this week.
2. **A hook in the first frame.** Something slightly impossible or delightful that is already readable in the still: a toy snowplough on an icing-sugar street, not a cup of coffee.
3. **A payoff.** A visible before and after within 10 seconds: a cleared path, a filled mould, a finished pattern.
4. **Physics the model can do.** One rigid object moving through or over one soft material: pushing, ploughing, pouring, spreading, rolling, pressing, melting. Avoid cutting something open to reveal an interior, hands doing fine work, and anything that transforms into something else.

Banned as stock AI looks: latte pours, fairy-light bokeh, "cozy" stills with nothing happening, and the words "cinematic", "film grain", "amber", "dreamy" in any prompt.

## The look (append to every image prompt)
`Real photo shot on a phone. Soft overcast daylight from a window, neutral true-to-life colour, shallow depth of field from a phone macro lens, slight sensor noise, small imperfections (crumbs, smudges, uneven edges). No text, no logos, no people.`

Scenes are small and domestic: a kitchen worktop, a windowsill, a workbench. Objects are generic and unbranded.

## Reel (1 per day): start frame, then Kling 4.0
1. **Start frame:** `gpt_image_2_6`, 9:16, quality high, resolution 2k, jpeg. 2.75 credits.
   - Describe the scene at the moment before the action starts, with the moving object centred and touching the material it will move.
   - State which way the object faces. The video prompt must match what the frame actually shows, so look at the frame before writing the video prompt.
2. **Video:** `kling4_0`, mode `image-to-video`, 9:16, 10 s, 1080p, the start frame as `start_image`. 32.5 credits.
   - Template: `Real handheld phone macro footage, real-time speed. <The object> <does one action> <direction relative to camera>. <What the material does, and what is left behind>. The camera <one small move> with slight natural hand sway. <Everything else> stays perfectly still and solid. Overcast window light, true-to-life colour. Sound: <two concrete sounds>. No text, no logos, no people.`
   - Keep Kling's native audio.

## Carousel (1 per day): 5 stills of the same scene
`gpt_image_2_6`, 4:5, quality high, jpeg. 1.5 credits each.
1. The hook: the scene before the action.
2. Macro detail of the material.
3. The object close up.
4. The wider setting.
5. The payoff: the finished result.

## Captions
- One lowercase line under about 80 characters that names the payoff, then a soft call to action. No engagement bait.
- 5 hashtags maximum: 1-2 from the trend, the rest from `#satisfying #oddlysatisfying #miniature #asmr #cozyaesthetic`.
- Always end with `(AI-generated visuals)`.
