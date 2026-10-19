#!/usr/bin/env node
'use strict';
// Offline contract tests: no npm packages or network required.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const source=fs.readFileSync(path.join(root,'app/src/main/assets/schalenwild-matrix.js'),'utf8');
const css=fs.readFileSync(path.join(root,'app/src/main/assets/schalenwild-matrix.css'),'utf8');
const anchor="  if (document.readyState === 'loading')";
assert(source.includes(anchor),'matrix initialization anchor must exist');
const instrumentation="  globalThis.__matrixTest = {SPECIES,CYCLE_DATA,IDENT_DATA,tableHtml,comparisonMarkup,markup,switchView,escapeHtml};\n";
const context={
  document:{readyState:'loading',addEventListener:()=>{}},
  MutationObserver:class MutationObserver {}
};
vm.runInNewContext(source.replace(anchor,instrumentation+anchor),context,{filename:'schalenwild-matrix.js',timeout:1500});
const m=context.__matrixTest;
assert(m,'matrix functions are available in test context');
const names=['Rehwild','Rotwild','Schwarzwild','Damwild','Sikawild','Gamswild','Muffelwild'];
for(const dataset of [m.SPECIES,m.CYCLE_DATA,m.IDENT_DATA]){
  assert.deepEqual(Array.from(dataset,z=>z.de),names,'same seven species/order across matrix views');
}
assert.deepEqual(Array.from(m.IDENT_DATA,z=>z.teeth),['32','34','44','32','34','32','32'],'GHC tooth count values');
assert.deepEqual(Array.from(m.IDENT_DATA,z=>z.digest==='Non-ruminant'),[false,false,true,false,false,false,false],'wild boar is only non-ruminant');
assert.deepEqual(Array.from(m.IDENT_DATA,z=>z.className==='Niederwild'),[true,false,false,false,false,false,false],'roe deer is only Niederwild');
assert.equal(m.SPECIES.find(x=>x.de==='Gamswild').gest,'20–21 wk*','preserve disputed Gamswild course figure');
assert.equal(m.CYCLE_DATA.find(x=>x.de==='Rotwild').shed,'Spring (first head)','keep age qualifier');
assert.equal(m.CYCLE_DATA.find(x=>x.de==='Muffelwild').shed,'Never','horn is permanent');
assert(m.markup().includes('Schalenwild · Vergleichsmatrizen'));
assert.equal((m.tableHtml().match(/<tr><th scope="row"/g)||[]).length,7,'calendar rows');
for(const view of ['antlers','identification']){
  const html=m.comparisonMarkup(view);
  assert.equal((html.match(/<tr><th scope="row"/g)||[]).length,7,view+' seven rows');
  assert(html.includes('ghc-matrix-scroll'),'comparison can scroll horizontally');
}
assert(m.comparisonMarkup('antlers').includes('Krucken (horns)'));
assert(m.comparisonMarkup('antlers').includes('Schnecken (horns)'));
assert(m.comparisonMarkup('identification').includes('Grandeln'));
assert.equal(m.escapeHtml('<>&"'), '&lt;&gt;&amp;&quot;','escape injected text');

function fakeElement(kind,name){
  return {name,hidden:false,tabIndex:0,attrs:{[kind]:name},
    getAttribute(k){return this.attrs[k];},
    setAttribute(k,v){this.attrs[k]=v;}
  };
}
const buttons=names.slice(0,3).map((_,i)=>fakeElement('data-matrix-view',['reproduction','antlers','identification'][i]));
const panels=names.slice(0,3).map((_,i)=>fakeElement('data-matrix-panel',['reproduction','antlers','identification'][i]));
const dom={querySelectorAll(selector){
  if(selector==='[data-matrix-view]')return buttons;
  if(selector==='[data-matrix-panel]')return panels;
  return [];
}};
m.switchView(dom,'identification');
assert.equal(buttons[2].attrs['aria-selected'],'true');
assert.equal(buttons[2].tabIndex,0);
assert.equal(buttons[0].attrs['aria-selected'],'false');
assert.equal(panels[0].hidden,true);
assert.equal(panels[2].hidden,false);
m.switchView(dom,'reproduction');
assert.equal(panels[0].hidden,false);
assert.equal(panels[2].hidden,true);
assert(css.includes('.ghc-matrix-panel[hidden]'),'hidden panel rule');
assert(css.includes('.ghc-matrix-view-tabs'),'tab stylesheet');
assert(source.includes("addComparisonViews(wrapper)"),'existing Schalenwild category mount retained');
console.log('PASS: Schalenwild matrix views, source fact contract, rendering, selection and CSS');
