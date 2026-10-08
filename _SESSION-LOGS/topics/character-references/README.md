# Topic — Character references

**Status:** REF-OWNER set built (8 images), 2 views need regeneration; no other character has a set.

## Current decisions
- **8 separate full-resolution images, not one multi-panel sheet** (a ~50-panel sheet gives ~200–300px per face; sheets need text labels; Nano Banana has no negative-prompt field; the ~700-word JSON sheet prompt was rejected).
- Identity held across a camera change from ONE reference in stills (Test B).

## REF-OWNER set — `products/suncatcher-dog-memorial/assets/turntable-owner/` (LOCAL ONLY)
`owner-front`, `owner-34left`, `owner-34right`, `owner-fullbody-standing`, `owner-fullbody-seated`, `owner-hands`, `owner-expr-relief`, `owner-expr-smile` (+ `reference-set-qa.png`).

| File | Problem | Fix |
|---|---|---|
| `owner-hands.png` | hands overlap; adds gold ring no other view has | regenerate hands apart, no ring |
| `owner-expr-relief.png` | reads as a plain smile | neutral mouth, breath-out cue, no smile |

~$0.60 total to regenerate.

## Open items
- **`*.png` is gitignored repo-wide (`.gitignore:7`)** — the set has never been committed. Decision pending: `git add -f`? **Do not force-add without user go-ahead.**
- No reference sets for REF-GIVER (suncatcher Body C, blocks clips 6–11) or any blanket character.
- Multi-reference identity across independent clips untested.

## Detail
- `research/reference/image-prompt-method.md` §"Character reference set — template" → "QA result — 2026-09-29"
- Session: [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
