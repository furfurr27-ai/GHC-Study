#!/usr/bin/env python3
"""Read-only, repeatable offline app audit. Produces actionable JSON; no mutation."""
import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path("app/src/main/assets")
HTML = ROOT / "index.html"
MEDIA = ROOT / "media"
OUT = Path("build/app-static-audit.json")
MAX_ISSUES = 500

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    html = HTML.read_text(encoding="utf-8")
    files = sorted(p for p in MEDIA.rglob("*") if p.is_file())
    all_media = {p.relative_to(ROOT).as_posix(): p for p in files}
    references = collections.Counter()
    for match in re.finditer(r"""(?:media/)[a-zA-Z0-9_.-]+(?:\.(?:png|jpg|jpeg|webp|svg|gif))""", html, re.I):
        references[match.group(0)] += 1
    missing = sorted(set(references) - set(all_media))
    unreferenced = sorted(set(all_media) - set(references))
    hashes = collections.defaultdict(list)
    for key, path in all_media.items():
        hashes[digest(path)].append(key)
    duplicates = [v for v in hashes.values() if len(v) > 1]
    sizes = sorted(((p.stat().st_size, k) for k, p in all_media.items()), reverse=True)
    flags = {
        "remote_urls": sorted(set(re.findall(r"https?://[^\\s\\\"'<>]+", html)))[:100],
        "local_storage_uses": len(re.findall(r"\blocalStorage\b", html)),
        "event_listener_calls": len(re.findall(r"addEventListener\s*\(", html)),
        "inline_images_data_uri": len(re.findall(r"data:image/", html)),
        "script_tags": len(re.findall(r"<script\b", html, re.I)),
        "external_script_sources": re.findall(r"<script[^>]*\bsrc\s*=\s*['\"]([^'\"]+)", html, re.I),
        "external_stylesheet_sources": re.findall(r"<link[^>]*\brel\s*=\s*['\"]stylesheet['\"][^>]*\bhref\s*=\s*['\"]([^'\"]+)", html, re.I),
    }
    report = {
        "html_bytes": HTML.stat().st_size,
        "html_sha256": digest(HTML),
        "media_count": len(files),
        "media_bytes": sum(p.stat().st_size for p in files),
        "media_extensions": dict(collections.Counter(p.suffix.lower() for p in files)),
        "media_references": len(references),
        "missing_media_references": missing[:MAX_ISSUES],
        "possibly_unreferenced_media": unreferenced[:MAX_ISSUES],
        "duplicate_content_groups": duplicates[:MAX_ISSUES],
        "largest_media": [{"bytes": n, "path": k} for n, k in sizes[:25]],
        "indicators": flags,
        "notes": [
            "Unreferenced media is heuristic; dynamically constructed filenames may be valid.",
            "External URLs may be reference links rather than required online resources.",
            "No file is deleted or rewritten by this audit."
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("html_bytes","media_count","media_bytes","media_references","missing_media_references","possibly_unreferenced_media","duplicate_content_groups")}, indent=2)[:7000])
    if missing:
        raise SystemExit("FAIL: HTML references missing local media")
if __name__ == "__main__":
    main()
