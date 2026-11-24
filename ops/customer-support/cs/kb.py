"""FAQ knowledge base: kb/faq.json. Keyword match now; the interface (match -> scored hits) stays the same
if it moves to Supabase + embeddings later."""
from __future__ import annotations
import json, re
from dataclasses import dataclass
from .config import KB_FILE

STATUSES = ("needs_answer", "draft", "approved")


def load() -> list[dict]:
    return json.loads(KB_FILE.read_text(encoding="utf-8"))["entries"]


def save(entries: list[dict]) -> None:
    data = json.loads(KB_FILE.read_text(encoding="utf-8"))
    data["entries"] = entries
    KB_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


@dataclass
class Hit:
    entry: dict
    score: float  # 0..1: share of the entry's strongest keywords found, boosted by phrase hits
    matched: list[str]


def _norm(s: str) -> str:
    return " " + re.sub(r"[^a-z0-9#]+", " ", (s or "").lower()) + " "


def match(text: str, entries: list[dict] | None = None, top: int = 3) -> list[Hit]:
    t = _norm(text)
    hits = []
    for e in entries if entries is not None else load():
        kws = e.get("keywords") or []
        found = [k for k in kws if _norm(k) in t]
        if not found:
            continue
        # a multi-word phrase is stronger evidence than one word
        weight = sum(2 if " " in k.strip() else 1 for k in found)
        hits.append(Hit(e, round(min(1.0, weight / 4), 2), found))
    hits.sort(key=lambda h: (-h.score, h.entry["id"]))
    return hits[:top]
