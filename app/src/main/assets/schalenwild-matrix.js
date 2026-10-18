(function () {
  'use strict';
  // Original GHC comparison visualization; numbers transcribed from the
  // GHC Section 1 Game Biology Conservation course study deck, Q4.
  // Waidwissen inspired the use of a month-by-month comparison, not the figures.
  var MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var SPECIES = [
    { de:'Rehwild', en:'roe deer', rut:[7,8], young:[5,6], gest:'40–42 wk', note:'Including Eiruhe (delayed implantation).' },
    { de:'Rotwild', en:'red deer', rut:[9,10], young:[5,6], gest:'33–34 wk' },
    { de:'Schwarzwild', en:'wild boar', rut:[12,1], young:[3,4], gest:'3 m · 3 w · 3 d' },
    { de:'Damwild', en:'fallow deer', rut:[10,11], young:[6], gest:'30–34 wk', note:'Rut begins late October.' },
    { de:'Sikawild', en:'sika deer', rut:[10,11], young:[6], gest:'30–34 wk' },
    { de:'Gamswild', en:'chamois', rut:[11], young:[5], gest:'20–21 wk' },
    { de:'Muffelwild', en:'mouflon', rut:[10,11,12], young:[3,4,5,6], gest:'≈22 wk' }
  ];
  var filter = 'both', isOpen = true;
  var ID = 'ghc-schalenwild-matrix';

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g,function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }
  function tableHtml() {
    var h = '<table class="ghc-matrix-table"><thead><tr><th scope="col" class="ghc-matrix-species">Wildart<span>Species</span></th>';
    MONTHS.forEach(function(m){h += '<th scope="col">'+m+'</th>';});
    h += '<th scope="col" class="ghc-matrix-gestation">Tragzeit<span>Gestation</span></th></tr></thead><tbody>';
    SPECIES.forEach(function(animal){
      h += '<tr><th scope="row" class="ghc-matrix-species">'+escapeHtml(animal.de)+'<span>'+escapeHtml(animal.en)+'</span></th>';
      MONTHS.forEach(function(month, idx){
        var breeding = animal.rut.indexOf(idx + 1) >= 0 && filter !== 'young';
        var birthing = animal.young.indexOf(idx + 1) >= 0 && filter !== 'rut';
        var kind = breeding && birthing ? 'both' : breeding ? 'rut' : birthing ? 'young' : 'none';
        var label = animal.de + ', '+month+': '+(breeding && birthing ? 'rut and births' : breeding ? 'rut' : birthing ? 'birth season' : 'not highlighted');
        h += '<td title="'+escapeHtml(label)+'"><span class="ghc-matrix-cell ghc-matrix-'+kind+'" role="img" aria-label="'+escapeHtml(label)+'">'+
             (kind==='rut'?'R':kind==='young'?'Y':kind==='both'?'R/Y':'·')+'</span></td>';
      });
      h += '<td class="ghc-matrix-gestation" title="'+escapeHtml(animal.note||'')+'">'+escapeHtml(animal.gest)+'</td></tr>';
    });
    return h + '</tbody></table>';
  }
  function markup() {
    return '<details class="ghc-matrix-details"'+(isOpen?' open':'')+'>'+
      '<summary><span class="ghc-matrix-heading">Schalenwild · Jahresmatrix</span><span class="ghc-matrix-subheading">Compare the seasons across 7 species</span></summary>'+
      '<div class="ghc-matrix-body">'+
        '<p class="ghc-matrix-intro">Spot the patterns at a glance. Colored months show <strong>Brunftzeit</strong> (rut) and <strong>Setzzeit</strong> (young born).</p>'+
        '<div class="ghc-matrix-controls" role="group" aria-label="Seasons to display">'+
          '<button type="button" data-matrix-filter="both" aria-pressed="true">Both</button>'+
          '<button type="button" data-matrix-filter="rut" aria-pressed="false">Rut</button>'+
          '<button type="button" data-matrix-filter="young" aria-pressed="false">Births</button>'+
        '</div>'+
        '<div class="ghc-matrix-legend"><span><i class="ghc-matrix-key ghc-matrix-rut"></i>Rut / mating</span><span><i class="ghc-matrix-key ghc-matrix-young"></i>Young born</span></div>'+
        '<div class="ghc-matrix-swipe">Swipe the month chart horizontally for all months and gestation lengths →</div>'+
        '<div class="ghc-matrix-scroll" role="region" tabindex="0" aria-label="Scrollable Schalenwild calendar matrix">'+tableHtml()+'</div>'+
        '<div class="ghc-matrix-notes">'+
          '<strong>Standouts to remember</strong>'+
          '<ul>'+
            '<li><b>Rehwild:</b> breeds in July–August, then <i>Eiruhe</i> (delayed implantation) separates mating from embryonic growth.</li>'+
            '<li><b>Schwarzwild:</b> the memorable <b>3 months + 3 weeks + 3 days</b> gestation; its breeding period falls mainly in winter.</li>'+
            '<li><b>Pattern:</b> roe deer starts in summer; red deer in early autumn; fallow, sika, chamois and mouflon mostly later. Most young arrive in spring or early summer.</li>'+
            '<li><b>Antlers versus horns:</b> Reh/Rot/Dam/Sika shed antlers. Gams/Muffel retain permanent horns. Schwarzwild has tusks, not antlers.</li>'+
          '</ul>'+
        '</div>'+
        '<p class="ghc-matrix-caveat">Month blocks are study approximations, not exact start/end dates. Use the class slides for exam answers; especially check species-specific ranges and gestation. R = rut, Y = young.</p>'+
        '<div class="ghc-matrix-source">Figures: GHC Section 1 course study deck, Question 4. Visualization inspired by <a href="https://youtu.be/bZSqIRW5zTQ" target="_blank" rel="noopener noreferrer">Waidwissen WaidMatrix ↗</a>; Waidwissen values were not substituted.</div>'+
      '</div></details>';
  }
  function setFilter(root, next) {
    filter = next;
    var scroll = root.querySelector('.ghc-matrix-scroll');
    var lastScroll = scroll ? scroll.scrollLeft : 0;
    if(scroll) {
      scroll.innerHTML = tableHtml();
      scroll.scrollLeft = lastScroll;
    }
    root.querySelectorAll('[data-matrix-filter]').forEach(function(button){
      var active = button.getAttribute('data-matrix-filter') === next;
      button.setAttribute('aria-pressed', active ? 'true':'false');
    });
  }
  function tryMount() {
    var app = document.getElementById('app');
    if (!app || document.getElementById(ID) || !app.querySelector('#studyHubBack')) return;
    var heading = app.querySelector('.study-category-head h1');
    var search = app.querySelector('#studySearch');
    if (!heading || !search || heading.textContent.trim().toLowerCase() !== 'schalenwild') return;
    var wrapper = document.createElement('section');
    wrapper.id = ID;
    wrapper.className = 'ghc-matrix';
    wrapper.setAttribute('aria-label', 'Schalenwild calendar and memory tips');
    wrapper.innerHTML = markup();
    app.insertBefore(wrapper, search);
    var details = wrapper.querySelector('details');
    details.addEventListener('toggle',function(){isOpen = details.open;});
    wrapper.addEventListener('click',function(e){
      var b = e.target.closest('[data-matrix-filter]');
      if(b && wrapper.contains(b)) setFilter(wrapper, b.getAttribute('data-matrix-filter'));
    });
    setFilter(wrapper,filter);
  }
  function start() {
    var app = document.getElementById('app');
    if (!app) return;
    new MutationObserver(tryMount).observe(app, {childList:true});
    tryMount();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',start);
  else start();
})();
