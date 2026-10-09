# Topic — Character references

**Status:** REF-OWNER set ✅ complete (8 images, fixed 2026-10-08); no other character has a set.

## Current decisions
- **8 separate full-resolution images, not one multi-panel sheet** (a ~50-panel sheet gives ~200–300px per face; sheets need text labels; Nano Banana has no negative-prompt field; the ~700-word JSON sheet prompt was rejected).
- Identity held across a camera change from ONE reference in stills (Test B).

## REF-OWNER set — `products/suncatcher-dog-memorial/assets/turntable-owner/` (LOCAL ONLY)
`owner-front`, `owner-34left`, `owner-34right`, `owner-fullbody-standing`, `owner-fullbody-seated`, `owner-hands`, `owner-expr-relief`, `owner-expr-smile` (+ `reference-set-qa.png`).

Fixed 2026-10-08 (~$0.30): `owner-hands` regenerated (apart, 5+5 fingers, no ring); `owner-expr-relief`
regenerated (neutral mouth, lowered lids; subtle vs front); `owner-fullbody-seated` **edited** to remove
a gold band the 09-29 QA missed. Old files → `_superseded-2026-09-29/`. Rule: QA hands at full res.

## Open items
- Media is never committed — backed up to Drive via `scripts/backup-media.sh` (decided 2026-10-08).
- No reference sets for REF-GIVER (suncatcher Body C, blocks clips 6–11) or any blanket character.
- Multi-reference identity across independent clips untested.

## Detail
- `research/reference/image-prompt-method.md` §"Character reference set — template" → "QA result — 2026-09-29" + "Fix pass — 2026-10-08"
- Session: [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
