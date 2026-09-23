# Handoff — Phase-1 Testing-Plan Page + Translation Tooling (2026-09-20 → 09-23)

## Where we are
The Phase-1 test **method** was already settled (see `2026-09-13-video-ad-decomposition-and-pod-tailoring.md`).
This session turned it into a **Vietnamese page a supervisor can approve**, closed two holes the plan had,
and rebuilt the translation tooling after finding out why every machine translation read badly.

**Live: https://testing-plan-phase-1.namvu47.workers.dev** (Cloudflare Worker `testing-plan-phase-1`,
assets served from `marketing/facebook-ads/testing-plan-page/`, deployed with `npx wrangler deploy`).

---

## ✅ DONE — 23 commits

### 1. The page (13 sections, Vietnamese, light theme)
`marketing/facebook-ads/testing-plan-page/index.html` — now committed, not just in scratchpad.
Sections: Mục tiêu · thành phần video · Concept 3/12 · một concept nhiều bản dựng · khung dựng 9 bước ·
Hook 2/9 · ráp lại · ngưỡng tắt/đi tiếp · xem nhiều ≠ sẽ mua · ngân sách chứng minh được gì · quy tắc ·
cuối cùng biết gì · **sau Phase 1 test gì tiếp** · Nguồn.

### 2. Two real gaps closed in the plan itself
- **Section 04 — when does a concept advance, get fixed, or get parked.** The page said Phase 1 can't
  separate "wrong concept" from "bad execution" but gave no rule, so "ranking" meant nothing. Added a
  5-row hook × hold table read across a concept's **6 ads** (3 products × 2 hooks). Hold rate needs only
  76 impressions, which is what makes the two failures separable:
  `hook↑hold↑ ≥2/3 products + ATC≠0 → advance` · `hook↓hold↑ → recut 1.5s` · `hook↑hold↓ → rebuild body` ·
  `passes 1 of 3 → product effect` · `all 6 low/low → concept is the likely fault, park it`.
  **Phase 1 still kills nothing** — that needs 2–3 executions all failing.
- **Section 13 — the post-Phase-1 roadmap** (new). Answers "what else is worth testing".

### 3. Naming system (section 13)
`Phase` = budget tier + the metric it can afford · `Vòng` = one test inside it · `Cổng` = pass/fail, ranks
nothing. Avoided `Tier` and `C1/C2/C3` — taken by hook tiers (06) and concepts (07). **"Phase 1.5" is now
`Cổng Ý định`**, which is what section 09 already argued it was. Rounds are named by component, not
decimals (`Vòng 1.2` was unsayable):

| Phase | Vòng | Metric | Tiền/nhánh |
|---|---|---|---|
| **1 · Chú ý** | Concept · **Hook** · Craft · Format | hook/hold/link CTR | $2–44 |
| **Cổng Ý định** | ATC-optimised gate | — | — |
| **2 · Ý định mua** | Offer · Store | ATC · purchase rate | $1.057 / $1.315 |
| **3 · Lời lỗ** | — | CPA · ROAS as loss guardrail | — |

Run order is **Vòng Hook first**, before the cheaper Vòng Craft: both need a winning body, and hook is the
highest-variance component (same body cut 3 ways → 18%→38%). Craft is cheap enough to ride along.
`Vòng Hook` is also not optional — creative fatigues in ~2–3 weeks.

**"10–20 hooks" vs "9 in section 06" was a real contradiction** (he caught it). The 9 are *cách mở*
(tactics), not hooks. A hook is one written execution = on-screen text + opening shot. The source doc's
hook library already holds **16 written lines**; 3 wordings × 2 opening shots × 2 subjects = 12 more from
the winning tactic alone.

### 4. CTA changed
`"Make it for them"` → **`"Make one that's only theirs"`** — the old line could sit on any POD store and
never said the object is one of a kind. Recipient-neutral because Phase 1 locks one CTA across three
products with different recipients; `"only hers"/"only his"` are a Phase-2 variant. Added both plus
`"Make one no one else can give"` (giver-framed, end-card/VO length) to the CTA library in
`research/reference/video-ad-decomposition-2026.md`.

### 5. Translation tooling rebuilt — this was the session's biggest lesson
**The defect was the unit of work, not the model.** `gemma_md.py` sent Markdown **one line at a time** and
`gemma_tr.py` sent **batches of 40 unrelated strings** — so Gemma never saw the sentence it was
translating. That produced every symptom: broken wrapped sentences ("Feeds Group A" → "Nhóm Feeds A"),
terminology drifting between adjacent lines, half-Vietnamese/half-English tables. Both also silently fell
back to English on a length mismatch **and still printed success** — the doc came back 53% untranslated
while claiming to be done.

New scripts (`research/scripts/`):
- **`gemma_block.py`** — Markdown by block (72 paragraphs/tables/lists), each sent whole with its section
  heading as context. Validates table row+column counts and list item counts; 4 retries; **names any block
  it could not translate** instead of silently keeping English.
- **`gemma_html_block.py`** — the page by `<section>` (14), strings sent together with the heading. Large
  sections chunk at 25 but still receive the full section text as context. Escapes **text nodes** as well
  as attributes (the old script only did attributes — that's what decoded `&lt;18%` into a raw `<`), and
  preserves each text node's leading/trailing whitespace (that's what produced `Nguồn:<a>`).
- `gemma_fill.py` — patches holes left by a prior run.

### 6. …and the finding that came out of fixing it
Block-level removed every mechanical defect but exposed a second, separate problem: **given a whole block,
Gemma-27B takes liberties.** On the doc it *invented a table that exists nowhere in the source* (turned the
glossary line from my own system prompt into document content — 130 table rows vs the source's 67) and
translated pinned-English terms (`Offer`→`Ưu đãi`, `hold`→`Giữ chân`). On the page it collapsed concepts
01 and 07 into the same wording, mislabelled concept 04 (`Gấp theo dịp` → `Tạo sự khan hiếm` — the doc says
explicitly a deadline is not FOMO), and pointed concept 03 at the buyer instead of the recipient.

**Neither machine version was shipped.** Candidates left at `/tmp/page-block3.html` and `/tmp/vi-block.md`.

### 7. Google Doc
`video-ad-decomposition-2026-vi.md` fully translated and pushed **in place** (same ID/link) to
`1rCt4W2x1f72tYpHIgHyXV-82xNveBTrX4i8RIEJAp70`. Structure verified 270/270 lines, 22/22 headings,
67/67 table rows. Remaining English is deliberate: title, doc links, and quoted US ad copy.
⚠️ Files must be staged in `~/.workspace-mcp/attachments/` — the MCP refuses paths outside it.

---

## Language rules learned the hard way (he rejected each of these by name)
- **`nó` never for people or pets** — use the name or the kinship term.
- **No calques.** `xuống cuối hàng đợi` (back of the queue) → `gác lại` · `gắn cờ` (flag) → `đánh dấu` ·
  `ý tưởng cộng với` (plus) → `gắn với` · `kết luận nghe như thế này` (sounds like) → `sẽ ra dạng này`.
- **No slang or wrong register.** `chiêu` (street slang) → `cách mở` · `khai tử` (registering a death) →
  `loại` · `bắt ca` (medical) → `phát hiện` · `Nghi can` (criminal suspect) → `nhiều khả năng lỗi ở…`.
- **One word per concept.** `hook` / `đoạn mở` / `opener` were all the same thing → all now `hook`.
- **Ad copy and CTAs stay English** — the ads run to US buyers.
- **Don't translate away precision.** `qua` alone is ambiguous for passing a threshold → `đạt ngưỡng`.
- **The page is for a supervisor.** Cut meta-commentary about my own naming and design choices.
  → saved as memory `page-audience-is-supervisor.md`.

## My own errors caught in review (worth re-checking in future passes)
- Section 08 cited `mục 07` for the intent gate — it is **09**; the page contradicted itself.
- `Vòng Format` showed `$21–44`; it reads hook+hold so it is **$2–21**.
- Phase 3 showed `$1.315+ mỗi cặp` — **fabricated**; CPA/ROAS is a guardrail with no arms, now `—`.
- `C2/C3` used in section 04 but only defined in section 07.
- `Anh ngồi lặng` guessed the suncatcher owner's gender → `Người chủ`.

---

## ▶️ NEXT
1. **Get the page approved**, then build the 18 ads (3 concepts × 2 hooks × 3 products) from the 12-field
   brief in section 05. Nothing runs until the briefs exist.
2. **Hook must qualify** — the 3s opening has to reveal what gift is being sold, even in the emotional cut.
   This is the fix for the MJ4U-111 failure (great engagement, zero ATC) and it costs nothing.
3. **Log LPV→ATC from day one** — underpowered for comparison, enough to catch "lots of views, no carts".
4. After a winner: **Vòng Hook** (10–20 hooks) → Vòng Craft rides along → Vòng Format → **Cổng Ý định**.
5. **Proof-beat ranking is the cheapest open question we own** — reaction #1 down to craft close-up #5 is
   recorded in the source doc as an untested hypothesis with no A/B data in this category, and reads on
   hold rate for ~$2/arm.

## Open / not done
- Two stale Cloudflare Workers still live: `testing-plan` and `mj4u-test-protocol`. Asked twice about
  deleting them, never answered.
- `index-gemma.html` and the block-translation candidates are kept as diff sources, not published.
- Phase 2 needs its own plan page — different component set, different metrics.
