# Short-Form Video Captions — High-Contrast, Always-Readable (verified checklist)

Built from a deep-research pass (24 sources, 119 claims, 25 adversarially verified — 16 confirmed,
9 refuted). Use this for EVERY short-form vertical video (TikTok/Reels/Shorts/FB). The failure it
prevents: **stroke-only or color-only captions that dissolve into busy or light backgrounds.**

## The core rule (verified 3-0)
Readability treatments rank: **solid background box > text outline/stroke > drop shadow > font color alone.**
- **Color-only fails**: text over similar-hue or light areas collapses to **1.2–1.7:1** contrast (measured:
  orange-on-orange 1.7:1; white-on-light-skin 1.2:1) — far below WCAG minimums.
- **WCAG minimums** (SC 1.4.3, AA): **4.5:1** normal text, **3:1** for large/bold (≥24px, or ≥18.7px bold).
- A **solid box guarantees** contrast no matter how the video behind it changes. **BBC "optimum legibility"
  = white text on SOLID black — opacity is NOT allowed.** (A "45% transparent black works on any
  background" claim was REFUTED 0-3. If you use a semi-transparent scrim, it does NOT guarantee contrast.)
- If you drop the box, the outline must be **≥2px and ~10% of font size, drawn OUTSIDE the glyph**
  (a black stroke on 1080×1920 ≈ **8–12px**). Outline beats shadow because it protects the WHOLE
  letter edge; **drop shadow alone is unreliable (fails on light backgrounds) — supplement, not replace.**

## Typography (verified 3-0 on substance; exact sizes refuted)
- **Bold sans only**: Anton, Montserrat Black/Bold, League Spartan, Poppins Bold, Bebas Neue. No thin/script/italic.
  (Anton is condensed → NN/g found condensed ~11% slower to read; fine for punchy captions, avoid for dense text.)
- **Hormozi style** (verified): ultra-heavy face, **ALL CAPS, 3–5 words per line**, **ONE keyword highlighted**
  per line in yellow/green/red, black stroke on all text. Keyword = the noun/verb that carries the meaning.
- **Size**: every specific "% of frame" number was REFUTED in verification — there is no defensible published
  figure. Judgment: big enough to read on a phone at arm's length, ~3–5 words filling most of the safe width.

## Color & contrast
- Highest-contrast pairs: **white on near-black box** (best), black on yellow, white on red/blue.
- Keep to **one accent color per caption** (the highlight); more than 2 reads messy.
- Outline color counts as the *foreground*, glow/halo counts as the *background* (WCAG). Test contrast at the
  LOWEST-contrast region the text passes over.

## Placement & safe zones (1080×1920)
- Platforms overlay their own UI — keep captions OUT of it:
  - **TikTok**: ~130px top dead zone; **~320–350px bottom dead zone** (caption/audio bar); ~120–164px right (icons).
  - Universal cross-platform safe band: **~900×1400 centered** (design text/faces/CTA inside it).
- Practically: park captions in a **lower-third band that ends ABOVE ~350px from the bottom** (≈ bottom 20–22%
  of the frame), and **never over the subject's face** or the product's payoff moment.

## Animation
- Pop/scale-in and word-by-word ("karaoke") reveals are standard; per-word timing ~200–500ms to match speech.
- No verified evidence that animation itself lifts retention — treat as polish, not a lever. Don't let motion hurt legibility (text must be fully readable while on screen).

## Why it matters (verified 3-0)
- **92% of mobile users watch with sound off** (Verizon Media/Publicis Media 2019, n=5,616); **83% desktop.**
- **80% are more likely to finish a video when captions are present**; **41% of videos are meaningless without sound.**
- **80% of Facebook users react negatively to unexpected sound-on autoplay.**
- (Specific uplift %s like "+12% view time / A&W +25%" were REFUTED — do not cite them.)

## The build checklist (apply every time)
1. Text lives on a **fully-opaque dark box** (or, if boxless, a **8–12px black outline drawn outside**). Never color-only.
2. **Anton / Montserrat Black, ALL CAPS, 3–5 words/line.**
3. **One keyword highlighted** in the accent color; one accent per caption.
4. Big, high-contrast (white on near-black).
5. **Lower-third, above the bottom ~350px UI band; never over the face/payoff.**
6. Pop-in animation is fine; readability first.

## Strongest sources
- W3C WCAG 2.2 SC 1.4.3 — https://www.w3.org/TR/WCAG22 (primary)
- WebAIM Contrast — https://webaim.org/articles/contrast (primary)
- BBC Subtitle Guidelines — https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles (primary)
- Ascynd Hormozi captions — https://ascynd.io/en/blog/hormozi-captions (stroke 8–12px, word timing)
- Digital Accessibility Centre — https://digitalaccessibilitycentre.org/blogs/Caption-Characteristics.html (outline spec)
- Verizon/Publicis via 3Play — https://www.3playmedia.com/blog/studies-find-captions-improve-engagement (sound-off stats)

_Refuted / do NOT cite: any specific caption-size % of frame, "45% transparent black works on any bg",
"white-on-black = 21:1 / 4px stroke = 12:1", "+12% view time / A&W +25%", "bold fonts score 31% higher"._
