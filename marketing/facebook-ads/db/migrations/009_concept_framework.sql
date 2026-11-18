-- 009 (2026-11-18): concept framework + hook element tags (research/reference/video-team/concept-framework.md §7).
-- Codes stay closed via `codebook`; every code column is validated by trigger (private.assert_code), which keeps
-- tables free of the *_dim helper columns the draft proposed while giving the same guarantee.

alter table ads rename column structure to structure_desc;   -- free text; `structure` is now the ST code from executions

create table codebook (
  dimension  text not null,
  code       text not null,
  label      text not null,
  layer      text not null check (layer in ('concept','execution','hook','hook_element')),
  source     text,
  retired    boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint codebook_pkey primary key (dimension, code)
);

create table concepts (                        -- concept CORE = the reason to buy
  concept_id   text primary key,               -- <PRODUCT>-K<nn>
  product_id   text not null references products(product_id) on delete restrict,
  name         text not null,
  angle        text not null,
  buyer_role   text not null,
  recipient    text not null,
  occasion     text not null,
  reason_line  text not null constraint concepts_reason_line_check
               check (array_length(regexp_split_to_array(trim(reason_line), '\s+'), 1) <= 15),
  insight      text,
  core_key     text generated always as (angle || '·' || buyer_role || '·' || recipient) stored,
  critic_score numeric, critic_spread numeric,
  status       text not null default 'candidate' constraint concepts_status_check
               check (status in ('candidate','cut','selected','reserve','shipped','parked','retired')),
  notes        text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

create table executions (                      -- one build of a concept
  execution_id text primary key,               -- <concept_id>-X<n>
  concept_id   text not null references concepts(concept_id) on delete restrict,
  structure    text not null, pov text not null, proof text not null, proof_2 text,
  prod_format  text not null, reveal text not null, register text not null,
  logline text, beat_map text, cast_artwork text, hypothesis text,
  is_bundle    boolean not null default false, bundle_note text,
  critic_score numeric, critic_spread numeric,
  status       text not null default 'candidate' constraint executions_status_check
               check (status in ('candidate','cut','selected','reserve','shipped','parked','retired')),
  notes        text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

alter table cells add column concept_id text references concepts(concept_id) on delete restrict,
                  add column execution_id text references executions(execution_id) on delete restrict,
                  add column round_type text constraint cells_round_type_check check (round_type in ('R0','R1','R2','R3','R4')),
                  add column axis text;
alter table ads   add column concept_id text references concepts(concept_id) on delete restrict,
                  add column execution_id text references executions(execution_id) on delete restrict;
alter table hooks add column f1_subject text, add column shot_size text, add column onset text, add column onset_s numeric,
                  add column caption_type text,
                  add column caption_words int constraint hooks_caption_words_check check (caption_words >= 0),
                  add column caption_band text generated always as (case when caption_words is null then null
                    when caption_words = 0 then 'LB0' when caption_words <= 4 then 'LB1' when caption_words <= 7 then 'LB2'
                    when caption_words <= 10 then 'LB3' else 'LB4' end) stored,
                  add column caption_on_s numeric, add column audio_cue_type text, add column product_vis text,
                  add column people_f1 text, add column factor_design text;

create index idx_concepts_product_id on concepts(product_id);
create index idx_executions_concept_id on executions(concept_id);
create index idx_cells_concept_id on cells(concept_id);
create index idx_cells_execution_id on cells(execution_id);
create index idx_ads_concept_id on ads(concept_id);
create index idx_ads_execution_id on ads(execution_id);

-- code validation ------------------------------------------------------------------------------------------
create function private.assert_code(dim text, val text) returns void language plpgsql stable set search_path = '' as $$
begin
  if val is not null and not exists (select 1 from public.codebook c where c.dimension = dim and c.code = val and not c.retired) then
    raise exception 'unknown or retired % code: %', dim, val using errcode = 'check_violation';
  end if;
end $$;

create function private.check_concept_codes() returns trigger language plpgsql set search_path = '' as $$
begin
  perform private.assert_code('angle', new.angle);        perform private.assert_code('buyer_role', new.buyer_role);
  perform private.assert_code('recipient', new.recipient); perform private.assert_code('occasion', new.occasion);
  return new;
end $$;
create function private.check_execution_codes() returns trigger language plpgsql set search_path = '' as $$
begin
  perform private.assert_code('structure', new.structure);   perform private.assert_code('pov', new.pov);
  perform private.assert_code('proof', new.proof);           perform private.assert_code('proof', new.proof_2);
  perform private.assert_code('prod_format', new.prod_format); perform private.assert_code('reveal', new.reveal);
  perform private.assert_code('register', new.register);
  return new;
end $$;
create function private.check_hook_codes() returns trigger language plpgsql set search_path = '' as $$
begin
  perform private.assert_code('format', new.format);         perform private.assert_code('trigger', new.trigger);
  perform private.assert_code('trigger', new.trigger_2);     perform private.assert_code('mechanism', new.mechanism);
  perform private.assert_code('f1_subject', new.f1_subject); perform private.assert_code('shot_size', new.shot_size);
  perform private.assert_code('onset', new.onset);           perform private.assert_code('caption_type', new.caption_type);
  perform private.assert_code('audio_cue', new.audio_cue_type); perform private.assert_code('product_vis', new.product_vis);
  perform private.assert_code('people_f1', new.people_f1);
  return new;
end $$;
create trigger concepts_codes_check   before insert or update on concepts   for each row execute function private.check_concept_codes();
create trigger executions_codes_check before insert or update on executions for each row execute function private.check_execution_codes();
create trigger hooks_codes_check      before insert or update on hooks      for each row execute function private.check_hook_codes();
create trigger codebook_updated_at   before update on codebook   for each row execute function set_updated_at();
create trigger concepts_updated_at   before update on concepts   for each row execute function set_updated_at();
create trigger executions_updated_at before update on executions for each row execute function set_updated_at();

-- access (same allowlist as every other table) -------------------------------------------------------------
alter table codebook   enable row level security;
alter table concepts   enable row level security;
alter table executions enable row level security;
create policy codebook_viewer_read   on codebook   for select to authenticated using ((select private.is_dashboard_viewer()));
create policy concepts_viewer_read   on concepts   for select to authenticated using ((select private.is_dashboard_viewer()));
create policy executions_viewer_read on executions for select to authenticated using ((select private.is_dashboard_viewer()));

-- views -----------------------------------------------------------------------------------------------------
drop view ad_performance;
create view ad_performance with (security_invoker = true) as
select a.*,
       k.name as concept_name, k.angle, k.buyer_role, k.recipient, k.occasion, k.recipient || '×' || k.occasion as cep, k.reason_line,
       x.structure, x.pov, x.proof, x.proof_2, x.prod_format, x.reveal, x.register, x.is_bundle,
       h.arm, h.arm_axis, h.format, h.trigger, h.trigger_2, h.primitives, h.mechanism, h.caption as hook_caption,
       h.f1_subject, h.shot_size, h.onset, h.caption_type, h.caption_band, h.audio_cue_type, h.product_vis, h.people_f1,
       c.round_type, c.axis,
       min(m.date) as first_day, max(m.date) as last_day, count(m.date) as days,
       coalesce(sum(m.impressions),0) as impressions, coalesce(sum(m.spend),0) as spend,
       coalesce(sum(m.link_clicks),0) as link_clicks, coalesce(sum(m.video_3s),0) as video_3s,
       coalesce(sum(m.video_p50),0) as video_p50, coalesce(sum(m.video_p100),0) as video_p100,
       coalesce(sum(m.thruplays),0) as thruplays, coalesce(sum(m.add_to_cart),0) as add_to_cart,
       coalesce(sum(m.purchases),0) as purchases, coalesce(sum(m.purchase_value),0) as purchase_value,
       sum(m.video_3s)::numeric / nullif(sum(m.impressions),0) as hook_rate,
       sum(m.thruplays)::numeric / nullif(sum(m.video_3s),0) as hold_rate,
       sum(m.link_clicks)::numeric / nullif(sum(m.impressions),0) as link_ctr,
       sum(m.spend) / nullif(sum(m.add_to_cart),0) as cost_per_atc,
       sum(m.purchase_value) / nullif(sum(m.spend),0) as roas
from ads a
left join concepts k   on k.concept_id = a.concept_id
left join executions x on x.execution_id = a.execution_id
left join hooks h      on h.hook_id = a.hook_id
left join cells c      on c.cell_id = a.cell_id
left join ad_metrics_daily m on m.ad_key = a.ad_key
group by a.ad_key, k.concept_id, x.execution_id, h.hook_id, c.cell_id;

-- one row per ad x dimension: group results by any code in one query
create view ad_dimension_long with (security_invoker = true) as
select p.ad_key, d.dimension, d.code, p.impressions, p.video_3s, p.thruplays, p.link_clicks, p.spend, p.add_to_cart, p.purchases
from ad_performance p
cross join lateral (values
  ('angle',p.angle),('buyer_role',p.buyer_role),('recipient',p.recipient),('occasion',p.occasion),
  ('structure',p.structure),('pov',p.pov),('proof',p.proof),('prod_format',p.prod_format),('reveal',p.reveal),('register',p.register),
  ('format',p.format),('trigger',p.trigger),('mechanism',p.mechanism),('f1_subject',p.f1_subject),('shot_size',p.shot_size),
  ('onset',p.onset),('caption_type',p.caption_type),('caption_band',p.caption_band),('audio_cue',p.audio_cue_type),
  ('product_vis',p.product_vis),('people_f1',p.people_f1)) as d(dimension, code)
where d.code is not null;

-- aliasing check: how often two codes appear on the same ads (report "X+Y" when they always co-occur)
create view code_cooccurrence with (security_invoker = true) as
select a.dimension as dim_a, a.code as code_a, b.dimension as dim_b, b.code as code_b, count(*) as n_ads
from ad_dimension_long a join ad_dimension_long b on a.ad_key = b.ad_key and a.dimension < b.dimension
group by 1, 2, 3, 4;
