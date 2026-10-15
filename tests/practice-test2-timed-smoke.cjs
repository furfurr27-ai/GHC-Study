const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');

const html=fs.readFileSync(path.resolve('app/src/main/assets/practice-test-2.html'),'utf8');
const data=JSON.parse(html.match(/<script type="application\/json" id="pt2-data">([\s\S]*?)<\/script>/)[1]);
const examKey='GHC_PT2_TIMED_EXAM_V1';
const questions=data.sections.flatMap(s=>s.questions);
const lengthMs=150*60*1000;
const errors=[];
const vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(String(e)));vc.on('error',e=>errors.push(String(e)));
async function page(stored){
 const dom=new JSDOM(html,{url:'https://ghc.local/practice-test-2.html',runScripts:'dangerously',virtualConsole:vc,pretendToBeVisual:true,
   beforeParse(w){w.confirm=()=>true;w.alert=()=>{};w.scrollTo=()=>{};if(stored)w.localStorage.setItem(examKey,JSON.stringify(stored));}});
 const w=dom.window;await new Promise(ok=>{if(w.document.readyState==='complete')ok();else w.addEventListener('load',ok,{once:true})});
 return {dom,w};
}
function click(w,sel){const x=w.document.querySelector(sel);assert(x,'Missing '+sel);x.click()}
function store(w){return JSON.parse(w.localStorage.getItem(examKey)||'null')}
function answersAll(){const result={};for(const q of questions){result[q.id]=q.kind==='matching'?q.correct:[...q.correct]};return result}
function stats(text){return text.replace(/\s+/g,' ').trim()}
(async()=>{
 assert.equal(questions.length,125);
 assert.equal(data.instructions.timeLimitMinutes,150);
 // Start timer and confirm it remains hidden during grading.
 let {dom,w}=await page();
 assert(!w.document.querySelector('#examLauncher').hidden);
 click(w,'#startExam');
 let s=store(w);
 assert.equal(s.endAt-s.startedAt,lengthMs);
 assert.equal(Object.keys(s.answers).length,0);
 assert(!w.document.querySelector('#examArea').hidden);
 assert(w.document.querySelector('#parts').hidden);
 assert.match(w.document.querySelector('#examClock').textContent,/^\d+:\d\d$/);
 assert(!w.document.querySelector('#examChoices').textContent.includes('Paper answer key'));
 click(w,'#examChoices input[value=a]');click(w,'#examChoices input[value=c]');
 click(w,'#examNext');
 s=store(w);
 assert.deepEqual([...s.answers['PT2-P1-Q01']],['a','c']);
 assert.equal(s.index,1);
 assert(!w.document.querySelector('#examChoices').textContent.includes('Correct.'));
 click(w,'#examChoices input[value=c]');
 click(w,'#examPrev');
 assert(w.document.querySelector('#examChoices input[value=a]').checked);
 assert(w.document.querySelector('#examChoices input[value=c]').checked);
 s=store(w);assert.deepEqual(s.answers['PT2-P1-Q02'],['c']);
 const fixedEnd=s.endAt;
 dom.window.close();
 // New WebView page should resume the same question and deadline.
 ({dom,w}=await page(s));
 assert.equal(store(w).endAt,fixedEnd);
 assert.equal(store(w).index,0);
 assert(w.document.querySelector('#examArea').hidden===false);
 assert.match(w.document.querySelector('#examStem').textContent,/Which answers are correct/);
 dom.window.close();
 // Cross-part navigation and matching item should remain one of 125.
 s.index=49;
 ({dom,w}=await page(s));
 assert.match(w.document.querySelector('#examStem').textContent,/Match English categories/);
 assert.equal(w.document.querySelectorAll('#examChoices select').length,6);
 for(const [l,r] of Object.entries({a:'5',b:'4',c:'6',d:'2',e:'1',f:'3'}))w.document.querySelector('#exam-m-'+l).value=r;
 click(w,'#examNext');s=store(w);
 assert.deepEqual(s.answers['PT2-P2-Q25'],{a:'5',b:'4',c:'6',d:'2',e:'1',f:'3'});
 assert.equal(s.index,50);
 assert.match(w.document.querySelector('#examPosition').textContent,/Part 3/);
 dom.window.close();
 // 112 correct in aggregate is still NOT PASSED when Part I only has 12/25.
 const all=answersAll();
 for(const q of data.sections[0].questions.slice(12))delete all[q.id];
 const startOfFailed=Date.now();
 s={version:1,startedAt:startOfFailed,endAt:startOfFailed+lengthMs,index:124,answers:all,submittedAt:null};
 ({dom,w}=await page(s));
 click(w,'#examFinish');
 assert(w.document.querySelector('#examResults').hidden===false);
 assert.match(stats(w.document.querySelector('#examResults').textContent),/112\/125 correct/);
 assert.match(stats(w.document.querySelector('#examResults').textContent),/NOT PASSED/);
 assert.match(stats(w.document.querySelector('#examResults').textContent),/12\/25 correct/);
 assert.equal(store(w).reason,'Submitted');
 assert(w.document.querySelector('#examResults').textContent.includes('historical'));
 dom.window.close();
 // All 125 correct: pass only if all five individual parts pass.
 const startOfPassed=Date.now();
 s={version:1,startedAt:startOfPassed,endAt:startOfPassed+lengthMs,index:124,answers:answersAll(),submittedAt:null};
 ({dom,w}=await page(s));
 click(w,'#examFinish');
 assert.match(stats(w.document.querySelector('#examResults').textContent),/125\/125 correct/);
 assert.match(stats(w.document.querySelector('#examResults').textContent),/PASS/);
 assert.equal((w.document.querySelector('#examResults').textContent.match(/25\/25 correct/g)||[]).length,5);
 dom.window.close();
 // Deadline is wall-clock based; closing and reopening cannot grant more time.
 const expiredAt=Date.now()-5000;
 s={version:1,startedAt:expiredAt-lengthMs,endAt:expiredAt,index:7,answers:{},submittedAt:null};
 ({dom,w}=await page(s));
 assert.equal(store(w).reason,'Time expired');
 assert(w.document.querySelector('#examArea').hidden);
 assert(!w.document.querySelector('#examResults').hidden);
 assert.match(stats(w.document.querySelector('#examResults').textContent),/0\/125 correct/);
 dom.window.close();
 assert.deepEqual(errors,[],'No JSDOM/runtime errors');
 console.log('PASS: full 150-minute Practice Test 2 exam, saved navigation, matching, time expiry, 13/25 per-part pass gate, historical-key reveal only on submission');
})().catch(e=>{console.error(e);process.exitCode=1});
