"""Paths, config files and secrets (~/.global-keys.env; values are never printed)."""
from __future__ import annotations
import json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
KB_FILE = ROOT / "kb" / "faq.json"
LOG_DIR = ROOT / "log"  # gitignored: holds customer text


def load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def support_cfg() -> dict:
    return load_json(CONFIG / "support.json")


def stage_replies() -> dict:
    return {k: v for k, v in load_json(CONFIG / "stage-replies.json").items() if not k.startswith("_")}


def secret(name: str) -> str | None:
    if os.environ.get(name):
        return os.environ[name]
    f = Path.home() / ".global-keys.env"
    if not f.exists():
        return None
    for line in f.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            if k.strip().removeprefix("export ") == name:
                return v.strip().strip('"').strip("'")
    return None


def require(*names: str) -> dict:
    vals = {n: secret(n) for n in names}
    missing = [n for n, v in vals.items() if not v]
    if missing:
        raise SystemExit(f"Missing in ~/.global-keys.env: {', '.join(missing)}")
    return vals
