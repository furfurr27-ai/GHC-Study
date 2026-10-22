(function(){
'use strict';
var data=window.GHC_TROPHY_CARDS||[];
var known=data.filter(function(c){return c.certainty==='identified'});
var mode='cards',filter='All',selected=data[0]||null,shown=false,queue=[],current=null,answers=[],answered=false,round={tried:0,right:0};
var key='ghc-trophy-test-progress-v1',progress={};
try{progress=JSON.parse(localStorage.getItem(key)||'{}')||{}}catch(e){progress={}}
var root=document.getElementById('content'),stats=document.getElementById('stats');
function clean(s){return String(s==null?'':s).replace(/[&<>"']/g,function(x){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]})}
function save(){try{localStorage.setItem(key,JSON.stringify(progress))}catch(e){}}
function touch(id,ok){var p=progress[id]||{tries:0,right:0,streak:0};p.tries++;if(ok){p.right++;p.streak++}else p.streak=0;progress[id]=p;save()}
function cardMarkup(c,hidden){if(!c)return '<p class="empty">No specimens available.</p>';
var heading=hidden?'Identify this mounted specimen':clean(c.de),en=hidden?'Reveal its identity when ready':clean(c.en);
return '<article class="card" data-card="'+clean(c.id)+'"><div class="heading"><span class="kicker">'+clean(c.group)+' · Exam-room trophy photo</span><h2>'+heading+'</h2><div class="en">'+en+'</div></div>'+
'<figure><img src="trophy-test-media/'+clean(c.id)+'.jpg" alt="Actual mounted animal from the German Hunting Course examination room" loading="eager"><figcaption>Exam-room photo · source '+clean(c.photo)+' · cropped to the mount</figcaption></figure>'+
(hidden?'':'<div class="facts"><span class="key">Spot it in the room</span><p>'+clean(c.cue)+'</p><span class="key">Avoid confusion</span><p>'+clean(c.contrast)+'</p>'+(c.certainty==='review'?'<div class="review">Exact species is not confirmed from this photograph. Browse for recognition, but this mount is excluded from scored identification questions.</div>':'')+'</div>')+'</article>'}
function stat(){var mastered=known.filter(function(c){return (progress[c.id]||{}).streak>=2}).length;stats.textContent=data.length+' mounted-specimen cards · '+known.length+' identified for scoring · '+(data.length-known.length)+' still need species verification · '+mastered+' with 2+ correct in a row'}
function tabs(){document.querySelectorAll('.tab').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.mode===mode))})}
function browse(){var subset=data.filter(function(c){return filter==='All'||c.group===filter});
var buttons=subset.map(function(c){return '<button type="button" data-specimen="'+clean(c.id)+'" class="'+(selected&&selected.id===c.id?'selected':'')+'"><b>'+clean(c.de)+'</b><small>'+clean(c.en)+'</small><span class="indicator">'+(c.certainty==='review'?'Identification to verify':'Exam-room specimen')+'</span></button>'}).join('');
root.innerHTML='<div class="filters" role="group" aria-label="Animal group">'+['All','Mammals','Birds'].map(function(x){return '<button class="filter" type="button" data-filter="'+x+'" aria-pressed="'+(x===filter)+'">'+x+'</button>'}).join('')+'</div><div class="list">'+buttons+'</div><div class="full">'+cardMarkup(selected,false)+'</div>';
root.querySelectorAll('[data-filter]').forEach(function(b){b.onclick=function(){filter=b.dataset.filter;var sub=data.filter(function(x){return filter==='All'||x.group===filter});if(!sub.some(function(x){return selected&&x.id===selected.id}))selected=sub[0];browse()}});
root.querySelectorAll('[data-specimen]').forEach(function(b){b.onclick=function(){selected=data.find(function(x){return x.id===b.dataset.specimen});browse();root.querySelector('.full').scrollIntoView({block:'start',behavior:'auto'})}})}
function freshQueue(){queue=known.slice().sort(function(){return Math.random()-.5})}
function next(){if(!queue.length)freshQueue();current=queue.shift();shown=false;answered=false}
function flash(){if(!current)next();root.innerHTML=cardMarkup(current,!shown)+'<div class="actions" id="flashActions">'+(shown?'<button class="secondary" data-score="bad">Needs review</button><button class="primary" data-score="ok">Recognized it</button>':'<button class="primary" id="reveal">Reveal name</button>')+'</div><p class="hint">The photo shows the exact room mount. Mark yourself only after checking the species name.</p>';
if(!shown)document.getElementById('reveal').onclick=function(){shown=true;flash()};
root.querySelectorAll('[data-score]').forEach(function(b){b.onclick=function(){touch(current.id,b.dataset.score==='ok');next();stat();flash()}})}
function options(c){var peers=known.filter(function(x){return x.id!==c.id&&x.group===c.group});peers.sort(function(){return Math.random()-.5});var a=[c].concat(peers.slice(0,3));return a.sort(function(){return Math.random()-.5})}
function quiz(){if(!current)next();if(!answers.length)answers=options(current);
root.innerHTML='<p class="question">Which animal is shown in this exam-room mount?</p>'+cardMarkup(current,true)+'<div class="actions choices" role="group" aria-label="Choose animal">'+answers.map(function(c){return '<button class="choice '+(answered?(c.id===current.id?'correct':c.id===window.__ghcTrophyChoice?'wrong':''):'')+'" data-answer="'+clean(c.id)+'" '+(answered?'disabled':'')+'>'+clean(c.de)+' — '+clean(c.en)+'</button>'}).join('')+'</div>'+
(answered?'<div class="feedback" role="status">'+(window.__ghcTrophyChoice===current.id?'Correct. ':'Not quite. ')+'This is <strong>'+clean(current.de)+' — '+clean(current.en)+'</strong>. '+clean(current.cue)+'</div><div class="actions"><button class="primary" id="nextQuestion">Next specimen</button></div>':'<p class="hint">Names are not revealed until you select an answer.</p>')+
'<p class="hint">This round: '+round.right+' correct / '+round.tried+' attempted</p>';
if(!answered)root.querySelectorAll('[data-answer]').forEach(function(b){b.onclick=function(){window.__ghcTrophyChoice=b.dataset.answer;answered=true;round.tried++;if(b.dataset.answer===current.id)round.right++;touch(current.id,b.dataset.answer===current.id);stat();quiz()}});
else document.getElementById('nextQuestion').onclick=function(){answers=[];window.__ghcTrophyChoice=null;next();quiz()}}
function render(){tabs();stat();if(mode==='cards')browse();else if(mode==='flash')flash();else quiz()}
document.querySelectorAll('[data-mode]').forEach(function(b){b.onclick=function(){mode=b.dataset.mode;current=null;answers=[];shown=false;render()}});
window.GHC_TROPHY_TEST={get cards(){return data.slice()},get scored(){return known.slice()},get progress(){return Object.assign({},progress)},setMode:function(x){if(['cards','flash','quiz'].indexOf(x)>=0){mode=x;current=null;answers=[];render()}}};
render();
})();