# Wander Prints — Winning-Creative Teardown

**Source:** WinningHunter MCP (`search_facebook_ads`, `scan_ad`, `get_ad_transcript`)
**Date pulled:** 2026-08-13 · **Analyst:** paid-ad creative analyst
**Filter:** `searchkeyword=landingurl`, `keyword=wanderprints.com`, `country=US`, `page_type=products`, `sort=longestrunning desc`
**Store:** wanderprints.com (`great-family-shop.myshopify.com`) · monthly visits ~1.43M · page likes 57K–129K across page variants

---

## Method & scope notes

- **Clean product-prospecting count = 183 ads** for the `landingurl=wanderprints.com` product filter (NOT the ~2,000 "ads on page" figure, which is mostly dynamic/catalog DPA — ignored per house rules).
- Analyzed the **top 60 by longest-running** (3 pages). All ≥300-day evergreen winners live in the top ~16 rows; captured all of them plus representative shorter-run creatives.
- Three Meta page variants all belong to Wander Prints: **Wander Prints Unique Gift**, **Wander Prints Home Decor**, **Personalized Family Gift** (same store, same `page_id` cluster / same shopify domain).
- **Days running** = `lastSeen − started` (WinningHunter's own dates). Several winners last-seen 2026-04, i.e. still alive at last scrape.
- **Transcripts:** attempted Whisper on the top 3 longest-running VIDEO winners (memorial bracelet, collar frame, nana suncatcher). All returned `download_failed` — the 2024-era Meta CDN video URLs have expired signed tokens (`oe/oh`), so Whisper cannot fetch them. On-image hook text + captions + copy captured instead (below). No credits wasted beyond the failed fetch.
- **AOV:** product prices cluster $19.95–$45.95; median ~$26. Confirms the low-AOV / breadth archetype.

---

## THE STANDING OFFER (evergreen)

Found verbatim in an evergreen **Wander Prints Home Decor** creative caption:

> **"Use code: WP10 to get 10% OFF"** + "Worldwide shipping!"

- This is the "DYN10 / 10%-off-everything" evergreen offer referenced in the deep crawl — surfaced live as promo code **WP10**.
- It is a **soft, always-on 10% code**, not a scarcity/countdown mechanic. No "ends tonight," no stock counters, no BFCM urgency in the evergreen creatives.
- The ONLY urgency lever used site-wide in these creatives is **"Worldwide Shipping!"** — appended to nearly every single ad. It functions as a reassurance/CTA closer, not urgency.

---

## TOP EVERGREEN WINNERS (≥300 days) — ranked by longevity

### 1. Memorial Engraved Bracelet — "I'll Carry You" · **803 days** ⭐ FLAGSHIP
- **URL:** /products/custom-photo-ill-carry-you-memorial-gift-...-personalized-engraved-bracelet (short link `tp126nah2925-fbf`)
- **Format:** VIDEO · **creatives: 3** · started 2024-01-20 · lastSeen 2026-04-02 · **$21.95**
- **Performance (scan_ad):** EU adspend ~$7,756 · est. revenue ~$29,381 (max est. ~$119K) · **adscore = Winning** · 705K views · runs US/CA/AU · 6 ad sets at peak.
- **Caption (on-feed):** *"Beautiful Way To Remember Your Loved Ones"*
- **Primary text (verbatim):** "Customize Your Bracelet and Keep Your Loved Ones Always → Order here → wanderprints.com/tp126nah2925-fbf → Worldwide Shipping!"
- **Hashtags reveal targeting:** #memorialgift #memorial #family #mom #dad #parents #grandparents #grandma #grandpa #heaven #loss #customphoto
- **Angle/mechanic:** Grief + keepsake. "Carry your loved one with you always" — wearable memorial, custom-photo engraving. Human memorial (not pet) → same emotional lane relevant to a grandparent store.

### 2. Pet-Memorial Collar Frame — "My Hardest Goodbye" · **757 days** ⭐
- **URL:** short link `ah590hal1990-fbf` (product: Custom Photo My Hardest Goodbye – Pet Loss Sign, Collar Frame)
- **Format:** VIDEO · **creatives: 4** · started 2024-03-06 · lastSeen 2026-04-02 · **$29.95**
- **Performance:** EU adspend ~$3,109 · est. revenue ~$11,764 (max ~$46.9K) · **adscore = Winning** · 282K views.
- **Caption:** *"Memorial Gift For Pet Parents"*
- **Primary text (verbatim):** "Frame The Memories Of A Lifetime With Our Collar Frame 🌈🐾 → Order here → ... → Worldwide Shipping!"
- **Hashtags:** #collarframe #petloss #memorialgift #petlovers #doglovers #catlovers #catmom #catdad #dogmom #dogdad
- **Angle/mechanic:** Pet grief. The 🌈 (rainbow bridge) + 🐾 emoji instantly signals pet-loss to the target. Physical product = holds the actual collar → tangible keepsake mechanic. This is the single strongest pet-memorial evergreen.

### 3. Camping "You, Me & The Dogs" 3D Doormat · **442 days** (STILL LIVE)
- **URL:** /products/camping-you-me-and-the-dogs-3d-effect-personalized-doormat (`at1679cin3445`)
- **Format:** IMAGE · creatives: 1 · started 2025-05-28 · **lastSeen 2026-08-13 (live today)** · **$31.95**
- **Copy:** "Every step says family, this doormat welcomes heart and soul! → Order here → ... → Worldwide Shipping!" #giftforall #fathersday
- **Angle/mechanic:** Lifestyle/identity (camping + pets + family). 3D-effect visual gimmick is the hook. Longest still-active image creative.

### 4. Golf Ball "If Found Return To This Guy" · **416 days**
- VIDEO · creatives 1 · 2024-03-21 → 2025-05-11 · $16.95 · dad/grandpa/golfer humor angle.

### 5. "Proud Father Of A Few" T-Shirt · **415 days**
- **URL:** /products/proud-father-of-a-few-funny-gift-for-dad-father-grandpa-personalized-t-shirt (`ak982nah3096-fbf`)
- VIDEO · creatives 1 · 2024-03-26 → 2025-05-15 · $24.99
- **Caption:** *"Hilarious Gift For Dad"* · **Copy:** "Every Proud Dad Has His Own Special Story to Tell 🤣"
- **Angle:** Humor + dad/grandpa identity. Number of kids personalizes it. Grandparent-adjacent.

### 6. "Dear Mom, Great Job We're Awesome" T-Shirt · **386 days**
- **URL:** ...gift-for-mother-grandma-grandmother-personalized-custom-t-shirt (`vt166hal1096-fbf`)
- VIDEO · **creatives: 3** · 2024-03-28 → 2025-04-18 · $24.99
- **Caption:** *"Cool Tee For Mommy"* · **Copy:** "Let Mom Know She's Amazing ❤️"
- **Angle:** Humor/affection from-the-kids POV; mother/grandma. #great #grandma #mom #parents.

### 7. Nana/Auntie/Mom Sunflower Suncatcher · **381 days** ⭐ GRANDPARENT
- **URL:** /products/nana-auntie-mom-family-sunflower-...-suncatcher-ornament (`ak1160nah3530`)
- **Format:** VIDEO · creatives: 1 · started 2025-03-18 · lastSeen 2026-04-03 · **$26.95**
- **Performance:** EU-index adscore reads "Testing" (only $4.72 EU spend — this is a **US-run** creative, EU index sparse per house rules), but **381 days live = revealed US winner.** Newer page variant has **129K page likes.**
- **Copy (verbatim):** "Brighten the lives of the special women with the Suncatcher Ornament" #kids #family #mother #giftforher #motherday
- **Angle/mechanic:** Multi-generation naming (Nana + Auntie + Mom) on ONE product → maximizes personalization slots + gift occasions. Sunflower = warmth. Sun-catcher = light/visual demo mechanic in video.

---

## OTHER MEMORIAL / BIRTH-FLOWER / GRANDPARENT LANE CREATIVES (shorter run, same playbook)

| Product | Fmt | Creatives | Days | Price | Hook / Copy |
|---|---|---|---|---|---|
| Memorial "Always With You" suncatcher (`gt481nel2311`) | video | 1 | 391 | $22.95 | "Not Just An Ornament, It's A Beautiful Symbol Of Family Love 💖" |
| "Now You Can Carry Me Too" aluminum wallet card | image | 3 | 496 | $19.99 | "Personalized Gift For Dad!" — new-parent/dad keepsake |
| Besties "Sitting On The Moon" suncatcher (`fl557dil973`) | video/img | 2–3 | 335 | $26.95 | "Celebrate The Bond Of Friendship" / "Let Your Friendship Shine Bright ✨" |
| **Birth-Flower "Grow An Old Friend"** stained-glass suncatcher (`fl661nel2719`) | video | 2 | 70 | $25.95 | "A wonderful gift for your best friend!" #birthflower #evergreen |
| Pet-Loss Collar Frame "My Hardest Goodbye" (2nd creative `bd1344...`) | video | 2 | 86 | $33.95 | (see #2) |
| Memorial "Your Light Will Always Shine" candlelight lantern | video | 2 | 97 | $21.95 | "Illuminate Your Memories This Christmas 🕯️🐾" |
| "A Piece Of My Heart Is At The Rainbow Bridge" pet car hanger | video | 1 | 50 | $18.95 | "Keep Their Memory Alive with Every Mile You Drive 💖" |
| Grandpa/Dad Kids-Handprints Cap (`nn452hel1081`) | image | 2 | 44 | $29.95 | "Awesome Personalized Gift For Grandpa & Dad" |
| "To My Granddaughter" pillow | image | 1 | 33 | $25.95 | "Personalized Gift For Grandma & Grandkid!" |
| Granddaughter Unicorn-Hug pillow | image | 7 | 183 | $25.95 | "Personalized Gift For Daughters And Granddaughters!" |
| Mom's/Grandma's Sweethearts LEATHER BAG (`kk...`) | video | 1 | 25 | $45.95 | "A Lovely Reminder To Grandma About The Love She Carries ❤️" (highest AOV) |
| "Mother/Daughters Is Forever" flameless LED candle (`kk1117dil1420`) | video | 2 | 344 | $27.95 | mother-daughter bond, light mechanic |

---

## PATTERN SYNTHESIS

**Format mix:** Longest runners skew **VIDEO** (bracelet, collar frame, suncatchers, tees). Doormat/pillow/mug winners are IMAGE. Video wins the ≥400-day tier; images win the visual-gimmick tier (3D doormat).

**Creative count:** Confirms archetype — **1–4 creatives per product** even for 800-day winners. They do NOT iterate heavily; they find a winner and let it ride for years. `countActive` of 3 on the flagship bracelet at 803 days is the tell.

**Copy skeleton (near-universal template):**
1. One benefit/emotion line (often with 1 emoji: ❤️ 🌈 🐾 💖 ✨ 🕯️)
2. "Order here → [short branded slug link]"
3. "Worldwide Shipping!"
4. Long hashtag block encoding the exact target (relation + occasion + niche)

**Caption line** (separate short field) is a punchy category label: "Beautiful Way To Remember Your Loved Ones," "Memorial Gift For Pet Parents," "Hilarious Gift For Dad."

**Emotional angles, in order of longevity payoff:**
1. **Memorial / grief** (human + pet) — the two longest runners. "Carry them with you," "Frame the memories," rainbow-bridge.
2. **Multi-generation identity naming** (Nana/Auntie/Mom on one SKU) — maximizes personalization + occasions.
3. **Humor + relation identity** (Proud Father Of A Few, Dear Mom Great Job) — from-the-kids POV.
4. **Bond/relationship** (besties, mother-daughter, birth-flower "old friend").

**Mechanic:** Every winner is a **custom-photo or custom-name personalization** on a **physical keepsake** (bracelet, frame, suncatcher, ornament, doormat). The personalization IS the ad — mockup shows the customized result.

**Offer posture:** Soft evergreen **WP10 = 10% off** code, "Worldwide Shipping" as the only recurring closer. No scarcity/urgency stacking. They win on emotional resonance + evergreen longevity, not on discount pressure.
