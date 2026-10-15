const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM,VirtualConsole} = require('jsdom');
const html=fs.readFileSync(path.resolve('app/src/main/assets/index.html'),'utf8');
const quiz1=JSON.parse(fs.readFileSync('app/src/main/assets/practice-test-2-part1.json','utf8')).questions;
const quiz2=JSON.parse(fs.readFileSync('app/src/main/assets/practice-test-2-part2.json','utf8')).questions;
assert.equal(quiz1.length,25);assert.equal(quiz2.length,25);
const all=quiz1.concat(quiz2);
assert.equal(new Set(all.map(x=>x.id)).size,50);
for(const q of all){assert.equal(q.answerBasis,'yellow-highlight-only');assert(q.correct.length);assert.equal(q.sourceGroup,'practice2022')}
assert.deepEqual(quiz1.find(x=>x.number===7).correct,['a','d']);
assert.deepEqual(quiz1.find(x=>x.number===18).correct,['b','c','d']);
assert.deepEqual(quiz2.find(x=>x.number===1).correct,['a','b','d','e']);
assert.deepEqual(quiz2.find(x=>x.number===16).correct,['a','c','d']);
assert.deepEqual(quiz2.find(x=>x.number===25).correct,['a:5','b:4','c:6','d:2','e:1','f:3']);
function makeDom(preload={}) {
 const errors=[], vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(String(e)));
 const d=new JSDOM(html,{url:'https://ghc.local/',runScripts:'dangerously',resources:'usable',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){
  w.scrollTo=()=>{};w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}});
  w.HTMLElement.prototype.scrollIntoView=function(){};
  if(Object.keys(preload).length)w.localStorage.setItem('ghc-study-progress-v1',JSON.stringify({progress:preload,settings:{sourceMode:'practice2022',focusSupport:'Direct'}}))
 }});
 assert.equal(errors.length,0,errors.join('\n'));
 return d.window;
}
function click(w,selector){const el=w.document.querySelector(selector);assert(el,'Missing: '+selector);el.click();return el;}
const w=makeDom();
assert.equal(w.GHC_QUESTIONS.length,867,'untouched legacy question count');
assert.equal(w.GHC_PRACTICE2_QUESTIONS.length,50,'available new questions');
assert(w.document.querySelector('[data-source="practice2022"]'),'new source card');
click(w,'[data-source="practice2022"]');
const scope=w.document.body.textContent;
assert.match(scope,/Practice Test 2/);
assert.match(scope,/50 of 125 questions/);
click(w,'[data-practice2-info]');
const modal=w.document.querySelector('#modalBody').textContent;
for(const s of ['closed-book','150 minutes','13 correct answers','yellow highlighted'])assert(modal.toLowerCase().includes(s.toLowerCase()),'Exam cover info missing: '+s);
click(w,'#closeModal');click(w,'[data-practice2-section="1"]');
assert.match(w.document.querySelector('.crumb').textContent,/Practice Test 2 · Part 1/);
assert(w.document.querySelector('.choice input'),'normal quiz controls');
assert.equal(w.document.querySelectorAll('.choice input').length>=2,true);
click(w,'.choice input');click(w,'#checkBtn');
assert.match(w.document.querySelector('#feedback').textContent,/Correct|Incorrect/);
click(w,'.backlink');assert(w.document.querySelector('[data-practice2-section="2"]'));
click(w,'.navbtn[data-tab="reference"]');click(w,'[data-action="resetmenu"]');
assert.match(w.document.querySelector('#modalBody').textContent,/Practice Test 2/);
const preload={};
for(const q of all){if(q.id!=='P2022-S2-Q25')preload[q.id]={stage:'mastered',mastery:4,attempts:4,correct:4}}
const m=makeDom(preload);
assert(m.document.querySelector('[data-practice2-section="2"]'),'previously selected Practice Test 2 mode restored');
click(m,'[data-practice2-section="2"]');
assert.match(m.document.querySelector('.crumb').textContent,/Part 2 · Q25/);
const inputs=[...m.document.querySelectorAll('select[data-match]')];
assert.equal(inputs.length,6);
const matching=all.find(q=>q.id==='P2022-S2-Q25');
for(const pair of matching.correct){const [left,right]=pair.split(':');const sel=m.document.querySelector('select[data-match="'+left+'"]');assert(sel);sel.value=right;}
click(m,'#checkBtn');
assert.match(m.document.querySelector('#feedback').textContent,/Correct · all six matches/);
assert.equal(inputs.every(el=>el.disabled),true);
assert(m.document.querySelector('#nextBtn:not(.hidden)'));
console.log('Practice Test 2 smoke PASS: 50 transcriptions, yellow keys, source mode, info, part scope, grading, six-way matching, reset; 867 legacy records unaffected.');
