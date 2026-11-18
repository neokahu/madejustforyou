-- 003 (2026-11-18): hook-framework fields
alter table hooks add column trigger_2 text;
alter table hooks add column primitives text;
alter table hooks add column truth_frame_s numeric;
alter table hooks add column arm_axis text;
