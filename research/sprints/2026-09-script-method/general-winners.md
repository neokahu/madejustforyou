# General long-runners: video ad script structure

This study covers long-running US-targeted Meta video ads. It compares personalized-gift ads with non-gift DTC ads, which are included for contrast. It was built only from `raw/general-beats-batch1-4.md`. No new WinningHunter calls or web lookups were made for this write-up.

**Sample:** 23 candidates. **16 have verified visuals** (8 gift, 8 non-gift) and 7 are VISUALS UNVERIFIED. Every count below uses the 16 verified ads only. N is stated each time.

---

## 1. Method, filters, credits

**Pulls.** Six WinningHunter `search_facebook_ads` pulls were made. All used country=US, videos only and English.

| pull | filter | min days active |
|---|---|---|
| keyword "personalized" | sorted by reach | 90 |
| keyword "memorial" | product pages | 90 |
| keyword "custom pet" | product pages | 90 |
| niche HI (home) | — | 180 |
| niche CG (apparel) | — | 180 |
| niche EL (electronics) | — | 180 |

- **Longevity measure.** `days_active` = lastSeen − started. Ads are validated on longevity, not on seller count.
- **Selection.** Candidates were picked for category spread and deduped by landing URL. Raw pulls are in `raw/general-search-*.json` and the candidate list is in `raw/general-candidates.json`.
- **Beat maps.** Each beat map was built from:
  - ffmpeg frame contact sheets, at 1s steps for 0-5s and then every 2.5-3s
  - scene-cut detection (`select='gt(scene,0.3)'`)
  - transcripts from WinningHunter `get_ad_transcript`, or from local whisper.cpp when WinningHunter failed
- **Credits.** The balance went from 19,998 to 19,936, so at most 62 credits were used (about 0.3%). That figure includes any spend by a concurrent agent.
- **Unverified ads.** For these 7, the video links had expired (fbcdn signature expired, WinningHunter media 404) and WinningHunter transcripts returned `download_failed`:

| advertiser | product | category | days |
|---|---|---|---|
| Wander Prints | "Besties sitting on the moon" suncatcher | gift: friends | 159 |
| Gifts For Family (pawfecthouse) | "Cat's Trip" car sunshade | gift: pet | 624 |
| Personalized Family Gifts (trendingcustom) | "Always With You" memorial keychain | gift: memorial | 295 |
| DoyoBest | "Brothers & Sisters Forever" poster | gift: family | 596 |
| Wander Prints | "My Hardest Goodbye" pet collar frame | gift: pet memorial | 757 |
| Awesome Personalized Gifts | "Together Since" couple plaque | gift: couple | 250 |
| Pride Of Winners (pawfecthouse) | "Hug This Pillow" pet memorial pillow | gift: pet memorial | 657 |

All 7 unverified ads are gift ads. As a result, the verified gift set has **no friends ads and no family (non-memorial) ads**. It also loses the oldest gift creatives: 4 of the 7 ran for more than 590 days.

**Caveats**
- True Tailor is UK-flavoured ("tradies", SAS).
- Giftstail reaches mostly EU/UK, and its end card says Sunflowerly.com, so it is a reused creative.
- MAGIC JOHN looks TikTok Shop-native ("click the yellow cart").
- "US" means the ad targets the US, not that the store is US-only.
- Wrappiness and Giftstail look AI-rendered.
- Cut detection at 0.3 misses crossfades and soft transitions, so cuts/sec is a floor.
- The gift pulls required at least 90 days and the non-gift pulls at least 180 days, so days_active **cannot be compared across groups**.

---

## 2. Verified ads

| # | advertiser | category | product | days | length | format | link |
|---|---|---|---|---|---|---|---|
| G1 | Soufeel | gift: couple | photo "music player" fridge magnet | 303 | 15.2s | demo | soufeel.com/products/customized-music-fridge-magnet-personalized-photo-fridge-magnet-can-play-songs-and-adjust-volume |
| G2 | Hope Rings | gift: memorial | "Hug From Heaven" engraved ring, $39.99 | 317 | 33.5s | UGC | hoperings.com/products/hug-from-heaven |
| G3 | Cuddle Clones | gift: pet memorial | custom pet plush, $209.99 | 168 | 151.8s | mixed (founder + UGC + process) | cuddleclones.com/products/custom-pet-memorial-plush-cuddle-clone |
| G4 | Macorner | gift: couple | caricature boxer briefs, $29.95 | 192 | 23.8s | mixed (UGC + site screen-rec) | macorner.co/products/f-valentines-day-i-love-you-every-day-gifts-for-him-personalized-mens-boxer-briefs-hus100101tvhn |
| G5 | Wrappiness | gift: memorial | memorial car ornament, $20.99 | 210 | 23.9s | demo (AI-look) | wrappiness.co/products/those-we-love-beside-us-every-day-personalized-custom-car-ornament |
| G6 | Doggovinci | gift: pet memorial | photo keychain, $19.99 | 197 | 18.0s | demo | doggovinci.com/products/dog-keychain-dog-memorial-gifts-for-loss-of-dog-personalized-keychains-pet-memorial-gifts-cat-keychain |
| G7 | Paw Lux Gems | gift: pet memorial | engraved pet-photo necklace, ~$20 | 682 | 11.9s | demo (maker process) | pawluxgems.com/products/pet-photo-necklace |
| G8 | Giftstail | gift: memorial (mom) | photo-shaped faux-fur pillow, $37 | 235 | 18.6s | slideshow (AI renders) | giftstail.com/products/custom-from-photo-when-you-miss-me-personalized-memorial-faux-fur-shaped-pillow |
| N1 | Seure | gadget | magnetic Apple Watch band, $35 | 473 | 15.9s | demo | seure.co/products/fearless-silicone-magnetic-band-for-apple-watch |
| N2 | Mookly | home | paint edger, $19.90 | 407 | 18.0s | demo | mookly-shop.com/products/paint |
| N3 | Forge Wallet | accessory | smart leather wallet, $48 | 635 | 51.5s | UGC (POV) | forge-wallet.com/products/forge-leather-wallet |
| N4 | Ooomay | accessory | vegan-leather tote, $45 | 465 | 9.5s | UGC (POV text) | ooomay.com/collections/all-bags/products/maya-tote |
| N5 | Roha Home | home | no-drill suction hooks, $39.99 | 485 | 36.5s | demo (silent) | roha-home.com/products/no-drill-aesthetic-hooks |
| N6 | Statik | gadget | magnetic mini power bank, $29.99 | 426 | 38.9s | mixed (testimonial VO + b-roll) | statikco.com/products/snap-n-charge-v1 |
| N7 | True Tailor | apparel | waterproof work trousers, $59.99 | 398 | 80.0s | founder (VO over b-roll) | thetruetailorcompany.com/products/ultraflex-waterproof-gortex-utility-trousers-sas |
| N8 | MAGIC JOHN | gadget | 4-in-1 240W cable, $16.98 | 383 | 75.5s | mixed (skit → presenter) | magicjohn.com/products/magic-john-4-in-1-usb-charging-cable-mfish-fast-charging |

**Format totals (N=16)**

| format | total | gift | non-gift |
|---|---|---|---|
| demo | 7 | 4 | 3 |
| mixed | 4 | 2 | 2 |
| UGC | 3 | 1 | 2 |
| founder | 1 | 0 | 1 |
| slideshow | 1 | 1 | 0 |
| **story-film** | **0** | 0 | 0 |

---

## 3. Per-ad beat maps (condensed)

In each map, `P@` is the second the product first appears. Audio is marked M (music only), VO (voiceover), T (on-screen text carries the message) or S (silent).

**G1 Soufeel (15.2s, 0 cuts, M)**
- **Beats:** 0-2 cluttered fridge; a hand with a Coke can reaches to the magnet → 2-4 presses play → 4-11 slow push-in on the couple photo and "Beautiful" track UI → 11-15 pull back; a second magnet shows "Ethan ♥ Sunny".
- **P@0.3.** Hook: product-reveal. No on-screen text. Personalization: result only.
- **Proof:** none. **Offer:** none. **CTA:** none in video; copy says "Order now →".

**G2 Hope Rings (33.5s, 9 cuts, T+M)**
- **Beats:**
  - 0-3 ring on hand: "This is more than just a ring 🥺"
  - 3-7.6 woman on sofa opens the box, hand to mouth: "I got it as a gift after my dad passed away 😭💔"
  - 7.6-14 "reminder of his love"
  - 14-17 "free engraving…" (not legible)
  - 17-22 angel-wing message card
  - 22-28.6 packaging: "he will always be by my side"
  - 28.6-33.5 white end card
- **P@0.3.** Hook: emotional moment plus a curiosity line. Personalization: mentioned, not shown.
- **Proof:** crying reaction and first-person testimonial.
- **Offer:** "50% Off + Free Shipping" and "Engraving & Message Card Included". **CTA:** "Order Today".

**G3 Cuddle Clones (151.8s, 64 cuts, VO + captions)**
- **Beats:**
  - 0-5 girl crying and hugging the plush: "What if you could bring a beloved pet back home for the holidays…?"
  - 5-18 presenter with her own bulldog; unboxing
  - 18-30 grief problem ("pain of losing them")
  - 30-70 process: photo upload screen, ear-position picker, artist pattern work
  - 70-99 grandmother, young man and girl hug plushes; shelter donation
  - 99-113 money-back guarantee
  - 113-131 "Over 10,000 pet parents", 5★ review cards
  - 131-146 holiday cutoff and "$150 OFF"
  - 146-152 CTA and logo
- **P@0.3.** Hook: question over an emotional moment. Personalization: process shown.
- **Proof:** reactions, a number, reviews and a guarantee. **Offer:** $150 off plus urgency.
- **CTA:** "Start creating your cuddle clone today".

**G4 Macorner (23.8s, 9 cuts, M song + T)**
- **Beats:**
  - 0-1 flat-lay: "SALE WON'T LAST / CUSTOMIZE YOUR GIFT NOW"
  - 1-2.4 "This is NOT the Valentine's gift I planned…he can't stop laughing about"
  - 2.4-4.5 husband laughing, holding the boxers
  - 5-8.4 wife's hand on the caricature print ("VINCENT ♥ SANDRA"): "customized exactly like us"
  - 8.4-14.6 "Quality is pretty good" / "men…want something dumb, spicy, and personal"
  - 14.6-21 phone screen-recording of the personalizer and "Buy 2+, Save 10%"
  - 22-23.8 logo
- **P@0.** Hook: offer, then a story caption. Personalization: process shown.
- **Proof:** reaction and a quality caption. **Offer:** sale plus bundle. **CTA:** "CUSTOMIZE YOUR GIFT NOW".

**G5 Wrappiness (23.9s, 3 cuts, M ballad)**
- **Beats:**
  - 0-4 ornament in a kraft box ("Dad 2019 / Mom 2023"): "THIS CAR ORNAMENT TRULY TOUCHED MY HEART..."
  - 4-6.5 hung on the mirror
  - 6.5-20.6 swinging in golden light; hands cradle it
  - 20.6-23.9 back in the box: "THEY ARE NO LONGER HERE, BUT I BELIEVE THEY ARE ALWAYS WATCHING OVER ME ❤"
- **P@0.** Hook: testimonial caption plus unboxing reveal. Personalization: result only.
- **Proof:** none. **Offer:** none. **CTA:** none in video.

**G6 Doggovinci (18.0s, 3 cuts, VO)**
- **Beats:** 0-4.2 two keychains on a table (Lab photo; "MAX" engraving) → 4.2-8.9 lifted and dangled → 8.9-17.3 macro on quality → 17.3-18 black frame.
- **VO:** "live customization keychains allow you to preview… prior to purchase. Crafted in stainless steel, laser engraved…"
- **P@0.** Hook: product-reveal. Personalization: result shown; the process is only claimed in the VO.
- **Proof:** feature claims only. **Offer:** none. **CTA:** none.

**G7 Paw Lux Gems (11.9s, 6 cuts, borrowed film dialogue + T)**
- **Beats:** 0-1.6 drawer opens: "the perfect pet memorial 🤍🕊️✨" → 1.6-3.3 pendants; chain goes on the laser → 3.3-6 dog photo on a phone becomes line art → 6-8.6 laser engraving → 8.6-10.5 polish → 10.5-11.9 finished pendant in palm.
- **Audio:** "I come to say goodbye… Charlie, will I ever see you again? Sure, sure you will."
- **P@1.** Hook: grief audio plus reveal. Personalization: process shown.
- **Proof:** none. **Offer:** none in video (copy: "TODAY Only 50% OFF"). **CTA:** none.

**G8 Giftstail (18.6s, 3 cuts, M + T)**
- **Beats:**
  - 0-4 render of a crying young woman hugging a grandma who holds the "Mom 1932-2025" pillow: "When the nights feel loneliest…one familiar embrace"
  - 4-14 real-looking portraits: "Upload their photo and instantly preview…" / "Soft faux fur…"
  - 14-17 doll pillow "Dora 1953-2025"
  - 17-18.6 CTA
- **P@0.** Hook: emotional moment (family). Personalization: photo → pillow shown.
- **Proof:** none. **Offer:** none.
- **CTA:** "Create your personalized memorial pillow today at Sunflowerly.com".

**N1 Seure (15.9s, 10 cuts, M)**
- **Beats:** 0-1.2 band on watch, 2 colourways → 1.2-4.2 stretched and twisted → 4.2-9 magnetic clasp → 9-15.9 on wrist, colour variants.
- **P@0.3.** Hook: product-reveal. No text.
- **Proof:** flex demo only. **Offer:** none. **CTA:** none in video.

**N2 Mookly (18.0s, 13 cuts, M)**
- **Beats:** 0-1.8 masked man edging the ceiling line → 1.8-5.2 corner and crisp stripe → 5.2-6.3 grey "old way" clip with a red X → 6.3-16 edging around a detector and a door frame → 16-18 finished wall.
- **P@0**, in use. Hook: product-reveal.
- **Proof:** before/after. **Offer:** none. **CTA:** none in video.

**N3 Forge (51.5s, 0 cuts, VO)**
- **Beats:** 0-3.5 POV in a car, grabs the wallet: "Bro, ditch your old wallet…" → 3.5-11.7 card pop-up and cash room → 11.7-15.6 "I get a lot of compliments" → 15.6-21.8 button and zipper → 21.8-26 "huge promotion… drop that link below" → 26-37 variants and unboxing → 37-43 "perfect gift for a husband, brother, father" → 43-51.5 zipper sound and close.
- **P@~1.** Hook: callout plus reveal.
- **Proof:** spoken testimonial and live demo. **Offer:** spoken promotion.
- **CTA:** "drop that link below… Forge Wallet is the way to go".

**N4 Ooomay (9.5s, 2 cuts, audio unverified, T)**
- **Beats:** 0-0.9 bag drops into frame → 0.9-8.5 MacBook, tablet, wallet and headphones go in → 8.5-9.5 bag lifted out (loop point).
- **Text throughout:** "pov: you found the perfect summer bag that fits your whole life".
- **P@0.2.** Hook: POV callout plus reveal.
- **Proof:** capacity demo. **Offer:** none. **CTA:** none.

**N5 Roha (36.5s, 7 cuts, S)**
- **Beats:** 0-4.5 handbag hanging on a hook (result first) → 4.5-10.3 kraft-box unboxing → 10.3-22 install, then the bag hung → 22-31 two more surfaces → 31-36.5 towel hung.
- **P@0.3.** Hook: result-first reveal. No text or sound.
- **Proof:** load demo. **Offer:** none in video (copy: "2+2… stock limited"). **CTA:** none in video.

**N6 Statik (38.9s, 30 cuts, VO + word captions)**
- **Beats:**
  - 0-2.4 pouch torn open by a lake: "Don't let your kids go on vacation without one of these."
  - 2.4-8.7 multi-device demo
  - 8.7-17.8 "nervous about her phone dying… got her a 3-pack… best gift she ever got"
  - 17.8-31.9 safety, photos, "so relieved to get texts from her"
  - 31.9-34 CTA
  - 34-38.9 end card
- **P@0.3** (pack), device at 1s. Hook: callout to parents.
- **Proof:** parent testimonial and demo.
- **Offer:** "50% OFF" and "save up to $209 with a 5-pack".
- **CTA:** "Grab your Snap N Charge" / "CLICK THE LINK".

**N7 True Tailor (80.0s, 48 cuts, VO + captions)**
- **Beats:**
  - 0-3 "What the SAS know that tradies don't" / "military secret… sold over 65,000 pairs"
  - 3-10 founder intro
  - 10-23 problem: canvas is "Stiff ❌"
  - 23-45 mechanism: ripstop, "4x more flexible ✅", water pour
  - 45-61 stretch, scissors, "torture-tested"
  - 61-73 BOGO, "10,000+ HAPPY CUSTOMERS", 30-day guarantee
  - 73-80 CTA
- **P@~3.** Hook: curiosity plus callout plus a number.
- **Proof:** numbers, demos and a guarantee. **Offer:** "BUY 1 GET 1 FREE — TODAY ONLY".
- **CTA:** "upgrade to True Tailor today".

**N8 MAGIC JOHN (75.5s, ~0 cuts, dialogue + subtitles)**
- **Beats:** 0-3 masked kid tries a plug-shaped object in a phone → 3-26 comedic skit and transition → 26-38 cable plugged in; screen shows "Max 66W" → 38-68 specs (4-in-1, 240W, zinc, silicone) → 68-72 bonus carry bag → 72-75 CTA.
- **P@~26.** Hook: shock/comedy pattern-interrupt.
- **Proof:** live charging screen. **Offer:** bonus bag only (copy: buy 2 get 15% off).
- **CTA:** "click the yellow cart and purchase it now".

---

## 4. Patterns with counts

### Product first appearance

| metric | gift (N=8) | non-gift (N=8) | all (N=16) |
|---|---|---|---|
| product on screen by ≤1s | **8/8** | 6/8 | 14/16 |
| product on screen by ≤0.3s (first frame) | 7/8 | 5/8 | 12/16 |
| median first appearance | 0.15s | 0.3s | 0.3s |
| latest | 1s (G7) | 26s (N8) | 26s |

The two late ones are both long talking ads: True Tailor (3s) and MAGIC JOHN (26s).

### Audio

| audio | gift (N=8) | non-gift (N=8) |
|---|---|---|
| music only, no VO or dialogue | **5** (G1 G2 G4 G5 G8) | 2 (N1 N2) |
| borrowed dialogue sound, no VO | 1 (G7) | 0 |
| silent | 0 | 1 (N5) |
| audio unverified | 0 | 1 (N4) |
| VO / presenter / dialogue | 2 (G3 G6) | 4 (N3 N6 N7 N8) |

- **No VO at all:** 6/8 gift vs 3/8 non-gift (3 of 7 when the unverified audio is excluded).
- **On-screen text carries the message when there is no VO:** gift 5/8 (G2 G4 G5 G7 G8), non-gift 1/8 (N4).

### Hook, first 3 seconds

| hook type | gift (N=8) | non-gift (N=8) |
|---|---|---|
| emotional / grief moment | **4** (G2 G3 G7 G8) | **0** |
| testimonial caption ("touched my heart", "NOT the gift I planned") | 2 (G4 G5) | 0 |
| wordless product-reveal | 2 (G1 G6) | 3 (N1 N2 N5) |
| callout ("Bro", parents, POV) + reveal | 0 | 3 (N3 N4 N6) |
| curiosity / shock pattern-interrupt | 0 | 2 (N7 N8) |

The 4 emotional hooks come from 4 of the 6 memorial-themed gift ads. The other two memorial ads are G5 and G6.

### Personalization (gift only, N=8)

- **Personalized result legible on the product** (names, photo or dates): 7/8. The exception is G2, whose engraving is not legible.
- **Customization process shown:** 4/8.
  - G3: upload screen
  - G4: screen recording of the site personalizer
  - G7: photo → laser engraving
  - G8: photo → pillow
- **Result only:** 4/8 (G1, G5, G6, and G2 where it is only mentioned).

### People on screen

| metric | gift (N=8) | non-gift (N=8) |
|---|---|---|
| human face on screen | 4 (G2 G3 G4 G8) | 3 (N6 N7 N8) |
| hands only | 4 | 4 (N1 N3 N4 N5) + N2 masked |
| reaction shot to the product (tears, laughter, hug) | **4** (G2 G3 G4 G8) | **0** |
| giver and receiver clearly together on screen | 1 (G8, AI render) | 0 |

### Proof

**Gift (N=8)**
- Any proof: 3/8 (G2 G3 G4), and all 3 include reactions.
- Numbers or reviews on screen: 1/8 (G3).
- No proof at all: 5/8.

**Non-gift (N=8)**
- Functional demo as proof (before/after, load, capacity, live charging, water pour): 7/8, with N1 flex-only.
- Numbers: 1/8 (N7).
- Spoken testimonial: 2/8 (N3 N6).

### Offer

| metric | gift (N=8) | non-gift (N=8) |
|---|---|---|
| offer shown or spoken in the video | 3 (G2 50% + free ship; G3 $150 off; G4 sale + bundle) | 3 (N3 promo; N6 50% / 5-pack; N7 BOGO) |
| offer in the video or the ad copy | 4 (adds G7) | 5 (adds N5, N8) |

### CTA

- **In-video CTA (spoken or on screen):** gift 4/8, non-gift 4/8.
- **By speech:**
  - Ads with VO or dialogue (N=6): 5 have an in-video CTA. Only G6 lacks one.
  - Ads with no speech (N=10): 3 have one (G2, G4, G8).
- **CTA verbs:**
  - Gift: "create" or "customize" in 3 of 4 (G3, G4, G8), plus "Order Today" (G2).
  - Non-gift: buy or click verbs ("grab", "click the link", "click the yellow cart", "upgrade", "drop that link below").
- **"today" or "now" in the CTA:** 7 of the 8 in-video CTAs. Forge is the exception.
- **Button** (N=12 where known): Shop now 9, Learn more 3 (G6, G8, N2).
- **Branded end card or logo:** gift 3/8 (G2 G3 G4), non-gift 1/8 (N6).

### By format

| format | N | length median | cuts/sec median | product ≤1s | VO | emotional hook |
|---|---|---|---|---|---|---|
| demo | 7 | 18.0s | 0.19 | 7/7 | 1/7 | 1/7 (G7) |
| mixed | 4 | 57.2s | 0.40 | 3/4 | 3/4 | 1/4 (G3) |
| UGC | 3 | 33.5s | 0.21 | 3/3 | 1/3 | 1/3 (G2) |
| founder | 1 | 80.0s | 0.60 | 0/1 | 1/1 | 0 |
| slideshow | 1 | 18.6s | 0.16 | 1/1 | 0/1 | 1/1 (G8) |

### Other counts

- **Memorial theme:** 6/8 of the verified gift ads. This is inflated because "memorial" was one of the pull keywords.
- **AI-render look:** 2/8 gift ads (G5, G8). Both still ran 210+ days.
- **Gift angle inside non-gift ads:** 2/8 (N3 "gift for a husband…", N6 a parent buying for her daughter).

---

## 5. Gift/emotional vs utility DTC: structural differences

| dimension | gift (N=8) | non-gift (N=8) | read |
|---|---|---|---|
| emotional hook in the first 3s | 4 | 0 | gift-specific |
| reaction shot | 4 | 0 | gift-specific |
| no VO | 6 | 3 (of 7 known) | gift ads lean on captions and music |
| the text layer tells the story | 5 | 1 | same |
| main proof | reaction/testimonial (3); none (5) | functional demo (7) | gift ads prove feeling, not function |
| product ≤1s | 8 | 6 | both groups front-load the product; gift ads always do |
| personalization legible | 7 | n/a | the name or photo *is* the product shot |
| median length | 21.2s | 37.7s | gift ads are shorter |
| median cuts/sec | 0.22 | 0.405 | gift ads are slower (about one cut per 4.5s) |
| offer in video | 3 | 3 | no difference |
| in-video CTA | 4 | 4 | no difference |

**Beat shapes**
- **Gift:** *personalized result (0s) → feeling line or reaction → how it is personalized or what it means → payoff or CTA*.
- **Non-gift:**
  - *product in use (0s) → demo or mechanism → proof → offer/CTA*, with a problem beat in 3 of 8 (N2, N6, N7).
  - The long non-gift ads (N3, N6, N7, N8, all 38-80s) are all speech-driven.
  - The one long gift ad (G3, 152s) is also speech-driven, with a full offer stack. It is the most expensive product in the sample ($209.99). Every other gift product costs $20-40.

---

## 6. Length and pacing

### Length (seconds)

| group | lengths | median | range | ≤25s |
|---|---|---|---|---|
| gift | 11.9, 15.2, 18.0, 18.6, 23.8, 23.9, 33.5, 151.8 | **21.2** | 11.9-151.8 | 6/8 |
| non-gift | 9.5, 15.9, 18.0, 36.5, 38.9, 51.5, 75.5, 80.0 | **37.7** | 9.5-80.0 | 3/8 |
| all (N=16) | — | 23.85 | 9.5-151.8 | 9/16 |

### Cuts per second (scene > 0.3, so a floor)

| group | values | median |
|---|---|---|
| gift | 0, 0.13, 0.16, 0.17, 0.27, 0.38, 0.42, 0.50 | **0.22** |
| non-gift | 0, 0.01, 0.19, 0.21, 0.60, 0.63, 0.72, 0.77 | **0.405** |
| all (N=16) | — | 0.24 |

**Non-gift pacing is bimodal:**
- Continuous single takes: N3, N4, N8 (≤0.21).
- Fast-cut montages: N1, N2, N6, N7 (0.60-0.77).

No gift ad goes above 0.50 cuts/sec.

---

## Implications for MadeJustForYou scripts

**Evidence tags**
- **[consistent]**: the same result in all or nearly all of the relevant ads.
- **[majority]**: 5-6 of 8.
- **[split]**: about half the ads.
- **[none]**: no data.

**Limits**
- n is 8 per group.
- The sample is selection-biased: it was picked for spread, the gift set is memorial-heavy, and it has no friends or family (non-memorial) ads.
- It is survivorship-biased: we only see what kept running, not what failed with the same structure.
- Long-running is a proxy for profitable, not proof of it.

**Rules**

1. **The personalized product with a name or photo legible goes on screen within 1s.** [consistent: 8/8 gift ≤1s, 7/8 legible] This is the strongest signal here. It also holds for 6/8 non-gift ads, so it is a general Meta norm, not a gift trick.
2. **Target 15-25s for a $20-40 gift.** [majority: 6/8 gift ≤24s; median 21.2s] Go long (60s+) only when a VO carries an offer stack and guarantee on a high-ticket item. The only case is G3, n=1.
3. **Music plus on-screen captions, with no VO, is a valid default for gift ads.** [majority: 6/8 no VO; 5/8 text-led] If there is no VO, write the CTA on screen: only 3 of the 10 no-speech ads had one.
4. **Open on feeling for memorial and sentimental products.** [split: 4/8 gift, 4/6 memorial; 0/8 non-gift] Use a tearful or grief moment, or a first-person line like "This is more than just a ring". The gift-vs-non-gift contrast is clear, but the memorial skew may be driving it.
5. **Keep pacing slow, about one cut every 4-5s** (≈0.2 cuts/sec). [majority: gift median 0.22, max 0.50] Do not copy fast-cut gadget montages.
6. **Show the personalization process as a beat.** [split: 4/8] Options are a screen recording of the personalizer, photo→product, or photo→engraving. It is common but not required. A/B test "process shown" vs "result only". Do not assume it wins.
7. **Show a reaction or a face.** [split: 4/8 face and reaction; only 1/8 shows giver and receiver together, and it is an AI render] This does not contradict the "show family connection" rule, but it gives that rule almost no support. Treat it as untested.
8. **Proof, offer and CTA in the video are optional, not structural.** [split: proof 3/8, offer 3/8, CTA 4/8] Long-runners survive without them, often because the ad copy carries the offer. If you include a CTA, use a create/customize verb plus "today" or "now". [3 of 4 gift CTAs use create/customize; 7 of 8 CTAs overall use today/now]
9. **An AI-rendered look did not stop longevity.** [weak: 2/8, both 210+ days] n is too small to conclude either way.
10. **Story-film format: no evidence.** [none] This sample has **zero** story-film ads, so it neither supports nor refutes the Thai-style story-film direction. The nearest cases are:
    - G2: a caption-told grief story over product shots, 33.5s.
    - N6: a VO parent story over b-roll.

    Neither is a narrative film with the product as a late payoff. In fact, every verified gift ad puts the product on screen by 1s, which is the opposite of a late reveal. That tension should be tested directly, not assumed away.
