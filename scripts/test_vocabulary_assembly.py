#!/usr/bin/env python3
"""Verify Jaegersprache1 is an actual selectable Quiz Mode bank, not a footer link."""
import json
from pathlib import Path

root = Path("app/src/main/assets")
s = (root / "index.html").read_text(encoding="utf-8")
source = json.loads((root / "german-vocabulary-quiz.json").read_text(encoding="utf-8"))
marker = "window.GHC_VOCAB_QUESTIONS="
pos = s.index(marker) + len(marker)
bank, _ = json.JSONDecoder().raw_decode(s[pos:])
assert len(bank) == len(source["entries"]) >= 70
assert all(q["sourceGroup"] == "vocabulary" and len(q["choices"]) == 4 for q in bank)
assert all(len({c["text"] for c in q["choices"]}) == 4 for q in bank)
assert set(q["topic"] for q in bank) == set(e["group"] for e in source["entries"])
assert "row('vocabulary','Jägersprache1'" in s
assert "function renderVocabularyScope()" in s
assert "function bindVocabularyScope()" in s
assert "sourceMode()==='vocabulary'?renderVocabularyScope()" in s
assert "sourceMode()==='vocabulary'?VOCAB_QS" in s
assert "kind==='vocab-section'" in s
assert s.count("</body>") == 1
print("PASS: integrated Quiz Mode bank, 4-way answers, five scopes, progress and reset; terms:", len(bank))
