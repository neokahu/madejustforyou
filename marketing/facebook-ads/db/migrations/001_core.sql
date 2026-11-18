-- MJ4U ads database (Supabase project mj4u-ads, ref bjplojqovxetmbchzzms)
-- Purpose: link every ad's Meta results back to the hook / concept / script it was built from,
-- so we can learn which hook formats, triggers, mechanisms and content win.
-- Writers: Claude only (service role / MCP). Readers: the dashboard (read-only via RLS select policies).
-- Attribute columns are TEXT, not enums: the hook framework will evolve.

create table products (
  product_id      text primary key,               -- MJ4U-NNN, or a slug for pre-ID products
  name            text not null,
  recipient       text,
  stage           text,
  price           numeric,
  break_even_cpa  numeric,
  break_even_roas numeric,
  store_url       text,
  notes           text,
  updated_at      timestamptz not null default now()
);

create table tests (
  test_id     text primary key,                   -- e.g. suncatcher-phase1
  product_id  text not null references products,
  name        text not null,
  phase       text,
  plan_url    text,
  primary_metric text default 'hook_rate',
  status      text default 'planned',             -- planned|building|live|done|killed
  started_on  date,
  ended_on    date,
  notes       text
);

create table cells (                              -- concept x hook combination in a test plan
  cell_id      text primary key,                  -- e.g. suncatcher-phase1:C1-H2
  test_id      text not null references tests,
  concept_code text not null,                     -- C1
  concept_name text,
  hook_arm     text,                              -- H1 / H2
  hypothesis   text,                              -- frozen pre-registration line
  is_control   boolean default false
);

create table hooks (                              -- one row per hook card (selected or not)
  hook_id      text primary key,
  test_id      text references tests,
  arm          text,
  format       text,                              -- hook-framework FORMAT family
  trigger      text,                              -- hook-framework TRIGGER
  mechanism    text,                              -- gift mechanism M1..M11
  cep          text,                              -- relationship x occasion
  frame1_visual text,
  onset_0_5s   text,
  caption      text,
  audio_cue    text,
  promise      text,
  paid_by_s    numeric,
  critic_score numeric,
  critic_spread numeric,
  status       text default 'candidate',          -- candidate|cut|selected|reserve|parked|shipped
  notes        text
);

create table creatives (                          -- one row per delivered file (ad x format x version)
  creative_id  text primary key,                  -- {PRODUCT}_{CONCEPT}-{HOOK}_{VAR}_{RATIO}_v{NN}
  product_id   text not null references products,
  test_id      text references tests,
  cell_id      text references cells,
  hook_id      text references hooks,
  concept_code text,
  variant      text,                              -- E0 = control edit
  ratio        text,                              -- 916 | 45
  version      int,
  length_s     numeric,
  has_vo       boolean,
  caption_style text,
  music_source text,
  ai_people    boolean,
  structure    text,                              -- e.g. HOOK-STAKES-TURN-PROOF-CONNECTION-CTA
  local_path   text,
  drive_path   text,
  sha256       text,
  recipe       text,
  qa_status    text,
  qa_report    text,
  waivers      text,
  meta_ad_id   text unique,                       -- set after upload
  meta_adset_id text,
  meta_campaign_id text,
  launched_on  date,
  notes        text,
  created_at   timestamptz not null default now()
);

create table ad_metrics_daily (                   -- one row per Meta ad per day (account timezone)
  meta_ad_id   text not null,
  date         date not null,
  creative_id  text references creatives,         -- resolved from meta_ad_id or ad name
  ad_name      text,
  adset_id     text,
  campaign_id  text,
  impressions  int  default 0,
  reach        int  default 0,
  spend        numeric default 0,
  link_clicks  int  default 0,
  video_plays  int  default 0,
  video_3s     int  default 0,
  video_p25    int  default 0,
  video_p50    int  default 0,
  video_p75    int  default 0,
  video_p95    int  default 0,
  video_p100   int  default 0,
  thruplays    int  default 0,
  avg_watch_s  numeric,
  add_to_cart  int  default 0,
  checkouts    int  default 0,
  purchases    int  default 0,
  purchase_value numeric default 0,
  pulled_at    timestamptz not null default now(),
  primary key (meta_ad_id, date)
);
create index on ad_metrics_daily (creative_id);
create index on creatives (hook_id);
create index on creatives (cell_id);

-- Per-creative totals + derived rates (all denominators exposed so the dashboard can compute intervals)
create view creative_performance with (security_invoker = true) as
select c.creative_id, c.product_id, c.test_id, c.cell_id, c.concept_code, c.ratio, c.length_s, c.has_vo,
       h.hook_id, h.arm, h.format, h.trigger, h.mechanism,
       min(m.date) as first_day, max(m.date) as last_day, count(m.date) as days,
       sum(m.impressions) as impressions, sum(m.spend) as spend, sum(m.link_clicks) as link_clicks,
       sum(m.video_3s) as video_3s, sum(m.video_p50) as video_p50, sum(m.video_p100) as video_p100,
       sum(m.thruplays) as thruplays, sum(m.add_to_cart) as add_to_cart, sum(m.purchases) as purchases,
       sum(m.purchase_value) as purchase_value,
       sum(m.video_3s)::numeric   / nullif(sum(m.impressions),0) as hook_rate,
       sum(m.thruplays)::numeric  / nullif(sum(m.video_3s),0)    as hold_rate,
       sum(m.link_clicks)::numeric/ nullif(sum(m.impressions),0) as link_ctr,
       sum(m.spend)               / nullif(sum(m.add_to_cart),0) as cost_per_atc,
       sum(m.purchase_value)      / nullif(sum(m.spend),0)       as roas
from creatives c
left join hooks h on h.hook_id = c.hook_id
left join ad_metrics_daily m on m.creative_id = c.creative_id
group by c.creative_id, h.hook_id;

-- Read-only access for the dashboard; writes only via service role (bypasses RLS)
alter table products         enable row level security;
alter table tests            enable row level security;
alter table cells            enable row level security;
alter table hooks            enable row level security;
alter table creatives        enable row level security;
alter table ad_metrics_daily enable row level security;
create policy read_all on products         for select to anon, authenticated using (true);
create policy read_all on tests            for select to anon, authenticated using (true);
create policy read_all on cells            for select to anon, authenticated using (true);
create policy read_all on hooks            for select to anon, authenticated using (true);
create policy read_all on creatives        for select to anon, authenticated using (true);
create policy read_all on ad_metrics_daily for select to anon, authenticated using (true);

-- (applied separately as migration 002_ad_key, 2026-11-18) — see 002_ad_key.sql
