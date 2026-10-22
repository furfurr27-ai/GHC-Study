#!/usr/bin/env python3
"""Static, offline invariants for the exam-room Trophy Test bank and photo crops."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
assets=root/'app/src/main/assets'
js=(assets/'trophy-test-data.js').read_text(encoding='utf-8')
m=re.search(r'window.GHC_TROPHY_CARDS=(\[.*?\]);\s*$',js,re.S)
assert m,'Trophy Test data missing'
cards=json.loads(m.group(1))
assert len(cards)==29
assert len({c['id'] for c in cards})==len(cards)
assert len([c for c in cards if c['certainty']=='identified'])==19
assert len([c for c in cards if c['certainty']=='review'])==10
for c in cards:
    assert c['group'] in ('Mammals','Birds')
    assert c['de'] and c['en'] and c['cue'] and c['contrast']
    assert c['certainty'] in ('identified','review')
    assert len(c['box'])==4
    assert (assets/'trophy-test-media'/(c['id']+'.jpg')).stat().st_size>2000,c['id']
info_source=(assets/'trophy-test-info-data.js').read_text(encoding='utf-8')
im=re.search(r'window.GHC_TROPHY_INFO=(\\{.*?\\});\\s*
assert index.count('id="ghc-trophy-test-launcher"')==1
assert 'trophy-test-launcher.js' in index
page=(assets/'trophy-test.html').read_text(encoding='utf-8')
assert 'src="trophy-test-info-data.js"' in page
assert all(x in page for x in ('data-mode="cards"','data-mode="flash"','data-mode="quiz"','href="index.html"'))
app=(assets/'trophy-test-app.js').read_text(encoding='utf-8')
assert 'ghc-trophy-test-progress-v1' in app
assert "ghc-study-progress-v1" not in app
assert "c.certainty==='identified'" in app
print('PASS: 29 sourced trophy cards (13 Study Mode, 11 class slides, 5 German external); 19 scored and 10 review-only; existing progress isolated')
,info_source,re.S)
assert im,'Missing trophy facts inventory'
facts=json.loads(im.group(1))
assert set(facts)=={c['id'] for c in cards},'Not every specimen has sourced facts'
assert sum(v['sourceType']=='study' for v in facts.values())==13
assert sum(v['sourceType']=='slides' for v in facts.values())==11
assert sum(v['sourceType']=='web' for v in facts.values())==5
for c in cards:
    x=facts[c['id']]
    assert x['title'] and x['rows'],'Missing source or detail: '+c['id']
    assert all(len(row)==2 and row[0] and row[1] for row in x['rows'])
    if x['sourceType']=='web':
        assert x['sourceUrl'].startswith('https://'),'Missing offline cited German reference'
    if c['certainty']=='review':
        assert x.get('notes'),'Uncertain specimen must carry qualified facts'
index=(assets/'index.html').read_text(encoding='utf-8')
assert index.count('id="ghc-trophy-test-launcher"')==1
assert 'trophy-test-launcher.js' in index
page=(assets/'trophy-test.html').read_text(encoding='utf-8')
assert all(x in page for x in ('data-mode="cards"','data-mode="flash"','data-mode="quiz"','href="index.html"'))
app=(assets/'trophy-test-app.js').read_text(encoding='utf-8')
assert 'ghc-trophy-test-progress-v1' in app
assert "ghc-study-progress-v1" not in app
assert "c.certainty==='identified'" in app
print('PASS: 29 cards, 19 scoreable, 10 review-only; offline photos, app linkage and independent progress')
