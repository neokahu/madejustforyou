# Products — the catalog

One folder per product, keyed by ID. **Flat, not category-nested** — category/recipient/season/status live as columns in the registry (the query layer), so products never have to move folders when they're recategorized or change lifecycle stage.

## Layout
```
products/
  _registry/          # the master index — product-tracker.csv + Google Sheet mirror
  <ID>-<slug>/        # one folder per product
    product.md        #   facts, IDs, live URL, competitor ref, status
    build/            #   build pipeline: reference → design → clipart → Teeinblue
    ads/              #   ad-copy.md · source-images/ · clips/ · final/
    listing/          #   store copy, listing images, SEO   [when needed]
```
IDs in use: `MJ4U-###` (from the shortlist/registry) and legacy `NV984-…` (pajama build).

## Rules
- **Lifecycle = status in the registry, never folders.** Don't move a product between backlog/live/retired folders; one folder per product, `stage` lives in `_registry/product-tracker.csv`.
- **Shared assets are NOT here.** Reusable clipart/library → `library/personalizer/`; brand assets → `library/brand/`. A product's `build/` *references* those; it doesn't copy them.
- **Binaries are Drive-synced, not git.** Images (`*.png/jpg/webp…`) and video (`*.mp4/mov…`) are gitignored; only text (`product.md`, `ad-copy.md`, etc.) is committed.
- **A product gets a folder when it enters build or goes live.** Pure backlog stays as a registry row only.

## Where things go
| Thing | Location |
|---|---|
| Product image (source stills) | `<ID>/ads/source-images/` |
| Generated ad clips → final ad | `<ID>/ads/clips/` → `<ID>/ads/final/` |
| Ad copy (caption/headline/hooks) | `<ID>/ads/ad-copy.md` |
| Status of everything | `_registry/` (tracker CSV + Sheet) |
