#!/usr/bin/env python3
"""Exercise the Java-embedded Android Back script using only real DOM-exposed state.

The quiz SPA stores view/mode inside an IIFE; those variables must NOT be
injected into this VM or the test would miss the original Android Back bug.
"""
import json
import re
import subprocess
from pathlib import Path

java = Path("app/src/main/java/org/ghcstudy/offline/MainActivity.java").read_text()
block = java.split("final String script = ", 1)[1].split(
    "        webView.evaluateJavascript", 1
)[0].rsplit(";", 1)[0]
fragments = re.findall(r'"(?:\\.|[^"\\])*"', block)
script = "".join(json.loads(part) for part in fragments)
cases = [
    ["modal", "modal", "study", "handled", "modal"],
    ["study card", "card", "studymode", "handled", "category"],
    ["study category", "category", "studymode", "handled", "hub"],
    ["study hub", "hub", "studymode", "handled", "quiz"],
    ["quiz question", "question", "study", "handled", "quiz"],
    ["reference", "reference", "reference", "handled", "quiz"],
    ["quiz root", "root", "study", "root", "none"],
    ["glossary separate page", "glossary", "", "root", "none"],
]
js = r"""
const vm=require('node:vm');
const cases=JSON.parse(process.argv[1]),script=process.argv[2];
for(const [name,screen,tab,expected,action] of cases){
 const calls=[];
 function button(id){return {click:()=>calls.push(id)};}
 const doc={
  getElementById(id){
   if(id==='modal')return {classList:{contains:()=>screen!=='modal'}};
   if(id==='closeModal')return button('modal');
   if(id==='studyCatBack'&&screen==='card')return button('category');
   if(id==='studyHubBack'&&screen==='category')return button('hub');
   return null;
  },
  querySelector(css){
   if(css==='#app [data-action=home]'&&screen==='question')return button('quiz');
   if(css==='.navbtn.active'&&tab)return {getAttribute:()=>tab};
   if(css==='.navbtn[data-tab=study]'&&tab)return button('quiz');
   return null;
  }
 };
 // Critically, do not place "view", "mode", render() or STUDY_CARDS in
 // the global context; the app's actual script captures them in a closure.
 const result=vm.runInNewContext(script,{document:doc});
 if(result!==expected||(action!=='none'&&!calls.includes(action)))
  throw new Error(name+': '+result+' / '+calls.join(',')+' expected '+expected+' '+action);
 console.log('PASS',name);
}
"""
run = subprocess.run(
    ["node", "-e", js, json.dumps(cases), script],
    text=True, capture_output=True
)
print(run.stdout, end="")
if run.returncode:
    print(run.stderr, end="")
    raise SystemExit(run.returncode)
