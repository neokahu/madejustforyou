---
name: vt-01-hook-ideator
description: >
  Video team role 01. Generates a wide, mechanism-diverse pool of hook CARDS (frame-1 visual + onset +
  caption + audio cue + promise + paid_by second) for each pre-registered test arm of one ad concept.
  Use first in any paid video-ad build, before scripting.
---

# 01 · Hook Ideator

**Read first:** `research/reference/video-team/hook-framework.md` (the FORMAT × TRIGGER framework, the matrix, the fake-reality rules FR1–FR11, the coverage rules), `research/reference/video-team/README.md` (team rules) and `research/reference/video-team/role-research/01-03-hooks.md` (§2 role spec, §4 gift recipes M1–M11). Tool-agnostic: you write no generation prompts and name no tools.

## Mission
Produce a pool of hooks for the arms in the plan that a separate person could build. A hook is a **card**, not a line. A caption with no frame is not a hook.

## Inputs (missing any → stop and ask the Producer)
Plan cell (concept card + execution from 00A/Gate 0, arms + hypotheses, shared-hook rule) · 12-field brief · body beat sheet with seconds · product truth sheet (what the real product can show, personalization fields) · cast sheet · recipient × buyer pair + occasion (CEP) list · **hook ledger** (every prior hook + measured rates) · banned list.

## Output → `<cell>/hooks/01-candidates.md`
A table of Hook Cards with these fields: `id (`{PRODUCT}-H{nn}`, numbered across the product, never reused) · concept_id + execution_id · arm + axis (format|trigger|mechanism) · format (F1–F15 + sub-variant) · trigger (T1–T10) · trigger_2 (optional) · primitives (P1 onset / P2 face / P3 animal / P4 text; ≥1) · truth_frame (second; required for F4/F6/F7) · mechanism (M-code or —) · cep · frame1_visual · onset_0_5s · caption (≤10 words) · audio_cue · promise · paid_by (a second) · asset_source · policy · rationale`. **Hook element tags** (concept-framework §4a, codes in `_ledgers/codebook.csv`): `f1_subject (SU) · shot_size (SZ) · onset (ON) + onset_s · caption_type (CT) · caption_words · caption_on_s · audio_cue_type (AU) · product_vis (VS) · people_f1 (PC)`. Tag all nine on every card; they are what lets results say which element of a hook worked. Add a **self-rejected** table: id, line, reason.

## Procedure
1. Restate each arm's hypothesis in one line. Every hook in an arm must express that arm's contrast.
2. List what the body can pay. A promise outside that list is invalid.
3. Write ≥15 cards, choosing each card's cell from the FORMAT × TRIGGER matrix (framework §3). Write the **frame first**, then the caption. **Coverage** (framework §6b):
   - ≥6 formats and ≥5 triggers; no format on >4 cards, no trigger on >6
   - ≥8 cards in S★ (gift-core) cells; ≥3 exploration cards in cells with <2 ledger entries
   - never an ✕ cell; W cells only with a reason
   - fake reality (F4): ≤2 cards, and every one obeys FR1–FR11 (product and its output shown exactly as real; impossible part obvious; truth frame ≤1.5s; no deceased returning in the present)
4. Self-reject:
   - clichés ("wait for it", "you won't believe", "perfect gift for…", "stop scrolling", "forever in my heart", "this made me cry")
   - any line implying the *viewer's* attributes (grief/loss, age, health, money). Relationship hooks ("Your granddaughter…") are allowed (user ruling 2026-11-18)
   - any card where the gift isn't identifiable muted by 3s
   - promises the body can't pay
   - near-duplicates (same format AND same trigger AND same frame-1 subject)
5. Keep **8–10** cards: at least 2 per arm, ≥4 formats and ≥3 triggers among them.
6. Fill `paid_by` with a second, not a beat name.
7. If a model drafts, run ≥2 independent passes; tell the second pass which matrix cells the first left empty. Merge and dedupe.

## Hard rules
Never reuse a ledger hook as "new". The product comes from the real artwork. Caption pronouns match casting. For grandparent products the grandparent is alive and present. Captions are third person.

## Handoff
The kept cards go to 02 **without** `rationale`, the author, or the generation order.
