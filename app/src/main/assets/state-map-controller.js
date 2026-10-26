/* State-first navigation and sourced season overlays for existing Jäger Field Guide.
   This is additive: original field-guide.js and all localStorage namespaces remain intact. */
(function(){
'use strict';
var data=window.GHC_SEASON_DATA,engine=window.GHC_SEASON_ENGINE,map=window.GHC_MAP_SHAPES;
if(!data||!engine)throw Error('Offline state registry or season evaluator unavailable');
var key='ghc-selected-bundesland-v1',chosen=null,mode='map',classes={};
try{var prior=localStorage.getItem(key);if(data.states.some(function(x){return x.code===prior}))chosen=prior}catch(e){}
var nativeBack=window.fieldGuideHandleBack;
var natives=['browse','detail','safety','handbookBrowse','handbookDetail','homeTabs'];
var custom=['stateMapHome','stateHome','seasonsPage','stateRulesPage'];
function el(id){return document.getElementById(id)}
function esc(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function state(){return data.states.find(function(s){return s.code===chosen})}
function species(){return window.GHC_FIELD_SPECIES||[]}
function get(s,klass,date){return engine.evaluate(data,chosen,s.id,klass===undefined?classes[s.id]:klass,date)}
function label(r){return ({
GENERAL_WINDOW_OPEN:'Allgemeine Jagdzeit · General window OPEN',
GENERAL_WINDOW_CLOSED:'Schonzeit · General window CLOSED',
CONDITIONAL:'Bedingt · Conditions / class vary',
UNKNOWN_OR_STALE:'Ungeprüft · Not verified',
PROTECTED_OR_NO_GENERAL_SEASON:'Keine allgemeine Jagdzeit · No general season'
})[r.status]||'Unknown status'}
function css(r){return 'season-'+r.status.toLowerCase().replace(/_/g,'-')}
function dates(r){return r.intervals&&r.intervals.length?r.intervals.map(function(x){return x.join('–')}).join('; '):'conditions vary / unknown'}
function badge(r,detail){
var out='<span class="seasonBadge"><b>'+esc(label(r))+'</b><span>'+esc(r.status==='UNKNOWN_OR_STALE'||r.status==='CONDITIONAL'?'Conditions vary / not verified for class':dates(r))+'</span>';
if(detail)out+='<span> · '+esc(r.reason)+'</span><span>Source: '+esc(r.sourceTitle)+' · Reviewed: '+esc(r.reviewed||'not verified')+' · German date: '+esc(r.date)+'</span>';
return out+'<span> · Not authorization</span></span>';
}
function setMode(next){
mode=next;
custom.forEach(function(id){el(id).classList.toggle('hidden',id!==({map:'stateMapHome',stateHome:'stateHome',seasons:'seasonsPage',stateRules:'stateRulesPage'}[next]))});
var isNative=['browse','detail','handbook','handbookDetail','safety'].includes(next);
if(!isNative)natives.forEach(function(id){el(id).classList.add('hidden')});
el('currentStateBar').classList.toggle('hidden',!chosen||!isNative);
if(isNative){el('currentStateBar').innerHTML='<b>'+esc(state().name)+'</b> · '+esc(engine.germanyToday())+
 ' · Calendar ≠ legal authorization <button type="button" class="chip" id="quickChangeState">Bundesland wechseln</button>';
 el('quickChangeState').onclick=function(){renderMap();setMode('map')};}
window.scrollTo(0,0);
}
function renderMap(){
el('continueState').classList.toggle('hidden',!chosen);
if(chosen)el('continueState').textContent='Continue: '+state().name;
el('stateChoices').innerHTML=data.states.slice().sort(function(a,b){return a.name.localeCompare(b.name,'de')}).map(function(s){
return '<button type="button" class="stateChoice" data-state="'+s.code+'" aria-pressed="'+(s.code===chosen)+'">'+esc(s.name)+'</button>'}).join('');
if(map&&Array.isArray(map.states)&&map.states.length===16){
el('germanyMap').innerHTML='<svg class="stateMapSvg" viewBox="'+esc(map.viewBox)+'" role="group" aria-label="Germany, sixteen selectable Bundesländer">'+map.states.map(function(s){
return '<path class="statePath '+(s.code===chosen?'isSelected':'')+'" data-state="'+s.code+'" d="'+esc(s.d)+'" role="button" tabindex="0" aria-label="'+esc(s.name)+'" aria-pressed="'+(s.code===chosen)+'"><title>'+esc(s.name)+'</title></path>'}).join('')+'</svg>';}
else el('germanyMap').textContent='Vector map unavailable. Use the complete state list.';
el('stateMapHome').querySelectorAll('[data-state]').forEach(function(node){
node.addEventListener('click',function(){choose(this.getAttribute('data-state'))});
if(node.tagName.toLowerCase()==='path')node.addEventListener('keydown',function(e){
if(e.key==='Enter'||e.key===' '){e.preventDefault();choose(this.getAttribute('data-state'))}});
});
}
function choose(code){
if(!data.states.some(function(s){return s.code===code}))return;
chosen=code;classes={};
try{localStorage.setItem(key,code)}catch(e){}
renderStateHome();setMode('stateHome');
}
function renderStateHome(){
if(!chosen)return;
el('stateTitle').textContent=state().name;
el('stateReview').textContent=chosen==='DE-HE'
?'Hessen: 16 animal season entries reviewed against the amended 2026 HJagdV and corrected May 18 table; three remain explicitly unverified. Review: 26 October 2026. Not authorization.'
:'Season rules for '+state().name+' not yet individually verified. All species show UNVERIFIED rather than invented general hunting windows.';
recolor();
}
function renderSeasons(){
el('seasonList').innerHTML=species().map(function(s){
var r=get(s);return '<button type="button" class="seasonEntry '+css(r)+'" data-season-id="'+esc(s.id)+'"><strong>'+esc(s.de)+'</strong><small>'+esc(label(r))+'</small><small>'+esc(r.reviewed||'unverified')+'</small></button>'
}).join('');
el('seasonList').querySelectorAll('[data-season-id]').forEach(function(n){n.onclick=function(){
showNative('browse');window.GHC_FIELD_GUIDE.openCard(n.getAttribute('data-season-id'));setMode('detail');decorateDetail();
}});
}
function renderRules(){
if(chosen!=='DE-HE'){el('stateRulesContent').innerHTML='<p class="alert">Unverified state. No Landesbesonderheiten or hunting seasons have been individually audited for '+esc(state().name)+'. General reference cards remain available.</p>';return}
el('stateRulesContent').innerHTML='<p class="alert">Hessen reviewed 26 October 2026 · HJagdV amendments effective 1 April 2026. This OFFLINE text cannot reflect new local orders. It is not a legal clearance.</p><article><h2>Hessen §2 HJagdV</h2><p>Deer have separate age/sex periods. Female pheasants have no general season. Feldhase and Stockente require sufficient population numbers. Season data are not a substitute for an Abschussplan, Jagdleiter Freigabe, local ASF/ASP orders, protection of dependent young or host permission.</p></article><h2>Legal sources</h2><ul>'+data.hessen.sources.map(function(s){return '<li><a href="'+esc(s.url)+'">'+esc(s.title)+'</a> · '+esc(s.kind)+'</li>'}).join('')+'</ul>';
}
function recolor(){
el('cards').querySelectorAll('[data-open]').forEach(function(node){
var animal=species().find(function(s){return s.id===node.getAttribute('data-open')});if(!animal)return;
var r=get(animal);node.className='tile '+css(r);
node.setAttribute('aria-label','Open '+animal.de+' · '+label(r));
var badgeNode=node.querySelector('.seasonBadge');
if(badgeNode)badgeNode.outerHTML=badge(r,false);
else node.insertAdjacentHTML('beforeend',badge(r,false));
});
}
function decorateDetail(){
var root=el('animalContent'),sheet=root.querySelector('.sheet');if(!sheet||mode!=='detail'||!chosen)return;
var animal=species().find(function(s){return s.id===window.GHC_FIELD_GUIDE_ACTIVE_ID})||
species().find(function(s){return s.de===sheet.querySelector('h1')?.textContent});
if(!animal)return;
var r=get(animal),rule=chosen==='DE-HE'?data.hessen.species[animal.id]:null;
sheet.className='sheet '+css(r);
var choice=rule&&Array.isArray(rule.classes)&&rule.classes.length>1?
'<label for="legalClass">Sex/age class — identify positively</label><select id="legalClass"><option value="">Choose verified class · conditions vary</option>'+
rule.classes.map(function(c){return '<option value="'+esc(c.id)+'" '+(classes[animal.id]===c.id?'selected':'')+'>'+esc(c.label)+'</option>'}).join('')+'</select>':'';
var strip='<section class="seasonStrip '+css(r)+'" aria-label="German general hunting-season information"><strong>'+esc(state().name)+' · '+esc(animal.de)+'</strong>'+choice+badge(r,true)+
'<p>Exceptions: '+esc(r.exceptions)+'</p>'+(r.sourceUrl?'<p><a href="'+esc(r.sourceUrl)+'">HJagdV §2 online</a>'+(r.secondaryUrl?' · <a href="'+esc(r.secondaryUrl)+'">Corrected 18 May 2026 table</a>':'')+'</p>':'')+'</section>';
var old=root.querySelector('.seasonStrip');if(old)old.remove();
sheet.insertAdjacentHTML('afterbegin',strip);
var select=el('legalClass');if(select)select.onchange=function(){classes[animal.id]=this.value||null;decorateDetail()};
}
function showNative(which){
if(which==='browse'||which==='detail'){el('animalsTab').click();setMode(which)}
else {el('handbookTab').click();setMode('handbook')}
recolor();
}
function openSection(which){
if(which==='animals'){showNative('browse');return}
if(which==='seasons'){renderSeasons();setMode('seasons');return}
if(which==='state'){renderRules();setMode('stateRules');return}
var categories={knowledge:'All',methods:'Jagdarten',safety:'Sicherheit',law:'Recht & Wild',after:'Nach dem Schuss'};
if(categories[which]!==undefined){showNative('handbook');el('handbookQuery').value='';el('handbookQuery').dispatchEvent(new Event('input',{bubbles:true}));
var b=el('handbookFilters').querySelector('[data-topic="'+categories[which]+'"]');if(b)b.click();}
}
el('stateSections').querySelectorAll('[data-section]').forEach(function(n){n.onclick=function(){openSection(this.getAttribute('data-section'))}});
el('stateChange').onclick=function(){renderMap();setMode('map')};
el('continueState').onclick=function(){if(chosen){renderStateHome();setMode('stateHome')}};
el('backFromSeasons').onclick=function(){renderStateHome();setMode('stateHome')};
el('backFromStateRules').onclick=function(){renderStateHome();setMode('stateHome')};
el('cards').addEventListener('click',function(e){var node=e.target.closest('[data-open]');if(node){window.GHC_FIELD_GUIDE_ACTIVE_ID=node.getAttribute('data-open');setMode('detail');decorateDetail()}});
el('handbookCards').addEventListener('click',function(e){if(e.target.closest('[data-guide-open]'))setMode('handbookDetail')});
el('backToList').addEventListener('click',function(){setMode('browse');recolor()});
el('backFromHandbook').addEventListener('click',function(){setMode('handbook')});
el('backFromSafety').addEventListener('click',function(){setMode('browse')});
el('showSafety').addEventListener('click',function(){setMode('safety')});
el('animalsTab').addEventListener('click',function(){setMode('browse');recolor()});
el('handbookTab').addEventListener('click',function(){setMode('handbook')});
new MutationObserver(function(){if(chosen)recolor()}).observe(el('cards'),{childList:true});
window.fieldGuideHandleBack=function(){
if(mode==='map')return false;
if(mode==='stateHome'){renderMap();setMode('map');return true}
if(mode==='seasons'||mode==='stateRules'){renderStateHome();setMode('stateHome');return true}
if(mode==='detail'){nativeBack();setMode('browse');recolor();return true}
if(mode==='handbookDetail'){nativeBack();setMode('handbook');return true}
if(mode==='safety'){nativeBack();setMode('browse');return true}
if(mode==='browse'||mode==='handbook'){renderStateHome();setMode('stateHome');return true}
return false;
};
window.GHC_STATE_GUIDE={chooseState:choose,openSection:openSection,seasonFor:function(id,date,klass){
return engine.evaluate(data,chosen,id,klass,date)},getState:function(){return chosen},getPage:function(){return mode}};
renderMap();setMode('map');
})();