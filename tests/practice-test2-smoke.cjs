const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');
const assets=path.resolve('app/src/main/assets');
const errors=[];
const vc=new VirtualConsole();
vc.on('jsdomError',e=>errors.push(String(e)));
vc.on('error',e=>errors.push(String(e)));
function click(w,selector){
 const el=w.document.querySelector(selector);
 assert(el,'Missing UI control '+selector);
 el.click();return el;
}
(async()=>{
 const doc=fs.readFileSync(path.join(assets,'practice-test-2.html'),'utf8');
 const dom=new JSDOM(doc,{url:'https://ghc.local/practice-test-2.html',runScripts:'dangerously',virtualConsole:vc,pretendToBeVisual:true,beforeParse(w){w.scrollTo=()=>{}}});
 const w=dom.window;
 await new Promise(resolve=>{if(w.document.readyState==='complete')resolve();else w.addEventListener('load',resolve,{once:true})});
 assert.match(w.document.body.textContent,/Practice Test 2/);
 assert.match(w.document.querySelector('#statusLine').textContent,/105 of 125 questions captured/);
 assert.match(w.document.querySelector('#statusLine').textContent,/100 available to quiz/);
 assert.match(w.document.querySelector('#statusLine').textContent,/5 pending completion/);
 assert.equal(w.document.querySelectorAll('#parts .part').length,4);
 assert(!w.document.querySelector('[data-part="5"]'),'Do not expose incomplete part');
 const data=JSON.parse(w.document.querySelector('#pt2-data').textContent);
 assert.equal(data.pendingSections[0].questions.length,5);
 assert.equal(data.sections[2].questions.length,25);
 assert.equal(data.sections[3].questions.length,25);
 assert(w.document.querySelector('#infoPanel').hidden);
 click(w,'#infoToggle');
 assert(!w.document.querySelector('#infoPanel').hidden);
 assert.match(w.document.querySelector('#infoPanel').textContent,/150 minutes/);
 assert.match(w.document.querySelector('#infoPanel').textContent,/13 out of 25/);
 // Part I Q1: highlighted A and C, not circled-pen marks.
 assert.match(w.document.querySelector('#stem').textContent,/Which answers are correct/);
 assert.equal(w.document.querySelectorAll('#choices input[type=checkbox]').length,4);
 click(w,'#choices input[value=a]');click(w,'#choices input[value=c]');
 click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 assert.equal(w.document.querySelector('#check').disabled,true);
 click(w,'#next');
 assert.match(w.document.querySelector('#stem').textContent,/age of a Rehbock/);
 assert.equal(w.document.querySelectorAll('#choices input[type=radio]').length,3);
 click(w,'#choices input[value=c]');click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 // Switch to independent second-part paper questions.
 click(w,'#parts [data-part="2"]');
 assert.match(w.document.querySelector('#stem').textContent,/Before firing a shot/);
 for(const id of ['a','b','d','e'])click(w,'#choices input[value='+id+']');
 click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 // Part II Q25 is six matches worth a single question.
 for(let n=1;n<25;n++)click(w,'#next');
 assert.match(w.document.querySelector('#stem').textContent,/Match English categories/);
 assert.equal(w.document.querySelectorAll('#choices select').length,6);
 for(const [left,right] of Object.entries({a:'5',b:'4',c:'6',d:'2',e:'1',f:'3'}))w.document.querySelector('#m-'+left).value=right;
 click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 click(w,'#next');
 assert.match(w.document.querySelector('#resultPanel').textContent,/Part 2/);
 assert.match(w.document.querySelector('#resultPanel').textContent,/2 \/ 25/);
 // Part III Q3 is A/B/D from yellow highlights, not handwritten corrections.
 click(w,'#parts [data-part="3"]');
 assert.match(w.document.querySelector('#stem').textContent,/sells his .308W rifle/);
 click(w,'#choices input[value=b]');click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 click(w,'#next');click(w,'#next');
 assert.match(w.document.querySelector('#stem').textContent,/6,5x57R/);
 for(const id of ['a','b','d'])click(w,'#choices input[value='+id+']');
 click(w,'#check');
 assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 // Part III Q4 has a historical answer key which should remain exactly A+B.
 click(w,'#next');
 assert.match(w.document.querySelector('#stem').textContent,/self defense/);
 for(const id of ['a','b'])click(w,'#choices input[value='+id+']');
 click(w,'#check');assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 // Part IV Q2 has two highlighted answers.
 click(w,'#parts [data-part="4"]');
 assert.match(w.document.querySelector('#stem').textContent,/firearm registration forms/);
 click(w,'#next');
 assert.match(w.document.querySelector('#stem').textContent,/hunting year/);
 for(const id of ['c','d'])click(w,'#choices input[value='+id+']');
 click(w,'#check');assert.match(w.document.querySelector('#feedback').textContent,/Correct/);
 const state=JSON.parse(w.localStorage.getItem('GHC_PT2_PARTIAL_PROGRESS_V1'));
 assert.equal(Object.keys(state).length,8,'Separate progress saves eight answered questions');
 dom.window.close();
 // Build-time Quiz Mode tile attaches without modifying original quiz source pool.
 const idx=fs.readFileSync(path.join(assets,'index.html'),'utf8');
 const snippet=idx.match(/<!-- GHC_PRACTICE_TEST_2_LINK -->[\s\S]*?<\/script>/);
 assert(snippet,'New quiz selection snippet packaged');
 const menu=new JSDOM('<!doctype html><html><body><main id="app"><h1>Quiz Mode</h1></main>'+snippet[0]+'</body></html>',{url:'https://ghc.local/',runScripts:'dangerously',virtualConsole:vc});
 await new Promise(resolve=>{if(menu.window.document.readyState==='complete')resolve();else menu.window.addEventListener('load',resolve,{once:true})});
 assert.equal(menu.window.document.querySelectorAll('#ghc-practice-test2-entry').length,1);
 assert.equal(menu.window.document.querySelector('#ghc-practice-test2-entry').getAttribute('href'),'practice-test-2.html');
 menu.window.close();
 assert.equal(errors.length,0,'Browser console errors: '+errors.join('; '));
 console.log('PASS: Practice Test 2 info bubble, Quiz Mode entry, 100-question preview with five pending, highlighted answer checks, matching, progress and results');
})().catch(e=>{console.error(e);process.exitCode=1});
