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
// Regression: the offline Glossary link must use the SAME bottom-ribbon
// icon-above-label layout as the three in-app navigation buttons.
const nav=w.document.querySelector('.bottomnav');
assert(nav,'bottom navigation missing');
const navEntries=Array.from(nav.children);
assert.equal(navEntries.length,4,'four balanced bottom-ribbon destinations');
assert.deepEqual(navEntries.map(el=>el.textContent.trim()),['Quiz Mode','Study Mode','Reference','Glossary']);
assert(navEntries.every(el=>el.classList.contains('navbtn')),'all four entries share navbtn styling');
assert(navEntries.every(el=>!!el.querySelector('.navicon svg[aria-hidden="true"]')),'each entry has the same size icon slot');
assert(navEntries.every(el=>el.querySelectorAll('span').length===2),'each entry has icon and label in separate spans');
const glossaryButton=nav.querySelector('a.navbtn.glossary-nav[href="glossary.html"]');
assert(glossaryButton,'Glossary remains an offline link rather than breaking navigation');
assert.equal(glossaryButton.getAttribute('aria-label'),'Open Jägersprache glossary');
assert.equal(glossaryButton.onclick,null,'offline Glossary link must not get an in-app tab click handler');
assert(nav.querySelectorAll('.navbtn[data-tab]').length===3,'only three buttons should be in-app tabs');
const referenceButton=nav.querySelector('button.navbtn[data-tab="reference"]');
const gs=w.getComputedStyle(glossaryButton),rs=w.getComputedStyle(referenceButton);
for(const property of ['display','flexDirection','alignItems','justifyContent','fontSize','fontWeight','gap','color']){
 assert.equal(gs[property],rs[property],'Glossary bottom-ribbon style mismatch: '+property);
}
assert.equal(gs.borderLeftWidth,rs.borderLeftWidth,'Glossary must not retain old divider border');
assert.equal(gs.textDecorationLine||'none','none','Glossary should not look like an underlined link');
assert.equal(w.GHC_QUESTIONS.length,867,'stable question bank');
assert.equal(w.GHC_STUDY_CARDS.length,117,'study card count');
assert.equal(w.GHC_VOCAB_QUESTIONS.length,77,'vocabulary count');
const fixedQuestion=w.GHC_QUESTIONS.find(q=>q.id==='H2023-D19-Q042');
assert(fixedQuestion,'fixed Hessen question must exist');
assert.equal(Array.from(fixedQuestion.correct).join(','),'b','Hessen source answer must not change');
assert(!/Jagdschein\s*\(hunting license\)/i.test(fixedQuestion.stem),'question stem must not give away license translation');
assert(!/hunting license/i.test(fixedQuestion.stem),'correct choice must not be repeated in question stem');
for(const id of ['H2023-D04-Q151','H2023-D15-Q010']){
 const item=w.GHC_QUESTIONS.find(q=>q.id===id);
 assert(item,'missing duplicate range safety question '+id);
 assert.equal(item.stem,'Must shooters follow the instructions of the person supervising the shooting range?');
}
for(const id of ['H2023-D09-Q083','H2023-D15-Q003']){
 const item=w.GHC_QUESTIONS.find(q=>q.id===id);
 assert(item,'missing duplicate trapping question '+id);
 assert.equal(item.stem,'Which of these traps is designed to capture game alive and unharmed?');
}

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
click(w,'.navbtn[data-tab="studymode"]');click(w,'[data-study-cat="othergame"]');click(w,'[data-study-card="marmot"]');
assert.match(w.document.querySelector('.study-historical-note').textContent,/Historical U.S. Forces course-guide reference \(2013\)/);
click(w,'#studyCatBack');click(w,'[data-study-card="seal"]');
assert.match(w.document.querySelector('.study-historical-note').textContent,/historical/);
click(w,'.navbtn[data-tab="reference"]');
assert(w.document.querySelector('a[href="glossary.html"]'),'reference glossary link');
click(w,'[data-action="resetmenu"]');assert(!w.document.querySelector('#modal').classList.contains('hidden'),'reset dialog opens');
click(w,'#closeModal');assert(w.document.querySelector('#modal').classList.contains('hidden'),'reset dialog closes');
assert.equal(a.errors.length,0,'base app script/runtime errors: '+a.errors.join(' | '));a.dom.window.close();
const b=domFile('glossary.html');const g=b.dom.window;await loaded(g);
assert.equal(g.document.querySelectorAll('article').length,162,'all glossary entries');
assert.equal(g.GHC_GLOSSARY.filter(x=>x.status==='defined').length+g.GHC_GLOSSARY.filter(x=>x.status==='pending').length,162,'every glossary term classified');
assert(g.document.body.textContent.includes('Rehwild'));
const search=g.document.querySelector('#search');search.value='Rehwild';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert(g.document.querySelectorAll('article').length>=1,'search finds German term');
const results=g.document.querySelectorAll('article');assert([...results].some(x=>x.textContent.includes('Roe deer')));
search.value='';search.dispatchEvent(new g.Event('input',{bubbles:true}));
const filter=g.document.querySelector('#status');filter.value='defined';filter.dispatchEvent(new g.Event('change',{bubbles:true}));assert.equal(g.document.querySelectorAll('article').length,g.GHC_GLOSSARY.filter(x=>x.status==='defined').length,'defined filter');
filter.value='pending';filter.dispatchEvent(new g.Event('change',{bubbles:true}));assert.equal(g.document.querySelectorAll('article').length,g.GHC_GLOSSARY.filter(x=>x.status==='pending').length,'pending filter');
filter.value='all';filter.dispatchEvent(new g.Event('change',{bubbles:true}));
search.value='Affe';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Young marmot')),'historical Affe sense');
search.value='Katz';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Female marmot')),'historical Katz sense');
search.value='Drilling';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Three-barrel combination gun')),'class-backed Drilling definition');
for(const [term,meaning] of [['Brucellose','Brucellosis'],['Schweinepest','Classical swine fever'],['Fuchsbandwurm','Fox tapeworm'],['Kleiner Muensterlaender','Small Münsterländer'],['Hahn in Ruh','Cease-fire'],['Untere Jagdbehoerde','Lower (local) hunting authority'],['Jagdschein','Hunting license'],['Wiederkäuer','Ruminant'],['Frettieren','ferreting']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing class-backed glossary definition for '+term);
}
for(const [term,meaning] of [['Absehen','Reticle'],['Kugelfang','Backstop'],['Objektiv','Objective lens'],['Okular','Eyepiece'],['Streckeplatz','game is laid out'],['Visier','Sight']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing new source-attributed glossary definition for '+term);
}
for(const [term,meaning] of [['Leberegel','Liver flukes'],['Jagende Hunde','Hounds']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing direct bilingual course definition for '+term);
}
for(const [term,meaning] of [['Bestaetigter Jagdaufseher','Appointed/confirmed hunting supervisor'],['Erleger bruch',"Shooter's branch"]]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing provenance-labeled contextual GHC meaning for '+term);
}
for(const [term,meaning] of [['Pelz','Fur or pelt'],['Baum','Baummarder'],['Stein','Steinmarder']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing class-context glossary definition for '+term);
}
for(const [term,meaning] of [['Bundesverwaltungsamt','Federal Office of Administration'],['Europaeischen Feuerwaffenpass','European Firearms Pass'],['Veterinaeramt','District veterinary authority']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing official-authority glossary definition for '+term);
}
for(const [term,meaning] of [['Epagneul Breton','Brittany Spaniel'],['Blindschleiche','Slow worm'],['Kreuzotter','European adder'],['Borkenkaefer','Bark beetle']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing externally attributed glossary definition for '+term);
}
assert.equal(g.GHC_GLOSSARY.filter(x=>x.status==='defined').length,160,'160 source-defined glossary entries');
assert.equal(g.GHC_GLOSSARY.filter(x=>x.status==='pending').length,2,'2 unresolved glossary entries');
for(const [term,meaning] of [['Einwachser-Mufflon','Mouflon ram with inward-growing horns'],['Stangensulze','Post-mounted salt lick']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing source-qualified hunting glossary meaning for '+term);
}
const undefinedTerms=Array.from(g.GHC_GLOSSARY.filter(x=>x.status==='pending'),x=>x.term).sort();
assert.deepEqual(undefinedTerms,['Jagdschuetz','Tiroler'].sort(),'Only two contextual worksheet headwords should remain pending');
search.value='Abschussgebuehr';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Fee charged per game animal harvested')),'Missing source-qualified contracted hunting fee translation');
assert(g.GHC_GLOSSARY.find(x=>x.id==='x100').etymology==='', 'Do not add invented Einwachser history');
assert(g.GHC_GLOSSARY.find(x=>x.id==='x144').etymology==='', 'Do not add invented Stangensulze history');
search.value='Haken';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('female wild boar')),'Missing multi-sense Haken trophy definition');

search.value='Bergstutzen';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Two-barrel break-action rifle')),'Missing externally verified Bergstutzen definition');

for(const [term,meaning] of [['Wildretter','Wildlife rescuer'],['Hirschlaus','European deer ked'],['Marienkaefer','Ladybird beetle']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing new DJV/university/dictionary glossary meaning for '+term);
}
for(const [term,meaning] of [['Wolfssprosse','Wolf tine'],['Fuehrende','Female game animal accompanied by dependent young']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing source-attributed hunting term '+term);
}
search.value='Moderhinke';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes('Footrot')),'Missing veterinary-source footrot translation');

for(const [term,meaning] of [['Wechselwild','Transient game moving between hunting grounds'],['Wildwechsel','Regularly used wildlife trail or crossing']]){
 search.value=term;search.dispatchEvent(new g.Event('input',{bubbles:true}));
 assert([...g.document.querySelectorAll('article')].some(a=>a.textContent.includes(meaning)),'Missing distinct Hessen/Duden glossary definition for '+term);
}
assert(g.GHC_GLOSSARY.find(x=>x.term==='Wechselwild').related.includes('x160'),'Wechselwild cross-references Wildwechsel');
assert(g.GHC_GLOSSARY.find(x=>x.term==='Wildwechsel').related.includes('x156'),'Wildwechsel cross-references Wechselwild');
search.value='';search.dispatchEvent(new g.Event('input',{bubbles:true}));
const inheritedOrigins=Array.from(g.GHC_GLOSSARY).filter(x=>typeof x.etymology==='string'&&x.etymology.trim().length>0);
assert.equal(inheritedOrigins.length,77,'exactly 77 inherited origin/breakdown notes must remain in data');
assert(inheritedOrigins.every(x=>x.id.startsWith('v')),'all 77 inherited word-origin notes must retain their IDs');
const verifiedOrigins=inheritedOrigins.filter(x=>x.originVerification==='verified'&&typeof x.originSource==='string'&&x.originSource.trim());
assert.deepEqual(verifiedOrigins.map(x=>x.id),['v047','v064'],'only individually cited Schweiß/Schweißhund word origins verified');
assert(verifiedOrigins.every(x=>/duden\.de/.test(x.originSource)),'verified word-origin field requires an attributable dictionary source');
assert.equal(g.document.querySelectorAll('article .origin-unverified').length,75,'75 unverified word origins must be labeled individually in the rendered glossary');
assert.equal(g.document.querySelectorAll('article .origin-verified').length,2,'the two independently sourced word origins must be labeled individually');
assert.match(g.document.querySelector('#summary').textContent,/160 meanings available, 2 meanings pending.*75 inherited origin notes unverified/,'live source-status counts must not be stale');
assert(!g.document.querySelector('footer').textContent.includes('55 worksheet-only'),'historical footer counts must not linger');
search.value='Schweiß';search.dispatchEvent(new g.Event('input',{bubbles:true}));
const bloodTerm=Array.from(g.document.querySelectorAll('article')).find(x=>x.querySelector('.term')?.textContent==='Schweiß');
assert(bloodTerm&&bloodTerm.querySelector('.origin-verified')?.textContent.includes('not proof that poachers invented a secret code'),'Schweiß history must distinguish documented taboo usage from unsupported poacher-code narrative');
assert(bloodTerm.textContent.includes('gfds.de'),'Schweiß historical sense must display independent language-authority attribution');
search.value='Schweißhund';search.dispatchEvent(new g.Event('input',{bubbles:true}));
const trackingDog=Array.from(g.document.querySelectorAll('article')).find(x=>x.querySelector('.term')?.textContent==='Schweißhund');
assert(trackingDog?.querySelector('.origin-verified')?.textContent.includes('Compound meaning is verified'),'Schweißhund must carry only verified compound etymology scope');
search.value='';search.dispatchEvent(new g.Event('input',{bubbles:true}));
assert(g.document.querySelectorAll('.related a').length>0,'cross-links rendered');
assert.equal(b.errors.length,0,'glossary script errors: '+b.errors.join(' | '));b.dom.window.close();
console.log('PASS app: quiz launch/answer, categories/cards/back, reference/reset, offline glossary search/filter/links, persistent data totals');
})().catch(e=>{console.error(e);process.exitCode=1});