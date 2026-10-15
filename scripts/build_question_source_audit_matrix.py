#!/usr/bin/env python3
"""Generate an honest source-review ledger for ALL 867 GHC examination questions.

Source tags from earlier app versions are navigation aids, not proof the cited
original classroom PDFs were individually checked. Only explicit review records
created by guarded question-source auditing count as reviewed.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

OUTPUT = Path("build/question-source-audit-matrix.json")

def parse_questions(html):
    tag = "window.GHC_QUESTIONS="
    start = html.index(tag) + len(tag)
    questions, _ = json.JSONDecoder().raw_decode(html[start:])
    return questions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk")
    a = parser.parse_args()
    if a.apk:
        with ZipFile(a.apk) as apk:
            html = apk.read("assets/index.html").decode("utf-8")
    else:
        html = Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
    questions = parse_questions(html)
    if len(questions) != 867 or len({q["id"] for q in questions}) != 867:
        raise AssertionError("867 unique question IDs required")
    records = []
    statuses = Counter()
    groups = Counter()
    risks = Counter()
    preexisting_links = Counter()
    for q in questions:
        review = q.get("sourceReview") or {}
        state = "source_compared_explanation_qualified" if review.get("status") == "qualified_after_source_comparison" else "not_individually_factual_audited"
        if state != "not_individually_factual_audited" and (review.get("keyPreserved") is not True or not review.get("checkedSource")):
            raise AssertionError("Audited claim lacks checkable source/immutable key proof: " + q["id"])
        topic = " ".join(map(str, (q.get("sectionTitle", ""), q.get("topic", "")))).lower()
        impact = (
            "high_law_or_safety_priority" if any(w in topic for w in
                ("law", "weapons", "ammunition", "ballistic", "safety", "firearm", "disease", "parasite", "hygiene"))
            else "general_factual_review"
        )
        refs = q.get("learningSourceRefs") or []
        attached = len(refs) > 0
        origin = q.get("sourceGroup") or "unspecified"
        rec = {
            "id": q["id"],
            "section": q.get("section"),
            "sectionTitle": q.get("sectionTitle"),
            "topic": q.get("topic"),
            "sourceGroup": origin,
            "originalQuestionSourceRefs": q.get("sourceRefs") or [],
            "preExistingLearningRefsNotIndependentlyVerified": refs,
            "preExistingClassroomSupportLabelUnverified": q.get("classroomSupport"),
            "factualAuditStatus": state,
            "actualReviewedSource": review.get("checkedSource") if state != "not_individually_factual_audited" else None,
            "sourceReviewType": "targeted_explanation_qualification_only" if state != "not_individually_factual_audited" else None,
            "reviewPriority": impact,
        }
        records.append(rec)
        groups[origin] += 1
        risks[impact] += 1
        statuses[state] += 1
        preexisting_links["existing_classroom_crossrefs" if attached else "missing_classroom_crossrefs"] += 1
    if statuses["source_compared_explanation_qualified"] != 3:
        raise AssertionError("Historical source-comparison review count changed; adjust only with new evidence")
    summary = {
        "questionCount": len(questions),
        "reviewStatuses": dict(statuses),
        "sourceGroups": dict(groups),
        "reviewPriority": dict(risks),
        "preExistingClassroomLinkAvailabilityNotProofOfAudit": dict(preexisting_links),
        "whatCountsAsVerified": "Only individually source-compared explanatory entries with original source and preserved exam keys; no bulk source or factual certification",
        "whatRemains": "864 more individual factual checks, plus current-law checks for dated original sources and device acceptance",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"summary": summary, "questions": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Source audit:", len(questions), "question IDs;", statuses["source_compared_explanation_qualified"], "individually qualified;", statuses["not_individually_factual_audited"], "not individually audited")
    print("Review priority:", dict(risks), "; pre-existing classroom links (not proof):", dict(preexisting_links))
    print("PASS: generated transparent", OUTPUT)

if __name__ == "__main__":
    main()
