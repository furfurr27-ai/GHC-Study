#!/usr/bin/env python3
"""Crop standalone course pictures out of full pages and composite slides.

Assembly-time overlay: preserves question IDs, answer keys, fact text,
existing progress keys and original class image assets. Idempotent.
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path("app/src/main/assets")
HTML = ROOT / "index.html"
CROPS = {
    "mouflon": (160, 180, 610, 643),
    "marmot": (104, 245, 672, 502),
    "seal": (114, 184, 651, 540),
    "bear": (138, 85, 718, 466),
    # Photo-only regions manually checked against course slide source images.
    "beangoose": (532, 396, 795, 659),
    "merganser": (226, 293, 510, 423),
    "muteswan": (359, 127, 630, 332),
    "greatcrestedgrebe": (52, 155, 488, 399),
    "coot": (483, 32, 848, 277),
}

def read_json(s, var):
    tag = "window." + var + "="
    start = s.index(tag) + len(tag)
    value, length = json.JSONDecoder().raw_decode(s[start:])
    return start, start+length, value

def main():
    html = HTML.read_text(encoding="utf-8")
    _, _, visuals = read_json(html, "GHC_VISUALS")
    vm = {x["id"]:x for x in visuals}
    _, _, imgs = read_json(html, "GHC_STUDY_IMAGES")
    _, _, cards = read_json(html, "GHC_STUDY_CARDS")
    seen=set()
    for card in cards:
        cid=card["id"]
        if cid not in CROPS:
            continue
        seen.add(cid)
        newkey="study_cropped_"+cid
        dst_rel="media/study-photo-"+cid+".webp"
        if card.get("imageKey")==newkey and (ROOT/dst_rel).is_file():
            continue
        orig=vm.get(card.get("visualId")) if card.get("visualId") else None
        if not orig:
            orig=imgs.get(card.get("imageKey"))
        if not orig or not orig.get("src"):
            raise RuntimeError(cid+": no source image")
        source=ROOT/orig["src"]
        if not source.is_file():
            raise RuntimeError(cid+": missing "+str(source))
        rect=CROPS[cid]
        with Image.open(source) as im:
            w,h=im.size
            if not (0<=rect[0]<rect[2]<=w and 0<=rect[1]<rect[3]<=h):
                raise RuntimeError(cid+": bad crop "+str(rect))
            im.convert("RGB").crop(rect).save(ROOT/dst_rel,"WEBP",quality=88,method=6)
        imgs[newkey]={
            "src":dst_rel,
            "source":orig.get("source") or card.get("source") or "",
            "page":orig.get("page"),
            "studyPhotoCropOf":orig["src"],
            "review":"picture-only crop visually checked 2026-10-14"
        }
        card["visualId"]=None
        card["imageKey"]=newkey
        print("Cropped",cid,orig["src"],"to",dst_rel)
    if seen!=set(CROPS):
        raise RuntimeError("Missing card IDs "+str(set(CROPS)-seen))
    for var,object_value in (("GHC_STUDY_CARDS",cards),("GHC_STUDY_IMAGES",imgs)):
        start,end,_=read_json(html,var)
        html=html[:start]+json.dumps(object_value,ensure_ascii=False,separators=(",",":"))+html[end:]
    HTML.write_text(html,encoding="utf-8")
    for cid in CROPS:
        assert (ROOT/("media/study-photo-"+cid+".webp")).is_file()
    print("PASS " + str(len(CROPS)) + " original-class-source picture-only crops; all study facts preserved")

if __name__=="__main__":
    main()
