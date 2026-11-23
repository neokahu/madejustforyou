#!/usr/bin/env bash
# verify.sh: the one command that proves the repo is in a good state. Run before saying "done".
# Exit 0 = pass. Stops at the first failing layer. Read-only: no Meta calls, no reports, no writes.
# Usage: bash scripts/verify.sh
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n== %s\n' "$1"; }
fail() { printf '\nVERIFY FAILED: %s\n' "$1" >&2; exit 1; }

# Layer 1: static checks
step "Layer 1: rules (harness-rules.json)"
python3 scripts/check-rules.py || fail "rule check (fix the hits listed above)"

step "Layer 1: nothing that belongs on Drive or in a keychain is tracked by git"
media=$(git ls-files | grep -iE '\.(png|jpe?g|webp|gif|psd|mp4|mov|webm|mp3|wav|m4a|pdf|zip|ttf|otf|woff2?|heic|ai)$' || true)
[[ -z "$media" ]] || fail "media is tracked (back it up with scripts/backup-media.sh and untrack it):
$media"
secrets=$(git ls-files | grep -E '(^|/)\.env(\.|$)' | grep -vE '\.(example|sample|template)$' || true)
[[ -z "$secrets" ]] || fail "secret files are tracked: $secrets"
echo "ok"

step "Layer 1: every Python script parses"
python3 - <<'PY' || fail "Python syntax errors (listed above)"
import ast, pathlib, subprocess, sys
files = subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True, check=True).stdout.split()
bad = 0
for f in files:
    try:
        ast.parse(pathlib.Path(f).read_text(encoding="utf-8"), filename=f)
    except SyntaxError as e:
        print(f"  {f}:{e.lineno}: {e.msg}"); bad += 1
print(f"ok: {len(files) - bad}/{len(files)} files parse")
sys.exit(1 if bad else 0)
PY

# Layer 2: behaviour
step "Layer 2: FB-ads engine (economics, kill/keep/scale verdicts)"
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s marketing/facebook-ads/engine/tests 2>&1 | tail -3
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s marketing/facebook-ads/engine/tests >/dev/null 2>&1 || fail "engine tests"

step "Layer 2: generation prompt guard still blocks a known-bad prompt"
guard=research/scripts/generation-prompt-guard.py
bad='{"tool_name":"mcp__kie-ai__seedance_2_video","tool_input":{"prompt":"a woman holds the gift and smiles and turns and the camera zooms and pans while flowers bloom"}}'
echo "$bad" | python3 "$guard" | grep -q '"permissionDecision": "deny"' || fail "guard did not block a prompt with no named shots and no constraint"
other='{"tool_name":"Read","tool_input":{"file_path":"x"}}'
[[ -z "$(echo "$other" | python3 "$guard")" ]] || fail "guard reacted to a non-generation tool"
echo "ok: blocks the bad prompt, ignores other tools"

printf '\nVERIFY PASSED\n'
