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
    # Bird and raptor photographs selected by inspecting each original slide.
    # Each rectangle avoids captions, numbered badges and other photographs.
    "curlew": (438, 243, 639, 398),
    "whitefrontedgoose": (633, 70, 833, 243),
    "tawnyowl": (25, 217, 259, 595),
    "osprey": (12, 118, 429, 492),
    "seaeagle": (498, 253, 889, 574),
    "eagleowl": (366, 105, 642, 435),
    "kestrel": (460, 76, 866, 343),
    # Additional original course corvid/harrier photos; no slide text retained.
    "harriers": (592, 75, 881, 287),
    "carrioncrow": (13, 16, 251, 175),
    "rook": (18, 278, 407, 570),
    "raven": (371, 345, 846, 646),
    "magpie": (493, 356, 860, 600),
    "jays": (398, 331, 860, 658),
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
    # Correct a separate picture/subject mismatch. This is the exact roe-deer
    # anatomical illustration embedded on page 23 of the 2026 Hunting Techniques
    # class PDF (xref 149), extracted without any surrounding slide text.
    # The original PNG was converted to high-contrast monochrome without
    # moving, deleting or drawing any anatomical lines.
    diagram_rel="media/shotplacement-class-diagram.png"
    diagram=ROOT/diagram_rel
    if not diagram.is_file():
        raise RuntimeError("Missing directly extracted original shot-placement course diagram")
    import hashlib
    if hashlib.sha256(diagram.read_bytes()).hexdigest()!="c00ab76a236fc161b4594dbcd93182a4ed2b4324d5ae7ee52f0916cf6d60cb0f":
        raise RuntimeError("Shot-placement original class diagram integrity check failed")
    shot=next((c for c in cards if c["id"]=="shotplacement"),None)
    if shot is None:
        raise RuntimeError("Missing Shot Placement study card")
    shot["visualId"]=None
    shot["imageKey"]="study_extracted_shotplacement"
    imgs["study_extracted_shotplacement"]={
        "src":diagram_rel,
        "source":"Hunting_Techniques_V3.1_16FEB26.pdf",
        "page":23,
        "studyIllustrationExtraction":"Original PDF page 23 embedded image xref 149, isolated; monochrome threshold only",
        "review":"Anatomically relevant roe-deer heart-lung target diagram, checked 2026-10-14"
    }
    for var,object_value in (("GHC_STUDY_CARDS",cards),("GHC_STUDY_IMAGES",imgs)):
        start,end,_=read_json(html,var)
        html=html[:start]+json.dumps(object_value,ensure_ascii=False,separators=(",",":"))+html[end:]
    HTML.write_text(html,encoding="utf-8")
    for cid in CROPS:
        assert (ROOT/("media/study-photo-"+cid+".webp")).is_file()
    print("PASS " + str(len(CROPS)) + " original-class-source picture-only crops; all study facts preserved")

if __name__=="__main__":
    main()
