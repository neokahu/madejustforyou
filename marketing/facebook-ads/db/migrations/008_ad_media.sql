-- 008 (2026-11-18): ad media from Meta, filled by db_sync.py media.
alter table ads add column meta_ad_name text, add column meta_status text, add column preview_url text, add column post_url text,
  add column video_url text, add column thumbnail_url text, add column video_length_s numeric, add column media_refreshed_at timestamptz;
-- ad_performance recreated as `a.* + hook tags + summed metrics` so new ads columns flow through automatically.
