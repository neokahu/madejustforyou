# Video Ad Decomposition & Phase-1 Test Plan (Meta DTC/ecom, 2026)

> 📄 **Google Doc mirror:** https://docs.google.com/document/d/1obX8brgMHnwmV1c4rpeZLkmC-ww7NXA-NC99hO84kaQ/edit
> *(the Markdown file in this repo is the source of truth; re-import after edits)*
>
> 🇻🇳 **Bản tiếng Việt:** https://docs.google.com/document/d/1rCt4W2x1f72tYpHIgHyXV-82xNveBTrX4i8RIEJAp70/edit

Research 2026-09-13. Purpose: break a short-form ecom video ad into testable parts, rank them for Phase-1
(engagement), and decide **how many video scenarios to test per product.** Feeds Group A (creative) + the
creative operating model in `TESTING-MATRIX-FRAMEWORK.md`. **[DATA]** = measured; **[OPINION]** = credible consensus.

## Decomposition — derived from sources (two lenses reconcile)
Every serious source uses one or both of these, and they fit together:
- **Timeline spine (what plays, in order):** **Hook → Body (Story + Proof) → CTA.** (Sovran, Barry Hott, Meta.)
  Hott's timing: first 3s = attention · next ~10s = proof · last ~5s = action.
- **Modular knobs (what you actually swap to test):** how the analytics tools tag every ad — **Motion**
  (Hook · Messaging/Angle · Visual/Format · Persona) and **creads.io** 6 dimensions (Hook · Concept/Angle ·
  Emotional resonance · Psychological bias · Wording · Visual composition).

**The components that RECUR across all sources (the real decomposition):**
1. **Hook** (0.5–3s: visual + on-screen text + optional VO/sound)
2. **Concept / Angle / Persona** (the core idea + awareness stage it targets)
3. **Body / Retention** ("Story + Proof" — the persuasion mechanism)
4. **Offer** ("the offer is the hook")
5. **CTA / close**
6. **Format / production style** (UGC · lifestyle · high-production; skit/listicle/founder/testimonial/demo)
7. **Cross-cutting craft:** captions/on-screen text (sound-off), pacing/cut-frequency, music/sound

> Sources agree on substance, differ only on granularity: structural people say Hook/Story-Proof/CTA;
> analytics people add Angle/Format/Offer as separate test knobs. Timeline = Hook→Body→CTA; test knobs =
> Hook/Angle/Format/Offer/Body/CTA.

## Per-component table
| Component | Drives | Sub-types / framework | Benchmark / data | How to test | Source |
|---|---|---|---|---|---|
| **Hook** (0.5–3s) | **Hook rate** — the gate for everything downstream | tactics: curiosity gap · contrarian · specific stat · transformation/before-after · question · callout · social proof · pattern-interrupt · face+eye-contact POV. Meta's 3: value-promise · curiosity/teaser · shock/stat | **[DATA]** good 25–35%, 30%+ scalable, 40%+ elite, <20% rebuild (AdLibrary/Triple Whale/hawky converge). Levers: payoff in frame 1 (+5–12pt), motion in first 0.5s (+3–8), text by 0.5s (+4–9), native 9:16 (+5–15) | **OFAT** — same body, N openers. **≥3 openers/concept min**; velocity mode 10–20 hooks/winning angle | motionapp.com/blog/best-dtc-meta-ad-hooks-2025 · adlibrary.com/posts/hook-rate |
| **Concept / Angle / Persona** | hook + hold + CTR + CPA (it's the whole idea) | match awareness stage (unaware→curiosity/transformation; problem-aware→empathy; solution-aware→proof; product-aware→offer) | **[DATA-ish]** 4+ distinct angles → **30–50% longer creative lifespan** before fatigue (creads.io) | **whole diverse concepts, NOT OFAT.** Tag each by angle so winners are legible | creads.io/ad-creative-performance-guide · help.motionapp.com AI-tagging |
| **Body / Retention** ("Story+Proof") | **Hold rate** (15s÷3s), avg watch, ThruPlay | PAS · AIDA · BAB · Problem-Solution-Proof; devices: demo, testimonial, before/after, fast cuts, open loops, listicle | **[DATA]** good hold **40–50%** (Motion); healthy 30–40%; <25–35% w/ strong hook = "bait-and-switch" | fix middle 5–15s **without touching opener** when hook OK/hold low; test proof type | adlibrary.com/posts/hold-rate · sovran.ai |
| **Offer** | CTR, CPA, CVR | BOGO/gift · risk-free · guarantee · discount; make it visible in-frame | **[OPINION]** rebuild the offer before the ad (Hott) | test as a messaging variation | LinkedIn (Elefante-Smith on Hott) · Motion offer tag |
| **CTA** | **outbound/link CTR**, CVR | explicit next step · urgency/scarcity · restate offer; front-load (many act before end) | **[DATA-ish]** Meta: "high hook+watch, low click → obsess over CTA" | **OFAT** — same ad, swap CTA/end-card | help.motionapp.com metrics · facebook.com/business/help/188534925073536 |
| **Format / production style** | hook + hold + lifespan | **For personalized-gift POD, use the fit-rated list below** (reveal · gift-reaction · occasion · POV-giving · testimonial · UGC = HIGH). ⚠️ **founder-story = LOW, podcast = SKIP** (generic-DTC, wrong for a gift store). | **[DATA]** native/UGC beats polished on Reels/Stories; repurposing winning *message* into new *formats* = #1 diversity play post-Andromeda | test whole new formats of a proven angle (diversity) | see POD-tailored section below |
| **Captions / sound-off** (cross-cut) | hook + hold | on-screen text by 0.5s; captions | **[DATA]** ~**80–85% of plays are sound-off** (Meta); captions ↑ view time ~12% | always present; test overlay wording as a hook variant | facebook.com/business |
| **Pacing / transitions / length** (cross-cut) | hold | cut frequency, transition style, length | **[DATA]** Meta: **6–15s** best in Feed/Stories; cuts every 1–2s short-form. **[OPINION] Cut-rate is format-specific, not one number:** ~**1.5s/cut** for fast persuasion formats · ~**5s/cut** for UGC/authenticity (fast cutting reads as *produced* and kills the native feel) · beat-matched cuts for unboxing/reaction · progress-paced for BTS | test length + first-0.5s trim (+2–5pt hook); **brief the cut-rate, don't leave it to the editor** | facebook.com/business/help/188534925073536 · VN script-framework table (see brief template below) |
| **Voice / VO & sound** (cross-cut) | hook + hold (and *believability*) | who speaks (real human vs AI vs none) · tone arc · music bed · SFX/ASMR | **[DATA]** 80–85% sound-off means voice can't carry the ad — but it decides the 15–20% who *do* hear it, and it's the whole mechanism for text-heavy products that can't do a visual reveal. **[OPINION]** prescribe per format: reaction/unboxing = warm bed + genuine emotion · UGC = natural phone voice · compare = analytical + dynamic SFX · BTS = sincere confiding + real ASMR · sentiment-build = **real human VO, never synthetic** | brief it as a field; only test it as an axis when the concept is VO-led | VN script-framework table · our POD proof ranking |

## Phase-1 priority (engagement: hook rate, hold rate, CTR)
Test in this order:
1. **Hook — dominant, test first & most.**
2. **Concept/Angle** — a weak angle caps the hook (validate hooks within a small angle set).
3. **Body/Retention** (hold) — optimize only once a hook clears the bar.
4. **CTA/Offer** (CTR) — last for engagement; matters more Phase-2.

**Hook dominance — the evidence:**
- **[DATA] Meta + Nielsen: up to 47% of a video campaign's value is delivered in the first 3 seconds**; 65% who watch 3s reach 10s, 45% reach 30s → the first 3s gates the whole watch. (facebook.com/business/news/updated-features-for-video-ads)
- **[DATA]** creatives alive past day 21 "almost universally hit 30%+ hook at launch; ones dead by day 7 launched at 15–20%" (AdLibrary saved-ads dataset).
- **[DATA]** hook is the highest-variance element: "same body cut 3 ways → 18% to 38%" (AdLibrary). That's *why* everyone tests hooks most.
- **[DATA] Google/YouTube: creative ≈ 50% of ROI.**

**Hook × Hold 2×2 diagnostic (route your effort):**
- low hook / low hold → wrong concept, replace.
- **high hook / low hold** → fix the body only.
- **low hook / high hold** → highest ROI: rebuild only the first ~1.5s (metric jumps 10–15pt).
- high hook / high hold → scale.

## How many scenarios to test for ONE product
**2026 consensus = HYBRID (Andromeda-era):** *diverse whole concepts to DISCOVER a winner; OFAT hook-swaps to
OPTIMIZE/scale it.* Pure micro-OFAT as your discovery method is outdated (small hook edits "don't move the
needle" — Meta VP Matt Steiner via Caleb Kruse). Andromeda rewards **diversity + volume.**

**Recommended first Phase-1 batch for one POD/gift product:**
- **3–4 distinct concepts/angles** (e.g. recipient personas: grandparent vs couple vs pet; or emotional angles) — the "big swings."
- **× 3 hooks each** (e.g. visual/pattern-interrupt · problem/emotion · curiosity/callout) → **≈ 9–12 ads** first batch.
- **Structure:** 3–5 creatives per ad set (so each exits learning); **~$20–40 per concept** minimum before judging (Motion needs ≥$50/ad to score); **settled-day metrics only.**
- **Judge Phase-1 on:** hook rate (25–35%+), hold rate (40–50%), link CTR → route via the hook×hold 2×2.
- **After a winner emerges (velocity mode):** **10–20 hook swaps** on the winning body + **repurpose the message into 2–3 new formats**; **refresh every ~2–3 weeks** (Andromeda fatigue is faster).

**Reference numbers (media-buyer consensus):**
| Item | Number | Source |
|---|---|---|
| Concepts per discovery round | 8–12 concepts, 2–3 variations each, refresh 2–3 wks | Segwise (growwithsakib.com) |
| Creatives per ad set | 3–5 (20+ usually counterproductive) | AdManage.ai |
| Creative "OS" | 3 angles × 3 formats; 6–9 concepts/week | Salman Munir |
| Hook sprint | 6–8 hooks / offer, different angles, 48h | Salman Munir |
| Hooks per winning angle (velocity) | 10–20 swaps on the winning body | Koro / Savannah Sanchez |
| New vs iteration split | ~90% net-new / ~10% iteration; 2–4 variations/test; "bigger swings" | Dara Denney |
| Account creative volume | ~50–100 ad variations/month; expect ~4× more creative in 2026 vs 2024 | Caleb Kruse (relaying Meta VP) |
| Winner hit-rate (expectation) | ~1–3 winners per 10 creatives | AdManage.ai |

## 🎁 Personalized-gift POD tailoring (format fit + angle library + hooks)
*Research 2026-09-13, fallback ladder: EXACT (personalized POD) → WIDER (general POD/merch) → LAST-RESORT
(generic DTC, flagged). **Honesty: no public ad-PERFORMANCE dataset exists for personalized-gift video ads** —
the EXACT rung is qualitative (Etsy strategy, live brand positioning, TikTok gift-reaction culture); all hard
numbers are POD-wide/general-DTC, directional only.*

### Format fit (rated for a personalized-gift store)
| Format | Fit | Why | Rung |
|---|---|---|---|
| **Personalization/customization reveal** (blank → name/photo appears) | **HIGH** | the customization *is* the product; "personalization sells best when seen" | near-EXACT |
| **Gift-reaction** (recipient opening/reacting) | **HIGH** | the emotional payoff of the category; travels organically | EXACT-ish |
| **Occasion / seasonal montage** (order-by-date) | **HIGH** | gifting is deadline-driven; urgency is the trigger | EXACT |
| **POV: you're giving the gift** | **HIGH** | casts the buyer as the hero giver | WIDER/EXACT |
| **Testimonial / review** | **HIGH** | kills "will it look cheap?" POD skepticism | WIDER |
| **UGC-raw** ("I ordered this for my mom…") | **HIGH** | native, cheap, remixable | WIDER |
| **Hyper-personalization flex** (handwriting · kid's drawing · paw print · recipe) | **HIGH** | beats generic name-drop competitors; fastest-growing Etsy behavior | EXACT |
| **Unboxing / "look what I got"** | **MED-HIGH** | shows real print/material quality | WIDER/EXACT |
| **Listicle** ("5 gifts that'll make grandma cry") | **MEDIUM** | scannable curiosity; warms cold audiences | WIDER |
| **High-production emotional short film** | **MEDIUM** | story-with-late-payoff wins at brand level but costly/risky — sparingly | EXACT |
| **Screen-record of the personalizer** | **MEDIUM** | answers "will it really say MY name?" — better for retargeting than cold | WIDER |
| **BTS / how-it's-made** (production → boxing → shipping) | **MEDIUM** | answers the category's #1 objection ("will it look cheap?") with real craft + ASMR. ⚠️ but craft close-ups are our **lowest-emotion proof (rank #5)** → **Stage-2 / retargeting asset, not a cold Phase-1 concept** | WIDER |
| **Lifestyle / skit / demo** | **MED-LOW** | connective tissue / scroll-stop, but a static keepsake has little to "demo" | WIDER |
| **Founder-story** | **LOW** | ⚠️ generic-DTC; a gift buyer cares about the *recipient's* emotion, not your origin story | LAST-RESORT |
| **Podcast format** | **SKIP** | ⚠️ generic-DTC/info-product; no fit for an impulse, emotion-led gift | LAST-RESORT |

### Angle library (12, tailored) — same product, different pitch
1. **"Made just for them" — personalization reveal** *(any recipient; the customization is the value)* — near-EXACT.
2. **Tear-jerk gift reaction** *(mom/grandma/partner; the gratitude payoff)* — EXACT-ish.
3. **"She'll know you actually thought about her" (feel truly seen)** *(mom/grandparent/spouse)* — EXACT (Etsy thesis).
4. **Occasion urgency / "order by [date]"** *(Mother's/Father's Day, Christmas, anniversary)* — EXACT.
5. **Memorial / keepsake ("keep them close")** *(pet-loss, in-memory)* — EXACT (highest emotional intensity).
6. **POV: you're the one giving it** *(couples, adult kids → parents)* — WIDER/EXACT.
7. **Hyper-personalization flex** *(handwriting / kid's drawing / paw print / recipe)* — EXACT.
8. **Quality-proof unboxing ("the quality shocked me")** *(cold skeptics)* — WIDER.
9. **Relationship-specific callout ("for the grandma who has everything")** *(niche recipient)* — WIDER.
10. **Emotional mini-film, product as late payoff (Thai-ad style)** *(family/mom; higher production/risk)* — EXACT-adjacent.
11. **Gift-for-yourself / self-gifting** *(the scroller herself; underused permission angle)* — WIDER.
12. **Listicle "gifts that'll make them cry"** *(gift-guide/seasonal shoppers)* — WIDER.

### Hook library (concrete first-3s: on-screen text + opening shot)
- **Reveal:** "Watch what happens when you add her name…" (blank mug → grandkids' names bloom) · "Same shirt. Totally different when it's *their* names." (split-screen generic vs personalized).
- **Gift-reaction:** "POV: she opens the one gift she didn't expect to cry over." · "Grandpa went quiet for 10 seconds. Then this." (hold on his face).
- **Feel seen:** "She has everything. So I gave her something no one else could." · "This isn't a gift. It's proof you paid attention."
- **Occasion urgency:** "Mother's Day is in 9 days. This is made-to-order — don't wait." (countdown over personalization).
- **Memorial:** "He's still on the tree every Christmas." (hanging a pet-memorial ornament w/ paw print).
- **POV giving:** "POV: you finally found the gift that makes *you* the favorite child." · "Watch her face — I'll wait."
- **Hyper-personalization:** "Anyone can put her name on it. We put her grandkid's actual drawing on it." · "That's not a font. That's your dad's real handwriting."
- **Quality-proof:** "I was scared it'd look cheap. Then I opened it." · "Custom usually means flimsy. Not this."
- **Relationship callout:** "For the grandma who says 'don't get me anything.'" · "If you're a dog mom, this one's gonna get you."

### Body / Retention — tailored (a gift ad is NOT a problem→solution ad)
PAS/AIDA engage rational System-2 (only fires for active shoppers). Emotional creative is ~2× more effective
long-term (Binet & Field/IPA) and positive-emotion ads show ~6× action lift (System1) `[LAST-RESORT — all-category
data, but argues for an emotion arc over PAS]`. So the gift-ad engine = **anticipation → escalation → payoff
(reveal + reaction).** The recipient's emotion is the arc; the product is the plot device that triggers it.
The category is built on the **reaction moment** (brands literally hire creators for "genuine reaction, tears to
joy") `[EXACT — creator briefs]`.

**Proof ranking for a personalized gift (what counts as proof here):**
1. **Recipient's genuine reaction** (tears/gasp) — the #1 proof; it proves the emotional impact that *is* the product. `[EXACT]`
2. **The personalization detail shown legibly** (their actual name/photo/date) — previews the buyer's own outcome; the name is the strongest attention trigger. `[WIDER]`
3. **Volume/longevity proof** ("10,000+ sold") — for cold traffic needing legitimacy (Etsy: CVR 1–2% at <10 reviews → 10–15% at 500+). `[WIDER]`
4. **Print/quality photo-UGC reviews** — kills "will it look cheap?". `[WIDER]`
5. **Craft close-ups** (engraving/canvas/warmer glow) — lowest emotion, closes quality doubt. `[WIDER]`
> Cold → lead with legitimacy (volume/reviews); warm/retarget → lead with objection-specific proof (quality, delivery).

**Beat-by-beat body skeletons (15–30s):**
- **A · Reaction-led (cold, UGC):** 0–2s reaction cold-open ("She didn't expect this") → 2–6s context (who/occasion) → 6–12s **reveal** (names legible, hold) → 12–20s reaction completes (hug, family in frame) → 20–27s proof+offer ("10,000+ · free personalization · order by [date]") → 27–30s CTA.
- **B · Sentiment build (warm, Thai-ad):** 0–3s hook = the *relationship/stakes* (not product) → 3–10s build (giver ordering it, product teased) → 10–16s reveal + reaction → 16–24s sentiment escalation (personalization line said aloud) → 24–30s payoff + CTA.
- **C · Personalization-demo hybrid (retargeting):** 0–2s reveal cold-open (blank → name typed on) → 2–8s occasion menu ("For Grandma. For Mom. For your dog's memorial.") → 8–16s quality proof (close-ups + photo review) → 16–24s risk-remover ("Don't love it? We remake it free" + order-by-date) → 24–30s CTA "See it with your names →".
> **Put the reveal at the MID-point, not the end** — you need post-reveal runtime for the reaction + CTA while retention is highest.

### Offer — tailored (ranked gift-native offers)
1. **Order-by-date / guaranteed delivery before the occasion** — highest leverage (gifts are deadline-bound + POD adds production time). Holiday urgency/clarity ~30–40% CVR lift. `[WIDER]`
2. **Remake / satisfaction guarantee on non-returnable personalized items** — removes the "typo/bad print, no recourse" blocker unique to personalized (final-sale) goods. Put it *at the point of doubt*. `[WIDER]`
3. **Free personalization (framed as a free gift, not a discount)** — free-gift framing raises purchase intent more than an equal discount (which lowers perceived value). Say "free personalization included," not "20% off." `[LAST-RESORT — peer-reviewed, general retail]`
4. **Multi-recipient / gift-set bundles** — fits gift-list behavior, +25–40% AOV. `[WIDER]`
5. **Free gift-wrap / gift message / gift-ready shipping** — low-cost, removes "I still have to wrap it." `[WIDER]`
6. **First-order discount** — works but rank LAST (competes on price, undercuts keepsake value); a *personalized* offer beats a blanket one. `[LAST-RESORT]`
> Strongest stack: **order-by-date + free remake + free personalization**; discount is the fallback, not the headline.

### CTA — tailored (gift language)
Meta's *button* is limited to ~17 presets (use **"Order Now"** for deadline/high-intent, "Shop Now" otherwise). Say the **gift CTA in the on-screen text / VO / end-card**:
- **"Make it for them" / "Make one with their names"** — default emotional CTA (cold, story-led).
- **"Personalize hers/his/theirs"** — recipient-targeted ad sets (Mom/Grandma/partner).
- **"See it with your names"** — low-commitment, retargeting / personalization-demo (Skeleton C).
- **"Create theirs / Design theirs in 60 seconds"** — reduces perceived effort.
- **"Order by [date] — get it before [occasion]"** — in-season deadline CTA (+ "Order Now" button).
- **Avoid** bare "Buy Now" for cold gift traffic — too transactional for an emotional keepsake. *(Personalized/first-person CTAs test better than generic — general-DTC data.)* `[LAST-RESORT]`

### Hook tactics — tailored (ranked for gifts)
**Tier 1 — gift-native (strongest, add these):** ① **reaction cold-open** (start on tears/gasp before context) · ② **personalization-reveal cold-open** (blank → their name appears) · ③ **occasion/deadline hook** ("Mother's Day is in 6 days and this takes 5 to make").
**Tier 2 — generic tactics that fit emotional buys:** ④ POV/relatable-emotional · ⑤ social-proof ("the gift 10,000 grandmas cried over" — cold) · ⑥ curiosity ("I didn't think a mug could make her cry") · ⑦ character/relationship open.
**Tier 3 — down-rank (fight the emotion arc):** stat · contrarian/controversy · problem-callout (System-2/functional). Before/after collapses into the reveal hook.
> **Stack a Tier-1 + Tier-2** (reaction cold-open → then name reveal) — practitioners note "multiple hooks" perform higher.

> ⚠️ **Honesty:** these four tailorings are **evidence-informed hypotheses**, not proven lifts — there is **no A/B data isolating any of them within the personalized-gift category.** EXACT rung = market behavior/creator briefs (qualitative); the quantified figures are WIDER (POD/holiday) or LAST-RESORT (all-category ad science). Test, don't assume.

### POD tailoring — source rungs
- **EXACT (qualitative):** Etsy Seller Handbook (occasions, hyper-personalization trends, "recipe plate" +110% YoY) · Marketing Dive (Etsy "feel truly seen" holiday campaign) · Printify Etsy-personalization guide · Sale Samurai · GetNameNecklace (live pet-memorial positioning) · TikTok gift-reaction culture + Kinfold Gifts creator call · Influee gifting-ad angle.
- **WIDER:** The Performers "10 gifting ad angles" · DesignRush (Ultimate Ears personalization reveal; <15s +38% completion; personalization ≈3× intent — POD-wide) · Printful/Gelato/Prodigi/Justin Cener POD ad mechanics.
- **LAST-RESORT (flagged):** Fraser Cottrell DTC tier list (founder-ad S-tier is a *general-DTC* claim, does NOT transfer) · Promer/Vlad Alexander/Sovran UGC theory.

## 🎬 Creative brief template (12 fields) — merged with an external script-framework table

*Added 2026-09-18. Source of the merge: an external "Kịch bản content phổ biến" table (5 script templates ×
8 craft columns: Hook · Storyline · Transitions · Visual · Voice · Caption&Text · Social Proof · CTA),
compared against this document. **It is a production spec; this document is a test system.** Theirs has no
measurement layer; ours under-specified craft. They compose — the merge below is the result.*

### The brief — every test case gets all 12 fields filled before it is shot
| # | Field | Who supplies it | Note |
|---|---|---|---|
| 1 | **Concept** | strategy | the whole idea, one sentence |
| 2 | **Angle / Persona** ⭐ | strategy | *ours — the external table has no slot for this.* Buyer ≠ recipient in gifting; a persona swap on an identical product is a real test |
| 3 | **Hook** (0.5–3s) | strategy | on-screen text + opening shot; Tier-1 gift-native preferred |
| 4 | **Storyline / Body** | strategy | which beat skeleton (A reaction-led / B sentiment-build / C demo-hybrid) |
| 5 | **Social-Proof beat** ⭐ | strategy | *promoted to a required field* — which proof type (rank 1–5) and **where it sits** |
| 6 | **Offer** ⭐ | strategy | *ours — absent from the external table.* Without it a beautiful ad can sell an unprofitable configuration |
| 7 | **CTA** | strategy | gift-language line + which of Meta's ~17 button presets |
| 8 | **Transitions / cut rate** | edit | **a number** (1.5s / 5s / beat-matched / progress-paced), not "fast cuts" |
| 9 | **Visual** | edit | colour temperature, background, camera distance |
| 10 | **Voice** ⭐ | edit | who speaks, tone arc, music bed, SFX/ASMR |
| 11 | **Caption & Text** | edit | overlay style, font, what gets highlighted; always sound-off legible |
| 12 | **Length** ⭐ | edit | *ours* — 6–15s Feed/Stories; 15–30s for the skeletons |

⭐ = field the external table does **not** have. Fields 8–11 are the ones **it** supplies that we previously
left to the editor's judgement.

### Adopted from the external table
- **① Voice as its own briefable field.** We had VO/music/sound in a single clause of "cross-cutting craft"
  and never prescribed it. Now a row in the per-component table above. This bites immediately: a text-heavy
  product (a printed letter/poem) **cannot do a personalization reveal**, so its concepts must be VO-led —
  and Voice is exactly the brief field that decision needs.
- **② Cut-rate as a number, per format.** ~1.5s/cut fast-persuasion vs ~5s/cut UGC. Encodes the real
  insight that **authenticity formats need slower cuts**. Matters for 60+ recipients, where fast-cut
  short-form pacing likely hurts.
- **③ Social Proof promoted to a required field.** Our proof ranking (reaction #1 · personalization detail
  #2 · volume/longevity #3 · photo-UGC #4 · craft close-ups #5) existed but was buried inside Body, so it
  was skippable. As a mandatory field it forces every video to answer *"what's the proof beat, and where?"*
- **④ The "Compare" recipe as a production spec** — split screen, parallel cutting, zoom into the
  differentiating detail. That is the shooting spec for our existing generic-vs-personalized split-screen
  hook; adopt verbatim.
- **⑤ BTS as a new format** (added to the format-fit table above, MEDIUM) — but Stage-2/retargeting only,
  since craft proof is our rank #5.

### Refused — where the external table conflicts with this research
| Their prescription | Why refused |
|---|---|
| **PAS / Problem-Solver as script #1** | PAS/AIDA engage rational System-2, which only fires for people already shopping for a solution; a gift buy runs the **emotion arc** (anticipation → escalation → reveal + reaction). Their visual spec makes it worse: *dark tones for the problem, red/yellow pain text* — the opposite of how a keepsake should look. "Problem-callout" is already **Tier 3** in our hook ranking. **Drop for gift products.** |
| **Social proof = order counts + screenshots of praising comments + before/after stats** | Wrong proof for this buyer. Our #1 proof is the **recipient's genuine reaction**; volume proof is #3 and only for cold legitimacy. Comment-screenshot stacking reads as dropship to a US Meta user in their 50s–60s. |
| **"Trending AI voice"** (offered in their UGC + Compare rows) | Fights the one thing the category runs on — a real human's voice breaking. Use real VO. |
| **Hard FOMO / urgency CTA** (their UGC row) | Our offer ranking puts **order-by-date deadline urgency** at #1 but *discount/FOMO pressure* last — it undercuts keepsake value. Deadline ≠ FOMO. |
| **Ordering instructions mid-video** (their Unboxing storyline) | Our skeletons put the **reveal at the midpoint** so there is runtime left for the reaction while retention is highest. |
| **CTA column as an emotional target** ("hit the emotions") | Not briefable. Ours specifies the actual line + the Meta button preset. |

> ⚠️ Provenance caution: that table is **TikTok / dropship-native**. Our buyer is a US Meta user, frequently
> 55+, buying an emotional keepsake. Adopt its *craft* fields; do not import its *persuasion* defaults.

### Their 5 scripts, mapped onto our format-fit ratings
| Their script | Maps to our format | Verdict |
|---|---|---|
| **Unboxing Review** | Gift-reaction (HIGH) + Unboxing (MED-HIGH) | **Keep — top format.** ≈ Skeleton A (reaction-led). Take beat-matched transitions + warm tone; drop mid-roll ordering instructions |
| **UGC** | UGC-raw (HIGH) | **Keep.** Take 5s/cut + word-by-word subtitles + phone-camera look. Drop AI voice, order-count proof, FOMO CTA |
| **Compare** | Hyper-personalization flex (HIGH) | **Keep.** The split-screen/zoom recipe is directly usable for generic-vs-personalized concepts |
| **BTS** | *(was absent from ours — now added, MEDIUM)* | **Adopt, Stage-2 / retargeting only** |
| **Problem-Solver (PAS)** | problem-callout = our **Tier 3** | **Drop** for gift products |

### What the external table cannot do (why this stays the source of truth)
No offer field · no angle/persona field · no format-fit rating (it presents 5 scripts as equals; we rate 15
and demote two hard) · no awareness-stage mapping · no length spec · **and no measurement layer at all** —
no hook rate, hold rate, sample gate, or kill line. It tells you what to *make*; only Part D of
`TESTING-MATRIX-FRAMEWORK.md` tells you what to *kill*.

## Honesty notes
- **Hard data:** Meta/Nielsen 47%-in-3s + 65%/45% watch-through [Meta primary]; sound-off ~80–85% [Meta]; Google creative≈50% ROI.
- **Practitioner benchmarks (vendors converge but self-reported):** hook 25–35% / hold 40–50% — conventions, not standards (denominators vary → 20–45% range exists).
- **Consensus/opinion:** the Andromeda diversity>OFAT shift and all volume numbers (8–12 concepts, 50–100/month, 3×3, 10–20 hooks, 90/10). The Meta-VP "4× more creative" is a secondhand paraphrase — directional.

### Source URLs
motionapp.com/blog/key-creative-performance-metrics · help.motionapp.com/en/articles/8991407 (Hook/Watch/Click/Convert) · help.motionapp.com/en/articles/12461770 (AI-tagging) · creads.io/ad-creative-performance-guide · sovran.ai/blog/hook-body-cta-video-ad-structure · adlibrary.com/posts/hook-rate · adlibrary.com/posts/hold-rate · facebook.com/business/news/updated-features-for-video-ads (47% data) · facebook.com/business/help/188534925073536 · triplewhale.com/blog/facebook-ad-analytics · growwithsakib.com/meta-ads-creative-testing (Segwise/Andromeda) · admanage.ai/blog/how-many-ad-creatives-to-test · motionapp.com/blog/best-dtc-meta-ad-hooks-2025 (Savannah Sanchez) · buildingadswithbarry.com (Barry Hott) · Dara Denney (Point Guard Media, LinkedIn/YouTube)
