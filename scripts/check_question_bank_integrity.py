#!/usr/bin/env python3
"""Validate GHC's shipped 867-question exam bank without changing answer keys.

Checks exact data in the offline index.html that is packaged in the APK.
A clean report checks structural consistency and answer giveaways only:
it is NOT semantic confirmation against source slides or German law.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HTML = Path("app/src/main/assets/index.html")
OUT = Path("build/question-bank-integrity.json")


def array_from_js(html: str, variable: str) -> list:
    anchor = "window." + variable + "="
    pos = html.find(anchor)
    if pos < 0:
        raise AssertionError(f"Missing embedded data bank: {variable}")
    value, _ = json.JSONDecoder().raw_decode(html[pos + len(anchor):])
    if not isinstance(value, list):
        raise AssertionError(f"Not an array: {variable}")
    return value


def normalized(text: str) -> str:
    return re.sub(r"[^\w]+", "", str(text).casefold())


def answer_leaks(q: dict) -> list[str]:
    """Flag explicit answer-string clues, not ordinary topic words."""
    stem = str(q.get("stem", ""))
    spans = re.findall(r"\(([^)]{3,220})\)", stem)
    stem_flat = normalized(stem)
    spans_tokens = set(re.findall(r"[a-z0-9]{3,}", " ".join(spans).lower()))
    choices = q.get("choices", [])
    answers = set(q.get("correct", []))
    found: list[str] = []
    for choice in choices:
        if choice.get("id") not in answers:
            continue
        option = str(choice.get("text", ""))
        compact = normalized(option)
        if len(compact) >= 24 and compact in stem_flat:
            found.append(f"Correct option repeated in stem: {option[:110]}")
        tokens = re.findall(r"[a-z0-9]{3,}", option.lower())
        significant = [t for t in tokens if t not in {"the", "and", "for", "with", "that", "this", "from"}]
        overlap = sum(t in spans_tokens for t in significant)
        if len(significant) >= 2 and overlap >= 2 and overlap / len(significant) >= 0.60:
            found.append(f"Parenthetical likely supplies correct choice: {option[:110]}")
    return found


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    questions = array_from_js(html, "GHC_QUESTIONS")
    vocab = array_from_js(html, "GHC_VOCAB_QUESTIONS")
    errors: list[str] = []
    duplicate_stems: dict[str, list[str]] = defaultdict(list)
    types = Counter()
    groups = Counter()
    ids: set[str] = set()
    suspicious: list[dict] = []
    no_visual = 0

    if len(questions) != 867:
        errors.append(f"Expected 867 exam questions, found {len(questions)}")
    if len(vocab) != 77:
        errors.append(f"Expected 77 vocabulary quiz questions, found {len(vocab)}")
    for q in questions:
        qid = str(q.get("id") or "")
        if not qid:
            errors.append("Question with no ID")
            continue
        if qid in ids:
            errors.append(f"{qid}: duplicate question ID")
        ids.add(qid)
        group = q.get("sourceGroup")
        groups[group] += 1
        qtype = q.get("answerType")
        types[qtype] += 1
        if not str(q.get("stem") or "").strip():
            errors.append(f"{qid}: missing question stem")
        choices = q.get("choices") or []
        if len(choices) < 2:
            errors.append(f"{qid}: fewer than two choices")
        choice_ids = [c.get("id") for c in choices]
        if len(choice_ids) != len(set(choice_ids)):
            errors.append(f"{qid}: duplicate choice IDs")
        content = [normalized(c.get("text") or "") for c in choices]
        if any(not x for x in content):
            errors.append(f"{qid}: empty choice")
        if len(set(content)) != len(content):
            errors.append(f"{qid}: duplicate choice text")
        correct = q.get("correct")
        if not isinstance(correct, list) or not correct:
            errors.append(f"{qid}: missing correct answer list")
            correct = []
        if len(set(correct)) != len(correct) or any(c not in choice_ids for c in correct):
            errors.append(f"{qid}: incorrect/unlisted correct-answer IDs")
        if qtype not in ("single", "multi"):
            errors.append(f"{qid}: invalid answerType")
        if qtype == "single" and len(correct) != 1:
            errors.append(f"{qid}: single-answer item has {len(correct)} correct choices")
        for field in ("explanation", "learningWhy"):
            if not str(q.get(field) or "").strip():
                errors.append(f"{qid}: missing {field}")
        duplicate_stems[normalized(q.get("stem", ""))].append(qid)
        if not (q.get("visualRefs") or q.get("animalVisualRefs")):
            no_visual += 1
        for reason in answer_leaks(q):
            suspicious.append({"question_id": qid, "reason": reason, "stem": q.get("stem")})

    if dict(groups) != {"practice2013": 100, "hessen2023": 767}:
        errors.append(f"Unexpected source pools: {dict(groups)}")
    duplicate_groups = [group for group in duplicate_stems.values() if len(group) > 1]
    # Answer-giveaway detections are blockers here because this app explicitly
    # avoids parenthetical hints in multiple-choice exam questions.
    if suspicious:
        errors.append(f"{len(suspicious)} possible answer giveaway(s): manual review required")
    summary = {
        "questions": len(questions),
        "source_groups": dict(groups),
        "answer_types": dict(types),
        "vocabulary_questions": len(vocab),
        "structural_errors": errors,
        "possible_answer_giveaways": suspicious,
        "duplicate_stem_groups_informational": duplicate_groups,
        "no_explicit_visual_reference_informational": no_visual,
        "scope_caution": "This validates structure and mechanical answer clues only. It does not verify factual answer keys, legal currency, images, or teaching explanations.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exam bank: {len(questions)} questions; {dict(groups)}; {dict(types)}")
    print(f"Duplicate stems (informational): {len(duplicate_groups)} groups")
    print(f"Questions lacking explicit image refs (informational): {no_visual}")
    print(f"Possible answer giveaways: {len(suspicious)}")
    for problem in errors[:20]:
        print("ERROR:", problem, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
