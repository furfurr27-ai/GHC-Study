#!/usr/bin/env python3
"""Guard the Practice Test 2 historical-paper intake and packaged UI."""
import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
assets = root / "app/src/main/assets"
data = json.loads((assets / "practice-test-2.json").read_text(encoding="utf-8"))
page = (assets / "practice-test-2.html").read_text(encoding="utf-8")
index = (assets / "index.html").read_text(encoding="utf-8")
assert "GHC_PRACTICE_TEST_2_LINK" in index
assert index.count("GHC_PRACTICE_TEST_2_LINK") == 1, "Repeated quiz tile injection"
assert 'href=\'practice-test-2.html\'' in index
assert "GHC_QUESTIONS" in index, "Existing quiz bank was damaged"
assert "<!-- PRACTICE_TEST_2_DATA -->" not in page
match = re.search(r'<script type="application/json" id="pt2-data">(.*?)</script>', page, re.DOTALL)
assert match, "Embedded data missing from packaged page"
embedded = json.loads(match.group(1))
assert embedded == data, "Generated page data diverged from authoritative JSON"
assert sum(len(x["questions"]) for x in data["sections"]) == data["receivedQuestionCount"]
if not data["isComplete"]:
    assert data["receivedQuestionCount"] < data["expectedQuestionCount"]
q1 = data["sections"][0]["questions"][0]
assert q1["correct"] == ["a", "c"]
q18 = data["sections"][0]["questions"][17]
assert q18["correct"] == ["b", "c", "d"]
q25 = data["sections"][1]["questions"][24]
assert q25["kind"] == "matching"
assert q25["correct"] == {"a": "5", "b": "4", "c": "6", "d": "2", "e": "1", "f": "3"}
script = page.rsplit("<script>", 1)[1].split("</script>", 1)[0]
result = subprocess.run(["node", "--check"], input=script, text=True, capture_output=True)
assert result.returncode == 0, "Offline page syntax invalid: " + result.stderr
print("PASS: verified", data["receivedQuestionCount"], "historical questions; info bubble; one-point matching; standalone script syntax")
