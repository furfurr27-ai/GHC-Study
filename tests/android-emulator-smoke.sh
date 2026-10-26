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
# Android's accessibility service may restart while WebView resumes. Retry a
# failed snapshot rather than misdiagnosing it as a broken in-app Back action.
# Persistent UIAutomator failures still fail this regression.
dump_ui() {
  local remote="$1" local_path="$2" attempt
  for attempt in 1 2 3 4; do
    if adb shell uiautomator dump "$remote" >/dev/null 2>&1 \
        && adb pull "$remote" "$local_path" >/dev/null 2>&1 \
        && [[ -s "$local_path" ]]; then
      return 0
    fi
    echo "UIAutomator snapshot retry $attempt: $remote"
    sleep 2
  done
  echo "UIAutomator unavailable after four attempts: $remote" >&2
  return 1
}
adb install -r "$APK"
adb shell am start -W -n org.ghcstudy.v141/org.ghcstudy.offline.MainActivity
sleep 9
# GitHub's constrained emulator can show a Pixel Launcher ANR system dialog
# over a healthy, already-rendered WebView. Dismiss the external launcher dialog
# before testing GHC navigation; never count dismissing a dialog as app Back.
dismiss_launcher_dialog() {
  local stage="$1" pos attempt
  for attempt in 1 2 3; do
    dump_ui /sdcard/ghc-check.xml emulator-evidence/system-check.xml
    if grep -Eq "(GHC Study|Jäger Field Guide) isn.t responding" emulator-evidence/system-check.xml; then
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
# 'Wait' repeatedly reopens the stuck Pixel Launcher ANR on this CI image.
# Close only the *external* launcher process; never close GHC.
for target in ("Close app", "Wait"):
    for n in r.iter("node"):
        if n.attrib.get("text")!=target:
            continue
        b=n.attrib.get("bounds","")
        m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",b)
        if m:
            x1,y1,x2,y2=map(int,m.groups())
            print((x1+x2)//2,(y1+y2)//2)
            break
    else:
        continue
    break
PY
)"
    if [[ -z "$pos" ]]; then
      echo "External Launcher ANR control inaccessible" >&2; return 1
    fi
    read -r tap_x tap_y <<< "$pos"
    adb shell input tap "$tap_x" "$tap_y"
    sleep 3
  done
  echo "External launcher ANR was not cleared at $stage" >&2
  return 1
}
wait_for_rendered_app() {
  local stage="$1" output="$2" bytes=0 attempt
  for attempt in $(seq 1 16); do
    dismiss_launcher_dialog "$stage"
    adb exec-out screencap -p > "$output"
    # A launcher error may overlay a normal-size page after the initial check.
    # Rechecking the dialog here avoids accepting that screenshot as app UI.
    dismiss_launcher_dialog "${stage}-after-screenshot"
    bytes="$(wc -c < "$output")"
    # A blank Android emulator frame is about 16 kB; the fully rendered GHC
    # Quiz/Glossary screens are much larger. This avoids tapping during the
    # system's white startup frame, which can send Back to the launcher.
    if [ "$bytes" -gt 70000 ]; then
      echo "Rendered screen at $stage after attempt $attempt ($bytes bytes)"
      return 0
    fi
    echo "Waiting for Android WebView at $stage ($bytes byte blank frame, attempt $attempt)"
    # GitHub emulator images sometimes leave the WebView surface white even
    # after the Activity starts. Retry one cold Activity launch on fresh CI
    # installs, preserving app data; do not mask Back/navigation failures.
    if [[ "$stage" == "home" && "$attempt" -eq 8 ]]; then
      echo "Cold-relaunching GHC on emulator after eight blank home captures"
      adb shell am force-stop org.ghcstudy.v141
      sleep 2
      adb shell am start -W -n org.ghcstudy.v141/org.ghcstudy.offline.MainActivity
      sleep 5
    fi
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
# The new app opens its offline field reference first. Verify that screen, then
# enter the preserved Study archive before running legacy quiz/glossary checks.
dismiss_launcher_dialog "field-guide-entry"
dump_ui /sdcard/ghc-field-home.xml emulator-evidence/field-guide-home.xml
if ! grep -Eq 'Jäger Field Guide|Jäger Field|Field Guide' emulator-evidence/field-guide-home.xml; then
  echo "New offline field-guide landing screen not visible" >&2; exit 1
fi
# v1.6: Exercise the new state-first flow BEFORE entering the legacy archive.
# Scroll to the accessible state list (city-states have tiny map polygons).
tap_accessible_text() {
  local wanted="$1" stage="$2" found attempt
  for attempt in $(seq 1 14); do
    dismiss_launcher_dialog "state-map-$stage-$attempt"
    dump_ui /sdcard/ghc-state.xml "emulator-evidence/$stage-$attempt.xml"
    found="$(GHC_TEXT="$wanted" GHC_XML="emulator-evidence/$stage-$attempt.xml" python3 - <<'PY'
import os,re,xml.etree.ElementTree as ET
wanted=os.environ['GHC_TEXT']
root=ET.parse(os.environ['GHC_XML']).getroot()
for n in root.iter('node'):
  if n.attrib.get('text','').strip()!=wanted and n.attrib.get('content-desc','').strip()!=wanted: continue
  m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',n.attrib.get('bounds',''))
  if not m: continue
  x1,y1,x2,y2=map(int,m.groups())
  if x2>x1 and y2>y1:
    print((x1+x2)//2,(y1+y2)//2)
    break
PY
)"
    if [[ -n "$found" ]]; then
      read -r gx gy <<< "$found"
      adb shell input tap "$gx" "$gy"
      sleep 2
      return 0
    fi
    local dims sw sh
    dims="$(adb shell wm size | grep -oE '[0-9]+x[0-9]+' | tail -n 1 | tr -d '\r')"
    sw="${dims%x*}"; sh="${dims#*x}"
    adb shell input swipe "$((sw/2))" "$((sh*80/100))" "$((sw/2))" "$((sh*28/100))" 375
    sleep 1
  done
  echo "Accessibility control '$wanted' not found after bounded scrolling during $stage" >&2
  return 1
}
tap_accessible_text "Hessen" "select-hessen"
wait_for_rendered_app hessen emulator-evidence/hessen-home.png
tap_accessible_text "Wildarten" "wildarten"
wait_for_rendered_app animals emulator-evidence/state-animals.png
tap_accessible_text "Rehwild" "rehwild-card"
wait_for_rendered_app animal-detail emulator-evidence/rehwild-state-detail.png
# The current selected-state strip and explicit non-authorization label must be readable.
dump_ui /sdcard/ghc-rehwild-detail.xml emulator-evidence/rehwild-state-detail.xml
if ! grep -q "Not authorization" emulator-evidence/rehwild-state-detail.xml; then
  echo "Selected-state animal card lacks visible non-authorization caution" >&2; exit 1
fi
adb shell input keyevent 4
sleep 3
wait_for_rendered_app animals-back emulator-evidence/state-animals-after-back.png
adb shell input keyevent 4
sleep 3
wait_for_rendered_app state-back emulator-evidence/hessen-home-after-back.png
adb shell input keyevent 4
sleep 3
wait_for_rendered_app map-back emulator-evidence/germany-map-after-back.png
dump_ui /sdcard/ghc-map-back.xml emulator-evidence/germany-map-after-back.xml
if ! grep -q 'Select a state\|Bundesland auswählen' emulator-evidence/germany-map-after-back.xml; then
  echo "Android Back did not return to Germany state map" >&2; exit 1
fi
# Capture the archive target again after scrolling and Back navigation.
dump_ui /sdcard/ghc-field-home.xml emulator-evidence/field-guide-home.xml
FIELD_ARCHIVE_TAP="$(python3 - <<'PY'
import re,xml.etree.ElementTree as ET
root=ET.parse("emulator-evidence/field-guide-home.xml").getroot()
for n in root.iter("node"):
  t=n.attrib.get("text","").strip()
  if t=="Study archive":
    m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",n.attrib.get("bounds",""))
    if m:
      x1,y1,x2,y2=map(int,m.groups())
      print((x1+x2)//2,(y1+y2)//2)
      break
PY
)"
if [[ -z "$FIELD_ARCHIVE_TAP" ]]; then echo "Study archive link missing" >&2; exit 1; fi
read -r FIELD_X FIELD_Y <<< "$FIELD_ARCHIVE_TAP"
adb shell input tap "$FIELD_X" "$FIELD_Y"
sleep 4
wait_for_rendered_app archive emulator-evidence/study-archive.png
assert_ghc_foreground archive
# Pixel Launcher ANRs can appear between the initial render and a second
# UIAutomator call. Never parse a system dialog as an application's UI.
for attempt in $(seq 1 8); do
  dismiss_launcher_dialog "before-quiz-accessibility-$attempt"
  dump_ui /sdcard/ghc-quiz.xml emulator-evidence/quiz-home.xml
  if grep -q "Pixel Launcher isn't responding" emulator-evidence/quiz-home.xml; then
    echo "Launcher dialog reappeared during quiz accessibility capture ($attempt)"
    sleep 2
    continue
  fi
  if grep -q 'text="Glossary"' emulator-evidence/quiz-home.xml; then
    break
  fi
  echo "Glossary anchor not visible in quiz accessibility tree ($attempt)"
  sleep 2
done
if ! grep -q 'text="Glossary"' emulator-evidence/quiz-home.xml; then
  echo "Glossary anchor missing after launcher-dialog recovery attempts" >&2
  exit 1
fi
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
for attempt in $(seq 1 8); do
  dismiss_launcher_dialog "before-glossary-accessibility-$attempt"
  dump_ui /sdcard/ghc-glossary.xml emulator-evidence/glossary.xml
  if grep -q "Pixel Launcher isn't responding" emulator-evidence/glossary.xml; then
    echo "Launcher dialog reappeared during glossary accessibility capture ($attempt)"
    sleep 2
    continue
  fi
  if grep -Eq 'German hunting terminology|Jägersprache glossary|Search terminology' emulator-evidence/glossary.xml; then
    break
  fi
  echo "Glossary content not visible in accessibility tree ($attempt)"
  sleep 2
done
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
dump_ui /sdcard/ghc-return.xml emulator-evidence/returned.xml
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


# Follow-up navigation coverage. The glossary is a separate WebView page; these
# cases exercise the native-JS Back bridge *within* index.html.
tap_visible_label() {
  local label="$1" stage="$2" pos="" attempt
  for attempt in $(seq 1 6); do
    dismiss_launcher_dialog "$stage"
    dump_ui /sdcard/ghc-nav.xml emulator-evidence/navigation-current.xml
    pos="$(GHC_NAV_LABEL="$label" python3 - <<'PY'
import os,re,xml.etree.ElementTree as ET
label=os.environ["GHC_NAV_LABEL"]
root=ET.parse("emulator-evidence/navigation-current.xml").getroot()
for n in root.iter("node"):
    value=n.attrib.get("text","").strip()
    if value!=label and not value.startswith(label+" "): continue
    m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",n.attrib.get("bounds",""))
    if not m: continue
    x1,y1,x2,y2=map(int,m.groups())
    if x2>x1 and y2>y1 and y1<2350:
        print((x1+x2)//2,(y1+y2)//2)
        break
PY
)"
    if [[ -n "$pos" ]]; then
      local x y
      read -r x y <<< "$pos"
      echo "Tapping $label at $x,$y ($stage)"
      adb shell input tap "$x" "$y"
      sleep 3
      return 0
    fi
    echo "Waiting for visible '$label' ($stage attempt $attempt)"
    sleep 2
  done
  echo "Could not locate '$label' for $stage" >&2
  return 1
}
assert_visible_text() {
  local label="$1" stage="$2" attempt
  # WebView page navigation may expose the new title before the next document
  # finishes painting its buttons. Poll the real accessibility tree rather than
  # marking a slow but valid page as a failed app navigation.
  for attempt in 1 2 3 4 5 6; do
    dump_ui /sdcard/ghc-verify.xml "emulator-evidence/verify-$stage.xml"
    if GHC_NAV_LABEL="$label" GHC_NAV_XML="emulator-evidence/verify-$stage.xml" python3 - <<'PY'
import os,re,xml.etree.ElementTree as ET
root=ET.parse(os.environ["GHC_NAV_XML"]).getroot()
needle=os.environ["GHC_NAV_LABEL"]
for n in root.iter("node"):
    value=n.attrib.get("text","").strip()
    if value!=needle and not value.startswith(needle+" "):continue
    m=re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]",n.attrib.get("bounds",""))
    if not m:continue
    x1,y1,x2,y2=map(int,m.groups())
    if x2>x1 and y2>y1 and y1<2150:
        print("PASS: visible",needle)
        break
else:
    raise SystemExit("Not yet visible: "+needle)
PY
    then return 0; fi
    echo "Waiting for '$label' to render ($stage, attempt $attempt/6)"
    sleep 2
  done
  echo "Expected visible content not found after six UI snapshots: $label ($stage)" >&2
  return 1
}
tap_visible_label "Reference" reference-tab
assert_ghc_foreground reference-tab
assert_visible_text "Reference" reference-content
adb shell input keyevent KEYCODE_BACK
sleep 3
assert_ghc_foreground back-from-reference
assert_visible_text "Quiz Mode" back-from-reference
# Verify Trophy Test's real native Quiz Mode entry opens the packaged offline
# baseball cards, supports the identification tab, and system Back works.
tap_visible_label "Trophy Test" trophy-test-entry
assert_ghc_foreground trophy-test-page
assert_visible_text "Trophy Test" trophy-test-heading
assert_visible_text "Cards" trophy-test-cards
tap_visible_label "Identify" trophy-identify-mode
assert_visible_text "Which animal is shown in this exam-room mount?" trophy-identify-question
adb shell input keyevent KEYCODE_BACK
sleep 3
assert_ghc_foreground back-from-trophy-test
assert_visible_text "Quiz Mode" back-from-trophy-test
tap_visible_label "Study Mode" study-tab
assert_visible_text "Schalenwild" study-hub
tap_visible_label "Schalenwild" hoofed-category
# The expanded comparison matrix also includes a non-clickable "Rehwild" row.
# Verify the new panel is present, collapse it, then tap the actual study card.
# This avoids selecting a table row instead of a Rehwild study-card tile.
assert_visible_text "Schalenwild · Vergleichsmatrizen" hoofed-matrix
tap_visible_label "Schalenwild · Vergleichsmatrizen" collapse-hoofed-matrix
assert_visible_text "Rehwild" hoofed-list
tap_visible_label "Rehwild" roe-study-card
assert_visible_text "Details" roe-card-detail
adb exec-out screencap -p > emulator-evidence/study-card-before-back.png
adb shell input keyevent KEYCODE_BACK
sleep 3
assert_ghc_foreground back-from-study-card
assert_visible_text "Schalenwild" back-from-study-card
# The category should show its Rehwild tile; card detail should have been closed.
assert_visible_text "Rehwild" returned-hoofed-list
adb exec-out screencap -p > emulator-evidence/study-category-after-back.png
if cmp -s emulator-evidence/study-card-before-back.png emulator-evidence/study-category-after-back.png; then
  echo "Back did not change the Rehwild study-card screen" >&2
  exit 1
fi
echo "PASS: Android system Back from Reference to Quiz and Rehwild card to Schalenwild category"
