-- 012 (2026-11-19): sync heartbeat. One row per db_sync run (ok/failed + message); Hook Lab warns on failure or >36h staleness.
create table sync_runs (run_id bigint generated always as identity primary key, started_at timestamptz not null default now(),
  finished_at timestamptz, command text not null, ok boolean not null, ad_days int, message text, host text);
create index idx_sync_runs_started_at on sync_runs(started_at desc);
alter table sync_runs enable row level security;
create policy sync_runs_viewer_read on sync_runs for select to authenticated using ((select private.is_dashboard_viewer()));
