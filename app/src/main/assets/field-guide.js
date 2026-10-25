(function(){
'use strict';
var species=window.GHC_FIELD_SPECIES||[];
var state={filter:'All',query:'',selected:null,page:'browse'};
var favKey='ghc-field-favorites-v1',notesKey='ghc-field-notes-v1';
function read(key){try{var val=JSON.parse(localStorage.getItem(key)||'{}');return val&&typeof val==='object'&&!Array.isArray(val)?val:{}}catch(e){return {}}}
var favorites=read(favKey),notes=read(notesKey);
function store(key,value){try{localStorage.setItem(key,JSON.stringify(value));return true}catch(e){return false}}
function esc(value){return String(value==null?'':value).replace(/[&<>"']/g,function(x){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]})}
function el(id){return document.getElementById(id)}
function media(s,large){
  var cls=large?'heroPhoto':'photo';
  // All media must be bundled within the APK. Never fetch third-party pictures at runtime.
  if(!s.photo)return '<div class="image-placeholder '+(large?'large':'')+'" role="img" aria-label="Photo not yet packaged"><span>'+esc(s.de.slice(0,2).toUpperCase())+'</span><small>Image to verify / add offline</small></div>';
  return '<img class="'+cls+'" src="'+esc(s.photo)+'" alt="'+esc(s.de)+' — course reference image" loading="'+(large?'eager':'lazy')+'">';
}
function matches(s){
 if(state.filter==='Favorites'&&!favorites[s.id])return false;
 if(state.filter!=='All'&&state.filter!=='Favorites'&&state.filter!==s.group)return false;
 var q=state.query.trim().toLocaleLowerCase();
 if(!q)return true;
 return [s.de,s.en,s.latin,s.group,s.quick,s.terms,s.sign,s.lookalike].join(' ').toLocaleLowerCase().indexOf(q)>-1;
}
function showPane(page){
 state.page=page;
 el('browse').classList.toggle('hidden',page!=='browse');
 el('detail').classList.toggle('hidden',page!=='detail');
 el('safety').classList.toggle('hidden',page!=='safety');
 window.scrollTo(0,0);
}
function paint(){
 var filters=['All','Favorites','Schalenwild','Raubwild','Niederwild','Federwild','Protection / ID'];
 el('filters').innerHTML=filters.map(function(x){return '<button class="chip" data-filter="'+esc(x)+'" aria-pressed="'+(state.filter===x?'true':'false')+'">'+esc(x)+'</button>'}).join('');
 var items=species.filter(matches);
 el('count').textContent=items.length+' of '+species.length+' animal cards · '+species.filter(function(s){return !!s.photo}).length+' with locally packaged picture references';
 el('cards').innerHTML=items.length?items.map(function(s){return '<button class="tile" type="button" data-open="'+esc(s.id)+'" aria-label="Open '+esc(s.de)+' field card">'+media(s,false)+'<span class="txt"><b>'+esc(s.de)+'</b><small>'+esc(s.en)+' · '+esc(s.latin)+'</small><span class="tag">'+esc(s.group)+(favorites[s.id]?' · ★ Saved':'')+'</span></span></button>'}).join(''):'<p>No cards match. Try a shorter German or English term.</p>';
 el('filters').querySelectorAll('[data-filter]').forEach(function(button){button.onclick=function(){state.filter=button.getAttribute('data-filter');paint()}});
 el('cards').querySelectorAll('[data-open]').forEach(function(button){button.onclick=function(){openCard(button.getAttribute('data-open'))}});
}
function row(label,value){return '<dt>'+esc(label)+'</dt><dd>'+esc(value)+'</dd>'}
function openCard(id){
 var s=species.find(function(x){return x.id===id});if(!s)return;
 state.selected=id;
 var src=s.source&&/^https:\/\//.test(s.source)?'<a href="'+esc(s.source)+'" target="_blank" rel="noopener noreferrer">Current DJV species page (online)</a>':'';
 var content='<article class="sheet"><div class="sheetHead"><div class="eyebrow">'+esc(s.group)+' · Field reference</div><h1>'+esc(s.de)+'</h1><p>'+esc(s.en)+' · <i>'+esc(s.latin)+'</i></p></div>'+media(s,true)+'<div class="photoCredit">'+esc(s.photoLabel)+(s.photo?' · mounted/course photo; field appearance may differ':'')+'</div>'+
 '<div class="fact"><button type="button" class="star" id="favorite" aria-pressed="'+(favorites[id]?'true':'false')+'">'+(favorites[id]?'★ Saved':'☆ Save')+'</button>'+
 '<p class="factIntro">'+esc(s.quick)+'</p><dl class="dl">'+
 row('Spotting ID',s.idmarks)+row('Confusion check',s.lookalike)+row('Habitat & food',s.habitat)+row('Annual cycle',s.cycle)+row('Group behavior',s.social)+row('Tracks & signs',s.sign)+row('Jägersprache',s.terms)+'</dl>'+
 '<div class="notice"><strong>Field caution.</strong> '+esc(s.caution)+'</div>'+
 '<div class="source"><b>Evidence & review</b><p>Biological profile reviewed 25 October 2026. '+(s.source==='https://www.jagdverband.de/zahlen-fakten/tiersteckbriefe'?'DJV species directory (individual page not yet checked).':'DJV species reference checked.')+' Source and course information are descriptive; no card grants hunting permission.</p>'+src+'<p>Existing GHC baseline: '+esc(s.course)+' (course source; older or unverified claims do not override current sources).</p></div>'+
 '<div class="noteWrap"><strong>My Revier notes (saved on this device)</strong><p style="font-size:12px">Personal observations only. Local notes are not official rules and may be lost on uninstall/data clearing.</p><label for="animalNotes" class="eyebrow">Field notes</label><textarea id="animalNotes" placeholder="e.g. tracks, habitat, repeated sightings"></textarea><button id="saveNote" class="save" type="button">Save note offline</button><div id="saveStatus" class="status" role="status"></div></div></div></article>';
 el('animalContent').innerHTML=content;
 el('animalNotes').value=notes[id]||'';
 el('favorite').onclick=function(){if(favorites[id])delete favorites[id];else favorites[id]=true;store(favKey,favorites);openCard(id)};
 el('saveNote').onclick=function(){notes[id]=el('animalNotes').value;if(store(notesKey,notes))el('saveStatus').textContent='Saved locally on this device.';else el('saveStatus').textContent='Unable to save. Check device storage.'};
 showPane('detail');
}
function back(){
 if(state.page==='browse')return false;
 showPane('browse');paint();el('query').focus({preventScroll:true});return true;
}
window.fieldGuideHandleBack=back;
el('query').addEventListener('input',function(){state.query=this.value;paint()});
el('backToList').addEventListener('click',back);
el('backFromSafety').addEventListener('click',back);
el('showSafety').addEventListener('click',function(){showPane('safety')});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&state.page!=='browse'){e.preventDefault();back()}});
// Missing or failed files never silently display a wrong animal.
document.addEventListener('error',function(e){var img=e.target;if(img&&img.tagName==='IMG'&&img.closest('.tile, .sheet')){var replacement=document.createElement('div');replacement.className='image-placeholder '+(img.classList.contains('heroPhoto')?'large':'');replacement.setAttribute('role','img');replacement.setAttribute('aria-label','Offline image unavailable');replacement.textContent='Offline image unavailable — verify species from the text';img.replaceWith(replacement)}},true);
window.GHC_FIELD_GUIDE={count:species.length,ids:species.map(function(s){return s.id}),openCard:openCard,back:back};
paint();
})();