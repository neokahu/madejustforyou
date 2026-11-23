#!/usr/bin/env python3
"""check-rules.py: enforce a project's written rules with pattern checks.

Reads harness-rules.json at the project root and reports every line in the matching files
that contains a forbidden pattern. Python 3.8+ standard library only.

Exit codes: 0 clean, 1 violations found, 2 configuration error.
Part of the `harness` skill; see references/rule-checks.md there for the format.
"""
import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".next", "dist", "build",
             ".wrangler", ".pytest_cache", ".idea"}
REQUIRED = ("id", "description", "why", "paths", "pattern", "fix")


def load_rules(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"config error: {path} not found (create it with {{\"rules\": []}})", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"config error: {path} is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)
    rules = data.get("rules")
    if not isinstance(rules, list):
        print(f"config error: {path} needs a top-level \"rules\" list", file=sys.stderr)
        sys.exit(2)
    seen = set()
    for i, r in enumerate(rules):
        missing = [k for k in REQUIRED if not r.get(k)]
        if missing:
            print(f"config error: rule #{i + 1} is missing {', '.join(missing)}", file=sys.stderr)
            sys.exit(2)
        if r["id"] in seen:
            print(f"config error: duplicate rule id {r['id']}", file=sys.stderr)
            sys.exit(2)
        seen.add(r["id"])
        try:
            r["_re"] = re.compile(r["pattern"], re.IGNORECASE if r.get("ignore_case") else 0)
        except re.error as e:
            print(f"config error: rule {r['id']} has a bad regex: {e}", file=sys.stderr)
            sys.exit(2)
    return rules


def matches(rel, patterns):
    for p in patterns:
        if fnmatch.fnmatch(rel, p):
            return True
        # let "**/x" also match "x" at the root
        if p.startswith("**/") and fnmatch.fnmatch(rel, p[3:]):
            return True
    return False


def files_for(root, rule):
    found = set()
    for pattern in rule["paths"]:
        for f in root.glob(pattern):
            if not f.is_file():
                continue
            rel = f.relative_to(root).as_posix()
            if any(part in SKIP_DIRS for part in Path(rel).parts):
                continue
            if matches(rel, rule.get("exclude", [])):
                continue
            found.add(f)
    return sorted(found)


def main():
    ap = argparse.ArgumentParser(description="Check project files against harness-rules.json")
    ap.add_argument("--root", default=".", help="project root (default: current directory)")
    ap.add_argument("--rules", help="rules file (default: <root>/harness-rules.json)")
    ap.add_argument("--only", action="append", help="run only this rule id (repeatable)")
    ap.add_argument("--list", action="store_true", help="list rules and matched file counts")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    rules = load_rules(Path(args.rules) if args.rules else root / "harness-rules.json")
    if args.only:
        unknown = set(args.only) - {r["id"] for r in rules}
        if unknown:
            print(f"config error: unknown rule id(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            sys.exit(2)
        rules = [r for r in rules if r["id"] in args.only]

    if not rules:
        print("check-rules: no rules defined (harness-rules.json is empty); nothing to check")
        return 0

    if args.list:
        for r in rules:
            print(f"{r['id']}: {len(files_for(root, r))} files  ({r['description']})")
        return 0

    total = 0
    for r in rules:
        files = files_for(root, r)
        allow = f"harness-allow: {r['id']}"
        hits = []
        for f in files:
            try:
                lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError as e:
                print(f"warning: cannot read {f}: {e}", file=sys.stderr)
                continue
            for n, line in enumerate(lines, 1):
                if allow in line:
                    continue
                m = r["_re"].search(line)
                if m:
                    hits.append((f.relative_to(root).as_posix(), n, m.group(0)))
        if hits:
            total += len(hits)
            print(f"\nFAIL [{r['id']}] {len(hits)} hit(s) in {len({h[0] for h in hits})} file(s)")
            print(f"  WHAT: {r['description']}")
            print(f"  WHY:  {r['why']}")
            print(f"  FIX:  {r['fix']}")
            for path, n, text in hits[:50]:
                print(f"    {path}:{n}  \"{text}\"")
            if len(hits) > 50:
                print(f"    ... and {len(hits) - 50} more")
        else:
            print(f"PASS [{r['id']}] ({len(files)} files checked)")

    if total:
        print(f"\ncheck-rules: {total} violation(s)")
        return 1
    print("\ncheck-rules: all rules pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
