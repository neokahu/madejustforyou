# General beat maps — batch 2

Method: WinningHunter get_ad_transcript + scan_ad for each ad (raw JSON saved as `general-transcript-<id>.json` / `general-scan-<id>.json`). Video downloaded from the WH media CDN or fbcdn. Cuts come from ffmpeg scene detection (`gt(scene,0.3)`). Frames were sampled at 0-5s every 1s, then every 2.5s, and read from contact sheets. Where WH Whisper could not download the video, I transcribed locally with whisper.cpp (small.en). Advertiser in scan matched the candidate pageName for all 6 ads.

### Macorner Home Decor — personalized couple-caricature men's boxer briefs (ad 1313737580474043)
- category: personalized gift: couple (apparel)
- days_active: 192 (2026-01-14 → 2026-07-25); landing: https://macorner.co/products/f-valentines-day-i-love-you-every-day-gifts-for-him-personalized-mens-boxer-briefs-hus100101tvhn; price: $29.95
- length: 23.8s; cuts: 9 detected (≈0.38 cuts/sec; the sampled frames show 1-2 more soft transitions); format: mixed. UGC-style flat-lays plus a husband's reaction clip, then a screen recording of the product-page personalizer, then a logo end card.
- audio: music only (licensed-sounding country song, "you and me in honky tonk"), no VO. All messaging is on-screen caption text.
- hook (0-3s): 0s shows black boxers flat on a bed with the text "SALE WON'T LAST / CUSTOMIZE YOUR GIFT NOW". By 1s it switches to red boxers with the text "This is NOT the Valentine's gift I planned...but it's the one he can't stop laughing about 😂🔥". Hook type: offer (0s) → testimonial/story caption (1s)
- product first appears: 0s (flat-lay of the actual product)
- personalization shown? yes. The couple caricature and names "VINCENT ♥ SANDRA" are visible from 0s. The customization process is shown at ~14.6-21s as a site screen recording with hair color, hairstyle, "Woman's Bottoms", "Woman's Name" and a "Preview Your Personalization" button.
- proof element: UGC reaction (the husband laughs hard while holding the boxers, ~2.4-5s), a "Quality is pretty good" caption, and a fabric close-up
- offer: "SALE WON'T LAST" (0s); on the product page, "Buy 2+, Save 10% | Code: MSW2" and an add-on card "$3.00 → $1.99". CTA wording: "CUSTOMIZE YOUR GIFT NOW" (on screen); ad-copy "Everyday love, now in boxers 😏❤️" (no explicit CTA line; button SHOP_NOW)
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-1 | hook / offer | black boxers flat-lay on bed | (song) | "SALE WON'T LAST / CUSTOMIZE YOUR GIFT NOW" |
| 1-2.4 | hook / story | red boxers flat-lay | (song) | "This is NOT the Valentine's gift I planned...but it's the one he can't stop laughing about 😂🔥" |
| 2.4-~4.5 | reaction | husband on couch, laughing, holding up red boxers, open gift box on lap | (song) | "I got my husband these custom boxers..." |
| ~5-8.4 | personalization / demo | woman's hand (ring) stroking the caricature print on black boxers | (song) | "customized exactly like us" |
| 8.4-12.6 | proof / demo | thumb pressing the "F♥CK Valentine's Day I LOVE YOU Every day" print | (song) | "Quality is pretty good" |
| 12.6-14.6 | story / angle | same close-up | (song) | "Turns out men don't want luxury... They want something dumb, spicy, and personal. 🤣👌👌" |
| 14.6-~21 | personalization / offer | phone screen recording of the macorner.co product page and personalizer options | (song) | "Buy 2+, Save 10% \| Code: MSW2"; option labels |
| ~22-23.8 | CTA / brand | macorner logo end card | (song) | "macorner.co" |

- transcript (song lyrics only): "Singing you and me in honky tonk The way you slip and let me on on Girl, there ain't a look you can't pull off Nothing turns me on like you In a honky tonk"

### Wrappiness Home Decor — personalized memorial car ornament "Those we love don't go away" (ad 1322858649604648)
- category: personalized gift: memorial (accessory)
- days_active: 210 (2026-01-30 → 2026-08-28); landing: https://www.wrappiness.co/products/those-we-love-beside-us-every-day-personalized-custom-car-ornament; price: $20.99
- length: 23.9s; cuts: 3 (≈0.13 cuts/sec); format: demo / product showcase. It uses slow, glossy footage with sparkle overlays that looks rendered or AI-generated. Only hands appear.
- audio: music only (a Christian/memorial ballad, "The only scars in heaven…"), no VO.
- hook (0-3s): hands hold an open kraft box. Inside, on shredded paper, is a round silver ornament with two jeweled butterflies, "Dad 2019 / Mom 2023" and the rim text "THOSE WE LOVE DON'T GO AWAY / THEY JUST FLY BESIDE US EVERY DAY". Text overlay: "THIS CAR ORNAMENT TRULY TOUCHED MY HEART...". Hook type: testimonial + product-reveal (unboxing)
- product first appears: 0s (in its gift box, in hand)
- personalization shown? The personalized result is shown (names and years on the ornament from 0s). The customization process is not shown: no
- proof element: none beyond a first-person testimonial-style caption
- offer: none in video. CTA wording: none on screen; ad copy "Customize yourss: https://wrappiness.co/wr-9290654515477" (button SHOP_NOW)
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-~4 | hook / reveal | hands tilting an open kraft box with the ornament | (song) | "THIS CAR ORNAMENT TRULY TOUCHED MY HEART..." |
| ~4-6.5 | demo | hand hangs the ornament from a car rear-view mirror, sun flare | (song) | none |
| 6.5-17.4 | demo / emotional | ornament swinging on the mirror in golden-hour light; hands cradle and touch it (~12-15s) | (song) | none |
| 17.4-20.6 | demo | static hanging shot, sunlight | (song) | none |
| 20.6-23.9 | emotional close / CTA-less end | back to the ornament in its box | (song) | "THEY ARE NO LONGER HERE, BUT I BELIEVE THEY ARE ALWAYS WATCHING OVER ME ❤" |

- transcript (song lyrics, local whisper; WH returned only "🎶 Music Outro 🎶"): "The only scars in heaven / That won't belong to me and you / There'll be no such thing as broken / And all the old will be made new / And the thought that makes me smile"

### Personalized Family Gifts (trendingcustom.com) — "Always With You" sky family-members memorial acrylic keychain (ad 1439057843618047)
- **VISUALS UNVERIFIED.** WH Whisper returned `download_failed`. Every video URL (the fbcdn HD/SD URLs expire 2023-10 per `oe=`, plus the WH bare hash under media.winninghunter.com root, /metalibrary/video/ and /video/) failed or 404'd, and the poster thumbnail also 404'd. No transcript and no frames.
- category: personalized gift: memorial (family members and pets; accessory)
- days_active: 295 (2025-10-16 → 2026-08-07); landing: https://trendingcustom.com/products/always-with-you-sky-family-members-grandma-grandpa-dad-mom-kids-dogs-cats-memorial-personalized-acrylic-keychain-1311141; price: unknown (candidate price field "False"; scan shows compare-at $112.99, which is likely a bundle or incorrect)
- length: unknown; cuts: unknown; format: unknown
- audio: unknown
- hook (0-3s): unknown. The ad copy opens "Heartwarming memorial personalized gift". Hook type: unknown
- product first appears: unknown
- personalization shown? unknown
- proof element: unknown
- offer: none in copy. CTA wording: ad copy "Order now ➡️ https://trendingcustom.com/s450786"; button SHOP_NOW
- beats: not mappable (no video)
- transcript: none available
- note: the page has 2,975 active ads, so it is a high-volume catalog seller. The fbcdn asset dates (2023) suggest the creative is older than the WH "started" date.

### Mookly Shop — paint edger roller with built-in shield (ad 1565328561493253)
- category: home (gadget)
- days_active: 407 (2025-08-15 → 2026-09-26); landing: https://mookly-shop.com/products/paint; price: $19.90
- length: 18.0s; cuts: 13 (≈0.72 cuts/sec); format: demo. It is a montage of stitched, re-used demo clips (square 720x720, "Mookly" watermark), with no people speaking.
- audio: music only (upbeat track; WH Whisper failed; local whisper heard only "(upbeat music)").
- hook (0-3s): a man in a face mask runs a yellow edger along the wall-ceiling line (0-1.8s). The edger then runs along a taped corner (1.8-3s), followed by a close-up of a crisp pink paint stripe. No text. Hook type: product-reveal (product in use from frame 1)
- product first appears: 0s (in hand, in use)
- personalization shown? no (not applicable)
- proof element: before/after-style contrast. A grayscale "old way" clip with a red X (~5-6.3s) is followed by clean-line results.
- offer: none in video. CTA wording: none on screen; ad copy "👉 Try it now: https://mookly-shop.com/products/paint" (button LEARN_MORE); copy hook "Tired of messy edges and painter's tape?"
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-1.8 | hook / demo | masked man edging the ceiling line with the yellow tool | (music) | watermark only |
| 1.8-3.0 | demo | edger at the ceiling corner, yellow tape on the wall | (music) | — |
| 3.0-5.2 | demo / result | close-up: edger laying a sharp pink stripe | (music) | — |
| 5.2-6.3 | problem | grayscale clip of a man painting with a long tool, big red X | (music) | red X graphic |
| 6.3-9.7 | demo | edger laying a clean grey band at the ceiling | (music) | — |
| 9.7-12.6 | demo | edging around a smoke detector (green paint) | (music) | — |
| 12.6-16 | demo | gloved hand edging a door frame (blue paint); man painting beside the door | (music) | — |
| 16-18 | result | finished grey wall | (music) | — |

- transcript: none (music only)

### Doggovinci — personalized pet-memorial photo keychain (ad 1612287576582625)
- category: personalized gift: pet (memorial; accessory)
- days_active: 197 (2026-03-12 → 2026-09-25); landing: https://doggovinci.com/products/dog-keychain-dog-memorial-gifts-for-loss-of-dog-personalized-keychains-pet-memorial-gifts-cat-keychain; price: $19.99
- length: 18.0s; cuts: 3 (≈0.17 cuts/sec); format: demo (product close-ups on a sunlit wood table, hands only, narrated)
- audio: VO (narrator, product-feature voiceover; voice gender not verified from frames)
- hook (0-3s): two stainless tag keychains on a wooden table. One has a black Labrador photo and the other is engraved "Once by my side forever in my heart ♥ MAX". A hand reaches in. VO: "Doggovinci's live customization keychains allow you to preview your customized photo…". Hook type: product-reveal
- product first appears: 0s (on table, then in hand)
- personalization shown? The result is shown (pet photo and name "MAX" from 0s). The VO describes the live preview, but the customization process is not shown on screen: no
- proof element: none (feature claims only: stainless steel, laser engraved, protective resin)
- offer: none. CTA wording: none on screen or spoken; ad copy "📸 Upload your pet's photo & name for a live preview!" (button LEARN_MORE)
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-4.2 | hook / reveal | both keychains on a wooden table, hand approaching | "Doggovinci's live customization keychains allow you to preview…" | none |
| 4.2-8.9 | personalization (claim) / demo | hand lifts and dangles the photo keychain | "…your customized photo and custom engraving prior to purchase." | none |
| 8.9-17.3 | demo / quality | macro of the tag edge, then a close-up of the printed dog photo | "Crafted in stainless steel, laser engraved and covered with a protective resin, these special keepsakes are built to last." | none |
| 17.3-18 | end | black frame | — | none |

- transcript: "Dogavinci's live customization keychains allow you to preview your customized photo and custom engraving prior to purchase. Crafted in stainless steel, laser engraved and covered with a protective resin, these special keepsakes are built to last."

### Forge Wallet Accessoires — Forge leather smart wallet with coin pouch (ad 1641337736775455)
- category: accessory (men's wallet; pitched as a gift for husband/brother/father)
- days_active: 635 (2024-12-28 → 2026-09-24); landing: https://forge-wallet.com/products/forge-leather-wallet; price: $48.00
- length: 51.5s; cuts: 0 detected (one continuous POV take in a parked car; any jump-cuts fall below the 0.3 threshold). Format: UGC (first-person POV review, hands only, face never shown).
- audio: VO/talking by an off-camera creator (casual, "Bro…"), no music detected in the transcript
- hook (0-3s): POV from the driver's seat. A hand reaches to the console, picks up the wallet (~1s), and holds it up by 2s. Spoken: "Bro, ditch your old wallet, this one even comes with a coin pouch." Hook type: callout ("Bro") + product-reveal
- product first appears: ~1s (in hand)
- personalization shown? no
- proof element: spoken testimonial ("I get a lot of compliments on this wallet", "my everyday wallet for a long time"), a live demo of the card pop-up, cash room, zipper sound, and unboxing of the Forge box and a second brown variant (~32-45s)
- offer: spoken "They have a huge promotion going on right now" (~22s); ad copy "Get a 50% discount now". CTA wording: spoken "I'll actually drop that link below so that you guys can get your own" / "Forge Wallet is the way to go"; ad copy "Get a 50% discount now: ➡️ https://forge-wallet.com/…" (button SHOP_NOW)
- beats:

| t_start-t_end | beat | on screen | VO/dialogue | on-screen text |
|---|---|---|---|---|
| 0-3.5 | hook | POV in car, hand grabs the wallet from the console and holds it up | "Bro, ditch your old wallet, this one even comes with a coin pouch." | none |
| 3.5-11.7 | demo | pushes the button, cards fan up, opens the cash section, shows the leather back | "So this is the Smart Wallet from Forge. On the inside I have even more room for cards…" | none |
| 11.7-15.6 | proof | handles the wallet | "I get a lot of compliments on this wallet. It has been my everyday wallet for a long time now." | none |
| 15.6-21.8 | demo | button card-eject, zipper coin pocket | "With the push of a button I get all my most important cards… the coin pocket is super helpful." | none |
| 21.8-26 | offer / CTA | card in and out, wallet flipped | "They have a huge promotion going on right now, so I'll actually drop that link below…" | none |
| 26-37 | demo / variants | slim profile, then opens the Forge box showing the brown leather version | "They also have different variations… I got the brown version just because I like the leather." | none |
| 37-43 | gift angle | handling the brown wallet | "This is a perfect gift for a husband, brother, father…" | none |
| 43-51.5 | CTA / close | zipper demo, closes the Forge box, holds it up | "…listen to the zipper. Super clean wallet… Forge Wallet is the way to go." | none |

- transcript: "Bro, ditch your old wallet, this one even comes with a coin pouch. So this is the Smart Wallet from Forge. On the inside I have even more room for cards, lots of room for cash, and then on the back of it is just this super nice leather. I get a lot of compliments"
