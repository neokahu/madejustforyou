# Live Products — per-product work folders

One folder per **live** product (things actually on the store). This is the *working* space for ad production; the `product-tracker/` CSV is the status overview. Cross-reference by `product_id` (`MJP-###`).

## Folder convention
```
live-products/
  MJP-###-<slug>/
    README.md         <- live URL, IDs, competitor ref, ad-library links, status, notes
    ad-copy.md        <- ad text: caption/body, headline, CTA, hooks, on-screen text
    source-images/    <- the product photos (source stills for image-to-video)
    clips/            <- generated AI video clips (raw, per shot)
    final/            <- assembled final ad videos
    prompts.md        <- the i2v prompts + which image → which clip (created when we generate)
```

## Rules
- **Naming:** `MJP-###-<short-slug>` — same ID as the tracker row.
- **Binaries are Drive-synced, NOT git:** images (`*.png/jpg/webp…`) and video (`*.mp4/mov…`) are gitignored. Only the `README.md` / `prompts.md` (text) are committed. Keep the actual files here locally; they sync to Google Drive (`My Drive/MadeJustForYou-assets/`).
- **Where the image goes:** drop the product image(s) with the printed names into `source-images/`.
- **A product gets a folder here only once it's live** (or actively in ad production). Backlog stays in the tracker.
