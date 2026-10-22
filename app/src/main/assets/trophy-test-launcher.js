(function(){
'use strict';
// A dedicated Quiz Mode tile, not a replacement for any existing question bank.
function install(){
 var app=document.getElementById('app');
 var hero=app&&app.querySelector('.home-hero');
 if(!hero||!/Quiz Mode/i.test(hero.textContent)||app.querySelector('#ghc-trophy-test-entry'))return;
 var a=document.createElement('a');a.id='ghc-trophy-test-entry';
 a.className='card source-card';a.href='trophy-test.html';
 a.setAttribute('aria-label','Trophy Test — identify exam room animal mounts');
 a.style.cssText='display:block;text-decoration:none;margin:11px 0;padding:14px 16px;background:#e3d3b7;color:#243828;border:2px solid #b78949;border-radius:13px';
 a.innerHTML='<h3 style="margin:0 0 4px">Trophy Test →</h3><p style="margin:0">Real exam-room mounts · photographic baseball cards · identify species</p>';
 hero.insertAdjacentElement('afterend',a);
}
function init(){install();var app=document.getElementById('app');if(app)new MutationObserver(install).observe(app,{childList:true,subtree:false})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();