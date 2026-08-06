# MJP-111 — Grandma's Garden Candle Warmer

**Working folder for ad production.** Status overview lives in `products/_registry/` (row MJP-111).

## Product
- **Name:** Grandma's Garden Love Grows Here – Personalized Candle Warmer (49)
- **Live URL:** https://madejustforyou.net/products/grandmas-garden-love-grows-here-personalized-candle-warmer-49?variant=50302396957029
- **Live date:** 2026-08-03
- **Price / AOV:** $49.95 (premium — well above our ~$24 tier)
- **Recipient:** Grandparents
- **Stage:** live · ad_status: none (no ads running yet)

## Clone source (competitor)
- **Cloned from:** Macorner — https://macorner.co/products/grandmas-garden-love-grows-here-personalized-candle-warmer-ma5b329so
- **Score:** 80% Evergreen (Tier 2), from `concept-scores-full.tsv` — one of the most-copied concepts in the set.
- **Competitor ad (LIVE):** Macorner Decor page, video, US-targeted, started 2026-04-13 (~114d), rank #5 & scaling. Ad copy: *"A warm glow, a forever garden 🌸 every light feels like love growing at home."*
- **Competitor ad-library link:** https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=love%20growing%20at%20home&search_type=keyword_exact_phrase&media_type=all

## Source images (`ads/source-images/`)
Product photos live on the Shopify CDN (2048×2048 webp). Save local copies into `ads/source-images/`. For the video models (which need jpg/png), convert on the fly via the weserv proxy: `https://images.weserv.nl/?url=ssl:<cdn-url-without-https>&output=jpg&w=1080`.

| # | type | CDN URL |
|---|---|---|
| 1 | main product | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a7196be83c7d.webp |
| 2 | lifestyle (AI) | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a7196be37d32.webp |
| 3 | lifestyle (AI) | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a7196bd6e15f.webp |
| 4 | lifestyle (AI) | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a6ee723c41af.webp |
| 5 | product detail | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a6ee72a0ca38.webp |
| 6 | lifestyle "Grandma's Garden" | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a6ee73216e21.webp |
| 7 | lifestyle "Grandma's Garden" | https://cdn.shopify.com/s/files/1/0885/3271/3829/files/6a6ee737c8ec1.webp |

> ⚠️ These store images are generic/mockup shots. **Preferred source = the finished product image with the personalized names printed on it** (user to provide) → put it in `ads/source-images/`.

## Clips (`ads/clips/`) & final (`ads/final/`)
- Proof clip (Atlas Kling, image #6, ambient glow, ~$0.30): generated 2026-08-05 — https://atlas-media.oss-us-west-1.aliyuncs.com/assetd-history/v1/a-c38f3b6230a5cd889f9de69e974fe650720dfe709d256bc2249f2840d050d732/u-3e4f4465a585e8d4e9773afb880d4aebf05e67ca413db45b4316bd0bea1689b2/s-45004c3353ccc155f809d9138a743e294032fad85a2d404f8bab1157c6cabf46/e311cffd33794db08bf41be3b31b3f47-99a66893ea6d60fe.mp4
- Production clips → generate with Kie.ai **Kling 3.0 Turbo** (`kling_v3_turbo_video`), save to `ads/clips/`.
- Assembled ad → HyperFrames render, save to `ads/final/`.

## Angle (from the playbook)
Warm memorial-adjacent glow. Hook = names appearing on the lamp; payoff = amber glow bloom + optional grandmother's hand. Headline: "Grandma's Garden – one bloom for every grandchild." See `research/reference/ai-emotional-video-ad-playbook.md` + `image-to-video-prompt-method.md`.
