# Handoff: MadeJustForYou — Home page template (Shopify Horizon)

## Overview
MadeJustForYou is a personalized print-on-demand gift brand (mugs, drinkware, apparel, signs, ornaments, pillows, tote bags, home decor). The core customer is a **gift-giver** buying something meaningful for one specific person.

This handoff covers the **home page template only** (`templates/index.json`). Phase 1 is deliberately lean — a small catalog with one seasonal campaign: **National Grandparents Day, September 13** (order-by date **September 5**). Do not add sections, categories, or products that don't exist yet.

Collection and product templates are specified separately.

## About the Design Files
The file in this bundle is a **design reference authored in HTML** — a prototype showing intended look, structure, and behavior. It is **not production code to copy**.

The target environment is an **existing Shopify store on the Horizon theme** (Online Store 2.0, section/block architecture, Liquid + theme settings, no build step). Reproduce the design in Horizon in this order:

1. **Theme settings first** — colors, typography, button styles, radii. Most of this design is achievable by configuring existing settings. Doing this first prevents writing CSS to override things that are just settings.
2. **Stock Horizon sections second** — every section below maps to a native Horizon section. Prefer configuring a stock section over building a custom one.
3. **Custom Liquid only where noted** — matching the theme's existing `mc-*` convention (`mc-name.liquid` + `mc-name.css` + `mc-name.js`, using `--mc-font-*` custom properties).

Do **not** introduce a JS framework, CSS framework, or build tooling. Do **not** hardcode hex values inside section CSS where a theme setting or `--mc-*` property already exists.

## Fidelity
**High-fidelity.** Colors, typography, spacing, and radii are final and should be matched. One caveat: where Horizon's native section offers a near-equivalent layout, **prefer the native section over pixel-exactness**. The hero was deliberately simplified to a single background image with overlaid text precisely so it maps to Horizon's Image Banner — do not rebuild it as a layered collage.

## Viewing the design
Open `MadeJustForYou Website.dc.html` in any browser. A **template switcher** sits at the top (Home / Collection / Product) — it's a design-tool affordance, **not part of the theme**. Select **Home**; ignore the other two for this handoff.

Every image is a labeled drop-target placeholder (`<image-slot>`). Replace each with a real Shopify image. `image-slot.js` and `support.js` are prototype helpers and **must not ship**.

---

## Design Tokens

### Colors
| Token | Hex | Role |
|---|---|---|
| Cream | `#FBF6EE` | Page background; text on dark surfaces |
| Warm Sand | `#EFE4D4` | Image wells, recessed fills |
| Sand Tint | `#F4E7D7` | Promise-band circles, chips |
| Clay | `#C15F3C` | **Primary accent** — buttons, price, links, active states |
| Clay Hover | `#A64C2C` | Button/link hover |
| Clay Pressed | `#8F3F23` | Button active |
| Honey | `#E0A458` | Secondary accent — stars, accents on dark surfaces |
| Soft Rose | `#D98E85` | Eyebrow text on light backgrounds |
| Rose Tint | `#F7DCD3` | Email-signup panel |
| Warm Ink | `#3B2A20` | Primary text; announcement bar, feature panel, footer |
| Stone | `#8A7E70` | Muted text on light backgrounds |
| Stone Light | `#A8977F` | Strikethrough prices |
| Footer Muted | `#9C8B78` | Muted text on brown |
| Footer Link | `#B7A794` | Footer body/link text |
| Footer Rule | `#55402F` | Divider inside footer |
| Border | `#EADCC8` | **Default border on cream** |
| White | `#FFFFFF` | Elevated surfaces — cards, inputs |

**Layering rule:** cream is the page, **white is elevation**, warm sand is recessed. A white card on a cream page still needs `1px solid #EADCC8`.

### Typography
Three fonts, each with **one fixed job on every surface**.

| Role | Family | Usage |
|---|---|---|
| Heading | **Playfair Display** | Section headings, hero, wordmark, price |
| Body | **DM Sans** | Body copy, nav, buttons, labels, product card text |
| Subheading / Accent | **Caveat** | Short handwritten eyebrows only |

- Design was authored against Hanken Grotesque, which isn't in Shopify's library. **DM Sans** is the approved substitute.
- **The brand name "MadeJustForYou" is always Playfair** — never Caveat. "Just" is italic clay.
- **Caveat is never uppercase, never letter-spaced, never below 20px.**
- Playfair never below weight 600.
- Two weights per family only: DM Sans 400 + 600; Playfair 600 + 700/800; Caveat 700.

**Scale used on this page**
| Element | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| Hero H1 (italic) | 70px | 800 | 0.96 | -0.02em |
| Section heading | 36px | 700 | 1.1 | -0.015em |
| Feature panel heading | 40px | 700 | 1.05 | -0.015em |
| Email signup heading | 32px | 700 | 1.1 | -0.015em |
| Caveat eyebrow | 26–30px | 700 | 1 | 0 |
| Hero body | 18px | 400 | 1.6 | 0 |
| Body | 14.5–16px | 400 | 1.6 | 0 |
| Product card title | 14.5px | 400 | 1.4 | 0 |
| Small / muted | 12.5–13px | 400 | 1.4 | 0 |
| Buttons | 15px | 600 | 1 | 0.08em, uppercase |

Body copy capped at ~60–65 characters — never full container width.

### Spacing, radius, elevation
- Container `max-width: 1300px`, side padding `40px`
- Section rhythm: `66–70px` between sections; `80px` before footer
- Grid gaps: product/recipient grids `20px` (product rows `24px 20px`)
- Radius: **14px** buttons/inputs · **12px** product cards · **16px** recipient cards · **20px** feature and signup panels · **999px** pills, search field
- Borders `1px` default, `1.5px` on interactive controls
- Primary button shadow (optional): `0 14px 26px -14px rgba(193,95,60,0.75)`

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
1. **Accent palette slot is hot pink `#FF5C9D`** — it leaks into link hovers, icon fills, and badge backgrounds theme-wide. Set to honey `#E0A458`.
2. **Buttons → Font is set to Accent**, rendering button labels in italic serif. Set to **Body**.
3. **Primary button background is mapped to a navy palette entry.** Map to clay `#C15F3C`.
4. **Headings have Loose line-height and Loose letter-spacing.** Serif headings need Tight for both.
5. **H5/H6 are mapped to Caveat at 14px/12px uppercase** — script has no real uppercase and breaks below ~20px.
6. **Footer muted text is `#C9C1C7`** (cool grey-mauve, reads purple on brown). Use `#9C8B78`.

---

## Sections, in order

All native Horizon sections. Section 9 (footer) is theme-level, not part of `index.json`.

### 1 · Announcement bar
Warm Ink `#3B2A20`, cream text, centered, 13px, `9px 16px` padding.
> Grandparents Day is Sept 13 · **Order by Sept 5 for guaranteed delivery**

Second clause in honey `#E0A458`.

### 2 · Header
Three-column grid (`1fr auto 1fr`), `18px 40px` padding, bottom border `1px #EADCC8`.
- **Left:** 36px stitched-heart mark + Playfair 600 23px wordmark, gap 11px.
- **Center:** search field — `width:100%; max-width:420px`, white, `1.5px solid #EADCC8`, radius 999px, padding `9px 7px 9px 19px`; 34px clay circular submit button with a magnifier icon. **Must be fluid, not fixed-width** — a hard width collapses the right column and wraps the links.
- **Right:** "Track Order", "Sign In" (14px `#5A4C42`, **`white-space:nowrap`**), cart icon 23px.
- **Nav row** below a `1px #EADCC8` rule, centered, gap 34px, 14px/600: Home · Shop All · **Grandparents Day** (clay, followed by a clay `SEP 13` pill, 9.5px/700) · Contact.

### 3 · Image banner — hero
**Horizon section: Image banner (buttons).** Min-height 520px, full-bleed background image.
- Scrim: `linear-gradient(90deg, rgba(59,42,32,0.62) 0%, rgba(59,42,32,0.34) 46%, rgba(59,42,32,0.04) 78%)` — left-weighted so the text stays legible while the product photo shows through on the right.
- Content left-aligned, `max-width: 560px`, container padding `70px 40px`:
  - Caveat eyebrow 30px `#F3D9CE` — "for the ones who started it all"
  - H1 Playfair **800 italic** 70px/0.96/-0.02em cream — "Gifts for Grandma & Grandpa"
  - Body 18px/1.6 `#F1E4DA`, max-width 460px — "Personalized keepsakes made just for them — Grandparents Day is September 13."
  - Primary button "SHOP NOW" with a right arrow, padding `16px 36px`

### 4 · Multicolumn — promise band
White background, bottom border `1px #EADCC8`, padding `26px 40px`. Three columns, centered.
Each: 42px circle `#F4E7D7` containing a Playfair **italic** numeral in clay, then title 14.5px/600 + subtitle 13px stone.

1. Personalized free — Add names, dates & photos
2. Made to order — Shipped in 3–5 days
3. Wrapped to gift — Every order ships with a tag

### 5 · Collection list — Shop by Recipient
Centered header: Caveat 26px `#D98E85` "find their perfect gift", then H2 Playfair 700 36px "Shop by **Recipient**" (second word clay).

Four cards, 4-column grid, gap 20px, aspect **4:5**, radius 16px:
- Photo fills the card
- Bottom-up scrim `linear-gradient(to top, rgba(59,42,32,0.6) 0%, rgba(59,42,32,0) 46%)`, `pointer-events:none`
- Label bottom-left (18px/16px inset): Playfair 600 24px cream
- Grandparents card carries a clay `SEP 13` pill above the label (10.5px/600, radius 999px)

Order: **Grandparents** · Mom · Dad · Couples

### 6 · Featured collection — New Arrivals
Header row: left = Caveat 26px `#D98E85` "just landed" + H2 Playfair 700 36px "New Arrivals"; right = underlined "Shop all" 14px/600.

Four product cards, grid gap `24px 20px`. Card anatomy:
- 1:1 image well, radius 12px, white, `1px #EADCC8`
- Optional badge top-left (11px inset): clay pill, 11px/600, uppercase, `5px 10px`
- Honey stars 13px + review count 12.5px stone
- Title 14.5px/1.4, **`min-height: 40px`** so rows align
- Clay price 15.5px/600 + strikethrough `#A8977F` 13.5px

### 7 · Image with text — Grandparents Day feature
Two columns `1.05fr 1fr`, radius 20px, `overflow:hidden`, `1px #EADCC8`.
- **Left:** photo, min-height 380px
- **Right:** Warm Ink panel, padding `56px 52px`, vertically centered
  - Caveat 28px honey — "september 13"
  - H2 Playfair 700 40px/1.05 cream — "Make this Grandparents Day unforgettable"
  - Body 15.5px/1.6 `#B7A794`, max-width 400px
  - Two stats separated by a `1px #55402F` vertical rule: **Sep 5** / Order-by date · **3–5 days** / Made & shipped (figures Playfair 26px honey; labels 12.5px `#9C8B78`)
  - Clay button "SHOP THE COLLECTION" with arrow

### 8 · Email signup
Rose Tint `#F7DCD3` panel, radius 20px, padding `48px 52px`, two columns (`1fr auto`).
- Left: Caveat 26px clay "stay inspired" · H2 Playfair 700 32px "Personalized gift ideas, delivered" · body 14.5px `#6B5A50`, max-width 440px
- Right: white pill (`radius 999px`, padding `6px 6px 6px 22px`, min-width 380px) with an email input and a clay Subscribe button

### 9 · Footer
Warm Ink `#3B2A20`. Four columns `1.4fr 1fr 1fr 1fr`, padding `52px 40px 36px`, gap 40px.
- Brand column: 34px honey heart + Playfair 600 20px wordmark ("Just" in honey) · blurb 14px/1.6 `#B7A794` max-width 280px · support email 13px `#9C8B78`
- Link columns: heading cream 14px/600, links 14px `#B7A794`, gap 10px
  - **Shop:** Grandparents Day · New Arrivals · Mugs & Drinkware · Shop All
  - **Help:** Contact Us · Track Order · Shipping · Returns
  - **About:** Our Story · Reviews · Privacy Policy · Terms
- Bottom bar above a `1px #55402F` rule, 13px `#9C8B78`: "© 2026 MadeJustForYou" (left) and "Made just for you, one order at a time." (right)

---

## Interactions & Behavior
- **Product card hover:** image `scale(1.035)`, 350ms ease. The card itself does not move.
- **Recipient card hover:** same image scale; the scrim and label stay fixed.
- **Buttons:** hover `#A64C2C` + `translateY(-1px)`, 150ms; active `#8F3F23` + `scale(0.99)`, 80ms; focus = 2px clay ring at 2px offset (keep Horizon's default).
- **Email signup:** inline validation, success message replaces the field in place — do not navigate away.
- Respect `prefers-reduced-motion`: disable transforms, transitions, smooth scrolling.

## Responsive
Horizon breakpoints: `749px` (mobile), `990px` (tablet).
- Hero: min-height 520px → ~420px mobile; H1 70px → ~40px; scrim shifts to a bottom-up gradient so text stays legible over a centered subject.
- Promise band: 3 columns → 1, stacked, left-aligned.
- Recipient grid: 4 → 2 columns.
- Product grid: 4 → 3 at ≤1200px → 2 at ≤749px. **Keep 2-up on mobile**; 1-up wastes the fold.
- Image-with-text: side-by-side → stacked, image first.
- Email signup: two columns → stacked, input full width.
- Footer: 4 columns → 2 → 1.
- Header: search collapses to an icon at ≤990px; nav becomes a drawer.
- **Minimum tap target 44px** on all mobile controls.

## Accessibility
- Text on clay must be cream `#FBF6EE`, not white.
- Stone `#8A7E70` on cream is for secondary text only — never body copy.
- Every image needs meaningful `alt` text (the product or recipient name, not "image"). Decorative scrims are `pointer-events:none` and are not images.
- Star rows need an accessible label (`aria-label="4.9 out of 5 stars"`) with the glyphs `aria-hidden`.
- The hero heading must be the page's only `h1`.
- Nav "Grandparents Day" pill text ("SEP 13") should be part of the link's accessible name, not a bare decorative span.

## Assets
Brand assets are in **`assets/logo/`**:
- `symbol-clay.svg`, `symbol-ink.svg`, `symbol-honey.svg`, `symbol-cream.svg` — stitched-heart mark per colorway
- `symbol-solid-clay.svg` — solid heart, no stitch; **use below 24px**
- `wordmark.svg`, `lockup-horizontal.svg`, `lockup-stacked.svg`
- `app-icon.svg`, `app-icon-512.png`, `app-icon-180.png`, `favicon-32.png`, `favicon-16.png`
- `README.md` — colorways, minimum sizes, clear space, usage rules

**The mark:** a heart drawn in dashed running stitch — "made by hand, for you." Clear space on all sides equals the height of the mark. Minimum 24px; below that use the solid version. Never recolor outside approved colorways.

**Photography does not exist yet.** Header/footer use the inline SVG mark; every photo is a placeholder.

Images needed for this page: hero background · four recipient photos (Grandparents, Mom, Dad, Couples) · four New Arrivals product shots · one Grandparents Day feature photo.

## Files
| File | Contents |
|---|---|
| `MadeJustForYou Website.dc.html` | All three templates; **select "Home"** in the top switcher |
| `MadeJustForYou Design System.html` | Self-contained design system — identity, palette, type, do/don't |
| `assets/logo/` | Production logo files + usage README |
| `image-slot.js`, `support.js` | Prototype helpers — **do not ship** |

Start with `MadeJustForYou Design System.html` for the visual system, then the Home template.

## The one rule to preserve
Every product is made for a specific person, so the interface should keep saying so: the personalization promise is stated up front, the campaign has a real order-by date, and the handwritten voice appears only in small warm moments — never in the brand name, never as body copy, never below 20px.
