# MJ4U-111 — Ad Copy

All written text for the ad: primary text, headline, CTA, hook variants, and the on-screen text in the video. Pairs with the film **"Everyone Is Still in Your Garden"** (`ads/film/script.md`) — this copy shares that film's hook and emotional thesis. Format follows the Meta-ad-fields spec in `research/reference/ai-emotional-video-ad-playbook.md`.

- **Product:** Grandma's Garden — *Love Grows Here* personalized candle-warmer lamp · $49.95 · madejustforyou.net
- **Recipient:** Grandparents (Grandma) · **Core emotion:** legacy / being remembered — *"everyone is still in your garden."* She may forget faces, but the light helps her find her people.
- **Mechanic:** a birth-flower + name printed on the shade for each grandchild; flameless warmer + soft night light; title "Grandma's Garden — Love Grows Here."
- **Real personalization (USE THESE EXACT NAMES — they match the film + product photo):** **Sophia · Cosmos** — **Donna · Aster** — **Sharon · Rose** — **Helen · Marigold** — **Sarah · Poppy** (5 grandchildren).
- **Emotional thesis (from the film):** the ending should make you feel *"we're all still here, Grandma"* — grief/forgetting resolved into warmth and a family reunited around one light.
- **Reference (competitor, proven — Macorner, ~114d live, scaling):** *"A warm glow, a forever garden 🌸 every light feels like love growing at home."*

---

## Meta ad fields

### Primary text — test these 3 (emotional-complementary default; #3 is the DR split)

> **Formatting rule:** write primary text with **line breaks** — short lines, blank line between beats, emoji/✔️ bullets for lists. Never one dense paragraph (unreadable in-feed). Copy below is the exact live format.

**1 — Emotional (the film's thesis, sound-off-safe)** · label `emo-thesis`
```
They said she was starting to forget us.

So we put everyone back in her garden. 🌸

It's a candle warmer lamp — one birth flower and one name for every grandchild, glowing soft on her nightstand.

Now when she touches a bloom, she finds her people again.

🌸 Personalized just for her — tap Shop Now.
```

**2 — Emotional ("count us all," warm + specific)** · label `count-us-all`
```
Your grandma raised the whole family.
This puts the whole family right back beside her — every night.

A birth flower + name for each grandchild on one soft-glowing lamp:
🌸 Sophia — cosmos
🌸 Donna — aster
🌸 Sharon — rose
🌸 Helen — marigold
🌸 Sarah — poppy

No flame, no smoke — just her garden lit up where she can always find it.

Made just for her 👇
```

**3 — Traditional DR (benefit + offer + urgency)** · label `dr-benefit`
```
The personalized gift grandmas actually cry over. 🌸

Grandma's Garden Candle Warmer — add each grandchild's name + birth flower to the shade.

✔️ Flameless warmer AND soft night light
✔️ No flame, no smoke
✔️ Premium keepsake — ships worldwide

$49.95 · selling fast for gifting season.
Shop now before her set sells out 👇
```

### Headline — test these 3 (Macorner pattern: `[emotional one-liner] – Personalized Gift For Grandma`)

1. Everyone Is Still In Your Garden – Personalized Gift For Grandma
2. One Bloom For Every Grandchild – Personalized Gift For Grandma
3. So She Can Always Find Her People – Personalized Gift For Grandma

### Description (optional)
Personalized with each grandchild's name and birth flower. Flameless candle warmer + soft night light. Premium keepsake — ships worldwide.

### CTA button
Shop Now

**Ad name (internal):** `MJ4U-111_<hook-label>_v1` (set `<hook-label>` per hook below; bump the version per reword)

---

## Hook variants (first 3s) — 5 DIFFERENT METHODOLOGIES (Round-1 concept test)
Not rewordings — five distinct ways in. Each names its **cold-open** (the film beat it opens on) and its **first caption line**.

**Hook 1 — Emotional-reaction** · label `emo-react`
- **Cold-open:** Scene 7 — Grandma's finger lands on **"Sharon — Rose"**, her face fills with recognition, eyes welling.
- **First caption:** *"Grandma forgot our faces… until she touched the names."*

**Hook 2 — Curiosity / pattern-interrupt (the break-in)** · label `curiosity-breakin`
- **Cold-open:** Scene 1 — rainy porch at midnight, brass key shaking in the granddaughter's hand as she slips into Grandma's house.
- **First caption:** *"She broke into her grandmother's house at midnight — to bring something *back*."*

**Hook 3 — Personalization-act** · label `perso-act`
- **Cold-open:** Scene 3 match-cutting to Scene 6 — the "Grandma's Garden" notebook page (Sophia·Cosmos, Donna·Aster, Sharon·Rose, Helen·Marigold, Sarah·Poppy) dissolving into those exact names printed on the glowing lampshade.
- **First caption:** *"Every grandchild gets their own flower on Grandma's lamp. 🌸"*

**Hook 4 — Relatable confession / UGC** · label `confession-ugc`
- **Cold-open:** Handheld, phone-style — granddaughter to camera, the wrapped lamp in her lap (framing of Scene 6 before the reveal).
- **First caption:** *"I cried making my grandma's gift — she's starting to forget us, so I gave her all of us back."*

**Hook 5 — Traditional DR / benefit** · label `dr-benefit`
- **Cold-open:** Scene 6/8 — slow orbit of the finished lamp glowing, names + birth flowers legible around the shade.
- **First caption:** *"A personalized candle warmer with every grandchild's name + birth flower — no flame, just glow."*

---

## On-screen text (the video reveal sequence)
Burned-in captions for the film. Beats marked **[composite]** need real text rendered sharp (PIL) and composited — AI garbles printed names. Names must match the lamp + notebook exactly.

1. **Hook (0:00):** hook caption per the variant above (rotate per creative).
2. **VO/curiosity beat (0:05–0:10):** *"They told me she was starting to forget us."*
3. **The notebook — [composite]** (0:10–0:15): "Grandma's Garden" page, one flower per name —
   **Sophia — Cosmos · Donna — Aster · Sharon — Rose · Helen — Marigold · Sarah — Poppy**
4. **The turn (0:20–0:25):** *"I'm not taking them. I'm bringing them back to her."*
5. **Product payoff — match cut, [composite]** (0:25): notebook flowers → the **exact same names + flowers printed on the lampshade** · line: *"So I put everyone back in your garden."*
6. **Recognition (0:30):** Grandma touches a bloom — *"Sharon… my rose."* / granddaughter: *"We're all still here, Grandma."*
7. **CTA card — [composite]** (0:35–0:40): title lockup **"Grandma's Garden — Love Grows Here"** · *"Put every name she loves where she can always find them."* · **Shop Now** · brand end card (logo + madejustforyou.net).

**Composite checklist:** notebook page names, lampshade names+flowers, title lockup, and CTA/end card. All five real names spelled exactly as above; at least three visible on-shade at once.

---

## Testing note
- **Round 1 = 5 different-methodology hooks over the SAME body + landing page** (isolate the hook). ~48h, ~1k impressions/variant; kill any hook-rate <15%.
- **Cold / top-funnel skews Hooks 1–3** (emotional-reaction, curiosity break-in, personalization-act) — face-forward, story-first, UGC-friendly. **Hook 4** also runs cold for UGC placements.
- **Retargeting / warm skews Hook 5** (DR/benefit) — for people who already know the story and need the offer + reason to buy now.
- **Round 2 = reword the winning hook ×5** to optimize, keeping body/LP fixed.

---

## Notes
- 2nd-person, specific (name the real grandchildren), resolve grief/forgetting into warmth — never a feature list, never a lonely grandma. She's always shown with family.
- Captions burned in (~85% watch muted); CTA bottom-third; 9:16 (or 4:5 for feed).
- Dialogue = on-screen captions (dodges lip-sync). Optional VO: read Primary text #1 (warmest, matches the film) over the glow shots; generate via ElevenLabs.
- The one non-negotiable: **on-screen names must match the REAL product's names** (Sophia·Cosmos, Donna·Aster, Sharon·Rose, Helen·Marigold, Sarah·Poppy) and the notebook↔lamp match-cut. The current `ads/film/script.md` still uses demo names (Emily·Sunflower, etc.) — flag for the Producer to reconcile the film to these real names before generation.
