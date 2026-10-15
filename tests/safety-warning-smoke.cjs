const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM, VirtualConsole} = require('jsdom');

async function main() {
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => errors.push(String(e)));
  vc.on('error', e => errors.push(String(e)));
  // Add a test-only hook *inside* the app's existing closure. The actual
  // production source is never edited; this avoids unpredictable quiz selection.
  const originalHtml = fs.readFileSync(path.resolve('app/src/main/assets/index.html'), 'utf8');
  const anchor = 'function renderQuestion(){';
  assert.equal(originalHtml.split(anchor).length, 2, 'expected one quiz renderer');
  const html = originalHtml.replace(anchor,
    "window.__ghcTestRenderExactQuestion=function(id){selected={};checked=false;current=window.GHC_QUESTIONS.find(q=>q.id===id);if(!current)throw Error('question ID missing');renderQuestion()};\n"+anchor);
  const dom = new JSDOM(html, {
    url: 'https://ghc.local/', runScripts: 'dangerously', resources: 'usable',
    pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(win) {
      win.scrollTo = () => {};
      win.matchMedia = () => ({matches: false, addListener(){}, removeListener(){}});
    }
  });
  const w = dom.window;
  if (w.document.readyState !== 'complete') {
    await new Promise(resolve => w.addEventListener('load', resolve, {once: true}));
  }
  assert.equal(w.GHC_QUESTIONS.length, 867);
  const disputed = w.GHC_QUESTIONS.find(q => q.id === 'P2013-S3-Q02');
  assert(disputed);
  assert.deepEqual(Array.from(disputed.correct), ['b','c'], 'never alter the archival key');
  assert.equal(disputed.sourceReview?.status, 'source_compared_key_conflict');
  assert(disputed.preAnswerWarning.includes('Legacy key under factual dispute'));
  // Force the actual app renderer to display the disputed question without
  // requiring random selection or altering the offline progress state.
  w.__ghcTestRenderExactQuestion('P2013-S3-Q02');
  const note = w.document.querySelector('.question .alert[role="note"]');
  assert(note, 'source-dispute alert must be visible before grading');
  assert(!note.classList.contains('hidden'));
  assert(note.textContent.includes('Legacy key under factual dispute'));
  assert(!note.textContent.includes('Getting into a car'), 'do not leak the hidden keyed option');
  assert(!w.document.querySelector('#checkBtn').classList.contains('hidden'), 'normal answer control must still exist');
  assert(w.document.querySelector('#feedback').textContent.trim() === '', 'notice comes before grading');
  assert.deepEqual(Array.from(disputed.safetyAcceptedCorrect), ['b','c','d'],
    'alternative safety-complete set must not change archived correct');
  // A candidate selecting the real-world safety-complete set must not receive
  // a false negative from the original 2013 paper's known omission.
  for (const value of ['b', 'c', 'd']) {
    const control = w.document.querySelector('.choice input[value="' + value + '"]');
    assert(control, 'choice ' + value + ' missing');
    control.click();
  }
  w.document.querySelector('#checkBtn').click();
  assert.match(w.document.querySelector('#feedback').textContent, /safety-complete answer/);
  assert.equal(w.document.querySelectorAll('.choice.wrong').length, 0,
    'vehicle option must not be styled as an incorrect choice');
  assert(w.document.querySelector('.choice[data-choice="d"]').classList.contains('correct'));

  // The original paper B/C answer remains accepted for archival fidelity.
  w.__ghcTestRenderExactQuestion('P2013-S3-Q02');
  for (const value of ['b', 'c']) {
    w.document.querySelector('.choice input[value="' + value + '"]').click();
  }
  w.document.querySelector('#checkBtn').click();
  assert.match(w.document.querySelector('#feedback').textContent, /Matched archived 2013 key/);
  assert(w.document.querySelector('.question .alert[role="note"]'), 'warning persists after answer');
  // Other questions must continue to use their original, single answer set.
  w.__ghcTestRenderExactQuestion('H2023-D17-Q018');
  assert(!w.document.querySelector('.question .alert[role="note"]'), 'non-disputed question must not receive conflict warning');
  assert.equal(errors.length, 0, 'runtime errors: ' + errors.join(' | '));
  w.close();
  console.log('PASS: original B/C and safety-complete B/C/D both accepted without altering archived key; pre-answer warning shown');
}

main().catch(error => { console.error(error); process.exitCode = 1; });
