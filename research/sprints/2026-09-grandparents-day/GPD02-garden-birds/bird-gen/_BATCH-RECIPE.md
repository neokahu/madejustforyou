# Bird-library generation batch (resumable)

Validates the prompts in [`../2B-bird-library.md`](../2B-bird-library.md).

Tool: `nano_banana_pro_image` · resolution **2K** · png · fired 2026-07-31
Pipeline next: for each → `recraft_remove_background` → trim + place on 520×520 (720 for grandma owl)
with feet/nest on bottom-center anchor (x=260, y≈470). Branch → place on full print canvas.

> Results expire 14 days — poll `get_task_status`. Re-fire from the brief if expired.

## Rounds
- **v1** = original prompt (§5a as first written). Robin, small-owl, grandma-owl, branch nailed it.
- **v2** = facing fix ("faces viewer head-on, NOT side profile"). Fixed side-profile drift, but
  "gripping a thin perch" drew a branch under the feet + cardinal/goldfinch got a paper border.
- **v3** = perch/border/tail fix — the **validated winner** (now §5a of the brief).

## Keeper set (use these)
robin=**v1** · small-owl=**v1** · grandma-owl=**v1** · branch=**v1** ·
bluebird=**v3** · cardinal=**v3** · chickadee=**v3** · sparrow=**v3** · dove=**v3** · goldfinch=**v3**

## TaskIds
| # | Asset | v1 taskId | v2 taskId | v3 taskId (keeper for 2–7) |
|---|---|---|---|---|
| 1 | Robin ✅v1 | `b2838110edef4089f253256fd7310a4a` | — | — |
| 2 | Bluebird | `317adae5fa0ea6896c3218955badaa15` | `13d41fd387a7074627396009c2d07f7b` | `52dffe785714a6268b149eb700690002` |
| 3 | Cardinal | `e3d5d06f02867423bae03518fcbd2b4c` | `8b72e85de4bd305df9074a1582b15824` | `5af662f44f85cb9bc7346bc817d544ee` |
| 4 | Chickadee | `1962908ecd1ea48a3f5abe5e019735e5` | `025815bd01517e7edc2a8aa52a25a97e` | `73c024022e19e20bac965bec919bc9d1` |
| 5 | Sparrow | `246ee893dc0f84cb942e65383bac0f70` | `f1fc7ce9cf960984cee69e96d462b330` | `e955dee132e8633a1062825debc32ba4` ⚠️jpeg |
| 6 | Dove | `69fa8b42020b2f53a2574adaa4133629` | `66bd95b2a792e774314e609744579257` | `6ab3df3acdc71148098ba26f63baaeab` |
| 7 | Goldfinch | `6a1e127b3cf2c63c4f041ec37f55acac` | `df5518c64b2debed560b4fb02a967309` | `13f061f47c1c067dc01cdaf05911d03d` |
| 8 | Owl (small) ✅v1 | `9cf98f55fec6829e62f2444cd46ef050` | — | — |
| 9 | Grandma owl ✅v1 | `be10aa1512e090f520ca546784279c86` | — | — |
| 10 | Branch (16:9) ✅v1 | `78edba74189505dc3c3d99ed6a6f3384` | — | — |

⚠️ sparrow v3 returned `.jpeg` (no alpha) — re-run for a transparent PNG before Teeinblue upload.

## Next (post-validation)
1. Re-run sparrow v3 to get a PNG (transparent). 2. Background-remove all 10 keepers →
   `recraft_remove_background`. 3. Trim + place each on 520×520 (720 grandma owl) with feet/nest on
   the bottom-center anchor. 4. Normalize optical scale across the flock. 5. Upload as Teeinblue
   Clipart Category "Birds".
