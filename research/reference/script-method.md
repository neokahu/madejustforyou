# Script method: Meta video ads for personalized gifts

**Status:** source of truth for writing ad scripts. Written 2026-09-26.
**Scope:** what goes in the script (beats, timing, text, audio, casting, product-on-screen). How to *prompt* each shot is covered in `seedance-prompt-method.md` and `image-prompt-method.md`. This doc does not repeat them.
**Built from:** `research/sprints/2026-09-script-method/` (four reports plus `raw/`), and our own tests of 2026-09-26.

---

## 0. Read this first: how much to trust the evidence

| Code | Source | n | Longevity verified? | Weight |
|---|---|---|---|---|
| **NW** | `niche-winners.md`: grandparent-to-grandchild keepsake ads (A Wavao baseball, B Cherish These bracelet, C Ziella bracelet) | 3 | **Partly.** A was verified in the Meta Ad Library (page and product link still active since Mar 2025). For B, only the page's longevity was verified. C was not confirmed. | Closest to our niche, but small. **None of the 3 is a blanket.** |
| **GW** | `general-winners.md`: 8 gift and 8 non-gift ads, beat-mapped | 16 | **No.** "Days live" comes from WinningHunter only. | Directional. Use it to spot patterns, not to prove them. |
| **PF** | `published-frameworks.md`: Meta, Google ABCD, TikTok, IPA, Motion | — | n/a | Graded A/B/C there. ABCD and TikTok evidence is A-grade on its own platform but only directional for Meta. |
| **AUD** | `existing-docs-audit.md`: Macorner candle winner (122d), Macorner visor (333d), and our `motion_qa` measurements | 1–2 | Partly | The motion benchmark is **n=1**. |
| **OWN** | Our own tests (Test C/D/E/F, D2–D7), 2026-09-26 | — | n/a | These are measured facts about *production*. They are not about ad performance. |

> ⚠️ **WinningHunter's "days live" (lastSeen − started) is unreliable.** Two ads it listed at 350+ days actually ran for **11 hours** (Soulteelife blanket) and **3 days** (AlmaGems blanket), according to the Meta Ad Library. Those were the only two *blanket* candidates, and both were rejected. The NW set was checked against the Ad Library. The GW set mostly was not. So GW counts are "patterns in ads WinningHunter *thinks* ran a long time". **Before calling any ad a winner, check "Started running on" in the Ad Library.**

A further limit applies to all of the above: we only see ads that survived. Structures that failed are invisible to us, and long-running is a proxy for profitable, not proof of it. **No source tests a story-film ad.** The GW sample contains 0 of them, and NW contains 0.

**Strength labels**
- **STRONG**: two or more independent sources agree (for example, winners plus an A-grade platform source).
- **MODERATE**: one solid source, or several weak ones pointing the same way.
- **WEAK/OPINION**: n≤2, practitioner opinion, or a house hypothesis.
- **HARD**: a production or policy correctness rule. Breaking it ships a wrong or rejected ad regardless of performance.

---

## 1. The rules

### 1a. Hook and product

| # | Rule | Evidence | Strength |
|---|---|---|---|
| **R1** | **The personalized product is on screen by 1s.** Frame 1 shows the gift, not a room, a face or a logo. | NW **3/3** at 0s. GW gift **8/8** ≤1s (median 0.15s), all ads 14/16. AUD candle winner: lampshade ECU, 5 names legible in <1s. PF: Meta "product in the first few seconds" [A], ABCD "brand in the first 5s" [A], TikTok product-on-screen +65% affinity [A]. Our approved §05 rule: "the gift must be identifiable in 3s". | **STRONG** |
| **R2** | **The personalization is the hero visual.** The name, photo or letter is legible and fills the frame for a large share of the runtime. | NW 3/3: the letter fills the frame for ~10/14s (A), ~14/31s (B) and ~32/56s (C). GW 7/8 gift ads have legible names, photos or dates. AUD E3 (Macorner, Wander Prints: "the personalization IS the ad"). | **STRONG** |
| **R3** | **The opening overlay speaks to the buyer about the recipient's reaction, in the third person.** Example: "Your granddaughter won't be able to hold back the tears when she gets this." | NW 3/3 open with a buyer-facing overlay. 2/3 use that exact tears line; the third is a superlative. GW: testimonial captions in 2/8 gift ads. | **MODERATE** |
| **R4** | **The opening shot moves.** No static open, no logo card, no slow intro. | PF H2/H3 [A]. OWN testC2 (fixed open) hook3 5.87, fail, vs testC3 (moving open) 14.68, pass. AUD E16. | **MODERATE** (our measurement is n=1 pair) |
| **R5** | **For memorial or sentimental products, the hook can be a feeling line, but the product still appears by 1s.** | GW: 4/8 gift ads open on an emotional moment, vs 0/8 non-gift. All 4 are memorial ads (4/6 memorial). G2 opens on the ring with "This is more than just a ring 🥺" at 0.3s. | **MODERATE** (the memorial skew in the sample may drive it) |

### 1b. Copy, text and policy

| # | Rule | Evidence | Strength |
|---|---|---|---|
| **R6** | **Meta Personal Attributes: describe the character, never the viewer.** Allowed: "Her dog died on Tuesday.", "Grandma hugged this blanket." Not allowed: "Did you lose your dog?", "Are you a new grandma?", "You're over 60…". This applies to overlays, VO and captions. | PF S6 (Meta policy text, including the age example) [A]. NW 3/3 comply: the VO is grandma speaking to the grandchild, and overlays say "your granddaughter… she". OWN rule 2026-09-26. | **HARD** |
| **R7** | **Burned-in captions carry the story with sound off,** kept inside the Reels safe zones. | PF C1/C3 [A]; +39% CTR from safe zones [B]. GW 5/8 gift ads are text-led. AUD E4 (candle winner = subtitled micro-story). | **STRONG** |
| **R8** | **End with a short on-screen text CTA using a create/customize verb, ideally with "today" or "now". The button is Shop Now.** | NW 3/3 end on a text CTA. GW: 3 of the 4 gift CTAs use create/customize, and 7/8 of all in-video CTAs use today/now. Button: Shop Now in 9 of 12 known. PF CTA1 [A/B]. AUD E12. | **MODERATE** |
| **R9** | **Offer and proof are optional in the video.** Put the offer in the primary text by default. | GW: offer in video 3/8 gift, proof 3/8. NW: 1/3 has an offer card. AUD E10: evergreen niche winners carry no in-ad discount. PF E2: offers help short-term [B]. | **WEAK** (the sources disagree; see T6) |

### 1c. Length, pacing, audio

| # | Rule | Evidence | Strength |
|---|---|---|---|
| **R10** | **Default length is 15–25s** for a $20–70 gift. | GW gift median 21.2s, and 6/8 are ≤24s. AUD: candle 19s and visor 17.7s won; MJ4U-111 at 36.6s failed. PF: Meta says ≤15s [A]. **Counter-evidence:** NW B and C run 31s and 56s, with a VO reading the letter. | **MODERATE** (see T2) |
| **R11** | **Vary shot length at about 2–5s per shot. Never use uniform 5s beats. Use hard cuts, not crossfades.** | GW gift median 0.22 cuts/s (~4.5s per shot), max 0.50. **Gift ads cut slower than gadget ads**, so don't copy 0.6–0.8 cuts/s montages. AUD E6: the winner cuts every 2.5s; MJ4U-111 used 5.0s clips with crossfades, scored hook3 3.59 vs 18.05, and `scdet` could not see its cuts at all. PF S1: "more motion, scenes and speed" [A]. | **MODERATE** (the motion benchmark is n=1) |
| **R12** | **The closing frame moves.** No frozen end card: keep the logo small, over a moving shot. | AUD E7: the last 3s of MJ4U-111 measured 0.00–0.01 motion; the winner ends on a spike of 23.08. | **WEAK** (n=1) |
| **R13** | **Music plus captions, with no VO, is the default for short product-hero ads.** | GW 6/8 gift ads have no VO. PF: Reels says build with audio (+15% [B]), so the music bed is required. | **MODERATE** |
| **R14** | **When the product carries a long letter, have a VO read it in the giver's first person** (grandma to grandchild). Let the camera find one line on screen while the VO carries the rest. | NW 2/3 do this, word for word with the same letter. OWN: a viewer cannot read 50 words in 20s (blanket README). | **WEAK–MODERATE.** B and C read the *same* script, so this may be one creative copied (effective n≈1–2). |
| **R15** | **Put the emotional pivot line at ~55–60% of the runtime.** | NW B and C: "I squeezed this bracelet really tight and filled it with my love, hope, wishes and light" lands at 55–60% in both. **Our blanket's printed poem has the same lines** ("I SQUEEZED IT REALLY TIGHT / I FILLED IT WITH MY WISHES / Hope and Love and Light"). | **WEAK** (effective n≈1) |

### 1d. People, casting, story

| # | Rule | Evidence | Strength |
|---|---|---|---|
| **R16** | **People on screen are optional.** Hands plus product is a proven format. | NW **0/3 faces** (hands, box or wrist only). GW 4/8 gift ads show a face, all memorial reactions. AUD C2/C12: no evidenced winner opens on a face. | **MODERATE** |
| **R17** | **If a person is shown, show the connection, not a lonely giftee** (giver and receiver together, or a relationship prop such as a framed photo). | House rule. It fits ABCD "Connection" [A, untested for this]. GW: only 1/8 shows giver and receiver together, and that one is an AI render. | **WEAK/OPINION**, but keep it as a house rule |
| **R18** | **When grandma is the buyer, grandma is alive and present in the ad.** She must see herself in it: her voice, her words, or her on screen. Never let an absence read as a death. | OWN rule, 2026-09-26. NW 3/3: grandma is present through her voice (B, C) or her words (A), and nothing implies she has died. AUD E9: living-legacy, present-tense framing is the proven grandparent default, and memorial is a separate variant. | **HARD** (house) / **MODERATE** (evidence) |
| **R19** | **Casting matches the customized figures printed on the product in that shot:** skin tone, hair texture, colour and style. Never write "a young woman". | OWN Test D2: the model cast a white woman against Black printed figures. D4/D5 were fixed by naming the traits. The user confirmed this as a requirement on 2026-09-26. | **HARD** |
| **R20** | **Story-film (Thai style, late reveal) is not the cold default.** Use it only as a test cell against a product-hero control. | No support: 0 story films in GW, 0 in NW. MJ4U-111 failed the motion gate 3 of 4. DEC rates the format MEDIUM. | **MODERATE** (absence of evidence plus one loss) |

### 1e. Production rules the script must plan for

| # | Rule | Evidence | Strength |
|---|---|---|---|
| **R21** | **The product always comes from the real artwork or a still.** The model never draws it. | AUD E19. OWN Test F: model-drawn close-ups deform. Test E: the model invented a stained-glass panel. | **HARD** |
| **R22** | **Long printed text: video works on cloth. For rigid products, a push-in deforms the text, so use a 4K still with a Ken Burns move for text beats.** | OWN D3: the ~50-word poem held in video on the blanket. OWN Test F / `product-text-fidelity-2026.md`: the letterforms on a rigid product drift under push-in, and the Ken Burns still passes. | **HARD** |
| **R23** | **QA printed text by eye across several frames.** `motion_qa.py` cannot read text, and one frame is an anecdote. | OWN D3: "feeling" read as "ceeling" in the last frame. It was a fold occluding the letter; frames 80 and 95 were correct. | **HARD** |
| **R24** | **For a hand near the product face, the simplest correct answer may be no hand.** State the surface to protect ("printed front face stays smooth and unbroken"). | OWN D5a→D6→D7 (blanket). | **HARD** for the blanket, WEAK in general |

---

## 2. Script template (15–25s gift ad, default 20s)

Default format: **product-hero plus subtitled micro-story, with a music bed.** Letter products add a grandma VO (R14).

| Sec | Beat | Visual | On-screen text | VO / music | Product on screen? | Rules |
|---|---|---|---|---|---|---|
| **0–1.5** | Hook | Moving ECU of the personalized product. The name, photo or letter line is legible. Real artwork only. | Buyer-facing, third-person reaction line: "Your granddaughter won't hold back the tears when she gets **this**" | Music starts at frame 1. Letter variant: VO opens "To my [sweetie pie]…" | ✅ **required** | R1 R2 R3 R4 R6 |
| **1.5–4** | Name / letter | Push or rack across the personalization, second angle | Line 2 (what it is: "Her name. Grandma's words.") | music / VO continues | ✅ | R2 R11 |
| **4–8** | Context / connection | Product in use: a cast-matched person, or hands. If grandma is the buyer, she is here (giving, wrapping, together). | 1 short line, character-described | music / VO | ✅ in frame (can be secondary) | R16–R19 |
| **8–12** | Pivot | Camera finds **one** printed line. Cloth: video is fine. Rigid product: Ken Burns on a still. | the pivot line, or none | VO lands the pivot line at ~55–60% (≈11–12s of 20) | ✅ | R14 R15 R22 |
| **12–16** | Payoff | Reaction or relationship: giver and receiver together, recipient holding it. Or a scale/hero shot. | optional payoff line | music swell | ✅ | R17 R18 |
| **16–20** | CTA | Moving hero shot. Small logo over the moving frame. | "Make one for her today" (create/customize verb + today) | music out | ✅ | R8 R12 |

**Shot lengths:** vary them (for example 1.5 / 2.5 / 4 / 3.5 / 4 / 4.5). Use hard cuts. A 5s *generated* clip is trimmed to the beat; the generation length is never the edit length.

**Pre-flight checklist (every script)**
- [ ] The product is visible in frame 1, and in every beat or no more than one beat away.
- [ ] No overlay, VO line or caption asserts anything about the viewer (age, family status, grief, health, money).
- [ ] The grandma buyer is alive and present. The ad is present tense unless it is explicitly a memorial variant.
- [ ] Each person's description names skin tone, hair texture, colour and style to match the printed figures.
- [ ] Text beats on rigid products are marked "STILL + Ken Burns".
- [ ] The QA plan says "read the text across ≥5 frames by eye".
- [ ] The length is 15–25s, no two consecutive shots have the same length, and there are no crossfades.
- [ ] The last 2s move. The CTA is on screen as text.
- [ ] The ad copy is line-broken (see `ad-copy-linebreak-format`) and carries the offer if the video doesn't.

---

## 3. Conflicts to TEST, not argue

Each row is an A/B cell pair: change only the named variable. Judge on the approved §08 metrics (3s hook rate, hold, CTR, cost per add-to-cart), and only on settled days.

| # | Conflict | Side A evidence | Side B evidence | Test |
|---|---|---|---|---|
| **T1** | **Late reveal (Thai film) vs product in the first second** | Product ≤1s: NW 3/3, GW 8/8, PF [A] ×3, candle winner | Late reveal: house style. The IPA/System1 emotion evidence covers long-term brand effects [A/B], not Meta prospecting. MJ4U-111 lost. | Same story and footage. Cell A opens on the product ECU; cell B holds the reveal until ~60%. A cheaper middle option (PF synthesis): a product glimpse at 0–3s with the full reveal late. |
| **T2** | **≤15s vs 20–30s** | Meta ≤15s [A] | GW gift median 21s. NW letter-VO ads run 31s and 56s. | Cut a 15s version from the same 20–25s master. |
| **T3** | **Faceless product close-up vs face-driven story** (includes the **granddaughter-growing-up timelapse**) | NW 0/3 faces. Candle winner has no face. Cheap to make. | GW 4/8 have faces or reactions (memorial). ABCD Connection [A]. House rule R17. | Control: hands + product + letter + grandma VO (the NW pattern, near-zero cost). Challenger: the face-driven story with the product still in frame from 0s. |
| **T4** | **VO vs captions only** | Captions: GW 6/8 no VO, PF sound-off [A] | VO: NW 2/3 (letter read aloud), Reels audio +15% [B] | Same cut: grandma VO plus captions vs music plus captions. Most relevant to letter products (the blanket). |
| **T5** | **Personalization process shown vs result only** | Process: GW 4/8 (a personalizer screen recording, photo→product) | Result only: GW 4/8, NW 3/3 | Add a 2–3s personalizer screen-recording beat vs none. |
| **T6** | **Offer in the video vs emotion only** | Offer: GW 3/8, NW C, Motion [B], Google/Nielsen CTA +2.6pp [B] | Emotion only: AUD E10 niche evergreen winners | Same cut ± a final offer card. |
| **T7** | **Phone-UGC hands vs polished AI film** | NW 3/3 are low-cost handheld phone footage | GW: AI-render look didn't prevent longevity (2/8) | Same script both ways, if we can get a physical sample. |

---

## 4. What this changes in our current scripts

### 4a. `marketing/facebook-ads/PHASE1-SUNCATCHER-shooting-scripts.md`

| Where | Problem | Rule | Edit |
|---|---|---|---|
| **HOOK-2** ("opens on the EMPTY WINDOW, product not visible") | No product for the first 2s. In Body A the panel then doesn't appear until A-3 at 6s, so there's no product for 6s. | R1 | Hang the panel in the window from frame 1, softly in focus, and keep the caption "We still leave the window open for him." The hook pair then tests **caption angle only**, which is its stated job. The product-timing question belongs in T1 as a separate cell, not inside the hook test. |
| **Body C** (C-2, C-3: the giver hears the news, can't decide) | The panel is visible at 0–2s (HOOK-1 only) and then absent until C-4 at 11s. With HOOK-2, it never appears before 11s. | R1 | Keep the product in C-2/C-3: the product page on her phone (C-2 already has a phone-screen composite), or the panel in the owner's window as a cutaway. |
| **Body B-3** ("sản phẩm lộ ra — held on the face") | The reveal is framed on the face, and the product only arrives at 6s. | R1, R16 | Open B on the product and let the face react to it, rather than holding on the face before the product. |
| **Beat sheet** "5s-native", with A-3/A-4/B-3/B-4/C-3/C-4 all at 5.0s | Uniform 5s shots are the MJ4U-111 flatness cause. | R11 | Keep 5s *generation*. Use the two-shot recipe inside each clip and trim each beat to a different length, for example 0–1.5 / 1.5–4 / 4–7.5 / 7.5–11 / 11–15.5 / 15.5–20. |
| **"Reveal still lands at ~30–55% — mid-film, per §05"** | Restates the late-reveal rule. | R1, AUD C15 | Change to "gift identifiable at 0–1s; name/breed *payoff* (the name in the shadow) at mid-film". |
| **Assembly** (not specified; the AFS editor role defaults to crossfades) | Crossfades are invisible to scdet and read as flat. | R11 | Add to the build plan: hard cuts only. |
| **SHARED-CLOSE** "end card: *Make one that's only theirs* + logo" | Risk of a frozen end card. | R12 | Put the text and a small logo over the moving panel shot. No static card. |
| **CTA** "Make one that's only theirs" | Good create verb, but no "today". | R8 | Optional variant: "Make his today". Low priority. |
| Captions such as "Her dog died on Tuesday." | ✅ Character-described, so policy-safe. | R6 | Keep. |

### 4b. Granddaughter blanket (`products/blanket-granddaughter/`, MJ4U-012)

| Issue | Rule | Change |
|---|---|---|
| **No verified long-running blanket video exists** in this niche. Both blanket "winners" ran 11 hours and 3 days. | §0 | Treat every blanket video script as a test. Build the **cheap NW-pattern control first**: hands unfold the blanket at 0s, the camera finds the poem, grandma's VO reads it, and the tears overlay runs on top. |
| **The poem is the NW letter** ("squeezed it really tight… wishes… Hope and Love and Light") | R14 R15 | The VO reads the poem in grandma's voice. Land "SO WHEN YOU'RE FEELING LOW / JUST HOLD IT REALLY TIGHT" at ~55–60%. On screen, show only that one line legibly. Don't hold a wide shot expecting viewers to read 50 words. |
| **User concept: "granddaughter growing up" timelapse** | R1, R18, R19, R20, T3 | Script it as the **T3 challenger**, not the default. Fixes: (1) **the blanket is in frame in every age shot from 0s**, as the constant through the years; (2) **grandma is alive and present**: she gives it in the first beat, her VO runs throughout, and the last beat shows them under it together (D5c). A timelapse without her reads as her death, and she is the buyer. (3) **Every age is cast to the printed figure** (NICOLE: warm brown skin, curly golden-brown puffs). That needs a turntable per age, and multiple ages multiply the identity-drift risk. (4) Decide the child vs adult question first, because the printed figure is a child. |
| **Hands** | R24 | Use D7 "both hands inside the blanket" for wrapped shots. |
| **Text QA** | R22 R23 | Video is fine on cloth. QA the poem across ≥5 frames by eye. |
| **Policy** | R6 | "Your granddaughter won't hold back the tears when she gets this" ✅. Never "Grandmas, …" or "Are you a grandma?". |

---

## 5. Retire / keep (old docs, per the audit)

| Doc | Verdict | Keep | Drop |
|---|---|---|---|
| `templates/film-script-template.md` | **Rewrite, don't patch.** It is the most dangerous doc because it is a default. | — | Product at ≥60%, face-first open, cool→warm grade, single-shot prompts, generic "no text". Replace with §2 of this doc plus the `seedance-prompt-method.md` shot block. |
| `ai-film-studio.md` | **Retire as a scripting source.** Keep it as a pipeline note. | Turntable gate, real product image, no mechanical hand actions | Product as late payoff, crossfades, uniform 4–5s, logo end card, cool→warm |
| `ai-emotional-video-ad-playbook.md` | **Retire.** | Recipient × emotion table, and the headline formula `[one-liner] – Personalized Gift For [recipient]` (move both to DEC) | Unsourced stats (71–80%, 49%, 4.2×/2.8×, 9-day fatigue), the MJ4U-111 worked example, the old toolchain |
| `video-ad-decomposition-2026.md` | **Keep** as the strategy and angle library, with fixes | Hook library, angles, [DATA]/[OPINION] labels | Add "product-hero ECU + subtitled micro-story" as HIGH. Change "reveal at mid-point" to "identifiable at 0–3s, payoff at mid". Flag 5s/cut as UGC-only. Demote "reaction = #1 proof". |
| `ad-video-director-research.md` | **Keep** §0 measurements and §2–§3 diagnosis | motion_qa benchmark (n=1), hard cuts | §4a "NEG never load-bearing", §4b `[0s][2s]` timecodes (`seedance-prompt-method.md` governs) |
| Testing-plan page §05 worked example | **Fix** | 3s gift-identification rule | "Cận mặt chủ của Max" face-first open, and "~5s per scene" |
| Memory `ad-style-thai-emotional-film` | **Demote** to "test cell / brand use" | — | "Preferred format" |

---

## 6. Open gaps (don't fill them from memory)

- No verified blanket video winner. Next step: manual Ad Library pulls for Macorner, GossbyGift and Wander Prints (video, started before 2026-06).
- No A/B-grade source on video ads for 55+ audiences.
- No transcripts or motion data for the 7 unverified GW gift ads, which include the oldest ones (4 of them ran 590+ days per WinningHunter).
- The motion/pacing benchmark rests on one visor ad. Run `motion_qa.py` on ≥10 Ad-Library-verified winners.
