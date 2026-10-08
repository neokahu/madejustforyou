# Topic — Translation tooling (EN → VI, Gemma)

**Status:** rebuilt; machine output still not shippable without review.

## Findings
- **Defect was the unit of work, not the model:** line-at-a-time (`gemma_md.py`) and 40-string batches (`gemma_tr.py`) meant Gemma never saw the sentence; both silently fell back to English and still printed success (doc came back 53% untranslated).
- Block-level fixes mechanics but **Gemma-27B takes liberties** given a whole block (invented a table — 130 rows vs 67; translated pinned-English terms; collapsed/mislabelled concepts). Neither machine version was shipped.

## Current tools (`research/scripts/`)
- `gemma_block.py` — Markdown by block with section heading as context; validates table/list counts; names failed blocks.
- `gemma_html_block.py` — page by `<section>`; escapes text nodes; preserves whitespace.
- `gemma_fill.py` — patches holes from a prior run.

## Rules
VI language rules (no `nó` for people/pets, no calques, no slang, one word per concept, ad copy/CTAs stay English) — sessions/2026-09-23.

## Detail
- Google Doc (VI decomposition) `1rCt4W2x1f72tYpHIgHyXV-82xNveBTrX4i8RIEJAp70`; stage files in `~/.workspace-mcp/attachments/`.
- Session: [2026-09-23](../../sessions/2026-09-23-phase1-testing-plan-page.md)
