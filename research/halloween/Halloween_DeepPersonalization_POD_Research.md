# Deep-Personalization POD Research — Halloween on Etsy
### Character-builder / live-preview products (Teeinblue · Customily class)

**Marketplace:** Etsy.com, US locale, USD
**Data captured:** 20 August 2026 (≈10 weeks before Halloween; 2026-season listings are live)
**Method:** Direct in-browser scraping of Etsy search results, listing pages, variation dropdowns, listing descriptions and item-review modals; Google Autocomplete (`google.com/complete/search`, client=chrome, hl=en, gl=us) plus live People-Also-Ask and "People also search for" blocks.

---

## 0. Methodology and three platform facts you must know before reading

**FACT — the star rating and review count on an Etsy *search card* is the SHOP's lifetime total, not the listing's.** Item-level review counts below were read separately from each listing page's `aggregateRating` block. Where a listing has zero item reviews, Etsy publishes the shop aggregate in that slot instead; I verified this fallback manually and flag those rows as `0 (none yet)`.

**FACT — Etsy does not host embedded third-party live-preview customizers.** I inspected the rendered DOM of **ten** listings (the deepest-personalization candidates in the set) for links or scripts belonging to Teeinblue, Customily, Zakeke, Kickflip or InkyBay. **Zero of the ten contained any**, and every one collected its options through Etsy's own native controls. Every "deeply personalized" Halloween listing on Etsy today collects its options one of three ways: (a) Etsy variation dropdowns (size/colour only, in practice), (b) Etsy's single free-text "Add personalization" box, or (c) a photo upload. This is the single most important structural fact in this report — it means the *option architecture* lives in the seller's back office, and the buyer never sees their design before it ships.

**RECOMMENDATION on tool framing:** for an Etsy-first business, Teeinblue/Customily are the **production engine** (layered artwork templates driven by option sets), not the storefront widget. The realistic Etsy workflow is: define option sets → publish them as numbered, illustrated menus in the listing images → collect the buyer's picks in the personalization box → auto-render in the customizer. If you also run a Shopify or WooCommerce storefront, that is where the true live preview goes, and Etsy becomes the discovery channel. Everything I recommend below is designed to work in both modes.

**Labels:** **FACT** = observed on the page today. **PATTERN** = my reading across many observations. **RECOMMENDATION** = my judgement.

Prices are the sale price displayed on 20 Aug 2026. Sales counters are live and tick upward; treat them as "at least this many."

**Verification pass:** every item-review count, rating and shop-sales figure quoted below was re-fetched a second time before publishing and matched, with one live-counter drift (FunnyDaisy 41,609 → 41,610 during the session).

---

## THE HEADLINE FINDING

**PATTERN — in the Halloween niche, customization *depth* and sales *volume* are almost perfectly inversely distributed.**

FACT, side by side:

| Listing | Customization actually offered | Shop lifetime sales | Item reviews |
|---|---|---|---|
| [BlinkStudioCrafts — "Choose Family Characters & Pets"](https://www.etsy.com/listing/4535084597/) | **40 published character options**: 10 girl costumes, 10 boy costumes, 10 cat breeds, 10 dog breeds, plus a name per character | **48** | 0 |
| [BlueDiamondTees — "Custom Cartoon Character Halloween Tee"](https://www.etsy.com/listing/4529961127/) | Description defines **no options at all** | **53,482** | 0 (none yet) |
| [TheTeeStudio — "Custom Character Matching Costume Tee"](https://www.etsy.com/listing/4550055738/) | "Choose a different Halloween character for every family member" — characters **never enumerated** | **143,112** | 0 (none yet) |
| [StudioCutee — "Custom Halloween Gothic Family Shirt"](https://www.etsy.com/listing/4544740957/) | Ordering steps are size → colour → add to cart. **Personalization is never explained** | **26,970** | 1 |

The shop with the only genuine character builder I found in Halloween has **48 lifetime sales**. The shops with six-figure sales are selling the *promise* of character customization with no system behind it.

**And the architecture is proven — one season later.** FACT: the identical product structure is a mature, enormous market at Christmas:

| Christmas benchmark | Price | Item reviews | Shop sales |
|---|---|---|---|
| [GloryParty — Family of 3/4/5 Ornament **with Pet Dog**, personalized people](https://www.etsy.com/listing/1106986178/) | $19.99 | **2,456** | 180,318 |
| [FunnyDaisy — Family Ornament with Pets, **up to 20 members**](https://www.etsy.com/listing/4395698361/) | $6.55 | **1,264** | 41,609 |
| [svgmilocom — Family With Pet 4D Shake Ornament](https://www.etsy.com/listing/4371815048/) | $19.79 | 38 | 103,344 |
| [HolidaysSewCute — Family Ornament with Pets, **hand-drawn characters**](https://www.etsy.com/listing/1750399974/) | $24.50 | 24 | 6,144 |

Halloween's best equivalent — [OrnamentallyYouGifts' "Ghost Family With Pets"](https://www.etsy.com/listing/1747606360/) — has **2 item reviews**, and its customization is names only. Nobody has ported the Christmas character-builder architecture to Halloween. That is the opportunity this entire report circles.

---

# PART 1 — Multi-layer scan of the Halloween niche, read through a personalization lens

## Layer A — Core "personalized Halloween" keyword

**What is selling (FACT):** page one of `personalized halloween family shirt characters`, `custom skin tone halloween shirt` and `personalized halloween cartoon family portrait shirt` is dominated by three formats — (1) **custom names** on a fixed ghost/pumpkin graphic, (2) **photo upload** cut into a spooky frame ("Custom Halloween Face Shirt", "Custom Photo to Cartoon Tee"), and (3) **licensed-character name shirts** (Disney/Mickey "Boo Crew" with names).

**Target customer:** mothers 28–45 buying for the whole household; grandparents buying for grandchildren; couples.

**Products:** Comfort Colors/Gildan/Bella tees, crewnecks, toddler and infant bodysuits, canvas totes, ceramic ornaments, mugs, pyjama sets.

**Aesthetic:** cute-not-scary. Rounded doodle characters, muted garment-dyed colours (Pepper, Yam, Ivory, Blue Jean, Moss), orange/cream/black. A pink coquette line and a gothic/Addams line run as counter-currents.

**Price range (FACT):** tees $5.49–$31.30 (dense $10–$23); ornaments $3.99–$20.84; mugs $7.45–$27.18; totes $3.95–$16.99.

**Competition:** very high on *keyword*, very low on *capability*. Hundreds of shops compete on the word "personalized"; almost none compete on how much you can actually change.

**Volume evidence (FACT):** TheTeeStudio 143,112 sales · BlueDiamondTees 53,482 · shirtbutcool 96,161 · creativencustomized 97,228 · SmyrnaDesignUS 37,689 · RoseApparelCrafts 42,400.

**Customization potential (RECOMMENDATION):** this is the richest possible category for a builder. A Halloween family scene naturally supports 5–8 characters, each with costume + skin tone + hair style + hair colour + name, plus pets with species/breed/coat. Personalization here is not decorative — it is the entire emotional proposition ("that's *us*"). Meaningful option count: **300+ combinations from ~50 assets.**

## Layer B — Priority product categories, ranked by personalization headroom

### B1. Hanging ornaments — **highest headroom, lowest competition**
FACT: Halloween family ornaments are a real, active category — [DomDomGift](https://www.etsy.com/listing/4554387919/) (811 shop reviews, $10.19), [NativeGreenWood](https://www.etsy.com/listing/4541976068/) (769, $12.33), [StudioCutee](https://www.etsy.com/listing/4555349205/) (4,985, $11.99), [ChristmasDecorationX](https://www.etsy.com/listing/4549045672/) (2,128, $9.54), [PrintFairyMomma "Family and Pet Halloween Portrait"](https://www.etsy.com/listing/4549574164/) ($19.35, 459 shop sales).
PATTERN: **every one of them is names-only or names+year.** Not one offers per-character appearance selection.
Price $3.99–$20.84. Competition: **low** — the shops here run 250–3,400 shop reviews versus 16,000+ for apparel shops.
Customization potential: **10/10.** Flat ceramic/acrylic print, no sizing, no fit risk, and the Christmas benchmark proves buyers will pay $19.99 and leave 2,456 reviews for exactly this.

### B2. T-shirts / sweatshirts — highest volume, deepest talent pool, most crowded
FACT: variation dropdowns are used almost exclusively for garment and colour. [ChupchupShop](https://www.etsy.com/listing/4546290531/) offers 19 size options and 26 colours — and the *dog breed*, the actual design variable, is not a dropdown at all; the description simply says "Choose your dog's breed."
Price $5.49–$63.23. Competition: extreme.
Customization potential: 9/10, but you are fighting 100k-sale shops on ad spend.

### B3. Mugs — **under-built relative to demand**
FACT: personalized Halloween family mugs exist but the field is shallow — [RojoCreativeStudio](https://www.etsy.com/listing/4363889807/) ($25.00, 39 shop reviews, 241 shop sales), [VelvetGiftDesign](https://www.etsy.com/listing/4517356625/) ($27.18, 6 shop reviews), [Jarify](https://www.etsy.com/listing/4336352122/) ($9.80, 123). The one substantial player is [SunsetStores' colour-change mug](https://www.etsy.com/listing/4544701207/) ($26.97, 6,691 shop reviews, 39,381 sales) — and it personalizes **names only**.
Price $7.45–$27.18. Competition: low-moderate.
Customization potential: 8/10 — a mug wraps, so it can hold a 4–6 character line-up better than a chest print.

### B4. Tote bags — proven multi-unit purchase, zero character depth
FACT: the category is enormous and entirely name-driven. [Creativencustomized](https://www.etsy.com/listing/1792793532/) 97,228 sales · [Lalalagiftland](https://www.etsy.com/listing/1083855409/) **1,828 item reviews** · [SmyrnaDesignUS](https://www.etsy.com/listing/4366864956/) 37,689 sales, 26 item reviews · [VizzBee](https://www.etsy.com/listing/4376329154/) 59 item reviews, Bestseller.
Price $3.95–$16.99. Competition: high on price, **nil on character**.
Customization potential: 7/10 — and uniquely, buyers order 2–4 at once (see Part 4), so a sibling-set builder has a natural basket multiplier.

### B5. Stickers, posters, hats — thin personalization
FACT: `custom halloween stickers with name` returns **no Google suggestions at all**; personalized Halloween hats are embroidered-name witch hats ([TinyBarns](https://www.etsy.com/listing/4530270026/), 69,811 sales) with no character system. Posters are dominated by *hand-made custom portraits from photo* rather than option-driven builders — [BlissfulVibesArt](https://www.etsy.com/listing/4536029263/) ($19.95, 4,705 sales), [BOBDEUS](https://www.etsy.com/listing/1805846757/) ($19.50, 10,553 sales), [Lekabrand](https://www.etsy.com/listing/4362411779/) ($16.00, 7,079 sales).
Customization potential: stickers 5/10, hats 4/10, posters 8/10 (but currently served by manual artists at 24–72h turnaround, not by a builder).

## Layer C — Audience sub-segments and their customization ceilings

| Segment | What sells now (FACT) | Personalization offered now | Ceiling if built properly |
|---|---|---|---|
| **Matching families** | "Boo Crew" name tees; skeleton family sets; Disney character name shirts ([R2Designer](https://www.etsy.com/listing/4544962618/), Bestseller, 9 item reviews) | names only, or one shared surname | 5–8 characters × costume × skin tone × hair × name. **10/10** |
| **Pet parents** | Boo-p ghost dog; breed tees; **photo-upload pet tees** ([PixelThreadAlchemy](https://www.etsy.com/listing/4551893525/) 3,981 sales; [GoodEnergyShirts](https://www.etsy.com/listing/4540072629/) 796 sales) | breed typed into a text box, or a photo | species → breed → coat colour → costume → name. **9/10** |
| **Grandparents** | "Grandma's Little Monsters/Boo Crew" with grandkids' names — [Luvilooom](https://www.etsy.com/listing/1770068151/) 2,435 shop reviews; [SingleLadyTee](https://www.etsy.com/listing/1756830632/) 6,100; [ScorpioBoy "Cute Doodle Characters"](https://www.etsy.com/listing/4531946106/) 196 | names only (ScorpioBoy hints at doodles but does not let you choose them) | one costumed character **per grandchild** + grandparent title. **9/10** |
| **Couples** | ghost couples, skeleton couples, custom year, "Her Boo/His Boo" — [ShopCleverly](https://www.etsy.com/listing/4539617880/) $27.02, 158 | names + year | 2 characters × appearance + optional pet. **8/10** |
| **Teachers** | personalized name/grade tees — [TheTeeStudio gothic teacher](https://www.etsy.com/listing/4546172780/) $19.99; [FanTeeCreations](https://www.etsy.com/listing/4554912541/) 1,900 shop reviews | name, grade, room number | teacher character + up to 25 tiny student ghosts with names. **8/10**, but heavy data entry |
| **Babies / first Halloween** | "My First Halloween" bodysuits and year-stamped ornaments — [Qatasta](https://www.etsy.com/listing/4529724314/) Bestseller; [ApparelByMoliva](https://www.etsy.com/listing/4528864724/) 7,889 sales | name + year | baby character + skin tone + hair wisp + parents + pet. **7/10** |
| **Coworkers / office teams** | generic group tees; personalized **dental practice** shirts are the one mature vertical ([EndeavorGoods](https://www.etsy.com/listing/4540245508/) 84,005 sales) | practice name | character + role per employee. **8/10** but high admin |

## Layer D — Slogans and community language already printed (FACT)

Boo Crew · Our Little Boo Crew · Hangin' With My Boos · My Favorite Boos Call Me Grandma · Grandma's Little Monsters · Home Is Where the Boos Are · Mom's Little Monsters · Boo-p (ghost dog) · Creepin' It Real · Our Crew Got Spookier · Trick or Teach · Daddy/Mommy/Bubba/Sissy titles · Est. [year] family lockups.

**PATTERN:** every one of these slogans is a **container for a variable cast**. "Boo Crew" is meaningless without a crew; "Grandma's Little Monsters" is meaningless without the monsters. The copy layer of this niche was built for a character builder — the artwork layer never caught up.

## Layer E — Design styles trending (PATTERN)

1. **Cute doodle characters** — rounded, flat-colour, thick outline. The dominant and most builder-friendly style.
2. **Gothic / Addams-family portrait** — Victorian frame, black clothing, moody palette. Highest emotional payoff, currently served by manual illustrators.
3. **Retro halftone** — faded 70s–90s print in garment-dyed colours.
4. **Coquette pink** — bows, pastel pink + black.
5. **Photo-cutout** — a real face dropped into a spooky frame. Fast, but it is the *opposite* of a designed product and it ages badly.
6. **Shaker / 4D layered ornaments** — proven at Christmas ([svgmilocom](https://www.etsy.com/listing/4371815048/), 103,344 sales), barely present at Halloween ([PoppinDripbyRon](https://www.etsy.com/listing/4530198322/) $6.80, 170).

## Layer F — "Gift for ___" phrasing in titles (FACT)

gift for dog mom · dog dad · pet parents · new parents · grandparents · friends · Halloween party hosts · teacher · dental office · husband · bestie · work bestie · family Halloween photos · pumpkin patch trips · trunk or treat.

**PATTERN:** the buyer is almost never the wearer. This is a **gifting category with an identity payload** — which is exactly the condition under which deep personalization converts, because the giver is trying to prove they know the recipient.

---

# PART 2 — Google validation of personalization demand

## 2.1 Autocomplete (FACT — verbatim, US, 20 Aug 2026)

| Seed | Suggestions returned |
|---|---|
| `personalized halloween shirt` | personalized halloween shirts · **for kids** · **for adults** · **personalized grandma halloween shirt** · personalized halloween t shirts · **personalized disney halloween shirts** · **personalized dog halloween shirt** · halloween custom shirt design |
| `personalized halloween` | **basket** · **bag** · **bucket** · **gifts** · candy bowl · decor · bags for kids · treat bags · book |
| `personalized halloween gifts` | **for kids** · **for adults** · personalised halloween gifts · unique halloween gifts for adults / kids / women / teens |
| `custom halloween gifts` | personalised · **for kids** · **for adults** · custom halloween gift bags · gift boxes |
| `custom family portrait` | painting · illustration · **from photo** · drawing · **cartoon** · **with pets** · **etsy** · canvas · puzzle |
| `custom family portrait with pets` | **personalized family portrait with pets** · **custom family portrait with dog** · family portrait with dog ideas · pets are family members |
| `custom family portrait cartoon` | **personalized family cartoon portrait** · custom family cartoon picture |
| `custom family ornament with pets` | **custom family ornament with dog** · **custom family christmas ornament with pets** · **personalized family ornament with dog and cat** · custom family christmas ornament with dog |
| `halloween family portrait` | ideas · photo · photo ideas · picture · photo shoot · captions · **personalized halloween family portraits** · spirit halloween chucky family portrait |
| `custom halloween family portrait` | **personalized halloween family portraits** |
| `personalized family halloween` | **personalized halloween family portraits** · custom family halloween · custom family halloween costumes |
| `family halloween costume with dog` | **with dog and baby** · ideas with dog · costume ideas with dog · **with two dogs** · **addams family halloween costume with dog** · best · funny · cute |
| `personalized grandma shirt with grandkids` | **personalized grandma shirts with grandkids names** · personalized grandma t shirts with grandkids names · **women's** personalized grandma shirts with grandkids names · grandma shirts with grandkids names · shirts with grandkids names |
| `personalized trick or treat bag` | **bags with names** · **for kids** · custom trick or treat bags **bulk** · personalized trick or treat bucket · personalized trick or treat tote |
| `boo crew shirt` | **ideas** · **kids** · **disney** · **boo crew shirts family** · nearby · old navy · toddler |
| `personalized halloween ornaments` | **custom halloween ornaments** · personalized halloween decor |
| `custom halloween mug` | custom halloween mugs · personalised halloween mug · **custom halloween cups** |
| `personalized halloween pajamas` | **custom halloween pajamas** · personalized halloween pjs |
| `personalized halloween couple` | **custom halloween couple** · custom couple halloween costumes |
| `personalized halloween hat` | **custom halloween hats** · personalized halloween costume · halloween hat ideas |
| `personalized ornament skin tone` | **[NONE]** |
| `custom halloween shirt with dog` | **[NONE]** |
| `personalized dog halloween shirt` (as a full phrase) | **[NONE]** — but it *is* returned as a suggestion under `personalized halloween shirt` |
| `personalized nurse halloween shirt` | **[NONE]** |
| `personalized teacher halloween shirt` | **[NONE]** |
| `custom halloween shirt for baby` | **[NONE]** |
| `custom family halloween shirt` | **[NONE]** — but `custom family halloween` and `custom family halloween costumes` both return |
| `custom halloween stickers with name` | **[NONE]** |
| `custom dog breed halloween` | dog costume for halloween (intent mismatch) |

## 2.2 People Also Ask + related searches (FACT — live SERPs)

**`family halloween costume ideas with dog`**
PAA: *"What are some cute Halloween costumes I can wear with my dog?"* · *"What to do on Halloween with a dog?"* · *"What are some popular family Halloween costume ideas?"* · *"What are the top three most popular Halloween costumes for dogs?"*
Related: **Family halloween costume ideas with dog for 4** · Adult family halloween costume ideas with dog · **Family Halloween Costumes with dog and baby** · Dog and owner costume ideas

**`personalized family portrait with pets`**
PAA: *"How much does a custom pet portrait cost?"* · *"Can I get a custom pet portrait painting made?"* · *"How can I create my own custom pet portrait?"* · *"What is the best website for getting a pet portrait?"*
Related: Best personalized family portrait with pets · **Pet portrait generator free** · Custom funny pet portraits · Best custom pet portraits

**`personalized halloween gifts for adults`**
PAA: *"What are some unique Halloween gift ideas for adults?"* · *"What are some good Halloween goodies for adults?"* · *"What to give to adults on Halloween?"*
Related: Unique / Best / cheap / **Luxury** personalized halloween gifts for adults · Personalized Halloween Doormat

## 2.3 REAL GAPS — search demand exists, Etsy's customization does not meet it

| # | Demand signal (Google) | Etsy supply reality | Why it is a gap |
|---|---|---|---|
| **R1** | `custom family ornament with pets` → "**with dog and cat**", "with dog"; `personalized halloween ornaments` → "custom halloween ornaments" | Every Halloween family ornament found is **names-only**. Best-selling one has **2 item reviews**. | Buyers want the *cast* rendered, not the names typed. The Christmas analogue with the same cast structure has **2,456 item reviews**. |
| **R2** | `family halloween costume with dog` → "**and baby**", "**two dogs**", "**Addams family… with dog**"; PAA asks for family+dog costume ideas | One micro-shop (48 sales) lets you pick family characters *and* pets. Everyone else: names or nothing. | Households now define "family" as adults + kids + named pets. No Halloween product lets them assemble that. |
| **R3** | `personalized grandma shirts with grandkids names` — **five** distinct autocomplete variants | Saturated with names on a fixed graphic ([Luvilooom](https://www.etsy.com/listing/1770068151/) 2,435 shop reviews; [SingleLadyTee](https://www.etsy.com/listing/1756830632/) 6,100) | The demand is proven and enormous; the *product* is a text field. One costumed character per grandchild is a straight upgrade of a validated seller. |
| **R4** | `custom family portrait` → "**cartoon**", "**with pets**", "**etsy**"; `custom halloween family portrait` → "personalized halloween family portraits" | Served by **manual illustrators** at $10.50–$34 with 24–72h turnaround and revision rounds ([pawfectpixco](https://www.etsy.com/listing/4341756502/) 70 item reviews) | An option-driven builder delivers the same emotional product instantly, at higher margin, with no artist bottleneck. |
| **R5** | `personalized halloween shirt` → "**personalized dog halloween shirt**"; PAA "pet portrait generator free" | Pet Halloween personalization splits into *photo upload* or *breed typed into a text box*. No illustrated breed picker. | Buyers who don't want a photograph printed on a tee currently have no designed option. |
| **R6** | `personalized trick or treat bag` → "**with names**", "**bulk**", "for kids" | Names on canvas; no character. Reviews show buyers ordering **3 at a time** for siblings/grandchildren. | A sibling-set builder (one character per child, matching art) converts a $4 single into a $30 set. |
| **R7** | `custom halloween mug` / `custom halloween cups` validated | Personalized Halloween family mugs are shallow — the biggest player personalizes **names only** at $26.97 | A wrap-around 4–6 character line-up is a natural mug format nobody is using. |
| **R8** | `personalized halloween couple` → "custom halloween couple" | Names + year on a fixed ghost pair | Two-character appearance selection + optional pet is unbuilt. |
| **R9** | `boo crew shirt` → "**boo crew shirts family**", "kids", "disney" | "Boo Crew" is everywhere as *words*; the crew is never depicted | The slogan already presells a variable cast. |
| **R10** | `personalized halloween gifts for adults` → "**Luxury**", "Best", "Unique" | Adult-facing personalized Halloween is thin; most personalization is aimed at kids | Room for a $25–$35 keepsake tier aimed at adults. |

## 2.4 FALSE GAPS — do not build these

| Idea | Evidence it fails |
|---|---|
| **Skin tone as a headline concept or keyword** | `personalized ornament skin tone` returns **[NONE]**. Nobody searches for it. **This does not mean skin-tone options are unimportant** — it means they are a *conversion and satisfaction* feature that must live *inside* a validated concept, never as the concept itself or as a title keyword. |
| **"Custom halloween shirt with dog" as a keyword** | **[NONE]**. The traffic sits under `personalized halloween shirt` → "personalized dog halloween shirt". Word order matters; title accordingly. |
| **"Personalized teacher/nurse halloween shirt" as keywords** | Both **[NONE]** as literal phrases. The volume is on the un-personalized head terms (`teacher halloween shirt`, `nurse halloween shirt`) — so personalization must be discovered *inside* those listings, not through a personalized-prefixed title. |
| **Custom Halloween stickers with names** | `custom halloween stickers with name` → **[NONE]**. Sticker demand is for *designs*, not for personalization. Low ceiling; skip as a hero product. |
| **`custom dog breed halloween`** | Autocomplete resolves to "dog costume for halloween" — the searcher wants to dress the dog, not buy a breed-illustrated shirt. Use `personalized dog halloween shirt` phrasing instead. |
| **Personalized Halloween hats** | `personalized halloween hat` returns only "custom halloween hats" and costume queries. Embroidered-name witch hats already own it and there is no character headroom on a hat. |
| **"Custom family halloween shirt" as an exact title phrase** | **[NONE]** in that word order. Use "personalized halloween family shirts" / "custom family halloween costumes". |

---

# PART 3 — Listings with proven sales potential, graded on customization

**Depth key:** **B** = basic text (names/dates only) · **M** = moderate (text + one or two structured choices, or photo upload) · **H** = highly customizable (multiple structured option sets driving the artwork).
**Customizer-compatible** = could this design be rebuilt as a layered Teeinblue/Customily template with option sets? (Assessed from the artwork structure, since — FACT — **no** Etsy listing inspected contained any embedded customizer script or link.)

| # | Listing | Product | Target customer | Concept / style | Price | Item rev · rating | Shop sales | Personalization offered | Depth | Workflow | Customizer-compatible |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Choose Family Characters & Pets Boo Crew Tee](https://www.etsy.com/listing/4535084597/) — BlinkStudioCrafts | Tee/sweatshirt | Matching families with pets | Cute doodle costume characters | $22.89–$63.23 | 0 · 5.0 | **48** | **40 published options**: 10 girl + 10 boy costumes, 10 cat breeds, 10 dog breeds, family name, name per character | **H** | Buyer types character *numbers* + names into Etsy's text box. No preview. | **Yes — ideal.** Already a discrete option matrix |
| 2 | [Custom Character Matching Costume Tee](https://www.etsy.com/listing/4550055738/) — TheTeeStudio | Tee | Families | Costume characters + titles (Daddy/Mommy/Nana/Papa) | $18.99–$31.09 | 0 (none yet) · 4.9 | **143,112** | "Choose a different character for every member" + names/titles — **characters never listed** | **M** | Free-text box; 30 garment × 14 colour variations | Yes — needs an option library it doesn't have |
| 3 | [Custom Cartoon Character Halloween Tee](https://www.etsy.com/listing/4529961127/) — BlueDiamondTees | Tee/bodysuit/sweatshirt | Families, babies | "Custom cartoon character" | $6.98–$34.37 | 0 (none yet) · 4.9 | **53,482** | Description defines **no options**; 36 size × 11 colour | **B** | Free-text box | Yes — pure whitespace inside a big shop |
| 4 | [Custom Halloween Gothic Family Shirt](https://www.etsy.com/listing/4544740957/) — StudioCutee | Tee | Gothic couples & families | Addams-style horror family | $12.29–$17.58 | 1 · 5.0 | 26,970 | Ordering steps never mention personalization | **B** | Free-text box | Yes |
| 5 | [Halloween Ghost Family With Pets Ornament](https://www.etsy.com/listing/1747606360/) — OrnamentallyYouGifts | Ceramic ornament | Families with pets | Ghost family incl. pets | $14.99 | **2** · 5.0 | 16,742 | Family names + pet names | **B** | Etsy "Add personalization" | **Yes — highest-value rebuild target** |
| 6 | [Family and Pet Halloween Portrait Ornament "Our Crew Got Spookier"](https://www.etsy.com/listing/4549574164/) — PrintFairyMomma | Ceramic ornament | Families with pets | Portrait-style crew | $19.35 | 0 (none yet) · 5.0 | 459 | Names | **B** | Text box | Yes |
| 7 | [Personalized Halloween Family Ornament, Ghost & Pet Acrylic](https://www.etsy.com/listing/4551958817/) — BetterHandcraft | Acrylic ornament | Families with pets | Pumpkin house + ghosts | $14.24 | 0 (none yet) · 4.5 | 1,673 | Names | **B** | Text box | Yes |
| 8 | [Personalized Halloween Family Ornament](https://www.etsy.com/listing/4554387919/) — DomDomGift | Ornament | Families | Ghost family + name | $10.19 | — · 4.6 | — (811 shop rev) | Names | **B** | Text box | Yes |
| 9 | [Personalized Vintage Halloween Family Ornament](https://www.etsy.com/listing/4541976068/) — NativeGreenWood | Wooden ornament | Families | Vintage character name tags | $12.33 | — · 4.6 | — (769 shop rev) | Names | **B** | Text box | Yes |
| 10 | [Family Halloween Ghost Ornament Boo Crew](https://www.etsy.com/listing/4555349205/) — StudioCutee | Ornament | Families | Ghost crew | $11.99 | 0 (none yet) · 4.8 | 26,970 | Names | **B** | Text box | Yes |
| 11 | [Personalized Ghost Family Ornament "Our Little Boo Crew"](https://www.etsy.com/listing/4549045672/) — ChristmasDecorationX | Ornament | Families | Ghost crew + names | $9.54 | — · 4.8 | 10,360 | Names | **B** | Text box | Yes |
| 12 | [Personalized Halloween Dog Shirt, 20+ Custom Breeds](https://www.etsy.com/listing/4546290531/) — ChupchupShop | Tee | Dog parents | Breed in witch hat + pumpkin basket | $16.15–$25.63 | 0 (none yet) · 4.9 | 6,232 | "Choose your dog's breed" — **breed list never published**, not a dropdown; 19 size × 26 colour | **M** | Free-text box | **Yes — breed library is the obvious upgrade** |
| 13 | [Personalized Dog Breeds Halloween Comfort Colors Shirt](https://www.etsy.com/listing/4534308317/) — HuynhByCreatorsUS | Tee | Dog parents | Pumpkin-coffee dog | $25.72–$36.17 | 0 (none yet) · 4.8 | 3,981 | Breed (undocumented); 15 size × 20 colour; PNG-file option at $7.50 | **M** | Free-text box | Yes |
| 14 | [Custom Dog Breed Halloween Shirt, Salem Witch Club, 25 Dog Breeds](https://www.etsy.com/listing/4543470242/) — AidenStudioUS | Tee | Dog parents | Witch-club club scene | $9.90 | — · 5.0 | — (2 shop rev) | Claims 25 breeds | **M** | Text box | Yes |
| 15 | [Custom Dog Photo Halloween Shirt, Witch Pet Tee](https://www.etsy.com/listing/4540072629/) — GoodEnergyShirts | Tee | Dog parents | Photo of the actual dog | $22.40 | 0 (none yet) · 5.0 | 796 | **Photo upload** | **M** | Upload | No — photo pipeline, not option-driven |
| 16 | [Custom Halloween Dog Shirt, Skeleton Dog Photo Tee](https://www.etsy.com/listing/4551893525/) — PixelThreadAlchemy | Tee | Dog parents | Photo + skeleton overlay | $18.40 | 0 (none yet) · 4.9 | 3,981 | Photo upload + name | **M** | Upload | No |
| 17 | [Grandma's Little Monsters Cute Doodle Characters](https://www.etsy.com/listing/4531946106/) — ScorpioBoy | Tee | Grandmothers | Doodle monsters, one per grandchild | $16.94 | 0 (none yet) · 4.9 | 2,545 | Grandkids' names (doodles are **fixed**, not chosen) | **M** | Text box | **Yes — closest existing shape to the winning concept** |
| 18 | [Custom Halloween Grandma's Little Monster Tee](https://www.etsy.com/listing/1770068151/) — Luvilooom | Tee | Grandmothers | Monster + names | $13.80 | — · 4.8 | — (2,435 shop rev) | Names | **B** | Text box | Yes |
| 19 | [Personalized Grandma With Grandkids Name Shirt](https://www.etsy.com/listing/1756830632/) — SingleLadyTee | Tee | Grandmothers | Ghost + names | $8.50 | — · 4.9 | — (6,100 shop rev) | Names | **B** | Text box | Yes |
| 20 | [Custom Family Name Halloween **Colour-Change** Mug](https://www.etsy.com/listing/4544701207/) — SunsetStores | Mug | Families | Boo ghosts + family name | $26.97 | 0 (none yet) · 4.8 | 39,381 | Names only | **B** | Text box | Yes — highest-priced mug in the set, on names alone |
| 21 | [Personalized Halloween Family Mug, Halloween Characters Boo Crew](https://www.etsy.com/listing/4363889807/) — RojoCreativeStudio | Mug | Families | Character line-up | $25.00 | 1 · 5.0 | 241 | Names + characters (undocumented) | **M** | Text box | Yes |
| 22 | [Custom Halloween Ghost Family Tote Bag](https://www.etsy.com/listing/4542540064/) — StudioCutee | Tote | Families / trick-or-treat | Ghost family | $10.79 | 0 (none yet) · 4.8 | 26,970 | Names | **B** | Text box | Yes |
| 23 | [Personalized Halloween Tote Bag: Custom Trick or Treat Canvas Bag](https://www.etsy.com/listing/1083855409/) — Lalalagiftland ⭐Bestseller | Tote | Parents & grandparents | Name + icon | $8.24 | **1,828** · 5.0 | 84,880 | Name, font, design choice | **B** | Text box + design number | Yes |
| 24 | [Custom Name Halloween Tote Bag](https://www.etsy.com/listing/4346792179/) — TeeTeeOutfit ⭐Bestseller | Tote | Parents | Name + type | $3.95 | **104** · 4.9 | 63,289 | Name | **B** | Text box | Yes |
| 25 | [Personalized Neon Trick or Treat Bag](https://www.etsy.com/listing/4376329154/) — VizzBee ⭐Bestseller | Tote | Parents | Neon name | $15.00 | **59** · 4.8 | 30,197 | Name + neon colour | **M** | Text box + colour choice | Yes |
| 26 | [Custom Trick or Treat Bag with Kids Names](https://www.etsy.com/listing/4366864956/) — SmyrnaDesignUS | Tote | Parents | Name + character | $4.79 | **26** · 5.0 | 37,689 | Name | **B** | Text box | Yes |
| 27 | [Custom Kids Halloween Neon Shirt](https://www.etsy.com/listing/4311458472/) — RoseApparelCrafts | Kids tee | Parents & grandparents | Neon ghost + name | $13.20 | **68** · 5.0 | 42,400 | Name + neon colour | **M** | Text box | Yes |
| 28 | [Custom Gothic Portrait: Addams Family Style **With Pets**](https://www.etsy.com/listing/4341756502/) — pawfectpixco | Digital poster | Couples & families with pets | Hand-drawn Addams-style | $10.50 | **70** · 5.0 | 781 | **Photo → manual illustration**, revisions by message | **M** | Human artist, 2 concept options offered | No — but proves the *demand* a builder would capture |
| 29 | [Custom Halloween Witch Portraits](https://www.etsy.com/listing/1805846757/) — BOBDEUS | Poster/print | Adults, gifting | Manual spooky portrait | $19.50 | 9 · 5.0 | 10,553 | Photo → manual art | **M** | Human artist | No |
| 30 | [Comfort Colors Personalized Disney Halloween Family Shirts](https://www.etsy.com/listing/4544962618/) — R2Designer ⭐Bestseller | Tee | Families | Licensed characters + names | $5.49 | 9 · 5.0 | 15,831 | Character *set* + names | **M** | Text box | Partially — IP-constrained |

### Christmas benchmark set (adjacent-season proof that the architecture works)

| Listing | Price | Item reviews | Shop sales | Customization |
|---|---|---|---|---|
| [GloryParty — Family of 3/4/5 with Pet Dog, personalized people](https://www.etsy.com/listing/1106986178/) | $19.99 | **2,456** | **180,318** | Number of people, per-person appearance details, pet, names — all typed |
| [FunnyDaisy — Family Ornament with Pets, **up to 20 members**](https://www.etsy.com/listing/4395698361/) | $6.55 | **1,264** | 41,609 | Member count + names |
| [svgmilocom — Family With Pet 4D Shake Gingerbread Ornament](https://www.etsy.com/listing/4371815048/) | $19.79 | 38 | 103,344 | Members + pet |
| [HolidaysSewCute — hand-drawn characters with pets](https://www.etsy.com/listing/1750399974/) | $24.50 | 24 | 6,144 | Hand-drawn per-character detail |
| [CaDoKoShop — Custom Couple With Dog Ornament](https://www.etsy.com/listing/4390659734/) | $10.75 | **29** | 80,867 | Couple + pet |

**PATTERN — three things this table proves.**
1. **Depth H exists exactly once** in 30 Halloween listings, and it belongs to a shop with 48 sales.
2. **Every high-volume Halloween "custom character" listing is Depth B or M** — the customization is a promise, not a system.
3. **Every one of these designs is customizer-compatible.** The artwork is already modular (a row of characters, a pet, a name band). Nothing about the category resists a Teeinblue/Customily template; the sellers simply haven't built one.

---

# PART 4 — Review mining for personalization signals

Reviews were read from item-review modals. Sizing and print-quality complaints unrelated to design are excluded per brief.

## 4.1 The customization-friction signal (the most valuable finding)

**From [GloryParty's Christmas family-with-pet ornament](https://www.etsy.com/listing/1106986178/) — 2,456 item reviews** *(adjacent-season, same product architecture)*:

- *"Great product! Very fast shipping! **Be sure to be specific to all hair hat etc.. :)**"*
- *"**Great ornaments considering all the details I added**"*
- *"Very cute. **Written just how I typed it.** High quality item."*
- *"Their hats are actually SUPER shimmery… **the names are hand written, which I LOVED, made it feel not factory copy paste**"*
- *"**I buy one every year!**"*
- *"Perfect for new family's 1st Christmas — they love to read to the baby!"*

**PATTERN:** buyers of multi-character personalized keepsakes are *already* doing the work of a customizer in prose — describing hair, hats and details in a free-text box, then hoping. One reviewer is literally coaching the next buyer on how to write a good brief. That instruction would be unnecessary in front of a live preview. **This is the clearest evidence in the whole study that the option-set + preview layer is the missing product, not the artwork.**

**From [pawfectpixco's Addams-style family portrait with pets](https://www.etsy.com/listing/4341756502/) — 70 item reviews:**

- *"The photo came out amazing! **I asked for a change and it was taken care of right away.**"*
- *"fricken love my piece, they were so accommodating with the request and **loved that they gave two options to choose from**"*
- *"**Sooo cute! It's exactly what I wanted. I did one edit just to change one or two things.** My husband was so happy."*
- *"**She's 'spot on' with the dark clothing and making us spooky!**"*
- *"Quality image that **captured the subject**."*
- *"It was **exactly what I envisioned**."*
- *"made a good family photo even better and **really goes with everything we own! already looking for another photo**"*

**PATTERN:** the emotional payoff is **likeness** — "spot on", "captured the subject", "exactly what I envisioned". The cost of achieving it today is a human revision loop: edits, alternate concepts, back-and-forth messages. A builder converts that revision loop into a pre-purchase preview, which removes the seller's labour *and* raises conversion, because the buyer commits only once they've already seen themselves.

## 4.2 Who is actually buying (and what it implies)

**From [RoseApparelCrafts' custom kids neon shirt](https://www.etsy.com/listing/4311458472/) — 68 item reviews:**
- *"The shirts were perfect, **my grandkids** looked adorable."* · *"Cute Halloween gift for **my granddaughters**"* · *"Not cheap t-shirts… Colors are brilliant! **My granddaughters** are going to love these"* · *"The shirts are adorable! **Purchased 3 shirts—grandchildren** look so cute in them!"* · *"Great shirts — **bought for a group camping trip and everyone loved them**!"*

**From [Lalalagiftland's personalized tote](https://www.etsy.com/listing/1083855409/) — 1,828 item reviews:**
- *"**My grand babies** loved them and they can be **used year after year**!!"* · *"**I ordered 3** trick or treat bags for 3 girls."* · *"**I bought 3 of these for my kids last year**… so **i reordered for this year**!"* · *"Gift for my best friend's kids!"* · *"**I ordered too late for Halloween**, but couldn't resist for next year!"*

**PATTERN:** three buyer facts that should shape every product decision here.
1. **Grandparents are a dominant hidden buyer** for personalized kids' Halloween goods — and they buy for *multiple* grandchildren at once.
2. **Multi-unit is the norm, not the exception** ("I ordered 3", "purchased 3 shirts"). Any builder should support a *set* in one order.
3. **This is an annual repeat purchase** ("I buy one every year", "reordered for this year", "used year after year"). A year field and an asset library that ages well are worth more than a clever one-off joke.

## 4.3 Missing-option and representation signals

| Signal observed | Source | What it implies for the schema |
|---|---|---|
| Buyer must describe *hair and hats* in prose | GloryParty reviews | Hair style + hair colour + hat/costume must be **pickable**, not typed |
| Buyer asks for an edit after seeing the proof | pawfectpixco reviews | Live preview eliminates the single largest support cost |
| Seller offers "two options to choose from" and buyers love it | pawfectpixco reviews | Offer 2–3 art directions as an option, not just one fixed style |
| "Written just how I typed it" praised as a feature | GloryParty reviews | Text accuracy is a trust signal — echo the typed names back in the preview |
| Pets named alongside people throughout | OrnamentallyYouGifts description; `custom family ornament with dog and cat` | Pets are **first-class cast members**, not an add-on toggle |
| Family titles requested (Daddy, Mommy, Nana, Papa, Aunt, Uncle, Bubba, Sissy) | TheTeeStudio description | Offer a **title picker** as well as a free name field |
| No reviewer anywhere asked for skin tone in words | all listings read | Consistent with `personalized ornament skin tone` → **[NONE]**. Skin tone is not a stated demand; it is an unstated expectation whose absence quietly costs sales. Build it, don't headline it. |

**FACT-check on that last row, stated plainly:** I did **not** find a review anywhere in this study saying "I wish I could choose our skin tones." I am not going to manufacture one. What I found is (a) no search demand for the phrase, and (b) a category whose entire emotional promise is "this is *us*" being delivered by products where the cast is either a fixed cartoon or a typed name. **RECOMMENDATION:** treat skin tone, hair and body type as *table-stakes fidelity features inside* the builder — the thing that makes the preview feel like the family — and market the concept on the family-and-pets cast, which *is* searched.

---

# PART 5 — Gaps, scoring and selected opportunities

## 5.1 Gap types

**Audience** (nobody speaks to this group) · **Wording** (right group, wrong words) · **Style** (right idea, wrong visual language) · **Product** (proven concept not carried to another format) · **Combination** (two proven things nobody has joined) · **Timing** (demand in an ignored window) · **Need** (a job the buyer is trying to do that no listing names — strongest, because it is confirmed on both Etsy and Google).

## 5.2 Scoring (1–10 each, /60)

| Rank | Gap | Proven Etsy demand | Google search demand | Emotional value of personalization | Customization depth & relevance | Market whitespace | Ease in Teeinblue/Customily | **Total** |
|---|---|---|---|---|---|---|---|---|
| 1 | **Halloween family + pets character-builder ORNAMENT** | 8 | 8 | 9 | 10 | 9 | 9 | **53** |
| 2 | **Family + pets character-builder MATCHING APPAREL SET** | 9 | 8 | 9 | 10 | 8 | 7 | **51** |
| 3 | **Grandparent "Little Monsters" — one character per grandchild** | 9 | 9 | 9 | 8 | 6 | 8 | **49** |
| 4 | **Owner + dog duo, breed-ILLUSTRATED (not photo)** | 8 | 7 | 9 | 8 | 7 | 9 | **48** |
| 5 | **Sibling trick-or-treat SET builder (one character per child)** | 9 | 7 | 8 | 7 | 5 | 9 | **45** |
| 6 | **Halloween couple builder (2 characters + optional pet)** | 7 | 6 | 8 | 8 | 7 | 9 | **45** |
| 7 | **Halloween family MUG builder (wrap-around cast)** | 6 | 6 | 7 | 8 | 8 | 9 | **44** |
| 8 | **Baby's First Halloween character keepsake (ornament + bodysuit)** | 8 | 7 | 9 | 6 | 5 | 8 | **43** |
| 9 | **Teacher / classroom "Boo Crew" — a character per student** | 7 | 7 | 7 | 8 | 7 | 6 | **42** |
| 10 | **Skin-tone / representation as a standalone concept — search demand 2/10, forced to bottom** | 4 | **2** | 9 | 9 | 8 | 8 | **40** |

**Ranking rules applied.** #5 and #6 tie at 45; #5 ranks higher on Google demand (7 vs 6). #10 scores 38/50 on its other five criteria — it would otherwise sit mid-table — but `personalized ornament skin tone` returns **no Google suggestions at all**, so per the brief it is forced to the bottom and must not be built as its own product. *Honourable mention, not scored in the top 10:* workplace/office team builder (character + role per coworker) — strong whitespace, but high per-order admin and weaker emotional pull than family.

## 5.3 Master opportunity table

| Rank | Target Customer | Existing Products/Designs | Etsy Evidence | Search Evidence | Gap Type | New Personalized Design Concept | Product Type | Suggested Price | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Households (2–8 people) with named pets who keep a Halloween tree or a keepsake shelf | Names-only ghost-family ornaments; no appearance choice anywhere | [OrnamentallyYouGifts](https://www.etsy.com/listing/1747606360/) "Ghost Family With Pets" $14.99, **2 item reviews**; [PrintFairyMomma](https://www.etsy.com/listing/4549574164/) $19.35, 459 shop sales; [BetterHandcraft](https://www.etsy.com/listing/4551958817/) 1,673 sales — **all names-only**. Christmas analogue [GloryParty](https://www.etsy.com/listing/1106986178/) **2,456 item reviews / 180,318 sales** at $19.99 | `custom family ornament with pets` → "**with dog and cat**", "with dog"; `personalized halloween ornaments` → "custom halloween ornaments" | **Need** | **"The Boo Crew, Est. 2026"** — build your household as costumed ghosts: 2–8 human characters + unlimited pets, each with costume, skin tone, hair, name; family surname + year | Ceramic / acrylic hanging ornament (2-sided) | **$18–$24** (single); $32–$40 for a 2-pack | 53 |
| 2 | Families doing coordinated Halloween outfits, incl. the dog | Character promised, never enumerated | [BlinkStudioCrafts](https://www.etsy.com/listing/4535084597/) is the **only** listing with published options (40) — and has **48 sales**; [TheTeeStudio](https://www.etsy.com/listing/4550055738/) **143,112 sales** with characters undefined; [BlueDiamondTees](https://www.etsy.com/listing/4529961127/) **53,482 sales**, zero options documented | `family halloween costume with dog` → "**and baby**", "**two dogs**", "**Addams family… with dog**"; PAA on family+dog costumes; `personalized halloween family portraits` | **Combination** | **"Our Crew" matching set** — same cast rendered across adult tee, youth tee, toddler tee and infant bodysuit, each garment showing the *whole* family | Tee · sweatshirt · youth · bodysuit (sold as a set) | $22–$28 adult · $18–$22 youth · **set of 4: $78–$92** | 51 |
| 3 | Grandmothers/grandfathers with 2–6 grandchildren | "Grandma's Little Monsters" with typed names on a fixed graphic | [Luvilooom](https://www.etsy.com/listing/1770068151/) 2,435 shop reviews; [SingleLadyTee](https://www.etsy.com/listing/1756830632/) 6,100; [HappyBdayBoutique](https://www.etsy.com/listing/4545315180/) 239; [ScorpioBoy doodle characters](https://www.etsy.com/listing/4531946106/) 196 — doodles are fixed | **Five** autocomplete variants of `personalized grandma shirts with grandkids names`; `personalized halloween shirt` → "**personalized grandma halloween shirt**" | **Audience** | **"Grandma's Little Monsters"** — one *chosen* monster costume per grandchild (2–6), each with skin tone, hair and name; grandparent-title picker (Grandma/Nana/Mimi/Gigi/Abuela/Oma/Papa/Pop) | Sweatshirt (hero) + tee + mug | $28–$34 sweatshirt · $22–$26 tee · $18–$21 mug | 49 |
| 4 | Dog and cat parents who want an *illustration*, not a photo, of their specific animal | Split between photo-upload tees and "choose your breed" typed into a text box with the breed list never shown | [ChupchupShop](https://www.etsy.com/listing/4546290531/) "20+ breeds" — breed is **not** a dropdown, 6,232 sales; [HuynhByCreatorsUS](https://www.etsy.com/listing/4534308317/) 3,981 sales, same problem; photo route: [GoodEnergyShirts](https://www.etsy.com/listing/4540072629/), [PixelThreadAlchemy](https://www.etsy.com/listing/4551893525/) | `personalized halloween shirt` → "**personalized dog halloween shirt**"; PAA "pet portrait generator free"; `custom family portrait with pets` deep set | **Style** | **"Me & My Ghoul"** — owner character + pet, illustrated: species → breed (40+) → coat colour → costume; owner gets skin tone, hair, costume | Tee · sweatshirt · mug · ornament | $24–$29 tee · $19–$22 mug · $18–$22 ornament | 48 |
| 5 | Parents & grandparents buying for 2–4 children at once | Single-name canvas totes at $3.95–$15 | [Lalalagiftland](https://www.etsy.com/listing/1083855409/) **1,828 item reviews**; [TeeTeeOutfit](https://www.etsy.com/listing/4346792179/) **104**; [VizzBee](https://www.etsy.com/listing/4376329154/) **59**; reviews say *"I ordered 3"*, *"my grand babies"*, *"reordered for this year"* | `personalized trick or treat bag` → "**with names**", "**bulk**", "for kids" | **Product** | **"Trick-or-Treat Crew" sibling set** — one costumed character per child, art coordinated across the set so the bags read as a family when photographed together | Canvas tote multi-pack (2/3/4) | $16–$19 each · **set of 3: $42–$48** | 45 |
| 6 | Couples, incl. newlyweds and couples with a pet | Ghost/skeleton couples with names + year | [ShopCleverly](https://www.etsy.com/listing/4539617880/) $27.02, 158; [HolidayOrnamentCo](https://www.etsy.com/listing/1780362655/) 2,199; Christmas analogue [CaDoKoShop couple-with-dog](https://www.etsy.com/listing/4390659734/) **29 item reviews**, 80,867 sales | `personalized halloween couple` → "custom halloween couple"; `custom family portrait with pets` | **Combination** | **"Creepin' It Real Since ____"** — two characters, appearance-built, optional pet, custom year | Ornament · tee pair · mug | $18–$22 ornament · $44–$52 tee pair | 45 |
| 7 | Families wanting a daily-use keepsake rather than apparel | Names-only family mugs; the biggest seller charges $26.97 for names | [SunsetStores colour-change](https://www.etsy.com/listing/4544701207/) $26.97, 39,381 sales, names only; [RojoCreativeStudio](https://www.etsy.com/listing/4363889807/) $25.00, 241 sales | `custom halloween mug` → "custom halloween mugs", "**custom halloween cups**" | **Product** | **"Home Is Where the Boos Are"** — the full cast wrapped 360° around the mug, which no chest print can do | 11oz / 15oz mug, optional colour-change | $19–$24 (11oz) · $24–$29 (15oz / colour-change) | 44 |
| 8 | New parents and grandparents marking a first Halloween | Year-stamped name ornaments and bodysuits | [ApparelByMoliva](https://www.etsy.com/listing/4528864724/) 7,889 sales; [Qatasta](https://www.etsy.com/listing/4529724314/) ⭐Bestseller, 18,947 sales | `personalized halloween` → "gifts", "book"; `personalized halloween gifts` → "**for kids**" | **Timing** | **"First Boo, 2026"** — baby character (skin tone, hair wisp, costume) + parents + pet, as a matched ornament-and-bodysuit gift box | Ornament + infant bodysuit set | $34–$42 as a set | 43 |
| 9 | Teachers and school staff | Personalized name/grade/room tees | [TheTeeStudio gothic teacher](https://www.etsy.com/listing/4546172780/) $19.99; [FanTeeCreations](https://www.etsy.com/listing/4554912541/) 1,900 shop reviews; [ACTrendyStudio group tees](https://www.etsy.com/listing/4555238829/) 818 | `teacher halloween shirt` head term is strong; **note** `personalized teacher halloween shirt` returns **[NONE]** — personalize inside the head term | **Combination** | **"Miss ____'s Little Ghouls"** — teacher character + up to 25 named mini-ghosts | Sweatshirt · tote · mug | $30–$36 sweatshirt · $22–$26 tote | 42 |
| 10 | — **DO NOT BUILD AS A CONCEPT** — | Representation-forward "choose your skin tone" positioning | No Etsy listing owns it; no reviewer asked for it | `personalized ornament skin tone` → **[NONE]** | Style | Fold skin tone, hair and body type **into** concepts 1–9 as fidelity features; never as the product's headline or title keyword | — | — | 40 |

---

## 5.4 Detailed breakdowns — Top 5

---

### #1 — "The Boo Crew, Est. 2026" — Family + Pets Character-Builder Ornament
**Gap type: Need · Score 53/60**

**What currently exists**
FACT: Halloween family ornaments are an active, healthy category and **every single one I inspected personalizes names only**. [OrnamentallyYouGifts' "Ghost Family With Pets"](https://www.etsy.com/listing/1747606360/) ($14.99, 16,742 shop sales) asks for "your family's names and the names of your pets" — the ghosts themselves are fixed art. [PrintFairyMomma](https://www.etsy.com/listing/4549574164/) ($19.35), [BetterHandcraft](https://www.etsy.com/listing/4551958817/) ($14.24), [DomDomGift](https://www.etsy.com/listing/4554387919/) ($10.19), [NativeGreenWood](https://www.etsy.com/listing/4541976068/) ($12.33), [StudioCutee](https://www.etsy.com/listing/4555349205/) ($11.99), [ChristmasDecorationX](https://www.etsy.com/listing/4549045672/) ($9.54) — same story. The best-selling one in the set has **2 item reviews**.

**What customers actually need**
The buyer's job is *"make an object that is unmistakably my household."* Names on generic ghosts get maybe 40% of the way there. FACT: the identical job, one season later, is served by a $19.99 ornament with **2,456 item reviews** and 180,318 shop sales ([GloryParty](https://www.etsy.com/listing/1106986178/)), where buyers type out appearance details in prose and reviewers coach each other — *"Be sure to be specific to all hair hat etc.."* Halloween has the same households, the same tree (the Halloween tree is a real and growing decor format), and none of the product.

**Search evidence**
FACT: `custom family ornament with pets` → "custom family ornament with dog" · "custom family christmas ornament with pets" · "**personalized family ornament with dog and cat**" · "custom family christmas ornament with dog". `personalized halloween ornaments` → "custom halloween ornaments" · "personalized halloween decor". `personalized halloween` → basket · bag · bucket · **gifts** · decor. `family halloween costume with dog` → "**with dog and baby**" · "**with two dogs**" · "Addams family halloween costume with dog", with PAA asking *"What are some cute Halloween costumes I can wear with my dog?"*

**Proposed concept**
A two-sided ceramic or acrylic ornament showing your household as a line-up of costumed Halloween characters — every human and every pet built by the buyer, with the family surname and year on a banner. The product promise in the first image is: **"Build your crew. See it before you buy it."**

**Specific target audience**
Primary: mothers 30–48 who already own a Halloween tree or a seasonal keepsake shelf and who post the family Halloween photo every year. Secondary: grandparents buying one per grandchild household (Part 4 proves grandparents buy in multiples). Tertiary: newlyweds and new-pet households marking a "first".

**Design direction**
Cute-doodle, not gothic: rounded silhouettes, thick warm outline, flat colour, so assets stay legible at 3 inches. Palette pulled from the winning Halloween POD range — pumpkin orange, bone cream, deep aubergine, moss, matte black. Each character is a **ghost-sheet-with-a-costume-on-top** device: the sheet standardises the silhouette (which keeps 8 characters visually coherent) while the costume, hair and face carry the identity. Pets get the same treatment at 60% scale.

**Suggested wording**
- "The ____ Boo Crew · Est. 2026"
- "Our Crew Got Spookier · 2026"
- "Home Is Where the Boos Are"
- "____ Family · Haunting Since ____"
- "Party of 5 (plus 2 very good boys)"

**Suggested products**
Hero: 3-inch two-sided ceramic ornament. Then acrylic (cheaper tier), a 2-pack (one for the grandparents), and — using the identical asset library — the mug and tee at #2 and #7.

**Suggested price**
$18–$24 single; $32–$40 for a 2-pack. FACT-anchored: the Christmas benchmark sells at $19.99 with 2,456 reviews, and Halloween's names-only ornaments already reach $19.35–$20.84 — so this price is *proven at lower value delivered*.

**Sales-content angle — 3 hooks**
1. *"Name-only ornaments are lazy. Build your actual crew — including the dog."* — a side-by-side of a generic ghost trio vs. a built one.
2. *"Every year the family photo changes. So should the ornament."* — leans on the FACT that this is an annual repeat purchase (*"I buy one every year"*).
3. *"Pick the costume. Pick the hair. Pick the dog's breed. See it before you buy it."* — a 10-second screen recording of the builder, which is the single strongest differentiator against every competitor listing in the category.

**Customization schema**

*Editable fields*
| Field | Type | Range |
|---|---|---|
| Number of humans | stepper | 1–8 |
| Per human: role/title | dropdown | Mom · Dad · Mama · Papa · Grandma · Nana · Mimi · Gigi · Abuela · Oma · Grandpa · Pop · Auntie · Uncle · Sister · Brother · Bubba · Sissy · Me · (custom text) |
| Per human: costume | thumbnail picker | 12 options (below) |
| Per human: skin tone | swatch row | 8 tones |
| Per human: hair style | thumbnail picker | 12 styles |
| Per human: hair colour | swatch row | 10 colours |
| Per human: name | text, 12 chars | — |
| Number of pets | stepper | 0–3 |
| Per pet: species | dropdown | Dog · Cat · (Rabbit · Bird as v2) |
| Per pet: breed | dropdown | 40 dog / 24 cat |
| Per pet: coat colour | swatch row | 8 |
| Per pet: name | text, 10 chars | — |
| Family surname | text, 14 chars | — |
| Year | dropdown | 2026 / 2027 / none |
| Banner phrase | dropdown | 5 preset phrases |

*Option sets*
- **Costumes (12):** ghost · witch · vampire · skeleton · mummy · pumpkin · black cat · devil · Frankenstein · werewolf · bat · grim reaper. *(FACT: this list is drawn from what BlinkStudioCrafts already publishes and what the top-selling Halloween graphics actually depict — it is not invented.)*
- **Skin tones (8):** an even ladder from very fair to deep, each with a matched line-work colour so outlines never muddy on deep tones. This is the fidelity feature that makes the preview land; it is deliberately **not** a title keyword (see false gaps).
- **Hair (12 styles × 10 colours):** short crop · buzz · short curls · bob · long straight · long wavy · long curly/coily · ponytail · bun · braids · locs · bald/none. Colours: black · dark brown · brown · light brown · auburn · red · blonde · platinum · grey · fun colour.
- **Dog breeds (40):** golden retriever · labrador · french bulldog · german shepherd · poodle · husky · dachshund · beagle · corgi · shih tzu · chihuahua · yorkie · boxer · rottweiler · doberman · great dane · pit bull/staffy · border collie · australian shepherd · cocker spaniel · cavalier · pug · bulldog · schnauzer · maltese · pomeranian · bernese · st bernard · shiba inu · basset hound · greyhound · whippet · jack russell · mini pinscher · samoyed · newfoundland · weimaraner · vizsla · mixed-breed (short coat) · mixed-breed (long coat).
- **Cat breeds (24):** black domestic shorthair · orange tabby · grey tabby · brown tabby · tuxedo · calico · tortoiseshell · white · ragdoll · maine coon · siamese · persian · bengal · scottish fold · sphynx · russian blue · british shorthair · norwegian forest · birman · abyssinian · burmese · devon rex · american shorthair · mixed.

*How the live preview should work*
1. **Step 1 — Crew size.** One question: how many people, how many pets. Everything downstream scales from this. The canvas immediately draws placeholder silhouettes so the buyer sees the composition before doing any work.
2. **Step 2 — One character at a time.** Character 1 is highlighted on the canvas; the panel shows only that character's five controls. Tapping a thumbnail updates the ornament instantly. A "copy from previous character" button matters more than it sounds — siblings usually share skin tone and hair colour, and it cuts the work for a family of six by half.
3. **Step 3 — Pets**, same pattern.
4. **Step 4 — Text.** Surname, year, banner phrase, and each character's name shown in position so the buyer can catch a spelling error themselves. Echo the typed text back verbatim — FACT: *"Written just how I typed it"* is praised as a feature in the benchmark's reviews.
5. **Auto-composition:** the engine spaces and scales the cast so a party of 8 never crowds; humans anchor the baseline, pets sit forward at 60%.
6. **Final gate:** a full-size render with a "this is exactly what will be printed" confirmation before add-to-cart. This is the step that kills the revision loop documented in Part 4.
7. **On Etsy specifically:** publish the numbered, illustrated option menus as listing images 3–8, collect picks in the personalization box in a fixed format (`Char1: 04 / Skin 3 / Hair 07 / Brown / "Mia"`), and put the live preview on your own storefront. Etsy is the discovery channel; the preview is the conversion channel.

*What stays fixed (to protect design quality)*
Layout, character spacing and scale · the ghost-sheet silhouette device · outline weight and the ornament's shape and border · the typeface and the banner geometry · the background scene (moon, fence, pumpkins) · the colour palette itself — buyers pick *from* swatches, never a free colour picker. Character count is capped at 8 humans + 3 pets, because past that the ornament stops reading at 3 inches and the product's quality promise breaks.

---

### #2 — "Our Crew" — Family + Pets Character-Builder Matching Apparel Set
**Gap type: Combination · Score 51/60**

**What currently exists**
FACT: the two shops with the most Halloween "custom character" volume define **no character options at all** — [TheTeeStudio](https://www.etsy.com/listing/4550055738/) (143,112 sales, "choose a different Halloween character for every family member", characters never listed) and [BlueDiamondTees](https://www.etsy.com/listing/4529961127/) (53,482 sales, description contains no options). The single listing with a real published matrix — [BlinkStudioCrafts](https://www.etsy.com/listing/4535084597/), 10 girl + 10 boy costumes + 10 cat + 10 dog breeds — has **48 lifetime sales and 8 shop reviews**.

**What customers actually need**
A family buying four garments needs the *cast to be identical across all four* and the *sizes to differ*. Today they must re-type the whole cast into four separate personalization boxes and trust that the seller keeps them consistent. That is both a conversion killer and the seller's biggest error source.

**Search evidence**
FACT: `family halloween costume with dog` returns a nine-deep set including "**with dog and baby**", "**with two dogs**", "**Addams family halloween costume with dog**", plus PAA *"What are some popular family Halloween costume ideas?"* and related *"Family Halloween Costumes with dog and baby"*. `personalized family halloween` → "**personalized halloween family portraits**" · "custom family halloween costumes". `boo crew shirt` → "**boo crew shirts family**".

**Proposed concept**
Build the cast once; buy the whole family's garments in one cart. Adult tee, youth tee, toddler tee and infant bodysuit all carry the *same* full-family artwork — which is what makes the group photo work.

**Specific target audience**
Households of 3–7 with at least one child under 12 and at least one pet, doing a pumpkin patch / trunk-or-treat / school parade circuit. Secondary: grandparents buying the adult garments to match.

**Design direction**
Same asset library as #1, re-laid-out for a chest print: a single horizontal row for ≤5 characters, a two-row stack for 6–8, with the surname banner beneath. Comfort Colors garment-dyed blanks in Yam, Pepper, Ivory, Blue Jean, Moss — the colourways already proven across the category.

**Suggested wording**
"The ____ Boo Crew" · "Our Crew Got Spookier · 2026" · "Trick-or-Treat Crew, Est. ____" · "____ Family Haunt · 2026" · role words printed under each character (Daddy · Mommy · Bubba · Sissy · Nana · the dog's name).

**Suggested products**
Adult tee and crewneck, youth tee, toddler tee, infant bodysuit — sold individually and as a 3/4/5-garment bundle with one shared design.

**Suggested price**
$22–$28 adult · $18–$22 youth · $16–$19 toddler/bodysuit · **4-garment set $78–$92.** FACT-anchored: BlinkStudioCrafts already asks $22.89 for a single tee with this level of choice, and TheTeeStudio reaches $31.09.

**Sales-content angle — 3 hooks**
1. *"Build the crew once. Everyone's shirt matches."* — the one-cart promise.
2. *"Yes, the dog is on the shirt. Pick the breed."* — this is the searched phrase and the emotional hook in one line.
3. *"Family of 3? Family of 8? Same builder."* — mirrors the "up to 20 members" positioning that earned FunnyDaisy 1,264 reviews at Christmas.

**Customization schema**
Identical field set and option sets to #1, plus: **Garment** (tee · crewneck · youth · toddler · bodysuit), **Size**, **Garment colour** (10 curated), **Layout** (auto: single row ≤5, two rows 6–8), and a **"same design, different sizes" bundle builder** that carries one saved cast across every garment in the cart.
*Preview:* the cast is built once on a garment mockup; switching garment or size re-renders the same cast, so the buyer sees the family line-up as it will actually print. *Fixed:* print size and placement, row logic, typeface, character scale ratios, and the curated garment-colour list (no arbitrary colours — dark art on dark garments is the most common quality failure in this category).

---

### #3 — "Grandma's Little Monsters" — one chosen character per grandchild
**Gap type: Audience · Score 49/60**

**What currently exists**
FACT: this is one of the most commercially proven phrases in the entire Halloween niche and it is served almost entirely by typed names on a fixed graphic — [Luvilooom](https://www.etsy.com/listing/1770068151/) (2,435 shop reviews), [SingleLadyTee](https://www.etsy.com/listing/1756830632/) (6,100), [HappyBdayBoutique](https://www.etsy.com/listing/4545315180/) (239), [BaoBrianDesign](https://www.etsy.com/listing/4546087218/) (1,400), [VYBRACO](https://www.etsy.com/listing/4553345426/) (95). The closest thing to depth is [ScorpioBoy's "Cute Doodle Characters"](https://www.etsy.com/listing/4531946106/) (2,545 shop sales) — where the doodles are **fixed and the buyer only supplies names**.

**What customers actually need**
A grandmother with five grandchildren does not want five identical monsters with different names on them. She wants the loud one to be the werewolf and the shy one to be the little ghost. That is the whole emotional transaction, and no listing currently permits it.

**Search evidence**
FACT — the deepest validated phrase set in this report: `personalized grandma shirt with grandkids` returns **personalized grandma shirts with grandkids names · personalized grandma t shirts with grandkids names · women's personalized grandma shirts with grandkids names · grandma shirts with grandkids names · shirts with grandkids names**. And `personalized halloween shirt` itself returns "**personalized grandma halloween shirt**" as a top-8 suggestion.

**Specific target audience**
Women 55–75 with 2–6 grandchildren, buying for themselves to wear at the school parade or trunk-or-treat; and adult children buying it *for* her as a gift (Part 4 shows the grandparent-as-buyer pattern in reverse too).

**Design direction**
Warm, soft, slightly retro. A grandparent character on the left, then a row of little monsters at 70% scale, names beneath each. Sweatshirt-first — FACT from the wider category: October is cold and the crewneck is the garment that gets worn all season.

**Suggested wording**
"Grandma's Little Monsters" · "My Favorite Boos Call Me ____" · "Nana's Boo Crew" · "These Little Monsters Call Me Mimi" · "Grandma of Ghouls, Est. ____"

**Suggested products**
Crewneck sweatshirt (hero), tee, mug. All three share one cast.

**Suggested price**
$28–$34 sweatshirt · $22–$26 tee · $18–$21 mug. FACT-anchored: names-only versions already sell at $8.50–$16.94, so a built version supports a genuine premium.

**Sales-content angle — 3 hooks**
1. *"Five grandkids, five different monsters — not five name tags."*
2. *"She'll tell you which one is which. Every single time she wears it."*
3. *"Nana, Mimi, Gigi, Abuela, Oma — pick her name too."* — the title picker is itself a hook, because the current market forces "Grandma".

**Customization schema**
*Editable:* grandparent title (18 presets + custom) · grandparent character (skin tone, hair style, hair colour, glasses on/off, costume from the 12) · number of grandchildren (1–8) · per child: costume, skin tone, hair style, hair colour, name (12 chars) · optional "and the grandpups" pet row (0–2, species/breed/coat/name) · optional Est. year.
*Preview:* build grandparent first, then children left to right in birth order, with drag-to-reorder — because grandmothers *will* want them in the right order, and getting it wrong is the one thing that would make this product fail emotionally. "Copy previous child" for siblings.
*Fixed:* the grandparent-left / children-right composition, the 70% child scale, spacing, typeface, and the arch of the title lockup.

---

### #4 — "Me & My Ghoul" — Owner + Pet, breed-illustrated
**Gap type: Style · Score 48/60**

**What currently exists**
FACT: Halloween pet personalization splits into exactly two unsatisfying routes. **Route A — photo upload:** [GoodEnergyShirts](https://www.etsy.com/listing/4540072629/) ($22.40, 796 sales), [PixelThreadAlchemy](https://www.etsy.com/listing/4551893525/) ($18.40, 3,981 sales), [SupraApparel](https://www.etsy.com/listing/4546647851/). **Route B — breed typed into a text box:** [ChupchupShop](https://www.etsy.com/listing/4546290531/) advertises "20+ Custom Breeds" but breed is **not a variation dropdown** and the breed list appears nowhere in the listing; [HuynhByCreatorsUS](https://www.etsy.com/listing/4534308317/) doesn't mention breed selection in its description at all.

**What customers actually need**
A designed garment that looks like it was *drawn for them*, featuring an animal that is recognisably theirs — without a photograph printed on their chest, and without having to trust that "goldendoodle, apricot" typed into a box will come back right. And increasingly the owner wants to be in the picture too: FACT, `custom family portrait with pets` returns a full suggestion set, and PAA on that query includes *"How can I create my own custom pet portrait?"*

**Search evidence**
FACT: `personalized halloween shirt` → "**personalized dog halloween shirt**". `custom family portrait with pets` → "personalized family portrait with pets" · "**custom family portrait with dog**" · "pets are family members". PAA on `personalized family portrait with pets` includes "**Pet portrait generator free**" — direct evidence people are looking for a *generator*, not an artist. **Caution (FACT):** `custom halloween shirt with dog` and `custom dog breed halloween` both fail — the latter resolves to dog *costumes*. Title with "personalized dog halloween shirt".

**Specific target audience**
Dog and cat parents 25–45 who treat the pet as family, buy Halloween gear for the animal already, and would rather have an illustration than a photo tee. Strong secondary: partners and adult children buying it as a gift.

**Design direction**
One owner character and one pet, standing together, retro halftone or clean doodle depending on the sub-line. The pet must be *breed-legible at a glance* — ear shape, muzzle length, coat texture and tail carriage do more work than colour. Costumes on both.

**Suggested wording**
"Me & My Ghoul" · "My Familiar" (witch/cat line) · "Boo Crew, Party of 2" · "Spooky Season with ____" · "Certified Ghoul Parent"

**Suggested products**
Tee and crewneck (hero), mug, and the ornament using the same two-character render.

**Suggested price**
$24–$29 tee · $30–$36 crewneck · $19–$22 mug · $18–$22 ornament. FACT-anchored: photo-upload competitors already charge $18.40–$32.99, so an illustrated version at $24–$29 is not a stretch.

**Sales-content angle — 3 hooks**
1. *"Not a photo on a shirt. An actual drawing of your actual dog."*
2. *"40 breeds. 8 coat colours. Pick yours and watch it change."*
3. *"Every dog-mom shirt on Etsy is the same generic ghost dog. This one is yours."*

**Customization schema**
*Editable:* owner (skin tone, hair style, hair colour, costume from the 12, name) · pet species · **breed (40 dog / 24 cat)** · coat colour (8) · pet costume (witch hat · pumpkin collar · ghost sheet · bat wings · devil horns · skeleton · none) · pet name · optional second pet · phrase.
*Preview:* breed picker is a **searchable thumbnail grid**, not a dropdown — buyers scan for the silhouette that matches their dog, and this is where the conversion happens. Coat swatches re-tint the breed illustration live. Show the pet at final print size so the buyer can judge the likeness before committing.
*Fixed:* the two-figure composition and their relative scale, the breed artwork line-work itself (only the coat re-tints), costume anchor points, typeface, and print placement. Coat colours must be swatch-constrained — a free colour picker on an animal produces unusable results and is the fastest way to generate refunds in this category.

---

### #5 — "Trick-or-Treat Crew" — Sibling Tote Set Builder
**Gap type: Product · Score 45/60**

**What currently exists**
FACT: the personalized trick-or-treat tote is one of the highest-volume proven products in Halloween POD — [Lalalagiftland](https://www.etsy.com/listing/1083855409/) **1,828 item reviews**, 84,880 shop sales, Bestseller; [TeeTeeOutfit](https://www.etsy.com/listing/4346792179/) **104 item reviews** at $3.95, Bestseller; [VizzBee](https://www.etsy.com/listing/4376329154/) **59 item reviews**, Bestseller; [SmyrnaDesignUS](https://www.etsy.com/listing/4366864956/) **26 item reviews**, 37,689 sales. **All of them personalize a name and, at most, a font or a colour.**

**What customers actually need**
FACT, straight from those reviews: *"I ordered 3 trick or treat bags for 3 girls"* · *"I bought 3 of these for my kids last year… so i reordered for this year"* · *"My grand babies loved them and they can be used year after year"* · *"Purchased 3 shirts—grandchildren look so cute in them"*. The purchase is **already a set purchase**, and the market is selling it one bag at a time with one name on it. Siblings want to be different from each other *and* to look like they belong together — which is precisely what a shared art system with per-child characters delivers.

**Search evidence**
FACT: `personalized trick or treat bag` → "personalized trick or treat bags **with names**" · "**for kids**" · "custom trick or treat bags **bulk**" · "personalized trick or treat bucket" · "personalized trick or treat tote". The word "bulk" appearing in autocomplete is the multi-unit intent showing up in search exactly as it does in the reviews.

**Specific target audience**
Parents and — critically — **grandparents** of 2–4 children. Part 4 shows grandparents named as the buyer in review after review on precisely this product type.

**Design direction**
One costumed character per bag, large and centred, with the child's name beneath, and a shared background/border treatment so the three bags photograph as a set. Natural canvas with one or two ink colours keeps unit cost low at a $16–$19 price point.

**Suggested wording**
"____'s Loot" · "Trick-or-Treat Crew" · "Feed Me Candy" · "____, Certified Ghoul" · "Boo Crew · 2026"

**Suggested products**
Canvas tote (hero), sold singly and as 2/3/4-packs; a matching sticker sheet as a low-cost add-on; the same characters carried onto the ornament from #1 as a natural upsell.

**Suggested price**
$16–$19 each · **set of 3 at $42–$48.** RECOMMENDATION with a caveat: the incumbent price band is $3.95–$15.00, so this is a deliberate premium repositioning justified entirely by the builder. Test the 3-pack price first; if it resists, hold the per-bag price at $13–$15 and win on set economics rather than unit margin.

**Sales-content angle — 3 hooks**
1. *"Three kids, three different monsters, one matching set."*
2. *"They'll use it every year until they're too cool for it."* — quoting the reviewers' own "used year after year".
3. *"Grandma's favourite order: one bag per grandchild."* — names the hidden buyer out loud.

**Customization schema**
*Editable:* number of bags (1–4) · per bag: child's name (10 chars), costume (from the 12), skin tone, hair style, hair colour · shared: background treatment (3 options), ink colourway (4 options), optional year.
*Preview:* show all bags in the set **side by side on one canvas** — the set is the product, so the preview must show the set, not one bag at a time. Per-bag tabs for editing, with the group view always visible.
*Fixed:* bag size and print area, character scale and placement, name typeface and baseline, the shared border/background system, and the ink colourway list (2-colour maximum, which is what keeps the price point viable).

---

## 5.5 Evidence-strength summary

| Opportunity | Etsy evidence | Google evidence | Both? | Personalization depth |
|---|---|---|---|---|
| #1 Family+pets ornament builder | ✅ strong (active category, all names-only; Christmas analogue at 2,456 item reviews) | ✅ strong (`with dog and cat`, `custom halloween ornaments`) | ✅ | **H** — 300+ combos from ~50 assets |
| #2 Family+pets apparel set | ✅ very strong (143k- and 53k-sale shops promising characters with no system) | ✅ strong (`with dog and baby`, `with two dogs`, PAA) | ✅ | **H** |
| #3 Grandparent grandkid builder | ✅ very strong (multiple 2k–6k-review shops on names alone) | ✅ very strong (5 autocomplete variants) | ✅ | **H** |
| #4 Owner + pet breed-illustrated | ✅ strong (breed claimed but never selectable; photo route thriving) | ✅ moderate–strong (`personalized dog halloween shirt`, "pet portrait generator free") | ✅ | **H** |
| #5 Sibling tote set | ✅ very strong (1,828 + 104 + 59 + 26 item reviews; multi-unit quotes) | ✅ moderate (`with names`, `bulk`) | ✅ | **M–H** |
| #6 Couple builder | ✅ moderate | ⚠️ moderate | ✅ | **H** |
| #7 Family mug builder | ✅ moderate (biggest seller = names only at $26.97) | ⚠️ moderate | ✅ | **H** |
| #8 First Halloween keepsake | ✅ strong | ⚠️ moderate | ✅ | **M** |
| #9 Teacher classroom builder | ✅ moderate | ⚠️ head-term only (personalized variant returns [NONE]) | partial | **H** but admin-heavy |
| #10 Skin tone as a concept | ❌ nobody owns it | ❌ **[NONE]** | ❌ | — |

## 5.6 Two honest caveats

**FACT, restated because it changes execution:** none of the ten listings whose rendered DOM I inspected contains an embedded Teeinblue, Customily, Zakeke, Kickflip or InkyBay preview. On Etsy, the builder cannot live on the listing page. Everything above is designed to work in the realistic split — illustrated numbered option menus in the listing images, picks captured in the personalization box, artwork auto-rendered by the customizer in your back office, and the true live preview hosted on your own storefront that Etsy traffic can graduate to.

**FACT, on the limits of this evidence:** Halloween's item-level review counts reset annually. Most 2026 listings — even inside shops with 100k+ lifetime sales — currently show 0–20 item reviews. That is why this report leans on shop lifetime sales, Bestseller badges, and the Christmas analogue for volume proof, and why a new seller publishing now is not competing against 2,000 reviews. They are competing against a listing that also has zero.

---

## Final answer

**"If I could choose only ONE concept to create from this entire research project, I would choose…"**

**…#1 — "The Boo Crew, Est. 2026": the Halloween family-and-pets character-builder ornament.**

**Audience specificity.** This is not "people who like Halloween." It is a household of a specific size, with specific pets, that already buys a keepsake every October — and the evidence that they exist in volume is not speculative. FACT: the exact same household, eight weeks later, buys a Christmas ornament with the same cast structure from a listing carrying **2,456 item reviews** and a shop with **180,318 sales**. I do not have to guess whether people will personalize a multi-character keepsake with their pets in it; I can see them doing it 2,456 times on one listing. What I also see is that on the Halloween side of the same shelf, the best-selling equivalent has **2 item reviews** and personalizes nothing but names.

**Emotional weight.** An ornament is the highest-emotion, lowest-utility object in this entire category, and that is exactly why it wins. Nobody needs it. They buy it because it is a *record* — "this was our household in 2026, and the dog was still with us." That reading is supported directly by the reviews: *"I buy one every year"*, *"Perfect for new family's 1st Christmas"*, *"can be used year after year."* Names on a generic ghost cannot carry that. A cast that actually looks like the family can. And the annual-repeat behaviour means one satisfied buyer is a decade-long customer with a growing cast — a new baby, a new dog — each of which is a reason to re-order.

**Customization depth.** This concept is the deepest of the ten and the only one that hits 10/10 on both depth and relevance. Eight humans × 12 costumes × 8 skin tones × 12 hair styles × 10 hair colours, plus up to three pets × 64 breeds × 8 coat colours, plus titles, names, surname and year. Crucially, **every one of those options changes the artwork rather than decorating it** — which is the brief's own test. And none of it is arbitrary: the costume list and the breed lists are lifted from what [BlinkStudioCrafts already publishes](https://www.etsy.com/listing/4535084597/), so the option architecture is validated even though that shop's traffic is not.

**Market opportunity.** The whitespace here is not a hunch, it is a measurement. Every Halloween family ornament I inspected — seven of them, across shops from 253 to 3,392 reviews — personalizes names only. The one Halloween listing on Etsy with a genuine published character matrix has **48 lifetime sales**. Meanwhile the shops with 143,112 and 53,482 sales are selling the *words* "custom character" with no system behind them. That is a category where the winning move is not out-marketing anyone; it is simply being the first to actually build the thing everyone is already promising.

**Speed of designing and publishing.** This is the decider. A 3-inch flat ceramic print has no sizing, no fit risk, no size-based returns, no garment-colour interaction, and the smallest possible asset set — because at 3 inches you need clean silhouettes, not detail. I can draw one ghost-sheet base and layer 12 costumes, 12 hairstyles and 8 skin swatches on top of it, and the same library then powers the tee (#2), the grandparent shirt (#3), the mug (#7) and the tote set (#5) with zero additional artwork. It is the cheapest possible entry into the deepest possible product. And the timing is right in front of us: FACT, it is 20 August 2026, Halloween listings for this season are live and still accumulating their first reviews, and — the part most sellers miss — **the identical asset library converts to a Christmas family-and-pets ornament in November, walking straight into the 180,318-sale market that proved the concept in the first place.**

One caveat I will state plainly rather than bury: the Halloween-specific version of this product has **not** been proven to sell at depth by anyone, because nobody has built it. My confidence comes from the adjacent-season analogue and from the fact that the shallow Halloween versions already sell at $19.35–$20.84 while delivering far less. That is a strong inference, not a measurement. The right response is to launch the ornament first — cheap, fast, low-risk — and let its first fifty orders tell you whether to build the apparel set behind it.

---

### Appendix — sources

All Etsy data was read from live pages on **etsy.com** (US locale, USD) on 20 August 2026; individual listings are linked inline throughout Parts 1, 3 and 5 in the form `https://www.etsy.com/listing/<id>/`. Variation option sets, personalization fields and descriptions were read from the rendered listing DOM; item-level review counts from each listing's `aggregateRating` block and confirmed against the on-page "Item average (N reviews)" label; shop lifetime sales and shop review counts from each seller's shop page. Google autocomplete was read from `google.com/complete/search` (client=chrome, hl=en, gl=us); People Also Ask and "People also search for" blocks from live `google.com/search` result pages, US region, same date.
