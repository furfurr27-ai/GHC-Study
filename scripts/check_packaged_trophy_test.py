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
    for c in cards:
        path='assets/trophy-test-media/'+c['id']+'.jpg'
        assert path in names and z.getinfo(path).file_size>2000,path
    assert not any('/trophy-test/photos/' in n for n in names),'Uncropped original room photos packaged'
    html=z.read('assets/index.html').decode('utf-8')
    assert 'id="ghc-trophy-test-launcher"' in html,'Missing Quiz Mode entrance'
    assert b'GHC_PRACTICE2_QUESTIONS' in z.read('assets/index.html'),'Practice Test 2 missing'
    assert 'assets/glossary-data.js' in names,'Glossary missing'
    assert 'assets/schalenwild-matrix.js' in names,'Schalenwild comparison missing'
print('PASS: APK includes 29 photo cards, 19 verified-name drills; prior quiz, glossary and matrices intact')
