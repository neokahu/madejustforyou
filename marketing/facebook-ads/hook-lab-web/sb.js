// Shared Supabase client for Hook Lab (publishable key: safe in the browser; RLS allowlist guards the data).
window.HL_SB = supabase.createClient("https://bjplojqovxetmbchzzms.supabase.co", "sb_publishable_nDRL2Boaf59NDxVd85BvHQ_3m0EzrRI",
  {auth: {persistSession: true, autoRefreshToken: true}});
