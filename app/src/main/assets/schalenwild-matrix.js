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
    { de:'Gamswild', en:'chamois', rut:[11], young:[5], gest:'20–21 wk*', note:'The class slide timing (November rut, May births) does not line up with its 20–21 week gestation figure.' },
    { de:'Muffelwild', en:'mouflon', rut:[10,11,12], young:[3,4,5,6], gest:'≈22 wk' }
  ];
  var filter = 'both', isOpen = true, activeView = 'reproduction';
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
      '<summary><span class="ghc-matrix-heading">Schalenwild · Vergleichsmatrizen</span><span class="ghc-matrix-subheading">7 species · patterns and exceptions</span></summary>'+
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
        '<p class="ghc-matrix-caveat">Month blocks are study approximations, not exact start/end dates. R = rut, Y = young. <b>Schwarzwild:</b> births may also occur outside the highlighted months.</p>'+
        '<p class="ghc-matrix-caveat"><b>* Gamswild slide inconsistency:</b> November rut, 20–21 weeks gestation and May births do not line up cleanly. Those are the course slide figures; confirm with your instructor.</p>'+
        '<div class="ghc-matrix-source">Figures: GHC Section 1 course study deck, Question 4. Visualization inspired by <a href="https://youtu.be/bZSqIRW5zTQ" target="_blank" rel="noopener noreferrer">Waidwissen WaidMatrix ↗</a>; Waidwissen values were not substituted.</div>'+
      '</div></details>';
  }

  // Original comparison tables use only the linked GHC animal slides.
  // Months intentionally omitted where no general adult cycle was established.
  var CYCLE_DATA = [
    {de:'Rehwild',en:'roe deer',kind:'Gehörn (antlers)',shed:'Nov–Dec (older bucks)',growth:'Jan–Mar (older bucks)',rub:'Mar–Apr'},
    {de:'Rotwild',en:'red deer',kind:'Geweih (antlers)',shed:'Spring (first head)',growth:'—',rub:'Sep (first head)'},
    {de:'Schwarzwild',en:'wild boar',kind:'Waffen (tusks)',shed:'Never',growth:'—',rub:'—'},
    {de:'Damwild',en:'fallow deer',kind:'Geweih (antlers)',shed:'Annually; older first',growth:'Bast: Apr/May–Aug',rub:'—'},
    {de:'Sikawild',en:'sika deer',kind:'Geweih (antlers)',shed:'Annually; older first',growth:'Bast: May–Aug',rub:'—'},
    {de:'Gamswild',en:'chamois',kind:'Krucken (horns)',shed:'Never',growth:'Throughout life',rub:'—'},
    {de:'Muffelwild',en:'mouflon',kind:'Schnecken (horns)',shed:'Never',growth:'Throughout life',rub:'—'}
  ];
  var IDENT_DATA = [
    {de:'Rehwild',en:'roe deer',kind:'Antlers',teeth:'32',digest:'Ruminant',className:'Niederwild'},
    {de:'Rotwild',en:'red deer',kind:'Antlers',teeth:'34',digest:'Ruminant',className:'Hochwild'},
    {de:'Schwarzwild',en:'wild boar',kind:'Tusks',teeth:'44',digest:'Non-ruminant',className:'Hochwild'},
    {de:'Damwild',en:'fallow deer',kind:'Antlers',teeth:'32',digest:'Ruminant',className:'Hochwild'},
    {de:'Sikawild',en:'sika deer',kind:'Antlers',teeth:'34',digest:'Ruminant',className:'Hochwild'},
    {de:'Gamswild',en:'chamois',kind:'Horns',teeth:'32',digest:'Ruminant',className:'Hochwild'},
    {de:'Muffelwild',en:'mouflon',kind:'Horns',teeth:'32',digest:'Ruminant',className:'Hochwild'}
  ];
  function compareTable(columns, items) {
    var html='<div class="ghc-matrix-scroll" role="region" tabindex="0" aria-label="Scrollable wildlife comparison table"><table class="ghc-matrix-table ghc-matrix-compare"><thead><tr>'+
      '<th scope="col" class="ghc-matrix-species">Wildart<span>Species</span></th>';
    columns.forEach(function(c){html+='<th scope="col">'+escapeHtml(c.label)+'</th>';});
    html+='</tr></thead><tbody>';
    items.forEach(function(item){
      html+='<tr><th scope="row" class="ghc-matrix-species">'+escapeHtml(item.de)+'<span>'+escapeHtml(item.en)+'</span></th>';
      columns.forEach(function(c){html+='<td>'+escapeHtml(item[c.key])+'</td>';});
      html+='</tr>';
    });
    return html+'</tbody></table></div>';
  }
  function comparisonMarkup(view) {
    if(view === 'antlers') {
      return '<p class="ghc-matrix-intro">Compare <b>Geweih/Gehörn</b> (antlers), <b>Horn</b> (horns), and <b>Waffen</b> (tusks). For antlers: <b>Abwerfen</b> (shed) → <b>Schieben</b> (grow in Bast/velvet) → <b>Fegen</b> (rub off velvet).</p>'+
        '<p class="ghc-matrix-swipe">Swipe sideways for shedding, velvet and rubbing details →</p>'+
        compareTable([{label:'Structure',key:'kind'},{label:'Abwerfen · Shed',key:'shed'},{label:'Schieben · Grow',key:'growth'},{label:'Fegen · Rub',key:'rub'}],CYCLE_DATA)+
        '<div class="ghc-matrix-notes"><strong>Prüfungsmerker · Standouts</strong><ul>'+
        '<li><b>Rehwild:</b> mature bucks shed in late autumn; rub the new antlers in early spring.</li>'+
        '<li><b>Gamswild and Muffelwild:</b> horns are permanent, so antler-cycle months do not apply.</li>'+
        '<li><b>Rotwild:</b> the spring shedding and September rubbing above apply to the <i>first head</i> specifically, not all ages.</li>'+
        '</ul></div>'+
        '<p class="ghc-matrix-caveat">— = no comparable month given in the reviewed source. No general adult month has been inferred. “Bast” is velvet.</p>'+
        '<div class="ghc-matrix-source">Source: GHC Rehwild, Rotwild, Damwild, Sikawild, Gamswild, Muffelwild and Schwarzwild species decks. Outside-video content is not used for exam figures.</div>';
    }
    return '<p class="ghc-matrix-intro">Compare the high-yield identification exceptions across all seven Schalenwild. <b>Gebiss</b> = teeth; <b>Wiederkäuer</b> = ruminant.</p>'+
      '<p class="ghc-matrix-swipe">Swipe sideways to see all comparison columns →</p>'+
      compareTable([{label:'Trophy',key:'kind'},{label:'Adult teeth',key:'teeth'},{label:'Digestion',key:'digest'},{label:'Game class',key:'className'}],IDENT_DATA)+
      '<div class="ghc-matrix-notes"><strong>Prüfungsmerker · Standouts</strong><ul>'+
      '<li><b>32 teeth:</b> Reh, Dam, Gams, Muffel. <b>34:</b> Rot, Sika. <b>44:</b> Schwarzwild.</li>'+
      '<li><b>Schwarzwild:</b> only non-ruminant in this comparison.</li>'+
      '<li><b>Rehwild:</b> only Niederwild in this comparison; the other six are Hochwild.</li>'+
      '<li><b>Grandeln</b> (upper canine “eyeteeth”): Rotwild and Sikawild; absent in Damwild.</li>'+
      '</ul></div>'+
      '<div class="ghc-matrix-source">Source: GHC Section 1, Questions 1, 2 and 6, verified against the seven original species decks.</div>';
  }
  function switchView(root, next) {
    if(['reproduction','antlers','identification'].indexOf(next)<0)return;
    activeView=next;
    root.querySelectorAll('[data-matrix-view]').forEach(function(button){
      var chosen=button.getAttribute('data-matrix-view')===next;
      button.setAttribute('aria-selected',chosen?'true':'false');
      button.tabIndex=chosen?0:-1;
    });
    root.querySelectorAll('[data-matrix-panel]').forEach(function(panel){
      var chosen=panel.getAttribute('data-matrix-panel')===next;
      panel.hidden=!chosen;
      panel.setAttribute('aria-hidden',chosen?'false':'true');
    });
  }
  function addComparisonViews(root){
    var body=root.querySelector('.ghc-matrix-body');
    if(!body || body.querySelector('[data-matrix-view]'))return;
    var reproduction=document.createElement('div');
    reproduction.id='ghc-matrix-panel-reproduction';
    reproduction.className='ghc-matrix-panel';
    reproduction.setAttribute('role','tabpanel');
    reproduction.setAttribute('aria-labelledby','ghc-matrix-tab-reproduction');
    reproduction.setAttribute('data-matrix-panel','reproduction');
    while(body.firstChild)reproduction.appendChild(body.firstChild);
    var tabs=document.createElement('div');
    tabs.className='ghc-matrix-view-tabs';
    tabs.setAttribute('role','tablist');
    tabs.setAttribute('aria-label','Schalenwild comparisons');
    [
      {key:'reproduction',label:'Fortpflanzung',sub:'Reproduction'},
      {key:'antlers',label:'Geweih & Horn',sub:'Antlers / Horns'},
      {key:'identification',label:'Erkennung',sub:'Identification'}
    ].forEach(function(v){
      var btn=document.createElement('button');
      btn.type='button';
      btn.id='ghc-matrix-tab-'+v.key;
      btn.setAttribute('role','tab');
      btn.setAttribute('data-matrix-view',v.key);
      btn.setAttribute('aria-controls','ghc-matrix-panel-'+v.key);
      btn.setAttribute('aria-label',v.label+', '+v.sub);
      btn.innerHTML='<span>'+escapeHtml(v.label)+'</span><small>'+escapeHtml(v.sub)+'</small>';
      tabs.appendChild(btn);
    });
    body.appendChild(tabs);
    body.appendChild(reproduction);
    ['antlers','identification'].forEach(function(view){
      var panel=document.createElement('div');
      panel.id='ghc-matrix-panel-'+view;
      panel.className='ghc-matrix-panel';
      panel.setAttribute('role','tabpanel');
      panel.setAttribute('aria-labelledby','ghc-matrix-tab-'+view);
      panel.setAttribute('data-matrix-panel',view);
      panel.innerHTML=comparisonMarkup(view);
      body.appendChild(panel);
    });
    switchView(root,activeView);
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
    wrapper.setAttribute('aria-label', 'Schalenwild comparison matrices and memory tips');
    wrapper.innerHTML = markup();
    app.insertBefore(wrapper, search);
    var details = wrapper.querySelector('details');
    details.addEventListener('toggle',function(){isOpen = details.open;});
    addComparisonViews(wrapper);
    wrapper.addEventListener('click',function(e){
      var t = e.target.closest('[data-matrix-view]');
      if(t && wrapper.contains(t)){switchView(wrapper,t.getAttribute('data-matrix-view'));return;}
      var b = e.target.closest('[data-matrix-filter]');
      if(b && wrapper.contains(b)) setFilter(wrapper, b.getAttribute('data-matrix-filter'));
    });
    wrapper.addEventListener('keydown',function(e){
      var t=e.target.closest('[data-matrix-view]');
      if(!t || !wrapper.contains(t) || ['ArrowLeft','ArrowRight','Home','End'].indexOf(e.key)<0)return;
      var keys=['reproduction','antlers','identification'],idx=keys.indexOf(t.getAttribute('data-matrix-view'));
      var n=e.key==='Home'?0:e.key==='End'?keys.length-1:(idx+(e.key==='ArrowRight'?1:-1)+keys.length)%keys.length;
      switchView(wrapper,keys[n]);
      var target=wrapper.querySelector('[data-matrix-view="'+keys[n]+'"]');
      if(target)target.focus();
      e.preventDefault();
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
