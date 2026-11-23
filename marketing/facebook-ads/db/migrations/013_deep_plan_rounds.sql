-- 013: round codes follow the deep test plan (decided 2026-11-21, replaces R0–R4).
-- C0 concept discovery · C1 concept core grid · C2 concept execution grid · H1 hook opening grid · H2 hook type grid
-- B break-even check · S scaling refreshes (hook swaps on the winner after B; not a test round).
-- cells was empty when applied (0 rows), so no data mapping is needed.
alter table cells drop constraint cells_round_type_check;
alter table cells add constraint cells_round_type_check
  check (round_type in ('C0','C1','C2','H1','H2','B','S'));
comment on column cells.round_type is 'Deep-plan round: C0, C1, C2, H1, H2, B, S (see research/reference/video-team/concept-framework.md §6)';
