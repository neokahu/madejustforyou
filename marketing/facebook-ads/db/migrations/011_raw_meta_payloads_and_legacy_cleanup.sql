-- 011 (2026-11-19): keep everything Meta returns + remove pre-framework ads.
alter table ad_metrics_daily add column raw jsonb, add column fields_requested text;   -- full insights row per ad-day
alter table ads add column meta_raw jsonb;                                              -- full ad object incl. creative
-- user 2026-11-19: "remove all the old data from old ads ... those were not following any framework"
delete from ad_metrics_daily where ad_key is null or ad_key in (select ad_key from ads where test_id = 'mj4u-111-aug');
delete from creatives where ad_key in (select ad_key from ads where test_id = 'mj4u-111-aug');
delete from ads where test_id = 'mj4u-111-aug';
delete from tests where test_id = 'mj4u-111-aug';
