const assert=require('node:assert/strict');
const fs=require('node:fs');const path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');
const base=path.resolve('app/src/main/assets');
function domFile(name,opts={}){const errors=[];const vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(String(e)));vc.on('error',e=>errors.push(String(e)));const url=name==='glossary.html'?'file://'+path.join(base,name):'https://ghc.local/';const dom=new JSDOM(fs.readFileSync(path.join(base,name),'utf8'),{url,runScripts:'dangerously',resources:'usable',pretendToBeVisual:true,virtualConsole:vc,beforeParse(win){win.scrollTo=()=>{};win.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});return{dom,errors}}
function click(w,sel){const x=w.document.querySelector(sel);assert(x,sel+' missing');x.click();return x}
async function loaded(w){if(w.document.readyState==='complete')return;await new Promise(resolve=>w.addEventListener('load',resolve,{once:true}))}
(async()=>{
const a=domFile('index.html');const w=a.dom.window;await loaded(w);
assert.match(w.document.querySelector('h1').textContent,/Quiz Mode/);
assert(w.document.querySelector('a[href="glossary.html"]'),'navigation link');
assert.equal(w.GHC_QUESTIONS.length,867,'stable question bank');
assert.equal(w.GHC_STUDY_CARDS.length,117,'study card count');
assert.equal(w.GHC_VOCAB_QUESTIONS.length,77,'vocabulary count');
click(w,'[data-source="classroomRelevant"]');
assert(w.document.querySelector('[data-focus-support="Direct"]'));
assert(w.document.querySelector('[data-focus-support="Related"]'));
click(w,'[data-focus-section="__all__"]');
assert(w.document.querySelector('.question h2'),'quiz question rendered');
const input=w.document.querySelector('.choice input');
assert(input,'answer input');input.click();click(w,'#checkBtn');
assert(w.document.querySelector('#feedback').textContent.trim().length>0,'feedback generated');
click(w,'.navbtn[data-tab="studymode"]');click(w,'[data-study-cat="schalenwild"]');click(w,'[data-study-card="roe"]');
assert.match(w.document.querySelector('.study-detail').textContent,/Rehwild/);
assert.match(w.document.querySelector('.study-detail').textContent,/Other Facts/);
assert(w.document.querySelector('.study-photo img'),'study image present');
click(w,'#studyCatBack');assert(w.document.querySelector('[data-study-card="roe"]'),'card back returns category');
click(w,'.navbtn[data-tab="reference"]');
assert(w.document.querySelector('a[href="glossary.html"]'),'reference glossary link');
click(w,'[data-action="resetmenu"]');assert(!w.document.querySelector('#modal').classList.contains('hidden'),'reset dialog opens');
click(w,'#closeModal');assert(w.document.querySelector('#modal').classList.contains('hidden'),'reset dialog closes');
assert.equal(a.errors.length,0,'base app script/runtime errors: '+a.errors.join(' | '));a.dom.window.close();
const b=domFile('glossary.html');const g=b.dom.window;await loaded(g);
assert.equal(g.document.querySelectorAll('article').length,162,'all glossary entries');
assert(g.document.body.textContent.includes('Rehwild'));
const search=g.document.querySelector('#search');search.value='Rehwild';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert(g.document.querySelectorAll('article').length>=1,'search finds German term');
const results=g.document.querySelectorAll('article');assert([...results].some(x=>x.textContent.includes('Roe deer')));
search.value='';search.dispatchEvent(new g.Event('input',{bubbles:true}));
const filter=g.document.querySelector('#status');filter.value='defined';filter.dispatchEvent(new g.Event('change',{bubbles:true}));assert.equal(g.document.querySelectorAll('article').length,109,'defined filter');
filter.value='pending';filter.dispatchEvent(new g.Event('change',{bubbles:true}));assert.equal(g.document.querySelectorAll('article').length,53,'pending filter');
filter.value='all';filter.dispatchEvent(new g.Event('change',{bubbles:true}));
assert(g.document.querySelectorAll('.related a').length>0,'cross-links rendered');
assert.equal(b.errors.length,0,'glossary script errors: '+b.errors.join(' | '));b.dom.window.close();
console.log('PASS app: quiz launch/answer, categories/cards/back, reference/reset, offline glossary search/filter/links, persistent data totals');
})().catch(e=>{console.error(e);process.exitCode=1});