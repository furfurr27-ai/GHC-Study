#!/usr/bin/env python3
"""Assemble an isolated historical Practice Test 2 preview without rewriting quiz banks.

The JSON is authoritative. The existing large index.html is left unchanged in
Git source, while CI inserts a small link in the packaged app. Safe to rerun.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "app/src/main/assets"
DATA = ASSETS / "practice-test-2.json"
INDEX = ASSETS / "index.html"
TEMPLATE = ROOT / "scripts/practice-test2-template.html"
PAGE = ASSETS / "practice-test-2.html"
ANCHOR = "<!-- GHC_PRACTICE_TEST_2_LINK -->"


def validate(data):
    assert data["id"] == "practice-test-2"
    assert data["instructions"]["totalParts"] == 5
    assert data["instructions"]["questionsPerPart"] == 25
    assert data["instructions"]["minCorrectPerPart"] == 13
    assert data["instructions"]["timeLimitMinutes"] == 150
    assert data["expectedQuestionCount"] == 125
    assert not data["isComplete"] or len(data["sections"]) == 5
    assert len(data["sections"]) in range(1, 6)
    ids = set()
    for section in data["sections"]:
        assert len(section["questions"]) == 25, "Only complete photo sections may appear"
        assert section["part"] in range(1, 6)
        for i, q in enumerate(section["questions"], 1):
            assert q["number"] == i
            assert q["id"] not in ids
            ids.add(q["id"])
            assert q["stem"].strip()
            assert q["sourceImage"].endswith(".jpg")
            if q["kind"] == "matching":
                assert len(q["left"]) == len(q["right"]) == 6
                assert {x["id"] for x in q["left"]} == set(q["correct"])
                assert set(q["correct"].values()) == {x["id"] for x in q["right"]}
            else:
                ids_available = {x["id"] for x in q["choices"]}
                assert len(ids_available) == len(q["choices"]) >= 2
                assert set(q["correct"]) <= ids_available
                assert q["correct"]
                if q["kind"] == "multiple_choice_single":
                    assert len(q["correct"]) == 1
                else:
                    assert q["kind"] == "multiple_choice_multiple" and len(q["correct"]) >= 2
    available = len(ids)
    assert available == data.get("availableQuestionCount", available)
    pending = data.get("pendingSections", [])
    assert len(pending) <= 1, "Only one incomplete part may be staged"
    pending_count = 0
    if pending:
        assert not data["isComplete"], "Completed test cannot retain pending questions"
        next_part = len(data["sections"]) + 1
        assert pending[0]["part"] == next_part
        assert 0 < len(pending[0]["questions"]) < 25
        for n, q in enumerate(pending[0]["questions"], 1):
            assert q["number"] == n
            assert q["id"] == f"PT2-P{next_part}-Q{n:02d}"
            assert q["id"] not in ids
            ids.add(q["id"])
            assert q["stem"].strip() and q["sourceImage"].endswith(".jpg")
            assert q["kind"] in ("multiple_choice_single", "multiple_choice_multiple")
            options = [x["id"] for x in q["choices"]]
            assert len(options) == len(set(options)) >= 2
            assert q["correct"] and set(q["correct"]) <= set(options)
            if q["kind"] == "multiple_choice_single":
                assert len(q["correct"]) == 1
            else:
                assert len(q["correct"]) >= 2
            pending_count += 1
    assert pending_count == data.get("pendingQuestionCount", 0)
    assert len(ids) == data["receivedQuestionCount"], "Count in data is stale"
    assert available + pending_count == data["receivedQuestionCount"]
    if data["isComplete"]:
        assert len(data["sections"]) == 5 and len(ids) == data["expectedQuestionCount"]
    return len(ids)


def build():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    count = validate(data)
    template = TEMPLATE.read_text(encoding="utf-8")
    placeholder = "<!-- PRACTICE_TEST_2_DATA -->"
    assert template.count(placeholder) == 1
    # Prevent an exam question from terminating an inline script tag.
    embedded = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = template.replace(placeholder, '<script type="application/json" id="pt2-data">' + embedded + "</script>")
    PAGE.write_text(page, encoding="utf-8")
    html = INDEX.read_text(encoding="utf-8")
    if ANCHOR not in html:
        assert "</body>" in html, "Cannot safely attach Practice Test 2 menu item"
        menu = """<!-- GHC_PRACTICE_TEST_2_LINK -->
<style>
#ghc-practice-test2-entry{display:block;margin:14px 0 20px;padding:15px 17px;background:#243c2e;color:#fff;border:1px solid #668269;border-radius:14px;text-decoration:none;box-shadow:0 3px 12px rgba(0,0,0,.12)}
#ghc-practice-test2-entry strong{display:block;font-size:1.08rem}
#ghc-practice-test2-entry small{display:block;color:#d2decf;margin-top:4px}
</style>
<script>
(function(){
var html='<strong>Practice Test 2 →</strong><small>Historical U.S. Forces exam · QUESTION_COUNT / 125 captured · Study available sections</small>';
function install(){
var root=document.querySelector('#app');
if(!root)return;
var h=Array.from(root.querySelectorAll('h1')).find(function(el){return /quiz mode/i.test(el.textContent)});
if(!h)return;
if(root.querySelector('#ghc-practice-test2-entry'))return;
var a=document.createElement('a');a.id='ghc-practice-test2-entry';
a.href='practice-test-2.html';a.innerHTML=html;
h.insertAdjacentElement('afterend',a);
}
function start(){install();var target=document.querySelector('#app')||document.body;
new MutationObserver(function(){install()}).observe(target,{childList:true,subtree:true});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
})();
</script>
""".replace("QUESTION_COUNT", str(count))
        html = html.replace("</body>", menu + "</body>", 1)
        INDEX.write_text(html, encoding="utf-8")
    print("PASS: Practice Test 2:", count, "transcribed,",
          data.get("availableQuestionCount", count), "playable,", data.get("pendingQuestionCount", 0),
          "pending; packaged entry and local quiz page assembled")


if __name__ == "__main__":
    build()
