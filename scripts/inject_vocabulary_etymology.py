#!/usr/bin/env python3
"""Attach reviewed vocabulary etymology notes to the embedded offline quiz bank."""
import json
import re
from pathlib import Path

root = Path("app/src/main/assets")
p = root / "index.html"
html = p.read_text(encoding="utf-8")
entries = json.loads((root / "german-vocabulary-quiz.json").read_text(encoding="utf-8"))["entries"]
marker = "window.GHC_VOCAB_QUESTIONS="
start = html.index(marker) + len(marker)
questions, length = json.JSONDecoder().raw_decode(html[start:])
assert len(questions) == len(entries), "Vocabulary source and quiz bank have diverged"
used = set()
for q in questions:
    serialized = json.dumps(q, ensure_ascii=False)
    hits = [e for e in entries if re.search(r"(?<!\\w)" + re.escape(e["word"]) + r"(?!\\w)", serialized)]
    if len(hits) != 1:
        raise ValueError("Cannot uniquely identify term in quiz question: " + serialized[:200])
    entry = hits[0]
    assert entry["word"] not in used, "Duplicate vocabulary term"
    used.add(entry["word"])
    note = "Etymology and word meaning: " + entry["etymology"]
    for field in ("explanation", "understanding", "whyCorrect"):
        if field in q and isinstance(q[field], str):
            q[field] += "\\n\\n" + note
            break
    else:
        q["explanation"] = entry["explanation"] + "\\n\\n" + note
assert len(used) == len(entries) == 77
replacement = json.dumps(questions, ensure_ascii=False, separators=(",", ":"))
p.write_text(html[:start] + replacement + html[start + length:], encoding="utf-8")
print("Injected etymology notes into", len(used), "vocabulary questions")
