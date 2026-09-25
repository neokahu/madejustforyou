#!/usr/bin/env python3
"""
PreToolUse guard for AI image/video generation calls.

Blocks a generation whose prompt violates the documented prompt method, and names
the rule + the doc. Advisory rules were ignored three times on 2026-09-26; this is
the mechanical enforcement.

Docs enforced:
  research/reference/image-to-video-prompt-method.md   (THE ONE RULE, length, camera-first)
  research/reference/seedance-prompt-method.md          (named shots, one move, constraints)
  research/reference/ai-film-studio.md                  (scale anchor, best-of-N, draft first)

Deliberate override: put ACK-<RULE> anywhere in commandId, e.g. ACK-LENGTH.
"""
import json, sys, re

GEN_TOOLS = (
    "submit_topview_canvas_generation_task",
    "seedance_2_video", "bytedance_seedance_video", "kling_video", "kling_v3_turbo_video",
    "veo31_video", "veo3_generate_video", "wan_video", "hailuo_video", "sora_video",
    "atlas_generate_video", "atlas_generate_image", "atlas_quick_generate",
)
DOCS = "research/reference/image-to-video-prompt-method.md · seedance-prompt-method.md · ai-film-studio.md"

CAMERA = r"\b(push[- ]?in|pull[- ]?back|dolly|track(?:ing)?|pan(?:ning)?|tilt(?:ing)?|crane|arc|orbit|zoom|locked[- ]?off|fixed camera|static shot|handheld|wide shot|close[- ]?up|medium shot)\b"

def fail(rule, msg, fix):
    return f"[{rule}] {msg}\n    FIX: {fix}"

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool = data.get("tool_name", "") or ""
    if not any(t in tool for t in GEN_TOOLS):
        sys.exit(0)

    ti = data.get("tool_input", {}) or {}
    prompt = (ti.get("prompt") or "").strip()
    if not prompt:
        sys.exit(0)

    cmd_id   = (ti.get("commandId") or "")
    task     = (ti.get("taskType") or "")
    media    = (ti.get("mediaType") or "")
    params   = ti.get("parameters") or {}
    res      = str(params.get("resolution", ti.get("resolution", "")))
    is_video = media == "video" or "video" in task or "video" in tool

    def acked(rule):
        return f"ACK-{rule}" in cmd_id.upper()

    problems, warnings = [], []
    words = len(prompt.split())

    # --- universal -------------------------------------------------------
    if words > 100 and not acked("LENGTH"):
        problems.append(fail("LENGTH",
            f"prompt is {words} words. The doc: '20-50 words. Tight wins; quality fragments past ~80-100 words.'",
            "cut to the camera move + ONE action + mood. Delete everything the reference image already shows."))

    # THE ONE RULE — re-describing the product
    caps = re.findall(r"\b[A-Z][A-Z'’]{2,}(?:\s+[A-Z][A-Z'’]{2,}){2,}", prompt)
    quoted = re.findall(r"[\"“]([^\"”]{100,})[\"”]", prompt)
    if (caps or quoted) and not acked("REDESCRIBE"):
        ev = (caps[0][:60] if caps else quoted[0][:60])
        problems.append(fail("REDESCRIBE",
            f"the prompt appears to reproduce the product's own printed text/design (e.g. \"{ev}...\"). "
            "THE ONE RULE: 'the image already defines the product, composition, and text. Never re-describe "
            "the product — it is the #1 cause of warping/morphing' and it makes the print outrank your pose.",
            "delete the product description entirely. Refer to it generically ('the blanket', 'the panel')."))

    soft = re.search(r"\b(reproduce|do not reword|re-?letter|original wording|original colours|original colors)\b", prompt, re.I)
    if soft and re.search(r"\b(text|wording|poem|letter|artwork|design|print(?:ed)?|names?)\b", prompt, re.I) and not acked("REDESCRIBE"):
        warnings.append(fail("REDESCRIBE-SOFT",
            "prompt instructs the model to reproduce the artwork/text.",
            "the reference already carries it; such instructions raise the print above the pose/action you actually want."))

    # --- video-specific --------------------------------------------------
    if is_video:
        if not re.search(r"\bShot\s*1\b", prompt) and not acked("SHOTS"):
            problems.append(fail("SHOTS",
                "no named 'Shot 1'. The settled recipe is TWO named shots, each with its own single camera move.",
                "structure as 'Shot 1: <move>. ... Shot 2: <different move>. ...' — this also buys the cuts/s the gate needs."))

        if re.search(r"\b\d+\s*[-–]\s*\d+\s*(s|sec|seconds)\b", prompt) and not acked("TIMECODE"):
            problems.append(fail("TIMECODE",
                "prompt contains timecodes. Official: 'support for precise timing is unstable and may lead to abnormal generation results.'",
                "convert beat timings to named shots. Beat sheets are for us, not the model."))

        m = re.search(r"Shot\s*1\s*:(.*?)(?=Shot\s*2\s*:|$)", prompt, re.S|re.I)
        if m:
            s1 = m.group(1)
            moves = set(x.lower() for x in re.findall(CAMERA, s1, re.I))
            statics = {"locked-off","locked off","fixed camera","static shot"}
            if not moves and not acked("OPENMOVE"):
                problems.append(fail("OPENMOVE",
                    "Shot 1 has no camera move. Verified: a fixed opening shot dropped hook3 from 14.90 to 5.87.",
                    "give Shot 1 its own single move (slow push-in or smooth lateral track)."))
            elif moves and moves.issubset(statics) and not acked("OPENMOVE"):
                problems.append(fail("OPENMOVE",
                    "Shot 1 is static. Verified: a fixed opening dropped hook3 14.90 -> 5.87 with everything else identical.",
                    "give Shot 1 its own move. If this is a mid-film beat not measured by hook3, add ACK-OPENMOVE."))
            framing = {"wide shot","close-up","close up","medium shot"}
            real = moves - statics - framing
            if len(real) > 1 and not acked("ONEMOVE"):
                problems.append(fail("ONEMOVE",
                    f"Shot 1 has {len(real)} camera moves ({', '.join(sorted(real))}). Official: more 'will increase image instability.'",
                    "one move per shot. Move the second to Shot 2."))

        if not re.search(r"(remain[s]? exactly|does not change|do not change|unchanged|stays? (seated|still|the same)|keeps its shape)", prompt, re.I) and not acked("CONSTRAINT"):
            problems.append(fail("CONSTRAINT",
                "no constraint pinning what must not change. 'Constraint words are very important. They can effectively avoid visual flaws, deformities, breakdowns.'",
                "add a constraint naming OUR failure mode (pose, geometry, identity, lettering) — not generic boilerplate."))

    # --- economy ---------------------------------------------------------
    if res in ("4K", "2160") and not acked("RES"):
        warnings.append(fail("RES",
            f"generating at {res} on what may be a first pass.",
            "doc: 'Draft 720p/2K to find the shot cheap, re-run the keeper at full res.'"))

    if not problems and not warnings:
        sys.exit(0)

    lines = []
    if problems:
        lines.append("BLOCKED — this generation prompt violates the documented prompt method.\n")
        lines += problems
    if warnings:
        lines.append("\nWarnings (not blocking):")
        lines += warnings
    lines.append(f"\nDocs: {DOCS}")
    lines.append("READ the relevant doc, rewrite the prompt, resubmit.")
    lines.append("Deliberate exception: add ACK-<RULE> to commandId and say why in your message to the user.")
    reason = "\n".join(lines)

    if problems:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason}}))
    else:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": reason}}))
    sys.exit(0)

if __name__ == "__main__":
    main()
