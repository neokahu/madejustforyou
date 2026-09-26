# Existing video-ad scripting docs: audit against repo evidence

2026-09-26. Read-only audit of five docs, checked against the in-repo evidence listed at the bottom.
Scope: rules about **script structure, hooks, beats, pacing, product reveal, VO, captions, emotion, CTA**
(plus prompt-grammar rules where they decide what a scripted shot can be). Testing/budget rules are only
noted where they collide.

**Classes**
- **EVIDENCED**: traceable to a named winning ad, a repo measurement, or a named primary/external source.
- **PLAUSIBLE**: reasonable, but no source, or a vendor opinion only.
- **CONTRADICTED**: evidence in the repo says otherwise.

**Evidence base caveat.** No competitor transcript was ever captured (WinningHunter `download_failed` / 502
on every attempt). What we know about winning *scripts* comes from poster frames, captions, copy, longevity
and one motion measurement (the Macorner visor, n=1). Beat-by-beat claims about competitor VO cannot be
evidenced from this repo. That gap is the main reason PLAUSIBLE dominates.

Doc abbreviations: **PB** = `ai-emotional-video-ad-playbook.md` · **DEC** = `video-ad-decomposition-2026.md` ·
**DIR** = `ad-video-director-research.md` · **TPL** = `templates/film-script-template.md` ·
**AFS** = `ai-film-studio.md` (demoted) · **§05** = testing-plan-page §05 (approved framework).

---

## 1. Summary counts (script-relevant claims only)

| Doc | Evidenced | Plausible | Contradicted | Notes |
|---|---:|---:|---:|---|
| PB (playbook, 2026-08-05) | 8 | 11 | 8 | Oldest. Several unsourced stats. Its worked example is the MJ4U-111 lamp |
| DEC (decomposition, 2026-09-13/18) | 12 | 19 | 4 | Best-sourced and self-labels [DATA]/[OPINION]. Weakness: niche tailoring is qualitative, and its format table leaves out the format the winners actually use |
| DIR (director research, 2026-09-18) | 9 | 8 | 3 | Only doc with our own measurements. Its prompt-grammar section is now partly overturned by `seedance-prompt-method.md` |
| TPL (script template) | 3 | 5 | 6 | Encodes MJ4U-111 decisions as defaults |
| AFS (film studio, demoted) | 3 | 6 | 7 | Every structural rule inherited from MJ4U-111 is either contradicted or unevidenced |
| **Total** | **35** | **49** | **28** | |

About 31% of claims are evidenced. The contradictions cluster on three topics: **product-reveal timing**,
**pacing/transitions**, and **"AI can't do text/people"**.

---

## 2. EVIDENCED rules worth keeping

| # | Rule | Where stated | Evidence |
|---|---|---|---|
| E1 | **The first 3s decide the ad.** Hook gets tested first and most | DEC, DIR, PB, TPL | Meta/Nielsen: ~47% of value in first 3s; 65% reach 10s (DEC, facebook.com/business). AdLibrary: same body, 3 hooks, 18%→38% |
| E2 | **The viewer knows what gift is sold within 3s. Product/personalization is on screen from frame 1** | §05 ("3 giây đầu phải lộ ra đang bán món quà gì"), DIR §2 | Macorner candle-warmer winner (ad 3999351280199871, 122d, "Winning"): opens on ECU of the lampshade, 5 names legible in <1s (`candle-warmer.md` §Hook). Macorner visor winner (333d) is hottest at second 0 (DIR §0). Kantar 2026: brand in ≤2s, product-forward in first 10s (DIR §2) |
| E3 | **The personalization IS the ad.** The printed names/photo are the hook and the proof. Show ≥3 real names legibly | DEC format #1 "reveal = HIGH", TPL rule, PB "name-stacking" | Macorner: "the personalization line printed on the product does the selling" (`macorner.md` §3). WP: "The personalization IS the ad" (`wanderprints.md` synthesis). Roster mechanic in nearly every grandparent winner (`competitor-spy.md` §4) |
| E4 | **Burned-in captions carry the story, legible with sound off** | PB §2, DEC, AFS rule 9, TPL, §05 | Candle winner = "subtitled micro-story, ~15–20s", lower-third white-box captions, "one for every child she's watched grow" (`candle-warmer.md` pattern 4). ~80–85% of plays are sound-off (Meta, DEC) |
| E5 | **Length ~15–20s for cold Meta** | PB (15–30s), DEC (6–15s Feed, 15–30s skeletons) | Candle winner 19s. Macorner visor 17.7s. MJ4U-111 at 36.6s failed (DIR §0: "2.1× too long") |
| E6 | **Front-loaded motion; hard cuts, not crossfades** | DIR §0/§3/§5.3 | motion_qa: winner hook3 18.05 vs MJ4U-111 3.59; winner 7 hard cuts (0.40/s) vs ours 1 (0.03/s). `scdet` could not see our crossfades at all. Treat as n=1 |
| E7 | **Don't end on a frozen end card** | DIR §0 ③ | Our last 3s measured 0.00–0.01 motion; winner ends on a 23.08 spike |
| E8 | **Memorial / "always with you" is the strongest, most durable angle**, and it resolves grief into warmth | PB §1, DEC angle #5 | Macorner #1 ad ~1005d (photo pillow). WP bracelet 803d, collar frame 757d. PFG "Always With You" 18 creatives. TikTok "in heaven" 6.0M views (`competitor-spy.md` §7) |
| E9 | **Living-legacy framing (present tense) is the proven grandparent default. Memorial is a separate variant** | (none of the five docs state it; `candle-warmer.md` pattern 4) | Candle winner is "NOT positioned as memorial... present-tense ('watched grow')" |
| E10 | **Sell emotion, not a discount. No % off or countdown in the ad** | DEC offer ranking ("discount last"), PB §0 "never a feature list" | Macorner, PFG, candle winner: no discount/urgency in-ad. WP: soft WP10 code only (`wanderprints.md` offer). Non-personalized candle warmers are the ones leaning on "50% OFF" |
| E11 | **Headline pattern `[emotional one-liner] – Personalized Gift For [recipient]`** | PB §1 | Macorner verbatim ("Congrats On Being My Husband… - Personalized Gift For Husband, Boyfriend", `macorner.md` §3) |
| E12 | **CTA button = Shop Now** | §05, DEC | Candle winner SHOP_NOW. PFG "SHOP_NOW universally" (`pfg.md`) |
| E13 | **Occasion is a re-skin of an evergreen roster, not a separate concept** | DEC format "occasion HIGH" (partly) | PFG snowman (Christmas skin, rank #1). Newsvips "little monsters" (Halloween skin, 1061d). "As 2026 begins" injected into evergreen copy (`pfg.md` Hero 4, `competitor-spy.md` §4) |
| E14 | **Concentrate on a proven hero: many light variants of one winning angle** | DEC velocity mode (10–20 hooks) | PFG 18 creatives on one URL. Macorner Legend 18 across 5 pages. Macorner candle = "one winning angle, lightly varied". *But* WP rides 1–4 creatives for 800d, so volume isn't required |
| E15 | **Emotion is written as physical detail, not adjectives** | PB §4 ("physical tell"), `seedance-prompt-method.md` rule 5 | BytePlus official Seedance guide; Test E relief row reproduced |
| E16 | **One camera move per shot, and the opening shot must move** | PB §4, DIR §4a, TPL | BytePlus official. testC2 (fixed open) hook3 5.87 fail vs testC3 (moving open) 14.68 pass |
| E17 | **Two named shots per generation (Shot 1 / Shot 2), not one** | none of the five docs, only `seedance-prompt-method.md` | Test E: one shot hook3 8.10, cuts 0.0 → two shots 14.90, cuts 0.21 (same model) |
| E18 | **Pin the product with a constraint that names the failure mode** | none of the five docs (DIR says the opposite) | testC→testC2: "the dog stays seated" / "shadow's outline does not change" fixed the morph |
| E19 | **Animate from a real product still. Never let the model draw the product** | PB §3.3, AFS rule 4 | Test F: model-drawn close-ups deform geometry and letterform. Test E ⚠6: the model invented a stained-glass window. Ken Burns on a 4K still passes the gate with correct lettering |
| E20 | **Text in close-up proof shots of a rigid product: 4K still + ffmpeg push, not video i2v** | none (supersedes AFS rule 5 / TPL) | `product-text-fidelity-2026.md`: testF2 letterform drifts; kenburns-native passes the gate with correct lettering |
| E21 | **Emotional short film = MEDIUM, not the cold default** | DEC format table, DIR §2 | MJ4U-111 failed the motion gate 3 of 4; DIR's head-to-head |

---

## 3. CONTRADICTED rules and the contradicting evidence

| # | Rule (doc) | Contradicting evidence |
|---|---|---|
| C1 | **"Product reveal at ~60% mark — never earlier"** (TPL header; AFS hard rule 8, "product as plot payoff") | Candle winner shows the product and names in <1s. Kantar: brand ≤2s. §05 (approved) requires the gift to be identifiable in 3s. **Worst contradiction: it is still the template's default** |
| C2 | **"First 3s = … a face on screen"** (TPL notes); **"A face holds viewers 49% longer… first frame = movement or a face"** (PB §2, unsourced stat) | Candle winner: "no UGC face, no talking head", opens on a product ECU. Macorner's creative anatomy is "product beauty-roll / hand-holding the personalized item". None of the longevity winners open on a face |
| C3 | **"UGC-style wins emotional/gift (4.2× engagement, 2.8× conversion)… giftee's reaction beats the buyer's"** (PB §2, unsourced) | Every teardown winner is a product-demo/emotional-montage video (PFG: "every single winning creative is a VIDEO… product-demo/emotional montage"). No UGC face in any evidenced winner. *(Caveat: no transcripts, so a reaction shot mid-video can't be ruled out.)* |
| C4 | **"Video fatigues in ~9 days; refresh every 7–10 days"** (PB §5) and **"refresh every ~2–3 weeks"** (DEC) | WP winners ride **1–4 creatives for 757–1,042 days** (`wanderprints-deep-crawl.md`: median 816d). Macorner pillow ~1005d. Fatigue is not the binding constraint in this niche |
| C5 | **Crossfades between scenes** (AFS Phase 4 / editor role; implied by TPL's cool→warm "match-cut" style) | scdet: 1 detectable cut in 36.6s. Hook3 3.59 vs 18.05 (DIR §0) |
| C6 | **Uniform ~5s beats** (AFS "4–5s"; TPL "4–5s"; **§05's own example: "Mỗi cảnh ~5 giây" for suncatcher and blanket**) | Winner cuts every 2.5s. MJ4U-111 "every clip exactly 5.0s" measured as a cause of flatness (DIR §0). DEC's "~5s/cut for UGC/authenticity" is [OPINION] from an external VN table, and §05 applies it to non-UGC formats |
| C7 | **"AI garbles printed text → composite real text in post" as a blanket rule** (AFS rule 5; TPL "legible via composite, not AI text"; PB "video models mangle text") | Test F stage 1: all three image models render "Alex" cleanly. Test D: a ~50-word poem held word-perfect in stills *and* video. The narrower true rule is E20 |
| C8 | **"Minimise humans — dodges faces/hands"** (PB §3.5 rationale) | Test E: Seedance 2.0 held identity and five-fingered hands in all runs. The *default* can stand (winners are product-hero, E2), but the reason given is wrong |
| C9 | **PB worked example: MJ4U-111 lamp as a "memorial-adjacent warmth angle", grandmother's hand entering, dusk** | Candle teardown: the winner is explicitly **not** memorial ("present-tense living legacy"). It opens on the lampshade ECU with a caption, not a mood shot. The example teaches the losing version |
| C10 | **Timeline prompting `[0s] [2s] [4s]`** (DIR §4b) | BytePlus official: "precise timing (0–3s) is unstable… may lead to abnormal generation". Storyboard by named shot instead (`seedance-prompt-method.md` rule 3, verified testC3/E3) |
| C11 | **"[NEG] last, minimal, never load-bearing" / "negation is not a control surface"** (DIR §4a) | testC2: the load-bearing fix *was* a constraint line ("The dog stays seated"). BytePlus: "Constraint words are very important" |
| C12 | **"Every beat shows relationships/family"** (TPL notes; AFS rule 10) as a structural requirement | Winners contain no people at all. The relationship is carried by the **roster text + caption** ("one for every child she's watched grow"). The lonely-giftee rule is still valid for shots that *do* show a person |
| C13 | **Cool→warm grade arc (rain-blue → gold at reveal)** (TPL rules; AFS rule 8) | Unevidenced in any winner. It came only from MJ4U-111 (failed). The candle winner is warm/neutral beige from frame 1. Counted contradicted because the only test of it lost |
| C14 | **Single-shot AI prompt with "No on-screen text" boilerplate** (TPL scene block) | Test E: one shot → cuts 0, hook3 8.10. Generic "no text" = the boilerplate the TopView contract bans (`seedance-prompt-method.md` audit). Template needs the two-shot recipe + a failure-mode constraint |
| C15 | **"Put the reveal at the MID-point, not the end"** (DEC skeletons; repeated in §05) as the *first* product appearance | Holds only if the product/gift is already identifiable in 0–3s (E2). As written, Skeleton B ("product teased", reveal 10–16s) conflicts with §05's own 3s rule and with the candle winner. Reconcile it: gift visible at 0–3s, name/roster **payoff** at mid |
| C16 | **Suncatcher example script in §05 opens "0–2s Cận mặt chủ của Max"** (owner's face) with the product at 6–12s | Same evidence as C1/C2. The hook-1 on-screen text ("That's his actual breed — and his name") partly rescues the 3s rule, but the picture doesn't show the gift until 6s |

---

## 4. Inter-doc conflicts

| Topic | Doc A says | Doc B says | Which the evidence favours |
|---|---|---|---|
| Hook share of performance | PB: "71–80% of performance" (unsourced) | DEC: "up to 47% of value in first 3s" (Meta/Nielsen) | DEC. Drop PB's figure |
| Hook-rate kill line | PB: <15% kill, 45%+ elite | DEC: <20% rebuild, 40%+ elite. DIR/§08: T0 red line <21% | DEC/§08 (the approved one) |
| Hold rate | PB: 15–25% "healthy" (15s/impr) | DEC: 40–50% good (15s÷3s) | Different denominators, not a real disagreement. PB should be deleted to stop the misreading |
| Product timing | TPL/AFS: ~60%, never earlier | DIR: brand ≤2s, product-forward first 10s. §05: identifiable in 3s. DEC: reveal mid-point | DIR + §05 (see C1, C15) |
| Opening frame | TPL/PB: a face | DIR §4c: text-first or pattern interrupt. Candle winner: product ECU + caption | Product ECU + caption (evidenced). Text-first is plausible |
| Pacing | AFS/TPL/§05 example: ~5s scenes | DEC: cuts every 1–2s short-form; DIR: 1.5–3s in the opening | DIR/DEC (winner 2.5s/cut) |
| Transitions | AFS: crossfades | DIR: hard cuts default, crossfade only for a time jump | DIR (measured) |
| Text on product | AFS/TPL/PB: never AI text, always composite | `product-text-fidelity-2026.md`: stills fine; video fine on cloth; rigid close-up → Ken Burns | product-text-fidelity (measured) |
| Timing marks in prompts | DIR: `[0s][2s][4s]` | seedance-prompt-method: named shots, no timecodes | seedance-prompt-method (official + measured) |
| Negatives/constraints | DIR: never load-bearing | seedance-prompt-method: constraints naming the failure mode are essential | seedance-prompt-method (testC2) |
| The word "cinematic" | DIR: ban it | seedance-prompt-method's verified template ends "…cinematic texture" and passed | Unresolved. Low stakes: DIR's ban is vendor opinion, and the passing template used it only in the trailing style line |
| Model for people | DIR §4d: Kling for character | seedance-prompt-method Test E: Seedance 2.0 for people (2.5 worse) | Seedance 2.0 (measured). Kling untested |
| Hook variants per film | AFS: 5 hooks, each a different methodology | §06 (approved): exactly 2 (name-shown vs relationship) for Phase 1 | §06 is the decision in force |
| Test structure | PB: 1 creative per ad set, ABO | DEC: 3–5 creatives per ad set | Out of script scope; §07/§11 govern |
| Offer urgency | DEC: order-by-date = #1 offer | Candle teardown: "if we test urgency at all, soft gift-timing"; evergreen winners carry none | Neither is contradicted. Deadline is a seasonal skin (E13), not a default |
| VO | DEC: real human VO, never synthetic (opinion) | AFS: captions default, VO optional; `competitor-spy`/teardowns can't say (no transcripts) | Unresolved. Human VO is PLAUSIBLE, and §05 already picks it only for the blanket |

**Duplicates** (same rule restated, which invites drift):
- Hook library / tier ranking: DEC §Hook tactics ≈ §06 (the page cites DEC as its source).
- Captions sound-off: PB §2, DEC, AFS rule 9, TPL.
- One camera move: PB §4, DIR §4a, TPL, AFS director role, seedance-prompt-method rule 1.
- Lonely-giftee rule: TPL, AFS rule 10, memory.
- Beat skeleton A: DEC and §05 carry the same 30s beat sheet verbatim.
- Real product still → i2v: PB §3.3, §3.5 and AFS rule 4.

---

## 5. Inherited from MJ4U-111 without support

MJ4U-111 scored hook3 3.59 vs 18.05. These rules exist *because* that film was made that way, and no
winner or measurement supports them:

1. **Product at ~60%** (TPL, AFS rule 8): contradicted (C1).
2. **Suspense → family-secret reveal story shape** (TPL header example): unevidenced. No winner uses suspense.
3. **Cool rain-blue → warm gold grade** (TPL, AFS): unevidenced (C13).
4. **Crossfades + match cuts** (AFS editor): contradicted (C5).
5. **Uniform 4–5s scenes, ~9 clips, ~35s film** (AFS §4 cost model, TPL): contradicted on length (E5) and pacing (C6).
6. **Logo end card** (AFS): measured as 3s of zero motion (E7). Keep a CTA card only if it moves.
7. **Notebook/insert names match-cut to product** (TPL): plausible craft. It is harmless but it came from that film's plot device.
8. **"Memorial-adjacent" framing of the Grandma's Garden lamp** (PB worked example): contradicted by the teardown (C9).
9. **15s FB cut of the film** (AFS Phase 4): DIR §2 argues a compressed slow-build loses its payoff. Untested.
10. **Thai-ad film as the house format** (memory `ad-style-thai-emotional-film`, AFS purpose): DEC rates it MEDIUM and DIR shows it lost. Keep it for warm/brand use only.

What survives from AFS on independent evidence: the turntable/reference gate (E19 capability plus Test E identity
hold), "use the real product image" (E19), and "avoid mechanical hand-object actions" (PLAUSIBLE; not
contradicted, since Test E tested hands but not object manipulation).

---

## 6. Recommendation: merge / retire

1. **Retire `ai-film-studio.md` as a scripting source.** Its demotion banner is correct. Move its only
   surviving script-relevant rules (turntable gate, real product image, no mechanical hand actions) into the new
   method doc, then leave AFS as a pipeline/folder-convention note only.
2. **Rewrite `film-script-template.md`. Don't patch it.** It is the most dangerous doc because it is a
   *default*: product ≥60%, face-first, cool→warm, single-shot prompts. Replace it with the §05 12-field brief
   plus a shot block that follows `seedance-prompt-method.md` (two named shots, the opening one moving,
   `<Subject>` labels, a failure-mode constraint, no generic "no text"). Add the fields it lacks: 3s
   gift-identification check, proof beat, cut rate as a number, length, and the text-shot method (E20).
3. **Retire `ai-emotional-video-ad-playbook.md`.** Keep E8/E11 (recipient × emotion table, headline formula)
   by moving them into DEC's angle library. Delete its unsourced stats (71–80%, 49%, 4.2×/2.8×, 9-day
   fatigue), its hook/hold benchmarks (superseded by DEC/§08), and its MJ4U-111 worked example. Its
   toolchain section (Sora, CapCut, Hailuo) is out of date against memory (PIL+ffmpeg, TopView plates).
4. **Keep `video-ad-decomposition-2026.md` as the strategy source of truth, with three fixes:**
   (a) add **"product-hero ECU + subtitled micro-story"** to the format-fit table as HIGH/EXACT. It is the
   format the evidenced winners use, and it is missing; (b) restate "reveal at mid-point" as
   "gift identifiable 0–3s, personalization *payoff* at mid-point" (C15); (c) flag the 5s/cut row as
   UGC-only and unmeasured (C6). Also demote "reaction = #1 proof" and "UGC-raw HIGH" from [EXACT]-sounding
   to *untested in our niche*. No evidenced winner is reaction-led.
5. **Keep `ad-video-director-research.md` for its §0 measurements and §2–§3 diagnosis.** Strike §4a's
   NEG rule and §4b timeline prompting (C10, C11), and point §4 at `seedance-prompt-method.md` as the
   authority for prompt grammar. Its §5 "separate repo" spec is unaffected by this audit.
6. **Fix §05's worked example before it becomes the next template.** The suncatcher opens on a face with
   product at 6s, and both suncatcher and blanket are paced at ~5s/scene. Both contradict evidence, and
   the suncatcher opening also cuts against §05's own 3s rule.
7. **Close the evidence gap first:** re-attempt `get_ad_transcript` on the candle winner
   (`media.winninghunter.com/.../ab7021e4….mp4`, URL in `candle-warmer.md`) and run `motion_qa.py` on
   ≥10 more longevity winners. The DIR benchmark is n=1. Every beat-level rule above rests on one visor ad
   and one poster frame.

---

### Evidence read
`research/sprints/2026-08-competitor-creative-teardown/{macorner,wanderprints,candle-warmer,pfg}.md` ·
`research/sprints/2026-07-competitor-ad-scoring/{README,wanderprints-deep-crawl}.md` ·
`research/sprints/2026-09-grandparents-day/competitor-spy.md` · `research/reference/seedance-prompt-method.md` ·
`research/reference/product-text-fidelity-2026.md` · `marketing/facebook-ads/testing-plan-page/index.html` §02, §05, §06.
