# Topic — Product text fidelity

**Status:** settled — the earlier "AI cannot render legible text" rule was WRONG.

## Current decisions
- Given the real product as reference at 2–4K, models reproduce printed text: 4-letter name word-perfect (Nano Banana Pro, Seedream, GPT Image); **~50-word four-colour poem word-perfect**, flat and draped.
- **Cloth needs no mesh warp** — print follows folds in correct perspective, unprompted.
- **Legibility ≠ fidelity:** right word in the wrong font still misrepresents what ships (GPT Image "Alex" wrong typeface; Seedance redrew the name bolder mid-shot and deformed the panel).
- Video re-synthesis causes drift → use stills + Ken Burns for text close-ups. The compositing engine was **never needed**.
- **QA must read the text across multiple frames** — never judge from one frame ("ceeling" was a fold occluding the ascender). `motion_qa.py` cannot read.

## Evidence
- Tests F, D1–D3 and the six-overturned-rules table — sessions/2026-09-26 §5–§10.

## Detail
- `research/reference/product-text-fidelity-2026.md`
- `research/reference/RESEARCH-REPORT-2026-10-ad-production.md`
- Session: [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md)
