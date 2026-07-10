# Session Handoffs

Chronological log of working sessions. **One file per session — never overwrite.**

## Convention
- **File name:** `YYYY-MM-DD-session-NN.md` (NN = 2-digit sequence if multiple sessions in a day).
- **Inheritance:** each new handoff **carries forward** the still-true state from the previous one,
  then records what changed this session. So the **latest file is always self-contained and is the
  source of truth** — you never have to read the whole history to get current.
- Older files remain as **historical snapshots** (what was true / decided at that time).

## How to write the next handoff (at session end)
1. Open the most recent handoff here.
2. Create a new file `YYYY-MM-DD-session-NN.md`.
3. Set **`Inherits from:`** to the previous file name.
4. **Carry forward** the sections that are still true (project overview, decisions/insights that
   still hold, open items not yet done). Trim what's now obsolete.
5. Add a **"New this session"** section (what changed/was built) and an updated
   **"Open items / next steps"** list.
6. Commit + push.

## Index (newest first)
- [`2026-07-10-session-01.md`](2026-07-10-session-01.md) — built the design-idea research
  playbook + ran the Grandparents Day 2026 sprint end-to-end; chose Teeinblue personalizer.
