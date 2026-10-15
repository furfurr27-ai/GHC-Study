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
        declared = review.get("status")
        if declared in {"qualified_after_source_comparison", "source_compared_explanation_qualified"}:
            state = "source_compared_explanation_qualified"
        elif declared == "source_compared_key_conflict":
            state = "source_compared_key_conflict"
        else:
            state = "not_individually_factual_audited"
        if state == "source_compared_key_conflict" and not (
            review.get("sourceBankKeyDisputed") is True and q.get("preAnswerWarning")
        ):
            raise AssertionError("Disputed answer must have pre-answer warning: " + q["id"])
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
            "sourceReviewType": ("original_key_conflict_preserved_and_qualified" if state == "source_compared_key_conflict"
                                 else "targeted_explanation_qualification_only" if state != "not_individually_factual_audited" else None),
            "classroomSourceActuallyChecked": review.get("classroomSource") if state != "not_individually_factual_audited" else None,
            "keyDisputeUnresolved": state == "source_compared_key_conflict",
            "original2013PaperAnswerKeyConfirmed": review.get("originalPaperKeyVerified") is True if state == "source_compared_key_conflict" else None,
            "originalPracticePaperSource": review.get("originalPracticePaperSource") if state == "source_compared_key_conflict" else None,
            "preservedOriginalPaperKey": q["correct"] if state == "source_compared_key_conflict" else None,
            "separatelyAcceptedSafetyAnswer": q.get("safetyAcceptedCorrect") if state == "source_compared_key_conflict" else None,
            "userWarnedBeforeScoring": bool(q.get("preAnswerWarning")) if state == "source_compared_key_conflict" else False,
            "reviewPriority": impact,
        }
        records.append(rec)
        groups[origin] += 1
        risks[impact] += 1
        statuses[state] += 1
        preexisting_links["existing_classroom_crossrefs" if attached else "missing_classroom_crossrefs"] += 1
    # Require exact fourteen source-reviewed IDs, never infer from inherited metadata.
    # remain explicitly unaudited regardless of prior inherited classroom tags.
    expected_reviewed = {
        "P2013-S4-Q05", "P2013-S4-Q08", "H2023-D04-Q137",
        "P2013-S3-Q02", "H2023-D08-Q052", "H2023-D08-Q047",
        "H2023-D17-Q008", "H2023-D17-Q018", "H2023-D08-Q024",
        "P2013-S3-Q01", "P2013-S3-Q03", "P2013-S3-Q04",
        "P2013-S3-Q08", "P2013-S3-Q11"
    }
    reviewed = {x["id"] for x in records if x["factualAuditStatus"] != "not_individually_factual_audited"}
    if reviewed != expected_reviewed:
        raise AssertionError("Individually reviewed IDs drifted; require source evidence for every new reviewed record")
    if (statuses["source_compared_explanation_qualified"] != 11
        or statuses["source_compared_key_conflict"] != 3
        or statuses["not_individually_factual_audited"] != 853):
        raise AssertionError("Expected 11 qualified, 3 dated-paper conflicts, 853 not audited")
    summary = {
        "questionCount": len(questions),
        "reviewStatuses": dict(statuses),
        "sourceGroups": dict(groups),
        "reviewPriority": dict(risks),
        "preExistingClassroomLinkAvailabilityNotProofOfAudit": dict(preexisting_links),
        "whatCountsAsVerified": "11 individually source-compared qualified explanations; 3 dated-paper conflicts/overbroad rules are explicitly NOT certified as current-law correct; all 867 original answer letters preserved",
        "whatRemains": "853 questions await individual source comparison. Legacy Q02 original 2013 B/C paper key omits mandatory vehicle unloading, separately accept B/C/D. Legacy Q03 transport checklist and Q11 semiauto magazine wording do not fully describe current federal law; prominently warn before answering while retaining original paper keys. Physical device testing remains pending.",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"summary": summary, "questions": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Source audit:", len(questions), "question IDs;", statuses["source_compared_explanation_qualified"], "individually qualified;",
          statuses["source_compared_key_conflict"], "legacy key conflicts;", statuses["not_individually_factual_audited"], "not individually audited")
    print("Review priority:", dict(risks), "; pre-existing classroom links (not proof):", dict(preexisting_links))
    print("PASS: generated transparent", OUTPUT)

if __name__ == "__main__":
    main()
