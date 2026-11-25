#!/usr/bin/env python3
"""Media cost ledger: one row per generated asset (image / video / audio), with the provider's
charged price and the file's technical specs, so the full cost of an ad can be summed later.

Ledger: marketing/facebook-ads/media-cost-ledger.csv (append-only; one row per prediction).

  media_ledger.py log  <prediction_id> <local_file> [--purpose P] [--notes N] [--status kept|rejected|test]
  media_ledger.py sum  [--by test_id|concept|product_id|model|purpose] [--test MJ4U-133-C0]
  media_ledger.py set  <prediction_id> status=<kept|rejected|test> [notes=...]

`log` reads price, model, timing and charge status from the AtlasCloud prediction API and the
size/duration/fps/bytes from the file (ffprobe). product_id, test_id and concept are inferred
from the path (products/<slug>/ads/<test>/<K..>/...) when present. scripts/atlas_poll.sh calls
`log` automatically after each download.
"""
import csv, json, os, re, subprocess, sys, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "marketing", "facebook-ads", "media-cost-ledger.csv")
COLS = ["logged_at", "created_at", "product_id", "test_id", "concept", "asset_name", "purpose",
        "media_type", "provider", "model", "prediction_id", "charge_status", "price_usd",
        "latency_s", "width", "height", "duration_s", "fps", "file_bytes", "output_file",
        "status", "notes"]


def key():
    k = os.environ.get("ATLASCLOUD_API_KEY")
    if k:
        return k
    for line in open(os.path.expanduser("~/.global-keys.env")):
        if line.startswith("ATLASCLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"\'')
    sys.exit("ATLASCLOUD_API_KEY not found")


def prediction(pid):
    req = urllib.request.Request(f"https://api.atlascloud.ai/api/v1/model/prediction/{pid}",
                                 headers={"Authorization": f"Bearer {key()}", "User-Agent": "curl/8.7.1", "Accept": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=30))["data"]


def probe(path):
    out = {"width": "", "height": "", "duration_s": "", "fps": "", "file_bytes": "", "media_type": ""}
    if not os.path.exists(path):
        return out
    out["file_bytes"] = os.path.getsize(path)
    try:
        j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                       "stream=codec_type,width,height,r_frame_rate:format=duration",
                                       "-of", "json", path], capture_output=True, text=True).stdout)
        v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), {})
        out["width"], out["height"] = v.get("width", ""), v.get("height", "")
        dur = float(j.get("format", {}).get("duration") or 0)
        num, _, den = (v.get("r_frame_rate") or "0/1").partition("/")
        fps = float(num) / float(den or 1) if den and float(den) else 0
        is_video = dur > 0.5 and fps > 1
        out["media_type"] = "video" if is_video else ("image" if v else "audio")
        out["duration_s"] = round(dur, 2) if is_video or not v else ""
        out["fps"] = round(fps, 2) if is_video else ""
    except Exception:
        pass
    return out


def infer(path):
    rel = os.path.relpath(os.path.abspath(path), ROOT)
    m = re.search(r"products/([^/]+)/", rel)
    slug = m.group(1) if m else ""
    pid = re.match(r"(MJ4U-\d+)", slug)
    test = re.search(r"/(MJ4U-\d+-[A-Z]\d+)/", rel)
    conc = re.search(r"/(K\d+)/", rel) or re.search(r"\b(K\d+)[-_]", os.path.basename(rel), re.I)
    parts = rel.split("/")
    purpose = next((p for p in ("refs", "turntable", "stills", "first-frames", "clips", "plates",
                                "renders", "music", "tests") if p in parts), "")
    return {"product_id": pid.group(1) if pid else "", "test_id": test.group(1) if test else "",
            "concept": conc.group(1).upper() if conc else "", "purpose": purpose, "output_file": rel}


def read():
    if not os.path.exists(LEDGER):
        return []
    return list(csv.DictReader(open(LEDGER)))


def write(rows):
    with open(LEDGER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)


def cmd_log(pid, path, opts):
    rows = read()
    if any(r["prediction_id"] == pid for r in rows):
        print(f"ledger: {pid} already logged")
        return
    d = prediction(pid)
    row = {c: "" for c in COLS}
    row.update(infer(path))
    row.update(probe(path))
    created, done = d.get("created_at", ""), d.get("completed_at", "")
    row.update({
        "logged_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "created_at": created, "asset_name": os.path.splitext(os.path.basename(path))[0],
        "provider": "atlascloud", "model": d.get("model", ""), "prediction_id": pid,
        "charge_status": d.get("charge_status", ""), "price_usd": d.get("price", ""),
        "latency_s": round(d["latency_ms"] / 1000, 1) if d.get("latency_ms") else "",
        "status": opts.get("status", ""), "notes": opts.get("notes", ""),
    })
    if opts.get("purpose"):
        row["purpose"] = opts["purpose"]
    rows.append(row)
    write(rows)
    print(f"ledger: +{row['asset_name']} {row['model']} ${row['price_usd']} "
          f"{row['width']}x{row['height']} {row['duration_s']}")


def cmd_set(pid, kv):
    rows = read()
    for r in rows:
        if r["prediction_id"] == pid:
            for k, v in kv.items():
                r[k] = v
    write(rows)


def cmd_sum(by, test):
    rows = [r for r in read() if not test or r["test_id"] == test]
    tot = {}
    for r in rows:
        k = r.get(by) or "(none)"
        n, c = tot.get(k, (0, 0.0))
        tot[k] = (n + 1, c + float(r["price_usd"] or 0))
    for k, (n, c) in sorted(tot.items()):
        print(f"{k:40s} {n:4d} assets  ${c:8.2f}")
    print(f"{'TOTAL':40s} {sum(n for n, _ in tot.values()):4d} assets  "
          f"${sum(c for _, c in tot.values()):8.2f}")


def opts(args):
    o = {}
    it = iter(args)
    for a in it:
        if a.startswith("--"):
            o[a[2:]] = next(it, "")
    return o


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "log" and len(a) >= 3:
        cmd_log(a[1], a[2], opts(a[3:]))
    elif a[0] == "set" and len(a) >= 3:
        cmd_set(a[1], dict(x.split("=", 1) for x in a[2:]))
    elif a[0] == "sum":
        o = opts(a[1:])
        cmd_sum(o.get("by", "test_id"), o.get("test", ""))
    else:
        sys.exit(__doc__)
