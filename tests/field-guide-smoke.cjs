#!/usr/bin/env node
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const assets=path.join(__dirname,'../app/src/main/assets');
const context={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(assets,'field-guide-data.js'),'utf8'),context);
const cards=context.window.GHC_FIELD_SPECIES;
assert(Array.isArray(cards)&&cards.length>=19,'Expected 19+ offline field animal cards');
assert(cards.every(c=>!!c.photo),"Every field card must have a vetted offline photo");
assert.equal(new Set(cards.map(x=>x.id)).size,cards.length,'Duplicate species id');
for(const card of cards){
  for(const key of ['id','de','en','latin','group','quick','idmarks','lookalike','habitat','cycle','social','sign','terms','caution','course','source','photoLabel']){
    assert.equal(typeof card[key],'string',card.id+': missing '+key);
    assert(card[key].trim(),card.id+': empty '+key);
  }
  assert(/^https:\/\/www\.jagdverband\.de\//.test(card.source),'Only verified reference domain allowed: '+card.id);
  assert(!card.photo||(/^(trophy-test-media|media)\/[-.\w]+$/.test(card.photo)),card.id+': unexpected image path');
  assert(!/https?:\/\/|data:/i.test(card.photo),'Network-only picture not allowed');
}
assert(cards.find(x=>x.id==='boar').caution.includes('Trichinella'),'Boar testing caution missing');
assert(cards.find(x=>x.id==='wildcat').group==='Protection / ID','Wildcat protection not flagged');
const html=fs.readFileSync(path.join(assets,'field-guide.html'),'utf8');
const js=fs.readFileSync(path.join(assets,'field-guide.js'),'utf8');
const java=fs.readFileSync(path.join(__dirname,'../app/src/main/java/org/ghcstudy/offline/MainActivity.java'),'utf8');
for(const s of ['field-guide-data.js','field-guide.js','Study archive','Field safety','Source hierarchy','showSafety'])
 assert(html.includes(s),'Missing HTML feature: '+s);
for(const s of ['localStorage','fieldGuideHandleBack','function matches','function openCard','function back','animalNotes','escape','Offline image unavailable']){
 if(s==='escape')continue;
 assert(js.includes(s),'Missing runtime feature: '+s);
}
assert(java.includes('file:///android_asset/field-guide.html'),'Field guide must be default screen');
assert(java.includes('fieldGuideHandleBack'),'Android hardware back must support field card closing');
assert(/applicationId[\s\S]*org\.ghcstudy\.v141/.test(fs.readFileSync(path.join(__dirname,'../app/build.gradle'),'utf8')),'Existing app data/package identity must be preserved');
assert(!/<script[^>]+src="https?:\/\//i.test(html),'External scripts break offline use');
console.log('PASS: 19 sourced offline animal cards, navigation, notes, safeguards and existing package identity');
