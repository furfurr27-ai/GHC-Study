/* Practice Test 2: self-contained timed-examination controller.
   Never modifies GHC's legacy question bank or section-practice progress. */
(function(){
"use strict";
const data=JSON.parse(document.getElementById("pt2-data").textContent);
if(!data.isComplete||data.sections.length!==5)return;
const $=id=>document.getElementById(id);
const key="GHC_PT2_TIMED_EXAM_V1";
const quiz=data.sections.flatMap(s=>s.questions.map(q=>({part:s.part,partTitle:s.title,q})));
const limit=data.instructions.timeLimitMinutes*60000;
const esc=s=>String(s).replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
let state=null;
let ticking=null;
try{const s=JSON.parse(localStorage.getItem(key)||"null");
 if(s && s.version===1 && Number.isFinite(s.startedAt) && Number.isFinite(s.endAt) &&
 s.endAt-s.startedAt===limit && s.answers && typeof s.answers==="object" &&
 Number.isInteger(s.index) && s.index>=0 && s.index<quiz.length)state=s;
}catch(_){}
function save(){try{localStorage.setItem(key,JSON.stringify(state));}catch(_){}}
function timeRemaining(){return Math.max(0,(state?state.endAt:0)-Date.now())}
function validate(q,answer){
 if(!answer)return false;
 if(q.kind==="matching")return Object.keys(q.correct).every(k=>answer[k]===q.correct[k]);
 return Array.isArray(answer) && answer.length===q.correct.length &&
 [...answer].sort().every((x,i)=>x===[...q.correct].sort()[i]);
}
function selection(q){
 if(q.kind==="matching"){
   const answer={};
   q.left.forEach(x=>{const v=$("exam-m-"+x.id).value;if(v)answer[x.id]=v});
   return Object.keys(answer).length===q.left.length?answer:null;
 }
 const checked=[...$("examChoices").querySelectorAll("input:checked")].map(x=>x.value).sort();
 return checked.length?checked:null;
}
function persistCurrent(){
 if(!state || state.submittedAt)return;
 const item=quiz[state.index];
 if(!item)return;
 const chosen=selection(item.q);
 if(chosen)state.answers[item.q.id]=chosen;
 else delete state.answers[item.q.id];
 save();
}
function scored(){
 return data.sections.map(s=>{
  let answered=0,correct=0;
  for(const q of s.questions){
   const choice=state.answers[q.id];
   if(choice)answered++;
   if(validate(q,choice))correct++;
  }
  return {part:s.part,title:s.title,answered,correct,total:s.questions.length,pass:correct>=data.instructions.minCorrectPerPart};
 });
}
function closeTicker(){if(ticking!==null){clearInterval(ticking);ticking=null}}
function showClock(){
 if(!state || state.submittedAt)return;
 const ms=timeRemaining();
 const sec=Math.ceil(ms/1000);
 $("examClock").textContent=String(Math.floor(sec/60)).padStart(2,"0")+":"+String(sec%60).padStart(2,"0");
 if(ms===0)finish("Time expired",true);
}
function finish(reason,forced){
 if(!state || state.submittedAt)return;
 if(!forced) {
   const count=Object.keys(state.answers).length;
   const missing=quiz.length-count;
   if(!confirm("Submit your full examination now?"+(missing?" You have "+missing+" unanswered questions.":"")+" This will finalize your score."))return;
 }
 state.submittedAt=Date.now();
 state.reason=reason;
 save();closeTicker();showResults();
}
function showResults(){
 closeTicker();
 const rows=scored();
 const all=rows.every(r=>r.pass);
 const total=rows.reduce((n,r)=>n+r.correct,0);
 $("examArea").hidden=true;
 $("questionPanel").hidden=true;$("resultPanel").hidden=true;
 $("parts").hidden=false;
 $("examLauncher").hidden=false;
 $("startExam").textContent="Start new full exam";
 $("examResults").hidden=false;
 const resultClass=all?"good":"bad";
 let html='<h2>Full exam results — '+esc(state.reason)+'</h2><p class="feedback '+resultClass+'"><strong>'+total+'/125 correct · '+(all?"PASS":"NOT PASSED")+'</strong></p><p>Each of the five parts must reach at least 13/25 correct. A high combined score cannot compensate for a failed part.</p>';
 html+='<div class="parts">'+rows.map(r=>'<div class="part"><strong>Part '+r.part+' — '+(r.pass?"PASS":"NOT PASSED")+'</strong><small>'+r.correct+'/25 correct · '+r.answered+'/25 answered</small></div>').join("")+'</div>';
 html+='<p class="muted">Graded against the yellow-highlighted historical paper, not verified modern legal or food-safety rules.</p>';
 const missed=quiz.filter(it=>!validate(it.q,state.answers[it.q.id]));
 html+='<details><summary>Review '+missed.length+' incorrect or unanswered questions</summary>';
 for(const it of missed){
  let answer;
  if(it.q.kind==="matching")answer=it.q.left.map(x=>x.text+" → "+it.q.right.find(y=>y.id===it.q.correct[x.id]).text).join("; ");
  else answer=it.q.correct.map(id=>id.toUpperCase()).join(", ");
  html+='<p><strong>Part '+it.part+', Q'+it.q.number+': '+esc(it.q.stem)+'</strong><br>Historical highlighted key: '+esc(answer)+'</p>';
 }
 html+='</details>';
 $("examResults").innerHTML=html;
}
function renderQuestion(){
 if(!state || state.submittedAt)return;
 if(timeRemaining()<=0){finish("Time expired",true);return}
 $("examLauncher").hidden=true;
 $("parts").hidden=true;$("questionPanel").hidden=true;$("resultPanel").hidden=true;
 $("examResults").hidden=true;$("examArea").hidden=false;
 const item=quiz[state.index],q=item.q,answer=state.answers[q.id];
 $("examPosition").textContent="Part "+item.part+" · Question "+q.number+" of 25";
 $("examCount").textContent="Full exam question "+(state.index+1)+" of "+quiz.length+" · "+Object.keys(state.answers).length+" responses saved";
 $("examBar").style.width=(100*(state.index+1)/quiz.length)+"%";
 $("examStem").textContent=q.stem;
 if(q.kind==="matching"){
   $("examChoices").innerHTML='<p class="muted">Match each German category to its English meaning; all pairs count as one question.</p>'+
   q.left.map(x=>'<label class="matchRow" for="exam-m-'+x.id+'"><strong>'+x.id.toUpperCase()+'. '+esc(x.text)+'</strong><select id="exam-m-'+x.id+'"><option value="">Choose category</option>'+q.right.map(r=>'<option value="'+r.id+'">'+r.id+'. '+esc(r.text)+'</option>').join("")+'</select></label>').join("");
   if(answer)q.left.forEach(x=>{$("exam-m-"+x.id).value=answer[x.id]||""});
 }else{
   const type=q.kind==="multiple_choice_multiple"?"checkbox":"radio";
   $("examChoices").innerHTML='<p class="muted">'+(type==="checkbox"?"Select all correct answers.":"Select one answer.")+'</p>'+
   q.choices.map(x=>'<label class="choice"><input type="'+type+'" name="examAnswer" value="'+x.id+'"><span><span class="letter">'+x.id.toUpperCase()+'.</span> '+esc(x.text)+'</span></label>').join("");
   if(answer)$("examChoices").querySelectorAll("input").forEach(i=>{i.checked=answer.includes(i.value)});
 }
 $("examPrev").disabled=state.index===0;
 $("examNext").textContent=state.index===quiz.length-1?"Save & review submission":"Save & next";
 showClock();
}
function start(){
 if(!confirm("Start a new 150-minute exam? The full-exam timer begins immediately and continues if you close this screen. Any previous timed-exam result will be replaced. Section-practice progress is unaffected."))return;
 const now=Date.now();
 state={version:1,startedAt:now,endAt:now+limit,index:0,answers:{},submittedAt:null};
 save();
 closeTicker();ticking=setInterval(showClock,1000);
 renderQuestion();
}
$("startExam").onclick=start;
$("examPrev").onclick=()=>{persistCurrent();if(state.index>0)state.index--;save();renderQuestion()};
$("examNext").onclick=()=>{
 persistCurrent();
 if(state.index<quiz.length-1){state.index++;save();renderQuestion()}
 else {save();finish("Submitted",false)}
};
$("examFinish").onclick=()=>{
 persistCurrent();finish("Submitted",false);
};
$("examLauncher").hidden=false;
if(state){
 if(state.submittedAt)showResults();
 else if(timeRemaining()===0)finish("Time expired",true);
 else {ticking=setInterval(showClock,1000);renderQuestion();}
}
})();
