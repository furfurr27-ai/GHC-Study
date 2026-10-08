#!/usr/bin/env python3
"""Audit original APK against recovered assets without modifying either."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apk", default="app/src/main/assets/GHC_Study_v1.4.5_FULL_Standalone_Consolidated_Study_Cards.apk")
    p.add_argument("--assets", default="app/src/main/assets")
    p.add_argument("--manifest", default="build/baseline-asset-manifest.json")
    p.add_argument("--compare", action="store_true")
    a = p.parse_args()
    apk, root = Path(a.apk), Path(a.assets)
    mismatches = []
    with zipfile.ZipFile(apk) as z:
        names = sorted(n for n in z.namelist() if n.startswith("assets/") and not n.endswith("/"))
        files = []
        for name in names:
            data = z.read(name)
            entry = {"path": name, "bytes": len(data), "sha256": digest(data)}
            files.append(entry)
            if a.compare:
                target = root / name.removeprefix("assets/")
                if not target.is_file():
                    mismatches.append({"path": name, "issue": "missing"})
                elif digest(target.read_bytes()) != entry["sha256"]:
                    mismatches.append({"path": name, "issue": "hash mismatch"})
        icon = "res/drawable/ic_launcher.png"
        icon_info = {"path": icon, "bytes": len(z.read(icon)), "sha256": digest(z.read(icon))} if icon in z.namelist() else None
    report = {"baseline_apk": str(apk), "baseline_sha256": digest(apk.read_bytes()), "asset_count": len(files), "assets": files, "launcher_icon": icon_info, "mismatches": mismatches}
    out = Path(a.manifest)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"APK assets: {len(files)}; mismatches: {len(mismatches)}; report: {out}")
    if mismatches:
        for problem in mismatches[:20]:
            print(problem)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
