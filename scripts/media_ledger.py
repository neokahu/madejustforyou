#!/usr/bin/env python3
"""Media cost ledger: one row per generated asset (image / video / audio), with the provider's
charged price and the file's technical specs, so the full cost of an ad can be summed later.

Ledger: marketing/facebook-ads/media-cost-ledger.csv (append-only; one row per prediction).

  media_ledger.py log  <prediction_id> <local_file> [--purpose P] [--notes N] [--status kept|rejected|test]
  media_ledger.py sum  [--by test_id|concept|product_id|model|purpose] [--test MJ4U-133-C0]
  media_ledger.py set  <prediction_id> status=<kept|rejected|test> [notes=...]
  media_ledger.py refresh                          # re-read price for rows logged before Atlas billed them
  media_ledger.py reconcile [--since 2026-11-24]   # pull AtlasCloud job history: log missing jobs
                                                    # (matched to local files by content hash) and fill
                                                    # request params / prompt / timing on every row

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
        "latency_s", "completed_at", "elapsed_s", "width", "height", "duration_s", "fps", "file_bytes", "output_file",
        "status", "notes", "n_ref_images", "request_params", "prompt"]


def key():
    k = os.environ.get("ATLASCLOUD_API_KEY")
    if k:
        return k
    for line in open(os.path.expanduser("~/.global-keys.env")):
        if line.startswith("ATLASCLOUD_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"\'')
    sys.exit("ATLASCLOUD_API_KEY not found")


def curl(url, auth=True, binary=False, timeout=90):
    """HTTPS via curl: Python's ssl handshake to AtlasCloud times out on this machine."""
    cmd = ["curl", "-sS", "--max-time", str(timeout), "-A", "curl/8.7.1", url]
    if auth:
        cmd[1:1] = ["-H", f"Authorization: Bearer {key()}"]
    out = subprocess.run(cmd, capture_output=True, check=True).stdout
    return out if binary else json.loads(out)


def prediction(pid):
    return curl(f"https://api.atlascloud.ai/api/v1/model/prediction/{pid}")["data"]


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


def history(since_epoch):
    out, page = [], 1
    while True:
        items = curl(f"https://api.atlascloud.ai/api/v1/model/history?pageNo={page}&pageSize=100")["data"]["items"]
        # The API ignores paging (2026-11-25: always returns the newest 20), so stop on a repeat page.
        if not items or (out and items[0]["ID"] == out[0]["ID"]) or any(i["ID"] in {o["ID"] for o in out} for i in items[:1]):
            break
        for it in items:
            if int(it["createdAt"]) < since_epoch:
                return out
            out.append(it)
        page += 1
    return out


def lit(x):
    if isinstance(x, (dict, list)):
        return x
    try:
        return json.loads(x)
    except Exception:
        import ast
        try:
            return ast.literal_eval(x)
        except Exception:
            return {}


def job_fields(it):
    body = lit(it.get("requestBody") or "{}")
    refs = 0
    for k in ("images", "reference_images", "image", "first_frame_image", "reference_videos"):
        v = body.get(k)
        refs += len(v) if isinstance(v, list) else (1 if v else 0)
    params = {k: v for k, v in body.items()
              if k not in ("prompt", "images", "reference_images", "image", "first_frame_image",
                           "reference_videos", "reference_audios", "model")}
    bill = lit(it.get("billing") or "{}")
    ts = lambda ms: datetime.datetime.fromtimestamp(int(ms) / 1000, datetime.timezone.utc).isoformat(timespec="seconds")
    return {"model": it.get("model", ""), "prompt": body.get("prompt", ""),
            "request_params": json.dumps(params, separators=(",", ":")), "n_ref_images": refs,
            "price_usd": bill.get("amount", ""),
            "created_at": ts(int(it["createdAt"]) * 1000),
            "completed_at": ts(it["completedAtMs"]) if it.get("completedAtMs") else "",
            "elapsed_s": round(int(it["elapsedMs"]) / 1000, 1) if it.get("elapsedMs") else "",
            "outputs": lit(it.get("result") or "{}").get("outputs", [])}


def local_files(since_epoch):
    """Map file size -> [paths] for recent media under products/ (cheap; hash only on size match)."""
    idx = {}
    for dp, _, fs in os.walk(os.path.join(ROOT, "products")):
        for f in fs:
            if not f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".mp4", ".mov")):
                continue
            fp = os.path.join(dp, f)
            try:
                st = os.stat(fp)
            except OSError:
                continue
            if st.st_mtime >= since_epoch - 86400:
                idx.setdefault(st.st_size, []).append(fp)
    return idx


def match_local(data, idx):
    import hashlib
    cands = idx.get(len(data), [])
    if not cands:
        return ""
    h = hashlib.sha1(data).hexdigest()
    for fp in cands:
        if hashlib.sha1(open(fp, "rb").read()).hexdigest() == h:
            return fp
    return ""


def cmd_reconcile(since):
    import hashlib
    se = int(datetime.datetime.fromisoformat(since).replace(tzinfo=datetime.timezone.utc).timestamp())
    jobs = history(se)
    rows = read()
    byid = {r["prediction_id"]: r for r in rows}
    idx = None
    added = filled = 0
    for it in jobs:
        if it.get("status") != "completed":
            continue
        f = job_fields(it)
        outs = f.pop("outputs")
        r = byid.get(it["ID"])
        if r:
            for k, v in f.items():
                if not r.get(k) and v != "":
                    r[k] = v
            filled += 1
            continue
        if idx is None:
            idx = local_files(se)
        path = ""
        if outs:
            try:
                data = curl(outs[0], auth=False, binary=True, timeout=120)
                path = match_local(data, idx)
            except Exception:
                pass
        row = {c: "" for c in COLS}
        if path:
            row.update(infer(path)); row.update(probe(path))
            row["asset_name"] = os.path.splitext(os.path.basename(path))[0]
        else:
            row["notes"] = "reconciled from AtlasCloud history; no local file matched (unsaved/renamed/re-encoded)"
        row.update(f)
        row.update({"logged_at": datetime.datetime.now().isoformat(timespec="seconds"),
                    "provider": "atlascloud", "prediction_id": it["ID"], "charge_status": "charged"})
        rows.append(row); byid[it["ID"]] = row; added += 1
    write(rows)
    print(f"reconcile: {len(jobs)} jobs since {since}; added {added}, filled {filled}")


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
    elif a[0] == "refresh":
        rows = read(); n = 0
        for r in rows:
            if r["prediction_id"] and not r["price_usd"]:
                try:
                    d = prediction(r["prediction_id"])
                    if d.get("price"):
                        r["price_usd"] = d["price"]; r["charge_status"] = d.get("charge_status", ""); n += 1
                except Exception:
                    pass
        write(rows); print(f"refresh: filled {n} blank prices")
    elif a[0] == "reconcile":
        cmd_reconcile(opts(a[1:]).get("since", "2026-11-24"))
    elif a[0] == "sum":
        o = opts(a[1:])
        cmd_sum(o.get("by", "test_id"), o.get("test", ""))
    else:
        sys.exit(__doc__)
