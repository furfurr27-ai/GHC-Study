#!/usr/bin/env python3
"""One-time migration of v1.4.5 packaged assets into tracked Android sources.

Never rewrites app logic. Requires --apply to change files. Original APK remains
in git history; do not run this during normal Android builds.
"""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

APK = Path("app/src/main/assets/GHC_Study_v1.4.5_FULL_Standalone_Consolidated_Study_Cards.apk")
ASSETS = Path("app/src/main/assets")
ICON = Path("app/src/main/res/drawable/ic_launcher.png")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", default="build/source-recovery-report.json")
    args = parser.parse_args()
    if not APK.is_file():
        raise SystemExit(f"Original APK missing: {APK}")
    report = {"baseline_apk_sha256": sha(APK.read_bytes()), "files": [], "errors": []}
    with zipfile.ZipFile(APK) as z:
        names = sorted(n for n in z.namelist() if n.startswith("assets/") and not n.endswith("/"))
        if "assets/index.html" not in names:
            raise SystemExit("Baseline lacks assets/index.html")
        if "res/drawable/ic_launcher.png" not in z.namelist():
            raise SystemExit("Baseline lacks expected launcher icon")
        for name in names + ["res/drawable/ic_launcher.png"]:
            data = z.read(name)
            target = ICON if name.startswith("res/") else ASSETS / name.removeprefix("assets/")
            if not target.resolve().is_relative_to(Path.cwd().resolve()):
                raise SystemExit(f"Unsafe destination: {target}")
            existing = target.read_bytes() if target.is_file() else None
            status = "identical" if existing == data else ("missing" if existing is None else "different")
            report["files"].append({"source": name, "target": str(target), "bytes": len(data), "sha256": sha(data), "prior_status": status})
            if args.apply:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                if sha(target.read_bytes()) != sha(data):
                    report["errors"].append(name)
    output = Path(args.report)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Files inventoried: {len(report['files'])}; changed/missing: {sum(f['prior_status'] != 'identical' for f in report['files'])}")
    if args.apply and report["errors"]:
        raise SystemExit("Recovered file verification failed")

if __name__ == "__main__":
    main()
