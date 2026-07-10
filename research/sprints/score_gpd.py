#!/usr/bin/env python3
"""Score the Grandparents Day 2026 idea shortlist against the rubric
(03-scoring-rubric.md) and append rows to the idea database.

Signals used:
  - search  : Ahrefs Keywords Explorer, US (live pull 2026-07-10)
  - mktpl    : Apify yumitori/etsy-listings-scraper, in-cart velocity (live 2026-07-10)
  - social   : Apify Pinterest (saves/theme volume) + TikTok (plays/saves) (live 2026-07-10)
Demand   = 0.5*search + 0.3*mktpl + 0.2*social      (each 0-5)
Composite= .30*demand + .20*compgap + .15*gift + .15*margin + .10*season + .10*brand

Idempotent: drops any existing rows for this occasion before re-writing.
"""
import csv, os

OCC = "grandparents day"
DATE = "2026-07-10"
SRC = "ahrefs+etsy+pinterest+tiktok"
DB = os.path.join(os.path.dirname(__file__), "..", "templates", "idea-database.csv")

# id, product, recipient, personalization, angle, hook,
# search_vol, slope, mktpl_evidence, social_note,
# [search, mktpl, social, compgap, gift, margin, season, brand]
IDEAS = [
    ("GPD01", "ceramic mug", "grandma", "grandkids names", "sentimental/milestone",
     "Grandma + grandkids' names (Promoted to Grandma)", 2200, "rising", "46 in-cart (promoted-to-grandma)",
     "pinterest med; tiktok product-mug low", [5, 4, 3, 3, 5, 4, 5, 5]),
    ("GPD02", "sweatshirt", "grandma", "grandkids names + birth flowers", "identity/sentimental",
     "Grandma's Garden — a birth flower per grandchild", 250, "rising", "64 in-cart (floral applique swtsht)",
     "pinterest: birth-flower DOMINANT theme", [4, 5, 5, 3, 5, 3, 5, 5]),
    ("GPD03", "necklace (jewelry)", "grandma", "grandkids birthstones/names", "sentimental",
     "A birthstone for every grandchild", 350, "rising", "291 in-cart (name necklace)",
     "tiktok jewelry/memorial 82K plays; pinterest present", [3, 5, 4, 3, 5, 4, 5, 4]),
    ("GPD04", "stainless tumbler", "grandma", "grandkids names + birth flower", "identity",
     "Nana's Garden tumbler", 600, "rising", "birth-flower tumbler bestsellers",
     "pinterest: birth-flower DOMINANT theme", [4, 3, 5, 3, 4, 4, 5, 5]),
    ("GPD05", "fleece/woven blanket", "grandma", "grandkids names, floral", "sentimental",
     "Grandma's woven family blanket", 500, "steady", "24 in-cart (woven blanket)",
     "moderate social", [3, 3, 3, 4, 5, 3, 5, 5]),
    ("GPD06", "t-shirt", "grandma", "nickname + grandkids names", "identity",
     "In a world full of grandmas, be a Mimi (Gigi/Nana/Mimi)", 500, "steady", "63 in-cart; shops w/100k+ sales",
     "present but not a viral standout", [4, 5, 3, 2, 4, 3, 4, 5]),
    ("GPD07", "ceramic mug", "grandpa", "grandkids names", "milestone",
     "First Dad, Now Grandpa", 4900, "rising", "178 in-cart (bestseller)",
     "pinterest present; tiktok product-mug low", [3, 5, 3, 3, 5, 4, 5, 5]),
    ("GPD08", "apron", "grandpa", "grandkids names", "identity/funny",
     "Grandpa's Grilling Crew + kids' names", 4900, "steady", "793 in-cart (grill cutting board); 82 grill plate",
     "tiktok grandpa novelty apparel viral (macorner 4.2M)", [3, 5, 4, 3, 4, 4, 5, 4]),
    ("GPD09", "t-shirt", "grandpa", "photo", "sentimental",
     "Best Papa Ever + photo", 450, "rising", "290 in-cart (photo grandpa shirt)",
     "tiktok photo/novelty viral; pinterest photo collage", [3, 5, 4, 3, 4, 3, 5, 4]),
    ("GPD10", "t-shirt", "grandma", "none/text", "funny",
     "You can't tell me what to do, you're not my grandkids", 500, "steady", "25-31 in-cart (funny tees)",
     "shareable but grandma social skews sentimental not funny", [3, 4, 4, 2, 3, 3, 4, 4]),
    ("GPD11", "doormat", "both", "nicknames", "sentimental/home",
     "Life is better at Gigi & Poppy's house", 200, "steady", "proven cat: shop w/720k sales",
     "low social", [2, 3, 3, 3, 4, 3, 5, 5]),
    ("GPD12", "canvas/wood sign", "grandma", "photo + grandkids names", "sentimental",
     "Grandkids make life grand", 200, "steady", "photo-holder bestseller",
     "tiktok photo-keepsake viral (photo books 128K)", [2, 4, 4, 3, 4, 3, 5, 5]),
    ("GPD13", "pillow", "grandma", "birth flowers + grandkids names", "sentimental",
     "Grandma's Garden — where love grows", 250, "rising", "birth-flower pillow bestseller",
     "pinterest: birth-flower DOMINANT theme", [3, 3, 5, 3, 4, 4, 5, 5]),
    ("GPD14", "cap/hat", "grandpa", "est. year", "milestone",
     "Grandpa Est. 2026", 450, "rising", "74 in-cart (EST hat)",
     "custom-hat tiktok present", [3, 4, 3, 3, 4, 4, 5, 4]),
    # --- NEW angles surfaced by the social pull ---
    ("GPD15", "tea towel / mug", "grandma", "grandma's handwritten recipe", "sentimental/nostalgic",
     "Grandma's Recipe — in her own handwriting", 500, "rising", "recipe-cookbook sellers; handwriting recipe on Etsy",
     "tiktok recipe-frame keepsake VIRAL (193K plays, 5.8K saves)", [3, 4, 5, 3, 5, 4, 5, 5]),
    ("GPD16", "canvas / blanket", "grandma", "photo collage", "memorial",
     "Grandmas should live forever — photo-collage keepsake", 350, "steady", "memorial collage present on Etsy",
     "tiktok memorial collage viral (85K plays; 'best gma')", [3, 3, 5, 3, 5, 3, 4, 5]),
]

W = dict(demand=.30, compgap=.20, gift=.15, margin=.15, season=.10, brand=.10)


def score(v):
    s, m, so, cg, g, mg, se, br = v
    demand = 0.5 * s + 0.3 * m + 0.2 * so
    comp = (W["demand"] * demand + W["compgap"] * cg + W["gift"] * g +
            W["margin"] * mg + W["season"] * se + W["brand"] * br)
    return round(demand, 2), round(comp, 2)


rows = []
for (iid, prod, rec, pers, angle, hook, vol, slope, mk, soc, v) in IDEAS:
    demand, comp = score(v)
    status = "greenlit" if comp >= 4.0 else "backlog"
    rows.append([f"IDEA-{iid}", DATE, status, prod, rec, OCC, pers, angle, hook,
                 SRC, vol, slope, mk, soc, demand,
                 v[3], v[4], v[5], v[6], v[7], comp, "", "", "", "", "", "",
                 "", "social pulled: pinterest saves + tiktok plays/saves", ""])

rows.sort(key=lambda r: r[20], reverse=True)  # composite desc

# Idempotent: read existing, drop this occasion's rows, keep the rest.
with open(DB, newline="") as f:
    reader = list(csv.reader(f))
header, existing = reader[0], reader[1:]
kept = [r for r in existing if not (len(r) > 5 and r[5] == OCC)]

with open(DB, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(kept)
    for r in rows:
        w.writerow(r)

print(f"Appended {len(rows)} Grandparents Day rows to idea-database.csv\n")
print(f"{'RANK':4} {'ID':10} {'COMP':5} {'DEM':4} {'STATUS':9} HOOK")
print("-" * 92)
for i, r in enumerate(rows, 1):
    print(f"{i:>2}.  {r[0]:10} {r[20]:<5} {r[14]:<4} {r[2]:9} {r[8]}")
