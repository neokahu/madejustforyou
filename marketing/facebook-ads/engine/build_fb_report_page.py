#!/usr/bin/env python3
"""Pull full per-ad Facebook performance for the LPV + ATC campaigns and render a
detailed child report page (facebook.html) next to the main report/index.html."""
import json, html
from pathlib import Path
from upload_draft import Uploader, load_env, ENV_PATH, REPO

OUT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/report/facebook.html"
CAMPAIGNS = [
    ("120251953447920556", "LPV / Traffic", "Landing Page View"),
    ("120251963479950556", "ATC / Sales",   "Add to Cart"),
]
ATC = ("offsite_conversion.fb_pixel_add_to_cart", "onsite_web_add_to_cart", "add_to_cart")
IC  = ("offsite_conversion.fb_pixel_initiate_checkout", "onsite_web_initiate_checkout", "initiate_checkout")
PUR = ("offsite_conversion.fb_pixel_purchase", "onsite_web_purchase", "purchase")
LPV = ("landing_page_view",)


def pick(lst, types):
    if not isinstance(lst, list): return 0.0
    for t in types:
        for a in lst:
            if a.get("action_type") == t:
                try: return float(a.get("value", 0))
                except Exception: return 0.0
    return 0.0

def v1(row, key):
    a = row.get(key)
    if isinstance(a, list) and a:
        try: return float(a[0].get("value", 0))
        except Exception: return 0.0
    return 0.0


def pull(up, cid):
    core = ("ad_id,ad_name,adset_name,spend,impressions,reach,frequency,cpm,cpc,ctr,"
            "inline_link_clicks,inline_link_click_ctr,actions,cost_per_action_type,action_values")
    rows = up.get(f"{cid}/insights", {"fields": core, "level": "ad", "date_preset": "maximum"}).get("data", [])
    # video metrics (separate request; degrade gracefully if a field is unsupported)
    vids = {}
    # NB: video_3_sec_watched_actions is INVALID on v26 (Meta replaced 3-sec plays with ThruPlay).
    vfields = ("ad_id,video_play_actions,video_p50_watched_actions,"
               "video_p100_watched_actions,video_thruplay_watched_actions,video_avg_time_watched_actions")
    try:
        for d in up.get(f"{cid}/insights", {"fields": vfields, "level": "ad", "date_preset": "maximum"}).get("data", []):
            vids[d.get("ad_id")] = d
    except Exception:
        vids = {}
    # status per ad
    status = {}
    try:
        for a in up.get(f"{cid}/ads", {"fields": "id,effective_status", "limit": "200"}).get("data", []):
            status[a["id"]] = a.get("effective_status", "")
    except Exception:
        pass
    out = []
    for d in rows:
        aid = d.get("ad_id"); vd = vids.get(aid, {})
        imp = float(d.get("impressions", 0)) or 0
        plays = v1(vd, "video_play_actions")
        p50 = v1(vd, "video_p50_watched_actions")
        p100 = v1(vd, "video_p100_watched_actions")
        thru = v1(vd, "video_thruplay_watched_actions")
        atc = pick(d.get("actions"), ATC)
        rev = pick(d.get("action_values"), PUR)
        spend = float(d.get("spend", 0))
        out.append({
            "ad": d.get("ad_name", ""), "adset": d.get("adset_name", ""),
            "status": status.get(aid, ""),
            "spend": spend, "impr": imp, "reach": float(d.get("reach", 0)),
            "freq": float(d.get("frequency", 0)), "cpm": float(d.get("cpm", 0)),
            "clicks": float(d.get("inline_link_clicks", 0)),
            "ctr": float(d.get("inline_link_click_ctr", 0)), "cpc": float(d.get("cpc", 0)),
            "plays": plays, "thru": thru, "thrurate": (thru / imp * 100 if imp else 0),
            "hold50": (p50 / imp * 100 if imp else 0), "hold100": (p100 / imp * 100 if imp else 0),
            "_p50": p50, "_p100": p100, "avgwatch": v1(vd, "video_avg_time_watched_actions"),
            "lpv": pick(d.get("actions"), LPV),
            "atc": atc, "cpatc": (spend / atc if atc else 0),
            "ic": pick(d.get("actions"), IC), "pur": pick(d.get("actions"), PUR),
            "rev": rev, "roas": (rev / spend if spend else 0),
        })
    return out


CSS = """
*{box-sizing:border-box}body{margin:0;background:#f5f6f8;color:#161a1e;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.5}
.wrap{max-width:1240px;margin:0 auto;padding:24px 18px 60px}
a.back{display:inline-block;margin-bottom:12px;color:#2563eb;text-decoration:none;font-size:14px}
a.back:hover{text-decoration:underline}
h1{font-size:22px;margin:0 0 4px}.sub{color:#667085;font-size:13.5px;margin-bottom:16px}
h2{font-size:16px;margin:26px 0 8px}
.scroll{overflow-x:auto;border:1px solid #e6e8ec;border-radius:12px;background:#fff}
table{border-collapse:collapse;font-size:13px;white-space:nowrap;min-width:100%}
th,td{padding:8px 12px;border-bottom:1px solid #eef1f5;text-align:right;font-variant-numeric:tabular-nums}
th{position:sticky;top:0;background:#f0f2f5;color:#475467;font-size:11.5px;text-transform:uppercase;letter-spacing:.3px;font-weight:600}
th.l,td.l{text-align:left}
tr td.l:first-child{font-weight:600}
tbody tr:hover{background:#f9fafb}
tr.total td{border-top:2px solid #cbd2da;font-weight:700;background:#fafbfc}
.badge{font-size:11px;padding:2px 7px;border-radius:20px}
.on{background:#dcfce7;color:#15803d}.off{background:#f1f3f5;color:#667085}
.win{color:#15803d;font-weight:600}.zero{color:#b91c1c}
.note{color:#667085;font-size:12.5px;margin-top:8px}
"""

COLS = [
    ("ad", "Quảng cáo (creative)", "l"), ("status", "Trạng thái", "l"),
    ("spend", "Chi tiêu", "n$"), ("impr", "Hiển thị", "n"), ("reach", "Reach", "n"),
    ("freq", "Tần suất", "n2"), ("cpm", "CPM", "n$"),
    ("plays", "Video plays", "n"), ("thru", "ThruPlay", "n"), ("thrurate", "ThruPlay %", "n%"),
    ("hold50", "Xem 50%", "n%"), ("hold100", "Xem 100%", "n%"), ("avgwatch", "TG xem TB(s)", "n"),
    ("clicks", "Link clicks", "n"), ("ctr", "CTR link", "n%"), ("cpc", "CPC link", "n$"),
    ("lpv", "Landing Views", "n"),
    ("atc", "Add to Cart", "n"), ("cpatc", "Chi phí/ATC", "n$"),
    ("ic", "Init. Checkout", "n"), ("pur", "Purchase", "n"),
    ("rev", "Doanh thu", "n$"), ("roas", "ROAS", "n2"),
]


def fmt(key, val, kind):
    if kind == "l":
        if key == "status":
            on = str(val).upper() == "ACTIVE"
            lab = "Đang chạy" if on else (val or "—").replace("_", " ").title()
            return f'<span class="badge {"on" if on else "off"}">{html.escape(lab)}</span>'
        return html.escape(str(val))
    if kind == "n":   return f"{val:,.0f}"
    if kind == "n2":  return f"{val:,.2f}"
    if kind == "n$":  return f"${val:,.2f}"
    if kind == "n%":  return f"{val:,.2f}%"
    return html.escape(str(val))


def cell(r, key, kind, css):
    val = r.get(key, 0)
    cls = "l" if kind == "l" else ""
    extra = ""
    if key in ("pur",) and (val or 0) == 0: extra = " zero"
    if key == "atc" and (val or 0) > 0: extra = " win"
    return f'<td class="{cls}{extra}">{fmt(key, val, kind)}</td>'


def render(data):
    parts = [f"<!doctype html><html lang='vi'><head><meta charset='utf-8'>",
             "<meta name='viewport' content='width=device-width, initial-scale=1'>",
             "<title>FB Ads — Chi tiết đầy đủ (MJ4U-111)</title><style>", CSS, "</style></head><body><div class='wrap'>",
             "<a class='back' href='./'>← Quay lại báo cáo tổng quan</a>",
             "<h1>Facebook Ads — Bảng hiệu suất đầy đủ</h1>",
             "<div class='sub'>MJ4U-111 “Grandma's Garden” · Cấp Quảng cáo (ad-level) · date_preset = maximum · Nguồn: Meta Ads Manager API</div>"]
    thead = "<tr>" + "".join(f"<th class='{'l' if k[2]=='l' else ''}'>{html.escape(k[1])}</th>" for k in COLS) + "</tr>"
    for cid, label, obj in data:
        rows = data[(cid, label, obj)]
        parts.append(f"<h2>{html.escape(label)} — tối ưu {html.escape(obj)}</h2>")
        parts.append("<div class='scroll'><table><thead>" + thead + "</thead><tbody>")
        tot = {k: 0.0 for k, _, _ in COLS if k not in ("ad", "status")}
        tot["_p50"] = 0.0; tot["_p100"] = 0.0
        for r in rows:
            parts.append("<tr>" + "".join(cell(r, k, ki, c) for (k, _, ki), c in [(col, col) for col in COLS]) + "</tr>")
            for k in tot: tot[k] += r.get(k, 0) or 0
        # weighted/derived totals
        tot["cpm"] = (tot["spend"] / tot["impr"] * 1000) if tot["impr"] else 0
        tot["ctr"] = (tot["clicks"] / tot["impr"] * 100) if tot["impr"] else 0
        tot["cpc"] = (tot["spend"] / tot["clicks"]) if tot["clicks"] else 0
        tot["cpatc"] = (tot["spend"] / tot["atc"]) if tot["atc"] else 0
        tot["freq"] = (tot["impr"] / tot["reach"]) if tot["reach"] else 0
        tot["thrurate"] = (tot["thru"] / tot["impr"] * 100) if tot["impr"] else 0
        tot["hold50"] = (tot["_p50"] / tot["impr"] * 100) if tot["impr"] else 0
        tot["hold100"] = (tot["_p100"] / tot["impr"] * 100) if tot["impr"] else 0
        tot["avgwatch"] = (tot["avgwatch"] / len(rows)) if rows else 0
        tot["roas"] = (tot["rev"] / tot["spend"]) if tot["spend"] else 0
        trow = ["<tr class='total'>"]
        for (k, _, ki), c in [(col, col) for col in COLS]:
            if k == "ad": trow.append("<td class='l'>TỔNG</td>")
            elif k == "status": trow.append("<td class='l'></td>")
            else: trow.append(f"<td>{fmt(k, tot[k], ki)}</td>")
        trow.append("</tr>")
        parts.append("".join(trow))
        parts.append("</tbody></table></div>")
    parts.append("<p class='note'>Video plays = số lần video bắt đầu phát. ThruPlay = xem ≥15s (hoặc hết video) — "
                 "chỉ số Meta thay thế cho “3-second video plays” cũ. ThruPlay % / Xem 50% / Xem 100% = trên tổng hiển thị. "
                 "Số liệu Meta theo pixel (cửa sổ phân bổ 7 ngày) — có thể lệch nhẹ so với GA4 (theo phiên).</p>")
    parts.append("</div></body></html>")
    return "".join(parts)


def main():
    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))
    data = {}
    for cid, label, obj in CAMPAIGNS:
        data[(cid, label, obj)] = pull(up, cid)
        print(f"{label}: {len(data[(cid, label, obj)])} ads")
    OUT.write_text(render(data))
    print("wrote", OUT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
