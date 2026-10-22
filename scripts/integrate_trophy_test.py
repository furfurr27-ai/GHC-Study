#!/usr/bin/env python3
"""Add Trophy Test as its own offline Quiz Mode tile without touching native banks."""
from pathlib import Path
p=Path('app/src/main/assets/index.html')
html=p.read_text(encoding='utf-8')
tag='<script src="trophy-test-launcher.js" id="ghc-trophy-test-launcher"></script>'
if tag in html:raise AssertionError('Trophy launcher already injected')
assert html.count('</body>')==1
assert '<main id="app"' in html
html=html.replace('</body>',tag+'\n</body>',1)
p.write_text(html,encoding='utf-8')
print('PASS: Trophy Test launcher linked in native Quiz Mode without editing existing quiz data')
