#!/usr/bin/env python3
"""Verify that the claim-level audit is synchronized with tracked HTML source.

Do NOT run after trophy assembly scripts which deliberately change display grouping.
"""
from __future__ import annotations

import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
html=(root/"app/src/main/assets/index.html").read_text(encoding="utf-8")
marker="window.GHC_STUDY_CARDS="
assert marker in html, "Study cards missing from index"
cards,_=json.JSONDecoder().raw_decode(html.split(marker,1)[1])
reg=json.loads((root/"audit/study-card-claim-register-20261012.json").read_text(encoding="utf-8"))
claims=reg["claims"]
lookup={}
for fact in claims:
    ident=fact["id"]
    assert ident not in lookup, f"Duplicate fact ID {ident}"
    lookup[ident]=fact
seen=set()
for card in cards:
    n=0
    expected=[]
    for row in card.get("detailsRows") or []:
        assert isinstance(row,list) and len(row)==2
        n+=1
        expected.append((f"{card['id']}-R{n}",row[0],row[1],"Details"))
    for claim in card.get("details") or []:
        n+=1
        expected.append((f"{card['id']}-D{n}",None,claim,"Details"))
    for claim in card.get("otherFacts") or []:
        n+=1
        expected.append((f"{card['id']}-O{n}",None,claim,"Other Facts"))
    for ident,label,statement,section in expected:
        assert ident in lookup, f"Unregistered fact {ident}"
        fact=lookup[ident]
        seen.add(ident)
        assert fact["cardId"]==card["id"], f"{ident}: wrong card"
        assert fact["claim"]==statement, f"{ident}: audit differs from shipped study card\\nAUDIT: {fact['claim']}\\nAPP:   {statement}"
        assert fact["label"]==label, f"{ident}: label drift"
        assert fact["section"]==section, f"{ident}: section drift"
        assert fact["courseSource"]==card["source"], f"{ident}: source drift"
assert seen==set(lookup),f"Audit has {len(set(lookup)-seen)} orphaned blocks: {sorted(set(lookup)-seen)[:10]}"
assert len(cards)==reg["cardCount"],"Card total drift"
assert len(seen)==len(claims)==reg["claimBlockCount"],"Fact-block count drift"
checked=sum(x["status"]=="checked_against_deck_text" for x in claims)
pending=sum(x["status"]=="pending_claim_level_review" for x in claims)
assert checked==reg["verifiedBlockCount"],"Verified count drift"
assert pending==reg["pendingBlockCount"],"Pending count drift"
assert checked+pending==len(claims),"Unknown/unclassified claim states"
print(f"PASS parity: {len(cards)} cards, {len(claims)} fact blocks, {checked} source-text checked, {pending} pending")
