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
published_count = sum(len(x["questions"]) for x in data["sections"])
pending_count = sum(len(x["questions"]) for x in data.get("pendingSections", []))
assert published_count == data.get("availableQuestionCount", published_count)
assert pending_count == data.get("pendingQuestionCount", 0)
assert published_count + pending_count == data["receivedQuestionCount"]
assert data["receivedQuestionCount"] == 105
assert published_count == 100
assert pending_count == 5
assert [x["part"] for x in data["sections"]] == [1, 2, 3, 4]
assert [x["part"] for x in data["pendingSections"]] == [5]
if not data["isComplete"]:
    assert data["receivedQuestionCount"] < data["expectedQuestionCount"]
q1 = data["sections"][0]["questions"][0]
assert q1["correct"] == ["a", "c"]
q18 = data["sections"][0]["questions"][17]
assert q18["correct"] == ["b", "c", "d"]
q25 = data["sections"][1]["questions"][24]
assert q25["kind"] == "matching"
assert q25["correct"] == {"a": "5", "b": "4", "c": "6", "d": "2", "e": "1", "f": "3"}
# Exact yellow-highlight keys from the 10 photographs in batch 2.
expected_keys = {
    3: ["b", "d", "abd", "ab", "b", "a", "acde", "c", "b", "a",
        "a", "b", "c", "a", "c", "ace", "a", "c", "ab", "b",
        "c", "b", "a", "bd", "abdef"],
    4: ["c", "cd", "b", "b", "b", "a", "b", "a", "ac", "a",
        "a", "c", "b", "c", "b", "a", "b", "b", "c", "abc",
        "b", "b", "a", "a", "b"],
    5: ["b", "abc", "cde", "abe", "ace"],
}
for part_number, expected in expected_keys.items():
    part = next(x for x in data["sections"] + data["pendingSections"] if x["part"] == part_number)
    assert ["".join(q["correct"]) for q in part["questions"]] == expected, (
        f"Source-image yellow highlights changed in Part {part_number}"
    )
assert data["sections"][2]["questions"][3]["correct"] == ["a", "b"], (
    "Part III Q4: preserve highlighted historical self-defense key; review current law separately"
)
assert data["sections"][3]["questions"][15]["correct"] == ["a"], (
    "Part IV Q16: preserve the highlighted historical animal-suffering key"
)
assert "105 of" not in page or "pt2-data" in page
script = page.rsplit("<script>", 1)[1].split("</script>", 1)[0]
result = subprocess.run(["node", "--check"], input=script, text=True, capture_output=True)
assert result.returncode == 0, "Offline page syntax invalid: " + result.stderr
print("PASS: verified", data["receivedQuestionCount"], "historical questions (",
      published_count, "playable /", pending_count, "pending), 55 new yellow keys, info bubble and script syntax")
