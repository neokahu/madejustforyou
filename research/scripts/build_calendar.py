#!/usr/bin/env python3
"""Build the US gifting-occasion calendar for MadeJustForYou.

Rule: start-selling by = occasion - 2 months (need >=2 months selling runway).
      last-order by     = occasion - 14 days (manufacturing + shipping buffer).
Today is fixed to the project 'as of' date for reproducibility.
"""
import calendar
from datetime import date, timedelta

TODAY = date(2026, 7, 10)
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


def nth_weekday(year, month, weekday, n):
    """n-th (1-based) `weekday` of month."""
    d = date(year, month, 1)
    offset = (weekday - d.weekday()) % 7
    return d + timedelta(days=offset + 7 * (n - 1))


def last_weekday(year, month, weekday):
    last_day = calendar.monthrange(year, month)[1]
    d = date(year, month, last_day)
    offset = (d.weekday() - weekday) % 7
    return d - timedelta(days=offset)


def first_weekday_after(d, weekday):
    offset = (weekday - d.weekday()) % 7
    return d + timedelta(days=offset or 7)


def minus_months(d, m):
    month = d.month - m
    year = d.year
    while month <= 0:
        month += 12
        year -= 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


labor_day_2026 = nth_weekday(2026, 9, MON, 1)  # Sep 7

# (name, category, date, notes)
OCC = [
    ("Parents' Day", "family", nth_weekday(2026, 7, SUN, 4), "4th Sun of July"),
    ("Friendship Day (US)", "friends", nth_weekday(2026, 8, SUN, 1), "1st Sun of Aug; Sisters' Day same date"),
    ("National Dog Day", "pets", date(2026, 8, 26), "fixed"),
    ("Labor Day", "seasonal", labor_day_2026, "1st Mon of Sep"),
    ("Grandparents Day", "family", first_weekday_after(labor_day_2026, SUN), "1st Sun after Labor Day"),
    ("National Pet Memorial Day", "pets/memorial", nth_weekday(2026, 9, SUN, 2), "2nd Sun of Sep"),
    ("Boss's Day", "work", date(2026, 10, 16), "fixed"),
    ("Sweetest Day", "partner", nth_weekday(2026, 10, SAT, 3), "3rd Sat of Oct (esp. Midwest/NE US)"),
    ("Halloween", "seasonal", date(2026, 10, 31), "fixed"),
    ("Day of the Dead", "memorial", date(2026, 11, 1), "Nov 1-2"),
    ("Veterans Day", "military", date(2026, 11, 11), "fixed"),
    ("Thanksgiving", "seasonal", nth_weekday(2026, 11, THU, 4), "4th Thu of Nov"),
    ("Black Friday / Cyber Monday", "retail", nth_weekday(2026, 11, THU, 4) + timedelta(days=1), "day after Thanksgiving"),
    ("Hanukkah (begins)", "seasonal", date(2026, 12, 4), "starts sunset Dec 4, 2026"),
    ("Christmas", "seasonal", date(2026, 12, 25), "peak POD season; buying opens early Oct"),
    ("Kwanzaa", "seasonal", date(2026, 12, 26), "Dec 26 - Jan 1"),
    ("New Year's Day", "seasonal", date(2027, 1, 1), "fixed"),
    ("Galentine's Day", "friends", date(2027, 2, 13), "fixed"),
    ("Valentine's Day", "partner", date(2027, 2, 14), "fixed"),
    ("Presidents' Day", "retail", nth_weekday(2027, 2, MON, 3), "3rd Mon of Feb"),
    ("International Women's Day", "identity", date(2027, 3, 8), "fixed"),
    ("St. Patrick's Day", "seasonal", date(2027, 3, 17), "fixed"),
    ("Easter", "seasonal", date(2027, 3, 28), "computed for 2027"),
    ("National Pet Day", "pets", date(2027, 4, 11), "fixed"),
    ("Administrative Professionals Day", "work", nth_weekday(2027, 4, WED, 3), "Wed of last full wk Apr (definition varies - verify)"),
    ("Teacher Appreciation Day", "work", nth_weekday(2027, 5, TUE, 1), "Tue of 1st full wk May; week May 3-7"),
    ("Cinco de Mayo", "seasonal", date(2027, 5, 5), "fixed"),
    ("Nurses Day", "work", date(2027, 5, 6), "Nurses Week May 6-12"),
    ("Mother's Day", "family", nth_weekday(2027, 5, SUN, 2), "2nd Sun of May - top POD occasion"),
    ("Armed Forces Day", "military", nth_weekday(2027, 5, SAT, 3), "3rd Sat of May"),
    ("Graduation season", "milestone", date(2027, 5, 15), "season mid-May to mid-Jun"),
    ("Memorial Day", "military", last_weekday(2027, 5, MON), "last Mon of May"),
    ("Juneteenth", "identity", date(2027, 6, 19), "fixed"),
    ("Father's Day", "family", nth_weekday(2027, 6, SUN, 3), "3rd Sun of Jun - top POD occasion"),
    ("Independence Day", "seasonal", date(2027, 7, 4), "fixed"),
]

EVERGREEN = [
    ("Birthday", "Year-round; personalize by name/age/zodiac. Base-load demand."),
    ("Anniversary", "Year-round; dates, 'together since', couple names."),
    ("Wedding / Engagement", "Year-round; peak May-Oct. Mr & Mrs, est. date."),
    ("New Baby / Baby Shower", "Year-round; birth stats, name, nursery decor."),
    ("Housewarming", "Year-round; address, coordinates, family name."),
    ("Memorial / Sympathy", "Year-round; high emotion; pet & human loss."),
    ("Retirement", "Year-round; milestone, years of service."),
]


def status(occ_d, start_d):
    d_start = (start_d - TODAY).days
    d_occ = (occ_d - TODAY).days
    if d_occ < 0:
        return "past", d_start, d_occ
    if start_d <= TODAY:
        return "BEHIND", d_start, d_occ           # start window already open/passed
    if d_start <= 30:
        return "ACT NOW", d_start, d_occ
    if d_start <= 75:
        return "PREP SOON", d_start, d_occ
    return "future", d_start, d_occ


rows = []
for name, cat, occ_d, notes in OCC:
    start_d = minus_months(occ_d, 2)
    last_d = occ_d - timedelta(days=14)
    st, d_start, d_occ = status(occ_d, start_d)
    rows.append(dict(name=name, cat=cat, occ=occ_d, start=start_d, last=last_d,
                     d_start=d_start, d_occ=d_occ, status=st, notes=notes))

rows.sort(key=lambda r: r["start"])

# ---- CSV ----
import csv
with open("research/calendar/occasions-calendar.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["occasion", "category", "occasion_date", "weekday",
                "start_selling_by", "last_order_by", "days_until_start_selling",
                "days_until_occasion", "status", "notes"])
    for r in rows:
        w.writerow([r["name"], r["cat"], r["occ"].isoformat(), r["occ"].strftime("%a"),
                    r["start"].isoformat(), r["last"].isoformat(),
                    r["d_start"], r["d_occ"], r["status"], r["notes"]])

# ---- ICS ----
def ics_date(d):
    return d.strftime("%Y%m%d")

lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//MadeJustForYou//Occasions//EN",
         "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:MJFY Gifting Occasions"]
stamp = "20260710T000000Z"
for i, r in enumerate(rows):
    if r["status"] == "past":
        continue
    # start-selling reminder
    lines += ["BEGIN:VEVENT", f"UID:mjfy-start-{i}@madejustforyou",
              f"DTSTAMP:{stamp}", f"DTSTART;VALUE=DATE:{ics_date(r['start'])}",
              f"DTEND;VALUE=DATE:{ics_date(r['start'] + timedelta(days=1))}",
              f"SUMMARY:🟢 START SELLING: {r['name']}",
              f"DESCRIPTION:Launch designs for {r['name']} ({r['occ'].isoformat()}). Last order {r['last'].isoformat()}.",
              "END:VEVENT"]
    # occasion day
    lines += ["BEGIN:VEVENT", f"UID:mjfy-occ-{i}@madejustforyou",
              f"DTSTAMP:{stamp}", f"DTSTART;VALUE=DATE:{ics_date(r['occ'])}",
              f"DTEND;VALUE=DATE:{ics_date(r['occ'] + timedelta(days=1))}",
              f"SUMMARY:🎁 {r['name']}",
              f"DESCRIPTION:Last order by {r['last'].isoformat()} to arrive in time.",
              "END:VEVENT"]
lines.append("END:VCALENDAR")
with open("research/calendar/occasions-calendar.ics", "w") as f:
    f.write("\r\n".join(lines) + "\r\n")

# ---- Markdown ----
EMO = {"ACT NOW": "🟢", "BEHIND": "🔴", "PREP SOON": "🟡", "future": "⚪"}
md = []
md.append("# US Gifting-Occasion Calendar\n")
md.append(f"> Generated by `build_calendar.py`. **As of {TODAY.isoformat()}.** "
          "Rerun the script to roll the window forward.\n")
md.append("**Rule:** `start-selling by = occasion − 2 months` (≥2 months of selling runway) · "
          "`last-order by = occasion − 14 days` (manufacturing + shipping buffer).\n")
md.append("| Status | Start-sell | Last-order | Occasion | Date | Day | Cat | Notes |")
md.append("|--------|-----------|-----------|----------|------|-----|-----|-------|")
for r in rows:
    if r["status"] == "past":
        continue
    md.append(f"| {EMO[r['status']]} {r['status']} | {r['start'].isoformat()} | "
              f"{r['last'].isoformat()} | **{r['name']}** | {r['occ'].isoformat()} | "
              f"{r['occ'].strftime('%a')} | {r['cat']} | {r['notes']} |")

md.append("\n## 🟢 Act now — start-selling window is open or within ~a month\n")
md.append("These are *the closest occasions minus 2 months* — work on these immediately:\n")
for r in rows:
    if r["status"] == "ACT NOW":
        md.append(f"- **{r['name']}** — occasion {r['occ'].isoformat()} ({r['occ'].strftime('%a')}); "
                  f"start selling **{r['start'].isoformat()}**; hard last-order {r['last'].isoformat()}.")

md.append("\n## 🔴 Behind — 2-month window already passed (occasion still ahead)\n")
md.append("Ideal runway is gone. Only pursue with rush designs / existing SKUs, or skip to next year:\n")
for r in rows:
    if r["status"] == "BEHIND":
        md.append(f"- **{r['name']}** — occasion {r['occ'].isoformat()} "
                  f"(last-order {r['last'].isoformat()}); start-sell date was {r['start'].isoformat()}.")

md.append("\n## 🟡 Prep soon — start-selling within ~2.5 months\n")
for r in rows:
    if r["status"] == "PREP SOON":
        md.append(f"- **{r['name']}** — start selling {r['start'].isoformat()} (occasion {r['occ'].isoformat()}).")

md.append("\n## ♻️ Evergreen occasions (no fixed date — always-on base load)\n")
for name, notes in EVERGREEN:
    md.append(f"- **{name}** — {notes}")

md.append("\n---\nData files: [`occasions-calendar.csv`](occasions-calendar.csv) (master) · "
          "[`occasions-calendar.ics`](occasions-calendar.ics) (import into Google/Apple Calendar).")
with open("research/calendar/occasions-calendar.md", "w") as f:
    f.write("\n".join(md) + "\n")

# ---- console summary ----
print(f"TODAY = {TODAY.isoformat()}  (start-selling = occasion - 2 months)\n")
hdr = f"{'STATUS':10} {'START-SELL':11} {'OCCASION':11} {'in':>4}d  NAME"
print(hdr); print("-" * len(hdr))
for r in rows:
    if r["status"] == "past":
        continue
    print(f"{r['status']:10} {r['start'].isoformat()} {r['occ'].isoformat()} {r['d_start']:>4}  {r['name']}")

print("\n=== ACT NOW / BEHIND (start-selling window is open or imminent) ===")
for r in rows:
    if r["status"] in ("ACT NOW", "BEHIND"):
        late = " (already late — occasion soon)" if r["status"] == "BEHIND" else ""
        print(f"  • {r['name']}: occasion {r['occ'].isoformat()} ({r['occ'].strftime('%a')}), "
              f"start-sell {r['start'].isoformat()}, last-order {r['last'].isoformat()}{late}")
