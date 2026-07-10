# Tool Research — Teeinblue Product Personalizer (Shopify)

Researched 2026-07-10 (teeinblue.com + Shopify App Store). The personalizer app we'll use to make
designs **customer-customizable** — see the production model in
[`../sprints/print-files/README.md`](../sprints/print-files/README.md).

## Verdict for MadeJustForYou
**Strong fit — it directly supports our two-layer model and the variable-count problem.** The key
capability is **Conditional Logic** (show/hide options by selection) + **Clipart** libraries, which
is exactly how you build "one flower/bird/star per grandchild." It auto-generates the print file and
pushes to 30+ POD partners. Your designer's job stays the same (build consistent component art);
Teeinblue handles the live customization + assembly + fulfillment.

**Trust signals:** Shopify App Store **4.8–4.9★ (400+ reviews)**, TrustPilot 4.8. Scale claims:
20M+ personalized orders, $600M+ merchant revenue processed. Purpose-built for personalized POD
(not a generic options app).

---

## Capabilities that matter to us

### The one that unlocks "one-per-grandchild"
- **Conditional logic** — "show or hide options based on previous selections." → customer picks
  *number of grandchildren* → app reveals N name fields + N motif slots, and shows the matching
  design layers. **This is the mechanism for variable count.**
- **Clipart images** — pre-made graphics the customer mixes/matches (no upload). → your birth-month
  flowers / bird / star motifs live here; birth-month selection → the right flower.
- **Custom text** — single-line + paragraph, custom fonts, color picker, **date picker**,
  **curve** (curved text for mugs), **auto-scale**, **auto-fill**, **limit characters**, stroke,
  shadow. → nicknames (Grandma/Gigi/Nana), grandkids' names, "Est. year".

### Built-in dynamic generators (free future concepts)
- **Star map** — real night sky from a date+location (a literal "Grandma's Night Sky" engine)
- **Moon phase**, **calendar** (highlight dates), **Spotify song** (title/lyrics/artist),
  **street/route map**, **crossword** (names→crossword), **spiral text**

### Photo + AI (for photo/recipe/memorial concepts)
- Photo upload with **remove background, face cutout, B&W, custom-shape crop, photo border,
  portrait sketch**, and **Gen-AI effects** (OpenAI / Flux / Gemini). → "Best Papa Ever + photo",
  memorial collage, recipe-handwriting **photo upload**.

### Design studio & print pipeline
- **Design Studio:** drag-and-drop, unlimited elements, group layers, multi-layer editing,
  multi-design templates, **PSD import** — *your designer hands off a layered PSD and it drops in.*
- **Auto-generate print-ready file**, formats **PNG / JPG / PDF / SVG / AI / EPS** (keeps quality).
- **30+ POD partners** (Printful, Printify, Gelato, CustomCat, Dreamship, ShineOn, Merchize…),
  **1-click bulk fulfill**, CSV export, **tracking sync** back to Shopify.
- **Live real-time preview** on mockup; multi-language; mobile-first; no-code theme compatibility;
  multiple stores; team management.

---

## Our 5 greenlit concepts → Teeinblue build

| Concept | Teeinblue features used | Setup notes |
|---------|-------------------------|-------------|
| **Garden** (flower/grandchild) | conditional logic + clipart (12 birth-flowers) + text | build 1–10 child layers; birth-month → flower |
| **Little Birds** (bird/grandchild) | conditional logic + clipart (bird) + text | same pattern, one bird clipart repeated + name |
| **Night Sky** (star/grandchild) | conditional logic + clipart (star) + text **or** the built-in **Star map** | stylized = clipart; astronomical = star-map generator |
| **Grandma's Crew** mug | custom text (curve, auto-scale, limit chars) | simplest — variable name row, no motifs |
| **Recipe** tea towel | photo upload (handwriting) **or** paragraph text; Caveat font | offer both: upload real recipe OR type it |
| **First Dad Now Grandpa** mug | custom text + date picker (Est. year) + curve | names row + year badge |

**Variable-count recipe (Garden example):** field "How many grandchildren?" (1–10) → conditional
logic reveals that many `{name + birth-month}` pairs → each birth-month maps to a flower clipart →
layers assemble the bouquet → live preview → print file to POD. Build once per count, reuse forever.

---

## Pricing
- **One plan — $49/month**, unlimited Shopify stores, all features from day one.
- **14-day free trial** (no feature limits); **first 100 orders free**.
- After 100 orders, a **usage-based per-order fee that decreases as volume grows** (exact tiers not
  published on the page — **confirm current per-order rates in-app** before modeling margin).

---

## Limitations / things to verify
- **Setup effort is real:** conditional logic for 1–10 children means building the layer/rule set
  per count — a one-time designer+setup task, not automatic. Budget time for it.
- **Print quality = your component art quality.** Teeinblue assembles what you give it; you still
  need **clean, consistent, high-res transparent components** (the designer job we scoped). Garbage
  in → garbage print.
- **AI/Gen-AI effects** may carry extra usage cost/credits — verify if you use them.
- **Per-order fee** after 100 orders affects unit economics — get the exact tier table and fold it
  into the margin/CPA gates in [`../04-validation-testing.md`](../04-validation-testing.md).
- Confirm your chosen **POD partner** (Printful/Printify/etc.) actually stocks the substrates you
  want (sweatshirt, mug, tea towel) with the print method/area you need.

## Bottom line
Teeinblue can do everything our sprint designs require — **conditional logic + clipart is the
"one-per-grandchild" engine**, PSD import means the designer's file drops straight in, and it
auto-generates print files to 30+ PODs. Order of operations unchanged: **validate the metaphor
(Tier-1) → designer builds the consistent component set → wire it into Teeinblue → connect POD.**
