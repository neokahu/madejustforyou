# Topic — Teeinblue personalizer + NV984 pajama build

**Status:** pajama base PSD built at real size; Teeinblue campaign not built; character anchors unresolved.

## Decisions / facts
- Teeinblue = personalizer; Conditional Logic + Clipart handles variable counts. Verified mechanics in `research/reference/teeinblue-assets-guide.md`.
- Text layer cannot populate from an Additional Option → Route A (conditional text layers) vs Route B (clipart word-images) — **open**.
- Pajama print master = **6335×7057 @300 DPI**, cut-and-sew leg panels.
- Photoshop MCP `execute_script`: no `#target`, explicit `return`.
- Binaries/PSDs live on firebits Drive `gdrive:madejustforyou` (rclone), not git.

## Open items
- Character-body anchors (regenerate from one template recommended); Tile B (11–15); background hex values; build the Teeinblue campaign.

## Detail
- `products/NV984-pajama/build/` · `library/personalizer/ASSET-SYSTEM.md` · SOPs in `sop-docs` (TASK-MKT-007…013, WF-MKT-005)
- Sessions: [2026-07-20](../../sessions/2026-07-20-pajama-clone-handoff.md) · [2026-07-26](../../sessions/2026-07-26-teeinblue-asset-system-handoff.md) · [2026-07-28](../../sessions/2026-07-28-winninghunter-ad-scoring-handoff.md)
