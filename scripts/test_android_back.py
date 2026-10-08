#!/usr/bin/env python3
"""Exercise the exact Java-embedded Back JavaScript in a mocked SPA context."""
import json
import re
import subprocess
from pathlib import Path
java=Path("app/src/main/java/org/ghcstudy/offline/MainActivity.java").read_text()
block=java.split('final String script = ',1)[1].split(';\n\n        webView.evaluateJavascript',1)[0]
fragments=re.findall(r'"(?:\\.|[^"\\])*"',block)
script=''.join(json.loads(x) for x in fragments if x != '\"handled\"')
cases=[
  ("modal","study","home","handled","modal"),
  ("study card","studymode","studycard","handled","category"),
  ("study category","studymode","studycategory","handled","hub"),
  ("study hub","studymode","studyhub","handled","home"),
  ("quiz question","study","continue","handled","home"),
  ("reference","reference","home","handled","home"),
  ("root","study","home","root","none")
]
js="""
const vm=require('node:vm');
const cases=JSON.parse(process.argv[1]), script=process.argv[2];
for(const [name,v,m,expected,action] of cases){
 let calls=[];
 const modal={classList:{contains:()=>name!=='modal'}};
 const ctx={
  view:v,mode:m,studyCardId:'x',
  STUDY_CARDS:[{id:'x',category:'animals'}],
  document:{getElementById:(id)=>id==='modal'?modal:id==='closeModal'?{click:()=>calls.push('modal')}:null},
  renderStudyCategory:(id)=>calls.push(id==='animals'?'category':'wrong'),
  renderStudyHub:()=>calls.push('hub'),
  render:()=>calls.push('home')
 };
 const result=vm.runInNewContext(script,ctx);
 if(result!==expected || (action!=='none'&&!calls.includes(action)))
   throw new Error(name+': '+result+' / '+calls.join(',')+' state '+ctx.view+'/'+ctx.mode+' script '+script);
 console.log('PASS',name);
}
"""
proc=subprocess.run(["node","-e",js,json.dumps(cases),script],text=True,capture_output=True)
print(proc.stdout,end="")
if proc.returncode:
    print(proc.stderr,end="")
    raise SystemExit(proc.returncode)
