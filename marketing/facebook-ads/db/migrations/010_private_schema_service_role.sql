-- 010 (2026-11-18): the code-check triggers run as the writer (service_role), which needs the private schema.
grant usage on schema private to service_role;
grant execute on all functions in schema private to service_role;
