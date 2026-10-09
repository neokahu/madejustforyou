# Suncatcher Phase 1: open questions for the user

> Collected from the "Escalate to the user" sections of the three council verdicts (`_council/C*/verdict.md`, 2026-10-08), deduplicated, plus the change-list items held back because they would break a plan lock.

## Revision 2 — user answers 2026-10-08

**Every question is now resolved or parked.** Nothing is open. The answers are applied in `HOOKS-shared.md`, `C1-personalization.md`, `C2-reaction.md` and `C3-buyer-swap.md` (each carries a Revision 2 changelog). No `⟂ IF / ⟂ ELSE` branch remains in any script. The build is ready to run from `HOOKS-shared.md` §10 (BUILD LIST).

| Status | Questions |
|---|---|
| ✅ Resolved and applied | Q1, Q2, Q3, Q4, Q5, Q6, Q11, Q14, Q15 |
| 📝 Kept as build/read notes | Q7, Q8 |
| 🅿️ Parked (not adopted this round) | Q9, Q10, Q12, Q13 |

## Answer log

| # | Question | User's answer (2026-10-08) | Status | Where it was applied |
|---|---|---|---|---|
| **Q1** | Does the real 6" panel, in direct sun, throw a legible "Alex" on the wall, and a recognisable German Shepherd shape? | **Yes**, both. | ✅ Resolved | Every `⟂ IF` (projection-true) branch kept and every `⟂ ELSE` deleted: B3b = `WALL-4K` with the real "Alex" (`HOOKS-shared.md` §4); third bullet "his shape lands on the wall" (§4b and all three primary texts); C1 plan role and C1-c; C2 beat 4 German Shepherd-shaped light in the bed (C2 #1). |
| **Q2** | Standard offer, shipping and delivery window, gift options? | **Irrelevant to the video ads.** | ✅ Resolved | `[STANDARD OFFER — confirm]` removed from all copy. Brief field 6 = "standard offer — handled outside the creative" (plan Phase 2). No shipping, delivery or arrival claim anywhere. `HOOKS-shared.md` S6 closed. |
| **Q3** | Does the product page show a breed picker, a live name preview and a real in-sun photo? | **Yes**, all three. | ✅ Resolved | No change needed. |
| **Q4** | Can a gift-buyer ship to the recipient, add a gift note, see an arrival date? Giver landing-page variant? | **No ship-to-recipient or gift-note feature.** | ✅ Resolved | No copy claims shipping to the recipient, a gift note or an arrival date. In C3 the friend hands it over herself (beat 4a), and her primary text says "So I **brought** him" (was "sent"). No giver landing-page variant (test structure unchanged). |
| **Q5** | Does the POD ship in kraft, tissue and twine? Could a gift tag be included? | Ships in a **standard box**. **Correction from the user:** the ad should still show an attractive gift box, because it is advertising; a plain shipping box would look unattractive. The handwritten tag may stay as the friend's own card. | ✅ Resolved | C3 keeps the kraft gift box, white tissue, twine and the card "For you — and Alex." as **her own wrapping and card** (styling props, not store features). `F-BOX.png` stays REUSE for beat 2. No copy claim about packaging. |
| **Q6** | Who is the buyer in C1 and C2? Add a gifter bridge? | **C2: OK** to add a gifter bridge line. Do not change C1. | ✅ Resolved | C2 primary text: "For anyone missing their dog — or someone you love who is." Persona and brief otherwise unchanged. C1 unchanged. `HOOKS-shared.md` S10 updated. |
| **Q7** | S-C2-H2 (and H2 generally) may read as a human death. | Keep as a build/read note. | 📝 Note | Muted "is this about a dog?" QA on HOOK-H2 frame 1 before animating (`HOOKS-shared.md` §3, §7). C2's new beat-2 caption (Q14) adds a second dog cue at 3.0s. Don't back H2 to scale on craft logic. |
| **Q8** | Can this test separate the concepts? | Keep as a read note: the concept is judged across the 3 products, per plan §04. | 📝 Note | `HOOKS-shared.md` §7 read note; cell differences recorded in C1-f, C3-c, C3-e, C3-g. Don't call H1 vs H2 from one concept. |
| **Q9** | Adult child's second hand over his in C1 beat 4. | Not adopted this round. | 🅿️ Parked | — |
| **Q10** | Breed flip in C1 beat 2. | Not adopted this round. | 🅿️ Parked | — |
| **Q11** | Music bed approval (`ads/shots/music.mp3`). | **Approved.** | ✅ Resolved | `HOOKS-shared.md` §6 Voice; all briefs field 10. |
| **Q12** | Re-shoot B3 in the armchair room (C2-d). | Not raised; council view stands (not needed). | 🅿️ Parked | — |
| **Q13** | Cat, coworker and vet-clinic versions of the C3 buyer swap. | Not adopted this round. | 🅿️ Parked | Log for after Phase 1. |
| **Q14** | C2 beat-2 caption naming Alex as a dog, within the caption-speed lock. | **Approved default:** "Alex, his German Shepherd, waited here 11 years." | ✅ Resolved | C2 beat 2 (8 words over 3.0s = 0.375s/word). C2-h closed. |
| **Q15** | Headline format differs between cells. | **Approved default:** one format for all three: `<concept's emotional line> – Personalized Dog Memorial Suncatcher`. | ✅ Resolved | C1 `There was only one Alex. So there's only one of these. – Personalized Dog Memorial Suncatcher` · C2 `The room still turns gold at four – Personalized Dog Memorial Suncatcher` · C3 `What to send when flowers feel wrong – Personalized Dog Memorial Suncatcher` (emotional line in sentence case in all three). |

## One wording note for the user (not a question that blocks the build)

C3's headline keeps its existing line, "What to send when flowers feel wrong", as instructed. "Send" is ordinary sympathy-gift wording, not a shipping claim, but since there is no ship-to-recipient feature, "What to give when flowers feel wrong" is available as a one-word swap if you prefer to avoid "send" altogether.

## Build notes (read before generating)

- **Single-move clips.** C1-B2, C1-B4, C2-B4 and C3-B4a are one named shot with one camera move, as the council asked (fewer moves, fewer morphs). These are body beats whose cuts come from the edit, so the trade against the two-shot recipe is deliberate. Each clip still opens on a moving camera.
- **C2-B2 is a fixed camera** (council C2 #4). The prompt guard blocks a fixed Shot 1 (`OPENMOVE`), and kie.ai `seedance_2_video` has no `commandId` to carry `ACK-OPENMOVE`. Ask the user before running row 8a; otherwise run row 8b (very slow push-in, same frame 1). Check that the assembled 0–3s doesn't feel dead.
- **No lettering in model references.** C1-B4 uses `WALL-4K-clean.png` (before the "Alex" paste) as its shadow reference, so the model has no text to copy. Every legible name is a PIL paste from the product artwork onto a still (R22).
- **Prompt guard check.** Every prompt in the BUILD LIST was run through the guard on 2026-10-08 and passes, except row 8a (above).
