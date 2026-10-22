#!/usr/bin/env python3
"""Fail release if actual APK lacks the complete Trophy Test room photographs/cards."""
import sys,json,re
from zipfile import ZipFile
assert len(sys.argv)==2
with ZipFile(sys.argv[1]) as z:
    names=set(z.namelist())
    files=['assets/index.html','assets/trophy-test.html','assets/trophy-test-app.js','assets/trophy-test-data.js','assets/trophy-test-launcher.js']
    for f in files:assert f in names,'Missing APK asset '+f
    data=z.read('assets/trophy-test-data.js').decode('utf-8')
    m=re.search(r'window.GHC_TROPHY_CARDS=(\[.*?\]);\s*$',data,re.S)
    assert m,'Missing inventory'
    cards=json.loads(m.group(1))
    assert len(cards)==29 and sum(c['certainty']=='identified' for c in cards)==19
    assert 'assets/trophy-test-info-data.js' in names,'Missing animal facts'
    info=z.read('assets/trophy-test-info-data.js').decode('utf-8')
    im=re.search(r'window.GHC_TROPHY_INFO=(\\{.*?\\});\\s*
        assert path in names and z.getinfo(path).file_size>2000,path
    assert not any('/trophy-test/photos/' in n for n in names),'Uncropped original room photos packaged'
    html=z.read('assets/index.html').decode('utf-8')
    assert 'id="ghc-trophy-test-launcher"' in html,'Missing Quiz Mode entrance'
    assert b'GHC_PRACTICE2_QUESTIONS' in z.read('assets/index.html'),'Practice Test 2 missing'
    assert 'assets/glossary-data.js' in names,'Glossary missing'
    assert 'assets/schalenwild-matrix.js' in names,'Schalenwild comparison missing'
    assert 'data-ghc-matrix="1"' in html,'Schalenwild UI not actually integrated'
print('PASS: APK includes 29 sourced species/animal-group summaries, 29 photos, 125 Practice Test 2 and previous glossary/matrices')
,info,re.S)
    assert im,'Invalid trophy facts record'
    facts=json.loads(im.group(1))
    assert {c['id'] for c in cards}==set(facts),'Source coverage incomplete'
    assert sum(x['sourceType']=='study' for x in facts.values())==13
    assert sum(x['sourceType']=='slides' for x in facts.values())==11
    assert sum(x['sourceType']=='web' for x in facts.values())==5
    assert b'src="trophy-test-info-data.js"' in z.read('assets/trophy-test.html')
    assert b'informationMarkup(current)' in z.read('assets/trophy-test-app.js'),'Missing post-answer explanation'
    for c in cards:
        path='assets/trophy-test-media/'+c['id']+'.jpg'
        assert path in names and z.getinfo(path).file_size>2000,path
    assert not any('/trophy-test/photos/' in n for n in names),'Uncropped original room photos packaged'
    html=z.read('assets/index.html').decode('utf-8')
    assert 'id="ghc-trophy-test-launcher"' in html,'Missing Quiz Mode entrance'
    assert b'GHC_PRACTICE2_QUESTIONS' in z.read('assets/index.html'),'Practice Test 2 missing'
    assert 'assets/glossary-data.js' in names,'Glossary missing'
    assert 'assets/schalenwild-matrix.js' in names,'Schalenwild comparison missing'
    assert 'data-ghc-matrix="1"' in html,'Schalenwild UI not actually integrated'
print('PASS: APK includes 29 photo cards, 19 verified-name drills; prior quiz, glossary and matrices intact')
