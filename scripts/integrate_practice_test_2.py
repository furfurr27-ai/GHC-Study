#!/usr/bin/env python3
"""Assemble photographed Practice Test 2 as an independent Quiz Mode bank.

Run after the historical question audit overlays, before building/testing the APK.
Never modifies the original 867 keyed exam records or their saved-progress IDs.
"""
import json
from pathlib import Path

HTML = Path("app/src/main/assets/index.html")
ASSETS = HTML.parent
MARKER = '<script id="practice-test-2-batch">'
NOTE = ("Answers follow ONLY the yellow highlights on the user's photographed "
        "practice copy (approximately 2021–2022; exact year not printed). "
        "This historical answer key has not been independently verified for modern "
        "German hunting law, safety rules, or biological accuracy.")

def change(html, old, new):
    count = html.count(old)
    if count != 1:
        raise AssertionError("Practice Test 2 expected one anchor, found " + str(count) + ": " + old[:90])
    return html.replace(old, new, 1)

def load_questions():
    out = []
    for part in range(1, 6):
        p = ASSETS / ("practice-test-2-part" + str(part) + ".json")
        if not p.exists():
            continue  # Later photo batches are pending.
        packet = json.loads(p.read_text(encoding="utf-8"))
        if packet["part"] != part:
            raise AssertionError("Section mismatch " + str(p))
        for q in packet["questions"]:
            if q["section"] != part or q["sourceGroup"] != "practice2022":
                raise AssertionError("Unexpected source/section " + q.get("id", ""))
            if not q["correct"] or not q["choices"]:
                raise AssertionError("Empty answer/choice " + q["id"])
            if q["answerType"] == "matching":
                keys = [x.split(":", 1) for x in q["correct"]]
                if len(keys) != len(q["choices"]) or len(set(k for k, _ in keys)) != len(keys):
                    raise AssertionError("Incomplete matching key " + q["id"])
                if set(k for k, _ in keys) != set(x["id"] for x in q["choices"]):
                    raise AssertionError("Matching keys not on page " + q["id"])
                if any(v not in [x["id"] for x in q["matchChoices"]] for _, v in keys):
                    raise AssertionError("Missing right-hand matching value " + q["id"])
            else:
                if any(c not in [x["id"] for x in q["choices"]] for c in q["correct"]):
                    raise AssertionError("Answer key not present " + q["id"])
                if q["answerType"] != ("multi" if len(q["correct"]) > 1 else "single"):
                    raise AssertionError("Answer input type " + q["id"])
            q["explanation"] = NOTE
            q["learningWhy"] = NOTE
            out.append(q)
    ids = [q["id"] for q in out]
    if len(ids) != len(set(ids)):
        raise AssertionError("Duplicate Practice Test 2 question IDs")
    if len(out) != 50 or [sum(q["section"] == n for q in out) for n in (1, 2)] != [25, 25]:
        raise AssertionError("Batch 1 must contain exactly 25 questions in each of Parts I and II")
    return out

def main():
    qs = load_questions()
    text = HTML.read_text(encoding="utf-8")
    if MARKER in text:
        raise AssertionError("Practice Test 2 already injected; never duplicate")
    payload = json.dumps(qs, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    insert = MARKER + "\nwindow.GHC_PRACTICE2_QUESTIONS=" + payload + ';\nwindow.GHC_SOURCES.push(' + json.dumps({
        "id": "SRC-PRACTICE-2021-22", "type": "course-practice-test",
        "title": "U.S. Forces Hunting Examination — Practice Test 2 (photographed copy)",
        "date": "circa 2021/22 (user estimate, unverified)",
        "notes": "Original question wording and yellow-only highlighted answer selections; 2 of 5 sections received so far."
    }, ensure_ascii=False) + ');\n</script>\n'
    text = change(text, "<script>(function(){\n'use strict';\nvar Q=", insert + "<script>(function(){\n'use strict';\nvar Q=")
    text = change(text, "var Q=(window.GHC_QUESTIONS||[]).concat(window.GHC_VOCAB_QUESTIONS||[]);",
                  "var Q=(window.GHC_QUESTIONS||[]).concat(window.GHC_VOCAB_QUESTIONS||[],window.GHC_PRACTICE2_QUESTIONS||[]);")
    text = change(text, "var PRACTICE_QS=[],FOCUSED_ALL_QS=[]",
                  "var PRACTICE_QS=[],PRACTICE2_QS=[],PRACTICE2_SECTIONS={},FOCUSED_ALL_QS=[]")
    text = change(text, " }else if(iq.sourceGroup==='vocabulary'){\n  VOCAB_QS.push(iq)",
                  " }else if(iq.sourceGroup==='practice2022'){\n  PRACTICE2_QS.push(iq);(PRACTICE2_SECTIONS[iq.section]||(PRACTICE2_SECTIONS[iq.section]=[])).push(iq)\n }else if(iq.sourceGroup==='vocabulary'){\n  VOCAB_QS.push(iq)")
    text = change(text, "var SOURCE_META={\n practice2013:",
                  "var SOURCE_META={\n practice2022:{label:'Practice Test 2',short:'Practice 2',count:PRACTICE2_QS.length,desc:'Photo-based U.S. Forces practice paper, 50 of expected 125 questions'},\n practice2013:")
    text = change(text, "return v==='practice2013'||v==='classroomRelevant'||v==='vocabulary'",
                  "return v==='practice2013'||v==='practice2022'||v==='classroomRelevant'||v==='vocabulary'")
    text = change(text, "FOCUSED_QS[focusSupport()]:PRACTICE_QS)}",
                  "FOCUSED_QS[focusSupport()]:(sourceMode()==='practice2022'?PRACTICE2_QS:PRACTICE_QS))}")
    text = change(text, "key==='classroomRelevant'?FOCUSED_ALL_QS:PRACTICE_QS))}",
                  "key==='classroomRelevant'?FOCUSED_ALL_QS:(key==='practice2022'?PRACTICE2_QS:PRACTICE_QS)))}")
    text = change(text, "var pm=sourceStats('practice2013'),cm=sourceStats('classroomRelevant'),vm=sourceStats('vocabulary'),sel=sourceMode();",
                  "var pm=sourceStats('practice2013'),p2=sourceStats('practice2022'),cm=sourceStats('classroomRelevant'),vm=sourceStats('vocabulary'),sel=sourceMode();")
    text = change(text, "+row('practice2013','Practice Test','100 questions · 5 sections',pm)+row('classroomRelevant'",
                  "+row('practice2013','Practice Test','100 questions · 5 sections',pm)+row('practice2022','Practice Test 2',PRACTICE2_QS.length+' of 125 questions · 2 of 5 sections received',p2)+row('classroomRelevant'")
    addon = r"""
function renderPractice2Scope(){
 function card(id,title,list){var st=progressStats(list);return '<button class="card scope-card progress-card" data-practice2-section="'+attr(id)+'">'+progressFill(st.pct)+'<div class="source-title-row"><h3>'+esc(title)+'</h3><span class="progress-value">'+st.pct+'%</span></div><p>'+list.length+' questions · '+st.mastered+' mastered</p></button>'}
 var html=card('__all__','All available Practice Test 2 Questions',PRACTICE2_QS);
 [1,2,3,4,5].forEach(function(n){if((PRACTICE2_SECTIONS[n]||[]).length)html+=card(String(n),'Part '+n+' · '+PRACTICE2_SECTIONS[n][0].sectionTitle,PRACTICE2_SECTIONS[n])});
 return '<div class="section-title">Quiz scope <button class="btn" style="margin-left:8px;padding:5px 10px" data-practice2-info aria-label="Practice Test 2 information">ⓘ Test instructions</button></div><p class="small" style="color:#e2cda7">Photo batch 1: '+PRACTICE2_QS.length+' of 125 questions available. Remaining parts pending.</p><div class="grid scope-grid">'+html+'</div>'
}
function showPractice2Info(){
 openModal('<h2 id="modalTitle">Practice Test 2 · Exam cover instructions</h2>'+
  '<p><strong>U.S. Forces Hunting Examination</strong> · photocopied practice paper, reported circa 2021–2022 (exact year unverified).</p>'+
  '<p><strong>Closed-book examination.</strong> Use an ink pen to mark answers. For multiple-choice and true/false questions, circle the letter <em>or letters</em> representing your choices.</p>'+
  '<p><strong>Five parts · 25 questions each · 125 questions total.</strong> Each question is worth one point. Minimum passing score is <strong>13 correct answers in EACH part</strong>. Overall exam time limit: <strong>150 minutes</strong>.</p>'+
  '<p><strong>App status:</strong> '+PRACTICE2_QS.length+' questions transcribed across '+Object.keys(PRACTICE2_SECTIONS).length+' parts so far. This app is an untimed study drill, not yet a full timed 125-question exam.</p>'+
  '<div class="note"><strong>Answer-key fidelity:</strong> only the yellow highlighted answers from the supplied photos are treated as correct. Blue pen circles and check marks are NOT the key. Historical keys are not independent confirmation of current rules or science.</div>')
}
function bindPractice2Scope(){
 document.querySelectorAll('[data-practice2-section]').forEach(function(b){b.onclick=function(){var sec=b.getAttribute('data-practice2-section');if(sec==='__all__')startStudy('continue');else startStudy('continue',function(q){return q.section===parseInt(sec,10)})}});
 document.querySelectorAll('[data-practice2-info]').forEach(function(b){b.onclick=showPractice2Info})
}
function renderPractice2MatchChoices(q){
 return '<p class="small">Select the numbered English category for each German term. All six pairs must match for one point.</p>'+
 q.choices.map(function(c){return '<label class="choice p2-match" data-choice="'+attr(c.id)+'"><span><strong>'+esc(c.id.toUpperCase())+'.</strong> '+esc(c.text)+'</span><select data-match="'+attr(c.id)+'" aria-label="Match '+attr(c.text)+'"><option value="">Choose an English category</option>'+q.matchChoices.map(function(t){return '<option value="'+attr(t.id)+'">'+esc(t.id)+'. '+esc(t.text)+'</option>'}).join('')+'</select></label>'}).join('')
}
function bindPractice2Matching(){
 var controls=Array.from(document.querySelectorAll('select[data-match]'));
 document.getElementById('checkBtn').onclick=function(){
  if(checked||controls.some(function(s){return !s.value}))return;
  checked=true;
  var expected={};current.correct.forEach(function(pair){var a=pair.split(':');expected[a[0]]=a[1]});
  var ok=controls.every(function(s){return s.value===expected[s.getAttribute('data-match')]});
  applyResult(current,ok);
  var display=current.correct.map(function(pair){var a=pair.split(':');return a[0].toUpperCase()+'→'+a[1]}).join(', ');
  document.getElementById('feedback').innerHTML='<div class="feedback '+(ok?'ok':'bad')+'">'+(ok?'Correct · all six matches':'Incorrect · Correct matches: '+display)+'</div>';
  controls.forEach(function(s){var id=s.getAttribute('data-match'),l=s.closest('.choice');l.classList.add(s.value===expected[id]?'correct':'wrong');s.disabled=true});
  document.getElementById('checkBtn').classList.add('hidden');
  document.getElementById('understandBtn').classList.remove('hidden');
  document.getElementById('nextBtn').classList.remove('hidden')
 };
 document.getElementById('understandBtn').onclick=showUnderstand;
 document.getElementById('nextBtn').onclick=function(){state.session.lastIds.push(current.id);if(state.session.lastIds.length>8)state.session.lastIds=state.session.lastIds.slice(-8);current=pick(currentFilter,false);selected={};checked=false;renderQuestion()}
}
"""
    text = change(text, "function renderVocabularyScope(){", addon + "\nfunction renderVocabularyScope(){")
    text = change(text, "sourceMode()==='vocabulary'?renderVocabularyScope():renderPracticeScope()",
                  "sourceMode()==='vocabulary'?renderVocabularyScope():sourceMode()==='practice2022'?renderPractice2Scope():renderPracticeScope()")
    text = change(text, "bindSourceChooser();bindFocusChooser();bindPracticeScope();bindVocabularyScope()",
                  "bindSourceChooser();bindFocusChooser();bindPracticeScope();bindVocabularyScope();bindPractice2Scope()")
    text = change(text, "q.sourceGroup==='practice2013'?'Practice Test · Section '",
                  "q.sourceGroup==='practice2022'?'Practice Test 2 · Part '+q.section+' · Q'+q.number:q.sourceGroup==='practice2013'?'Practice Test · Section '")
    start = text.index("function renderQuestion(){")
    end = text.index("function updateChoiceSelection(){", start)
    block = text[start:end]
    before = "'+current.choices.map(function(c){return"
    after = "'+(current.answerType==='matching'?renderPractice2MatchChoices(current):current.choices.map(function(c){return"
    if block.count(before) != 1:
        raise AssertionError("Matching quiz choices anchor not found")
    block = block.replace(before, after, 1)
    if block.count("}).join('')+'</div><div id=\"feedback\"") != 1:
        raise AssertionError("Matching closing anchor not found")
    block = block.replace("}).join('')+'</div><div id=\"feedback\"", "}).join(''))+'</div><div id=\"feedback\"", 1)
    text = text[:start] + block + text[end:]
    text = change(text, "function bindQuestion(){document.querySelectorAll('.choice input')",
                  "function bindQuestion(){if(current.answerType==='matching'){bindPractice2Matching();return}document.querySelectorAll('.choice input')")
    text = change(text, "function showResetMenu(){\nvar practiceSections=",
                  "function showResetMenu(){\nvar practice2Sections=[1,2,3,4,5].filter(function(n){return (PRACTICE2_SECTIONS[n]||[]).length}).map(function(n){return resetChoiceButton('practice2-section','Part '+n+' · '+PRACTICE2_SECTIONS[n][0].sectionTitle,PRACTICE2_SECTIONS[n].length+' questions',null,String(n))}).join('');\nvar practiceSections=")
    text = change(text, "+practiceSections+'</div></details>' +focusedGroup",
                  "+practiceSections+'</div></details>'+'<details class=\"reset-group\"><summary>Practice Test 2</summary><div class=\"reset-list\">'+resetChoiceButton('practice2-all','All Practice Test 2',PRACTICE2_QS.length+' questions')+practice2Sections+'</div></details>' +focusedGroup")
    text = change(text, "else if(kind==='focused-branch'){list=FOCUSED_QS[branch]",
                  "else if(kind==='practice2-all'){list=PRACTICE2_QS;label='all Practice Test 2 progress'}else if(kind==='practice2-section'){var p2n=parseInt(section,10);list=PRACTICE2_SECTIONS[p2n]||[];label='Practice Test 2 Part '+p2n}else if(kind==='focused-branch'){list=FOCUSED_QS[branch]")
    text = change(text, "Practice Test + Direct + Related + Jägersprache1 · ",
                  "Practice Test + Practice Test 2 + Direct + Related + Jägersprache1 · ")
    # Keep correct legacy count descriptions and existing GHC_QUESTIONS untouched.
    text = change(text, "Quiz Mode lets you work the 100-question Practice Test, 767 GHC Focused",
                  "Quiz Mode lets you work the 100-question Practice Test, '+PRACTICE2_QS.length+' Practice Test 2 questions, 767 GHC Focused")
    text = change(text, "Practice Test: 100 questions<br>GHC Focused:",
                  "Practice Test: 100 questions<br>Practice Test 2: '+PRACTICE2_QS.length+' questions (partial photo intake)<br>GHC Focused:")
    HTML.write_text(text, encoding="utf-8")
    print("Practice Test 2 assembled:",len(qs),"new items;",len(text),"HTML characters; legacy 867 questions unchanged")

if __name__ == "__main__":
    main()
