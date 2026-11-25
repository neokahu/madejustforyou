# K02 generation briefs (role 05, O3)

Tool-agnostic, template §4.1 of `research/reference/video-team/role-research/05-visual-director.md`. Every field filled or "n/a".
No generation tool has been called. Before any spend: turn each brief into a prompt with its adapter (`image-prompt-method.md` for stills, `seedance-prompt-method.md` + `image-to-video-prompt-method.md` for video) and pass the PreToolUse guard (`generation-prompt-guard.py`). Planned tools: Nano Banana Pro Edit (refs, first frames), Seedance 2.0 Fast reference-to-video 720p (video). Labels come from `../refs/REFS-PLAN.md`.

Order of work: refs (B-REF-*) → Gate B → first frames (*-FF) → 07 → video (*-VID) → 07 shot mode.

| Brief | Asset | Output |
|---|---|---|
| B-REF-C1-Jacob … B-REF-C6-Luna | cast reference views | stills |
| B-REF-SCALE-plate | scale-anchored product plate | still |
| B-H61-FF / B-H61-VID | arm A hook | still / video |
| B-H63-FF / B-H63-VID | arm B hook | still / video |
| B-B2-FF / B-B2-VID | stakes | still / video |
| B-B3-FF / B-B3-VID | turn | still / video |
| B-B5a-FF / B-B5a-VID | hug | still / video |
| B-B5b-FF / B-B5b-VID | hang at the tree | still / video |
Beat 4 (STILL+MOVE of the real render) and beat 6 (shared end card) have no brief: nothing is generated.
