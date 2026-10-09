# Suncatcher Phase 1: caption sheet (re-edit v2)

> Date 2026-10-09. Applies decisions D1–D7 from `EDIT-CRITERIA.md` §(e), as the user decided them on 2026-10-09. This is a spec for the editor. No media and no build script was touched.
> Text in this sheet is final. Wherever a line differs from `HOOKS-shared.md` or a `C*.md` script, it is marked **CHANGED** with old → new.

## FINAL decisions (user, 2026-10-09). These override the tables below wherever they differ

| Item | Final |
|---|---|
| H1 hook text | **His actual breed. / His actual name.** (6 w; replaces "Not clip art. / His breed. His name.") |
| Hook window | **Both** hook captions 0.0–3.2 (H2 8 w = 2.50 w/s ✓). Every beat-2 caption runs **3.2–6.0**. The picture still cuts at 2.0 (hard) |
| Transitions | Hard cuts everywhere **except one 0.4s dissolve centred on 6.0 (5.8–6.2) in all 6 ads**. C3's 12.0 is a **hard cut**, so the edit style is identical across all 6 |
| Shots | One shot per beat: 2.0 / 4.0 / 2.8 / 3.2 / 5.0 / 3.0. C3 beat 4 = C3-B4a 3.0 + C3-B4b 2.0, hard cut at 15.0 |
| Band (as built) | **y 1000–1210 (52–63%) in all 6 ads**, not 36–47%. Checked on every board: 36–47% covered the dog's head in the H1 frame-1 close-up and the framed photo + shadow head in C1 beat 4. "Alex" is re-aimed to sit above the band (42–47% of height) in HOOK-H1, B3b, C3-B2 and C3-B4b. CTA alone stays in the top band |
| Captions | 84px Arial Bold, 10px black outline + soft shadow, sentence case, no fades, hard on/off |

## Rules applied to every caption

| Rule | Value |
|---|---|
| Reading speed (D3) | ≤2.5 words/s. Numbers ("11") count as one word |
| Minimum on screen (D3) | ≥2.0s |
| Fades | **None.** Captions switch on and off hard, so the listed duration is the full readable time |
| Gaps | The next caption starts on the frame the last one ends, or there is a clean gap of ≥0.5s. No blank flashes |
| Treatment (D5) | Arial Bold, white, sentence case (no ALL CAPS), **10px black outline outside the glyph** + the existing soft shadow. 84px font (≈60px cap height). Max 2 lines, centred |
| Width | 6% side margins → 950px. After the 2 × 10px outline, a text line may be at most **930px** at 84px. Every line below was measured with PIL (Arial Bold 84) |
| Band (D6) | One fixed body band per ad: **y 690–900px (36–47% of 1920)**, the same in all 6 ads. CTA alone sits in the top band (y 270–480, 14–25%) |
| Hook window (D4) | Hook caption 0.0–3.0 in both H1 and H2, so the bodies stay identical from 3.0 on (E11) |

**Why that band.** The C2-H2 board shows the owner's face at about 17–35% of the height (beats 1-H2, 2 and 4) and the wall "Alex" at about 49–60% (B3b). The old mid band (≈50–60%) would cover "Alex", and the old top band (≈14–30%) would cover his face. 36–47% sits between them: it crosses his chest, not his face, and stays above the name. **Only C2-H2 was checked against a board.** Before rendering, check the band on the other 5 boards, especially the H1 hook's frame-1 close-up of "Alex" (0.0–2.0) and C1/C3 beat 4.

## Shot timeline (same structure in all ads, D1 + D2)

D2 rule: a hard cut everywhere, plus a 0.4s dissolve (centred on the boundary) **only where the story jumps in time or place**. The cut at 2.0 is always hard.

### C1 and C2 (H1 and H2)

| Beat | Start | End | Len | Shot | Join into this shot |
|---|---|---|---|---|---|
| 1 hook | 0.0 | 2.0 | 2.0 | `HOOK-H1` (H1 ads) / `HOOK-H2` (H2 ads) | (start) |
| 2 context | 2.0 | 6.0 | 4.0 | C1: tag + bowl, overcast · C2: owner in armchair, cool daylight | **hard cut** |
| 3a | 6.0 | 8.8 | 2.8 | `B3a` sun through panel → shadow | **dissolve 5.8–6.2** (time jump: overcast/cool → afternoon sun) |
| 3b reveal | 8.8 | 12.0 | 3.2 | `WALL-4K` Ken Burns to "Alex" | hard cut |
| 4 | 12.0 | 17.0 | 5.0 | C1: owner raises photo by the shadow · C2: same framing as beat 2, gold light | hard cut (same afternoon, continuous) |
| 5 close | 17.0 | 20.0 | 3.0 | `B5` panel + logo | hard cut |

Hard cuts the scdet gate can see: 2.0, 8.8, 12.0, 17.0 = **4 → 0.20 cuts/s** (gate ≥0.15).

### C3 (H1 and H2)

| Beat | Start | End | Len | Shot | Join into this shot |
|---|---|---|---|---|---|
| 1 hook | 0.0 | 2.0 | 2.0 | `HOOK-H1` / `HOOK-H2` | (start) |
| 2 context | 2.0 | 6.0 | 4.0 | `F-BOX` Ken Burns pull-out, her hands at the gift box | **hard cut** |
| 3a | 6.0 | 8.8 | 2.8 | `B3a` | **dissolve 5.8–6.2** (her kitchen → his wall, afternoon) |
| 3b reveal | 8.8 | 12.0 | 3.2 | `WALL-4K` | hard cut |
| 4a | 12.0 | 15.0 | 3.0 | she hands him the box at his door | **dissolve 11.8–12.2** (his wall → his front door, a later moment) |
| 4b | 15.0 | 17.0 | 2.0 | `C3-B4b` open box still, "Alex" legible | hard cut |
| 5 close | 17.0 | 20.0 | 3.0 | `B5` | hard cut |

Hard cuts: 2.0, 8.8, 15.0, 17.0 = **4 → 0.20 cuts/s**. Shot lengths 2 / 4 / 2.8 / 3.2 / 3 / 2 / 3: no two consecutive shots are the same length.

> Producer call: D2 says "identical across all 6". The **rule** is identical, but C3 has two time jumps and C1/C2 have one, so C3 gets a second dissolve at 12.0. If identical **positions** matter more for the later cut-rate test, make C3's 12.0 a hard cut instead.

## Captions per ad

Shared rows are written out in each table so every ad can be built from its own table. "|" inside the text cell marks the line break.

### S-C1-H1

| Beat | On | Off | Dur | Text (line 1 / line 2) | Words | w/s | Change |
|---|---|---|---|---|---|---|---|
| 1 hook | 0.0 | 3.0 | 3.0 | Not clip art. / His breed. His name. | 7 | 2.33 | **CHANGED** (H1) |
| 2 | 3.0 | 6.0 | 3.0 | His bowl hasn't / moved since spring. | 6 | 2.00 | — |
| 3a | 6.0 | 8.8 | 2.8 | Every afternoon, / he's back on the wall. | 7 | 2.50 | line break only |
| 3b | 8.8 | 12.0 | 3.2 | His breed. His name. / In the light. | 7 | 2.19 | — |
| gap | 12.0 | 12.5 | 0.5 | (none) | | | |
| 4 | 12.5 | 17.0 | 4.5 | Only one Alex. / Only one of these. | 7 | 1.56 | **CHANGED** (C1 beat 4) |
| gap | 17.0 | 17.5 | 0.5 | (none) | | | |
| 5 CTA (top band) | 17.5 | 20.0 | 2.5 | Make one that's / only theirs | 5 | 2.00 | — |

### S-C1-H2

Same as S-C1-H1 except row 1:

| Beat | On | Off | Dur | Text | Words | w/s | Change |
|---|---|---|---|---|---|---|---|
| 1 hook | 0.0 | 3.0 | 3.0 | We still leave the / window open for him. | 8 | **2.67** ⚠ | — (not changed, by instruction; see Flags) |
| 2 → 5 | | | | identical to S-C1-H1 rows 2–5 | | | |

### S-C2-H1

| Beat | On | Off | Dur | Text | Words | w/s | Change |
|---|---|---|---|---|---|---|---|
| 1 hook | 0.0 | 3.0 | 3.0 | Not clip art. / His breed. His name. | 7 | 2.33 | **CHANGED** (H1) |
| 2 | 3.0 | 6.0 | 3.0 | His German Shepherd, / Alex, waited 11 years. | 7 | 2.33 | **CHANGED** (C2 beat 2) |
| 3a | 6.0 | 8.8 | 2.8 | Every afternoon, / he's back on the wall. | 7 | 2.50 | line break only |
| 3b | 8.8 | 12.0 | 3.2 | His breed. His name. / In the light. | 7 | 2.19 | — |
| gap | 12.0 | 12.5 | 0.5 | (none) | | | |
| 4 | 12.5 | 17.0 | 4.5 | Alex is back / in his spot. | 6 | 1.33 | — |
| gap | 17.0 | 17.5 | 0.5 | (none) | | | |
| 5 CTA (top band) | 17.5 | 20.0 | 2.5 | Make one that's / only theirs | 5 | 2.00 | — |

### S-C2-H2

Row 1 = the H2 hook (as in S-C1-H2, 8 words, 2.67 w/s ⚠). Rows 2–5 are identical to S-C2-H1.

### S-C3-H1

| Beat | On | Off | Dur | Text | Words | w/s | Change |
|---|---|---|---|---|---|---|---|
| 1 hook | 0.0 | 3.0 | 3.0 | Not clip art. / His breed. His name. | 7 | 2.33 | **CHANGED** (H1) |
| 2 | 3.0 | 6.0 | 3.0 | My neighbor lost Alex. / Flowers felt wrong. | 7 | 2.33 | **CHANGED** (C3 beat 2) |
| 3a | 6.0 | 8.8 | 2.8 | Every afternoon, / he's back on the wall. | 7 | 2.50 | line break only |
| 3b | 8.8 | 12.0 | 3.2 | His breed. His name. / In the light. | 7 | 2.19 | — |
| gap | 12.0 | 12.5 | 0.5 | (none; the dissolve ends at 12.2) | | | |
| 4 (spans 4a→4b cut at 15.0) | 12.5 | 17.0 | 4.5 | This felt like Alex. | 4 | 0.89 | — |
| gap | 17.0 | 17.5 | 0.5 | (none) | | | |
| 5 CTA (top band) | 17.5 | 20.0 | 2.5 | Make one that's / only theirs | 5 | 2.00 | — |

### S-C3-H2

Row 1 = the H2 hook (8 words, 2.67 w/s ⚠). Rows 2–5 are identical to S-C3-H1.

## Changed lines (old → new)

| Where | Old | New | Why |
|---|---|---|---|
| H1 hook (3 ads) | That's not a generic dog. / That's his actual breed — and his name. (12 w) | **Not clip art. / His breed. His name.** (7 w) | D4. The suggested "Not a generic dog. His breed. His name." is 8 words = 2.67 w/s in 3.0s, which fails D3. 7 words is the maximum (2.5 × 3.0 = 7.5). Same claim: name and breed are shown, not a generic image. No second person. Fallback if "clip art" tests unclear: "His actual breed. / His actual name." (6 w) |
| C2 beat 2 | Alex, his German Shepherd, / waited here 11 years. (8 w) | **His German Shepherd, / Alex, waited 11 years.** (7 w) | D3 (8 w = 2.67 w/s). Also, at 84px "Alex, his German Shepherd," is 1120px wide, over the 930px limit. Name, breed, "his" (= the owner) and 11 years are kept; "here" is dropped because the picture shows the place. Line 1 is 906px, close to the limit |
| C3 beat 2 | Alex was my neighbor's dog. / Flowers felt wrong. (8 w) | **My neighbor lost Alex. / Flowers felt wrong.** (7 w) | D3. Every 7-word wording that still had "dog" and "my" ran over 930px ("My neighbor's dog, Alex." = 988px). "Lost" makes the death clear. The picture under it (tight on the dog silhouette with "Alex") tells the viewer Alex is the dog. Check this in the muted cold read |
| C1 beat 4 | There was only one Alex. / So there's only one of these. (11 w) | **Only one Alex. / Only one of these.** (7 w) | Reading speed was fine (2.44 w/s), but at the D5 size the lines are 1001px and 1140px, over 930px, and the old 68px font fails the 60px cap height. The idea and the parallel are kept. The C1 headline in the ad copy can keep the long form |
| Beat 3a (all 6), line break only | Every afternoon, he's / back on the wall. | Every afternoon, / he's back on the wall. | Breaks at the comma; both lines ≤860px |

Unchanged wording: H2 hook, C1 beat 2, beat 3b, C2 beat 4, C3 beat 4, CTA.

## Flags (rules not fully met)

1. **H2 hook: 8 words in 3.0s = 2.67 w/s, over D3's 2.5.** Not changed, as instructed. To meet 2.5 it needs 3.2s, which breaks the D4 hook window (≤3.0s). The user decides: (a) accept 2.67 w/s; (b) run both hook captions 0.0–3.2 and start beat 2 at 3.2 (C1 6 w/2.8s = 2.14 ✓, C2/C3 7 w/2.8s = 2.50 ✓); or (c) trim H2 to 7 words.
2. **Band check:** 36–47% was checked only on the C2-H2 board. Verify the other 5, especially frame 1 of `HOOK-H1` (an ECU of "Alex") and C1/C3 beat 4.
3. **D2 "identical across all 6":** the rule is identical; the positions are not (C3 has a second dissolve at 12.0). See the producer call under the C3 timeline.
4. Beat 3a sits exactly on the limit (2.50 w/s), and it depends on having no caption fade. If the editor adds a fade-in, trim it to 6 words or start it at 5.8.
