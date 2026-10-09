# Suncatcher Phase 1: editing criteria, audit, and re-edit spec

> Scope: the edit only (pacing, transitions, camera moves, captions, sound, CTA). No media or build script was changed while writing this.
> Inputs: `_plan-page-text.txt` (approved plan, highest authority), `HOOKS-shared.md`, `C1/C2/C3-*.md`, and `research/reference/` `short-form-caption-design.md`, `script-method.md`, `video-ad-decomposition-2026.md`, `ad-video-director-research.md`, `ai-film-studio.md`, `ai-emotional-video-ad-playbook.md`, `RESEARCH-REPORT-2026-10-ad-production.md`, `fb-ads-benchmarks-2026-sources.md`, plus `research/scripts/motion_qa.py`.
> Audited files: `products/suncatcher-dog-memorial/ads/out/phase1/S-C{1,2,3}-H{1,2}.mp4` (all 20.0s), `ads/build_phase1.py`, `out/phase1/_boards/`.
> Date: 2026-10-09.

**How to read the "Locked?" column.** **PLAN** = written on the approved plan page. **SCRIPT** = locked in `HOOKS-shared.md` or a concept file (our own script, not the plan). **no** = research only.

---

## (a) The criteria (49)

Strength labels are copied from each source: script-method uses STRONG / MODERATE / WEAK / HARD; the decomposition doc uses [DATA] / [OPINION]; caption-design uses "verified 3-0" or "refuted"; the director doc uses [DATA] / [OPINION] plus measurements.

### Length and structure

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E1 | Length **20.0s** for the suncatcher | Plan §05 "Thông số dựng" Length; R10 (15–25s); Decomp brief field 12 (15–30s for skeletons) | R10 MODERATE; Meta ≤15s [A] is the counter | **PLAN** |
| E2 | Structure A beat map **0–2 / 2–6 / 6–12 / 12–17 / 17–20** (hook / context / name / reaction / close + CTA) | Plan §05 suncatcher example; HOOKS §2 | n/a (plan) | **PLAN** |
| E3 | Name reveal **in the middle, not at the end**, leaving runtime for the reaction and CTA | Plan §05; Decomp "Put the reveal at the MID-point" | plan + [OPINION] | **PLAN** |
| E4 | Name reveal 6–12s: **"chữ rõ, giữ lâu"** (text clear, held long) | Plan §05 example | no number given | **PLAN** |
| E5 | Generated length ≠ edit length: every clip is trimmed to its beat | HOOKS §6; ai-film-studio §2; script-method template | house rule | SCRIPT |

### Hook

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E6 | The hook is the **first 0.5–3s**: the opening frame plus the on-screen text | Plan §02, §06 | plan | **PLAN** |
| E7 | Muted 0–3s: the viewer can tell **which gift is being sold** | Plan §05 screening check, §09 Fix 1 | plan, "mandatory" | **PLAN** |
| E8 | Product on screen **by 1s**, and frame 1 shows the gift | R1 | STRONG | PLAN (3s version) |
| E9 | The opening shot moves | R4; motion_qa | MODERATE (n=1 pair) | no |
| E10 | On-screen text **by 0.5s** | Decomp per-component "Captions" row | [DATA] | no |
| E11 | **H1 and H2 of a concept differ only in 0.0–2.0s of picture plus the hook caption.** Everything else is identical, so the hook test isolates one variable | Plan §06 ("keep the whole film, change only the hook"), §11 (one change at a time); HOOKS §1 | plan | **PLAN** |
| E12 | Hook text is verbatim: H1 **"That's not a generic dog. That's his actual breed — and his name."** H2 **"We still leave the window open for him."** | Plan §05 "Thông số dựng" | plan | **PLAN** |

### Pacing, cuts, transitions

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E13 | Pacing **"Mỗi cảnh ~5 giây"** (~5s per scene) | Plan §05 "Thông số dựng" Pacing (suncatcher column) | plan | **PLAN** |
| E14 | Cut rate is briefed **as a number**, not left to the editor | Plan §04 (the brief fixes "nhịp cắt"); Decomp brief field 8 | plan | **PLAN** |
| E15 | Shot length **varies, about 2–5s**. Never uniform 5s beats, and **no two consecutive shots the same length** | R11 + template pre-flight checklist | **MODERATE** (motion benchmark n=1) | no |
| E16 | **Hard cuts, not crossfades** | R11; HOOKS §6 "Hard cuts only"; director §3 (crossfades are "invisible as edits": scdet saw 1 cut in MJ4U-111) | MODERATE / measured n=1 / [OPINION] | SCRIPT |
| E17 | Crossfade **only where a time jump is intended** | Director §5 item 3 | [OPINION] | no |
| E18 | Gift ads cut **slower than gadget ads**: gift median 0.22 cuts/s (~4.5s/shot), max 0.50 | R11 evidence (GW n=16, not longevity-verified) | directional | no |
| E19 | Cut rate depends on the format: ~1.5s/cut for persuasion, **~5s/cut for authenticity formats**, beat-matched for reaction; fast cutting likely hurts with **60+ recipients** | Decomp "Pacing" row, adopted item ② | [OPINION] | no |
| E20 | **Motion gate** (`motion_qa.py --gate`): hook3 ≥8, motion ≥6, **cuts/s ≥0.15** (scdet, so crossfades do not count), onsets/s ≥0.25, static ≤10% | motion_qa.py header | thresholds from **one** benchmark ad (n=1), set below it | house gate |
| E21 | A scale jump between adjacent shots; at least 2 distinct shot sizes | Director §5 item 3–4 | [OPINION] | no |
| E22 | Match cuts are used where they fit | ai-film-studio Editor role | house (the same bible's "crossfades" rule is contradicted by director §3) | no |

### Camera motion and Ken Burns

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E23 | Name beats on a rigid product = **4K still + Ken Burns at native resolution**, never generated video | R22; Research report §3 | **HARD** | SCRIPT |
| E24 | Ken Burns moves **from frame 1** and is **still moving on the last frame** | HOOKS §10 conventions; R4, R12 | MODERATE / WEAK | SCRIPT |
| E25 | **One camera move per shot** | ai-film-studio Director; playbook "ONE move per clip" | house / [OPINION] | no |
| E26 | **Slow** dolly-in = intimacy. HOOKS calls B3b and B5 "slow" push-ins | Playbook "camera = tone lever"; HOOKS §4 | [OPINION]. **No source gives a speed number** | SCRIPT (word only) |
| E27 | "Alex" is **≥100px wide** in the 1080 output while it is the read, and is read by eye on **≥5 frames** | R23 (HARD); C3 rows 10/12; build KB comments | HARD | SCRIPT |

### Captions

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E28 | Burned-in captions **carry the story with sound off** | Plan §02 craft row ("tắt tiếng vẫn hiểu"), §05; R7 | **STRONG** | **PLAN** |
| E29 | Contrast treatment ranks **solid box > outline (≥8–12px, outside the glyph) > drop shadow > colour alone**. Shadow alone fails on light backgrounds. Test at the lowest-contrast region the text passes over | caption-design core rule | **verified 3-0** | no (HOOKS §6 locks "soft 30% shadow") |
| E30 | Bold sans only; no thin, script or italic | caption-design | verified 3-0 | SCRIPT |
| E31 | Size **~64px cap height** at 1080w | HOOKS §6 (caption-design: every "% of frame" size was **refuted**) | no evidence | SCRIPT |
| E32 | **Max 2 lines**, centred | HOOKS §6 | house | SCRIPT |
| E33 | Each caption holds **≥0.33s per word** (≤3 words/s) | HOOKS §6 | **unsourced**: no reading-speed study is in the corpus | SCRIPT |
| E34 | Safe zone: no text above 14% or below 65% of the height, 6% side margins | HOOKS §6; caption-design (TikTok ~130px top / ~320–350px bottom; ~900×1400 centred band); playbook (~250 top / 340 bottom); R7 (+39% CTR from safe zones [B]) | [B] + house | SCRIPT |
| E35 | **Never over a face or the product's payoff** | caption-design checklist #5 | verified checklist | no |
| E36 | Motion must not hurt legibility: **text fully readable for its whole time on screen**. Pop-in and fades are polish, with no retention evidence | caption-design "Animation" | verified (no-lift) | no |
| E37 | Hormozi style (ALL CAPS, 3–5 words/line, one highlighted keyword, black stroke) | caption-design | verified as a *style*, not as a lift | no |
| E38 | Captions describe the character, **never the viewer** | R6 | **HARD** | SCRIPT |

### Sound

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E39 | **Music bed, no voice**; one approved bed (`ads/shots/music.mp3`) from frame 1, lifting at 6.0, resolving at 20.0 | Plan §05 Voice ("Nhạc nền, không lời"); R13; HOOKS §6 | plan; R13 MODERATE | **PLAN** |
| E40 | Cuts are **beat-matched** in reaction formats | Decomp "Pacing" row | [OPINION] | no |

### CTA, end, brand

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E41 | CTA text **"Make one that's only theirs"**, button **Shop Now** | Plan §05 | plan | **PLAN** |
| E42 | CTA on screen as text, and **the last 2s move** (no frozen end card) | R8, R12, template checklist | MODERATE / WEAK | SCRIPT |
| E43 | Logo small, over moving footage, beat 5 only | HOOKS §6; R12 | WEAK | SCRIPT |
| E44 | CTA in the **bottom third** | Playbook production specs | [OPINION] | no (HOOKS puts it at the top on purpose) |

### Product, name, story

| # | Criterion | Source | Strength | Locked? |
|---|---|---|---|---|
| E45 | Product visible in **every beat, or no more than one beat away** | Template pre-flight checklist; Plan §09 cause 3 | MODERATE | PLAN (spirit) |
| E46 | The personalization is the **hero visual**: legible for a large share of the runtime | R2 | **STRONG** | PLAN (proof = name + breed) |
| E47 | Emotional pivot line at **~55–60%** of the runtime (11–12s) | R15 | WEAK | no |
| E48 | Grief **resolves into warmth** by the end (peak-end); cool→warm | Playbook; HOOKS §6 grade | [OPINION] | SCRIPT |
| E49 | Show connection, **not a lonely giftee** | R17; house rule (memory) | WEAK, kept as a house rule | SCRIPT (S9) |

---

## (b) Audit of the current 6 cuts

**Measured facts** (from `build_phase1.py`, ffprobe, `motion_qa.py`, the boards).

Shot list (hard cuts at every boundary):

| | 0–2 | 2–6 | 6–9 | 9–12 | 12–17 | 17–20 | Shots | Mean shot |
|---|---|---|---|---|---|---|---|---|
| C1, C2 | hook 2.0 | B2 4.0 | B3a 3.0 | B3b 3.0 | B4 5.0 | B5 3.0 | 6 | 3.33s |
| C3 | hook 2.0 | B2 (KB) 4.0 | B3a 3.0 | B3b 3.0 | B4a 3.0 + B4b 2.0 | B5 3.0 | 7 | 2.86s |

Ken Burns zoom (crop width, start → end): HOOK-H1 1300→2600 = **2.0× in 2.0s**; C3-B2 1050→2600 = **2.5× in 4.0s**; B3b 2600→1500 = **1.73× in 3.0s**; C3-B4b 2000→1200 = 1.67× in 2.0s; B5 2900→2000 = 1.45× in 3.0s.

Motion gate (all **PASS**):

| Ad | hook3 | motion | cuts/s | onset/s | static |
|---|---|---|---|---|---|
| C1-H1 | 29.8 | 16.4 | 0.25 | 0.30 | 0% |
| C1-H2 | 13.4 | 13.9 | 0.20 | 0.30 | 0% |
| C2-H1 | 26.4 | 14.1 | 0.25 | 0.25 | 0% |
| C2-H2 | 10.3 | 11.7 | 0.20 | 0.25 | 0% |
| C3-H1 | 29.6 | 19.6 | 0.30 | 0.40 | 0% |
| C3-H2 | 13.7 | 17.2 | 0.25 | 0.40 | 0% |

Caption timeline. Font is Arial Bold; cap height ≈ 0.716 × the px size.

| Time | Caption | Words | On screen | s/word | w/s | Font (cap) | Lines | Band |
|---|---|---|---|---|---|---|---|---|
| H1 0.0–1.0 | line 1 only | 5 | 1.0 | | | 78 (56) | 1 | top |
| H1 1.0–2.0 | + lines 2–3 appear | 12 | | | | 78 (56) | **3** | top |
| H1 2.0–3.0 | **same block jumps** to the mid band | 12 | **3.0 total** | **0.25** | **4.0** | 78 (56) | **3** | mid |
| H2 0.0–2.0 → 2.0–3.0 | **jumps** top → mid at 2.0 | 8 | 3.0 | 0.375 | 2.67 | 86 (62) | 2 | top→mid |
| C1 3.0–6.0 | His bowl hasn't moved since spring. | 6 | 3.0 | 0.50 | 2.00 | 86 (62) | 2 | mid |
| C2 3.0–6.0 | Alex, his German Shepherd, waited here 11 years. | 8 | 3.0 | 0.375 | 2.67 | **70 (50)** | 2 | mid |
| C3 3.0–6.0 | Alex was my neighbor's dog. / Flowers felt wrong. | 8 | 3.0 | 0.375 | 2.67 | **68 (49)** | 2 | upper |
| all 6.0–9.0 | Every afternoon, he's back on the wall. | 7 | 3.0 | 0.43 | 2.33 | 86 (62) | 2 | mid |
| all 9.0–12.0 | His breed. His name. In the light. | 7 | 3.0 | 0.43 | 2.33 | 86 (62) | 2 | **top** |
| 12.0–12.3 | **blank (0.3s)** | | | | | | | |
| C1 12.3–17.0 | There was only one Alex. / So there's only one of these. | 11 | 4.7 | 0.43 | 2.34 | **68 (49)** | 2 | mid |
| C2 12.3–17.0 | Alex is back / in his spot. | 6 | 4.7 | 0.78 | 1.28 | 86 (62) | 2 | mid |
| C3 12.3–17.0 | This felt like Alex. | 4 | 4.7 | 1.17 | 0.85 | 86 (62) | 1 | mid |
| 17.0–17.2 | **blank (0.2s)** | | | | | | | |
| all 17.2–20.0 | Make one that's / only theirs | 5 | 2.8 | 0.56 | 1.79 | 86 (62) | 2 | **top** |

Caption treatment: white text with a blurred 30% shadow and a 40% halo. **No box and no outline.** The caption state changes **10 times in 20s in H1 ads and 9 in H2 ads**, and every body caption swaps exactly on a picture cut.

### Pass/fail per criterion

| # | Result | Evidence (timestamps) |
|---|---|---|
| E1 | ✅ all 6 | 20.0s |
| E2 | ✅ | beat boundaries 2/6/12/17 match |
| E3 | ✅ | name at 6–12 |
| E4 | ⚠️ **partial**, all 6 | "Alex" is legible on the wall only in B3b (9.0–12.0, 3.0s). B3a (6–9) is generated video, so no legible name. B3b pushes in, so "Alex" is largest only at the end |
| E5 | ✅ | every clip trimmed |
| E6, E7, E8, E10 | ✅ all 6 | product and caption from 0.0s (board, HOOKS §7) |
| E9 | ✅ | H1 Ken Burns; H2 push-in |
| E11 | ✅ | the body is built from identical code |
| E12 | ✅ | verbatim |
| E13 | ⚠️ **partial**, all 6 | Beats are 2/4/6/5/3, but beat 3 is two 3.0s shots, and in C3 beat 4 is 3.0 + 2.0. Shots average 3.33s (C1/C2) and 2.86s (C3), not ~5s |
| E14 | ✅ | numbers are in the briefs |
| E15 | ❌ all 6 | consecutive equal lengths: B3a 3.0 → B3b 3.0 (6.0–12.0); C3 also has 3.0 / 3.0 / 3.0 at 6–15 |
| E16 | ✅ | 4–6 scdet cuts |
| E17 | n/a | no crossfades |
| E18 | ✅ | 0.20–0.30 cuts/s, inside the gift range |
| E19 | ❌ (opinion) | 2.9–3.3s/shot is quicker than the ~5s/cut the doc suggests for authenticity formats and 60+ recipients |
| E20 | ✅ all 6 | the H2 ads are closest to the gate on hook3 (10.3–13.7 vs ≥8) |
| E21 | ⚠️ | there is a scale jump at 2.0, but in C1/C3-H1 it jumps from the wide panel straight back to an ECU of the **same panel** (board 1.0s → 2.5s), which reads as a restart |
| E22 | ❌ | no match cuts |
| E23 | ✅ | |
| E24 | ✅ | motion 0% static; B5 is still moving at 19.8s |
| E25 | ✅ | |
| E26 | ⚠️ | HOOKS calls B3b and B5 "slow", but B3b zooms 1.73× in 3s, and HOOK-H1 (2× in 2s) and C3-B2 (2.5× in 4s) are fast. There is no numeric rule |
| E27 | ⚠️ not re-verified here | boards show "Alex" legible at 0.05s, 10.5s and 16.0s; the ≥5-frame by-eye read was not repeated |
| E28 | ✅ | |
| E29 | ❌ all 6 | shadow and halo only. The boards show white text over bright yellow and blue glass at 1.0s (hook), 4.0s (C3 beat 2) and 18.5s (CTA) |
| E30 | ✅ | |
| E31 | ❌ all 6 | the H1 hook has a 56px cap (3 ads); C1 12.3–17.0 is 49px; C2 3.0–6.0 is 50px; C3 3.0–6.0 is 49px |
| E32 | ❌ H1 ×3 | the hook caption wraps to **3 lines** (0.0–3.0) |
| E33 | ❌ H1 ×3 | 12 words in 3.0s = 0.25s/word (the script's own §6 asks for ≥0.33) |
| E34 | ✅ | every caption sits between y=309 and y=1238 (16–64.5%) |
| E35 | ❌ at least C3-H1 | 2.0–3.0: the hook block in the mid band sits across the silhouette and "Alex" (board 2.5s). Not yet checked on the other 5 |
| E36 | ❌ all 6 | the hook block **moves** at 2.0 (top→mid) in all 6 and **reflows** at 1.0 in H1. Blank flashes at 12.0–12.3 and 17.0–17.2. The band alternates every ~3s (mid 6–9 → top 9–12 → mid 12.3 → top 17.2) |
| E37 | n/a | not used (see D5) |
| E38 | ✅ | |
| E39 | ⚠️ | correct bed, from frame 1. The end is a 1.4s **fade-out** (st 18.6), not a musical resolve |
| E40 | not measured | cuts are on fixed times, not checked against the bed's beats |
| E41, E42, E43 | ✅ | |
| E44 | ❌ (deliberate) | CTA in the top band so it does not cover "Alex" (build comment) |
| E45, E46 | ✅ | |
| E47 | ✅ | the beat-4 line lands at 12.3 (61%) |
| E48 | ✅ | warm reveal |
| E49 | ✅ per S9 | |

**Tally: 15 criteria failed or partial on at least one ad.** Hard fails: E15, E19, E22, E29, E31, E32, E33, E35, E36, E44. Partial or soft: E4, E13, E21, E26, E39. Of these, **5 fail on all 6 ads** (E15, E29, E31, E36, plus E13 partial). E32 and E33 fail on the 3 H1 ads.

---

## (c) User complaints → criteria

| Complaint | Failed criteria | Where the research itself pushed the wrong way |
|---|---|---|
| **"Scenes switch too quickly, hard to follow; for emotional we want it slower"** | **E13** (plan ~5s/scene: we cut 3.0s shots inside the 6s scene and 2–3s in C3); **E15** (3.0/3.0 rhythm); **E19** (~5s/cut for authenticity, 60+); **E21** (2.0s cut back to an ECU of the same panel feels like a restart); **E26** (fast zooms: 2× in 2s, 2.5× in 4s, 1.7× in 3s add felt speed even inside a shot) | **R11 and the motion gate (E20)** push toward faster cuts and more motion, but both rest on **one** product-hero benchmark (a car visor). script-method R20 says **no source tests a story film**. For this emotional variant the user's reaction is real evidence and the n=1 gate is not. |
| **"Some text changes so fast I can't read it"** | **E33, E32** (H1: 12 words, 3 lines, 3.0s = 4 w/s); **E36** (the hook block reflows at 1.0 and jumps at 2.0; 0.2–0.3s blank flashes; captions swap on every cut and alternate top/mid); **E29, E31** (shadow-only, 49–56px caps over bright glass: slower to decode, so the same on-screen time feels shorter) | **HOOKS §6's ≥0.33s/word is unsourced.** No reading-speed study exists in the corpus, so the rule we passed against was a guess. Even so, the H1 hook broke it (S5 in HOOKS knew 12 words don't fit and only extended the caption to 3.0). |
| **"Transitions not smooth, too choppy"** | **E15** (an even 3s rhythm, each cut doubled by a caption swap); **E22** (no match cuts); **E21** (same-subject jump at 2.0); **E36** (text jumping at the cuts) | **R11 / HOOKS §6 "hard cuts only"** (MODERATE, n=1) was applied with no exception. The director doc's own rule, **E17** (crossfade where a time jump is intended), was never applied, though C3 has two time jumps (C3-b: pack → result → delivery). |

---

## (d) Audit of the drafted re-edit spec

| Draft item | Complies with | Conflicts with | Verdict |
|---|---|---|---|
| **~5s per scene** | E13 (PLAN), E19, user | **E2** (PLAN): the hook is fixed at 0–2 and the skeleton is 2/4/6/5/3, so "5s per scene" can only mean one shot per beat, not uniform 5s. **E15** (R11: never uniform 5s, MODERATE) | OK if it means **one shot per beat** (2/4/6/5/3). Wrong if it means literal 5s shots. → D1 |
| **0.5s cross-dissolves** | user ("smooth"); E17 only at time jumps; old ai-film-studio rule | **E16** (R11 MODERATE + HOOKS §6 SCRIPT lock); **E20**: scdet does not count dissolves, so with all-dissolve joins cuts/s falls toward 0.05 and the **gate FAILS** (≥0.15). **E11**: a dissolve at 2.0 bleeds the hook picture into the body, so H1 and H2 bodies would differ | Conflict. Never at 2.0. Elsewhere → D2 |
| **Ken Burns 40% slower** | E26 (direction), user | none by rule. Risks: **E27** ("Alex" ≥100px) if slowing means stopping short of the end crop; **E24** (must still move at the first and last frame). H1 hook3 has headroom (26–30 vs 8) | Complies if done by **shortening the path while keeping the legible end crop** |
| **One caption per scene, ≥2.5s, ≤2.5 w/s, with fades** | E33 (stricter), E36 (if position-locked), user | **Shared B3 copy (SCRIPT lock, HOOKS §4)**: beat 3 has two locked lines, so one caption per 6s scene means dropping one. At ≤2.5 w/s the **8-word** C2/C3 beat-2 lines need 3.2s but get 3.0s; the **12-word** PLAN-locked H1 needs 4.8s. Fades eat reading time unless excluded | Mostly complies. The copy collisions → D3, D4, D7 |
| **H1 hook split into two cards across 0–5s** | user; E33 | **E6** (PLAN: hook = 0.5–3s); **E11** (PLAN: H1 ads would lose the concept's 3–6s caption that H2 ads keep, so the hook test is confounded); it also deletes C2's 3.0s "German Shepherd" dog cue (C2-h fix) and C3's buyer reason in H1 ads | **Conflicts with the plan.** → D4 |

The draft also left out E29 (box or outline), E31 (cap size), E35 (never over "Alex"), the blank flashes in E36, E21, and the gate re-run (E20).

---

## (e) Decisions pending (conflicts)

| ID | Conflict | Side A | Side B | Recommendation |
|---|---|---|---|---|
| **D1** | **Shot length** | R11: vary 2–5s, never uniform, gift median ~4.5s/shot (MODERATE, n=1 motion benchmark, product-hero ads only) | Plan §05 "~5s per scene" (PLAN) + E19 [OPINION] + user "slower" | **Plan and user win:** one shot per beat, except B3 = **2.8 + 3.2** (unequal, keeps both locked lines) and C3 beat 4 = 3.0 + 2.0. Lengths 2 / 4 / 2.8 / 3.2 / 5 / 3: none consecutive equal, inside 2–5s, and a calmer rhythm. Gate cuts/s stays ≥0.20. |
| **D2** | **Transition type** | Hard cuts only: R11 (MODERATE), HOOKS §6 lock, motion gate (n=1) | User "smooth"; E17 "crossfade where a time jump is intended" [OPINION]; ai-film-studio "crossfades + match cuts" | **Hard cut at 2.0 always** (hook isolation and hook3). Elsewhere use **motivated** hard cuts: match direction of motion and scale between shots. Short dissolves (≤0.4s) are **allowed only at C3's time jumps (6.0, 12.0)**, with ≥3 hard cuts kept so the gate passes. Plan §13 makes cut rate a **later Craft-round test (~$2)**, so whatever is chosen must be identical across all 6 ads. |
| **D3** | **Reading speed** | HOOKS §6: ≥0.33s/word (≤3 w/s), unsourced | Draft ≤2.5 w/s (unsourced) + user "can't read it" | Adopt **≤2.5 w/s and ≥2.0s on screen, counted after any fade-in**. The user's direct test outranks an unsourced number. Consequence: the 8-word C2/C3 beat-2 lines need copy trims to ≤7 words, or 0.2s more (see D4/D7). |
| **D4** | **H1 hook text vs the hook window** | Plan locks the 12-word H1 line (E12) and the 0.5–3s hook (E6), and requires the bodies to be identical (E11) | At ≤2.5 w/s, 12 words need 4.8s; the user can't read it | **Ask the user to approve a shorter H1 line** (≤7–8 words, same idea: name + breed shown, e.g. "Not a generic dog. His breed. His name."). It changes a PLAN-locked field, so it is the user's call. Reject the two-card 0–5s version: it breaks E6 and E11. |
| **D5** | **Caption treatment** | HOOKS §6 locks a soft 30% shadow (SCRIPT) | caption-design (verified 3-0): box > ≥8–12px outline > shadow; shadow alone fails on light backgrounds (as seen on the glass) | Use a **black outline of 8–12px outside the glyph, plus the existing soft shadow.** A box is the safest, but heavier for an emotional film. Do **not** adopt Hormozi ALL CAPS or keyword highlights (E37): a style, not a proven lift, and wrong for grief. |
| **D6** | **Caption band** | HOOKS: 14–65% band; CTA at the top on purpose (keeps "Alex" clear) | caption-design: lower third above the bottom ~350px; playbook: CTA in the bottom third | Keep the HOOKS band. **One fixed band per ad, chosen so it is clear of faces and "Alex" in every shot** (E35, E36). Keep the CTA at the top. |
| **D7** | **"One caption per scene"** (draft) | Shared beat-3 copy is two locked lines (HOOKS §4) | Draft wants one per scene | Keep both lines, **one per B3 shot** (2.8s and 3.2s at 2.5 w/s). Dropping one changes locked shared copy, which is the user's call. |

---

## (f) Consolidated edit spec (re-edit v2)

**Locked and unchanged:** 20.0s; the beat map 0–2 / 2–6 / 6–12 / 12–17 / 17–20; hook picture 0.0–2.0 is the only picture difference between H1 and H2; the bodies are byte-identical; the approved music bed; CTA "Make one that's only theirs" + Shop Now; logo small over moving B5; 9:16 1080×1920 at 25fps.

**Picture**
1. Shots (D1 pending): C1/C2 = hook 2.0 · B2 4.0 · B3a **2.8** · B3b **3.2** · B4 5.0 · B5 3.0. C3 = hook 2.0 · B2 4.0 · B3a 2.8 · B3b 3.2 · B4a 3.0 · B4b 2.0 · B5 3.0.
2. Transitions (D2 pending): **hard cut at 2.0**. Elsewhere, hard cuts matched on motion direction and scale. Only if D2 allows: ≤0.4s dissolves at C3's 6.0 and 12.0. Keep ≥3 scdet-visible hard cuts in every ad.
3. Ken Burns: about **40% less zoom per second**, done by moving the **start** crop closer to the end crop and **keeping every end crop** that makes "Alex" legible. Motion from frame 1, still moving on the last frame, one move per shot. Targets: H1 ≤1.6× over 2.0s (frame 1 still shows "Alex" ≥100px); C3-B2 ≤1.6× over 4.0s; B3b ≤1.3× over 3.2s, ending on "Alex" ≥100px; B5 ≤1.3×; C3-B4b ≤1.3×.
4. At 2.0 in the H1 ads, avoid cutting from the wide panel back to an ECU of the same panel. Open beat 2 at a scale between the two (e.g. ≥1600px crop in C3-B2), or let the beat-2 move continue the hook's direction.

**Captions**
5. Treatment (D5 pending): Arial Bold, white, **8–12px black outline outside the glyph**, plus the soft shadow. **Cap height ≥60px** (≥84px font), **max 2 lines**, centred, 6% side margins, inside 14–65% of the height.
6. Reading time (D3 pending): **≤2.5 words/s and ≥2.0s on screen**, counted after the fade-in. Fade in and out ≤0.15s each.
7. **No caption ever moves, reflows or adds lines while on screen.** No line-by-line build of the hook.
8. **One fixed band per ad** (D6), clear of faces, the silhouette and "Alex" in every shot it spans. Check every frame where a caption crosses a cut.
9. Between captions: either the next caption starts on the frame the last one ends, or there is a clean gap of **≥0.5s**. No 0.2–0.3s blank flashes.
10. Timings (after D3/D4/D7):

| Time | Caption | Words | w/s |
|---|---|---|---|
| 0.0–3.2 | H2 "We still leave the window open for him." | 8 | 2.5 |
| 0.0–3.2 | H1: **D4 pending** (needs ≤8 words to fit) | | |
| 3.2–6.0 | C1 "His bowl hasn't moved since spring." | 6 | 2.1 |
| 3.2–6.0 | C2 and C3 8-word lines: 2.86 w/s, **fails** → trim to ≤7 words (user's call) or accept 2.86 | | |
| 6.0–8.8 | "Every afternoon, he's back on the wall." | 7 | 2.5 |
| 8.8–12.0 | "His breed. His name. In the light." | 7 | 2.2 |
| 12.5–17.0 | beat-4 line, 0.5s clean gap after the cut (C1 11 words = 2.44 w/s) | | |
| 17.5–20.0 | CTA + logo | 5 | 2.0 |

The hook caption end (3.2) is the **same in H1 and H2**, so the bodies stay identical (E11).

**Sound**
11. Same bed. If possible, nudge each cut to the nearest bar or beat within ±0.2s (E40, opinion). End on the bed's own resolve rather than a 1.4s fade if the track allows (E39).

**QA before showing the user**
12. `motion_qa.py --gate` on all 6: hook3 ≥8, motion ≥6, cuts/s ≥0.15, onsets/s ≥0.25, static ≤10%. Report the H2 hook3 values (currently 10.3–13.7).
13. Read "Alex" by eye on ≥5 frames of every Ken Burns shot that shows it (R23).
14. Do a muted 0–3s cold read on each of the 6 ads.
15. Re-render the storyboards with a frame at **every caption change and every cut ±0.1s**, so jumps and flashes are visible before the user watches.

---

## Feed placement (added 2026-10-09)

Source and citations: `research/reference/feed-video-best-practice.md`. Grades: A = Meta official, B = data-backed, C = opinion or our own inference.
These rules apply to the 4:5 Feed cuts (`FMT=feed`, `ads/out/phase1/feed/`) only.

### Rules
- **F1** Native 4:5 for FB Feed, re-framed rather than letterboxed. (A)
- **F2** Resolution 1440×1800 is recommended; 1080×1350 is the accepted floor. (A / C)
- **F3** H.264, fixed fps, square pixels, stereo AAC ≥128 kbps. (A)
- **F4** Length ≤15s, with the main message in the first 3–5s. (A, Meta creative guide; B, completion data)
- **F5** Product, person or brand cue visible in the first 3s, with motion on frame 1. (A)
- **F6** Sound-off: burned-in captions carry the whole story. (A)
- **F7** Captions: large, high-contrast, clean bold font; ≥~60px cap height at 1080 wide. (A / C)
- **F8** One message per screen, ≤2 lines, never a paragraph. (A)
- **F9** Safe zone: all text and the logo sit ≥10% (≥135px) above the bottom edge and ≥6% (≥65px) in from each side. (A rule, C numbers)
- **F10** Captions never cover the key subject: "Alex", the name tag, the product, the light. (A, "don't obstruct the visuals")
- **F11** Re-frame check: no key element sits on or past the 4:5 crop edge. (A, "frame your visual story"; C)
- **F12** Pacing: motion in every shot, no static hold longer than ~4s. Feed can run slower than Reels. (C)
- **F13** End card: one CTA held ≥2s, and the logo legible at phone size (wordmark ≥~40px tall at 1080 wide). (A single CTA / C sizes)
- **F14** Audio: sound bed present, about −16 LUFS. (A "recommended" / C level)
- **F15** Uploaded through asset customization: 4:5 to Feed, 9:16 to Stories/Reels. Run an IG Feed test of 9:16 against 4:5, because Meta now recommends 9:16 for IG Feed. (A / C)

### Audit of the 6 Feed cuts (2026-10-09)
Measured with ffprobe and frames pulled at the times below. All 6 files: 1080×1350, 25 fps CFR, H.264 High, SAR N/A (square), AAC-LC stereo 48 kHz 160 kbps, 20.00s, mean −18 dB.
Caption block runs y≈1010–1205, which leaves 145px (10.7%) at the bottom. Line width ≤950px, so side margins are ≥65px.
The logo wordmark sits at y≈1250–1295, only 55px (4%) above the bottom, and the wordmark is ~25–30px tall.

| Rule | C1-H1 | C1-H2 | C2-H1 | C2-H2 | C3-H1 | C3-H2 | Note |
|---|---|---|---|---|---|---|---|
| F1 | P | P | P | P | P | P | |
| F2 | P* | P* | P* | P* | P* | P* | *floor only. The sources are 720×1280, so a 1440 render adds no real detail |
| F3 | P | P | P | P | P | P | |
| F4 | **F** | **F** | **F** | **F** | **F** | **F** | 20.0s against ≤15s |
| F5 | P | P | P | P | P | P | panel + "Alex" (H1) / man + panel in window (H2) at 0.0s |
| F6 | P | P | P | P | P | P | captions on 0–12.0 and 12.5–20; 0.5s gaps at the cuts |
| F7 | P | P | P | P | P | P | Arial Bold 84px, 10px stroke |
| F8 | P | P | P | P | P | P | |
| F9 | **F** | **F** | **F** | **F** | **F** | **F** | captions pass; logo 17.5–20.0s at 96% height |
| F10 | **F** | **F** | P | P | P | P | C1-B2: ALEX bowl tag sits under the hook caption 2.0–~3.0s, cropped at the bottom edge. The shot tilts up after that; the beat runs 2–6s |
| F11 | P | P | **F** | **F** | P | P | C2-B4, 12.0–17.0s: projected-Alex light on the bed is cropped at the bottom-left corner, and the hanging panel is clipped at the top-left edge. Watch: C3-B2 note card touches the top edge ~5.8s |
| F12 | P | P | P | P | P | P | shots 2.0–5.0s, all moving |
| F13 | **F** | **F** | **F** | **F** | **F** | **F** | CTA 17.5–20.0s passes; logo too small to read |
| F14 | P | P | P | P | P | P | loudnorm −16 LUFS |
| F15 | – | – | – | – | – | – | upload-time step, not yet done |

**Totals: 84 checks (F1–F14 × 6). 62 pass, 22 fail.** Every ad fails 3 (F4, F9, F13). C1 also fails F10, and C2 also fails F11.

### Fix list (Feed cuts only; not yet applied)
1. **C1-B2 (both C1 ads), 2.0–~3.0s:** move the hook and beat-2 captions to an upper band for this shot only (~25–40%, over the empty wall), or lower `CLIP_FEED_OFF["C1-B2"]` so the tag leaves the frame. Going up keeps the name proof.
2. **C2-B4 (both C2 ads), 12.0–17.0s:** a fixed 720×900 window can't hold both the panel and the bed light. Replace the fixed `CLIP_FEED_OFF["C2-B4-t2"]=150` with a vertical pan (e.g. offset 60→330 across the 5s) so the shot ends on the light on the bed. Then re-check that the light stays above the caption band.
3. **Logo (all 6):** move it into the safe zone and enlarge it. Make the lockup ~560–600px wide (wordmark ≥40px) with its bottom ≤ y 1200, and move the CTA text up to ~y 880–1080 for `FMT=feed`.
4. **Length (all 6):** keep the 20s cuts as the control and add a ≤15s Feed cutdown. Candidate trims: B3a+B3b 6.0→3.5s, B4 5.0→3.5s, CTA 2.5→2.0s.
5. **Upload:** use asset customization with 4:5 → FB Feed/IG Feed and 9:16 → Stories/Reels, plus one IG-Feed-9:16 test cell.
6. Optional: render at 1440×1800 only if the clips are regenerated above 720p.
