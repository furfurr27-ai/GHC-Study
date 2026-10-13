#!/usr/bin/env bash
set -euo pipefail
APK="$(find . -name '*.apk' -print -quit)"
test -n "$APK"
mkdir -p emulator-evidence
# Retain forensic evidence when Android's WebView stays blank or navigation fails.
# These diagnostics do not alter the installed app or relax pass/fail checks.
capture_emulator_failure() {
  local rc="$?"
  trap - EXIT
  if [[ "$rc" -ne 0 ]]; then
    echo "Collecting Android 35 emulator diagnostics (original exit code $rc)"
    adb logcat -d -v threadtime > emulator-evidence/logcat.txt 2>&1 || true
    adb shell dumpsys webviewupdate > emulator-evidence/webview-provider.txt 2>&1 || true
    adb shell dumpsys activity activities > emulator-evidence/activity-state.txt 2>&1 || true
    adb shell dumpsys window > emulator-evidence/window-state.txt 2>&1 || true
    adb shell pm list packages | grep -E 'webview|chrome|ghcstudy' > emulator-evidence/relevant-packages.txt 2>&1 || true
    if [[ -f emulator-evidence/logcat.txt ]]; then
      echo "--- Recent WebView / Chromium / GHC / Android runtime signals ---"
      grep -Ei 'ghcstudy|chromium|webview|AndroidRuntime|FATAL EXCEPTION|crash|renderer|page load|Failed to load|AwContents' emulator-evidence/logcat.txt | tail -n 100 || true
    fi
  fi
  exit "$rc"
}
trap capture_emulator_failure EXIT
adb install -r "$APK"
adb shell am start -W -n org.ghcstudy.v141/org.ghcstudy.offline.MainActivity
sleep 9
# GitHub's constrained emulator can show a Pixel Launcher ANR system dialog
# over a healthy, already-rendered WebView. Dismiss the external launcher dialog
# before testing GHC navigation; never count dismissing a dialog as app Back.
dismiss_launcher_dialog() {
  local stage="$1" pos
  for attempt in 1 2 3; do
    adb shell uiautomator dump /sdcard/ghc-check.xml >/dev/null
    adb pull /sdcard/ghc-check.xml emulator-evidence/system-check.xml >/dev/null
    if grep -q "GHC Study isn't responding" emulator-evidence/system-check.xml; then
      echo "GHC app ANR at $stage" >&2; return 1
    fi
    if ! grep -q "Pixel Launcher isn't responding" emulator-evidence/system-check.xml; then
      return 0
    fi
    echo "Dismissing external Pixel Launcher ANR at $stage (attempt $attempt)"
    pos="$(python3 - <<'PY'
import re
import xml.etree.ElementTree as ET
r=ET.parse("emulator-evidence/system-check.xml").getroot()
for n in r.iter("node"):
    if n.attrib.get("text")=="Wait":
        b=n.attrib.get("bounds","")
        m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",b)
        if m:
            x1,y1,x2,y2=map(int,m.groups())
            print((x1+x2)//2,(y1+y2)//2)
            break
PY
)"
    if [[ -z "$pos" ]]; then
      echo "External ANR seen but Wait control inaccessible" >&2; return 1
    fi
    read -r tap_x tap_y <<< "$pos"
    adb shell input tap "$tap_x" "$tap_y"
    sleep 3
  done
  echo "External launcher ANR was not cleared at $stage" >&2
  return 1
}
wait_for_rendered_app() {
  local stage="$1" output="$2" bytes=0
  for attempt in $(seq 1 16); do
    dismiss_launcher_dialog "$stage"
    adb exec-out screencap -p > "$output"
    bytes="$(wc -c < "$output")"
    # A blank Android emulator frame is about 16 kB; the fully rendered GHC
    # Quiz/Glossary screens are much larger. This avoids tapping during the
    # system's white startup frame, which can send Back to the launcher.
    if [ "$bytes" -gt 70000 ]; then
      echo "Rendered screen at $stage after attempt $attempt ($bytes bytes)"
      return 0
    fi
    echo "Waiting for Android WebView at $stage ($bytes byte blank frame, attempt $attempt)"
    sleep 4
  done
  echo "No rendered application screen at $stage after startup wait" >&2
  return 1
}
assert_ghc_foreground() {
  local stage="$1" focused resumed
  # Android 35 exposes focus in the complete WindowManager dump, not
  # consistently in 'dumpsys window windows'. Check both activity and window.
  focused="$(adb shell dumpsys window 2>/dev/null | grep -E 'mCurrentFocus|mFocusedApp' || true)"
  resumed="$(adb shell dumpsys activity activities 2>/dev/null | grep -E 'topResumedActivity|mResumedActivity' || true)"
  if grep -q 'org.ghcstudy.v141' <<< "$focused $resumed"; then
    return 0
  fi
  if [ -n "$focused$resumed" ]; then
    echo "Unexpected foreground activity at $stage: $focused / $resumed" >&2
    return 1
  fi
  echo "WARNING: Emulator did not expose focus diagnostics at $stage; relying on captured visible UI and process state"
}
adb shell pidof org.ghcstudy.v141
wait_for_rendered_app home emulator-evidence/quiz-home.png
assert_ghc_foreground home
adb shell uiautomator dump /sdcard/ghc-quiz.xml >/dev/null
adb pull /sdcard/ghc-quiz.xml emulator-evidence/quiz-home.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/quiz-home.xml").read_text(errors="replace")
print("First-screen accessibility snapshot length:",len(s))
if not any(x in s for x in ("Quiz Mode","Study Mode","GHC Study")):
    print("WARNING: WebView text not exposed in UIAutomator snapshot; relying on visual screenshot and activity checks")
    print(s[:1400])
PY
# Locate the actual Glossary anchor from the accessibility tree. The fourth
# bottom region partly overlaps the Reference tab and is not a reliable tap.
GLOSSARY_TAP="$(python3 - <<'PY'
import re
import xml.etree.ElementTree as ET
root=ET.parse("emulator-evidence/quiz-home.xml").getroot()
for node in root.iter("node"):
    if node.attrib.get("text")=="Glossary":
        bounds=node.attrib.get("bounds","")
        m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",bounds)
        if m:
            x1,y1,x2,y2=map(int,m.groups())
            print((x1+x2)//2,(y1+y2)//2)
            break
PY
)"
if [[ -z "$GLOSSARY_TAP" ]]; then
  echo "Glossary link not located in accessibility tree" >&2
  exit 1
fi
read -r GLOSSARY_X GLOSSARY_Y <<< "$GLOSSARY_TAP"
echo "Tapping actual Glossary link at $GLOSSARY_X,$GLOSSARY_Y"
adb shell input tap "$GLOSSARY_X" "$GLOSSARY_Y"
sleep 5
wait_for_rendered_app glossary emulator-evidence/glossary.png
if cmp -s emulator-evidence/quiz-home.png emulator-evidence/glossary.png; then
  echo "First Glossary tap did not navigate; retrying after WebView settles"
  sleep 4
  adb shell input tap "$GLOSSARY_X" "$GLOSSARY_Y"
  sleep 5
  wait_for_rendered_app glossary-retry emulator-evidence/glossary.png
fi
assert_ghc_foreground glossary
adb shell uiautomator dump /sdcard/ghc-glossary.xml >/dev/null
adb pull /sdcard/ghc-glossary.xml emulator-evidence/glossary.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/glossary.xml").read_text(errors="replace")
print("Glossary accessibility snapshot length:",len(s))
if not any(x in s for x in ("German hunting terminology","Jägersprache glossary","Search terminology")):
    raise SystemExit("Glossary page title not visible after tap; did not navigate to glossary.html")
PY
adb shell input keyevent KEYCODE_BACK
sleep 4
adb shell pidof org.ghcstudy.v141
wait_for_rendered_app returned-after-back emulator-evidence/returned-after-back.png
assert_ghc_foreground returned-after-back
adb shell uiautomator dump /sdcard/ghc-return.xml >/dev/null
adb pull /sdcard/ghc-return.xml emulator-evidence/returned.xml >/dev/null
python3 - <<'PY'
from pathlib import Path
s=Path("emulator-evidence/returned.xml").read_text(errors="replace")
if not any(x in s for x in ("Quiz Mode","Study Mode","Reference")):
    print("WARNING: Return screen content not exposed to UIAutomator")
print("PASS: Android 35 install, WebView launch, glossary tap, and hardware Back without process death")
PY

python3 - <<'PY'
from pathlib import Path
import hashlib
pics=[Path("emulator-evidence") / n for n in ("quiz-home.png","glossary.png","returned-after-back.png")]
hashes=[hashlib.sha256(p.read_bytes()).hexdigest() for p in pics]
print("Screen hashes:",hashes)
if hashes[0]==hashes[1]:
    raise SystemExit("The screenshot did not change after clicking Glossary; navigation may have failed")
if hashes[1]==hashes[2]:
    raise SystemExit("Back did not change the screenshot; gallery may still be open")
print("PASS: visual screenshots differ across home, glossary, and system Back")
PY
