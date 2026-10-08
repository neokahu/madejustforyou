# Topic — Generation platforms & cost

**Status:** decided 2026-10-08. **TopView DROPPED for video.**

## Current decisions
| Job | Primary | Fallback |
|---|---|---|
| Images | kie.ai | AtlasCloud |
| Video | AtlasCloud | kie.ai |

- **TopView dropped:** ~13× AtlasCloud cost for the identical Seedance 2.0 model; Motion Control broken via MCP (4/4 failed); Unlimited, 3D Shot Composer, Motion Control are GUI-only or non-functional through automation. Consider cancelling the monthly plan.
- **ComfyUI deferred** — can't run our models natively, needs a 24GB+ GPU; revisit only if 8-image references fail.
- Seedance real cost ≈ **$0.98/clip @720p** (was wrongly "$0.09") — sessions/2026-08-08.
- Video models need jpg/png, not webp → weserv proxy (sessions/2026-08-06).

## Operational state (as of 2026-10-08)
| What | Value |
|---|---|
| AtlasCloud balance | ~$48.89 |
| kie.ai balance | untracked — endpoint returns no usable number |
| TopView credits | 28.96 · canvas `4ed6f979c13244c9b8ba102ae2d14d91` |
| TopView free MCP quota | 4 MiniMax-H3 video · 3 Wan 3.0 video · 7 GPT Image 2.5 (1K) |
| Signed URLs | TopView CloudFront URLs expired ~2026-10-04; kie.ai tempfiles expire 14 days |

## Detail
- `research/reference/topview-evaluation-2026.md` (original eval + SUPERSEDING VERDICT — DROP)
- `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` §4a, §4c, §4e
- Kie.ai MCP repo: `~/Desktop/projects/kie-ai-mcp` (sessions/2026-08-06)
- Sessions: [2026-09-25](../../sessions/2026-09-25-topview-evaluated-seedance-method.md) · [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md) · [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
