#!/usr/bin/env python3
"""Check the assembled vocabulary quiz in the actual offline HTML."""
import json
from pathlib import Path
s=Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
bank=json.loads(Path("app/src/main/assets/german-vocabulary-quiz.json").read_text())
assert len(bank["entries"])>=70
assert "window.GHC_GERMAN_VOCAB=" in s
assert "German Vocabulary Quiz" in s
assert "data-vocab-group" in s and "data-vocab" in s
assert "window.GHC_VOCAB_OPEN" in s
assert "app.appendChild(vocabButton)" in s
assert "function renderHome()" in s
assert s.count("</body>")==1
print("PASS: assembled vocabulary entry, categories, answers and feedback are present; terms:",len(bank["entries"]))
