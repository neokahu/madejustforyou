# Niche winners: grandparent → grandchild personalized-gift video ads (US Meta)

Pulled 2026-09-26. **The data is thin.** I could beat-map 3 ads, and none of them is a blanket. Read §5 before you use any pattern below.

## 1. Method, credits, filters

- **WinningHunter** `search_facebook_ads`: 17 searches, all with `media_type=videos`, `country=US`, `sort_by=longestrunning`, and mostly `min_days_running` of 90 or 180. Keywords used:
  - "to my granddaughter", "to my grandson", "granddaughter blanket", "grandma blanket", "letter blanket", "never forget that I love you", "hug this blanket"
  - landing URLs containing granddaughter / grandson / blanket / custom-blanket / fleece-blanket
  - landing URLs for wanderprints / macorner / gossby / ohcanvas / personalhouse
  - The search list and rejected candidates are in `raw/niche-summary.md`. Raw responses are in `raw/niche-search-*.json`.
- **Credits:** WinningHunter went from 19,999 to 19,949, so **51 credits** (0.26% of the balance). Firecrawl used about 35 credits for Ad Library checks.
- **`get_ad_transcript` failed** with `download_failed` on all 6 candidates (no charge; results in `raw/niche-transcript-*.json`). As a workaround I downloaded the videos from the CDN URLs in the search data. That worked for 3 of the 6; the other links had expired. I transcribed those 3 locally with faster-whisper small.en (`raw/niche-whisper-local-*.json`) and made a timestamped contact sheet for each (`raw/frames/*_sheet.jpg`). The beat maps below come from those files.
- **Longevity check:** I looked up each ad directly in the Meta Ad Library (firecrawl). This changed the results (see §5.1).

## 2. Winners

| # | Advertiser | Product | Landing URL | Days active | Length | Ad Library | Status |
|---|---|---|---|---|---|---|---|
| A | Wavao | "To My Grandson" engraved baseball | wavao.com/products/to-my-grandson-baseball-never-lose | ~546 per WinningHunter (started 2025-03-27). The Ad Library still shows several Wavao ads to `wavao.com/BQ-0101-TGS` started Mar 27 2025 and **active**. | 14 s | https://www.facebook.com/ads/library/?id=883751713867820 | **Verified long-runner** (at page + product-link level) |
| B | Cherish These | "To My Granddaughter" infinity-heart bracelet + message card | cherishthese.com/products/to-my-granddaughter-love-you-forever-black | ~565 per WinningHunter (started 2025-03-10). 6 ads seen on this URL. The page still runs ads started Oct 20 2024. | 31 s | https://www.facebook.com/ads/library/?id=1024956938851112 | Page longevity verified; this exact ad not confirmed |
| C | Top 5 Gifts / Ziella | Granddaughter graduation bracelet + message card | ziella.shop/products/gdr-b02 | ~751 per WinningHunter (started 2024-09-05). 3 ads seen on this URL. | 56 s | https://www.facebook.com/ads/library/?id=1551779152039730 | Not confirmed. The Ad Library only shows newer ziella.co ads. |
| D | Soulteelife | Granddaughter Christmas **blanket** | soulteelife.com/products/nttd-skub-christmas | WinningHunter says ~356. **Ad Library says it ran 11 hours on Oct 4 2025.** | 16 s | https://www.facebook.com/ads/library/?id=1497368381412077 | **Rejected** (not a long-runner) |
| E | AlmaGems | "To My Granddaughter, Learn To Dance In The Rain" **blanket** | almagems.com/products/to-my-granddaughter-learn-to-dance-in-the-rain-…gdt440_blk | WinningHunter says 352. **Ad Library says Oct 8 – Oct 11 2025 (3 days).** | 19 s | https://www.facebook.com/ads/library/?id=1199289718715686 | **Rejected** |
| F | AlmaGems | "To My Granddaughter, Whenever You Feel Overwhelmed" stuffed bunny | almagems.com/…gdt223_bun | ~252 per WinningHunter | ? | https://www.facebook.com/ads/library/?id=1057017999571572 | Not confirmed; video link expired |

Counting only the ads that survived the check, this is **3 winners, and all 3 are "letter-engraved keepsakes" rather than blankets**. The format is the same idea as the letter blanket (a printed grandparent letter on a physical object). The scripts carry over directly, but a blanket version is not verified.

## 3. Beat maps

### A. Wavao: "To My Grandson" baseball (14 s, music only)
| Beat | Sec | On screen | Sound | On-screen text | Who |
|---|---|---|---|---|---|
| Hook | 0–1 | A hand holds the ball in front of a bookshelf; small title | music | "The Best Gift For Your GrandSon!" | hands only |
| Product/letter | 1.5–5 | Close-up of the engraved letter ("To my grandson… you will never lose, you either win or learn… just go forth and aim for the skies… love you") | music | "The Best Gift For Your GrandSon!" (large) | hands only |
| Nudge | 5.5–9 | Ball turned in the hand | music | "Don't Miss An Opportunity to Tell Her That You Love Him!!" (sic) | hands only |
| CTA | 9.5–12 | Ball in the hand | music | "Get Yours!" | hands only |
| End card | 12.5–14 | Black "View More" card, then Wavao logo | music | "View More / wavao.com" | — |

- The product is on screen from **0 s**. There is no voiceover.
- There is no real emotional pivot; the engraved letter is the whole payload.
- Copy: "⚾ The perfect way to express your everlasting love and encouragement to your grandson. Get yours 👉". CTA button: unknown.

### B. Cherish These: granddaughter bracelet (31 s, VO reads the letter)
| Beat | Sec | On screen | VO | On-screen text | Who |
|---|---|---|---|---|---|
| Hook | 0–3 | A hand opens a black gift box outdoors | "To my beautiful granddaughter." | "your granddaughter won't be able to hold back the tears when she gets **this**" | hands only |
| Reveal | 3.5–7 | Box opens: bracelet and the "To My Beautiful Granddaughter" card | "From the moment I first held you in my arms, I knew that my life would never be the same." | — | hands only |
| Worn | 8–10 | Bracelet on a wrist | (VO continues) | — | wrist only |
| Letter hold | 11–25 | Box held up against a street; the card fills the frame | "…so proud to have you as my granddaughter… **I squeezed this bracelet really tight and filled it with my love, hope, wishes and light.**" | 12–15 s: "this had me in tears 😭❤️" | hands only |
| Close | 24–30 | Box against a house | "…no matter where life takes you, you will always have a piece of my heart with you. I love you forever and always." | — | hands only |
| CTA | 30.5–31.5 | Box closed | — | "Imagine Her Reaction / Shop Now" | hands only |

- The product (the box) is on screen from **0 s**; the bracelet is revealed at **3.5 s**.
- Emotional pivot: the "squeezed this bracelet really tight" line at **~17–24 s**.
- The VO is written as **grandma speaking to the granddaughter**. The on-screen text speaks to the **buyer in the third person** ("your granddaughter… she").

### C. Ziella / Top 5 Gifts: granddaughter graduation bracelet (56 s, same letter)
| Beat | Sec | On screen | VO | On-screen text | Who |
|---|---|---|---|---|---|
| Hook | 0–7 | A hand opens the box and shows the bracelet | "To my beautiful granddaughter…" (slow read) | "Your granddaughter won't be able to hold back the tears when she gets this on graduation day 😭❤️" | hands only |
| Letter | 8–40 | Card close-up fills the frame; karaoke captions follow the VO line by line | Same letter as B, word for word, ending "I love you forever & always." | Karaoke captions of the VO | card only |
| Product | 40–44 | Box on a kitchen counter | — | — | none |
| Meaning | 45–52 | Bracelet worn on a wrist | — | "The heart on the bracelet represents your neverending love for her" | wrist only |
| Offer | 53–56 | White end card with the ziella logo | — | "Free shipping + 40% off this week only" | — |

- The product is on screen from **0 s**.
- Emotional pivot: the "squeezed… really tight" line at **~25–31 s**.
- Copy: "Bring your granddaughter to tears with this 😢 / Your love, worn on her wrist 💕".

## 4. Cross-ad patterns (n = 3 beat-mapped ads)

1. **3 of 3 show the product in the first second.** None of them uses a story or cold open before the product.
2. **3 of 3 make the printed letter the main visual.** The letter or engraving fills the frame for most of the runtime: B about 14 s of 31, C about 32 s of 56, A about 10 s of 14.
3. **3 of 3 open with a buyer-facing text overlay that sets up the recipient's reaction.**
   - 2 of 3 promise tears: "won't be able to hold back the tears when she gets this".
   - The third is a superlative: "The Best Gift For Your GrandSon!"
4. **2 of 3 use a VO that reads the letter aloud in grandma's first person**, and they read **the same text** from two different advertisers. It includes the line "I squeezed this bracelet really tight and filled it with my love, hope, wishes and light", which is the jewelry version of "hugged this soft blanket". The emotional pivot lands on that line at 55–60% of the runtime in both.
5. **3 of 3 show no faces.** They show hands, a box, a wrist, or the object only. **0 of 3 show grandma or the grandchild, and 0 of 3 dramatize a family moment.**
6. **3 of 3 end with a short text CTA:** "Get Yours!", "Imagine Her Reaction / Shop Now", and an offer card. Only C has an offer ("Free shipping + 40% off this week only").
7. **Production is low-cost UGC-style handheld phone footage in 3 of 3.** There are no actors and no AI film.

## 5. Absences, surprises, caveats

1. **WinningHunter "days active" (last seen minus start date) is unreliable.** Both blanket "winners" (D and E) looked like 350+ day runners but actually ran for 11 hours and 3 days in the Ad Library. Check longevity against the Ad Library ("Started running on" / date range) before calling anything a winner. This should become a rule.
2. **No verified long-running grandparent letter-BLANKET video ad was found.**
   - Wanderprints, GossbyGift, Oh Canvas and Personal House returned 0 results as landing URLs in WinningHunter.
   - Macorner's long-running blankets are daughter-themed and "God says you are", not grandparent gifts.
   - One unverified lead: letsgiveitawhirl, "Grandma, hug this blanket and think of me!" (id 856753577309047, started 2025-12-07).
   - Either blankets in this niche are sold mainly with static or carousel ads, or they run on pages WinningHunter doesn't index.
   - Next step: look up Ad Library pages for Macorner, GossbyGift and Wanderprints manually, with media=video and "Started running" before 2026-06.
3. **Is grandma alive or present?** She is never on screen. Her presence is only her *voice* (B, C) or her *words* (A). Nothing implies she has died.
4. **Point of view:** the VO is first-person (grandma to grandchild). The overlays talk about "your granddaughter… she", which is a third-person recipient. **No ad addresses the viewer's own hardship.** "You will always have a piece of my heart" is inside the product letter, not aimed at the viewer. That is the safe pattern under the Meta Personal Attributes policy.
5. **This contradicts our house style.** Our house style is a Thai-style emotional short film that shows family connection, with the product as a late payoff. Every verified winner does the opposite: the product appears at 0 s, the letter is the hero, and there are no people. That doesn't prove the film format loses, since no competitor is running it, so there is no evidence either way. It does mean the proven baseline to beat is "hands + box + letter + grandma-voice VO", which costs almost nothing to produce.
6. **Sample limits:**
   - n = 3, and all 3 are jewelry or keepsakes.
   - I have no CTA-button data for A–C.
   - Whisper small.en transcripts may have minor wording errors.
   - Frames were sampled every 1–2.5 s, so exact cut points are within ±1 s.
