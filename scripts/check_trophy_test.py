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
