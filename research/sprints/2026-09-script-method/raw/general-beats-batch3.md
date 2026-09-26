# General beat maps — batch 3

Source: WinningHunter `get_ad_transcript` + `scan_ad` (saved as `general-transcript-<id>.json` / `general-scan-<id>.json`; for 1737721673670281, 555194367334992 and 7244975012222216 the scan came back inline and was saved as a key-field extract), plus local ffmpeg analysis of the downloaded video. Cuts = ffmpeg `select='gt(scene,0.3)'` count. Contact-sheet frames were checked visually.

Advertiser check: the scan `pageName` matches the candidate page for all 6 ads.

---

### DoyoBest — Personalized "Brothers & Sisters Forever" poster/canvas (ad 1737721673670281)
**VISUALS UNVERIFIED. AUDIO/TRANSCRIPT UNAVAILABLE.** The fb_video URL has expired (oe=2024-10). The wh_video hash returned 404 on every media.winninghunter.com path tried. WH transcript returned `download_failed` (no credit charged). Everything below comes from metadata only.
- category: personalized gift: family (siblings; the product title also says "Memorial Keepsake")
- days_active: 596 (2024-10-24 → 2026-06-12); landing: https://doyobest.com/products/9705559654717; price: $23.99 (compare-at $34.99)
- length: unknown; cuts: unknown; format: unknown (display_format = video)
- audio: unknown
- hook (0-3s): unknown. Ad-copy hook: "🎁 Personalized Poster For Siblings 🎁 Love between brothers & sisters is forever"; hook type: unverifiable (copy reads as a callout to siblings)
- product first appears: unknown
- personalization shown? unknown
- proof element: unknown (store Trustpilot 4.5, 5,913 reviews; not in the ad)
- offer: none in copy (site compare-at $34.99 → $23.99); CTA wording: ad-copy "👇🏻👇🏻Shop Now👇🏻👇🏻"; button "Shop now"
- beats: not mappable (no video)
- transcript: none available

### Paw Lux Gems — Custom pet photo engraved necklace (ad 555194367334992)
- category: personalized gift: pet (on-screen text frames it as a memorial: "the perfect pet memorial")
- days_active: 682 (2024-11-12 → 2026-09-25); landing: https://pawluxgems.com/products/pet-photo-necklace; price: $20 per scan (compare-at $50); candidate price blank
- length: 11.9s; cuts: 6 (≈0.50 cuts/sec); format: demo (a "how it's made" maker-process clip: hands only, drawer → laser engraver → phone photo → engraving → polishing → finished pendant)
- audio: dialogue from a borrowed film/TV clip used as a trending sound ("I come to say goodbye… Charlie, will I ever see you again?"). No VO. The speakers are never on screen.
- hook (0-3s): a hand in a red sleeve opens a white drawer full of gold disc necklaces. Text: "the perfect pet memorial 🤍🕊️✨". Audio: "I come to say goodbye." Hook type: emotional moment (grief audio) + product-reveal
- product first appears: 1s (blank/finished necklaces in the drawer). Engraving machine with chain at 2s.
- personalization shown? yes. Dog photo on phone at 4s, converted to line-art at 5s, laser-engraved onto the pendant at 6–8s, finished engraved dog pendant at 11.5s
- proof element: none
- offer: none in video. Ad copy: "TODAY Only… 50% OFF Sale" (urgency + discount). CTA wording: none on screen or spoken. Ad copy has no explicit CTA line; button "Shop now"
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-1.6 | hook | hand opens drawer | "I come to say goodbye." | "the perfect pet memorial 🤍🕊️✨" |
| 1.6-3.3 | reveal | drawer of gold pendants; chain placed on laser engraver | "Where are you going?" | same (0-~1.6s) |
| 3.3-6.0 | personalization | phone shows a husky puppy photo, then a line-art version | "My, it's not a long trip." | none |
| 6.0-8.6 | personalization/demo | laser engraving the dog face onto the pendant (macro) | "Charlie, will I ever see you again?" | none |
| 8.6-10.5 | demo | pendant polished with a blue cloth | — | none |
| 10.5-11.9 | reveal (payoff) | finished engraved dog-face pendant in palm | "Sure, sure you will." | none |

- transcript: "I come to say goodbye. Where are you going? My, it's not a long trip. Charlie, will I ever see you again? Sure, sure you will."

### Ooomay — "The Maya" vegan-leather tote (ad 584144738072726)
- category: accessory (bag)
- days_active: 465 (2025-06-16 → 2026-09-24); landing: https://ooomay.com/collections/all-bags/products/maya-tote; price: $45.00
- length: 9.5s; cuts: 2 (≈0.21 cuts/sec); the detector's cuts are hand-motion jumps, and it is effectively one static locked-off shot. Format: UGC-style "what fits in my bag" demo (a POV text overlay on one static shot of the bag on a bed, a hand loading items)
- audio: audio track present (mean −16 dB) but content NOT VERIFIED. WH transcript `download_failed`, no local Whisper. Likely a music/trending sound; unconfirmed.
- hook (0-3s): the bag drops/swings into frame at 0.2s, then a hand holds it up. A MacBook is slid in at 1–2s. Text: "pov: you found the perfect summer bag that fits your whole life 🤎🍦👜☀️". Hook type: callout/POV + product-reveal
- product first appears: 0.2s (the product itself, dropping into frame)
- personalization shown? no
- proof element: capacity demo (it fits a 15" MacBook, a tablet, a wallet, headphones). No reviews.
- offer: none; CTA wording: none on screen. Ad copy: "Meet our #1 best selling bag - carries up to a 15" macbook…" (no explicit CTA line)
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-0.9 | hook | bag drops/swings into frame | unverified | "pov: you found the perfect summer bag that fits your whole life 🤎🍦👜☀️" (persists entire video) |
| 0.9-2.5 | demo | hand holds up a MacBook and slides it into the bag | unverified | same |
| 2.5-8.5 | demo | teal tablet/book, then iPad, wallet/clutch, small item in the front pocket, headphones go in | unverified | same |
| 8.5-9.5 | CTA/end | bag lifted out of frame (loop point) | unverified | same |

- transcript: none available (WH download_failed)

### Roha Home — No-drill suction hooks (ad 646767257902957)
- category: home
- days_active: 485 (2025-05-27 → 2026-09-24); landing: https://roha-home.com/products/no-drill-aesthetic-hooks; price: $39.99
- length: 36.5s; cuts: 7 (≈0.19 cuts/sec); format: demo (silent ASMR-style hands-only install demo: result → unboxing → installs → result)
- audio: none. The audio track is silent (mean −91 dB). The WH transcript "you you" is a Whisper hallucination on silence. No on-screen text in any sampled frame.
- hook (0-3s): a black round hook is already fixed on a dark kitchen cabinet, and a hand hangs a checkered designer handbag on it. No text or sound. Hook type: product-reveal (result-first)
- product first appears: 0.3s (installed on a cabinet). Packaging ("ROHA HOME" kraft box) at 4s.
- personalization shown? no
- proof element: load demo (a handbag hangs from the suction hook), shown on several surfaces. No reviews or numbers.
- offer: none in video. Ad copy: "2 + 2 ACTION TODAY… Be quick, stock is limited!" (bundle + scarcity). CTA wording: ad copy "Order now and enjoy a tidy…"; nothing on screen
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-4.5 | hook (result) | handbag hung on black hook on kitchen cabinet | none | none |
| 4.5-10.3 | reveal/unboxing | ROHA HOME kraft box on marble counter; hook taken out | none | none |
| 10.3-17.7 | demo (install) | hands press the suction hook onto the cabinet side | none | none |
| 17.7-22 | demo (result) | installed hook, then a handbag hung on it | none | none |
| 22-27 | demo (2nd surface) | hook pressed onto a low stone/tile wall | none | none |
| 27-31 | demo (3rd surface) | hook pressed onto a green cabinet door | none | none |
| 31-36.5 | result/end | striped tea towel hung on the hook; lights dim at the end | none | none |

- transcript: none (silent; WH returned "you you" = hallucination)

### Wander Prints Unique Gift — "My Hardest Goodbye" custom-photo pet-loss sign / collar frame (ad 7244975012222216)
**VISUALS UNVERIFIED. AUDIO/TRANSCRIPT UNAVAILABLE.** The fb_video has expired (oe=2024-03). The wh_video hash returned 404 on every media.winninghunter.com path tried. WH transcript returned `download_failed` (no credit charged). Everything below comes from metadata only.
- category: personalized gift: memorial (pet)
- days_active: 757 (2024-03-06 → 2026-04-02); landing: https://wanderprints.com/ah590hal1990-fbf; price: $29.95
- length: unknown; cuts: unknown; format: unknown (display_format = video)
- audio: unknown
- hook (0-3s): unknown. Ad-copy hook: "Frame The Memories Of A Lifetime With Our Collar Frame 🌈🐾". Headline/caption: "Memorial Gift For Pet Parents". Hook type: unverifiable
- product first appears: unknown
- personalization shown? unknown (the product is a custom photo + collar frame)
- proof element: unknown
- offer: "Worldwide Shipping!" (ad copy); CTA wording: ad-copy "Order here → [link]"; button "Shop now"
- beats: not mappable (no video)
- transcript: none available

### Statik — Snap-N-Charge magnetic mini power bank (ad 731494416307444)
- category: gadget
- days_active: 426 (2025-07-25 → 2026-09-24); landing: https://statikco.com/products/snap-n-charge-v1; price: $29.99
- length: 38.9s; cuts: 30 (≈0.77 cuts/sec); format: mixed. A parent-testimonial VO (gifting story: bought for her daughter's trip) over fast b-roll demo cuts in travel settings, with a static offer end card. Mostly hands only, one B&W street shot of a young woman.
- audio: VO (adult female, first-person parent testimonial) plus bold word-by-word captions
- hook (0-3s): hands tear open a Statik pouch by a lake, with big googly-eye emoji. The device is shown in a palm, then snapped onto a phone. VO: "Don't let your kids go on vacation without one of these." Captions: "DON'T LET… VACATION… ONE OF THESE!" Hook type: callout (to parents) / problem
- product first appears: 0.3s (packaging being torn open); device in hand at 1s
- personalization shown? no
- proof element: testimonial ("she said it's the best gift she ever got") + multi-device demo (iPhone, Android, MacBook, headphones). No reviews or numbers shown.
- offer: "50% OFF" end card; spoken "save up to $209 with a 5-pack today"; ad copy "Enjoy our discount right now!" CTA wording: spoken "Grab your Snap N Charge…"; end card "KEEP GOING, KEEP CHARGING! 50% OFF CLICK THE LINK"
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-2.4 | hook | Statik pouch torn open by a lake; device in palm; clipped to a phone on a forest trail; 👀 emoji | "Don't let your kids go on vacation without one of these." | "DON'T LET" / "VACATION" / "ONE OF THESE!" |
| 2.4-8.7 | reveal/demo | device snapped to a phone, then shown on iPhone, MacBook, headphones and Android at the beach and in a field | "This is the Snap N Charge… small magnetic power bank… iPhone or an Android." | "SNAP-N-CHARGE" / "IT'S A SMALL" / "POWER BANK" / "YOUR PHONE" / "OR AN" |
| 8.7-14.4 | problem/story | phone at a ruin; B&W shot of a dead-battery phone | "Since my daughter was going on vacation… nervous about her phone dying… strange city." | "I WAS REALLY" / "CITY." |
| 14.4-17.8 | story (gift) | device on a keyboard/desk | "I got her a 3-pack… best gift she ever got." | "GIFT" |
| 17.8-26.8 | proof/benefit | B&W young woman crossing a street with a taxi, 😰 emoji; beach photo-taking; device on an iPhone | "…call an Uber at night… take all the photos and videos… without worrying…" | "AND GET BACK" / "ALL THE PHOTOS" / "PHONE DYING." |
| 26.8-31.9 | emotional payoff | two phones on a picnic blanket | "I was so relieved to get texts from her… have fun and stay safe…" | "AND I'M GLAD" |
| 31.9-34 | CTA | device on a phone on a park path | "Grab your Snap N Charge and save up to $209 with a 5-pack today." | "GRAB YOUR SNAP" |
| 34-38.9 | offer | end card with 3 Statik packs over mountains | — | "KEEP GOING, KEEP CHARGING! 50% OFF CLICK THE LINK STATIK" |

- transcript: "Don't let your kids go on vacation without one of these. This is the Snap N Charge. It's a small magnetic power bank that keeps your phone charged up, whether you have an iPhone or an Android. Since my daughter was going on vacation with her friends, I was really nervous…"
