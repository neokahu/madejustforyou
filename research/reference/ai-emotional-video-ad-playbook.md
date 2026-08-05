# AI Emotional Video-Ad Playbook — MadeJustForYou

**Purpose:** how to produce emotionally-appealing video ads for personalized gifts using AI generation, end-to-end. Built 2026-08-05 from web research (emotional-ad psychology · short-form ad structure · 2026 AI-video toolchain · live competitor ad teardown). Tailored to our tools (Kie.ai: Veo 3, Sora, Kling, Hailuo, Seedance, Wan + nano-banana / flux / ideogram + ElevenLabs) and our [[recipient categories]].

> **One sentence:** lead with the *personalization act* (names/photo being added) or a *giftee reaction*, pay it off with a *glow / tears* shot, headline it `[emotional one-liner] – Personalized Gift For [recipient]`, generate product motion via **image-to-video from a real product still**, keep AI to mood/b-roll while compositing the real product + logo, finish in CapCut with burned-in captions, and test 4–5 hooks on a 48h loop.

---

## 0. Why emotion (the business case)
- Emotional ad content ~**doubles** performance vs rational (31% vs 16%, Neil Patel / 1,400-campaign analysis). High positive-emotion creative drove **140% higher action intent** (System1/Pinterest).
- Personalization is a *neurological* hook — seeing one's name/photo fires the brain's reward center ("name-letter effect"): people "feel seen." That's the whole niche.
- A gift is a **relationship statement** ("I thought about YOU"). Sell what the gift *says*, never a feature list.

---

## 1. The emotional engine, by recipient
Match the emotion → angle → hook to the recipient. (Headline formula everywhere: **`[emotional one-liner] – Personalized Gift For [recipient]`**, Macorner's proven pattern.)

| Recipient | Core emotion | Winning angle | Video hook | Real example one-liner |
|---|---|---|---|---|
| **Grandparents** | Legacy · being remembered · watching family grow | "Count us all" — every grandkid named on one object | Name-stacking demo (add grandkid #1, #2, #3 on screen) | "Grandma's Garden – one bloom for every grandchild" |
| **Parents** | Gratitude · "you raised me" | Sentimental thank-you from adult child | Photo/handwriting reveal | "Mom, We Love You" |
| **Couples** | Milestone permanence · (or cheeky humor) | Anniversary "forever"; OR funny lane | Glow shot / "our story" reveal | "The night we got married"; "Congrats On Being My Husband You Lucky Bastard" |
| **Pets (alive)** | Breed-identity pride | Hyper-specific per breed | Breed-trait confession hook | "Corgi owners know the drill: short legs, big ears…" |
| **Memorial / loss** | Continuing bonds · comfort (grief→warmth) | Turn a memory into light you keep — **year-round evergreen** | Real photo → glowing suncatcher/art | "My Favorite Hello And My Hardest Goodbye"; "Always with you" |
| **Kids / grandkids** | Pride · "first Christmas / growing up" | Milestone keepsake (giver is often grandma) | Huggable object / first-Christmas framing | "Baby's First Christmas" |

Rules that hold across all: **2nd-person** ("for her"), **specific** personalization detail (names a shared thing), **sensory/warmth** language, and any grief/nostalgia must **resolve into warmth** by the end (peak-end rule). Avoid: product-first feature lists, generic emotion, unresolved sadness.

---

## 2. Video-ad anatomy (the structure that converts)
- **Hook (first 1–3s) = ~71–80% of performance.** A face on screen holds viewers **49% longer**. Open on motion/tension, never a logo intro. Rotate hook styles (they fatigue).
  - Gift-niche hooks that win: the **personalization act** (typing names / dropping in the photo), a **giftee reaction** (grandma tears up), a **relatable confession** ("I almost cried making this").
- **Arc:** Hook → desire/relationship → **personalization demo** → reaction/social proof → **one** CTA. One message, one CTA. (30s split: hook 3–5s · body 10–15s · payoff 5–8s · CTA 3–5s.)
- **Length:** 15–30s (TikTok 9–15s top-of-funnel; Meta converts best <45s). Frequent cuts / pattern-interrupts at drop points.
- **Format:** **UGC-style wins** emotional/gift (Meta: ~4.2× engagement, 2.8× conversion vs polished). For gifts, the **giftee's reaction beats the buyer's**. Keep polished versions for **retargeting** + premium ($40+ AOV like our candle warmer).
- **Production specs (non-negotiable):** burned-in **captions** (~85% watch sound-off) · **9:16** (or 4:5 for Meta feed) · trending/native audio (+~18% recall) · **CTA bottom-third**, action verb · first frame = movement or a face · key action in centre 50% (safe zones ~250px top / 340px bottom).

---

## 3. The AI production pipeline (weighted to our tools)
The mistake is generating footage before locking the look → "character/product drift." Do it in this order:

1. **Script the angle.** Mine competitor `ref_ads_link`s (Meta Ad Library) for a proven hook; write pain→transformation→warmth. Keep to ONE emotion.
2. **Lock the visual identity FIRST.** Build hero stills with **nano-banana / flux** (scene + mood) and **ideogram** for any **on-pack text / names / logo** (video models mangle text). This still is your anchor.
3. **Image-to-video, NOT text-to-video.** Animate a **real/clean product still** so the model preserves the actual product (shape, color, gloss, the printed names) instead of hallucinating it. This is the load-bearing move.
   - **Kling** → best product-fidelity from a source image (the "make the real product move" default).
   - **Veo 3 / Seedance** → cinematic hero motion + native audio (push-in, glow, steam) off the same still.
   - **Hailuo / Wan** → cheap, fast **b-roll volume** for variant testing.
   - (Sora is being deprecated in 2026 — don't build on it.)
4. **Keyframe** start + end of each clip to kill drift. Clips **5–8s**; plan cuts, not long takes.
5. **Hybrid composite** = the pro move: real product close-ups (or the flat mockup) for fidelity + AI for **environment / lifestyle / mood / b-roll**; re-overlay the real logo/names in post. Cut away before AI physics (hands, opening, pouring) breaks.
6. **Assemble in CapCut** — auto-captions, beat-sync, text animation, music. **VO via ElevenLabs**, synced in CapCut.
7. **Ship 5–10 variants → test → scale winner** (§5).

**Optional talking-avatar UGC** (testimonial hooks with an AI actor): Arcads (most realistic, ~$110/mo) / Creatify (URL→ad, ~$33–49/mo) / HeyGen (localization). Not in our API stack — paid add-ons if we want person-to-camera hooks.

### 3.5 Pipeline: product-direct vs character-first
**We already have the product image → animate it directly (i2v). Never "build" the product.** You only build a reference image first when introducing a **recurring PERSON** (grandma, giftee) who must look the same across shots. **An ad = 3–6 short clips cut together** — generate per shot type, assemble in CapCut:

| Clip type | Pipeline | Build a character first? |
|---|---|---|
| Product ambient (glow / push-in / living still) | product image → i2v (Kling) | No |
| Product + anonymous hand | product image → i2v, prompt the hand | No (hand isn't a recurring identity) |
| Personalization reveal (names/photo appearing) | **CapCut motion-graphic in edit**, not AI | No |
| Human reaction / testimonial (recurring person) | build 1 consistent character ref → i2v, OR AI-UGC avatar | **Yes** |

**Default = product-direct, minimize humans** (dodges the 3 hardest AI problems: faces, hands, text). Add a person only when the concept needs the reaction shot. **Decision rule:** no recurring person → product image → i2v; one recurring person → build ONE character ref image first (nano-banana/flux) then i2v with it as reference (Veo ingredients / Seedance `@image` / Kling ref), or use Arcads/Creatify. **Continuity trick:** chain product clips by using the product image as each clip's first frame (or clip 1's last frame as clip 2's first frame) — no character needed.

---

## 4. Prompt formula (cinematic + emotional)
Google's own structure, front-load the most important element, change **one variable at a time**:

```
[Camera move] + [Subject] + [Action/emotion] + [Context/setting] + [Lighting] + [Style & mood] + [Audio]
```
- **Camera = tone lever:** slow dolly-in = intimacy/tension; orbital = reveal; start static, add ONE move per clip.
- **Lighting = mood:** name source/direction/quality/color ("soft warm window light, golden hour" for warmth; dim room + object glow for memorial/LED).
- **Emotion:** name the feeling + a physical tell ("grandmother's eyes welling up, hand to mouth").
- **Consistency:** repeat an **identity anchor verbatim** every shot ("same 60-yo woman, silver bob, cream cardigan — as previous shot") + reference image; keep a continuity table (character/wardrobe/props/lens/grade/lighting).

**Worked example — candle warmer (MJP-111), memorial-adjacent warmth angle:**
> *Slow dolly-in on a personalized "Grandma's Garden" candle-warmer lamp glowing on a windowsill at dusk; warm amber light blooms across engraved grandchildren's names; a grandmother's hand enters frame and rests beside it; soft golden window light, shallow depth of field, cozy nostalgic film grade; gentle piano; 6s.*
Then compose the **real product still** (with real names via ideogram) as the hero; use the AI clip as the ambient glow/lifestyle wrap.

---

## 5. Testing methodology
- **Reality:** only ~5% of creatives win; ~50% get no spend; video **fatigues in ~9 days** → volume + velocity matter.
- **Isolate ONE variable** — most testing is *hook* testing (same body/LP). One creative per ad set (ABO), Advantage+ Creative OFF, so you can attribute. Test **4–5 concepts → then 5 element-variants** of winners.
- **Cadence:** leading signal at **24–72h** (hook rate tells you fast); verdict at **48h + ~1,000 impressions/variant**; refresh every 7–10 days.
- **Benchmarks (cold, Meta; TikTok ~5–10pts lower):** Hook rate (3s/impr) **25–35% healthy**, <15% kill, 45%+ elite · Hold rate (15s) 15–25% · then **CPA is the money metric.** Diagnose bad CPA → hook rate → hold rate → landing page/offer. Don't optimize watch-time over purchases.
- **Tools:** Motion (hook/hold/fatigue analytics) · Foreplay (swipe file / competitor Ad Library) · Triple Whale/Northbeam (attribution).

---

## 6. Quick-start checklist (concept → shipped ad)
1. Pick a product + recipient; grab the competitor hook from its `ref_ads_link`.
2. Write 1 emotional one-liner headline + 1 CTA. Pick the angle from §1.
3. Make the hero still (nano-banana/flux) + real names/logo (ideogram).
4. Image-to-video: Kling (product) + Veo/Seedance (1 hero glow/reaction shot), 5–8s each.
5. Composite real product + AI mood in CapCut; burn captions; ElevenLabs VO; trending audio; 9:16.
6. Cut 4–5 hook variants over the same body.
7. Launch ABO test; read hook rate at 48h; kill <15%, scale the winner; refresh in ~9 days.

---

## Sources
Emotional psychology: System1, Van Tilburg et al. (nostalgia), continuing-bonds grief research, Yale SOM / Positive Acorn (gift-as-signal), Neil Patel (emotional vs rational). Ad structure: TikTok/Meta creative data, Motion (550k ads), Zebracat, gotolstoy, benly.ai. AI toolchain: Google Veo prompting guide, masonry.so (product-fidelity test), evolink/fal.ai/morphed (pricing), prst.media (workflow). Niche teardown: live Meta Ad Library (Macorner, PFG/trendingcustom, Pawfect House, Amber Shop — longest-running = proven), Foreplay dropshipping examples. Full URLs in session research notes.
