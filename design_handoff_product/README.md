# Handoff: MadeJustForYou — Product page template (Shopify Horizon)

## Overview
MadeJustForYou is a personalized print-on-demand gift brand (mugs, drinkware, apparel, signs, ornaments, pillows, tote bags, home decor). The core customer is a **gift-giver** buying something meaningful for one specific person.

This handoff covers the **product page template only** (`templates/product.json`). The home page template is specified separately; header, footer, and announcement bar are shared and already covered there.

## ⚠ Scope boundary: the personalizer belongs to teeinblue

**Personalization is rendered by teeinblue, not by the theme.** The name/photo/preview UI — its inputs, live preview, validation, upload flow, and internal markup — is app-owned and largely not editable from the theme. **Do not rebuild it, and do not restyle its internals.**

What this handoff specifies is **everything around it**: page layout, gallery, headings, price, benefit pills, quantity/add-to-cart, shipping note, accordion, description, related products, reviews, and the type/color/button system they all share.

The personalizer appears in the design as a simplified stand-in (a label + a filled field showing "Nathan & Bruce"). Treat that block as a **placeholder marking where the teeinblue app block mounts** — match its vertical position and the space it occupies, not its internals.

**Where the theme can still influence teeinblue** — do these, and stop there:
1. **Position** — place the teeinblue app block in the Product information section between the variant picker and the buy buttons. That order is intentional: choose the thing, personalize the thing, buy the thing.
2. **Inherited type and color** — the app inherits page font-family and many colors from theme CSS. Getting the theme tokens right (below) fixes most of its appearance for free.
3. **A section-scoped nudge, if needed** — if the app's labels or inputs clash badly, a narrow override scoped to the app block's wrapper is acceptable for **font-family, font-size, label color, input border-radius, and border color only**. Keep it minimal and commented. Do not restyle its layout, do not fight its JS, do not touch its preview canvas.
4. **Anything beyond that is a teeinblue setting**, not a theme change — configure it in the app, don't patch it in Liquid.

Two things to verify rather than build:
- The **chosen personalization value must travel with the line item** into the cart, drawer, and order confirmation. This is what reassures a gift-buyer the right name is on the right product. It's teeinblue line-item-property behavior — confirm it renders in the cart drawer; don't reimplement it.
- **"Personalized free"** is stated in the benefit pills, which are theme-side. Keep that claim consistent with whatever the app actually charges.

## About the Design Files
The file in this bundle is a **design reference authored in HTML** — a prototype showing intended look, structure, and behavior. It is **not production code to copy**.

Target environment: an **existing Shopify store on the Horizon theme** (Online Store 2.0, section/block architecture, Liquid + theme settings, no build step). Work in this order:

1. **Theme settings first** — colors, typography, buttons, radii. Most of this design is achievable by configuring existing settings, and it also fixes the app's inherited styling. Doing this first prevents writing CSS to override things that are just settings.
2. **Stock Horizon blocks second** — the Product information section already has blocks for title, price, variant picker, quantity, buy buttons, description, and accordion. Prefer configuring them over building custom ones.
3. **Custom Liquid only where noted** — matching the theme's existing `mc-*` convention (`mc-name.liquid` + `mc-name.css` + `mc-name.js`, using `--mc-font-*` custom properties).

No JS framework, no CSS framework, no build tooling. Don't hardcode hex values where a theme setting or `--mc-*` property exists.

## Fidelity
**High-fidelity** for everything theme-owned — colors, typography, spacing, and radii are final. **Best-effort** for the teeinblue block: match position and surrounding rhythm; accept its own internals.

## Viewing the design
Open `MadeJustForYou Website.dc.html` in any browser. A **template switcher** sits at the top (Home / Collection / Product) — a design-tool affordance, **not part of the theme**. Select **Product**.

Every image is a labeled drop-target placeholder (`<image-slot>`). `image-slot.js` and `support.js` are prototype helpers and **must not ship**.

---

## Design Tokens

### Colors
| Token | Hex | Role |
|---|---|---|
| Cream | `#FBF6EE` | Page background; text on dark surfaces |
| Warm Sand | `#EFE4D4` | Image wells, recessed fills |
| Sand Tint | `#F4E7D7` | Benefit pills |
| Clay | `#C15F3C` | **Primary accent** — add to cart, price, links, active thumb, icons |
| Clay Hover | `#A64C2C` | Button/link hover |
| Clay Pressed | `#8F3F23` | Button active |
| Honey | `#E0A458` | Stars |
| Rose Tint | `#F7DCD3` | Selected variant chip background |
| Rose Deep | `#B0472A` | Text on Rose Tint |
| Warm Ink | `#3B2A20` | Primary text; announcement bar, footer |
| Stone | `#8A7E70` | Muted text, labels, chevrons |
| Stone Light | `#A8977F` | Strikethrough compare-at price |
| Border | `#EADCC8` | **Default border on cream** |
| Border Alt | `#E2D5C3` | Slightly stronger border on inputs/steppers |
| White | `#FFFFFF` | Elevated surfaces — gallery, cards, inputs |
| Shop Pay Purple | `#5A31F4` | Shopify-owned, not editable |

**Layering rule:** cream is the page, **white is elevation** (gallery, cards, inputs), warm sand is recessed. A white surface on a cream page still needs `1px solid #EADCC8`.

### Typography
Three fonts, each with **one fixed job on every surface**.

| Role | Family | Usage |
|---|---|---|
| Heading | **Playfair Display** | Product title, price, section headings, accordion headings, wordmark |
| Body | **DM Sans** | Body copy, labels, buttons, variant chips, review text |
| Subheading / Accent | **Caveat** | Short handwritten eyebrows only — **not used on this page** |

- Design was authored against Hanken Grotesque, which isn't in Shopify's library. **DM Sans** is the approved substitute.
- **The brand name is always Playfair** — never Caveat. "Just" is italic clay.
- **Caveat is never uppercase, never letter-spaced, never below 20px.** There's no Caveat on the product page by design — this page is a transaction, not a campaign.
- Playfair never below weight 600.
- Two weights per family: DM Sans 400 + 600; Playfair 600 + 700; Caveat 700.

**Scale used on this page**
| Element | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| Product title (h1) | 44px | 700 | 1.06 | -0.015em |
| Price | 32px | 700 | 1 | 0 |
| Section heading | 32px | 600 | 1.1 | -0.015em |
| Accordion heading | 17px | 600 | 1.3 | 0 |
| Body / description | 15px | 400 | 1.65 | 0 |
| Review body | 15px | 400 | 1.6 | 0 |
| Reviewer name | 15px | 600 | 1.4 | 0 |
| Buttons | 15px | 600 | 1 | 0.08em, uppercase |
| Uppercase field label | 13px | 600 | 1 | 0.06em |
| Variant chip | 14px | 500 | 1 | 0 |
| Small / muted | 12.5–13px | 400 | 1.4 | 0 |

Description capped at **56 characters** (`max-width: 56ch`); review body at ~60ch.

### Spacing, radius, elevation
- Container `max-width: 1300px`, side padding `40px`
- Two-column product layout: `1fr 1fr`, gap **56px**, `align-items: start`
- Section rhythm below the fold: `76px`
- Radius: **14px** buttons, inputs, gallery, Shop Pay · **12px** personalization input, product cards · **10px** thumbnails, variant chips · **999px** benefit pills, quantity stepper
- Borders `1px` default, `1.5px` on interactive controls (inputs, stepper, unselected chips)
- Thumbnails: active `2px solid #C15F3C`, inactive `1px solid #EADCC8`

---

## Theme settings to apply

**Palette:** Background `#FBF6EE` · Text `#3B2A20` · Muted text `#8A7E70` · Accent `#E0A458`
**Footer group:** Background `#3B2A20` · Text `#B7A794` · Muted text `#9C8B78` · Accent `#E0A458`

**Typography:** Body → DM Sans · Heading → Playfair Display · Subheading → Caveat · Accent → Caveat
- Paragraph 16px, line height Loose
- H1 48px — line height **Tight**, letter spacing **Tight**, case Default
- H2 40px — line height **Tight**, letter spacing **Tight**, case Default
- H3 32px — line height Tight
- H4 → font **Body**, 14px, uppercase, letter spacing Loose
- H5 → font **Body**, 14px, uppercase, letter spacing Loose *(or Caveat 24px, case Default)*
- H6 → font **Body**, 12px, uppercase, letter spacing Loose *(or Caveat 20px, case Default)*

**Primary button:** Background `#C15F3C` · Text `#FBF6EE` · Border `#C15F3C` · thickness 0 · radius 14px · Font **Body** · Case **Uppercase**
**Secondary button:** transparent · Text/Border `#C15F3C` · thickness **1.5px** · radius 14px · Font **Body** · Case Uppercase
**Pills:** radius 40px.

### Known theme bugs to fix as part of this work
These are live and visible on the product page:
1. **Accent palette slot is hot pink `#FF5C9D`** — it leaks into the benefit-pill check icons, link hovers, and badges. Set to honey `#E0A458`. *(This is also the most likely source of stray pink inside the teeinblue block.)*
2. **Buttons → Font is set to Accent**, so "Add to cart" renders in italic serif. Set to **Body**.
3. **Primary button background is mapped to a navy palette entry** — Add to cart renders navy. Map to clay `#C15F3C`.
4. **Headings have Loose line-height and Loose letter-spacing** — Playfair needs Tight for both, or the 44px title sprawls.
5. **H5/H6 are mapped to Caveat at 14px/12px uppercase.** Script has no real uppercase and breaks below ~20px.
6. **Footer muted text is `#C9C1C7`** (cool grey-mauve, reads purple on brown). Use `#9C8B78`.

---

## Page structure

Breadcrumb, then a two-column grid, then three full-width sections.

### Breadcrumb
13px stone, `24px` bottom margin. Current page in `#3B2A20`:
> Home / Grandparents Day / **Being Grandpa Is An Honor Mug**

### Left column — Product media
- **Main image:** 1:1, radius 14px, white, `1px #EADCC8`
- **Prev/next:** 38px circles, `rgba(251,246,238,0.9)`, `1px #EADCC8`, vertically centered, inset 14px, `z-index` above the image
- **Thumbnails:** 5 across, gap 10px, radius 10px, `12px` top margin. Active `2px solid #C15F3C`, inactive `1px solid #EADCC8`

### Right column — Product information

Block order in the Horizon Product information section, top to bottom:

| # | Block | Spec |
|---|---|---|
| 1 | **Title** (h1) | Playfair 700 44px/1.06/-0.015em |
| 2 | **Star ratings** | Honey `#E0A458` stars 15px, `letter-spacing: 1px`, then "4.9 · 214 reviews" 14px stone. `14px` top margin |
| 3 | **Price** | Playfair 700 32px clay + compare-at 17px `#A8977F` strikethrough, gap 12px. Below: "Taxes included. Shipping calculated at checkout." 13px stone |
| 4 | **Benefit pills** | Three pills: Sand Tint `#F4E7D7`, `1px #EADCC8`, radius 999px, padding `8px 15px`, 13px/500. Each opens with a 16px **clay** circle holding a cream ✓ at 9px. Labels: "Personalized free" · "Made to order" · "Secure checkout". **The check circles must be clay — they currently render magenta from the accent bug** |
| 5 | Divider | `1px #EADCC8`, `26px` vertical margin |
| 6 | **Variant picker** | Uppercase 13px/600/`0.06em` stone label per option. Chips: radius 10px, padding `11px 18px`, 14px/500. Selected = `#F7DCD3` bg, `1.5px solid #C15F3C`, `#B0472A` text. Unselected = white, `1.5px solid #EADCC8`, `#3B2A20`. Size chips get `min-width: 52px`, centered. Rows gap 9–10px, `20px` between option groups |
| 7 | **teeinblue app block** | **App-owned — see the scope boundary above.** Occupies roughly: uppercase 13px/600 stone label + a `FREE` marker in clay 11px/700, a full-width input (white, `1.5px #EADCC8`, radius 12px, padding `13px 16px`, 15px text), and a 12.5px stone helper line. `22px` top margin. Match position and footprint; leave internals to the app |
| 8 | **Buy buttons** | Row, gap 12px, `26px` top margin. Quantity stepper: white, `1.5px solid #EADCC8`, radius 14px, 54px tall, 44px −/+ hit areas, value 16px/600 with `min-width: 30px`. Add to cart: `flex: 1`, 54px, clay, cream text, 15px/600, uppercase, `0.08em`, radius 14px |
| 9 | **Shop Pay** | Full width, 50px, `#5A31F4`, white text 15px/600, radius 14px, `10px` top margin. Below, centered: underlined "More payment options" 13px |
| 10 | **Shipping note** | Clay truck icon 17px (`flex-shrink: 0`) + 14px `#5A4C42` text **in a single `<span>`** so it reads as one sentence: "Made to order · ships in 3–5 days · order by **Sep 5** for Grandparents Day". `20px` top margin |
| 11 | **Accordion** | `1px #EADCC8` rules top and between rows, `18px` vertical padding. Headings Playfair 600 17px; stone chevron 15px. Rows: Item details · Shipping & returns · How personalization works |
| 12 | **Description** | 15px/1.65 `#5A4C42`, `max-width: 56ch`, `24px` top margin |

The **order matters**: price and the "personalized free" promise land before the personalizer, so the buyer knows the cost is settled before they invest effort typing a name.

### Related products
`76px` top padding. Centered H2 Playfair 600 32px "You may also like". Four cards, gap 20px:
1:1 image well radius 12px white `1px #EADCC8` · title 14.5px/1.4, `11px` top margin · clay price 15px/600.

### Reviews
`76px` top padding. Centered: H2 Playfair 600 32px "Customer reviews" · honey star row 17px `letter-spacing: 2px` · "4.9 out of 5 · 214 reviews" 14px stone.

Three cards, gap 20px, `30px` top margin: white, `1px #EADCC8`, radius 14px, padding `22px 24px`.
Each: honey stars 14px · quote 15px/1.6 `#5A4C42` · reviewer name **15px/600** · product label **13px stone**.

**Reviewer name and product label must be body font at 15px/13px** — the live theme renders these in Caveat at ~12px, which is illegible. If the reviews carousel is the existing custom `mc-happy-customers` section, apply the fixes in the section below.

---

## Interactions & Behavior

### Add to cart — implement exactly
| State | Spec |
|---|---|
| Hover | Background → `#A64C2C`, `translateY(-1px)`, soften shadow. 150ms ease |
| Active | Background → `#8F3F23`, `scale(0.99)`. 80ms |
| Focus | 2px clay ring, 2px offset. Keep Horizon's default; don't remove it |
| Loading | **Keep the label** and add a spinner, or swap to "Adding…". Never blank the button, and **lock its width** for the whole sequence so nothing shifts. Disable while the request is in flight to prevent double-adds |
| Success | Checkmark + "Added" for ~500ms, then open the cart drawer |
| Total | Click → drawer open in **under 800ms**. Longer and people click twice |

If teeinblue validation fails (missing name, bad upload), surface its error and **do not** enter the loading state.

### Other
- **Variant selection** updates price, media, and availability. Unavailable combinations are **visibly disabled, not hidden** — hiding them makes the picker feel broken.
- **Gallery:** thumbnail click swaps the main image; arrows advance; keyboard arrows work when the gallery has focus. Active thumb border updates.
- **Accordion:** one row at a time is fine; chevron rotates 180°, 200ms. Rows are real `<button>`s with `aria-expanded`.
- **Product card hover** (related): image `scale(1.035)`, 350ms ease; card doesn't move.
- Respect `prefers-reduced-motion`: disable transforms, transitions, smooth scrolling.

## Responsive
Horizon breakpoints: `749px` (mobile), `990px` (tablet).
- Two-column → **stacked at ≤749px, gallery first**.
- Product title 44px → ~30px; price 32px → ~26px.
- Thumbnails 5-across → horizontal scroll strip.
- Benefit pills wrap to two rows; keep all three.
- **Add to cart becomes a sticky bottom bar on mobile** — clay, full width, safe-area inset padding, with the price alongside it.
- Related products 4 → 2 columns. Reviews 3 → 1.
- **Minimum tap target 44px.** The 38px gallery arrows and 32px controls must grow on mobile.
- Give teeinblue room to reflow; don't constrain its width below the container.

## Accessibility
- Text on clay must be cream `#FBF6EE`, not white.
- Stone `#8A7E70` on cream is for secondary text only — never body copy.
- Product title is the page's only `h1`.
- Star rows need `aria-label="4.9 out of 5 stars"` with the glyph row `aria-hidden`.
- Gallery images need real `alt` text (the product name and view, not "image"); the active thumbnail needs `aria-current`.
- Variant chips are radio-group semantics, not links; disabled combinations get `aria-disabled` and a visible disabled style.
- Announce cart updates via a live region.
- Price changes on variant change should be announced, not silent.

## Custom section fixes — `mc-happy-customers`
If the reviews carousel is the existing custom section, it renders reviewer names, product labels, and stars in `--mc-font-accent-*` (Caveat) at 12–13px. In `mc-happy-customers.css`:

- `.mc-happy-customers__header > p` — `color: #C15F3C` (was `#d7195f`), `font-size: 26px`, `letter-spacing: 0` (was `0.14em` on a script face)
- `.mc-happy-customers__header h2` — `letter-spacing: -0.015em` (was `-0.045em`, which crushes Playfair)
- `.mc-happy-customers__stars` — `font-family: inherit`, `font-style: normal`, `color: #E0A458`, 14px
- `.mc-happy-customers__name` — `font-family: var(--mc-font-body-family)`, `font-style: normal`, `font-size: 15px`, `font-weight: 600`, `margin: 12px 0 0`
- `.mc-happy-customers__content a` — body family, `font-style: normal`, 13px, `color: #8A7E70`, no underline; hover clay + underline at 3px offset
- `.mc-happy-customers__card` — add `border: 1px solid #EADCC8` (it has `box-shadow: none` on white, so it vanishes on cream)
- `.mc-happy-customers__media` — `background: #EFE4D4` (was `#eee7ea`, pink-tinted)
- `.mc-happy-customers__placeholder` — `color: #A8977F` (was `#9e8d94`)
- `.mc-happy-customers__content blockquote` — 15px, `margin: 10px 0 0`, clamp to 5 lines (`-webkit-line-clamp: 5`) so cards in a row stay equal height

Schema defaults are off-brand too: `background` `#FFF8F5` → `#FBF6EE`, `text_color` `#151515` → `#3B2A20`. `card_background` `#FFFFFF` is correct.

**General rule:** anywhere `--mc-font-accent-*` lands on small text, switch to `--mc-font-body-family` with `font-style: normal`.

## Assets
Brand assets are in **`assets/logo/`**:
- `symbol-clay.svg`, `symbol-ink.svg`, `symbol-honey.svg`, `symbol-cream.svg` — stitched-heart mark per colorway
- `symbol-solid-clay.svg` — solid heart, no stitch; **use below 24px**
- `wordmark.svg`, `lockup-horizontal.svg`, `lockup-stacked.svg`
- `app-icon.svg`, `app-icon-512.png`, `app-icon-180.png`, `favicon-32.png`, `favicon-16.png`
- `README.md` — colorways, minimum sizes, clear space, usage rules

**The mark:** a heart in dashed running stitch — "made by hand, for you." Clear space equals the mark's height. Minimum 24px; below that use the solid version. Never recolor outside approved colorways.

**Photography does not exist yet.** Images needed here: 1 main product shot + 4 alternate views · 4 related-product shots. Review cards are text-only in this design.

## Files
| File | Contents |
|---|---|
| `MadeJustForYou Website.dc.html` | All three templates; **select "Product"** in the top switcher |
| `MadeJustForYou Product + Cart.dc.html` | Product page with the cart drawer open — reference for post-add behavior |
| `MadeJustForYou Design System.html` | Self-contained design system — identity, palette, type, do/don't |
| `assets/logo/` | Production logo files + usage README |
| `image-slot.js`, `support.js` | Prototype helpers — **do not ship** |

Start with `MadeJustForYou Design System.html` for the visual system, then the Product template.

## The one rule to preserve
Every product is made for a specific person, so the page should keep saying so: personalization is free and stated before the buyer invests effort, the campaign carries a real order-by date, and the name they typed follows the item into the cart. The handwritten voice stays off this page — it belongs to campaigns and packaging, never to a transaction.
