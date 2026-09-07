# Halloween POD Market Research — Etsy (US) + Google Validation

**Researcher:** POD market research pass
**Marketplace:** Etsy.com, US locale, USD (currency forced to USD/en-US/US region for this session)
**Data captured:** 20 August 2026 (≈10 weeks before Halloween — Etsy Halloween listings for 2026 are already live and already accumulating reviews)
**Method:** Direct Etsy search-result and listing-page scraping in-browser + Google Autocomplete (`/complete/search`), People Also Ask and "People also search for" blocks read from live Google SERPs.

---

## 0. How to read this report (methodology + honesty notes)

Every number below was read off a live page. Nothing is estimated, modelled or invented. Three things you must understand about the numbers, because most Etsy research gets this wrong:

**FACT — the star rating and review count shown on an Etsy *search results card* is the SHOP's rating and lifetime review count, not the listing's.** A card reading "4.9 (12.5k)" means the shop has 12,500 reviews across all products, not that the t-shirt does.

**FACT — listing-level ("item") review counts were obtained separately** by opening each listing page and reading the `aggregateRating` block. Where a listing has zero item reviews, Etsy falls back to publishing the shop's aggregate in that block. I verified this behaviour manually on two listings (one where the two numbers differed — item 21 vs shop 5,798 — and one where they matched exactly, where the page read *"Be the first to review this item / No reviews yet"*). Any listing below marked `item reviews = 0` was detected by that fallback rule.

**FACT — shop lifetime sales counts** ("33,674 Sales") were read from each seller's shop page. This is the single most reliable public volume signal on Etsy. Etsy does not publish per-listing sales.

Labels used throughout:

- **FACT** — directly observed on the page, reproducible today.
- **PATTERN** — my reading of repeated facts across many listings.
- **RECOMMENDATION** — my judgement about what to make. Not evidence.

**Verification pass:** every shop-sales figure and every item-review count quoted below was re-fetched a second time before publishing this report and matched. Shop sales counters are live and tick upward continuously — on re-check, three shops had each gained 1–3 sales in the space of the session (OldSchoolCulture 94,253→94,256; MojoSticker 191,637→191,638; ValenTeenoDesign 107,470→107,472). Treat all sales figures as "at least this many, as of 20 Aug 2026."

Prices are the **sale price displayed on 20 Aug 2026**. Etsy POD sellers run near-permanent discounts (20–70% off), so treat the "original price" as anchoring, not as a real price point.

---

# PART 1 — Multi-layer scan of the Halloween niche on Etsy

I scanned 40+ distinct search queries across six layers: core keywords, priority product categories, audience sub-segments, occasions/roles, slogans and style aesthetics, and "gift for ___" phrasing. Findings are grouped by cluster.

---

## Layer A — Core Halloween keyword ("halloween shirt", "halloween sweatshirt")

**What is selling (FACT — titles observed on page 1 of `halloween shirt`):**

- Comfort Colors® is in roughly half of all titles. It is functioning as a *keyword*, not just a blank.
- Retro/vintage 70s–90s treatments: "Vintage Halloween VHS Shirt", "Halloweentown Est 1998", "Vintage Horror Characters Abbey Road", "Retro 'Tis The Season".
- Cute-spooky character mashups: cute ghost + pumpkin + black cat, "Monster Mash", "Kitty Biscuits", skeleton goose, spooky frog on a scooter, "Bring Candy or Else" Mothman.
- Meme/viral piggybacks: Jimothy the Seattle raccoon appears on shirts AND ornaments; "I Got A Rock" (Charlie Brown); "Stay Weird" raccoon.
- Licensed-adjacent: Halloweentown, Hocus Pocus ("I Smell Children", "Midnight Margaritas"), Nightmare Before Christmas, Mickey's Not So Scary, Harry Potter ("Hagrid's Pumpkin Patch"), Freddy/Jason.

**Target customer (PATTERN):** women 25–45 buying for themselves, described in titles as "Women's Halloween Shirt", "Gift For Her". Oversized/relaxed fit is called out constantly.

**Main product types:** Comfort Colors 1717 tee, crewneck sweatshirt, hoodie, "baby tee" (cropped, 80s-inspired), embroidered crewneck (a clear premium tier).

**Aesthetic preferences (PATTERN):** garment-dyed muted colourways (sand, moss, yam, pepper); distressed/faded halftone print; single large centre-chest graphic; cream/black/orange palette; a fast-growing pink "coquette" counter-current.

**Typical price range (FACT):** $6.99–$45 sale price; the dense middle is **$13–$25**. Embroidered items sit $17–$51.

**Competition level:** **Extreme.** `halloween shirt` returns "1,000+ items with ads" and roughly one in three page-one slots is a paid ad. Do not enter on the head term.

**Volume evidence (FACT):** OldSchoolCulture — **94,253 lifetime sales**; IvyCustomShirt — **154,154 sales**; TheTeeStudio — **143,112 sales**; TruePassionStyles — **108,392 sales**; ValenTeenoDesign — **107,470 sales**; MojoSticker — **191,637 sales**. Halloween POD on Etsy is a six-figure-unit category for the top ~50 shops.

---

## Layer B — Priority product categories

### B1. T-shirts / sweatshirts / hoodies
Covered above. Hoodie-specific search surfaces a distinct sub-format: **front-and-back / shoulder-to-shoulder prints** ("Retro Halloween Skeleton Hoodie, Spooky Season Front-Back Design", "Shoulder-to-Shoulder Print On The Back Halloween Hoodie"). Price band $6–$55. Competition high.

### B2. Mugs
**FACT — what's on page 1:** the category splits cleanly in two.
- **3D/sculpted novelty mugs** — witch cauldron mugs, haunted-house cauldron mugs, embossed ghost mugs. $19–$31. These are sourced, not designed — high barrier for a pure POD seller.
- **Flat-print personalised ghost mugs** — "Personalized Ghost Halloween Mug, Cute Halloween Mug, Best Friends Gift" ($13.50, CaDoKoShop, **80,863 shop sales**); "Halloween Ghost Coffee Mug" ($12.96, DYCustomDesigns, **64,696 sales**, 26 item reviews).
- **Profanity/dark-humour mugs** — "I Like Spooky Things & The Word F**k Mug" ($22, Untamedegoshop, 11.2k shop reviews).

**Target customer:** gift-buyer (best friend, coworker, bestie) more than self-purchase. **Price range:** $5–$32, dense at **$12–$20**. **Competition:** moderate — noticeably thinner than tees.

### B3. Tote bags
**FACT — page 1 of `halloween tote bag` is ~90% personalised kids' trick-or-treat bags.** "Personalized Halloween Tote Bag: Custom Trick or Treat Canvas Bag" (Lalalagiftland, $8.24, **1,828 item reviews**, 84,880 shop sales, Bestseller badge). "Custom Name Halloween Tote Bag" (TeeTeeOutfit, $3.95, **104 item reviews**, Bestseller).
**PATTERN:** the adult/aesthetic Halloween tote (bat print, gothic market bag) is a thin minority. The bookish Halloween tote is the one adult segment that IS well served (see D5).
**Price range:** $3.95–$31. **Competition:** high on personalised kids' bags; moderate on adult aesthetic totes.

### B4. Stickers
**FACT:** sticker sheets and party-favour label sets dominate. "Halloween Treats Sticker Sheet" ($3.99, PaperliciousbySu, 10 item reviews, 19,499 shop sales); "Personalized Halloween Stickers, Cute Kids Halloween Labels, Classroom" ($6.75, ThePinkLemonStore); "Halloween Planner Stickers" (Bloomplanners, 14.4k shop reviews); "Ghost Reading Stickers" (ArtsyLegacy, $3.49, **285 item reviews**).
**PATTERN:** two distinct buyers — (a) the *party host / teacher* buying labels in bulk, (b) the *journaller / reader* buying a single die-cut for a Kindle, planner or reading journal.
**Price:** $1.11–$11.53, dense at **$3–$7**. **Competition:** moderate; low barrier, low ticket.

### B5. Posters / wall art
**FACT:** vintage-illustration and gothic-painting styles lead — "Vintage Headless Horseman Wall Art", "Vintage Black Cat Trick or Treat Poster", "Girly Gothic Halloween Wall Art Set". Snoopy/Peanuts Halloween art appears. $9.96–$36.46.
**Competition:** moderate. **PATTERN:** buyers want *sets* (2–4 prints) for a gallery wall, not single prints.

### B6. Hats
**FACT:** two totally separate products share the keyword.
- **Costume witch hats** (quilted, celestial, personalised, embroidered) — $14.99–$27.99; TinyBarns' "Custom Name Halloween Witch Hat" at $4.99 with **69,811 shop sales**.
- **Embroidered baseball caps** (jack-o'-lantern, minimalist ghost) — $7.79–$14.99. Thin, and the most POD-accessible sub-format here.

### B7. Hanging ornaments
**FACT:** the "Halloween tree" is a genuine, growing decor format on Etsy — "Mini Halloween Ornaments For Small Tree" (Donfash, $6.59, Bestseller, 8 item reviews), "Gothic Dark Academia Halloween Christmas Tree Shatter Proof Ornaments — Bat" (TheGreyHouseshop, $6.05, **126 item reviews**, Bestseller).
**PATTERN — the Halloween ornament market is overwhelmingly *keepsake*, not *decor*:** "Personalized Baby First Halloween Ornament 2026", "First Halloween Married Ornament", "Custom Pet Halloween Ornament / Pet Memorial". Personalised ceramic/acrylic flat-print ornaments are pure POD and priced $2.70–$24.
**Competition:** **lowest of all seven priority categories.** Shops here are small (ApparelByMoliva 7,889 sales; TheGreyHouseshop 6,307; Donfash 3,418) versus 100k-sale apparel shops.

---

## Layer C — Audience sub-segments

### C1. Teachers
**Selling:** "I Smell Children" (Hocus Pocus), "Trick or Teach", ghost-holding-books, "school supplies" doodle tees, personalised name tees, "Boo Crew"/grade-team matching sets, teacher totes with 5 chosen icons.
**Target:** K–5 teachers buying for themselves + parents buying *for* the teacher.
**Products:** tee, sweatshirt, tote, sticker sheets, ornaments, mugs (thin — see gaps).
**Aesthetic:** cute-not-scary; ghost + books + pencils; sage/cream/black Comfort Colors.
**Price:** $5.60–$22.95 tees; $4.79–$26.99 totes.
**Competition:** **Extreme.** **Volume evidence (FACT):** IvyCustomShirt 154,154 sales; MojoSticker 191,637 sales; ValenTeenoDesign's ghost-reading sweatshirt alone has **1,417 item reviews**.

### C2. Nurses & healthcare
**Selling:** "Boo Boo Crew", "Code Boo", "Trick or Treatment", pain-scale-with-pumpkins, ghost-in-scrubs, "Trach or Treat" (respiratory therapists), NICU-specific ("caring for the spookiest littles").
**Sub-roles already served on Etsy (FACT):** NICU, pediatric, ER, school nurse, vet tech, dental hygienist/dental office, respiratory therapist, paraprofessional, school counselor/psychologist, bus driver.
**Price:** $6.25–$29.99. **Competition:** high and rising — this is where 2024–25 POD sellers went.

### C3. Dog moms / cat moms / pet parents
**Selling:** "Boo-p" (a ghost dog going "boop") is the runaway concept of 2026 — I found **five different shops** running near-identical Boo-p listings. Breed-specific variants (dachshund, corgi, German shepherd, 20+ breeds). "Kitty Biscuits" (cat making biscuits, in a Halloween bakery scene). Skeleton dog. Custom pet-photo ghost tees.
**Price:** $6.95–$34.66. **Competition:** high, and concept-cloning is rampant.
**Volume evidence (FACT):** FastShirtPrint 10.7k shop reviews; TripletsDesignParty 37,896 sales; 22ndOfOctober 10.8k shop reviews.

### C4. Matching family / couples / groups
**Selling:** skeleton family sets, personalised "Boo Crew" with names, Mickey & Minnie couple tees (LemEmotion and Kosall both carry Bestseller badges), "Her Boo / His Boo", Disney Not-So-Scary trip tees, "Trunk or Treat Crew".
**Price:** $5.95–$68. **Competition:** high on family, moderate on couples, **noticeably lower on workplace/coworker groups**.

### C5. Grandparents
**Selling:** "Grandma's Little Boos", "Grandma's Little Monsters", "Grandma's Pumpkin Patch", all personalised with grandkids' names; Mimi/Nana/Gigi variants.
**FACT:** KiwiPicks' personalised grandma shirt has **16 item reviews**, 40,998 shop sales. **Competition:** high; the concept is fully mined.

### C6. Bookish / librarians
**Selling:** ghost reading a book (the single most-reviewed individual listing I found in this entire niche), "Support Your Local Haunted Library", "All Booked For Fall", "Keep The Candy I Will Take The Books", "Read More Books" ghost, Sleepy Hollow dark-academia crewnecks.
**Products:** tee, sweatshirt, tote, mug, sticker, bookmark, ornament, bookshelf figurine — **this is the only sub-niche where all seven priority product types are already populated**.
**Price:** $2.99–$30. **Competition:** high on apparel, moderate elsewhere.
**Volume evidence (FACT):** ValenTeenoDesign ghost-reading sweatshirt **1,417 item reviews**; ArtsyLegacy ghost reading sticker **285 item reviews**; CuppaTeeClothing 65,050 sales.

---

## Layer D — Occasions, roles and life events

### D1. Baby's first Halloween
**Selling:** "My First Halloween" bodysuits, "Little Boo", personalised name rompers, ghost/pumpkin onesies, plus **ornament keepsakes** ("Personalized Baby First Halloween Ornament 2026").
**Price:** $5.69–$30. **Competition:** high on bodysuits, **moderate on ornaments**.
**FACT:** Qatasta's personalised baby romper carries a Bestseller badge (18,947 shop sales).

### D2. Halloween pregnancy announcement
**Selling:** skeleton-baby-in-belly x-ray graphic (dominant), "There's A Skelly In My Belly", "Growing a Little Pumpkin", couple/matching announcement sets, "Spooky Mama".
**FACT — the strongest single proof point in the whole occasion layer:** BashVibesUS "Skeleton Halloween Maternity Shirt, Funny Pregnancy Announcement 2026" — **448 item reviews**, 4.9★, $12.39, 40,058 shop sales.
**Price:** $8.75–$34. **Competition:** high on the skeleton x-ray; the graphic is essentially commoditised.

### D3. Halloween birthdays
**Selling — kids:** personalised name+age pumpkin/ghost tees, "Spooky One" first-birthday matching family sets, Disney Halloween birthday.
**Selling — adults:** thinner. "Ghouls Gone Wild" 30th birthday, "Spooky Since 1996", "50th Birthday Halloween Shirt", "October Girl" birthday tees (which sit in a *separate* birthday-month niche, not the Halloween niche).
**Price:** $5.99–$25. **Competition:** high kids, **moderate adults**.

### D4. Weddings / newlyweds
**Selling:** "First Halloween Married" ornaments, ghost bride & groom keepsakes, Mr & Mrs spooky baubles. $2.70–$20.97. **Competition:** moderate. Volume shops are small (ChristmasDecorationX 10,360 sales; HolidayOrnamentCo 14,796).

### D5. Boo baskets (the October equivalent of an Easter basket, gifted between adults and to kids)
**FACT — Etsy page 1 for `halloween boo basket` and `boo basket for him` is:** personalised kids' candy baskets/buckets ($6.90–$26.40), assembled physical gift boxes ($28–$88.50), and candles. Almost nothing POD, and almost nothing addressed to an adult partner.
This is the largest disconnect between Etsy supply and Google demand that I found. See Part 2 and Part 5.

---

## Layer E — Phrases and slogans currently printed on products

**FACT — recurring printed copy observed across listings:**

| Slogan / phrase | Where it lives |
|---|---|
| Spooky Season / Spooky Vibes / Stay Spooky | universal |
| 'Tis The Season (with ghost-pumpkin-skeleton trio) | tees, sweatshirts — at least 5 shops |
| Boo Crew / Boo-Boo Crew / Office Boo Crew | family, nurses, workplace |
| Boo-p (ghost dog "boop") | dog-mom tees — 5+ shops |
| Trick or Teach | teachers (shirt, sweatshirt, mug, tumbler) |
| Trick or Treatment / Code Boo / Trach or Treat | nurses, RTs |
| I Smell Children | teachers |
| Ghouls Just Wanna Have Fun / Ghouls Night Out / Let's Go Ghouls | women's group |
| Midnight Margaritas / "put the lime in the coconut" | Practical Magic fans |
| Halloweentown Est. 1998 / Halloweentown University | 90s nostalgia |
| I Got A Rock | Charlie Brown meme |
| Don't Ghost Your Feelings | school counselors, mental health |
| Keep The Candy I Will Take The Books | bookish |
| All Booked For Fall | bookish |
| Support Your Local Murder (a "murder" of crows) | witchy/dark humour |
| Kitty Biscuits | cat people |
| Dadcula / Momster / Mombie / Spooky Mama | parents |
| Howdy Halloween / cowboy ghost | western |
| Hot Ghoul Summer / Summerween / Slasher Summer | off-season (June–August) |

### Community-specific language (would be opaque to an outsider)
**FACT:** "Boo-p" (dog people), "kitty biscuits" (cat people — kneading), "trach or treat" (respiratory therapists), "para" (paraprofessional), "TBR"/"book club girlies" (BookTok), "Jimothy" (viral Seattle raccoon), "Summerween" (Gravity Falls-derived, now a real July–August shopping moment), "boo basket" (Halloween gift basket), "trunk or treat" (church/school parking-lot event), "murder" (collective noun for crows).

---

## Layer F — Design styles trending in this niche (PATTERN)

1. **Retro/vintage halftone** — faded 70s–90s print, muted palette. The default winning style.
2. **Coquette / pink Halloween** — bows on pumpkins and ghosts, pastel pink + black. Fastest-growing aesthetic; PoppyRosePrintCo (57,172 sales) and ShirtsEverAfterLLC (20.6k shop reviews) both run it.
3. **Cottagecore / dark academia** — haunted library, bookshelves, candles, moths, ravens, mushrooms.
4. **Western / cowboy ghost** — "Howdy Halloween", ghost on horseback, rodeo skeletons.
5. **VHS / video-nasty** — fake VHS spine, tracking lines, "Fright Night".
6. **Embroidery** — a distinct premium tier ($17–$51) that visually separates from flat DTG.
7. **Meme-jacking** — raccoons, geese, frogs, capybaras wearing Halloween costumes.
8. **Front + back / shoulder-to-shoulder placement** — used to justify a higher hoodie price.

---

## Layer G — "Gift for ___" phrasing observed in titles (FACT)

gift for her · gift for horror fans · gift for teacher · gift for book lover · gift for librarian · gift for dog mom · gift for cat mom · gift for corgi mom · gift for dachshund mom · gift for coworker · gift for best friend / bestie / work bestie · gift for grandma / mimi / nana · gift for new mom · gift for nurse / RN / vet tech / dental assistant · gift for bus driver · gift for pregnant wife · secret santa gift (on the Jimothy ornament) · employee appreciation gift · teacher appreciation gift · hostess gift.

**PATTERN:** the highest-volume Halloween POD listings are **not** costume products. They are *identity gifts* — the buyer is saying "I know exactly who you are" via an occupation, a pet, a hobby or a life stage, with Halloween as the seasonal wrapper.

---

# PART 2 — Validation against real Google search demand

Method: Google Autocomplete via `google.com/complete/search` (client=chrome, hl=en, gl=us) — this returns the actual suggestion set Google serves, which is a direct proxy for query volume. Plus People Also Ask (PAA) and "People also search for" blocks read from live US SERPs.

**Rule applied:** if a phrase returns `[NONE]` or returns suggestions about a *different* intent (e.g. costumes when we want shirts), it does not count as validated demand for a product.

## 2.1 Autocomplete results (FACT — verbatim)

| Seed query | Google suggestions returned |
|---|---|
| `halloween shirt for` | for women · **for pregnant women** · for boys · for men · for kids · for girls · for dogs · for toddler boy · for mom · for cat · for baby · **for pregnancy** |
| `halloween shirt ideas for` | for adults · for kids · for women · **for work** · **for teachers** · for couples · for men · **for groups** · for cricut · for family |
| `teacher halloween shirt` | ideas · svg · costumes · nearby · **math teacher** · funny · cute · t shirts · **preschool teacher** · **teacher team halloween shirts** |
| `nurse halloween shirt` | ideas · amazon · near me · svg · costume shirt · tops · **er nurse** · **nicu nurse halloween shirt** · funny · **school nurse halloween shirt** |
| `nicu nurse halloween` | **nicu nurse halloween shirt** · costume · costume ideas · … |
| `school nurse halloween` | **school nurse halloween shirt** · door ideas · bulletin board ideas · costumes · … |
| `pediatric nurse halloween` | **pediatric nurse halloween shirts** · costumes · … |
| `respiratory therapist halloween` | **respiratory therapist halloween shirts** · costume · … |
| `paraprofessional halloween` | costumes · **paraprofessional halloween shirts** · … |
| `daycare teacher halloween` | costume ideas · costumes · **gift** · **daycare teacher halloween shirt** · preschool teacher gift ideas |
| `work halloween shirt` | work halloween shirts · work shirt halloween costume · halloween work shirt ideas · **office halloween shirts** · office halloween shirt ideas · **work appropriate halloween shirts** · social work halloween shirts · funny work halloween shirts |
| `office halloween shirt` | office halloween shirts · ideas · **work halloween shirts** · **dental office halloween shirts** · **medical office halloween shirts** · post office · **office staff halloween shirts** · funny |
| `group halloween shirts` | **for work** · for adults · **for teachers** · funny · ideas · **company halloween shirts** · band · group t shirts · **etsy group halloween shirts** · candy |
| `matching halloween shirts` | family · **friends** · kids · adults · nearby · near me · **for work** · disney · couples · couples for adults |
| `boo basket` | **ideas** · **for men** · for kids · **for boyfriend** · **for girlfriend** · **for women** · **stuffers** · **ideas for women** · **for wife** · ideas for girlfriend |
| `boo basket for adults` | for adult daughter · ideas for adults · **fillers for adults** · halloween boo baskets for adults · for girlfriend · for boyfriend · for kids · for men |
| `boo basket for him` | ideas · diy · cheap · valentines · **gifts for him** · halloween boo basket for him · **stuffers for him** · **items for him** |
| `boo basket for wife` | ideas · **for pregnant wife** · fall · for woman · how to make · **what goes in a boo basket for wife** · **what to put in boo basket for wife** |
| `boo basket for husband` | diy · for my husband · halloween boo basket for husband · **items for husband** · for your husband · **for men ideas** |
| `boo basket stuffers` | for kids · **for women** · **for men** · for teens · **for adults** · for toddlers · **for him** · near me |
| `teacher halloween gift` | gifts · **gift ideas** · gift tags · gifts for students · gift card holder · gift bag · **gifts from parents** · **gift basket** · gift card · gift tag free |
| `halloween mug for teacher` | **halloween cups for teachers** · halloween mugs near me |
| `personalized halloween mug` | personalized halloween mugs · personalised halloween mug · **personalized halloween cups** · personalized halloween coffee mugs |
| `trick or teach` | **trick or teach shirt** · printable · svg · png · flag · trick or teacher · **t shirt** · **sweatshirt** |
| `bookish halloween` | decor · costumes · **shirts** · wallpaper · costume ideas · blanket · quotes · crafts · **stickers** · **gifts** |
| `book club halloween` | **ideas** · costumes · costume ideas · **party** · **reads** · **theme** · snacks · activities |
| `spooky season` | movies · **sweatshirt** · meme · **shirt** · embroidery design · … |
| `coquette halloween` | costumes · wallpaper · decor · nails · background · **shirt** · costume ideas · pfp · blanket · png |
| `trunk or treat shirt` | **trunk or treat shirts** · **shirt ideas** · trick or treat shirt · design · women · target · kids · **trunk or treat t shirt** |
| `halloween ornaments for tree` | nearby · diy · amazon · near me · walmart halloween tree ornaments · halloween decorations for tree · … |
| `personalized halloween ornament` | **personalized halloween ornaments** · **custom halloween ornaments** · personalized halloween decorations |
| `october birthday shirt` | october birthday shirts · **ideas** · **for women** · october birthday t shirts · t shirt design |
| `halloween 30th birthday` | **party** · **ideas** · **theme** · cake · invitations · card · … |
| `ghouls gone wild` | blu ray · youtube · **bar crawl** · **halloween bar crawl** · kings island · **shirt** · tampa |
| `summerween` | **summerween 2026** · movies · **decor** · date · nails · **books** · **party** · gravity falls |
| `grandma halloween shirt` | old lady halloween shirt · **personalized grandma halloween shirt** · grandma halloween t shirts · grandma hubie · grandma and grandpa halloween shirts |
| `custom halloween shirt` | custom halloween shirts · custom shirt design · **personalized halloween shirts for kids** · **for adults** · costume · custom disney · custom dog |
| `sensory friendly halloween` | **costumes** · events near me · activities · events · costumes for toddlers · costumes kids · treats · ideas · party · costume ideas |
| `sober halloween` | **events near me** · events · party · costumes · activities · party near me · party ideas · ideas · meme · nyc |
| `pet memorial halloween` | pet **cemetery** halloween decorations · pet cemetery halloween ideas · … · pet memorial near me · pet memorial gifts near me |
| `ghouls night out` | rochelle · lagoona · spectra · fabric · ghoulia · clawdeen · **monster high** · mtg · venus · lyrics |
| `halloween shirt for coworkers` | **[NONE]** |
| `halloween gifts for coworkers` | **[NONE]** |
| `halloween shirt with kids names` | **[NONE]** |
| `halloween shirt for book lovers` | **[NONE]** |
| `halloween reading shirt` | **[NONE]** |
| `halloween shirt for social worker` | **[NONE]** |
| `halloween shirts for healthcare workers` | halloween shirts near me (i.e. no real depth) |
| `halloween shirt for grandma` | **[NONE]** (but `grandma halloween shirt` word-order DOES return suggestions) |
| `work appropriate halloween` | **costumes** (women / for guys / for groups) · makeup · jokes · movies |
| `tbr halloween` | the halloween tree · the halloween movies · … (no BookTok intent) |
| `halloween bookmark` | halloween bookmarks · ideas · **printable** · craft · printable free · **to color** · diy · for kids |

## 2.2 People Also Ask + related searches (FACT — verbatim from live SERPs)

**Query: `boo basket ideas for women`**
- PAA: *"What goes in a boo basket for adults?"* · *"What are some unique gift basket ideas for a woman?"* · *"What are some ideas for a spooky basket for my girlfriend?"* · *"What are good basket ideas for adults?"*
- People also search for: Unique boo basket ideas for women · Diy · Christmas boo basket ideas for women · nearby · amazon · **Boo basket ideas for adults** · **for wife** · **for boyfriend**

**Query: `teacher halloween gift ideas`**
- PAA: *"What can a teacher be for Halloween?"* · *"What gifts do teachers really want?"* · *"What are some unique gift ideas for teachers?"* · *"What to put in a treat bag for teachers?"*
- People also search for: **from parents** · pinterest · diy · amazon
- Note: Etsy's own `/market/halloween_gifts_for_teachers` page ranks on page 1 — Google is already sending this query to Etsy.

**Query: `matching halloween shirts for work`**
- PAA: *"What are some fun Halloween ideas for the workplace?"* · *"What are good duos for Halloween?"* · *"What will be the most popular Halloween costume in 2026?"* · *"Where can I find Halloween shirts?"*
- People also search for: **Women** matching halloween shirts for work · **funny** · **adults** · amazon · **Men** · Kids
- Etsy's `/market/work_team_halloween_tshirts` ranks page 1.

**Query: `nicu nurse halloween shirt`**
- PAA: *"What is a good gift for a NICU nurse?"* · *"What to wear as a nurse on Halloween?"* · *"How to show appreciation for NICU nurses?"* · *"What are some ideas for a gift basket for a NICU nurse?"*
- People also search for: Women · amazon · Men

**Query: `bookish halloween gifts`**
- PAA: *"What are some unique bookish gifts?"* · *"What are some good bookish Halloween costumes?"* · *"What are some unique Halloween-themed gifts?"* · *"What are some good bookish gifts that are not books?"*
- People also search for: **Bookish halloween gifts for adults** · amazon
- Etsy's `/market/halloween_bookish_gifts` ranks page 1.

## 2.3 REAL GAPS — search demand exists, Etsy does not serve it well

| # | Phrase family | Search evidence | Etsy supply reality |
|---|---|---|---|
| R1 | **boo basket for him / wife / husband / boyfriend / girlfriend / adults + boo basket stuffers** | 5 separate seed queries all return deep suggestion sets; PAA explicitly asks *"What goes in a boo basket for adults?"* and *"What to put in boo basket for wife"* | Page 1 = kids' personalised candy totes, or fully assembled physical gift boxes at $28–$88.50. Essentially **zero** POD items (mug/tee/tote) titled as an adult boo-basket stuffer for a partner |
| R2 | **work appropriate halloween shirts / office halloween shirts / office staff halloween shirts** | `work halloween shirt` autocomplete returns "work appropriate halloween shirts"; `halloween shirt ideas for` returns "for work"; PAA asks about workplace Halloween ideas | Searching `work appropriate halloween shirt` on Etsy returns **generic** Halloween tees; no listing is written around "subtle enough for the office" |
| R3 | **matching halloween shirts for work / group halloween shirts for work / company halloween shirts** | `group halloween shirts` → "for work", "company halloween shirts", "etsy group halloween shirts"; `matching halloween shirts` → "for work"; PAA + 6 related searches | Etsy has ~4 real workplace-group listings on page 1 (SellItAgainDesigns 1.1k, Studio73G 210, PuguTeeDesign 228, BellaArtisanDesign 3k) vs **hundreds** for teacher/family. Under-supplied relative to demand |
| R4 | **teacher halloween gift(s) / halloween cups for teachers / trick or teach mug** | `teacher halloween gift` returns a 10-deep suggestion set including "gifts from parents"; `trick or teach` returns "shirt", "t shirt", "sweatshirt" — but for mugs the only suggestion is "halloween cups for teachers" | Teacher Halloween **shirts and totes are saturated**; teacher Halloween **mugs** on Etsy are mostly listings created in the last few weeks with 1–75 shop reviews. Real product-format gap |
| R5 | **bookish halloween stickers / gifts + book club halloween** | `bookish halloween` → "stickers", "gifts", "shirts"; `book club halloween` → ideas, party, reads, theme; PAA: *"bookish gifts that are not books"* | Bookish Halloween **apparel and totes are saturated**. But the *reading-ritual* artefacts buyers describe in reviews (reading journal, Kindle, plan book, book-club matching sets) are barely addressed |
| R6 | **halloween ornaments for tree / personalized halloween ornaments / custom halloween ornaments** | All three return real suggestion sets | Etsy ornaments are ~90% baby / couple / pet keepsakes. Adult *identity* ornaments (nurse, healthcare, book lover, "first Halloween as a teacher") are thin, and the shops in this category are 10–20× smaller than apparel shops |
| R7 | **ghouls gone wild bar crawl / halloween bar crawl** | `ghouls gone wild` autocomplete returns "bar crawl", "halloween bar crawl", "shirt" | Etsy has **one** dedicated pub-crawl matching listing on page 1 (HomeStoryCollective, 167 shop reviews) plus adjacent drinking tees |
| R8 | **october birthday shirts for women / halloween 30th birthday** | `october birthday shirt` → "for women", "ideas"; `halloween 30th birthday` → party, ideas, theme, invitations | Etsy Halloween-birthday supply skews hard to toddlers/kids; the adult milestone-birthday-in-October crossover is thin |
| R9 | **halloween shirt for pregnant women / pregnancy + boo basket for pregnant wife** | `halloween shirt for` returns *both* "for pregnant women" and "for pregnancy"; `boo basket for wife` returns "for pregnant wife" | Etsy is saturated with the *skeleton-in-belly* graphic aimed at the pregnant woman. It is **not** serving the person actually buying — partners, mothers, aunts (see Part 4 reviews) |
| R10 | **daycare / preschool teacher halloween gift** | `daycare teacher halloween` returns both "gift" and "shirt" | Etsy teacher supply is K–12-coded ("classroom", "grade team"); daycare/preschool-specific language is comparatively rare |

## 2.4 FALSE GAPS — do not build these

| Idea | Why it fails |
|---|---|
| **"Ghouls Night Out" as a standalone concept** | Autocomplete for `ghouls night out` is **100% Monster High dolls** (Rochelle, Lagoona, Spectra, Clawdeen, Ghoulia). The search intent is toys, not apparel. Etsy has plenty of these shirts and the phrase looks busy — but Google says the traffic isn't there for apparel. Classic false positive. |
| **Sober Halloween apparel** | Etsy supply is genuinely thin (several listings with <25 shop reviews) which *looks* like whitespace. But `sober halloween` autocomplete is entirely **events/parties/costumes near me** — people are searching for something to *do*, not something to *wear*. |
| **Pet memorial Halloween ornaments** | `pet memorial halloween` autocomplete redirects to "pet **cemetery** halloween decorations" (i.e. yard decor). Genuine pet-memorial demand exists year-round but is not Halloween-coded. Etsy already has these listings and they are not the volume drivers. |
| **Sensory-friendly Halloween apparel** | Strong search demand — but 10/10 suggestions are **costumes, events and activities**, not shirts. A POD tee cannot deliver on "sensory friendly" credibly (seams, tags and fabric are the product, not the print). |
| **"Halloween shirt for coworkers" / "halloween gifts for coworkers" as literal keywords** | Both return `[NONE]`. The demand is real but only under the *"office/work/group"* word order (R2/R3). Title your listings accordingly. |
| **"Halloween reading shirt" / "halloween shirt for book lovers" as literal keywords** | Both `[NONE]`. Use **"bookish halloween"** — that phrase is fully validated. Wording, not concept, is the issue. |
| **"Halloween shirt with kids names"** | `[NONE]`. Buyers search "**personalized** halloween shirts for kids/adults" and "**custom** halloween shirt". |
| **TBR / BookTok slang on Halloween products** | `tbr halloween` returns Ray Bradbury's *The Halloween Tree*. The slang does not carry search volume outside the platform it lives on. |
| **"Halloween shirt for grandma"** | `[NONE]` in that word order — but `grandma halloween shirt` works and returns "personalized grandma halloween shirt". A pure word-order trap, and the concept is already saturated on Etsy. |
| **Summerween / Halloween in July as a *gap*** | Search demand is real ("summerween 2026", "summerween party/decor"). But Etsy already has a healthy Summerween apparel market (SugarChip 837, WayabaShirts 1.3k, PrimeTeeGifts 1.4k, CherryBlossomCoUS Bestseller). Validated, **not** a gap — file it as an off-season revenue extension instead. |
| **NICU / paraprofessional / respiratory therapist as *gaps*** | Search demand is genuinely validated for all three. But Etsy has already caught up hard — 12/12 results on page 1 are on-target with shops at 3k–20k reviews. Validated **and** saturated. |

---

# PART 3 — Listings with proven sales signals (30 listings)

Selection filter: Bestseller badge, "Popular now" flag, high item-level review count, high shop lifetime sales, or a concept repeated across ≥3 successful independent shops.

Reminder on columns: **Item rev** = reviews on that specific listing. **Shop rev / Shop sales** = the seller's lifetime totals (the volume proof). Price = sale price on 20 Aug 2026. All links are `https://www.etsy.com/listing/<id>/`.

| # | Listing title (truncated) | Product | Target customer | Concept / style | Price | Item rev · rating | Shop rev · lifetime sales | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Retro Ghost Reading Sweatshirt, Halloween Librarian Teacher Gift | Sweatshirt | Librarians, teachers, readers | Ghost reading in a candlelit library; dark cottagecore | $6.90 | **1,417** · 4.9★ | 23,215 · **107,470** | [1746114176](https://www.etsy.com/listing/1746114176/) |
| 2 | Personalized Halloween Tote Bag: Custom Trick or Treat Canvas Bag ⭐Bestseller | Tote | Parents & grandparents of trick-or-treaters | Name + ghost/pumpkin, canvas | $8.24 | **1,828** · 5.0★ | 16,099 · 84,880 | [1083855409](https://www.etsy.com/listing/1083855409/) |
| 3 | Skeleton Halloween Maternity Shirt, Funny Pregnancy Announcement 2026 | Tee | Pregnant women + partners buying for them | Skeleton x-ray baby in belly | $12.39 | **448** · 4.9★ | 8,548 · 40,058 | [1515343101](https://www.etsy.com/listing/1515343101/) |
| 4 | Ghost Reading Stickers, Teacher Halloween Sticker, Librarian Sticker | Sticker | Readers, teachers, journallers | Die-cut ghost reading; sold in packs of 1–6 | $3.49 | **285** · 5.0★ | 5,423 · 22,345 | [1551100086](https://www.etsy.com/listing/1551100086/) |
| 5 | Personalized Bestie Gift, Halloween Best Friend Mug ⭐Bestseller | Mug | Women gifting a best friend / work bestie | Skeleton besties + custom names | $14.99 | **142** · 4.9★ | 2,827 · 16,439 | [4331102955](https://www.etsy.com/listing/4331102955/) |
| 6 | Gothic Dark Academia Halloween Christmas Tree Ornaments — Bat ⭐Bestseller | Ornament | Halloween-tree decorators | Shatterproof bat baubles, gothic | $6.05 | **126** · 5.0★ | 1,563 · 6,307 | [4406169998](https://www.etsy.com/listing/4406169998/) |
| 7 | Custom Name Halloween Tote Bag: Trick or Treat Candy Bag ⭐Bestseller | Tote | Parents of young kids | Name + simple type, lowest price point | $3.95 | **104** · 4.9★ | 6,490 · 63,289 | [4346792179](https://www.etsy.com/listing/4346792179/) |
| 8 | Halloweentown Est 1998 Vintage 90s Graphic Sweatshirt | Sweatshirt | Millennial women, 90s nostalgia | Collegiate "Halloweentown University" | $14.40 | **101** · 5.0★ | 14,252 · **94,253** | [4340550024](https://www.etsy.com/listing/4340550024/) |
| 9 | Mom Halloween Comfort Colors Shirt, Mombie T-Shirt | Tee | Mothers of young kids | "Mombie" retro type | $23.19 | **48** · 4.9★ | 5,248 · 22,575 | [1757695254](https://www.etsy.com/listing/1757695254/) |
| 10 | Support Your Local Murder Shirt, Comfort Colors Raven Shirt ⭐Bestseller | Tee | Witchy / dark-humour women | Crow pun, vintage line art | $7.20 | **41** · 5.0★ | 15,113 · 67,414 | [4375803883](https://www.etsy.com/listing/4375803883/) |
| 11 | Halloween Ghost Coffee Mug, Cute Spooky Ghost Halloween Mug | Mug | Self-purchase + housewarming/hostess gift | Cute minimal ghost, ceramic | $12.96 | **26** · 5.0★ | 12,063 · 64,696 | [1749696724](https://www.etsy.com/listing/1749696724/) |
| 12 | Comfort Colors Kitty Biscuits Shirt, Black Cat Halloween Fall Tee | Tee | Cat owners | Cat making biscuits in a Halloween bakery; retro | $17.04 | **21** · 5.0★ | 5,798 · 33,674 | [4526589660](https://www.etsy.com/listing/4526589660/) |
| 13 | Comfort Colors Reader Ghost Shirt, Bookish Halloween Shirt | Tee | Book lovers, librarians | Ghost + stack of books | $9.99 | **16** · 5.0★ | 9,670 · 65,050 | [4336367087](https://www.etsy.com/listing/4336367087/) |
| 14 | Personalized Halloween Grandma Shirt with Grandkids' Names | Sweatshirt | Grandmothers | Ghost + custom name list | $17.99 | **16** · 4.9★ | 7,521 · 40,998 | [1760701533](https://www.etsy.com/listing/1760701533/) |
| 15 | Coquette Halloween Shirt, Pumpkin Bow Tshirt, Jack-O-Lantern Tee | Tee | Gen-Z / young millennial women | Pink coquette bows on pumpkins | $15.26 | **15** · 5.0★ | 10,670 · 57,172 | [1793646495](https://www.etsy.com/listing/1793646495/) |
| 16 | Halloween Treats Sticker Sheet — Ghosts, Pumpkins, Witches | Sticker sheet | Party hosts, teachers, planners | Cute flat-illustration sheet | $3.99 | **10** · 5.0★ | 4,287 · 19,499 | [4352176958](https://www.etsy.com/listing/4352176958/) |
| 17 | Mini Halloween Ornaments For Small Tree, Vintage Halloween Decor ⭐Bestseller | Ornament set | Halloween-tree decorators | Vintage vampire/ghost/pumpkin minis | $6.59 | 8 · 4.9★ | 514 · 3,418 | [4522625402](https://www.etsy.com/listing/4522625402/) |
| 18 | Comfort Colors Cat Halloween Shirt, Skeleton Cat Shirt ⭐Bestseller | Tee | Cat owners | Skeleton cat, cute-spooky | $9.99 | 6 · 5.0★ | 5,996 · 37,298 | [4340844350](https://www.etsy.com/listing/4340844350/) |
| 19 | Personalized Couple Ghosts Halloween Ornament | Ornament | Couples / newlyweds | Two ghosts + names, glass or ceramic | $8.99 | 6 · 5.0★ | 2,199 · 14,796 | [1780362655](https://www.etsy.com/listing/1780362655/) |
| 20 | Momster Tee, Mom Halloween Graphic Tee | Tee | Mothers | "Momster" vintage type | $33.50 | 5 · 4.1★ | 5,593 · 27,590 | [1522699468](https://www.etsy.com/listing/1522699468/) |
| 21 | Halloween Dog Wall Art Print, Cottagecore Gothic Poster | Poster | Dog owners decorating for fall | Cottagecore gothic illustration | $12.00 | 4 · 5.0★ | 5,321 · 35,994 | [1777841739](https://www.etsy.com/listing/1777841739/) |
| 22 | Personalized Ghost Halloween Mug, Best Friends Gift | Mug | Gift-buyers (bestie / coworker) | Cute ghost + custom name | $13.50 | 4 · 5.0★ | 15,939 · 80,863 | [1781679563](https://www.etsy.com/listing/1781679563/) |
| 23 | Personalized Halloween Baby Boy Romper, Custom Name Bodysuit ⭐Bestseller | Bodysuit | New parents / baby-shower gifters | Custom name + spooky icons | $15.37 | 3 · 4.7★ | 3,331 · 18,947 | [4529724314](https://www.etsy.com/listing/4529724314/) |
| 24 | Halloween Vet Tech Shirt, Veterinary Technician Halloween Shirt | Tee | Vet techs & vet assistants | Trendy ghost + occupation | $16.73 | 2 · 5.0★ | 4,275 · 25,595 | [4340538145](https://www.etsy.com/listing/4340538145/) |
| 25 | Custom Name Halloween Witch Hat, Embroidered Kids Witch Hat | Hat | Parents buying costume accessories | Embroidered name on witch hat | $4.99 | 1 · 5.0★ | 9,264 · 69,811 | [4530270026](https://www.etsy.com/listing/4530270026/) |
| 26 | Halloween Birthday Shirt Custom, Name + Age Pumpkin Ghost | Tee | Parents of October-birthday kids | Personalised name & age | $24.99 | 0 · 4.9★ | 16,695 · **143,112** | [4521993178](https://www.etsy.com/listing/4521993178/) |
| 27 | Halloween Bus Driver Shirt, Spooky School Bus Driver Tshirt | Tee/sweatshirt | School bus drivers (+ gifters) | Ghost + school bus | $20.99 | 0 · 4.9★ | 19,759 · **108,392** | [4539321223](https://www.etsy.com/listing/4539321223/) |
| 28 | Funny Dental Halloween Shirt, Personalized Dental Practice Shirt | Tee | Whole dental offices (bulk) | Custom practice name + spooky teeth | $12.99 | 0 · 4.9★ | 13,409 · 84,005 | [4540245508](https://www.etsy.com/listing/4540245508/) |
| 29 | Personalized Halloween Teacher Tote Bag with Zipper, Choose Five Icons | Tote | Teachers + parents gifting teachers | Custom name + 5 chosen icons | $12.99 | 0 · 4.7★ | 32,246 · **191,637** | [4540841817](https://www.etsy.com/listing/4540841817/) |
| 30 | Personalized Baby First Halloween Ornament 2026, Ceramic Keepsake | Ornament | New parents / grandparents | Year-stamped keepsake | $10.39 | 0 · 4.9★ | 1,725 · 7,889 | [4528864724](https://www.etsy.com/listing/4528864724/) |

### Supplementary proven listings (concept-repetition evidence)

| Listing | Product | Signal |
|---|---|---|
| [4553249750](https://www.etsy.com/listing/4553249750/) Boo-p Ghost Dog Comfort Colors Tee | Tee | "Popular now"; TripletsDesignParty 37,896 sales — **and the same "Boo-p" concept runs in ≥5 independent shops** (FastShirtPrint, BiCraftedDesigns, EmiTeeStudio, DreamDaisyDesignShop, MuyazDesign) |
| [4544040524](https://www.etsy.com/listing/4544040524/) I Smell Children Teacher Halloween Sweatshirt | Sweatshirt | IvyCustomShirt 31,636 shop reviews · **154,154 sales** |
| [4557836887](https://www.etsy.com/listing/4557836887/) Halloween Family Matching Skeleton Shirts | Tee set | KiwiPicks 40,998 sales |
| [4539265617](https://www.etsy.com/listing/4539265617/) Retro Mickey & Minnie Signature Halloween Shirt ⭐Bestseller | Tee | Kosall, Bestseller badge |
| [4551867052](https://www.etsy.com/listing/4551867052/) Cowboy Ghost Halloween Shirt, Western Spooky Tee | Tee | DestinyDesignUS 58,490 sales — western/cowboy-ghost style validated |
| [4549211886](https://www.etsy.com/listing/4549211886/) Spooky Season Leopard Ghost Hoodie | Hoodie | "Popular now"; RoyaltyTeesTreasures 22,841 sales |
| [4550915176](https://www.etsy.com/listing/4550915176/) Skeleton Dog Ceramic Ornament | Ornament | ApparelByMoliva 7,889 sales; dog-identity ornament working |
| [4549014918](https://www.etsy.com/listing/4549014918/) First Halloween Married Ornament | Ornament | ChristmasDecorationX 10,360 sales |
| [4545795696](https://www.etsy.com/listing/4545795696/) Personalized Halloween Stickers, Classroom Labels | Stickers | ThePinkLemonStore 17,181 sales |
| [1776797533](https://www.etsy.com/listing/1776797533/) Personalized Teacher Reward Halloween Stickers | Stickers | LoveMoreByElzaan 26,155 sales |

**FACT — live cart signal:** listing [4543624123](https://www.etsy.com/listing/4543624123/) (Trick Or Treat Coquette Comfort Colors Shirt, ThreadifiedShop) displayed **"In 20+ carts"** on 20 Aug 2026 while having **zero item reviews** — proof that a brand-new 2026 listing in the coquette style is already converting ten weeks out.

**PATTERN — the most important structural insight in Part 3:** high item-review counts cluster on listings that are **1–3 years old** (IDs beginning `1…`), while 2026-season listings (IDs beginning `45…`) mostly show 0–20 item reviews even inside 100k-sale shops. Etsy's Halloween market **resets its review evidence every year**. A new seller is not competing against 1,400 reviews — they are competing against a new listing that also has zero. What the incumbents actually carry into the season is *shop-level* trust. That is the real moat, and it is why picking an under-served sub-niche matters more than out-designing a big shop.

---

# PART 4 — Review mining for new-idea signals

Reviews were read from the item-review modal on individual listings (all star ratings available; I sorted to 1-star on the highest-volume listing to check for design-related complaints). Sizing, shipping and print-defect complaints are excluded as instructed.

## 4.1 Verbatim signals (FACT — quoted from live Etsy reviews)

### From [1551100086](https://www.etsy.com/listing/1551100086/) — Ghost Reading Stickers (285 item reviews)
- *"I LOVE these ghost stickers! I bought one for my **plan book** last year and it still looks great, so I ordered another one for this year's book."*
- *"These little ghosts are so cute. I'm excited to use them in my **reading journal** this Halloween"*
- *"Such a cute sticker! looks great on my **Kindle**"*
- *"Loved this item for my **book club girlies** for fall!"*
- *"Really cute stickers that show both my **spooky side and love of books**!"*
- *"I love this sticker! It looks clean and is amazing for my spooky feeling **all year long**!"*
- *"Super cute stickers. **I ordered more!**"* / *"Would purchase again"*

**What this tells you (PATTERN):** the buyer is not decorating a wall. She is decorating **the objects of her reading ritual** — a Kindle, a reading journal, a teacher plan book — and she buys in repeat multiples. She also explicitly frames the purchase as a *dual-identity* statement ("spooky side AND love of books") and as **year-round**, not October-only.

### From [1515343101](https://www.etsy.com/listing/1515343101/) — Skeleton Halloween Maternity Shirt (448 item reviews)
- *"**My wife loved it!!!** Shipped quickly too!"*
- *"Item was fantastic **my daughter loved it** and is due in Dec."*
- *"**My pregnant niece** loved this as a gift from me"*
- *"Great costume for **my pregnant wife** this year."*
- *"…felt super festive and I got a ton of compliments on it! It's an **easy way to feel festive in those final weeks of pregnancy while still being comfortable**."*
- *"Super cute way to **announce pregnancy during Halloween**!"*
- *"Can't wait to wear this for Halloween!"*
- *"The shirt was cute, **I didn't think about how cold it could be in October, so size up in case you have to layer!**"*

**What this tells you (PATTERN):** at least four of the reviews in the sample were written by **someone other than the pregnant person** — husband, mother, aunt. Etsy's supply is written *as* the pregnant woman ("There's a skelly in my belly"). The buyer is often the partner or a relative, and there is currently almost no product that lets *them* say something. Second signal: **October is cold** — buyers are asking for warmth/layering, i.e. the sweatshirt version outperforms the tee for this occasion and nobody is merchandising it that way.

### From [1083855409](https://www.etsy.com/listing/1083855409/) — Personalized Halloween Tote (1,828 item reviews)
- *"These bags are the perfect trick or treat bag. **My grand babies** loved them and they can be **used year after year**!!"*
- *"Item arrived very quickly… **My granddaughter** is going to love it!"*
- *"**I ordered 3** trick or treat bags for 3 girls. They loved them!"*
- *"**I bought 3 of these for my kids last year** for Halloween and I ended up losing 2 of them so **i reordered for this year**! They are great quality and look brand new still even after a year!"*
- *"**Gift for my best friend's kids**! They love them!"*
- *"A beautiful halloween bag. **I ordered too late for Halloween**, but couldn't resist for next year!"*
- *"I love these bags for Trick or Treating. **They hold up well and are cute for each kid**."*

**What this tells you (PATTERN):** (a) grandparents are a major hidden buyer for kids' Halloween POD; (b) this is a **multi-unit, annually repeating** purchase — one buyer buys 3 and comes back next year; (c) durability/reuse is the stated value, not novelty; (d) "I ordered too late" confirms the season has a hard cliff around late October.

### From [1746114176](https://www.etsy.com/listing/1746114176/) — Retro Ghost Reading Sweatshirt (1,417 item reviews, 93% 5-star, 1% 1-star)
- *"It is incredibly cozy and perfect for **curling up on the couch with a good book**, or wearing for an outing on a chilly day… I can't wait to **order more as gifts**!"*
- *"This was **a gift**, so I don't know exactly what it looks like… but **my bestie was happy** so I'm happy"*
- *"**Ready for all Hallows Eve now**"*
- 1-star reviews on this listing (checked explicitly): *"Wrong color was sent to me!"*, *"Customer service very bad"* — **fulfilment issues only, zero design complaints.** Excluded per brief.
- Shop-level review stream on the same page shows the same shop selling *Custom Halloween Spooky Gigi Sweatshirt* and Father's Day/birthday personalised tees — i.e. these shops win by re-skinning one graphic engine across many identities.

### From [4331102955](https://www.etsy.com/listing/4331102955/) — Personalized Bestie Halloween Mug (142 item reviews)
- *"Love this so much! Came exactly as described and in the time it said! **My bestie will ❤️ it**"*
- Variant data on the page is itself a signal: the listing sells **11oz and 15oz**, and **five handle colours** (black, red, blue, pink, white) — FACT: the 15oz + coloured-handle upgrade is priced **$4.00 higher** ($14.99 → $18.99–$21.99). Buyers are opting into an upsell tier on a Halloween mug.

### From [4526589660](https://www.etsy.com/listing/4526589660/) — Kitty Biscuits Tee (21 item reviews)
- *"Cute shirt! **Can't wait to wear to work.**"*
- *"Adorable cat shirt, **ready for the spooky season**."*
- Etsy's own AI review summary on this listing lists: *Looks great · Great quality · Love it · Fast shipping · Fits well.*

## 4.2 Synthesised idea signals

| Signal type | What buyers actually said | Idea it points to |
|---|---|---|
| **Different product, same design** | "on my Kindle", "in my reading journal", "for my plan book" | Bookish-Halloween **sticker sets sized for Kindle / journal / planner**, sold as a set rather than singles |
| **Different product, same design** | "can't wait to wear to work" | A **desk-object** version of the winning graphics (mug, small print) for people whose workplace bans graphic tees |
| **Wrong buyer addressed** | "my wife loved it", "my pregnant niece", "great costume for my pregnant wife" | Pregnancy-announcement products written **for the partner/relative to give**, and matching partner sets |
| **Comfort / weather** | "didn't think about how cold it could be in October, so size up to layer" | Lead the maternity + outdoor-Halloween ranges with the **crewneck sweatshirt**, not the tee |
| **Repeat & multi-unit** | "I ordered 3", "reordered for this year", "order more as gifts" | Build **sibling/group sets and quantity tiers**; design for reuse ("used year after year") |
| **Hidden buyer** | "my grand babies", "my granddaughter", "gift for my best friend's kids" | Grandparent- and family-friend-facing copy in titles and photos, not just parent-facing |
| **Dual identity** | "shows both my spooky side and love of books" | The winning formula is **Halloween × one other identity**, stated explicitly |
| **Year-round intent** | "amazing for my spooky feeling all year long" | Products that are spooky-but-not-October-dated sell past 31 Oct |
| **Group/social use** | "for my book club girlies" | **Matching sets for adult friend-groups**, not just families |
| **Upsell acceptance** | 15oz + coloured handle at +$4 | Offer size/colour tiers on mugs by default |
| **Season cliff** | "I ordered too late for Halloween, but couldn't resist for next year" | Publish early (now), and add a post-Halloween "next year" hook to keep converting in November |

---

# PART 5 — Gaps, scoring and selected opportunities

## 5.1 Gap types used

- **Audience** — the design exists, but nobody is speaking to this specific group.
- **Wording** — the audience is served, but the words on the product address the wrong person or the wrong feeling.
- **Style** — right audience, right words, but the visual language is dated or mismatched.
- **Product** — the concept sells on one product format and has not been carried to another.
- **Combination** — two proven things (an audience × an occasion, or an identity × a format) that nobody has joined up.
- **Timing** — demand exists in a window the market ignores.
- **Need** — a job the buyer is trying to get done that no listing currently names. Strongest type, because it is confirmed independently on **both** Etsy and Google.

## 5.2 Scoring (1–10 per criterion, /60)

| Rank | Gap | Proven demand | Search demand | Emotional appeal | Market whitespace | Differentiation | Ease of execution | **Total** |
|---|---|---|---|---|---|---|---|---|
| 1 | Adult "boo basket" POD stuffers (partner/wife/husband/adult daughter) | 7 | 10 | 9 | 9 | 8 | 9 | **52** |
| 2 | Halloween pregnancy — written for the *partner/relative who buys it*, sweatshirt-first | 9 | 8 | 9 | 6 | 7 | 8 | **47** |
| 3 | Work-appropriate / dress-code-safe Halloween shirt | 6 | 7 | 7 | 9 | 8 | 9 | **46** |
| 4 | Bookish Halloween for the *reading ritual* — Kindle / reading-journal / plan-book sticker sets + book-club sets | 8 | 7 | 8 | 7 | 6 | 9 | **45** |
| 5 | Office / company team matching Halloween with role personalisation | 7 | 8 | 7 | 7 | 6 | 7 | **42** |
| 6 | Halloween teacher **mug** (format gap next to saturated tee/tote) | 6 | 7 | 8 | 7 | 5 | 9 | **42** |
| 7 | Halloween bar-crawl / "Ghouls Gone Wild" crawl group tees | 5 | 6 | 7 | 8 | 7 | 8 | **41** |
| 8 | Adult-identity hanging ornaments (healthcare, book lover, "First Halloween as a Teacher/Nurse") | 6 | 6 | 8 | 7 | 6 | 7 | **40** |
| 9 | Grandparent-as-buyer trick-or-treat **sibling multi-packs** | 9 | 5 | 8 | 5 | 5 | 7 | **39** |
| 10 | Sober / alcohol-free Halloween apparel — **search demand 2/10, forced to bottom** | 3 | **2** | 8 | 8 | 8 | 9 | **38** |

**Ranking rule applied:** #10 scores 33/50 on the other five criteria — it would otherwise rank mid-table — but `sober halloween` autocomplete returns only events, parties and costumes, never products. Per the brief it is pushed to the bottom and should not be built.

*Also considered and left out of the top 10:* adult October-birthday × Halloween (39/60 — validated by `october birthday shirts for women` but competes with a separate, mature birthday-month niche rather than the Halloween niche).

## 5.3 Master opportunity table

| Rank | Target Customer | Existing Products/Designs | Etsy Evidence | Search Evidence | Gap Type | New Design Concept | Product Type | Suggested Price | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Adults gifting a partner, spouse, best friend or adult daughter a Halloween "boo basket" | Kids' personalised candy totes ($6.90–$26.40); assembled physical gift boxes ($28.00–$88.50); generic ghost candles | `boo basket` page 1 is kids' buckets + assembled boxes: WildflowerPop $28.00 (6.8k shop rev), SucculentkreationsCo $33.08 (28.8k shop rev), RusticZebraBoutique "Guy Boo Basket For Him" **$88.50**. **No POD mug/tee titled as an adult boo-basket stuffer** | 5 seed queries all deep: `boo basket for him / wife / husband / adults / stuffers`. PAA: *"What goes in a boo basket for adults?"*, *"What to put in boo basket for wife"* | **Need** | "Boo Basket Certified" / "You've Been Booed (by your favourite ghoul)" — a matched set of stuffer-priced items with the *relationship* named on the product | Mug (11/15oz), Comfort Colors tee, canvas tote, sticker | Mug $16–$21 · Tee $18–$24 · Tote $14–$18 · Sticker $4–$6 | 52 |
| 2 | The husband / mother / aunt buying for a pregnant woman, and the pregnant woman herself in cold October | Skeleton-x-ray "baby in belly" tee, "Skelly In My Belly", "Spooky Mama" — all written in the pregnant woman's voice | BashVibesUS **448 item reviews**, 4.9★, 40,058 shop sales; ≥6 shops running near-identical x-ray art; reviews written by *"my wife"*, *"my pregnant niece"*, *"my daughter"* | `halloween shirt for` returns **both** "for pregnant women" and "for pregnancy"; `boo basket for wife` returns "**for pregnant wife**"; "halloween costume ideas for pregnant couples" | **Wording** | "Haunted House / Under New Management" — a two-piece his-and-hers set where the partner's shirt carries the joke and hers carries the reveal; **cosy crewneck-first** because October is cold | Crewneck sweatshirt (hero) + tee + partner tee | Sweatshirt $28–$36 · Tee $19–$25 · Set $45–$58 | 47 |
| 3 | Adults who want to do Halloween at an office/hospital/school with a dress code | Loud centre-chest graphics; nothing addresses "is this OK at work?" | Etsy `work appropriate halloween shirt` returns **generic** Halloween tees — no listing frames itself around dress code | `work halloween shirt` autocomplete returns literally "**work appropriate halloween shirts**"; `halloween shirt ideas for` → "for work"; PAA on workplace Halloween ideas | **Need** | "Quietly Haunted" — small left-chest embroidery-style ghost/bat/moon on solid charcoal, navy, black, sage. No slogan. Reads as a normal shirt from 2m away | Left-chest tee, embroidered crewneck, mug | Tee $22–$27 · Embroidered crewneck $34–$42 · Mug $16–$19 | 46 |
| 4 | Readers & teachers who decorate their Kindle, reading journal and plan book | Bookish Halloween tees, sweatshirts, totes, mugs — all saturated. Single die-cut ghost stickers | ValenTeenoDesign ghost-reader sweatshirt **1,417 item reviews**; ArtsyLegacy ghost-reading sticker **285 item reviews** with buyers naming *Kindle*, *reading journal*, *plan book*, *book club girlies*; buyers say *"I ordered more"* | `bookish halloween` → "**stickers**", "**gifts**"; `book club halloween` → ideas / party / reads / theme; PAA *"bookish gifts that are not books"* | **Product** | "Haunted TBR" set — a die-cut sheet sized and laid out for Kindle back, journal cover and planner margins; matched book-club mini-set | Sticker sheet/set, matching bookmark, mug | Sheet $6–$9 · Bookmark $4–$6 · Mug $16–$20 | 45 |
| 5 | Office managers, practice managers, HR/culture leads buying 6–30 matching shirts for the work Halloween party | Some generic group tees; personalised **dental** office shirts are the one mature vertical | SellItAgainDesigns office group tee (1.1k shop rev), Studio73G coworker set (210), PuguTeeDesign "Office Boo Crew" (228), BellaArtisanDesign (3k). EndeavorGoods dental-practice personalisation: **84,005 sales** — proof the *personalised workplace* model works | `group halloween shirts` → "for work", "**company halloween shirts**", "etsy group halloween shirts"; `office halloween shirt` → "**office staff halloween shirts**", "medical office halloween shirts"; `matching halloween shirts` → "for work" | **Combination** | "The [Company Name] Boo Crew, Est. 2026" — custom company/department name + optional per-shirt role line, in a retro varsity lockup | Tee + crewneck, quantity tiers | $18–$24 each; bundle pricing at 6/12/24 | 42 |
| 6 | Parents buying a Halloween gift *for* their child's teacher; teachers buying for themselves | Teacher Halloween tees and totes — both saturated; teacher **mugs** are mostly listings created within the last few weeks | Teacher tote: MojoSticker **191,637 sales**. Teacher mug page 1 is dominated by shops with 1–75 shop reviews (MoodyGoodsCoStudio 11, ChloeLifeDesigns 6, LunaCuddleStudio 8, PrintAura15 —), i.e. no incumbent | `teacher halloween gift` returns a full 10-deep set incl. "**gifts from parents**"; `halloween mug for teacher` → "**halloween cups for teachers**"; `trick or teach` → shirt / t-shirt / sweatshirt | **Product** | "Fuelled by Coffee & Small Ghouls" — personalised teacher name + room number, cute-not-scary ghost, matched to the winning tee aesthetic | Mug 11/15oz + coloured handle tier | $17–$22, +$4 for 15oz/colour handle | 42 |
| 7 | Friend-groups doing an organised Halloween bar/pub crawl | One dedicated pub-crawl matching listing on page 1; the rest are generic drinking tees | HomeStoryCollective "Matching Halloween Pub Crawl Shirts" $25.50 (167 shop rev); BlanchardBend "Booze Crew / Bar Crawl" (378) — thin field | `ghouls gone wild` autocomplete returns "**bar crawl**", "**halloween bar crawl**", "**shirt**" | **Audience** | "Ghouls Gone Wild — [City] Crawl 2026" with editable city/date and a numbered back print | Tee + tank, group quantity tiers | $19–$25 each | 41 |
| 8 | Adults who keep a Halloween tree and want it to say who they are | Ornaments are ~90% baby / couple / pet keepsakes | Ornament category shops are small — ApparelByMoliva 7,889 sales, TheGreyHouseshop 6,307 (Bestseller), Donfash 3,418 — vs 100k-sale apparel shops. Teacher & book-lover ornaments exist and are growing; **nurse/healthcare ornaments are near-absent** | `personalized halloween ornament` / `custom halloween ornaments` / `halloween ornaments for tree` all return real suggestion sets | **Product** | "First Halloween as a Nurse / Teacher / Vet Tech, 2026" — year-stamped flat-print ceramic identity keepsake | Ceramic / acrylic hanging ornament | $12–$18 | 40 |
| 9 | Grandparents buying for 2–4 grandchildren at once | Single personalised trick-or-treat totes | Lalalagiftland **1,828 item reviews**; reviews say *"I ordered 3"*, *"my grand babies"*, *"reordered for this year"*, *"used year after year"* | `custom halloween shirt` → "personalized halloween shirts for kids"; `grandma halloween shirt` → "personalized grandma halloween shirt". (Note: "halloween shirt for grandma" returns nothing — word order matters) | **Audience** | "Grandma's Ghouls" matched set — one adult sweatshirt + 2–4 kids' totes with coordinating art, sold as a bundle | Bundle: sweatshirt + tote multi-pack | Bundle $46–$68 | 39 |
| 10 | Sober / in-recovery adults at Halloween — **DO NOT BUILD** | A handful of listings, most under 25 shop reviews | Thin supply looks like whitespace | `sober halloween` returns **only** events / parties / costumes near me — no product intent | Audience | — | — | — | 38 |

---

## 5.4 Detailed breakdowns — Top 5

---

### #1 — The Adult Boo Basket (Need gap) · Score 52/60

**What currently exists**
FACT: Searching Etsy for `halloween boo basket`, `boo basket for him` and `boo basket mug` returns three things and nothing else. (a) Personalised kids' candy baskets and trick-or-treat buckets, $6.90–$26.40 — the Halloween-tree of this category, everybody sells them. (b) Fully assembled physical gift boxes: WildflowerPop's "Boo Basket for Women… Cozy Fall, Ghost Mug" at **$28.00**, SucculentkreationsCo's "Boo Basket Gift Box with Ghost Mug" at **$33.08**, RusticZebraBoutique's "Guy Boo Basket For Him" at **$88.50**. (c) Generic Halloween candles and mugs that happen to mention "boo basket" in the tail of their title. There is no POD product whose *concept* is "this is the thing you put in her/his boo basket."

**What customers actually need**
PATTERN: a boo basket is a gift *assembled by the giver*. The giver's problem is not "sell me a finished basket" — it is "I have a basket and I need 3–4 things to put in it that will make my wife/boyfriend/best friend feel seen." Google's PAA asks this in plain English: *"What goes in a boo basket for adults?"* and *"What to put in boo basket for wife."* The $88.50 assembled basket is the wrong answer for most of them; so is the kids' candy tote.

**Search evidence**
FACT: `boo basket` → ideas · **for men** · for kids · **for boyfriend** · **for girlfriend** · **for women** · **stuffers** · ideas for women · **for wife** · ideas for girlfriend. `boo basket for him` → ideas · diy · cheap · gifts for him · **stuffers for him** · **items for him**. `boo basket for wife` → ideas · **for pregnant wife** · how to make · **what goes in a boo basket for wife** · **what to put in boo basket for wife**. `boo basket for husband` → diy · **items for husband** · **for men ideas**. `boo basket stuffers` → for kids · for women · **for men** · for teens · **for adults** · **for him**. PAA (live SERP, `boo basket ideas for women`): *"What goes in a boo basket for adults?"* · *"What are some ideas for a spooky basket for my girlfriend?"* · *"What are good basket ideas for adults?"* Related: *Boo basket ideas for adults · for wife · for boyfriend*.

**Proposed concept**
A tightly art-directed capsule of four stuffer-priced items sharing one graphic system, each titled as a boo-basket stuffer **for a named relationship**. The joke is the ghost-as-affection pun ("boo" = both the Halloween sound and the pet name), which is exactly the emotional register a partner gift needs — funny enough not to be embarrassing, warm enough to mean something.

**Specific target audience**
Primary: women 25–40 assembling a boo basket for a boyfriend/husband. Secondary: men doing the same for a wife/girlfriend (this is the emptier and higher-intent half — "boo basket for him ideas" and "boo basket for husband diy" both signal a giver with *no idea what to buy*). Tertiary: parents building one for an adult daughter ("boo basket for adult daughter" is a literal suggestion), and friend-to-friend.

**Design direction**
Retro halftone in the proven Comfort Colors palette (yam, moss, sand, pepper) — do NOT go horror. Two ghosts holding hands / one ghost handing the other a coffee. Chunky 70s slab or groovy script. Muted, warm, giftable. A second colourway in the coquette pink-and-black for the girlfriend/wife SKUs, since the coquette style is the fastest-growing aesthetic in the niche (PoppyRosePrintCo, 57,172 sales).

**Suggested wording**
- "You've Been Booed — by your favourite ghoul"
- "Certified Boo Basket Material"
- "My Boo. My Problem. My Whole Personality."
- "Property of My Boo, Est. 2026" (personalisable year)
- "Boo Basket Approved ✓"
- For him specifically: "Her Boo. Officially Haunted." — pairs with her "His Boo."

**Suggested products**
Hero: 11oz/15oz ceramic mug (fastest to publish, highest gift-conversion, and Part 4 proves buyers accept the +$4 15oz/coloured-handle upsell). Then Comfort Colors tee, canvas tote sized as the basket itself, and a die-cut sticker as an add-on stuffer.

**Suggested price**
Mug $16–$21 · Tee $18–$24 · Tote $14–$18 · Sticker $4–$6 · "Boo Basket Starter Set" (mug + sticker) $22–$26.

**Sales-content angle — 3 hooks**
1. *"POV: you have the basket and no idea what goes in it."* — a 4-item flatlay, each item captioned with who it's for. Answers the exact PAA question.
2. *"Boo baskets aren't just for kids."* — split-screen: a kid's candy bucket vs. an adult's mug-tee-tote. This is literally the market gap, stated as a hook.
3. *"Things to put in a boo basket for him (that he'll actually use in November)."* — leans on the strongest, emptiest search phrase and on the durability angle buyers already praise in reviews.

---

### #2 — Halloween Pregnancy, Written For The Person Who Buys It (Wording gap) · Score 47/60

**What currently exists**
FACT: the category is dominated by one graphic — a skeleton x-ray of a baby in the belly — and by copy written in the pregnant woman's own voice: "There's A Skelly In My Belly", "Skeleton Halloween Maternity Shirt", "Spooky Mama", "Growing a Little Pumpkin". BashVibesUS's version has **448 item reviews** at 4.9★ ($12.39, 40,058 shop sales); AuthenticTee, KavasClothing, ValenTeenoDesign, CustomanduniqueCo and SebarenShop all run near-identical art. Couple sets exist (CrumbsAndChaosCo, LomariDesigns) but are a small minority and are still generic "mom & dad" pairings.

**What customers actually need**
FACT from reviews on that 448-review listing: *"My wife loved it!!!"* · *"Item was fantastic my daughter loved it and is due in Dec"* · *"My pregnant niece loved this as a gift from me"* · *"Great costume for my pregnant wife this year."* At least four of the sampled reviews were written by someone who is **not pregnant**. The market is being bought by partners, mothers and aunts, and every product on the shelf speaks only to the wearer. Second unmet need, stated directly: *"I didn't think about how cold it could be in October, so size up in case you have to layer!"* and *"an easy way to feel festive in those final weeks of pregnancy while still being comfortable."* The buyer wants **warm and comfortable**, and the category leads with a thin tee.

**Search evidence**
FACT: `halloween shirt for` returns **both** "halloween shirt for pregnant women" and "halloween shirt for pregnancy" in the top 15. `halloween shirt for pregnant` returns: for pregnant women · for pregnant mom · **for pregnant with skeleton** · pregnant women halloween shirt · halloween t shirt for pregnant women · cute halloween shirts for pregnant women · halloween costumes for pregnant moms · **halloween costume ideas for pregnant couples**. Separately, `boo basket for wife` returns "**boo basket for pregnant wife**" — confirming that partners are actively shopping for a pregnant woman at Halloween.

**Proposed concept**
A two-piece set where the *partner's* garment carries the punchline and the pregnant person's carries the reveal — plus a cosy oversized crewneck as the hero SKU rather than a tee.

**Specific target audience**
Primary: partners (mostly men, 28–40) buying a Halloween couple's announcement or costume substitute. Secondary: expectant mothers 8–9 months pregnant in October who cannot wear a costume and want to be comfortable and warm. Tertiary: mothers and aunts of the pregnant person (proven buyers, addressed by nobody).

**Design direction**
Move away from the medical x-ray — it is commoditised and slightly clinical. Go **vintage haunted-house / Victorian house-plate** instead: a warm, illustrated house with lit windows. Muted heather grey, sand and black. Oversized boxy crewneck styling in the mockups, layered over a long sleeve, shot outdoors in autumn — mirroring the "cold in October" review insight.

**Suggested wording**
- Hers: "Haunted House — Occupied Since [Month]" · His: "I Live With A Haunted House"
- Hers: "Under New Management, Oct 2026" · His: "Management Trainee"
- "Something Wicked This Way Comes — Spring 2027"
- "Boo Crew, Party of 3 (as of October 2026)"
- For the aunt/grandmother SKU: "Promoted to Spooky Aunt / Spooky Grandma, 2026"

**Suggested products**
Hero: oversized crewneck sweatshirt. Then Comfort Colors tee, matching partner tee, and a "Party of 3" ornament keepsake as the year-stamped upsell (which extends the sale past Halloween into the Christmas-tree window).

**Suggested price**
Sweatshirt $28–$36 · Tee $19–$25 · Two-piece couple set $45–$58 · Ornament $12–$16.

**Sales-content angle — 3 hooks**
1. *"She can't wear a costume this year. Here's what to get her instead."* — spoken to the partner, who is the real buyer.
2. *"Announcing at Halloween? Do it in a sweatshirt — it's freezing by October 31."* — turns a review complaint into a positioning statement.
3. *"The aunt shirt nobody makes."* — targets the aunt/grandmother buyer who appears in reviews and has no product.

---

### #3 — "Quietly Haunted": The Work-Appropriate Halloween Shirt (Need gap) · Score 46/60

**What currently exists**
FACT: Etsy's `halloween shirt` results are overwhelmingly large centre-chest graphics with slogans. Several are explicitly unwearable at work ("I Like Spooky Sh*t & The Word F*ck", $39.35, 210 shop reviews). When I searched Etsy for `work appropriate halloween shirt` the engine returned **generic** Halloween tees — the coquette Trick-or-Treat tee, the Boo-p dog tee, "Support Your Local Murder" — none of which is written or designed around a dress code. Not one listing on page 1 owns that phrase.

**What customers actually need**
PATTERN: a large group of adults want to participate in Halloween at a hospital, school, dental practice, law firm or corporate office where a loud graphic tee is not acceptable. They want *subtle enough to keep on all day*. The Kitty Biscuits review — *"Cute shirt! Can't wait to wear to work"* — is the same need surfacing from the opposite direction: buyers are already filtering the whole category by "can I wear this at work?"

**Search evidence**
FACT: `work halloween shirt` autocomplete returns, verbatim, "**work appropriate halloween shirts**", alongside "office halloween shirts", "halloween work shirt ideas" and "funny work halloween shirts". `halloween shirt ideas for` returns "**for work**". `office halloween shirt` returns "office halloween shirts", "**office staff halloween shirts**", "medical office halloween shirts", "dental office halloween shirts". PAA on `matching halloween shirts for work`: *"What are some fun Halloween ideas for the workplace?"* Note: the literal phrase `halloween shirt for coworkers` returns `[NONE]` — the demand lives under **work / office**, not *coworker*. Title accordingly.

**Proposed concept**
A minimalist "Quietly Haunted" range: one small left-chest mark, no slogan, on adult solid colours. The product promise in the title and first photo is explicitly *"subtle enough for the office."*

**Specific target audience**
Adults 28–50 in dress-coded workplaces: healthcare admin, dental and medical offices, schools with staff dress policies, corporate offices, law/finance. Skews slightly older and higher-income than the core Halloween tee buyer — which supports a higher price.

**Design direction**
Left-chest only, 2.5–3 inches. A single tiny motif: a plain ghost outline, a crescent moon with one bat, a small black cat silhouette, a minimal jack-o'-lantern line drawing. Tonal or single-colour ink. Garment colours: charcoal, black, navy, forest, oatmeal. Embroidery-look (or true embroidery) is the premium tier and is already validated as a price-lifting format in this niche ($17–$51 observed). Mockups must be shot on a person in an office/collared-layer context — that photo *is* the value proposition.

**Suggested wording**
Mostly none — that is the point. Where words are used, keep them to a discreet left-chest lockup:
- "quietly haunted"
- "spooky, professionally"
- "boo. (indoor voice)"
- "31.10" (date only — the most dress-code-safe of all)
- "haunted but employed"

**Suggested products**
Left-chest tee, embroidered crewneck sweatshirt (premium), and a desk mug carrying the same tiny motif for people whose workplace bans graphics entirely.

**Suggested price**
Tee $22–$27 · Embroidered crewneck $34–$42 · Mug $16–$19. Deliberately above the $13–$25 category median: minimal design justifies premium positioning and filters out the discount shopper.

**Sales-content angle — 3 hooks**
1. *"Halloween shirts you won't get asked to change out of."*
2. *"For everyone whose office has a dress code and a Halloween party."*
3. *"From 2 metres away, it's just a shirt."* — a zoom-out video showing the mark disappearing into a normal outfit.

---

### #4 — "Haunted TBR": Bookish Halloween For The Reading Ritual (Product gap) · Score 45/60

**What currently exists**
FACT: bookish Halloween **apparel** is one of the most proven concepts in the entire niche — ValenTeenoDesign's ghost-reading sweatshirt has **1,417 item reviews** at 4.9★, and Etsy carries bookish Halloween tees, sweatshirts, totes, mugs, bookmarks, ornaments and bookshelf figurines. It is saturated. What is *not* saturated is the sticker layer: ArtsyLegacy's single ghost-reading die-cut has **285 item reviews** and is sold as loose singles or packs of 2–6, with no format designed around where buyers actually put it.

**What customers actually need**
FACT from those 285 reviews, verbatim: *"I bought one for my **plan book** last year… so I ordered another one for this year's book"* · *"excited to use them in my **reading journal** this Halloween"* · *"looks great on my **Kindle**"* · *"Loved this item for my **book club girlies** for fall"* · *"shows both my **spooky side and love of books**"* · *"amazing for my spooky feeling **all year long**"* · *"Super cute stickers. **I ordered more!**". Buyers are decorating three specific objects and buying repeatedly. Nobody is selling a set built for those three objects.

**Search evidence**
FACT: `bookish halloween` → decor · costumes · **shirts** · wallpaper · costume ideas · blanket · quotes · crafts · **stickers** · **gifts**. `book club halloween` → **ideas** · costumes · costume ideas · **party** · **reads** · **theme** · snacks · activities. PAA on `bookish halloween gifts`: *"What are some unique bookish gifts?"* · *"What are some good bookish gifts that are not books?"* — the second question is the entire brief for this product. Etsy's own `/market/halloween_bookish_gifts` page ranks on Google page 1, so Google is already routing this demand to Etsy. **Do not** title anything "halloween reading shirt" or "halloween shirt for book lovers" — both return `[NONE]`.

**Proposed concept**
"Haunted TBR" — a die-cut sticker **set** explicitly laid out and sized for the three objects readers named: a large piece for a Kindle/e-reader back, medium pieces for a reading-journal cover, and a strip of small margin/tab stickers for a planner or plan book. Plus a "Book Club Ghouls" mini-set for friend-groups.

**Specific target audience**
Women 22–40 on BookTok/bookstagram who keep a reading journal and a TBR; teachers and librarians (the same buyer wearing a different hat — note the review about a *plan book*); adult book clubs, which the `book club halloween` autocomplete set confirms are actively planning October events.

**Design direction**
Cottagecore/dark-academia palette already proven in this sub-niche: warm candlelight, deep green and oxblood, aged-paper cream. Ghosts reading in armchairs, a black cat on a stack of books, a candle on a bookshelf, moths. Matte water-resistant vinyl. Design the sheet so pieces are *usable at three different scales* — that is the actual product innovation.

**Suggested wording**
- "Haunted TBR"
- "One More Chapter, Then I'll Haunt You"
- "Currently Reading: Something Cursed"
- "Book Club Ghouls, Est. 2026"
- "Support Your Local Haunted Library"
- "Keep the Candy, I'll Take the Books" (already proven on totes — extend the phrase to stickers)

**Suggested products**
Kindle-and-journal sticker set (hero), matching laminated bookmark with tassel (a validated format — TheHauntedHalo carries a Bestseller badge on one at $6.00), and a 15oz book-club mug.

**Suggested price**
Sticker set $6–$9 · Bookmark $4–$6 · Mug $16–$20 · "Reader's Boo Basket" bundle (set + bookmark) $11–$14.

**Sales-content angle — 3 hooks**
1. *"Bookish gifts that aren't a book."* — lifted verbatim from Google's PAA.
2. *"Your Kindle deserves a spooky season too."* — a 5-second before/after on an e-reader back.
3. *"Book club, but make it October."* — the friend-group set, which is the highest-basket-value SKU.

---

### #5 — The Company Boo Crew: Office Team Matching (Combination gap) · Score 42/60

**What currently exists**
FACT: Etsy has fully industrialised **teacher team** and **dental office** matching shirts — EndeavorGoods' personalised dental-practice shirt sits on **84,005 lifetime sales**, and JaxGraphicTees' dental squad shirt on 8.1k shop reviews. But general workplace group shirts are thin: page 1 of `work team halloween shirt` yields only four genuinely on-target listings (SellItAgainDesigns 1.1k shop reviews, BellaArtisanDesign 3k, PuguTeeDesign "Office Boo Crew" 228, Studio73G 210) and the rest are teacher/dental listings bleeding across.

**What customers actually need**
PATTERN: one person — an office manager, practice manager, HR or culture lead — is buying 6 to 30 shirts on a company card, and needs the company or department name on them so it feels official rather than costume-y. The dental vertical proves the model converts spectacularly when the *practice name* is personalised. Every other workplace is left with generic "Boo Crew" tees.

**Search evidence**
FACT: `group halloween shirts` → **for work** · for adults · for teachers · funny · ideas · **company halloween shirts** · band · group t shirts · **etsy group halloween shirts** · candy. `matching halloween shirts` → family · friends · kids · adults · nearby · near me · **for work** · disney · couples. `office halloween shirt` → **office staff halloween shirts** · **medical office halloween shirts** · dental office halloween shirts · funny office halloween shirts. PAA on `matching halloween shirts for work`: *"What are some fun Halloween ideas for the workplace?"* Related searches split by **women / men / adults / funny**, i.e. Google itself recognises this as a distinct commercial query. Note again: `halloween gifts for coworkers` returns `[NONE]` — the phrase to own is **office / work / company / staff**, not *coworker*.

**Proposed concept**
"The [Company Name] Boo Crew — Est. 2026": a personalisation engine, not a design. One retro varsity/collegiate lockup that takes any company or department name, with an optional second line for each person's role, sold in quantity tiers.

**Specific target audience**
Office managers, practice managers, clinic coordinators, HR/people-ops and "culture committee" volunteers at businesses of 5–40 people — vets, physio and optometry clinics, real-estate and insurance offices, salons, restaurants, small agencies. This buyer is spending someone else's money, orders in bulk, and reorders annually.

**Design direction**
Collegiate arch or vintage-varsity lockup (the same visual grammar that makes "Halloweentown University" a perennial winner — OldSchoolCulture, **94,253 sales**). Two-colour print, front only, on Comfort Colors or a comparable garment-dyed blank. Cream/black/orange plus a corporate-safe navy and grey. Show a mockup of six people wearing them together — the group photo *is* the product.

**Suggested wording**
- "[Company] Boo Crew — Est. 2026"
- "The [Department] Ghouls — Haunting This Office Since [Year]"
- "Certified Spooky Staff · [Company]"
- "Trick or Treat Yo' Staff"
- Per-person second line: role or nickname ("Reception · Chief Ghoul")

**Suggested products**
Tee (core), crewneck sweatshirt (upsell for cold-climate offices), and a matching mug so the team gift extends beyond the party day.

**Suggested price**
$18–$24 per shirt with explicit quantity breaks at 6 / 12 / 24 units. State the bulk discount in the title and first photo — this buyer is comparing against a local screen-printer, not against another Etsy tee.

**Sales-content angle — 3 hooks**
1. *"Your office Halloween party, but everyone matches."* — the six-person group photo.
2. *"Put your company name on it — 6, 12 or 24 shirts, one order."* — speaks to the bulk buyer's actual anxiety.
3. *"The dental offices already figured this out."* — social proof borrowed from the one workplace vertical that has visibly gone all-in.

---

## 5.5 Evidence-strength summary

| Opportunity | Etsy evidence | Google evidence | Both? |
|---|---|---|---|
| #1 Adult boo basket | ✅ strong (mature adjacent market, zero POD supply) | ✅ very strong (5 deep seed queries + 2 PAA questions) | ✅ |
| #2 Pregnancy, partner-voiced | ✅ very strong (448 item reviews + buyer quotes) | ✅ strong (2 autocomplete variants + couples query) | ✅ |
| #3 Work-appropriate | ⚠️ absence-based (no listing owns it) | ✅ strong (literal autocomplete phrase) | ✅ |
| #4 Bookish reading ritual | ✅ very strong (1,417 + 285 item reviews, buyer quotes) | ✅ strong ("stickers", "gifts", book club set) | ✅ |
| #5 Office team matching | ✅ moderate (thin supply, proven dental analogue) | ✅ strong (3 query families + PAA) | ✅ |
| #6 Teacher mug | ✅ moderate (no incumbent) | ⚠️ moderate (thin mug-specific autocomplete) | ✅ |
| #7 Bar crawl | ⚠️ thin supply | ⚠️ moderate (one autocomplete family) | ✅ |
| #8 Identity ornaments | ✅ moderate (small shops = low barrier) | ⚠️ moderate (generic ornament queries) | ✅ |
| #9 Grandparent multi-pack | ✅ very strong (1,828 reviews, multi-unit quotes) | ⚠️ weak (word-order sensitive) | partial |
| #10 Sober Halloween | ❌ thin | ❌ **no product intent** | ❌ |

---

## 5.6 Timing note (FACT)

Captured 20 Aug 2026. Etsy listings are already stamped **2026** ("Scary Halloween 2026 Tee", "Personalized Baby First Halloween Ornament 2026", "Mickey's Not So Scary Halloween Party 2026"), and a zero-review 2026 coquette listing was already showing **"In 20+ carts."** Meanwhile the highest item-review counts sit on listings 1–3 years old, which means this season's review race has effectively just started. Publishing in the next two weeks puts a new listing on the same starting line as everyone else's 2026 SKUs. A review from the buyer quoted in Part 4 — *"I ordered too late for Halloween, but couldn't resist for next year"* — marks the far end of the window.

---

## Final answer

**"If I could choose only ONE concept to create from this entire research project, I would choose…"**

**…the Adult Boo Basket capsule — starting with a single mug: "You've Been Booed — by your favourite ghoul."**

Here is why, on the three criteria you asked me to weigh.

**Audience specificity.** This is not "people who like Halloween." It is a person with a wicker basket on their kitchen counter, ten days before Halloween, typing *"what to put in boo basket for wife"* into Google — a question Google itself surfaces as a People Also Ask, and which five separate autocomplete families confirm is being asked constantly, split cleanly by relationship: him, her, wife, husband, boyfriend, girlfriend, adult daughter. That is about as specific and as high-intent as a buyer gets. And the current Etsy answer to that person is genuinely bad: a children's candy bucket, or an $88.50 pre-assembled hamper. The mismatch between how loudly this is being searched and how completely it is unserved on the POD side is the single widest gap I found in this entire study, and it is the only one of my top ten that scored 9 or 10 on both search demand and market whitespace.

**Emotional weight.** "Boo" is doing double duty — the Halloween sound and the pet name — which means the product is a Halloween item *and* a term of endearment at the same time. That is why it outperforms every other concept on gifting: it lets someone say something affectionate under cover of a joke, which is exactly the permission structure that makes people buy gifts for partners. Part 4's reviews show what this niche rewards: the highest-volume listings are the ones where a buyer says "my wife loved it," "my bestie was happy so I'm happy," "my grand babies loved them." Boo baskets are, structurally, that same emotional transaction — someone assembling a small pile of things to say *I thought about you.* A product built for the assembler rather than the wearer sits at the centre of that.

**Speed of designing and publishing.** This is the decisive one. The hero SKU is a **flat-print ceramic mug**. One graphic, one aesthetic system I can reuse across four products, no personalisation engine to build, no size chart, no fit risk, no returns from sizing, no embroidery digitisation, no bulk-order logistics. Mugs are also the thinnest of the seven priority categories on Etsy and carry a proven upsell ladder — the Bestseller bestie mug I examined charges **+$4.00** for 15oz or a coloured handle, and buyers take it. I can design and publish the mug in a day or two, add the tee and tote inside the same week using the same artwork, and still be live with a full capsule well before the late-September demand ramp. Compare that with #5 (Office Team Matching), which scores well but requires a personalisation workflow, bulk-quantity pricing and customer service on custom company names before it earns a single sale.

One honest caveat, stated plainly: this is the **only** idea in my top five whose Etsy-side evidence is *absence-based for the POD format specifically*. Adjacent boo-basket products sell extremely well — WildflowerPop, SucculentkreationsCo and RusticZebraBoutique are all substantial shops — but nobody has yet proven that a $16–$21 POD mug titled as a boo-basket stuffer converts. That is precisely why it is worth doing, and precisely why it should be validated with one fast, cheap product rather than a full range. Publish the mug. If it takes carts within two weeks, roll out the tee, the tote and the sticker behind it.

---

### Appendix — sources

All Etsy data was read from live pages on **etsy.com** (US locale, USD) on 20 August 2026. Individual listings are linked inline in Part 3 and Part 5 in the form `https://www.etsy.com/listing/<id>/`. Google autocomplete data was read from `google.com/complete/search` (client=chrome, hl=en, gl=us); People Also Ask and "People also search for" blocks were read from live `google.com/search` result pages, US region, on the same date.
