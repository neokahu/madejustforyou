---
name: video:new
description: Build paid video ads for one test cell with the video team (hook → script → visuals → edit → QA), gate by gate
argument-hint: "[test-id / plan cell, e.g. suncatcher-phase2 C1]"
---

<objective>
Run the video-team pipeline for one plan cell and deliver ads that pass QA: 2+ hook arms per concept, a 9:16 and a 4:5 cut each.
You are the PRODUCER (role 00). You orchestrate, hold the budget, enforce the gates and take structural questions
to the user. You do not write hooks, scripts or briefs yourself; the role agents do.
</objective>

<context>
Cell: $ARGUMENTS
Team method: @research/reference/video-team/README.md
Test authority: the plan page section for this product (memory: follow-plan-page-scripts-via-agent)
</context>

<process>
0. **Brief + budget.** Read the plan cell. Confirm the arms, length, CTA and budget cap with the user. Set up `marketing/facebook-ads/<test-id>/<cell>/`.
   Compile and LOCK `marketing/facebook-ads/<test-id>/CRITERIA.md` from every relevant doc (template: suncatcher-phase1/EDIT-CRITERIA.md).
   Collect: the product truth pack + fact sheet, cast sheet, music + licence evidence, the open user rulings (AI disclosure).
1. **vt-01-hook-ideator** → `hooks/01-candidates.md`.
2. **vt-02-hook-critic** × 3 independent runs. Strip `rationale` and author, and shuffle the card order per run. Use different models where available, or include the user as one judge. Take the median, flag spreads ≥2, apply the calibration rule.
3. **vt-03-hook-selector** (a fresh agent; did not write the hooks) → `hooks/03-selection.md` + pre-registration lines.
4. **vt-04-script-editor** → `script.md`, then `/llm-council` per script (craft only, no restructuring).
   **GATE A: the user approves hooks + script.**
5. **vt-05-visual-director** → shot list + reference sheet.
   **GATE B: vt-07-qa (shot mode) + the user approve the references. No scene asset before this.**
   Then briefs → adapter + prompt guard → drafts → **GATE C: vt-07-qa shot mode accepts each shot** (reshoot only the rejects).
6. **vt-06-editor** → control first, then variants, both formats, recipe, self-check, media backup, log row.
7. **vt-07-qa** (final mode, a fresh agent) → **GATE D: PASS = zero S1/S2.** On FAIL, route each defect to its fix owner and re-check.
8. **Upload prep.** Asset customization by ratio; Advantage+ creative enhancements that alter the video OFF for test cells. Record the settings.
9. **Close.** Append the hooks to `_ledgers/hook-ledger.csv` and the shipped shots to `_ledgers/scene-ledger.csv`, update the product tracker + Sheet, commit the docs (never media).
</process>

<rules>
- Never let one agent make and grade the same work (01≠02/03, 05≠07, 06≠07).
- Structural changes (concepts, arms, length, CTA, offer) → ask the user. Craft fixes inside a cell are fine.
- Tool-agnostic: role outputs never name a generator. Tool choice + prompt craft = adapter docs + the prompt guard.
</rules>
