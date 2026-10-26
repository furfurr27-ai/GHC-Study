/* Pure, deterministic hunting-calendar evaluation. Not legal authorization.
   Input YYYY-MM-DD is a German LOCAL date; default uses Europe/Berlin, not the device's timezone. */
(function(root,factory){
 const engine=factory();
 if(typeof module!=='undefined'&&module.exports)module.exports=engine;
 root.GHC_SEASON_ENGINE=engine;
})(typeof window!=='undefined'?window:globalThis,function(){
 'use strict';
 const UNKNOWN='UNKNOWN_OR_STALE',CONDITIONAL='CONDITIONAL',
       OPEN='GENERAL_WINDOW_OPEN',CLOSED='GENERAL_WINDOW_CLOSED',
       NO_GENERAL='PROTECTED_OR_NO_GENERAL_SEASON';
 function germanyToday(now){
   const parts=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Berlin',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(now||new Date());
   const get=k=>parts.find(p=>p.type===k).value;
   return get('year')+'-'+get('month')+'-'+get('day');
 }
 function validDate(s){if(!/^\d{4}-\d{2}-\d{2}$/.test(String(s)))return false;const x=new Date(s+'T12:00:00Z');return !Number.isNaN(x.getTime())&&x.toISOString().slice(0,10)===s;}
 function matchesRange(monthDay,range){
   if(!Array.isArray(range)||range.length!==2||!/^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$/.test(range[0])||!/^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$/.test(range[1]))return false;
   const start=range[0],end=range[1];
   return start<=end ? monthDay>=start&&monthDay<=end : monthDay>=start||monthDay<=end;
 }
 function evaluate(dataset,stateCode,speciesId,classId,date){
   const on=date||germanyToday(); const base={stateCode,speciesId,classId:classId||null,date:on,
     status:UNKNOWN,reviewed:null,sourceTitle:'No individually verified rule',sourceUrl:null,
     intervals:[],exceptions:'Not authorization. Check the current law, Revier, age/sex, dependent young and local restrictions.',
     reason:'No verified state rule for this species/class.'};
   if(!validDate(on))return {...base,reason:'Invalid German calendar date.'};
   if(!dataset||!Array.isArray(dataset.states)||!dataset.states.some(s=>s.code===stateCode))
     return {...base,reason:'Unknown state code.'};
   if(stateCode!=='DE-HE')return {...base,reason:'Season data not yet verified for this Bundesland.'};
   const h=dataset.hessen;
   if(!h||!h.species||!h.sourceReviewed||!h.reviewExpires||on<h.effectiveFrom||on>h.reviewExpires)
     return {...base,reason:'Legal data outside confirmed effective/review window; reverify legislation.'};
   const item=h.species[speciesId];
   if(!item||item.unverified)return {...base,reviewed:h.sourceReviewed,reason:item?.reason||'Species not individually verified.'};
   const source=h.sources.find(x=>x.id==='HJagdV-2');
   const citation=h.sources.find(x=>x.id==='LJV-20260518');
   const info={...base,reviewed:h.sourceReviewed,sourceTitle:source.title+'; '+citation.title,
     sourceUrl:source.url,secondaryUrl:citation.url,exceptions:(item.exceptions||base.exceptions)+' Not authorization.',reason:''};
   if(item.conflict)return {...info,reason:'Conflicting regulatory sources; reverify before display.'};
   const classes=item.classes;
   if(!Array.isArray(classes)||!classes.length)return {...info,reason:'Class data missing.'};
   if(!classId&&classes.length>1)return {...info,status:CONDITIONAL,reason:'Age/sex class must be selected and verified; conditions vary.',intervals:classes.flatMap(c=>c.intervals||[])};
   const chosen=classId?classes.find(x=>x.id===classId):classes[0];
   if(!chosen)return {...info,status:CONDITIONAL,reason:'Unrecognized or unsupported age/sex class.'};
   if(chosen.conflict)return {...info,reason:'Conflicting rule for selected class.'};
   const more={...info,classId:chosen.id,classLabel:chosen.label,intervals:chosen.intervals||[]};
   if(chosen.noGeneral)return {...more,status:NO_GENERAL,reason:chosen.reason||'Verified: no general hunting season.'};
   if(!Array.isArray(chosen.intervals)||!chosen.intervals.length)return {...more,reason:'No documented calendar intervals.'};
   const active=chosen.intervals.some(r=>matchesRange(on.slice(5),r));
   if(active&&chosen.conditional)return {...more,status:CONDITIONAL,reason:chosen.reason||'Additional class/management conditions must be resolved.'};
   return {...more,status:active?OPEN:CLOSED,reason:active?'Verified general calendar window only; not permission.':'Verified general calendar window currently closed.'};
 }
 return {UNKNOWN,CONDITIONAL,OPEN,CLOSED,NO_GENERAL,germanyToday,validDate,matchesRange,evaluate};
});
