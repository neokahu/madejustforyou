# Video team: Role 06 Editor/Assembler and Role 07 QA/Gatekeeper

Researched 2026-11-18. Scope: the last two roles before an ad reaches Ads Manager. These roles do not depend on any tool. They define decisions, specs, checks and gates. Any editor, renderer, generator or voice engine can carry them out. Measurements say what to probe (codec, fps, loudness), not which program does the probing.

**Grades.** [STRONG] = first-party platform document, published standard or statute, or our own repeated measurement. [MODERATE] = consistent third-party data or several independent practitioner sources. [WEAK] = one source, opinion, vendor marketing, or n=1.
**Internal sources** (repo paths): `EDIT-CRITERIA.md` and `CAPTION-SHEET.md` = `marketing/facebook-ads/suncatcher-phase1/`. `FEED` = `research/reference/feed-video-best-practice.md`. `CAP` = `research/reference/short-form-caption-design.md`. `SM` = `research/reference/script-method.md`. `DIR` = `research/reference/ad-video-director-research.md`. `TMF` = `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md`.

---

## 1. Evidence summary

### a) Meta paid-video specs (2026)
| Claim | Grade | Source |
|---|---|---|
| Reels (FB and IG): ratio 9:16. **Recommended resolution 1440×2560.** H.264, square pixels, fixed frame rate, progressive, stereo AAC ≥128 kbps. No edit lists or special boxes in the container. Captions "optional, but recommended". Sound "optional, but strongly recommended". | STRONG | [Ads Guide FB Reels](https://www.facebook.com/business/ads-guide/update/video/facebook-facebook-reels), [IG Reels](https://www.facebook.com/business/ads-guide/update/video/instagram-reels) |
| Length: FB Reels has "no maximum". IG Reels allows 0s–15 min. Max file size 4 GB. The length limit never binds for us. Length is a creative and test decision. | STRONG | same |
| **9:16 safe zone: keep ~14% top, 35% bottom and 6% each side free of text, logos and key elements.** The same zone applies to Stories, Reels, 9:16 Feed and FB in-stream reels. With a disclaimer, keep the bottom 40% free. Ads Manager has a "Safe Zone guardrail" overlay. | STRONG | [Meta: text overlays & safe zones](https://www.facebook.com/business/help/980593475366490) |
| At 1080×1920 these are 269 px top / 672 px bottom / 65 px sides. The right-hand action rail covers the bottom ~40% of the lower-right corner. | MODERATE (third-party pixel maps of Meta's %) | [AdKit](https://adkit.so/tools/safe-zones/facebook), [adsuploader](https://adsuploader.com/blog/meta-ads-safe-zones) |
| FB Feed: 4:5 recommended, 1440×1800. IG Feed: Meta now lists 9:16 as recommended. A 9:16 asset in IG Feed follows the Reels safe zone. Supply one asset per placement through **asset customization**. | STRONG | `FEED` §1–5 (Ads Guide links inside) |
| 4:5 Feed has **no published pixel safe zone**. Our working margin is ≥10% bottom and ≥6% sides. | WEAK (house inference) | `FEED` §6 |
| Meta's creative guide says Feed ads should be ≤15s with the main message in the first 3–5s. We accepted a 20s length on 2026-10-09 (F4 waiver). | STRONG (as guidance) | `FEED` §11; `EDIT-CRITERIA` re-audit |
| Advantage+ creative features (`video_auto_crop`, `text_optimizations`, `inline_comment`; also music, overlays and touch-ups in the UI) **generate per-viewer variations of the ad**. Each can be opted out separately. | STRONG | [Meta dev blog v22](https://developers.facebook.com/blog/post/2025/01/17/marketing-api-v22-impacts-to-advantage-plus-creative-enhancements), [Standard enhancements](https://developers.facebook.com/docs/marketing-api/advantage-catalog-ads/standard-enhancements) |

### b) Captions for sound-off viewing
| Claim | Grade | Source |
|---|---|---|
| Design for sound-off and caption the whole story. Text should be large, clean, high-contrast, carry one message per screen, and not block the visuals. | STRONG (Meta; partly 2016-era) | [Meta safe-zone/text page](https://www.facebook.com/business/help/980593475366490); `FEED` §7–8 |
| Treatments rank **solid box > outside outline ≥8–12 px at 1080w > drop shadow > colour alone**. A shadow alone fails over light glass (we saw this in the suncatcher audit, E29). | STRONG (verified 3-0 + own audit) | `CAP`; `EDIT-CRITERIA` E29 |
| WCAG contrast: 4.5:1 for normal text, 3:1 for large/bold. Test at the lowest-contrast region the text passes over. | STRONG (standard) | [WCAG 2.2](https://www.w3.org/TR/WCAG22) via `CAP` |
| Reading speed: Netflix allows ≤20 cps for adults and 17 cps for children. BBC recommends 160–180 wpm (≈0.33 s/word). DCMP gives a ≥2 s minimum. Netflix allows 5/6 s to 7 s per event, with a ≥2-frame gap between events. | STRONG (first-party style guides; written for subtitles, not ads) | [Netflix TTSG](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide), [summary](https://www.captioncraft.studio/guides/subtitle-guidelines) |
| Our house rule is **≤2.5 w/s and ≥2.0 s on screen, with no blank flashes**. It is stricter than BBC because the viewers are scrolling past, and the user found 4 w/s unreadable. | STRONG for us (direct user test) | `CAPTION-SHEET` D3 |
| **Word-by-word ("karaoke") captions: there is no controlled study showing they lift ad retention.** The claims for them come from vendors. Accessibility writers argue that pop-in word-by-word removes read-ahead and phrase structure and adds load. A "highlight inside a stable phrase" style keeps the context. | WEAK (both sides) | [disabled-world](https://www.disabled-world.com/disability/accessibility/karaoke-captions.php) (cites Rajendran et al. 2013 on segmentation), vendor pages ([recapo](https://recapo.ai/blog/how-to-add-word-by-word-captions)); `CAP` "no verified evidence that animation lifts retention" |
| Specific uplift figures ("+12% view time", "+80% completion", "% of frame size") are refuted or unverified. Do not cite them. | STRONG (as a negative finding) | `CAP` refuted list |

### c) Audio
| Claim | Grade | Source |
|---|---|---|
| **Meta: Reels ads "should not contain licensed music". It recommends original audio or royalty-free tracks from the Meta Sound Collection.** | STRONG | [Ads Guide IG Reels](https://www.facebook.com/business/ads-guide/update/video/instagram-reels) |
| The Instagram/Facebook consumer music library is licensed for personal use only. Boosted or paid use can be muted or rejected. The Sound Collection is cleared for ads on Meta surfaces only. Third-party library licences must name paid social or advertising. **Keep the licence or receipt with the asset.** | MODERATE (several licensing vendors agree; one blog dissents on the Sound Collection for ads, so check the in-product eligibility mark) | [Soundstripe](https://www.soundstripe.com/blogs/royalty-free-music-for-instagram-ads), [audiodrome](https://audiodrome.net/for-creators/meta-sound-collection), [foximusic](https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide) |
| AI-generated music has the same problem: the rights come from the generator's commercial terms on the date the track was generated. Record the plan, the terms URL and the date. | WEAK (inference; no source found) | none: treat as a gap |
| Meta publishes **no LUFS target**. The working norm is about −16 LUFS integrated for mobile/streaming music. AES TD1008 gives −16 for music, −18 for speech or mixed content, and **true peak ≤ −1 dBTP at the codec input**, because lossy encoding raises peaks. | STRONG (TD1008 standard) / MODERATE (applying it to Meta) | [AES TD1008 summary](https://elephantaudio.pk/reference/aes-td1008), [soundeducation](https://www.soundeducation.fm/specs/aes-td1008); `FEED` §16 |
| Music plus VO beat no music/VO by +15 points on a "positive response score" (Meta research, quoted second-hand). | WEAK (we could not reach the primary source) | [Shuttlerock](https://www.shuttlerock.com/resources/how-to-build-effective-ad-creative-instagram-reels) |
| VO intelligibility: duck music 6–10 dB under VO. Speech presence lives at about 2–5 kHz. | WEAK (practitioner) | [vibesdrop](https://vibesdrop.com/best-practices-mixing-music-voiceovers-reels) |

### d) Editing for retention
| Claim | Grade | Source |
|---|---|---|
| Crossfades are invisible as edits: our 36.6s film had 1 detectable cut against 7 in a 333-day winner. It also ended on 3 s of zero motion. | STRONG (own measurement, n=1 pair) | `DIR` §0 |
| For gift ads, about 2–5 s per shot with varied lengths. The gift median is 0.22 cuts/s. For emotional story ads the user asked for slower cutting, and one shot per beat won that argument. | MODERATE / user-decided | `SM` R11; `EDIT-CRITERIA` D1 |
| Brand, product or person should appear early; Meta's examples are the 2016 Finish and Wells Fargo tests. The closing frame should move rather than freeze on an end card. | STRONG (old) / WEAK (n=1) | `FEED` §10; `SM` R12 |
| One CTA, held ≥2 s at the end, inside the safe zone. | STRONG (single CTA) / WEAK (2 s) | `FEED` §14 |
| **J/L cuts, beat-matching, cut-on-motion:** we found no ad-performance evidence. They are craft lore. | WEAK | none found |
| Post-production can destroy energy that the shots had (crossfades, uniform 5 s beats, frozen end card). | STRONG for us | `DIR` §3 |

### e) QA methodology and policy
| Claim | Grade | Source |
|---|---|---|
| Broadcast QC groups its checks into file conformance (codec, container, duration, frame count), picture (black, freeze, flash frames, levels), sound (loudness, true peak, silence, clipping, channel layout), captions (present, in sync, readable, inside the safe area) and compliance. **Automate what can be measured, keep people on judgement, and record results with timecodes.** | STRONG (industry consensus; EBU QC catalogue) | [metavert QC overview](https://metavert.io/video-quality-control), [N.White](https://nwhite.systems/resources/learn/broadcast-qc), [Broadcast Bridge](https://www.thebroadcastbridge.com/content/entry/8002/understanding-quality-control-for-file-based-video-workflows) |
| Photosensitivity: no more than 3 general or red flashes in any 1 s (WCAG 2.3.1). Broadcasters test with Harding-type analysers. | STRONG (standard) | [WCAG 2.2](https://www.w3.org/TR/WCAG22), [Harding test](https://en.wikipedia.org/wiki/Harding_test) |
| A motion score detects the *absence* of energy. It cannot certify good motion, and it cannot read printed text. The name must be read by eye on ≥5 frames. | STRONG (own) | `DIR` §0; `SM` R23 |
| Meta does not allow ads that assert or imply the viewer's personal attributes (age, health, religion and so on), including by asking a question. Ads must accurately represent the product. | STRONG | [Meta personal attributes](https://www.facebook.com/business/help/2557868957763449), [policy checklist](https://www.facebook.com/business/help/757209948405699) |
| AI labels: Meta auto-labels ads when it detects C2PA or other AI metadata ("AI info"). Advertisers can self-disclose in some regions, **including California and New York**. Disclosure is *mandatory* only for social-issue, election and political ads. | STRONG | [Meta: AI info on ads](https://www.facebook.com/business/help/1010479435004531), [Meta Help](https://www.meta.com/help/artificial-intelligence/355108217670024) |
| A third-party claim says undisclosed photorealistic-person AI ads are now rejected (2026). | WEAK (not in Meta's own pages) | [commonthreadco](https://commonthreadco.com/blogs/coachs-corner/meta-ai-ad-labels-mandatory-disclosure-ecommerce-2026) |
| **New York GBL §396-b (in effect 2026-06-09): an ad that features a "synthetic performer" (an AI person not recognizable as a real one) must disclose this conspicuously, where the advertiser knows. Penalties are $1k for a first violation and $5k after.** Our AI-cast story ads shown to NY viewers appear to be in scope. | STRONG (statute + governor) | [NY Senate S8420A](https://www.nysenate.gov/legislation/bills/2025/S8420/amendment/A), [Governor](https://www.governor.ny.gov/news/governor-hochul-announces-first-nation-law-requiring-disclosure-when-advertisements-include-ai), [Skadden](https://www.skadden.com/insights/publications/2026/01/two-newly-enacted-new-york-laws-will-regulate) |
| The FTC rule (in effect 2024-10-21) bans fake or false consumer testimonials, including AI-generated ones. It does not ban AI avatars as such. A dramatized story must not be presented as a real customer's review. | STRONG (rule) / MODERATE (applied to our format) | [FTC rule](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials), [FTC Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) |
| Test integrity: each variant differs from baseline **only on the tested axis**. Code every combination. | STRONG for us (house framework) | `TMF` Part C, E |
| We found no Meta-specific rule on grief or memorial imagery. The general "low quality / disruptive / sensational" policy applies. | gap | none |

### f) Asset management
| Claim | Grade | Source |
|---|---|---|
| Ad names should encode a stable creative ID, concept, hook, format/ratio and version. Assign the ID **before** launch, because platform IDs change on duplicate or relaunch. | MODERATE (practitioners agree) | [admanage](https://admanage.ai/blog/ad-creative-naming-conventions), [apogee](https://www.apogee.ad/en/blog/nomenclature-meta-ads-guide), [adlibrary](https://adlibrary.com/posts/meta-ads-campaign-naming-conventions) |
| One row per ad, with the matrix factors as columns plus per-stage metrics. Log covariates. | STRONG for us | `TMF` Part F |
| Media stays out of git and is backed up to Drive. The tracker CSV and its Sheet mirror are updated together, by one writer. | STRONG for us (user directives) | memory: media-backup-drive-rclone, product-tracker-and-sheet-sync |

---

## 2. Role 06: Editor / Assembler

**Mission.** Turn locked inputs into the exact deliverables the test plan calls for. Every ad gets two placement cuts. Each is reproducible from a recipe and handed to QA with a self-check. The editor adds **no creative decisions** that are not in the locked script, caption sheet or criteria sheet. Each judgement call is written down as a flagged question.

### Inputs (all must be LOCKED before assembly starts; a missing lock = stop and ask)
1. **Test plan / cell map**: which ads exist, the variable each one tests, and what must stay identical (`TMF` Part E table, or the plan page).
2. **Locked script**: beat map, lengths, on-screen text and VO lines verbatim.
3. **Accepted shots**: only takes that passed the upstream shot gate (identity, scale, morphs, printed text). Record in/out points per shot.
4. **Caption sheet**: final text, timings, band per format, treatment (template: `CAPTION-SHEET.md`).
5. **Criteria sheet for this batch**: compiled from every relevant research doc **before** rendering (template: `EDIT-CRITERIA.md`, rule from memory follow-plan-page). Conflicts are resolved by the user, not the editor.
6. **Audio**: the music bed plus its **licence evidence** (source, licence type, ad use allowed, receipt or terms URL with date). Any VO comes with its script and voice choice.
7. **Brand assets**: logo lockups for both formats, the CTA text, and the personalization artwork from the real product file. The product is never redrawn.

### Outputs (per ad)
| Deliverable | Spec |
|---|---|
| `…_916` Reels/Stories cut | 9:16. Target 1440×2560; 1080×1920 is the floor. Don't upscale sources below 1080 and call the result 1440 (`EDIT-CRITERIA` F2). H.264, constant fps equal to the source fps (no mixed rates), progressive, square pixels, stereo AAC ≥128 kbps, no edit lists. |
| `…_45` Feed cut | 4:5. Target 1440×1800; 1080×1350 is the floor. **Re-framed per shot** (no letterbox, no blind centre crop). Same audio, captions re-banded for 4:5. |
| Name | `{PRODUCT_ID}_{CONCEPT}-{HOOK}_{VAR}_{RATIO}_v{NN}`, e.g. `MJ4U-120_C1-H2_E0_916_v03.mp4`. The `{CONCEPT}-{HOOK}` code equals the combo code in the plan. `{VAR}` names the tested-axis level (E0 = control edit). The version bumps on **any** re-render. Never overwrite a delivered version. |
| Build recipe (one per ad, text, in git) | Every source file with its content hash, in/out points, the transform per shot per format (crop path, move, speed), caption sheet version, music file hash, music offset and licence ID, loudness target, render settings, and the tool/model **named as free text** (record what was used; do not depend on it). The recipe must re-create the same frames. |
| Storyboard/contact sheet | Frames at every cut ±1 frame, every caption change, and the first and last frame, for both formats. QA uses it as an index only, never as the evidence. |
| Self-check report | §2 checklist below, with measured values. |
| Log entry | One row per ad × format in the ad-creative log (see §4): ID, version, file links, hashes, licence ID, QA status = `PENDING`. |

### Procedure
1. **Pre-flight.** Confirm all 7 inputs are locked. Diff the caption sheet against the script, word for word. Check every on-screen pronoun or role against the people in the shots (memory casting-matches-caption). Any conflict → stop and raise it.
2. **Lay the spine.** Build the beat map exactly. Trim each shot to its beat. **Measure the real durations; never time-stretch a voice or music performance to fit.** If it doesn't fit, re-cut the picture or send the copy back.
3. **Build the control first, then derive the variants.** Each variant is the control's recipe with **only** the tested segment swapped. The shared segments come from the same render path, so they are frame-identical.
4. **Picture.** Use the transitions in the criteria sheet: hard cuts by default; dissolves only at story time jumps and never at the hook boundary. Every move starts on frame 1 and is still moving on the last frame. One move per shot. Product and name beats on rigid products use a high-resolution still with a slow move, never a generated push-in (`SM` R22).
5. **Captions.** Burn them in from the sheet: phrase captions, ≤2 lines, ≤2.5 w/s, ≥2.0 s, outline or box treatment, one fixed band per ad per format, never over a face, the product payoff or the name. No caption moves, reflows or flashes blank (<0.5 s gap) while it is meant to be up. **Word-highlight captions only when there is VO.** Highlight inside a stable, fully visible phrase. No pop-in word-by-word for emotional ads.
6. **Audio.** Bed from frame 1. VO ducked under music only where VO plays. End on a musical resolve where the track allows. Normalize to −16 LUFS integrated (−18 when VO leads), true peak ≤ −1 dBTP **measured after encoding**.
7. **End card / CTA.** One CTA, the locked text, ≥2 s, inside the safe zone. Logo legible at phone size (wordmark ≥~40 px tall at 1080w) over **moving** picture.
8. **Feed re-frame.** For each shot, place the 4:5 window so that no key element (face, name, product, light) sits on the crop edge. Pan where one window can't hold them. Re-band the captions to clear the subjects.
9. **Disclosure.** If the user has ruled that an AI-person disclosure is needed (see 07 policy), burn it in at the ruled size and position, identically across all variants.
10. **Render, probe and self-check** (below). Back up media to Drive. Commit the recipe and the log row. Hand to QA.

### Hard rules / must-nots
- Do not change locked copy, the beat map, length, CTA or test structure. Craft fixes are allowed only *inside* a cell (memory follow-plan-page).
- Never use a consumer/in-app music library track, or a track with no licence evidence.
- Never let a variant differ outside its tested window. That includes music offset, gain, grade, caption timing and end card.
- Never pick covers, thumbnails or takes at random. Every choice is deliberate and logged.
- The editor does not mark its own work PASS. Its self-check is input to QA, not a verdict.
- Never `git add` media. Media lives on Drive, recipes and logs live in git.

### Self-check before hand-off (measured, not eyeballed)
Container, codec, fps, resolution, audio channels and bitrate match the spec · duration = planned ± 1 frame · integrated LUFS and true peak · no black or frozen runs that the plan doesn't call for · detected cuts = planned cuts (a missing cut means a mushy dissolve; an extra one is a glitch) · motion gate for the format (`DIR` thresholds, flagged as n=1) · every caption against its sheet line: text, in/out, w/s, band · the name read on ≥5 frames per name beat · the frame-diff of the shared segments across variants is zero · the recipe re-renders the same frame hash on at least one sampled segment.

### Failure modes → guards
| Failure (seen or likely) | Guard |
|---|---|
| Criteria ignored, build made from the user's notes alone (2026-10-09) | Step 1: the criteria sheet is a locked input. No sheet, no render. |
| Crossfades flatten the cut (MJ4U-111) | Hard-cut default. Detected cuts must equal planned cuts. |
| Caption jumps band, reflows or flashes blank (suncatcher E36) | One band per ad. Gap is 0 or ≥0.5 s. The contact sheet shows every caption change. |
| Feed crop hides the name or product (F10/F11) | Per-shot re-frame in step 8. QA checks 4:5 separately. |
| Variant bodies drift (a tweak to one ad only) | Derive variants from the control recipe. QA runs a zero-diff check. |
| Lost "how was this made" | Recipe with hashes. Versions are immutable. |
| Unlicensed or unknown music | Licence evidence is a locked input. QA treats a missing licence as S1. |

---

## 3. Role 07: QA / Gatekeeper

**Mission.** Decide PASS or FAIL for each deliverable against the **locked criteria sheet**, platform spec, ad policy and test integrity. Re-measure everything; nothing is taken on trust. A FAIL comes back as a timestamped defect list with a named fix owner. QA does not fix, and does not waive.

### Inputs
The delivered files (both formats, all variants) · build recipes · the locked criteria sheet, script, caption sheet and test plan · licence evidence · the editor's self-check (**read only after QA has measured on its own**, so it can't anchor QA) · the previous QA report if this is a re-check.

### Frame sampling (for all visual items)
First frame, 0.5 s, 1.0 s and 3.0 s (hook window) · **every planned cut ±1 frame, and every detected cut** (scene detection; reconcile the two lists) · **every caption on/off ±0.1 s** · mid-point of every shot · the **last frame** · name/personalization beats at ≥5 frames each · the variable window of each variant against its control. Then **one real-time viewing on a phone-sized screen, muted, and a second unmuted.** Sampled frames alone miss motion, flicker and pacing.

### Checklist (pass condition · how to check · severity if failed)

**T. Technical spec** (automatable)
| # | Pass condition | Check | Sev |
|---|---|---|---|
| T1 | Ratio and resolution per format (9:16 ≥1080×1920; 4:5 ≥1080×1350), square pixels | probe | S1 |
| T2 | H.264, progressive, constant fps equal to the recipe fps, no edit lists | probe | S1 |
| T3 | Stereo AAC ≥128 kbps; audio track runs the full duration | probe | S1 |
| T4 | Duration = plan ±1 frame; the same across every variant of a cell | probe | S1 |
| T5 | Integrated −16 LUFS ±1 (−18 when VO leads); true peak ≤ −1 dBTP on the **delivered** file; no clipping | loudness measure | S2 |
| T6 | No unplanned black, frozen or silent runs (≥2 frames black, ≥0.5 s freeze, ≥0.3 s silence) | detectors + plan | S2 |
| T7 | ≤3 flashes in any 1 s (WCAG 2.3.1) | flash analysis, or a frame-luma delta scan | S1 |
| T8 | Detected cuts = planned cuts; motion gate passes (n=1 thresholds, reported not worshipped) | scene detection, motion score | S2 / S3 |

**V. Frames / visual** (human, on sampled frames + playback)
| # | Pass condition | Sev |
|---|---|---|
| V1 | Same character identity in every shot; age, gender and role match the captions and pronouns | S1 |
| V2 | No morphs: hands, fingers, faces, pets; no spurious objects (e.g. the gold ring the model kept adding) | S1 if on the product or a face, else S2 |
| V3 | Product true to the real artwork: shape, colours, scale; never model-drawn on a name beat | S1 |
| V4 | Personalization text (name, breed, dates) is exact and legible (≥100 px wide at 1080w) on ≥5 frames per beat | S1 |
| V5 | 4:5: no key element on or past the crop edge in any shot | S2 |
| V6 | Opening frame moves and shows the gift or person cue; closing frame moves | S2 |
| V7 | Grade continuity, no flicker or temporal shimmer in generated clips at playback speed | S2 / S3 |

**C. Captions / text**
| # | Pass condition | Sev |
|---|---|---|
| C1 | Text is word-for-word the caption sheet: spelling, names, punctuation (diff against the sheet) | S1 for names, else S2 |
| C2 | ≤2.5 w/s, ≥2.0 s on screen, ≤2 lines, gap 0 or ≥0.5 s, no reflow or movement while up | S2 |
| C3 | All text and the logo inside the safe zone: 9:16 = 14% top, 35% bottom, 6% sides, and clear of the lower-right rail at the bottom 40%; 4:5 = ≥10% bottom, ≥6% sides | S2 (S1 if the CTA or name is covered) |
| C4 | Contrast: outline or box present; readable at the lowest-contrast frame it crosses | S2 |
| C5 | Never over a face, the product payoff or the name | S2 |
| C6 | Muted cold read: someone who did not build the ad can say, from 0–3 s, **what gift is being sold**, and can retell the story by the end | S2 |
| C7 | With VO: the caption matches the spoken word timing within ±0.2 s; highlight style per the sheet | S2 |

**S. Story / brief fidelity**
| # | Pass condition | Sev |
|---|---|---|
| S1 | Beat map, hook text, CTA text and length match the plan exactly | S1 |
| S2 | Each shot shows what its line says (the visual matches the line) | S2 |
| S3 | Shows connection, not a lonely giftee; grief resolves into warmth by the end | S2 |
| S4 | Every PLAN- or HARD-graded criterion in the criteria sheet passes; opinion-graded items are reported | S2 / S3 |

**B. Brand**
B1 Logo is the correct lockup, legible at phone size, over moving picture (S2) · B2 One CTA, the locked text, ≥2 s (S2) · B3 Store and product names are spelled correctly everywhere (S1).

**P. Ad policy and legal**
| # | Pass condition | Sev |
|---|---|---|
| P1 | No text asserts or implies the viewer's attributes ("Lost your dog?", "As a grandma…"); captions describe the character, never the viewer (`SM` R6) | S1 |
| P2 | Product shown as it really ships: the real artwork, a plausible scale, no features it doesn't have | S1 |
| P3 | Music licence evidence present and covering paid Meta ads; no consumer-library track | S1 |
| P4 | No dramatized story is framed as a real customer review or testimonial (FTC) | S1 |
| P5 | **AI people:** the ad carries the disclosure the user has ruled on for NY (GBL §396-b), or the user has decided on geo-exclusion or no disclosure in writing. QA flags it; **only the user decides** | S1 until ruled |
| P6 | No flashing (T7), shock or sensational grief imagery (dead animal, gore) | S1 |

**I. Test integrity** (run across all files of a cell)
| # | Pass condition | Check | Sev |
|---|---|---|---|
| I1 | Variants differ **only** inside the tested window/axis: zero frame difference outside it | per-frame hash or pixel diff vs control | S1 |
| I2 | Audio identical outside the window (same offset, gain, LUFS within 0.2 LU) | waveform/loudness diff | S1 |
| I3 | Same length, end card, CTA, caption treatment and both formats present for every variant | probe + list | S1 |
| I4 | Names follow the convention; the combo code matches the plan row; versions unique | log vs files | S2 |
| I5 | Upload settings recorded so the test runs as built: asset customization (4:5 → Feed, 9:16 → Stories/Reels); **Advantage+ creative features that alter the video (auto-crop, overlays, music, text, touch-ups) OFF for test cells** unless they are the variable | checked at upload, logged | S1 at upload |

### Severity and the PASS/FAIL rule
- **S1 Blocker**: spec non-conformance, policy, legal or rights exposure, a broken test, wrong name or identity, a morph on the product or a face. **The ad cannot ship.**
- **S2 Major**: fails a PLAN- or HARD-graded criterion or a craft rule with real evidence behind it.
- **S3 Minor**: opinion-graded craft, polish, or a proposed new criterion.
- **PASS = zero S1 and zero S2.** S3s are listed and do not block.
- **Waivers:** only the user can waive an S2 (precedent: the F4 20 s length, waived 2026-10-09). S1 policy and rights items are not waivable. The legal item P5 needs an explicit user ruling. QA and the editor can never waive. Every waiver is recorded in the log with date and reason.
- A **partial cell is not shippable**: if one variant fails, the whole cell waits. Shipping a cell without its control breaks the test.

### Defect report format (one line per defect, grouped by file)
`[S1] MJ4U-120_C1-H2_E0_45_v03 · 00:02.40–00:03.00 · C5 caption over name tag · evidence: frame 00:02.48 (contact sheet #7), tag at y 1180–1240 under band y 1000–1210 · fix: Editor (re-band or pan) · re-check: C5, C3, I1`

Every defect has: severity · file · timestamp or range · criterion ID · evidence (a frame or measured value) · fix owner (Editor / upstream shot gate / Screenwriter / User ruling) · items to re-check. A re-check runs the **whole** T and I groups plus the failed items, because a re-render can break anything.

### Independence rules
- QA is a different agent and session from the builder, with no write access to the media or recipes.
- QA measures before reading the editor's self-check. Disagreements are reported, not reconciled quietly.
- QA judges only against the **locked** criteria sheet. A new concern found mid-QA is filed as S3 "proposed criterion" and goes to the user. It does not become a fail retroactively.
- QA verdicts and the verbatim defect lists go in the log. They are never paraphrased into "looks good".

### Failure modes → guards
| Failure | Guard |
|---|---|
| Rubber-stamp: QA trusts the builder's numbers | Independent measurement first; self-check read afterwards |
| Sampled frames miss motion problems, flicker or pacing | Mandatory real-time muted and unmuted playback |
| Motion score treated as quality | T8 is reported as S3 unless the plan locks it; the motion score can't read text (V4 is by eye) |
| QA moves the goalposts (new taste each round) | Locked sheet; new items are S3 proposals only |
| Single-variant QA misses cross-variant drift | The I group always runs across the whole cell |
| Legal question decided by an agent | P5 and other legal items are escalated to the user, never resolved by QA |

### Old agents: keep / drop
- **`film-editor.md`**: **Drop** "crossfades ~0.4s between scenes" (contradicted by `DIR` §0/§3 and E16), the ~35s master, the static logo + url end card (R12), italic dialogue (`CAP`: bold sans only), and the ffmpeg + PIL binding (tool-agnostic). **Keep** trim-to-beat, match cuts where scripted, real composited text, the real product animated, the cool→warm grade (opinion), and the storyboard sheet for QA.
- **`film-qa.md`**: **Keep it as the upstream shot gate** (dailies: identity, scale, morphs, text, mood, connection), which runs *before* 06. Its shot checks are reused as V1–V4 and S3 on the final cut. **Drop** the idea that it is the final gate: 07 adds spec, captions, policy, rights and test integrity, which `film-qa` never covered.

---

## 4. Recommendations vs the creator's 7-role pipeline

| Their rule | Keep / change for us | Why |
|---|---|---|
| "Only assemble when script and visuals are locked" | **Keep, and extend:** captions, music licence, criteria sheet and test plan must be locked too | Our two worst losses were building without the criteria (2026-10-09) and restructuring the test (2026-10-08) |
| 55–65 s | **15–25 s, plan-locked**; Feed ≤15 s is Meta guidance, tested rather than assumed | `SM` R10, `FEED` §11 |
| Measure the real duration, never slow the voice | **Keep, generalized:** never time-stretch any performance; re-cut the picture | Same principle |
| Warm male regional AI voice, no clone | **Voice is a per-concept creative variable.** It must match casting and pronouns and stay fixed across a cell; music-only is our default | `SM` R13; casting-matches-caption |
| Word-by-word captions, current word changes colour | **Only with VO,** as a highlight inside a stable phrase. Music-only ads use phrase captions at ≤2.5 w/s | No lift evidence; accessibility cost; our user found fast text unreadable |
| 3 covers, one chosen at random | **Drop the randomness.** In a paid test a random cover adds an uncontrolled variable. Paid Reels autoplay from frame 1, so **frame 1 is the real cover**. Choose one cover deliberately (frame-1-derived, readable inside the safe zone) and use it for every variant unless the cover is the variable | `TMF` Part C (one axis per comparison) |
| Upload to Drive + log in the sheet with the reel code | **Keep, enriched:** a per-creative log row with combo code, version, both format links, file and music hashes, licence ID, recipe path, QA verdict + report link, waivers, Meta ad ID(s) after upload, and the upload settings (I5). The CSV in git plus a Sheet mirror, one writer, both updated together. Media → Drive backup. The product tracker keeps only the product-level `ad_status` | memory: product-tracker-and-sheet-sync, media-backup-drive-rclone; `TMF` Part F |
| Output MP4 1080×1920 | **Two deliverables per ad:** 9:16 (1440×2560 target) + 4:5 re-framed (1440×1800 target), assigned by asset customization; plus one IG-Feed-9:16 test cell (`FEED`) | Meta Ads Guide |
| QA: duration, dimensions, codec, audio | Keep, and add loudness and true peak after encoding, flashes, black/freeze/silence, and planned-vs-detected cuts | Broadcast QC practice |
| Frames at start, middle, end, every scene change | Keep, and add every caption change, name beats ×5, the variant window, and real-time muted/unmuted playback | Our caption-flash and crop defects appeared exactly there |
| Captions match VO, correct diacritics | Becomes **exact personalization text** (the name/breed on the product = in the captions = in the plan) and sheet-diff | V4, C1 |
| Visuals match the line; characters the right age | Keep (S2, V1) and add product fidelity, morphs and connection | `SM` R17/R21 |
| Chosen cover is one of the 3 approved | Replaced by cover = the deliberate, logged choice, identical across the cell | see above |
| PASS only when every item passes | **Severity-tiered:** PASS = zero S1/S2. S3 doesn't block. Only the user waives S2; S1 is never waived | Avoids both rubber-stamping and endless polish loops |
| *(missing)* | **Add policy (P), rights (P3), and test integrity (I)** | Our ads are paid tests: a broken cell wastes the spend even when the craft is perfect |

**Open items for the user** (QA cannot resolve these):
1. **NY synthetic-performer disclosure** for AI-cast ads: disclose on all ads, exclude NY, or get legal review. This affects every story ad with an AI person.
2. **Licence evidence for the current music bed** (`products/suncatcher-dog-memorial/ads/shots/music.mp3`): where the track came from and what its terms allow for paid use are not recorded in the repo.
3. Whether to create a **creative-level log** (`products/_registry/ad-creatives.csv` + Sheet tab), separate from the product tracker.
