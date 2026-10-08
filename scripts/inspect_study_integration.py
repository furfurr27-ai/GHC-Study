from pathlib import Path
s=Path('app/src/main/assets/index.html').read_text()
for term in ['STUDY_CARDS=', 'STUDY_CATEGORIES=', 'function renderStudyHub(', 'function renderStudyCategory(', 'function renderStudyCard(', 'function studyCard', 'studyCategory=']:
 p=s.find(term)
 print('===',term,p,'===')
 if p>=0: print(s[max(0,p-160):p+2300])
