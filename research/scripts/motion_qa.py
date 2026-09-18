#!/usr/bin/env python3
"""motion_qa.py — measure whether a video ad actually MOVES. ffmpeg only, no cv2.

Built 2026-09-18 to test the claim in research/reference/ad-video-director-research.md that our
AI films are dull by construction. It is also the programmatic motion-QA gate specced there.

Usage:
    python3 motion_qa.py clip.mp4 [more.mp4 ...]          # score table
    python3 motion_qa.py --profile clip.mp4               # per-second motion profile
    python3 motion_qa.py --gate clip.mp4                  # exit 1 if it fails the thresholds

Metrics (mean abs luma diff between frames sampled at 8fps, 128px wide, 0-255 scale):
    hook3       mean motion in the 0-3s window   <- THE metric. Meta/Nielsen: ~47% of value is here.
    motion      mean motion over the whole clip
    p90         90th-pct frame diff = peak motion
    flat        motion/p90; ~1.0 = perfectly even (drift), lower = has rhythm
    cuts        hard cuts via ffmpeg scdet (NB: crossfades do NOT register - that is the point)
    cuts/s      cut rate
    static%     share of frame pairs with diff < 1.0 (essentially frozen)

Benchmark, measured (see the research doc §0 for provenance):
    Macorner "car visor" memorial ad, 333 days running, our exact niche:
        17.7s | hook3 18.05 | motion 12.62 | p90 29.81 | 7 cuts (0.40/s) | static 3%
    Our shipped MJ4U-111 film:
        36.6s | hook3  3.59 | motion  8.42 | p90 17.99 | 1 cut  (0.03/s) | static 17%
"""
import subprocess, sys, os, json, statistics

FPS, W = 8, 128
# Gate thresholds, derived from the single benchmark above. Deliberately set BELOW the winner
# (n=1 - do not treat as a distribution) so the gate catches the defect we shipped, not marginal cases.
GATE = dict(hook3=8.0, motion=6.0, cuts_per_s=0.15, static_pct=10)


def _frames(path):
    d = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "json", path],
        capture_output=True).stdout)["streams"][0]
    h = max(2, round(W * d["height"] / d["width"] / 2) * 2)
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={FPS},scale={W}:{h},format=gray",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
    n = W * h
    return [raw[i * n:(i + 1) * n] for i in range(len(raw) // n)]


def _diffs(path):
    fr = _frames(path)
    return [sum(abs(x - y) for x, y in zip(a, b)) / len(a) for a, b in zip(fr, fr[1:])]


def _cuts(path):
    p = subprocess.run(["ffmpeg", "-v", "info", "-i", path, "-vf", "scdet=threshold=10",
                        "-f", "null", "-"], capture_output=True)
    return p.stderr.decode().count("lavfi.scd.time")


def score(path):
    d = _diffs(path)
    if len(d) < 3:
        return None
    dur = len(d) / FPS
    h3 = d[:3 * FPS] or d
    s = sorted(d)
    p90 = s[int(0.9 * (len(s) - 1))]
    mean = sum(d) / len(d)
    return dict(clip=os.path.basename(path), dur=round(dur, 1),
                hook3=round(sum(h3) / len(h3), 2), hook3_peak=round(max(h3), 2),
                motion=round(mean, 2), p90=round(p90, 2),
                flat=round(mean / p90, 2) if p90 else 0.0,
                cuts=_cuts(path), cuts_per_s=round(_cuts(path) / dur, 2) if dur else 0.0,
                static_pct=round(100 * sum(1 for x in d if x < 1.0) / len(d)))


def profile(path):
    d = _diffs(path)
    secs = [sum(d[i * FPS:(i + 1) * FPS]) / len(d[i * FPS:(i + 1) * FPS])
            for i in range(len(d) // FPS + 1) if d[i * FPS:(i + 1) * FPS]]
    print(f"\n{os.path.basename(path)} ({len(d)/FPS:.1f}s)")
    for i, v in enumerate(secs):
        flag = "  <- HOOK" if i < 3 else ""
        print(f"  {i:3}s {v:6.2f} {'#' * int(min(v, 40) / 40 * 46)}{flag}")


def gate(path):
    r = score(path)
    fails = [f"{k}={r[k]} (need {'>=' if k != 'static_pct' else '<='}{v})"
             for k, v in GATE.items()
             if (r[k] < v if k != "static_pct" else r[k] > v)]
    print(f"{r['clip']}: " + ("PASS" if not fails else "FAIL — " + "; ".join(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--profile":
        for p in args[1:]:
            profile(p)
    elif args[0] == "--gate":
        sys.exit(max(gate(p) for p in args[1:]))
    else:
        rows = [r for r in (score(p) for p in args) if r]
        if not rows:
            sys.exit("no clips scored")
        hdr = (f"{'clip':34}{'dur':>5}{'hook3':>7}{'peak':>7}{'motion':>8}"
               f"{'p90':>7}{'flat':>6}{'cuts':>6}{'cuts/s':>8}{'static%':>9}")
        print(hdr); print("-" * len(hdr))
        for r in rows:
            print(f"{r['clip'][:33]:34}{r['dur']:5}{r['hook3']:7}{r['hook3_peak']:7}"
                  f"{r['motion']:8}{r['p90']:7}{r['flat']:6}{r['cuts']:6}"
                  f"{r['cuts_per_s']:8}{r['static_pct']:9}")
        if len(rows) > 1:
            print("-" * len(hdr))
            m = lambda k: round(statistics.mean(r[k] for r in rows), 2)
            print(f"{'MEAN':34}{'':5}{m('hook3'):7}{m('hook3_peak'):7}{m('motion'):8}"
                  f"{m('p90'):7}{m('flat'):6}{'':6}{m('cuts_per_s'):8}{round(m('static_pct')):9}")
