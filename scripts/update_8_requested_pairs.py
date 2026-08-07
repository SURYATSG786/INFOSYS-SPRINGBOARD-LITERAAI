import json, re

from build_ta_hi import build_ta_hi
from build_hi_ta import build_hi_ta
from rebuild_requested_8_pairs import build_te_en, build_en_te
from build_remaining_4_pairs import build_te_ta, build_ta_te, build_hi_te, build_te_hi

# Load existing BILINGUAL_COURSES from file
with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)
if not match:
    match = re.search(r'const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)

courses = json.loads(match.group(1))

# Update ONLY the 8 requested pairs
courses['te-en'] = build_te_en()
courses['en-te'] = build_en_te()
courses['te-ta'] = build_te_ta()
courses['ta-te'] = build_ta_te()
courses['hi-ta'] = build_hi_ta()
courses['ta-hi'] = build_ta_hi()
courses['hi-te'] = build_hi_te()
courses['te-hi'] = build_te_hi()

new_json_str = json.dumps(courses, indent=2, ensure_ascii=False)

new_file_content = f'''export const BILINGUAL_COURSES = {new_json_str};

export function getBilingualCourse(courseIdOrPath, uiLang, learnLang) {{
  if (!uiLang || !learnLang) return null;
  const pairKey = uiLang + '-' + learnLang;
  const pairCourses = BILINGUAL_COURSES[pairKey];
  if (!pairCourses) return null;

  const key = courseIdOrPath.split('-')[0].trim();
  const levelKey = key.toLowerCase();
  
  if (pairCourses[levelKey]) return pairCourses[levelKey];
  
  for (const lvl of ['foundation', 'beginner', 'intermediate', 'advanced']) {{
    if (courseIdOrPath.toLowerCase().includes(lvl)) return pairCourses[lvl];
  }}
  return null;
}}

export function loadBilingualCoursesList(uiLang, learnLang) {{
  if (!uiLang || !learnLang) return null;
  const pairKey = uiLang + '-' + learnLang;
  const pairCourses = BILINGUAL_COURSES[pairKey];
  if (!pairCourses) return null;
  return Object.values(pairCourses);
}}
'''

with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print("Successfully updated only the 8 requested pairs in bilingualCourses.js!")
