# Grandma's Little Birds — Layout Spec (1–10 birds) · test build

**Concept:** GPD02 slot 2B — *"a bird per grandchild on a branch."* **Mechanic:** roster (one-per-grandchild). Differentiates from Macorner's owned "Grandma's Garden" birth-flower lane by swapping the metaphor (birds, not flowers) — works year-round, not just spring.

**The rule that defines this build:** the **bird artwork is NOT hard-coded.** Each grandkid bird is a **customer-picked clipart** from a bird library. What *we* design is the **LAYOUT** — how N birds arrange so the composition looks balanced at every count 1→10. The customer never moves anything; they pick a count, pick a bird + type a name per grandchild, and Teeinblue swaps to the matching layout.

Teeinblue mapping (per `research/reference/teeinblue-assets-guide.md` §7):
| Customer sees | Teeinblue type | Renders |
|---|---|---|
| Bird per grandchild | **Clipart Category** "Birds" (transparent PNGs) | placed into the slot |
| Number of grandkids (1–10) | **Additional Option** 1–10 | no render — drives conditional layout |
| Name per grandchild | **Text layer** (auto-scale, ~12-char limit) | text under each bird |
| Nickname (Grandma/Nana/Mimi…) | Additional Option or Text | title line |

---

## 1. Fixed frame (always on — solves the "1 bird looks empty" problem)
These render at **every** count, so low counts never look sparse:
- **Branch / tree art** — the perch. Two stacked branches (a top and a lower) drawn so either can be used.
- **"Grandma bird"** — one larger anchor bird (owl or robin), perched top-center or on a small nest. Fixed focal point.
- **Title** — "**{Nickname}'s Little Birds**" (Grandma/Nana/Mimi/Gigi via nickname option) + optional subtitle *"the whole flock loves you."*
- Grandkid birds are added **below / around** the grandma bird.

## 2. Shared design rules (designer builds once)
- **Print area:** treat as portrait ~3600×4200px (apparel); rebuild proportionally per product. Keep birds inside a center **safe column** (~80% width).
- **Bird slot = normalized box.** ⚠️ Teeinblue **reposition is per-clipart-category** — every bird in the library inherits ONE size/anchor. So build the whole bird library on a **common canvas** (suggest **520×520px**, subject centered, **feet on the bottom-center anchor**) so any picked bird perches identically in any slot. (Guide §4.)
- **Name tag:** small hanging tag or text directly under each bird. Text layer, max-width ~360px, **auto-scale on**, char limit ~12, one font (script accent, e.g. Caveat).
- **Even spacing, center-balanced.** Every count is **horizontally centered** about the mid-line — never fill left-to-right (that looks lopsided at low N). Positions below are % of print width, center = 50.

## 3. Per-count layouts (the deliverable)

**Row logic:** 1–5 birds = single (lower) branch; 6–10 = two branches, split as evenly as possible. Grandma bird + title sit above throughout.

```
 ┌───────────────── every count ─────────────────┐
 │            🦉  {Nickname}'s Little Birds        │   ← fixed grandma bird + title
 └────────────────────────────────────────────────┘
```

| N | Rows (top / bottom) | Bird X-positions (% width, centered) | Sketch (lower branch) |
|---|---|---|---|
| **1** | 1 | 50 | `———🐦———` |
| **2** | 2 | 38 · 62 | `——🐦——🐦——` |
| **3** | 3 | 30 · 50 · 70 | `—🐦—🐦—🐦—` |
| **4** | 4 | 24 · 41 · 59 · 76 | `🐦 🐦 🐦 🐦` |
| **5** | 5 | 18 · 34 · 50 · 66 · 82 | `🐦 🐦 🐦 🐦 🐦` |
| **6** | 3 / 3 | top 30·50·70 · bottom 30·50·70 | two rows of 3 |
| **7** | 4 / 3 | top 24·41·59·76 · bottom 30·50·70 | 4 over 3 |
| **8** | 4 / 4 | top & bottom 24·41·59·76 | 4 over 4 |
| **9** | 5 / 4 | top 18·34·50·66·82 · bottom 24·41·59·76 | 5 over 4 |
| **10** | 5 / 5 | top & bottom 18·34·50·66·82 | 5 over 5 |

**Vertical:** single-row counts (1–5) sit on the **lower** branch (leaves room for grandma + title above). Two-row counts (6–10) use **both** branches. Name tags hang ~120px below each bird's feet.

**Two-row sketch (e.g. N=8, 4/4):**
```
        🦉  Nana's Little Birds
   🐦   🐦   🐦   🐦        ← top branch  (24·41·59·76)
    Ava  Leo  Mia  Sam
   🐦   🐦   🐦   🐦        ← lower branch (24·41·59·76)
    Ivy  Max  Zoe  Eli
```

## 4. Teeinblue build & layer budget
- **1 Additional Option** `Number of grandkids` (items 1–10) → drives all conditionals (no render). Guide §5.
- **Per count N:** a layer group shown only when `Number of grandkids = N`, containing **N bird-clipart layers + N name-text layers** positioned per the table.
- **Layer budget:** Σ(1..10) = **55 bird slots + 55 name layers ≈ 110 layers** (+ fixed frame + title). Heavy but standard for this mechanic. Bird clipart library + name tags are shared assets; only *positions* differ per count.
- **Each bird slot** = layer personalized via **"1 Clipart category" → Birds** (customer picks the bird). Guide §2.
- **Nickname** drives the title (Additional Option → conditional title text, Route A, Guide §3), or a simple text field.

*(Build-cost reduction options were considered and declined — see LOCKED decisions below. Full 1–10, center-balanced.)*

## 5. Test plan
> **Asset brief (art + Nano-Banana prompts):** [`2B-bird-library.md`](2B-bird-library.md). This spec = layouts; that brief = the reusable art.

1. **Design first:** the fixed frame (branch + grandma bird + title) + the **bird library** (start ~8 birds: robin, bluebird, cardinal, owl, chickadee, sparrow, dove, goldfinch — all normalized to the 520×520 feet-anchor box).
2. Build layouts **N=1–5** (single branch) first to validate spacing/centering, then **6–10** (two branches) — all 10 ship in this test.
3. **Validate:** mock each count with real names; check no overlap, tags legible, group optically centered. Compare against the branch competitors in the concepts doc refs (Macorner candle, birth-flower sweatshirts).
4. Lead test = **2A "Grandma's Garden" vs 2B "Grandma's Little Birds"** (per concepts doc) — this spec is the 2B build.

## Decisions — LOCKED 2026-07-30
1. ✅ **Center-balanced per-count layouts** (not fixed-perch). Each N 1–10 gets its own centered arrangement → **~110 layers** (55 bird slots + 55 name tags). Best composition at every count.
2. ✅ **Full 1–10** built now (~55 bird slots) — no 1–6 MVP staging.
3. ✅ **Fixed Grandma bird + title anchor** ON — larger owl/robin + "{Nickname}'s Little Birds" always on screen; fills low counts.
4. ✅ **Names ON** (tags under each bird) — roster personalization is the point.
5. Branch rows (not tree tiers) — matches the metaphor, easiest to center.

→ Build scope is settled; §3 table + §2 rules are the authoritative build target. Designer starts with §5 step 1 (fixed frame + normalized bird library), then all 10 layouts.
