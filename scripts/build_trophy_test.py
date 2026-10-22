#!/usr/bin/env python3
"""Crop user-supplied exam-room mount photographs for standalone offline Trophy Test cards.
Source photos are kept outside Android assets. Cropped outputs strip metadata/room context.
"""
from pathlib import Path
import json
import re
from PIL import Image, ImageOps
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'app/src/main/assets'
text=(ASSETS/'trophy-test-data.js').read_text(encoding='utf-8')
m=re.fullmatch(r'(?s).*?window.GHC_TROPHY_CARDS=(\[.*\]);\s*',text)
assert m,"Trophy inventory must be one JS array literal"
cards=json.loads(m.group(1))
assert len(cards)>=20
assert len({c['id'] for c in cards})==len(cards)
assert sum(c['certainty']=='identified' for c in cards)>=15
out=ASSETS/'trophy-test-media'
out.mkdir(exist_ok=True)
for c in cards:
    src=ROOT/'research/trophy-test/photos'/('IMG-20261022-'+c['photo']+'.jpg')
    assert src.is_file(),f"Source photo missing: {src}"
    im=ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    x1,y1,x2,y2=c['box']
    assert 0<=x1<x2<=im.width and 0<=y1<y2<=im.height,(c['id'],im.size,c['box'])
    photo=im.crop((x1,y1,x2,y2))
    photo.thumbnail((800,800),Image.Resampling.LANCZOS)
    assert photo.width>=110 and photo.height>=110,c['id']
    target=out/(c['id']+'.jpg')
    photo.save(target,'JPEG',quality=82,optimize=True,exif=b'')
    assert target.stat().st_size>2000,c['id']
print('PASS:',len(cards),'offline exam-room photo crops; separate score bank; originals excluded from APK assets')
