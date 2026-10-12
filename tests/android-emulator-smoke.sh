#!/usr/bin/env bash
set -euo pipefail
APK="$(find . -name '*.apk' -print -quit)"
test -n "$APK"
mkdir -p emulator-evidence
adb install -r "$APK"
adb shell am start -W -n org.ghcstudy.v141/org.ghcstudy.offline.MainActivity
sleep 9
adb shell pidof org.ghcstudy.v141
adb exec-out screencap -p > emulator-evidence/quiz-home.png
adb shell uiautomator dump /sdcard/ghc-quiz.xml >/dev/null
adb pull /sdcard/ghc-quiz.xml emulator-evidence/quiz-home.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/quiz-home.xml").read_text(errors="replace")
print("First-screen accessibility snapshot length:",len(s))
if not any(x in s for x in ("Quiz Mode","Study Mode","GHC Study")):
    raise SystemExit("No GHC Study text exposed to Android accessibility tree")
PY
# Use fourth navigation region (Glossary tab) and then system Back.
SIZE="$(adb shell wm size | grep -oE '[0-9]+x[0-9]+' | tail -1)"
W="${SIZE%x*}"; H="${SIZE#*x}"
adb shell input tap "$((W * 7 / 8))" "$((H - 95))"
sleep 5
adb exec-out screencap -p > emulator-evidence/glossary.png
adb shell uiautomator dump /sdcard/ghc-glossary.xml >/dev/null
adb pull /sdcard/ghc-glossary.xml emulator-evidence/glossary.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/glossary.xml").read_text(errors="replace")
print("Glossary accessibility snapshot length:",len(s))
if not any(x in s for x in ("German hunting terminology","Jägersprache glossary","Search terminology")):
    raise SystemExit("Glossary navigation not confirmed in emulator")
PY
adb shell input keyevent KEYCODE_BACK
sleep 4
adb shell pidof org.ghcstudy.v141
adb exec-out screencap -p > emulator-evidence/returned-after-back.png
adb shell uiautomator dump /sdcard/ghc-return.xml >/dev/null
adb pull /sdcard/ghc-return.xml emulator-evidence/returned.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/returned.xml").read_text(errors="replace")
if not any(x in s for x in ("Quiz Mode","Study Mode","Reference")):
    raise SystemExit("System Back did not visibly return to GHC Study")
print("PASS: Android 35 install, WebView launch, glossary navigation, and hardware Back return")
PY
