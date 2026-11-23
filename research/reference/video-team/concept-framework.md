# Concept framework: building ad concepts (and hook elements) from taggable dimensions

> Research 2026-11-18. Upstream of roles 01–04. Mirrors `hook-framework.md` (FORMAT × TRIGGER, coverage rules, gates) one layer higher, and adds the **hook element** layer below it. Builds on `video-ad-decomposition-2026.md` (12-angle library, format fit, proof ranking, offer, 12-field brief), `ad-science-foundations.md` (§2 relational processing, §3 gift psychology, §4 CEPs, §5 power) and `role-research/04-script.md` (beats HOOK→STAKES→TURN→PROOF→CONNECTION→CTA). Does not repeat their evidence.
> **Why (user, 2026-11-18):** *"we need a framework to create hook and also concept. Not just create out of thin air then we never know why this concept works, that not work."* Every concept is assembled from closed code sets, so results can be read per code.
> **Tool-agnostic by rule.** No generator, model, editor or stock library is named.
> Grades: **[STRONG]** peer-reviewed or platform first-party · **[MODERATE]** large practitioner dataset, preprint, or one solid source · **[WEAK]** vendor blog, opinion, n≤2. "Gap" = searched, found nothing.
> House rules used: R1 product identifiable by 1s, R6 describe the character never the viewer (relationship hooks like "Your granddaughter…" allowed, ruling 2026-11-18), R18 grandparent alive and present, R19 casting matches artwork and caption pronouns (`script-method.md`); FR1–FR11, G1–G9 (`hook-framework.md`); FTC 2024 fake-review rule; "show family connection, never a lonely giftee".

---

## 0. Definitions that end the confusion

Practitioners use "concept", "angle" and "hook" loosely; tools tag them differently. Motion's AI tagging splits **Visual** (asset type, visual format), **Persona**, **Messaging** (theme, seasonality, offer type) and **Hook** (headline tactic) (https://help.motionapp.com/en/articles/12461770-getting-started-with-ai-tagging-in-motion) [MODERATE]. A practitioner hierarchy ranks *concept > audience/problem > angle > hook > format/execution* by production cost and test frequency (http://www.faceplantcreative.com/best-social-media-marketing-agency-blog/creative-testing-for-paid-social-how-to-test-concepts-angles-hooks-and-formats; https://hawky.ai/blog/creative-strategy-performance-marketing) [WEAK]. Meta asks for ads "truly different in **look, feel, storyline, and message**" and defines diversification as "distinct campaign assets tailored to different **personas or use cases**" (https://www.facebook.com/business/news/demystifying-creative-diversification) [STRONG first-party]. Academic message-strategy typologies separate the *strategy* (what is said) from the *execution* (how it is shown): Frazer 1983 (7 creative strategies), Laskey, Day & Crask 1989 (*J Advertising* 18:1; informational vs transformational, with user-image / brand-image / use-occasion sub-types), Puto & Wells 1984 (*Advances in Consumer Research* 11; transformational ads make the experience of owning the product richer than an objective description), Taylor 1999 (*JAR* 39:6; six-segment wheel: ego, social, sensory = ritual view; ration, acute need, routine = transmission view) (https://www.econbiz.de/Record/segment-message-strategy-wheel-comprehensive-message-strategy-model-builds-earlier-ones-suggests-basic-message-strategies-social-sensory-routine-acute/10006517338; https://ufdcimages.uflib.ufl.edu/AA/00/05/29/45/00001/creativestrategi00inth.pdf) [STRONG as typologies; they classify, they do not predict].

**Our definitions (binding for every role):**

| Term | Definition here | Dimensions that make it up | Changes frame 1? | Test that answers it | Primary metric |
|---|---|---|---|---|---|
| **Concept core** ("lý do mua") | The reason to buy, for which buyer, for which recipient and moment. Changing it = a *new concept*. | AN angle · BY buyer role · CEP (recipient × occasion) | Usually | Concept round (§6 R1), read across products and ≥2 executions | hook + hold + link CTR, ATC≠0 gate |
| **Angle** | The single claim about why this gift is worth giving (one AN code). One sub-part of the core. Not a hook, not a format. | AN | — | inside the concept round | — |
| **Execution** ("bản dựng") | How one concept core is told: story structure, whose eyes, which proof, production format, when the personalization lands, emotional register. Changing it = *another build of the same concept*. | ST · PV · PF · PX · RV · EM | Often | Execution round (§6 R2) on a surviving core | hold rate (cheapest, $2/arm) + hook |
| **Story / structure** | The arc the body follows; always laid on the beats HOOK→STAKES→TURN→PROOF→CONNECTION→CTA (`04-script.md` §3). ST says what the TURN *is*. | ST | No | execution round | hold |
| **Format** | Two different things, never mix them: **production format** (PX, the whole film's look: mini-film, UGC-style, demo…) belongs to the execution; **hook format** (F1–F15) is the first 0–3s only. | PX vs F | PX yes | PX: execution round · F: hook round | hold / hook |
| **Hook package** | The first 0–3s as one card: F × T + caption + frame 1 (`hook-framework.md`). Swappable over a fixed body. | F · T · P | Yes | hook round (H1 vs H2 arms) | hook rate |
| **Hook elements** | The taggable slots inside one hook package (frame-1 subject, shot size, onset, caption type/length, audio, product visibility at 0s). §4. | HE1–HE9 | Some | factorial hook test (§4c) | hook rate |
| **Body / CTA / offer** | Beats 2–6 and the close. Offer and CTA are **locked** in Phase 1 (plan page); recorded, not varied. | OF · CTA | No | Phase 2 | CTR / ATC |

**Hierarchy (what sits inside what):** `CONCEPT CORE (AN·BY·CEP) ⊃ EXECUTION (ST·PV·PF·PX·RV·EM) ⊃ HOOK PACKAGE (F×T, arm) ⊃ HOOK ELEMENTS (HE1–HE9)` + `BODY (beats 2–5) + CTA/OFFER (locked)`. A result can only be attributed to the layer that was *the only thing varied*; that is the whole point of the codes.

**Mapping to Meta's four words** (used by the distinctness rule §5c): *message* = AN; *storyline* = ST + PV; *feel* = EM; *look* = PX + frame-1 subject (HE1) + setting. *Persona / use case* = BY × CEP.

---

## 1. CONCEPT DIMENSIONS (9 closed code sets: 3 core + 6 execution)

Prefixes are two letters so they never collide with hook codes (F, T, P, M, G, H). A concept card carries exactly one primary code per dimension (PF may add one secondary).

### D1 · AN Angle: the reason to give (core)
Re-codes the 12-angle library: 7 entries are true *reasons*, the other 5 were formats, proofs or hooks and move to their own dimension. Taylor segment / Puto-Wells type shown so we know which psychological job the angle does.

| AN | Angle (claim from the giver's side) | Library # | Taylor / Puto-Wells | Mechanism | Grade | Gift example |
|---|---|---|---|---|---|---|
| AN1 | **Only theirs**: one of a kind because it carries *their* name, breed, faces | 1, 7 (flex = sub-variant) | social / transformational | Givers buy uniqueness and thoughtfulness (pmid:15901395, 28914152); recipients value personalization because it *expresses the giver* and imagine its creation as effortful (Pizzetti & Gibbert 2018, https://www.researchgate.net/publication/328771629) | STRONG mech. / MODERATE (Pizzetti) | "There was only one Alex. So there's only one of these." |
| AN2 | **Proof you paid attention**: the thought made physically visible | 3, 7 | social / transformational | Thought counts only when the receiver is cued to it (pmid:22774790); relational, not name, processing (PMC6368470) | STRONG | "She never said she kept every drawing. He noticed." |
| AN3 | **Keep them close**: presence of someone gone, or far away | 5 | sensory + social / transformational | Personal-nostalgia ads lift ad/brand attitudes (Muehling & Pascal 2011) | STRONG (attitudes) | memorial suncatcher light on the wall |
| AN4 | **The moment it lands**: the smile/tears the giver is buying | 2 (as benefit) | social / transformational | Smile-seeking giver (pmid:29920154) | STRONG mech. | grandma reading the names aloud |
| AN5 | **All of them, together**: the whole family on one object; belonging | new (grandparent products) | social / transformational | Closeness is the deliverable (pmid:30027819) | STRONG mech., untested in ads | 4 grandkids' names on one blanket |
| AN6 | **Right on time**: a real occasion/deadline makes now the moment | 4 | acute need / informational | CEP retrieval cue (Ehrenberg-Bass, `ad-science` §4); deadline offer rank #1 (decomposition) | MODERATE | "Her 80th is Saturday." (real order-by only) |
| AN7 | **It's built to last / not cheap**: quality reassurance | 8 | ration / informational | Objection removal; lowest emotion (proof rank #5) | MODERATE | close-up of glass and lead lines |
| AN8 | **For yourself, too**: permission to keep one | 11 | ego / transformational | Different buyer pool (plan page) | WEAK | owner buys a panel for his own window |

Moved out: 6 POV → PV1 · 9 relationship callout → hook F2×T3 (plan page already merged it into H2) · 10 emotional mini-film → PX1 · 12 listicle → PX6 · 2 reaction-as-shot → PF2.

### D2 · BY Buyer role (core): who the viewer is cast as
| BY | Buyer role | Viewer relation to name on product | Note |
|---|---|---|---|
| BY1 | **Close giver**: adult child, grandchild, partner buys for someone they love | name = their person | default gift buyer; low-narcissism, relationship-focused skew (pmid:39425564, abstract only) |
| BY2 | **Sympathy / outer-circle giver**: friend, neighbour, colleague | name = the recipient's loss or person | Phase-1 C3; gift crosses a weaker tie, so AN2 "paid attention" is strongest here |
| BY3 | **Self-buyer**: buys for own home (own pet's memorial, own family) | name = their own | Phase-1 C1/C2; R6 risk highest (never "Did you lose…") |
| BY4 | **Group giver**: siblings/grandkids chip in together | name = shared person | pairs with AN5 |

### D3 · CEP Recipient × occasion (core): the retrieval cue
Coded as `RCn×OCn`. RC: RC1 grandparent · RC2 parent · RC3 partner · RC4 child/new baby · RC5 pet (memorial) · RC6 pet (living) · RC7 friend/sibling. OC: OC1 winter holidays · OC2 birthday/milestone age · OC3 Mother's/Father's/Grandparents' Day · OC4 loss / anniversary of a loss · OC5 just because (no date) · OC6 new arrival / new home · OC7 wedding/anniversary. Ehrenberg-Bass: angles should be written as CEPs we own (`ad-science` §4) [MODERATE, evidence-base].

### D4 · ST Story structure / emotional arc (execution)
All ST codes fill the same six beats; the code fixes what STAKES and TURN contain. Evidence for arcs at all: more complete dramatic acts → higher Super Bowl ratings (Quesenberry & Coolsen 2014, *J Marketing Theory & Practice*, 108 ads; https://hub.jhu.edu/2014/01/31/super-bowl-ads) [MODERATE, likability not sales]; narrative transportation raises affect (r=.57) and lowers critical thought (r=−.20); identifiable characters r=.20, imaginable plot r=.29, verisimilitude r=.27 (van Laer et al. 2014 meta-analysis, *JCR* 40:797, https://openaccess.city.ac.uk/id/eprint/18870/1/Extended%20Transportation-Imagery%20Model%20CRO.pdf) [STRONG]; mental simulation persuades via transportation, and argument strength stops mattering under simulation (Escalas 2004, *J Advertising* 33:2) [STRONG]; rising joy and early surprise cut zapping (Teixeira, Wedel & Pieters 2012) [STRONG].

| ST | Structure | STAKES (2–6s) | TURN (6–9s) | Where PROOF/CONNECTION land | Decomposition skeleton | Fits |
|---|---|---|---|---|---|---|
| ST1 | **Reveal** | anticipation: someone about to see it | the personalization appears | proof = the reveal; connection = reaction + family | A | AN1, AN4, AN5 |
| ST2 | **Sentiment build** (mini-film) | a relationship moment, product present but unexplained | the gift's meaning clicks | late-mid payoff ~12s | B | AN2, AN3 |
| ST3 | **Absence → presence** | an empty ritual (bed, chair, window) | the product fills the gap (light lands, names glow) | connection = the person's response | — (suncatcher Phase 1) | AN3 |
| ST4 | **Gift exchange** | the giver chooses/prepares | hand-off | proof = recipient reads it; connection = embrace | A/B hybrid | AN2, AN4, BY1/BY2 |
| ST5 | **Vignettes** | 3–4 short recipients/moments with one rule | each payoff in turn | proof repeated per vignette | listicle-adjacent | AN5, AN6 |
| ST6 | **Process / thought-made-visible** | the source material (photo, drawing, handwriting) | it becomes the product | proof = match between source and product | C | AN2, AN7 |
| ST7 | **Comic turn** | a setup ("don't get me anything") | the reversal | connection = affectionate payoff | — | AN4, AN5 (never RC5) |

### D5 · PV Protagonist / point of view (execution)
| PV | Whose story the camera follows | Risk |
|---|---|---|
| PV1 | **Giver** (casts the viewer as the hero giver) | must still show the recipient's response (connection rule) |
| PV2 | **Recipient / user** (face, reaction) | "lonely giftee" if no second person or relational cue appears after the TURN |
| PV3 | **Ensemble / family** (both sides, several people) | casting load; R19 every printed name needs a matching person |
| PV4 | **Object-led** (camera on product, room, light; people secondary) | weakest identifiable character (van Laer r=.20 antecedent); needs a human in ≥1 beat |

### D6 · PF Proof type (execution): what pays the hook
Ranking from decomposition, corrected by `ad-science` §3①: the reaction is the *benefit* (lives in CONNECTION or the hook), not evidence.
| PF | Proof | Truth requirement | Default beat |
|---|---|---|---|
| PF1 | **Personalization legible on the real product** (name, breed, faces) | real product artwork, never model-drawn text (house rule 5) | PROOF (≤12s / ≤9s) |
| PF2 | **Recipient response** (dramatized) | character in a story; never presented as a real customer (FTC 2024) | CONNECTION or hook |
| PF3 | **Source-to-product match** (photo → silhouette, handwriting → print) | real source + real output | PROOF |
| PF4 | **Craft / material close-up** | real product photo | PROOF (Stage-2) |
| PF5 | **Real customer photos / reviews** | real, permissioned, fact-sheet ID | PROOF (retarget) |
| PF6 | **Volume / longevity** | true number with source | end (velocity only) |

### D7 · PX Production format (execution): the whole film's look
| PX | Format | Decomposition fit | Cut rate (brief) | Notes |
|---|---|---|---|---|
| PX1 | **Cinematic mini-film** (scripted characters, no address to camera) | MEDIUM (cost) but house default | ~2–5s varied | Phase-1 suncatcher |
| PX2 | **Creator-style / talking to camera** (a *character* speaks) | HIGH (UGC) | ~5s | ✕ as fake testimonial (F13 note ᵍ); character line only |
| PX3 | **Hands / demo / process** | MED (BTS), HIGH (flex) | progress-paced | pairs with ST6 |
| PX4 | **Product-hero motion** (real stills + moves, text-led) | MEDIUM | ~1.5–2.5s | cheapest; strongest truth |
| PX5 | **Native artefact** (chat, note, letter in scene) | MEDIUM | per artefact | FR8 no fake UI |
| PX6 | **Montage / list** | MEDIUM | beat-matched | pairs with ST5 |
Excluded: founder story (LOW), podcast (SKIP) per decomposition.

### D8 · RV Reveal timing of the personalization (execution)
The *product* is identifiable by 1s in every code (R1, gate). RV times when the **personalization becomes legible**, which is what "late payoff" really means. Brand/product pulsing beats one long block (Teixeira et al. 2010, *Marketing Science* 29:5) [STRONG].
| RV | Personalization legible at | Effect on hook arms |
|---|---|---|
| RV1 | 0–1s (in the hook) | H1 "name shown" lives here |
| RV2 | pulsed: a cue by ~3s (tag, box card), full proof at PROOF beat | house default (C1 ALEX tag) |
| RV3 | PROOF beat only (≈9–12s), nothing earlier | maximises curiosity, risks G1 "what is sold" |

### D9 · EM Emotional register (execution)
| EM | Register | Evidence | Valid with |
|---|---|---|---|
| EM1 | Tender / warm | joy dynamics retain (Teixeira 2012) [STRONG] | all |
| EM2 | Bittersweet (sad → warm inside the ad) | mixed happy-sad appeals are disliked by people low in "acceptance of duality" (younger, Anglo-American) and accepted by older adults (Williams & Aaker 2002, *JCR* 28; https://www.gsb.stanford.edu/faculty-research/publications/can-mixed-emotions-peacefully-co-exist) [STRONG]; fits a 55+ buyer, may repel younger buyers | RC5, RC1 (R18: grandparent alive) |
| EM3 | Joyful / celebratory | positive affect, early surprise (Teixeira 2012) [STRONG] | OC2, OC1, AN5 |
| EM4 | Humorous / affectionate | humor raises Aad and brand attitude via affect (Eisend 2009) [STRONG] | ✕ RC5/OC4 |
| EM5 | Awe / wonder | surprise mechanism (`hook-framework` T2) [STRONG mech.] | light/transformation products; FR rules |

Core = AN, BY, CEP; execution = ST, PV, PF, PX, RV, EM. Offer framing (OF) and CTA are recorded fields, locked in Phase 1, not dimensions.

---

## 2. Validity matrix and rules

### 2a. Core: AN × BY  (`S★` strong for personalized gifts · `S` workable · `W` weak, reason required · `✕` invalid)
| AN \ BY | BY1 close | BY2 sympathy | BY3 self | BY4 group |
|---|---|---|---|---|
| AN1 only theirs | **S★** | S | **S★** | S |
| AN2 paid attention | **S★** | **S★** | ✕ᵃ | S |
| AN3 keep close | S | **S★** | **S★** | S |
| AN4 moment it lands | **S★** | S | ✕ᵃ | **S★** |
| AN5 all together | **S★** | W | S | **S★** |
| AN6 right on time | S | W | W | S |
| AN7 built to last | W | W | S | W |
| AN8 for yourself | ✕ | ✕ | **S★** | ✕ |
ᵃ "paid attention" and "the moment it lands" need a second person; a self-buyer has nobody to notice.

### 2b. Execution: ST × EM and ST × PX
| ST | EM1 | EM2 | EM3 | EM4 | EM5 | Best PX |
|---|---|---|---|---|---|---|
| ST1 reveal | S★ | S | S★ | W | S | PX1, PX4 |
| ST2 sentiment build | S★ | S★ | W | · | S | PX1 |
| ST3 absence→presence | S★ | S★ | · | ✕ | S★ | PX1, PX4 |
| ST4 gift exchange | S★ | S | S★ | S | W | PX1, PX2 |
| ST5 vignettes | S | W | S★ | S | · | PX6, PX4 |
| ST6 process | S | W | S | · | S | PX3 |
| ST7 comic turn | S | ✕ | S | S★ | · | PX1, PX2 |

### 2c. Hard invalid combinations (any one = card rejected, gate CG2)
| # | Invalid | Why |
|---|---|---|
| IC1 | PV2 or PV4 with no second person or relational cue after the TURN | house rule: lonely giftee reads as the wrong emotion |
| IC2 | EM4 (humor) × RC5 or OC4 | memorial; `hook-framework` T9 |
| IC3 | EM2 × RC1/RC2 where the parent/grandparent reads as dead or absent | R18 |
| IC4 | PF2/PX2 presented as a real customer ("I ordered…", "real reaction") | FTC 2024 rule; Meta |
| IC5 | PF5/PF6 without a fact-sheet ID | FTC; no invented numbers |
| IC6 | AN6 without a real order-by date | Meta prohibited practices (fake urgency) |
| IC7 | any copy describing the viewer's attribute ("Grieving?", "Did you lose…") | R6 / Meta Personal Attributes; relationship "your granddaughter" allowed |
| IC8 | the product shown doing what it cannot (light without sun, brighter name) | FR1–FR2; FTC v. Colgate; Meta misrepresentation |
| IC9 | memorial: the deceased moving/returning in the present | FR5 |
| IC10 | casting that contradicts printed artwork or caption pronouns | R19, memory casting-matches-caption |
| IC11 | AN8 × any BY other than BY3 | logical contradiction |

### 2d. Soft rules
- **Personalization is relational, not decorative:** a concept whose only proof is a stranger's name (PF1 with no RC cue) is `W` (PMC6368470).
- **Over-individuation risk:** givers over-pick gifts that fit a recipient's traits but are hard to use (Steffel & LeBoeuf 2014; https://spsp.org/news-center/press-release/psychology-gift-giving-and-receiving) [STRONG mech.]. A concept should show the object *in use* in the recipient's life at least once (CONNECTION beat).
- **Desirable vs feasible:** givers think about attractiveness, receivers about use (Baskin et al. 2014, *JCR*; https://som.yale.edu/story/2022/behavioral-scientists-guide-gift-giving) [STRONG]. Sell the giver's criteria in the hook; let the body show the object living with the recipient.

---

## 3. The CONCEPT CARD

### 3a. Fields (one row per concept in `_ledgers/concepts.csv`; one per execution in `executions.csv`)
| Field | Layer | Content |
|---|---|---|
| `concept_id` | core | `<PRODUCT>-K<nn>`, e.g. `SUN-K01` (K, not C, so it never collides with plan "C1" cell labels) |
| `angle` `buyer_role` `recipient` `occasion` | core | one code each |
| `reason_line` | core | the reason to buy in ≤15 words, giver's view, character-described |
| `insight` | core | one sentence of mechanism + citation (§1 tables) |
| `execution_id` | exec | `<concept_id>-X<n>`, e.g. `SUN-K01-X1` |
| `structure` `pov` `proof` `proof_2` `prod_format` `reveal` `register` | exec | one code each (`proof_2` optional) |
| `logline` | exec | ≤40 words, who / what changes / how it ends |
| `beat_map` | exec | 6 lines: HOOK / STAKES / TURN / PROOF / CONNECTION / CTA, one clause each, with second marks |
| `hook_space` | exec | ≥3 `S★`/`S` F×T cells this execution can carry, with the arm axis planned |
| `cast_artwork` | exec | every person, trait and printed name; pronoun map (R19) |
| `locked` | exec | offer, CTA line + button, length, ratios (copied from the plan) |
| `policy` | exec | IC1–IC11 check, one word each |
| `distinctness` | exec | Meta four-word diff vs every running concept (look/feel/storyline/message) |
| `hypothesis` | exec | what this card tests vs which control, on which dimension |
| `critic_score` `critic_spread` `status` | both | candidate / cut / selected / reserve / shipped / parked / retired |

### 3b. Phase-1 suncatcher concepts mapped onto the codes
| Cell | AN | BY | CEP | ST | PV | PF (+2) | PX | RV | EM |
|---|---|---|---|---|---|---|---|---|---|
| C1 Personalization | AN1 | BY3 | RC5×OC4 | ST3 | PV4 | PF1 | PX1 | RV2 (ALEX tag 2s, wall 9–12s; H1 adds RV1) | EM2 |
| C2 Reaction | **AN3** | BY3 | RC5×OC4 | ST3 | **PV2** | PF1 (+PF2) | PX1 | RV2 | EM2 |
| C3 Buyer swap | **AN2** | **BY2** | RC5×OC4 | **ST4** | **PV1** | PF1 | PX1 | RV2 | EM1→EM2 |

**What the mapping shows.** (1) "02 Reaction" is not a reason to buy under these definitions: it is an execution (PV2 + PF2). Coded honestly, C2 differs from C1 on AN *and* PV *and* proof emphasis, so a C1/C2 difference cannot be pinned on one dimension. (2) C3 changes BY, AN, ST and PV together (a bundled swing). (3) All three hold CEP, PX, RV and EM constant, so Phase 1 says nothing about those. This is acceptable for a **discovery** round (`ad-science` §5e: diverse batches generate hypotheses, they don't test them) but must be reported as "bundle C3 vs bundle C1", never "buyer swap works". (4) The hook arms are a trigger-arm inside F5/F2 (`hook-framework` §6c) and cross all three concepts, so the hook result *is* attributable.

### 3c. Worked example 1: dog-memorial suncatcher, new concept
| Field | Value |
|---|---|
| concept_id | `SUN-K04` · core AN2 × BY1 × RC5×OC4 |
| reason_line | "She remembered exactly how he sat in the window." |
| insight | Thought counts when cued (pmid:22774790); a close giver making it visible is the cue. |
| execution | `SUN-K04-X1`: ST4 gift exchange · PV1 giver (adult daughter) · PF3 source-to-product match (+PF1) · PX1 · RV2 · EM2 |
| logline | A daughter finds her late dog's photo on her father's fridge, has the panel made from it, and hangs it in his window; the light lands where the dog used to sit; he puts his hand on her shoulder. |
| beat_map | HOOK 0–2 her hand lifts the photo off the fridge, panel box on the counter · STAKES 2–6 his empty chair-side spot by the window · TURN 6–9 she hangs it, sun comes through · PROOF 9–12 silhouette on the floor matches the photo's pose, "Alex" legible · CONNECTION 12–17 he sees it, hand on her shoulder · CTA 17–20 panel, locked line |
| hook_space | F11×T7 (photo→panel match), F9×T1 ("Dad hasn't moved that chair."), F8×T3 POV her hands · planned arm: format-arm F11×T7 vs F8×T7 (T held; F9×T1 is the reserve) |
| cast_artwork | daughter (40s), father (~70, matches C1 owner turntable if reused, logged), German Shepherd "Alex" in photo and silhouette; captions: "she" = daughter, "he/him" = Alex, father never "he" in a caption with Alex in frame |
| policy | IC1 pass (two people) · IC7 pass (character-described) · IC8 pass (light only in sun) · IC9 pass (photo = past) |
| distinctness vs C1–C3 | storyline (ST4 vs ST3) + cast (daughter) + message (AN2) = 3 of 4 words differ |
| hypothesis | vs C1 (AN1×BY3): does a close-giver "paid attention" core lift hook+hold over the self-buyer "only theirs" core? Bundled (AN+BY); single-dimension follow-up = SUN-K05 AN1×BY1 with the same execution |

### 3d. Worked example 2: grandma gift (blanket / magnet with all grandkids' names)
| Field | Value |
|---|---|
| concept_id | `GMA-K01` · core AN5 × BY4 × RC1×OC2 (80th birthday) |
| reason_line | "All four of them, on the one thing she keeps on her lap." |
| insight | Closeness is the deliverable (pmid:30027819); group giver shares the credit. |
| execution X1 | ST1 reveal · PV3 ensemble · PF1 (+PF2) · PX1 · RV2 · EM3 |
| execution X2 (same core) | ST7 comic turn ("don't get me anything" → she won't let a grandkid sit on it) · PV2→PV3 · PF1 · PX2 (a grandkid character to camera) · RV2 · EM4 |
| beat_map X1 | HOOK cake "80", wrapped blanket, four grandkids crowding in · STAKES she waves it away · TURN unfolds it, names visible · PROOF names legible, one per grandkid, each kid points to theirs · CONNECTION she pulls the youngest under it · CTA |
| cast_artwork | grandma alive, present (R18); exactly 4 grandkids whose genders/ages match the 4 printed names; pronouns: "she" = grandma only |
| hypothesis | X1 vs X2 = execution round on one core (ST+EM+PX bundle); if both lose on hook+hold across ≥2 products, retire the core (plan page rule: 2–3 builds) |

---

## 4. HOOK ELEMENT layer (extends `hook-framework.md`, does not redo it)

A hook card already has F, T, P, frame1_visual, onset_0_5s, caption, audio_cue. Those fields are free text, so nothing can be counted. HE codes make them countable.

### 4a. Element slots
| HE | Slot | Codes | Evidence for why the slot matters |
|---|---|---|---|
| HE1 | **Frame-1 subject type** | SU1 product hero · SU2 human face · SU3 animal/pet (real or silhouette) · SU4 hands + product · SU5 text/artefact · SU6 scene with product small · SU7 impossible/composited | faces draw gaze (Cerf 2008), animals get priority (New et al. 2007 *PNAS*) [STRONG]; Meta groups by visual attributes [STRONG] |
| HE2 | **Shot size at 0.0s** | SZ1 ECU/detail · SZ2 close · SZ3 medium · SZ4 wide | Google ABCD tight framing [STRONG first-party]; feature clutter hurts (Pieters, Wedel & Batra 2010) [STRONG] |
| HE3 | **Onset by 0.5s** | ON0 static · ON1 camera drift/push only · ON2 subject action onset · ON3 light/colour change · ON4 hard cut / scale jump · ON5 text pop-on | onset > smooth motion (PMC3711149) [STRONG]; ON1 is the weakest by that evidence |
| HE4 | **Caption type** | CT0 none · CT1 statement about a character · CT2 question to the giver role · CT3 relationship callout · CT4 number/specific · CT5 dialogue/quoted line · CT6 label ("POV:", "Day 1") | headline wording effects (Robertson 2023; Upworthy inverted U) [STRONG, text] |
| HE5 | **Caption length band** | LB1 1–4 words · LB2 5–7 · LB3 8–10 · LB4 >10 (card invalid; legacy tag only) | text by 0.5s, ≤8 words for a "5" (critic anchor) [MODERATE] |
| HE6 | **Caption on-time** | TM1 frame 1 · TM2 ≤0.5s · TM3 >0.5s | "text by 0.5s" vendor +4–9 pts [MODERATE] |
| HE7 | **Audio cue type** | AU0 bed only · AU1 sync hit on onset · AU2 diegetic room/tactile · AU3 voice (VO/dialogue) · AU4 silence → sound | sound-off majority; audio never carries meaning (G1) |
| HE8 | **Product visibility at 0s** | VS1 present, <1/3 width · VS2 prominent ≥1/3 · VS3 personalization legible (name/breed readable) | R1 / G1; payoff in frame 1 vendor +5–12 pts [MODERATE]; VS0 (absent) = invalid unless product by 1.0s and logged |
| HE9 | **People / relation in frame 1** | PC0 none · PC1 one person · PC2 two+ with visible relation | connection rule; relational processing (PMC6368470) |

### 4b. Tag everything; test only four (deep plan, 2026-11-21)
- **Tag (always, by 01; verified by 02 under G9):** all nine slots. Tagging costs seconds and it is the only way the ledger ever answers "does ON3 beat ON1".
- **Test as factors in round H1** (§6): **HE1 subject (SU)**, **HE3 onset (ON)**, **HE9 people in frame 1 (PC)** and **personalization timing (RV1 vs RV2,
  carried at 0s by HE8: VS3 when RV1, VS2 when RV2)**. Each changes the frame or the main stop mechanism and has a mechanism hypothesis.
  Hook format (F) × trigger (T) are tested in round H2.
- **Fix by rule, don't test** (user directive 2026-11-19: captions, sound and music are minor): HE2 (tight by default), HE4 caption type,
  HE5 (≤LB2 preferred), HE6 (TM1/TM2), HE7 (AU0/AU1). Tag them anyway.
- Caption-only changes over an identical frame are "iteration" to Meta and share delivery; another reason they are not a factor.

### 4c. 2×2 factorial example (one body, four hooks)
Factor A = **HE8** VS3 (name "Alex" legible at 0.0s) vs VS2 (panel prominent, name not yet legible). Factor B = **HE3** ON3 (sun hits the panel at 0.4s) vs ON1 (slow push-in only). Held: F5 reveal family, T7, caption CT1 LB2 TM2, AU0, SZ1, same 2–20s body (byte-identical), same CTA.
| | ON3 light onset | ON1 drift |
|---|---|---|
| **VS3 name at 0s** | A1B1 | A1B2 |
| **VS2 name later** | A2B1 | A2B2 |
- **Why factorial:** each main effect compares 2 cells vs 2 cells, so every impression counts twice. For a hook-rate 22%→28% difference at 80% power you need ~814 impressions per level (`ad-science` §5b), i.e. ~410 per cell, ~1,630 total ≈ **$21 at CPM $13 for both main effects at once**. Detecting the A×B interaction needs roughly four times that (≈$85) [standard factorial design result; estimate assumes our §5b CPM].
- **Validity:** run as a randomized split (Meta A/B test, or one ad per ad set with equal budget and schedule), never four ads in one ad set (§5d delivery confound). Pre-register: factors, levels, primary metric = hook rate, secondary = hold (bait-and-switch check), sample per cell fixed in advance.
- **Read:** main effect of VS = name-at-0s value; main effect of ON = onset value; if the interaction is large, report cells, not mains.

---

## 5. Generation procedure: concept roles

### 5a. Recommendation: add two roles and one gate; selection stays with the user
| New | Role | Why separate | Inputs | Output |
|---|---|---|---|---|
| **00A** | **Concept Ideator** | wide pool by coverage, like 01 | product fact sheet (F-IDs, real features, what the product physically does), product photos, plan constraints (locked offer/CTA/length), concept ledger + results, scene ledger, this codebook | `concepts/00A-candidates.md`: ≥12 concept cards (core + 1 execution each) |
| **00B** | **Concept Critic** | maker ≠ judge (self-preference, Panickssery 2024 [STRONG]); a filter, not a fortune-teller (Armstrong 2016: checklist + several raters ≈75% vs ~55% unaided [STRONG]) | 00A cards with rationale hidden; calibration concepts with known results | `concepts/00B-scores.md`: gates, scores, spread, cut list |
| — | **Selection (Producer proposes, user approves = GATE 0)** | the plan page is the test authority; concepts *are* the plan's structure, so no agent may pick them (README §2.1) | 00B survivors, round type (§6), budget | `concepts/00C-slate.md`: proposed slate + declared axis + pre-registration lines → user approves → plan page updated → cells created |
Why not a third agent: a concept slate is a structural decision that the user already owns; a "selector agent" would either duplicate the Producer or override the plan. The selection *procedure* (§5d) is written so the Producer applies it mechanically and the user sees why each concept made the slate. Agent files to add: `.claude/agents/vt-00a-concept-ideator.md`, `vt-00b-concept-critic.md`; README pipeline becomes `PLAN ◄─ GATE 0 ◄─ 00B ◄─ 00A` then `01…07`.

### 5b. 00A coverage rules (pool of ≥12 cards per product)
1. Every card: exactly one code per dimension (PF may add `proof_2`); `reason_line` ≤15 words.
2. **Spread:** ≥5 AN codes, ≥3 BY codes, ≥3 CEPs, ≥4 ST, ≥3 PV, ≥3 PX, ≥3 EM in the pool.
3. **Caps:** no AN on >3 cards; no ST on >4; PX1 (mini-film) ≤50% (cost).
4. **Gift core floor:** ≥7 cards in `S★` cells of 2a and 2b.
5. **Exploration floor:** ≥2 cards (~15%) using a code with <2 entries in the concept ledger.
6. **No IC1–IC11**; `W` cells only with a one-line reason.
7. **Near-duplicate:** same AN + BY + RC → one concept core; keep the better execution as `X2` of it, don't count it as a second concept.
8. **Product truth:** every card names the product feature it relies on (e.g. "projects silhouette + name in direct sun") with its F-ID; no feature → cut.
9. **Two independent passes** if a model ideates; pass 2 is told which codes pass 1 left empty (homogeneity guard, `04-script` §1g [STRONG]).
10. Each card lists ≥3 compatible F×T hook cells, so 01 has room.

### 5c. 00B gates (binary; any fail = cut) and rubric
| Gate | Pass condition |
|---|---|
| CG1 One reason | `reason_line` states one reason to buy in ≤15 words; needing "and" = two concepts |
| CG2 Policy | IC1–IC11 all pass |
| CG3 Connection | a relationship is visible in ≥1 beat after the TURN |
| CG4 Producible truthfully | proof uses the real product/artwork; personalization legible by plan; FR rules if any impossible shot |
| CG5 Casting | every printed name/figure and pronoun has a matching cast member |
| CG6 Tag validity | the card does what its codes say (an ST3 card has an absence; a PV1 card follows the giver) |
| CG7 Distinct | differs from every running concept on ≥2 of Meta's look/feel/storyline/message (§0 map) |
| CG8 Payable hook space | ≥3 hook cells from 2a/§3 of `hook-framework` that the body can pay by 12s/9s |

| Criterion (/100) | Wt | 1 | 3 | 5 |
|---|---|---|---|---|
| Buyer relevance (CEP strength) | 25 | generic occasion, any buyer | named relationship, common moment | a specific, widely shared moment the buyer would recognise instantly |
| Gift-psychology fit | 20 | sells features/utility | shows the gift, implies thought | makes the giver's thought visible *and* shows closeness (pmid:22774790, 30027819) |
| Proof payability | 20 | proof needs invented text or claims | proof present but late/small | personalization legible on the real product at the PROOF beat, and cued early (RV2) |
| Story transport | 15 | no character, no change | character or change | identifiable character + imaginable plot + verisimilitude (van Laer 2014) |
| Distinctiveness | 10 | 1 of 4 Meta words differ | 2 differ | 3–4 differ and an under-tested code |
| Production risk | 10 | needs hands-on-text, faces in impossible shots, many people | moderate | real stills carry the proof; ≤2 recurring people |
Kill: total <70, any criterion at 1, or proof payability ≤2. Panel = 3 blind judges, shuffled order, median, flag spread ≥2 (same as 02). Calibration: once ≥4 concepts have results, blind them into every batch; if the panel can't rank them, scores are advisory.

### 5d. Slate selection procedure (Producer, then user at GATE 0)
1. **Declare the round's axis first** (§6): `core-AN`, `core-BY`, `core-CEP`, or an execution dimension. The slate varies *only* that axis; every other code is held equal across the slate where the product allows.
2. **Bundles must be declared.** If changing the axis forces another code (BY2 usually forces PV1 and ST4), record the bundle; the result is reported for the bundle.
3. Pick the top-scoring survivor per axis level; reserve = next best.
4. **Distinctness:** slate members pass CG7 against each other, not only against running ads.
5. **Cross-product rule** (plan page): a concept slate runs the same cores on every product in the round; a core that can't be built on one product (e.g. AN3 memorial on a grandma magnet) is swapped for the round, not forced.
6. Write the pre-registration line per concept: axis, codes, control concept, primary metric, sample gate, decision rule.

---

## 6. Testing ladder and attribution (deep plan, decided 2026-11-21; replaces R0–R4)

Only hooks and concepts are tested (the two largest levers, `impact-ranking.md`). Everything else is FIXED and identical in every ad:
product visible from 0s (VS1+), length 15–25s, 9:16 + 4:5, captions (type, length, timing), sound and music, voiceover, CTA + end card,
**one offer**. Deck: https://mj4u-test-plan.namvu47.workers.dev.

### 6a. Rounds (power from `ad-science` §5b; budgets at CPM $25, maximum)
| Round | Varies (2 levels each) | Holds | Design | Ads × imp | Read on | Decides |
|---|---|---|---|---|---|---|
| **C0** Concept discovery | whole concepts (bundles, declared) | the fixed list | 6 concepts × 2 hooks, large gaps only | 12 × 800 · $240 | hook rate, CTR; concept = mean of its 2 ads | keep the best 1–2; all <21% hook → new concepts |
| **H1** Hook opening | people in frame 1 (PC) · personalization timing (RV1/RV2) · frame-1 subject (SU) · onset (ON) | C0 winner's concept + body | 8-ad grid, 4 factors | 8 × 1,700 · $340 | hook rate | the opening recipe |
| **C1** Concept core | angle (AN) · buyer role (BY) · occasion (OC) | recipient, execution codes where possible, C0 winner's hook style | 8-ad grid, 3 factors (full) | 8 × 1,700 · $340 | hook + hold + CTR | the reason to buy |
| **C2** Concept execution | structure (ST) · point of view (PV) · tone (EM) · proof type (PF) | C1 winning core, H1 opening, PX from C0 | 8-ad grid, 4 factors | 8 × 1,700 · $340 | **hold** + CTR, then hook | the story template |
| **H2** Hook type | hook format (F) · trigger (T): best 2 of each from C0 | the final concept + body | 4-ad grid, 2 factors (full) | 4 × 1,700 · $170 | hook rate | hook rules for refreshes |
| **B** Break-even check | nothing (not a creative test) | the top 2 ads | consolidated | 2 ads, 17,000 imp · $425 | cost per sale vs break-even | scale / fix site / stop |
| S Scaling | hook swaps on the winner | everything else | — | scaling budget | hook, CTR, CPA | refresh or stop |

Per product: 42 test ads, 13 elements, ≈ $1,855 max ($1,485 @$20, $2,225 @$30); typical ≈ 80%. 5 products ≈ $9,300 max.
**RV is tested only in H1** and **proof type only in C2** (user ruling 2026-11-21: RV was in both H1 and C2, which would alias them).
Production format (PX) is decided inside C0's bundles, then held. Recipient comes with the product.

**Run order:** C0 alone → (H1 ∥ C1) → (C2 ∥ H2) → B. Two rounds run together only when they change different parts of the ad
(H1 and H2 never together), each in its own ad sets, equal budgets, launched the same day. ~3–5 days per round (~$14/ad/day),
~3–4 weeks per product; products overlap. Production: C0 builds 6 concepts; H1/H2 are hook swaps on existing footage; C1/C2 need new scenes.

**Picking the 2 levels of a factor:** the current winner's code is level 1 (control); level 2 is the strongest-for-gifts challenger
(`codebook.csv` + §2 validity), chosen so every grid cell is still a valid card. Levels are pre-registered before production.

### 6b. Grid layouts (balanced; each level sits in exactly half the ads)
Factors coded −/+ (− = control level). **8-ad, 4 factors** (H1, C2): A, B, C full, **D = A·B·C** (resolution IV: main effects are clean;
two-factor interactions are confounded in pairs, AB=CD, AC=BD, AD=BC).
| Ad | A | B | C | D |
|---|---|---|---|---|
| 1 | − | − | − | − |
| 2 | − | − | + | + |
| 3 | − | + | − | + |
| 4 | − | + | + | − |
| 5 | + | − | − | + |
| 6 | + | − | + | − |
| 7 | + | + | − | − |
| 8 | + | + | + | + |
**8-ad, 3 factors** (C1): drop column D (full factorial; all interactions estimable, under-powered). **4-ad, 2 factors** (H2): ads 1, 3, 5, 7 on A, B.
- Each main effect = 4 ads vs 4 ads ≈ 6,800 impressions per side → detects ≈ 2 points of hook rate (80% power).
- A cell that would be an invalid card (§2c) or cannot be built truthfully: swap which factor is D, or change a level; never drop a cell.
- The grid runs as a whole: stop at a pre-registered 50% or 75% checkpoint, never ad by ad (that breaks the balance). C0 ads can be stopped singly.
- Record the cell in `hooks.factor_design` (hook rounds) or `cells.axis` (concept rounds), e.g. `H1 grid ad 5: SU+ ON− PC− RV+`.

### Stops
C0: hook rate <18% after ~800 impressions → kill that ad. Grids: whole-grid checkpoints only. B: spend ≥ 3× break-even cost per sale
(~$75) with 0 purchases → stop; CPA ≤ break-even over ≥3 purchases → scale; CPA 1–2× with CTR ≥2.5% and many ATCs but few checkouts → fix the site.
Settled days only.

### 6c. Reading results by dimension
- **Unit = ad**, metrics with their denominators (the DB view already exposes them). A concept's result = all its ads, never its best ad (plan page rule).
- **Minimum before reading any ad:** settled days only; ≥814 impressions for a hook comparison, ≥76 3-second plays for hold (`ad-science` §5b), ≥1,700 impressions for coarse CTR.
- **Minimum before reading a code** (e.g. "EM2 vs EM1"): ≥4 ads per code, spread over ≥2 concepts *or* ≥2 products, and the two codes must not be aliased.
  A grid gives each level 4 ads per product, so a grid factor is readable within one product and confirmed on a second (Hook Lab coverage panel).
- **Grid reads:** main effect = pooled rate of the 4 "+" ads vs the 4 "−" ads; report it with its interval. A suspected interaction (the
  effect flips between halves) is a hint only: confirm with a small follow-up test, never read cells as winners.
- **Aliasing check:** before reading code X, the dashboard shows its co-occurrence table; if X always appears with Y (e.g. in Phase 1, BY2 always with PV1 and ST4), report "X+Y", not X.
- **Report effect + interval, vs a pre-named control**, never all-vs-all (`ad-science` §5e). Concept-level conversion comparisons are guardrails only (Tier C).
- **Hook × hold routing** (decomposition 2×2) per concept: low/low → core suspect; high hook/low hold → execution/body; low hook/high hold → hook only.

---

## 7. Data model (Supabase `mj4u-ads`; canonical CSVs in git first)

Migration `009_concept_framework.sql`, same conventions as 001–008: natural text keys, `ON DELETE RESTRICT`, every FK indexed, RLS `<table>_viewer_read` via `private.is_dashboard_viewer()`, created_at/updated_at + trigger.

```sql
-- codebook: every code of every dimension; FK target, so codes stay closed but can grow by INSERT
create table codebook (
  dimension  text not null,   -- angle|buyer_role|recipient|occasion|structure|pov|proof|prod_format|reveal|register
                              -- |f1_subject|shot_size|onset|caption_type|caption_band|caption_time|audio_cue|product_vis|people_f1
  code       text not null,   -- AN1, BY2, RC5, OC4, ST3, PV1, PF1, PX1, RV2, EM2, SU3, SZ1, ON3, CT1, LB2, TM2, AU1, VS3, PC2
  label      text not null,
  definition text,
  framework_version text not null default '2026-11-18',
  retired    boolean not null default false,
  primary key (dimension, code));

create table concepts (                       -- concept CORE (= "lý do mua")
  concept_id  text primary key,               -- SUN-K01
  product_id  text not null references products,
  name        text not null,
  angle       text not null, angle_dim      text not null default 'angle'      check (angle_dim='angle'),
  buyer_role  text not null, buyer_role_dim text not null default 'buyer_role' check (buyer_role_dim='buyer_role'),
  recipient   text not null, recipient_dim  text not null default 'recipient'  check (recipient_dim='recipient'),
  occasion    text not null, occasion_dim   text not null default 'occasion'   check (occasion_dim='occasion'),
  reason_line text not null check (array_length(regexp_split_to_array(trim(reason_line), '\s+'),1) <= 15),
  insight     text,
  core_key    text generated always as (angle||'·'||buyer_role||'·'||recipient) stored,  -- near-duplicate key
  critic_score numeric, critic_spread numeric,
  status      text not null default 'candidate',
  notes text, created_at timestamptz not null default now(), updated_at timestamptz not null default now(),
  foreign key (angle_dim, angle)           references codebook,
  foreign key (buyer_role_dim, buyer_role) references codebook,
  foreign key (recipient_dim, recipient)   references codebook,
  foreign key (occasion_dim, occasion)     references codebook);

create table executions (                     -- one build ("bản dựng") of a concept
  execution_id text primary key,              -- SUN-K01-X1
  concept_id   text not null references concepts,
  structure text not null, pov text not null, proof text not null, proof_2 text,
  prod_format text not null, reveal text not null, register text not null,
  -- (same *_dim + composite FK pattern to codebook for each column)
  logline text, beat_map text, cast_artwork text, hypothesis text,
  is_bundle boolean not null default false, bundle_note text,
  critic_score numeric, critic_spread numeric, status text not null default 'candidate',
  notes text, created_at timestamptz not null default now(), updated_at timestamptz not null default now());

alter table cells add column concept_id text references concepts,
                  add column execution_id text references executions,
                  add column round_type text check (round_type in ('C0','C1','C2','H1','H2','B','S')),  -- 013 (was R0–R4 in 009)
                  add column axis text;          -- e.g. 'core-BY', 'exec-EM', 'hook-VS×ON'
alter table ads   add column concept_id text references concepts,
                  add column execution_id text references executions;
alter table hooks add column f1_subject text, add column shot_size text, add column onset text,
                  add column onset_s numeric, add column caption_type text,
                  add column caption_words int check (caption_words >= 0),   -- >10 is a critic-gate fail, not a DB error (legacy H1 = 12)
                  add column caption_band text generated always as
                    (case when caption_words is null then null when caption_words=0 then 'LB0'
                          when caption_words<=4 then 'LB1' when caption_words<=7 then 'LB2' when caption_words<=10 then 'LB3' else 'LB4' end) stored,
                  add column caption_on_s numeric, add column audio_cue_type text,
                  add column product_vis text, add column people_f1 text,
                  add column factor_design text;   -- e.g. '2x2 VS×ON cell A1B2'
-- indexes on every new FK: idx_executions_concept_id, idx_cells_concept_id, idx_cells_execution_id,
-- idx_ads_concept_id, idx_ads_execution_id
```
**Views:** (1) `ad_performance` recreated as `a.* + concept core codes + execution codes + hook codes (F, T, HE1–HE9) + summed metrics`, so every code is a groupable column. (2) **`ad_dimension_long`** (`ad_key, dimension, code, impressions, video_3s, thruplays, link_clicks, spend, add_to_cart`): one row per ad × dimension, built by `UNION ALL` over the code columns; the dashboard groups by `(dimension, code)` for any dimension with one query and computes rates + intervals from the summed denominators. (3) `code_cooccurrence` (`dim_a, code_a, dim_b, code_b, n_ads`) for the aliasing check in §6c.
**Git side:** `_ledgers/codebook.csv`, `_ledgers/concepts.csv`, `_ledgers/executions.csv`; new columns in `cells.csv`, `hooks.csv`, `ads-legacy.csv`; `db_sync.py seed` upserts codebook first. Backfill Phase 1: `SUN-K01/K02/K03` with `-X1` from §3b, cells C1/C2/C3 → those ids, `is_bundle=true` on K02/K03 executions; the two shipped hooks tagged with HE codes (H1: SU3, SZ1, ON1, CT1, LB4 = 12 words, over the ≤10 card rule because it predates the team, TM1, AU0, VS3, PC0 · H2: SU2, SZ3, ON1, CT1, LB2, TM1, AU0, VS2, PC1).

---

## 8. Evidence gaps

1. **No study ties concept-level dimensions to Meta outcomes.** Message-strategy typologies (Taylor, Laskey, Frazer, Puto & Wells) are content-analysis tools; we could not verify any paper showing that a strategy *type* predicts paid-social performance. A 1995 Laskey/Fox/Crask JAR paper on strategy vs commercial effectiveness exists by title but its results could not be retrieved; not used.
2. **Motion-type tag reports** rank visual formats and hook tactics by hit rate / spend share across a BFCM-heavy window, with machine-labelled tags and no gifts vertical (`hook-framework` §8) [MODERATE]; nothing published by angle or persona for gifts. Claims like "different motivators unlock new audiences 89% of the time" (LinkedIn) are unaudited and not used.
3. **Narrative evidence is mostly lab and TV** (van Laer meta, Escalas, Quesenberry 30–60s Super Bowl). Transfer to a 15–25s, sound-off, AI-made feed ad is assumed.
4. **Giver-focus vs recipient-focus in ads** (PV1 vs PV2): the gift literature is about choices and appreciation, not about whose perspective an *ad* should take. Gap; PV is a test dimension, not a rule.
5. **Bittersweet (EM2) by buyer age:** Williams & Aaker predicts older buyers tolerate mixed emotions better; no ad test on Meta, and Meta age data are available only in aggregate. Test EM1 vs EM2 rather than assume.
6. **Hook element effects** (onset type, product-at-0s, caption type) come from lab attention studies and vendor lift claims; no first-party isolation of frame-1 visual vs caption vs audio (`01-03-hooks` §1b).
7. **Factorial cost estimate** assumes our §5b CPM and independent impressions; clustered delivery makes it a lower bound.
8. **Pizzetti & Gibbert (vicarious pride)** read from abstract/snippet; venue not verified. Treated as MODERATE.
9. **What fills the gaps:** our own ledger. After ≥3 rounds, read codes with ≥4 ads each; re-weight 00A's exploration floor toward codes that beat the round median, and retire codes that lose twice across products.
