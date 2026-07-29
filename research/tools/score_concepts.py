#!/usr/bin/env python3
"""First-pass auto-scorer for competitor ad concepts vs new-ad-potential-scorecard.md.
Reads /tmp/ads_records.jsonl (one ad per line), clusters to concept level, scores.
Objective criteria (A1/A7/A4 · B1/B2) use the PART-0 calibrated thresholds.
Judgment criteria (A5/A6/B6/B7) use transparent keyword heuristics — flagged for human review.
Track is assigned by proxy (long-runner/mature-format=Evergreen; young+novel-mechanic=Trending)
because Google Trends (A3/B3) was not pulled. Output: ranked TSV to stdout.
"""
import json, re, statistics
from collections import defaultdict

recs = [json.loads(l) for l in open('/tmp/ads_records.jsonl') if l.strip()]

# ---- cluster to concept (cleaned slug) ----
concepts = defaultdict(lambda: {'days': [], 'price': [], 'fmt': [], 'active': 0, 'copy': '', 'brand': ''})
for r in recs:
    c = re.sub(r'-(psnl|pnl)-', '-', r['concept']).strip('-')
    if not c or c in ('tsn', 'collections'):
        continue
    k = (r['brand'], c)
    d = concepts[k]
    d['brand'] = r['brand']
    if r['days'] is not None: d['days'].append(r['days'])
    p = r['price']
    try:
        pv = float(p)
        if pv > 0: d['price'].append(pv)
    except: pass
    d['fmt'].append(r['fmt'])
    d['active'] += r.get('active', 1)   # PER-PRODUCT active creatives (sum countActive over its ads)
    if len(r['copy']) > len(d['copy']): d['copy'] = r['copy']

# ---- keyword tag helpers ----
def has(s, *kw): return any(k in s for k in kw)
SEASON = ['christmas','halloween','fathers-day','mothers-day','valentine','4th-of-july','patriotic',
          'back-to-school','graduation','senior','fall','summer','woofmas','day-of-the-dead','america-250','pregnancy']
NOVEL  = ['squishy','book-nook','moon','crystal-ball','night-light','bottle-lamp','solar-mason','candle-warmer',
          'suncatcher','action-figure','figure','lapel-pin','book-page-holder','resin','trinket-tray','jewelry-dish','desk-mat']
YEARROUND = ['pet','dog','cat','couple','anniversary','memorial','always-with-you','gaming','gamer','book','guitar',
             'sewing','coworker','boss','brother','sister','sibling','bestie','friend','camping','husband','wife','naughty']

def price_band(prices, brand):
    if prices: return statistics.median(prices)
    return 24.0 if brand == 'PFG' else None  # PFG known $18.99-27.99, else unknown

def sc_A1(days):
    m = max(days) if days else 0
    return (3 if m>=90 else 2 if m>=60 else 1 if m>=30 else 0), m
def sc_A7(p):
    if p is None: return 1, 'n/a'   # unknown -> conservative 1
    return (3 if p>=60 else 2 if p>=35 else 1 if p>=25 else 0), round(p,2)

for (brand, c), d in concepts.items():
    s = c + ' ' + d['copy'].lower()
    days = d['days']; a1,maxd = sc_A1(days)
    p = price_band(d['price'], brand); a7,pv = sc_A7(p)
    nact = d['active']                                  # PER-PRODUCT active-creative count (fixed 2026-07-30)
    a4 = 3 if nact>=4 else 2 if nact>=2 else 1           # evergreen: sustained scale
    b2 = 3 if nact>=8 else 2 if nact>=4 else 1 if nact>=2 else 0   # trending: strong momentum
    # judgment heuristics
    seasonal = has(s, *SEASON); novel = has(s, *NOVEL); yearround = has(s, *YEARROUND)
    a5 = 3 if yearround else (1 if seasonal else 2)                 # occasion durability
    a6 = 3 if has(s,'photo','portrait','moon','figure','family','grandkids','names','multi','memorial') else \
         1 if has(s,'shirt','mug','sweatpants','boxer','belt','notebook','cap','journal') and not has(s,'photo','name') else 2
    # track assignment (proxy; Google Trends A3/B3 not pulled)
    track = 'Trending' if (novel and maxd < 60) else 'Evergreen'
    # scores
    ever = a1*3 + 3*3 + a5*2 + a6*3 + a4*2 + a7*2      # A2 fixed=3 (multi-seller template), A3 omitted(pending Trends)
    ever_max = 3*3+3*3+3*2+3*3+3*2+3*2                  # =60 (excl A3)
    b1 = 3 if maxd<30 else 2 if maxd<60 else 1 if maxd<90 else 0
    b7 = a6
    trend = b1*3 + b2*3 + b7*2 + a7*2                   # excl B3(pending),B4,B5,B6 needing more data
    trend_max = 3*3+3*3+3*2+3*2                          # =40
    d.update(track=track, maxd=maxd, price=pv, nact=nact, a1=a1,a4=a4,a5=a5,a6=a6,a7=a7,b1=b1,b2=b2,
             ever=ever, ever_pct=round(100*ever/ever_max), trend=trend, trend_pct=round(100*trend/trend_max),
             seasonal=seasonal, novel=novel)

rows = [ (brand,c,d) for (brand,c),d in concepts.items() ]
# rank: evergreen concepts by ever_pct, trending by trend_pct
def key(x):
    d = x[2]; return d['ever_pct'] if d['track']=='Evergreen' else d['trend_pct']
rows.sort(key=lambda x:(x[2]['track'], -key(x)))

print(f"# concepts clustered: {len(rows)}\n")
hdr = ['TRACK','BRAND','SCORE%','maxDays','price','#activeCreatives','A1','A4','A5','A6','A7','B1','B2','CONCEPT']
print('\t'.join(hdr))
for brand,c,d in rows:
    pct = d['ever_pct'] if d['track']=='Evergreen' else d['trend_pct']
    print('\t'.join(str(x) for x in [d['track'],brand,pct,d['maxd'],d['price'],d['nact'],
          d['a1'],d['a4'],d['a5'],d['a6'],d['a7'],d['b1'],d['b2'], c[:60]]))
