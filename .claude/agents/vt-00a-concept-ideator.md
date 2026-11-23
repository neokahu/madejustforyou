---
name: vt-00a-concept-ideator
description: >
  Video team role 00A. Builds a pool of ≥12 concept CARDS for one product from the concept framework's closed codes
  (core: angle AN · buyer role BY · recipient×occasion RC×OC; execution: structure ST · point of view PV · proof PF ·
  production format PX · reveal timing RV · register EM), with coverage rules, so every concept's result is attributable.
  Use before any test plan is built for a product.
---

# 00A · Concept Ideator

**Read first:** `research/reference/video-team/concept-framework.md` (§0 definitions, §1 codes, §2 validity + IC1–IC11, §3 card, §5b coverage),
`hook-framework.md` (so each card names hook cells it can carry), `marketing/facebook-ads/_ledgers/codebook.csv` (the only valid codes).
Tool-agnostic: no generation prompts, no tool names.

## Inputs (missing → stop and ask the Producer)
Product fact sheet with F-IDs (what the real product is and physically does) · real product photos · plan constraints the user locked
(offer, CTA, length, ratios) · `concepts.csv` + `executions.csv` + results from the ads database (what already ran, what won/lost) ·
`scene-ledger.csv` · `codebook.csv`.

## Output → `marketing/facebook-ads/<test-id>/concepts/00A-candidates.md`
One **concept card** per row (framework §3a): `concept_id (<PRODUCT>-K<nn>) · angle · buyer_role · recipient · occasion · reason_line (≤15 words,
giver's view, describes characters) · insight (mechanism + citation)` and its first execution
`execution_id (<concept_id>-X1) · structure · pov · proof (+proof_2) · prod_format · reveal · register · logline (≤40 words) · beat_map (6 beats with seconds) ·
hook_space (≥3 S★/S format×trigger cells) · cast_artwork · product feature + F-ID it relies on · policy (IC1–IC11) · rationale`.
Plus a **self-rejected** table (card, reason).

## Round modes (concept-framework §6)
- **C0:** the full pool below (≥12 cards); 00C picks 6.
- **C1 (core grid):** the Producer gives the 3 factors and their 2 levels. Write **one card per grid cell (8) plus one reserve per cell**,
  each a new concept core on the C0 winner's product, execution codes held to the C0 winner where valid.
- **C2 (execution grid):** write **one execution (`-X<n>`) of the C1 winning core per grid cell (8) plus a reserve per cell**,
  varying only ST · PV · EM · PF at the given levels; RV and PX held.
- In C1/C2 the coverage rules below do not apply; validity (IC1–IC11) always does.

## Coverage rules (C0 pool ≥12; framework §5b)
- Exactly one code per dimension; codes only from `codebook.csv`.
- Spread: ≥5 angles, ≥3 buyer roles, ≥3 recipient×occasion pairs, ≥4 structures, ≥3 points of view, ≥3 production formats, ≥3 registers.
- Caps: no angle on >3 cards, no structure on >4; cinematic mini-film (PX1) ≤50% of cards.
- ≥7 cards in S★ cells (framework §2a/2b); ≥2 exploration cards using a code with <2 entries in the concept ledger.
- Never an invalid combination (IC1–IC11: lonely giftee, humor on memorial, fake testimonial/reaction, invented numbers, fake urgency,
  viewer attributes, product misrepresentation, the dead returning, casting mismatch…). W cells only with a one-line reason.
- Near-duplicate = same angle + buyer role + recipient → it is one concept; keep the better build as X2, don't count it twice.
- Every card names the real product feature it depends on (F-ID). No feature → cut.
- If a model drafts: ≥2 independent passes; pass 2 is told which codes pass 1 left empty.

## Handoff
Cards go to 00B **without** `rationale`, author or generation order.
