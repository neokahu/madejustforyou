# MJ4U-111 — Product-Reveal Creative (static + carousel)

**Built:** 2026-08-14 · **Format:** copies the proven Macorner winner (see `research/sprints/2026-08-competitor-creative-teardown/candle-warmer.md`).
**Why this exists:** the emotional Thai-film ad underperformed; every scaling competitor uses **product-as-hero, no actors, roster visible in the first second, terse copy, no discount**. This is that. Diagnosis is done — this is the creative we test next.

## What's here
- `build.py` — regenerates every asset from the real Shopify product photos in `src/`. Re-run: `python3 build.py`. Zero cost (PIL + local fonts, no AI generation).
- `src/01..08.jpg` — the live product photos (pulled from the Shopify product JSON, 2048²).
- `out/` — the finished ad assets, all **4:5 (1080×1350)**, mobile-first:
  | file | role | copy on-image |
  |---|---|---|
  | `hero.jpg` | **single static ad** | "One flower for every grandchild she's raised" |
  | `slide-1.jpg` | carousel 1 — hook (= hero + SWIPE cue) | same |
  | `slide-2.jpg` | carousel 2 — meaning | "Love Grows Here · each birth-flower = a grandchild (Alice, Grace, Jade)" |
  | `slide-3.jpg` | carousel 3 — lifestyle | "A soft glow that fills her room every evening" |
  | `slide-4.jpg` | carousel 4 — personalize | "Add every name. Watch her garden grow." + 1-2-3 |
  | `slide-5.jpg` | carousel 5 — utility | "Beautiful by day. Glowing by night." + no-flame/timer badges |
  | `slide-6.jpg` | carousel 6 — CTA | "Give her a garden that never fades · Personalize hers →" |

## Design / strategy locked to the teardown
- **Product-as-hero.** The personalized lampshade (names + birth flowers) is the first thing you read.
- **Present-tense living legacy, NOT memorial.** "one for every child she's watched grow" — warm, not grief. (The old film's "she's forgetting us" angle is retired.)
- **No discount, no urgency.** Full $49.95 premium gift positioning — the winner ran 122 days clean.
- **Locked title:** "GRANDMA'S GARDEN — Love Grows Here" (template equity; never reword; only swap the matriarch word for new audiences).
- The on-image sample names are **Alice · Grace · Jade** (what the live product mockup shows) — copy stays roster-agnostic so it never contradicts the image.

---

## Ad copy (for the uploader — primary_text as line arrays, scannable)

### Primary text A — "forever garden" (default; closest to the proven winner)
```
A warm glow. A forever garden. 🌸

One birth-month flower for every grandchild she's watched grow — her whole family, blooming on one little lamp.

It's a real candle warmer: no flame, no smoke, just soft light on her nightstand every evening.

Grandma's Garden — Love Grows Here.
Personalize hers 👇
```

### Primary text B — "watch her garden grow" (roster / how-it-works)
```
Her garden started with the ones she raised. 🌸

Add every grandchild — a name and their birth-month flower — and watch her whole family bloom across the shade of a real candle-warmer lamp.

Warm glow by night. A beautiful keepsake by day.
No flame. No smoke. Just love, growing at home.

Personalize hers 👇
```

### Headlines (Macorner pattern: `[emotional one-liner] – Personalized Gift For Grandma`)
1. One Flower For Every Grandchild – Personalized Candle Warmer
2. Grandma's Garden, Love Grows Here – Personalized Gift For Grandma
3. Her Whole Family, Blooming On One Lamp – Personalized Gift For Grandma

### Description
Personalized with each grandchild's name + birth-month flower. Flameless candle warmer + soft night light. Premium keepsake — ships worldwide.

### CTA button
Shop Now

---

## Next steps (not done yet — confirm before spending)
1. **Test as a NEW ad set** alongside the current dr-benefit / emo-thesis (creative is the variable). Upload the static (`hero.jpg`) as one ad + the 6-slide carousel as another.
2. Optional **premium AI hero**: regenerate an extreme macro of the *lit* shade with a 5-name roster on a warm homey background (peonies bleeding in) via nano-banana, to A/B against `hero.jpg`.
3. Optional **simple product-reveal video** (6-8s): slow push-in on the lit shade → names resolve → warm-glow bloom. No actors, no story. Copy the winner's 19s product-only cut.
