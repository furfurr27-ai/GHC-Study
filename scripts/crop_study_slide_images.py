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
    # Final bird photo crops inspected at full resolution. We favor intact
    # identification features over feet or outer wing-tips when slide badges
    # would otherwise intrude on the individual source picture.
    "capercaillie": (37, 56, 270, 211),
    "blackgrouse": (302, 107, 612, 252),
    "blackkite": (592, 75, 886, 426),
    "brantgoose": (625, 262, 834, 465),
    "canadagoose": (409, 476, 792, 661),
    # Class photographs rather than the surrounding terminology/kennel slides.
    "combinationguns": (650, 79, 879, 231),
    "rangesafety": (436, 33, 885, 185),
    "doggroups": (527, 491, 869, 654),
    "kennel": (76, 73, 688, 464),
    # Standalone class pictures extracted from dog and game-disease lessons.
    # Dog/disease examples are visual references, not proof of diagnosis.
    "labrador": (167, 113, 546, 333),
    "dogcert": (432, 71, 686, 253),
    "trichinella": (607, 264, 895, 439),
    "rabies": (652, 42, 800, 203),
    "asf": (76, 88, 700, 394),
    "footmouth": (648, 388, 880, 492),
    # Standalone photographs or *individual technical illustrations* cut
    # from original course slides, visually checked against source pixels.
    # Diagram labels/leader lines intrinsic to the illustration are retained.
    "goldeneagle": (476, 289, 890, 653),
    "hornsignals": (547, 142, 873, 386),
    "waidgerechtigkeit": (502, 402, 861, 632),
    "branchsigns": (518, 158, 876, 580),
    "lastbite": (577, 443, 871, 658),
    "methods": (352, 69, 894, 448),
    "followup": (315, 414, 613, 593),
    "coldweapons": (54, 94, 653, 354),
    "shotgunshell": (192, 72, 526, 531),
    "ammotypes": (121, 78, 319, 498),
    "stecher": (319, 176, 571, 515),
    "scopebasics": (111, 234, 347, 510),
    # Source technical bird-beak plate and revolver photograph, isolated from
    # lecture slide frames. Handgun image is illustrative, NOT legal quota data.
    "birdanatomy": (350, 93, 506, 529),
    "handgunquota": (460, 333, 700, 498),
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
    # Immutable study-card facts are part of the source-audit contract:
    # the offline photo assembly may change only imageKey/visualId.
    original_card_facts={
        c["id"]:{k:v for k,v in c.items() if k not in ("imageKey","visualId")}
        for c in cards
    }
    if len(original_card_facts)!=len(cards):
        raise RuntimeError("Duplicate study card ID before image assembly")
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
    # The firearms-action slide contains four distinct source photographs.
    # Retain their exact source pixels, arranged as an unlabeled photo montage
    # rather than displaying the original text-heavy lecture slide.
    actions=next((c for c in cards if c["id"]=="firearmactions"),None)
    if actions is None:
        raise RuntimeError("Missing Firearm Action Names card")
    action_src=vm.get(actions.get("visualId")) if actions.get("visualId") else None
    if not action_src:
        action_src=imgs.get(actions.get("imageKey"))
    montage_key="study_cropped_firearmactions"
    montage_rel="media/study-photo-firearmactions.webp"
    if actions.get("imageKey")!=montage_key or not (ROOT/montage_rel).is_file():
        if not action_src or not action_src.get("src"):
            raise RuntimeError("Missing original GHC firearm-actions slide picture")
        photo_rects=[
            (510,90,830,174),    # Lever action
            (508,196,837,260),   # Pump action
            (508,284,863,331),   # Semiautomatic
            (668,333,853,475),   # Combination firearm
        ]
        with Image.open(ROOT/action_src["src"]) as base:
            base=base.convert("RGB")
            photo_rows=Image.new("RGB",(660,580),"white")
            for idx,rect in enumerate(photo_rects):
                x1,y1,x2,y2=rect
                if not (0<=x1<x2<=base.width and 0<=y1<y2<=base.height):
                    raise RuntimeError("Invalid Firearm Action Names photo crop")
                photo=base.crop(rect)
                photo.thumbnail((630,135),Image.Resampling.LANCZOS)
                photo_rows.paste(photo,((660-photo.width)//2,idx*145+(145-photo.height)//2))
            photo_rows.save(ROOT/montage_rel,"WEBP",quality=90,method=6)
        imgs[montage_key]={
            "src":montage_rel,
            "source":action_src.get("source") or actions.get("source") or "",
            "page":action_src.get("page"),
            "studyPhotoCropOf":action_src["src"],
            "review":"Four original class firearm photos; unlabeled montage; verified 2026-10-14"
        }
        actions["visualId"]=None
        actions["imageKey"]=montage_key
        print("Assembled four picture-only action photos",montage_rel)
    # Extract five original tree photographs from their class comparison
    # slide. Assemble in the same Oak/Fir/Alder/Spruce/Pine order, with no
    # text or presentation chrome. Individual class photos remain untouched.
    trees=next((c for c in cards if c["id"]=="trees"),None)
    if trees is None:
        raise RuntimeError("Missing Big 5 German Trees card")
    trees_key="study_cropped_trees"
    trees_rel="media/study-photo-trees.webp"
    if trees.get("imageKey")!=trees_key or not (ROOT/trees_rel).is_file():
        original=vm.get(trees.get("visualId")) if trees.get("visualId") else None
        if not original:
            original=imgs.get(trees.get("imageKey"))
        if not original or not original.get("src"):
            raise RuntimeError("Missing original five-tree classroom picture")
        parts=[
            (70,149,221,350),    # Eiche / Oak
            (410,166,707,316),   # Tanne / Fir
            (31,372,219,623),    # Erle / Alder
            (303,380,536,565),  # Fichte / Spruce
            (611,351,873,557),  # Kiefer / Pine
        ]
        with Image.open(ROOT/original["src"]) as base:
            base=base.convert("RGB")
            composite=Image.new("RGB",(900,360),"white")
            for ix,rect in enumerate(parts):
                x1,y1,x2,y2=rect
                if not (0<=x1<x2<=base.width and 0<=y1<y2<=base.height):
                    raise RuntimeError("Invalid five-trees picture crop")
                photo=base.crop(rect)
                photo.thumbnail((170,330),Image.Resampling.LANCZOS)
                composite.paste(photo,(6+ix*180+(170-photo.width)//2,15+(330-photo.height)//2))
            composite.save(ROOT/trees_rel,"WEBP",quality=90,method=6)
        imgs[trees_key]={
            "src":trees_rel,
            "source":original.get("source") or trees.get("source") or "",
            "page":original.get("page"),
            "studyPhotoCropOf":original["src"],
            "review":"Five original class tree photographs, unlabeled composite, visually checked 2026-10-14"
        }
        trees["visualId"]=None
        trees["imageKey"]=trees_key
        print("Assembled five original class tree photographs",trees_rel)
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
    assembled_card_facts={
        c["id"]:{k:v for k,v in c.items() if k not in ("imageKey","visualId")}
        for c in cards
    }
    if assembled_card_facts!=original_card_facts:
        raise RuntimeError("Photo overlay unexpectedly modified a study card fact, ID or note")
    if len(cards)!=117:
        raise RuntimeError("Study-card count changed; review before adjusting this invariant")
    for var,object_value in (("GHC_STUDY_CARDS",cards),("GHC_STUDY_IMAGES",imgs)):
        start,end,_=read_json(html,var)
        html=html[:start]+json.dumps(object_value,ensure_ascii=False,separators=(",",":"))+html[end:]
    HTML.write_text(html,encoding="utf-8")
    for cid in CROPS:
        assert (ROOT/("media/study-photo-"+cid+".webp")).is_file()
    print("PASS " + str(len(CROPS)) + " original-class-source picture-only crops; all study facts preserved")

if __name__=="__main__":
    main()
