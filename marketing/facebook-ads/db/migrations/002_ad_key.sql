-- One Meta ad carries both the 9:16 and 4:5 files (asset customization), so metrics attach to the AD,
-- keyed by ad_key = creative_id minus the ratio, e.g. SUN-P1_C1-H1_E0_v01.
drop view creative_performance;
alter table creatives drop constraint creatives_meta_ad_id_key;
alter table creatives add column ad_key text;
create index on creatives (ad_key);
create index on creatives (meta_ad_id);
alter table ad_metrics_daily drop column creative_id;
alter table ad_metrics_daily add column ad_key text;
create index on ad_metrics_daily (ad_key);
-- views `ads` (one row per ad with build attributes) and `ad_performance` (ads + hook attributes + summed metrics
-- and hook_rate / hold_rate / link_ctr / cost_per_atc / roas) — full DDL as applied in Supabase migration 002_ad_key.
