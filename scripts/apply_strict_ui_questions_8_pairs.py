import json
import re

# Load existing BILINGUAL_COURSES
with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)
if not match:
    match = re.search(r'const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)

courses = json.loads(match.group(1))

# Define strict UI questions for each UI language:

# 1. TELUGU UI QUESTIONS (For te-en, te-ta, te-hi)
te_ui_questions = {
    'foundation': [
        'ప్రశ్న: ఈ భాషలో అచ్చులు ఎన్ని ఉన్నాయి?',
        'ప్రశ్న: "అమ్మ" (Mother) అనేది ఏ పదవర్గానికి చెందుతుంది?',
        'ప్రశ్న: "చెట్టు" (Tree) పదానికి బహువచనం ఏది?',
        'ప్రశ్న: "మంచి" (Good) అనేది ఏ పదవర్గం?',
        'ప్రశ్న: "చదువుతున్నాను" (Reading) అనేది ఏ పదవర్గానికి చెందుతుంది?',
        'ప్రశ్న: "పుస్తకం" (Book) అనే పదానికి అర్థం ఏమిటి?',
        'ప్రశ్న: "పాఠశాల" (School) అనే పదానికి అర్థం ఏమిటి?'
    ],
    'beginner': [
        'ప్రశ్న: "నేను పాఠశాలకు వెళుతున్నాను." ఇది ఏ కాలం?',
        'ప్రశ్న: "అతను నిన్న వచ్చాడు." ఇది ఏ కాలం?',
        'ప్రశ్న: "నేను రేపు వెళ్తాను." ఇది ఏ కాలం?',
        'ప్రశ్న: "ఆమె పాట పాడుతోంది." ఇది ఏ కాలం?',
        'ప్రశ్న: "తిన్నాడు" అనేది ఏ కాలాన్ని సూచిస్తుంది?',
        'ప్రశ్న: "చదువుతాను" అనేది ఏ కాలానికి చెందుతుంది?',
        'ప్రశ్న: "ఆడుతున్నాడు" అనేది ఏ కాలానికి ఉదాహరణ?'
    ],
    'intermediate': [
        'ప్రశ్న: "రాము మరియు రవి పాఠశాలకు వెళ్లారు." ఇందులో సంధాన పదం ఏది?',
        'ప్రశ్న: "అమ్మ మరియు నాన్న" లలో సంధాన పదం ఏది?',
        'ప్రశ్న: "అతను చదివాడు, కానీ ఉత్తీర్ణుడు కాలేదు." ఇందులో సంధాన పదం ఏది?',
        'ప్రశ్న: "మరియు" (And) ఏ పదవర్గానికి చెందుతుంది?',
        'ప్రశ్న: "అందువల్ల" (Therefore) అనే పదాన్ని ఎప్పుడు ఉపయోగిస్తారు?',
        'ప్రశ్న: సరైన సంధాన పదం ఏది?',
        'ప్రశ్న: "లేదా" (Or) అంటే ఏమిటి?'
    ],
    'advanced': [
        'ప్రశ్న: రాహుల్ ఎక్కడికి వెళ్తాడు?',
        'ప్రశ్న: రాహుల్ కు ఏమి ఇష్టం?',
        'ప్రశ్న: ఈ గద్యభాగం ఎవరి గురించి?',
        'ప్రశ్న: "ప్రతిరోజూ" అంటే ఏమిటి?',
        'ప్రశ్న: రాహుల్ ఏమి చేస్తాడు?',
        'ప్రశ్న: ఈ గద్యభాగం యొక్క ప్రధాన భావం ఏమిటి?',
        'ప్రశ్న: సరైన వాక్యం ఏది?'
    ]
}

# 2. TAMIL UI QUESTIONS (For ta-en, ta-te, ta-hi)
ta_ui_questions = {
    'foundation': [
        'கேள்வி: இந்த மொழியில் உயிரெழுத்துகள் எத்தனை?',
        'கேள்வி: "அம்மா" (Mother) என்பது எந்த வகைச் சொல்?',
        'கேள்வி: "மரம்" (Tree) என்பதன் பன்மை என்ன?',
        'கேள்வி: "நல்ல" (Good) என்பது எந்த வகைச் சொல்?',
        'கேள்வி: "படிக்கிறேன்" (Reading) என்பது எந்த வகைச் சொல்?',
        'கேள்வி: "புத்தகம்" (Book) என்பதன் பொருள் என்ன?',
        'கேள்வி: "பள்ளி" (School) என்பதன் பொருள் என்ன?'
    ],
    'beginner': [
        'கேள்வி: "நான் பள்ளிக்குச் செல்கிறேன்." இது எந்த காலம்?',
        'கேள்வி: "அவன் நேற்று வந்தான்." இது எந்த காலம்?',
        'கேள்வி: "நான் நாளை செல்வேன்." இது எந்த காலம்?',
        'கேள்வி: "அவள் பாடுகிறாள்." இது எந்த காலம்?',
        'கேள்வி: "சாப்பிட்டான்" என்பது எந்த காலத்தைக் குறிக்கிறது?',
        'கேள்வி: "படிப்பேன்" என்பது எந்த காலத்தைச் சேர்ந்தது?',
        'கேள்வி: "விளையாடுகிறான்" என்பது எந்த காலத்திற்கு உதாரணம்?'
    ],
    'intermediate': [
        'கேள்வி: "ராமும் ரவியும் பள்ளிக்குச் சென்றார்கள்." இதில் இணைப்புச் சொல் எது?',
        'கேள்வி: "அம்மாவும் அப்பாவும்" என்பதில் இணைப்புச் சொல் எது?',
        'கேள்வி: "அவன் படித்தான், ஆனால் தேர்ச்சி பெறவில்லை." இதில் இணைப்புச் சொல் எது?',
        'கேள்வி: "மற்றும்" (And) என்பது எந்த வகைச் சொல்?',
        'கேள்வி: "ஆகையால்" (Therefore) என்ற சொல் எப்போது பயன்படுத்தப்படுகிறது?',
        'கேள்வி: சரியான இணைப்புச் சொல் எது?',
        'கேள்வி: "அல்லது" (Or) என்பதன் பொருள் என்ன?'
    ],
    'advanced': [
        'கேள்வி: ராஹுல் எங்கே செல்கிறான்?',
        'கேள்வி: ராஹுலுக்கு என்ன பிடிக்கும்?',
        'கேள்வி: பகுதி யாரைப் பற்றி?',
        'கேள்வி: "தினமும்" என்பதன் பொருள் என்ன?',
        'கேள்வி: ராஹுல் என்ன செய்கிறான்?',
        'கேள்வி: பகுதியின் முக்கிய கருத்து என்ன?',
        'கேள்வி: சரியான கூற்று எது?'
    ]
}

# 3. HINDI UI QUESTIONS (For hi-ta, hi-te)
hi_ui_questions = {
    'foundation': [
        'प्रश्न: इस भाषा में स्वर कितने होते हैं?',
        'प्रश्न: "अम्बा / माँ" (Mother) किस प्रकार का शब्द है?',
        'प्रश्न: "पेड़" (Tree) का बहुवचन क्या है?',
        'प्रश्न: "अच्छा" (Good) किस प्रकार का शब्द है?',
        'प्रश्न: "पढ़ रहा हूँ" (Reading) किस प्रकार का शब्द है?',
        'प्रश्न: "पुस्तक" (Book) का अर्थ क्या है?',
        'प्रश्न: "स्कूल" (School) का अर्थ क्या है?'
    ],
    'beginner': [
        'प्रश्न: "मैं स्कूल जा रहा हूँ।" यह कौन सा काल है?',
        'प्रश्न: "वह कल आया था।" यह कौन सा काल है?',
        'प्रश्न: "मैं कल जाऊँगा।" यह कौन सा काल है?',
        'प्रश्न: "वह गा रही है।" यह कौन सा काल है?',
        'प्रश्न: "उसने खाया" कौन सा काल दर्शाता है?',
        'प्रश्न: "पढ़ूँगा" किस काल से संबंधित है?',
        'प्रश्न: "खेल रहा है" किस काल का उदाहरण है?'
    ],
    'intermediate': [
        'प्रश्न: "राम और श्याम स्कूल गए।" इसमें संयोजक शब्द कौन सा है?',
        'प्रश्न: "माता और पिता" में संयोजक कौन सा है?',
        'प्रश्न: "उसने पढ़ा लेकिन पास नहीं हुआ।" इसमें संयोजक शब्द कौन सा है?',
        'प्रश्न: "और" (And) किस प्रकार का शब्द है?',
        'प्रश्न: "इसलिए" (Therefore) शब्द का प्रयोग कब किया जाता है?',
        'प्रश्न: सही संयोजक शब्द कौन सा है?',
        'प्रश्न: "या" (Or) का अर्थ क्या है?'
    ],
    'advanced': [
        'प्रश्न: राहुल कहाँ जाता है?',
        'प्रश्न: राहुल को क्या पसंद है?',
        'प्रश्न: यह गद्यांश किसके बारे में है?',
        'प्रश्न: "प्रतिदिन" का अर्थ क्या है?',
        'प्रश्न: राहुल क्या करता है?',
        'प्रश्न: गद्यांश का मुख्य विचार क्या है?',
        'प्रश्न: सही कथन चुनिए।'
    ]
}

# 4. ENGLISH UI QUESTIONS (For en-te)
en_ui_questions = {
    'foundation': [
        'Question: How many vowels are there in this alphabet?',
        'Question: What part of speech is the word "Mother" (Amma)?',
        'Question: What is the plural form of the word "Tree" (Chettu)?',
        'Question: What part of speech is the word "Good" (Manchi)?',
        'Question: What part of speech is the word "Reading" (Chaduvutunnanu)?',
        'Question: What is the meaning of the word "Book" (Pustakam)?',
        'Question: What is the meaning of the word "School" (Pathashala)?'
    ],
    'beginner': [
        'Question: "I am going to school." Which tense is this?',
        'Question: "He came yesterday." Which tense is this?',
        'Question: "I will go tomorrow." Which tense is this?',
        'Question: "She is singing a song." Which tense is this?',
        'Question: "Ate" — Which tense does this indicate?',
        'Question: "Will read" — Which tense does this belong to?',
        'Question: "Is playing" — Which tense is this an example of?'
    ],
    'intermediate': [
        'Question: "Ram and Ravi went to school." Which word is the conjunction?',
        'Question: In "Mother and Father", which word is the conjunction?',
        'Question: "He studied, but he did not pass." Which word is the conjunction?',
        'Question: What part of speech is the word "And"?',
        'Question: When is the word "Therefore" used?',
        'Question: Which of the following is a valid conjunction?',
        'Question: What does the word "Or" mean?'
    ],
    'advanced': [
        'Question: Where does Rahul go?',
        'Question: What does Rahul like to do?',
        'Question: Who is this passage about?',
        'Question: What does the term "Every day" mean?',
        'Question: What does Rahul do every day?',
        'Question: What is the main idea of this passage?',
        'Question: Which statement is correct according to the passage?'
    ]
}

def apply_ui_questions(pair_key, ui_q_map):
    if pair_key not in courses:
        return
    pair_obj = courses[pair_key]
    for lvl_key, lvl_data in pair_obj.items():
        if lvl_key not in ui_q_map:
            continue
        q_texts = ui_q_map[lvl_key]
        for lesson in lvl_data.get('lessons', []):
            pq = lesson.get('practice_questions', [])
            for idx, q in enumerate(pq):
                if idx < len(q_texts):
                    q['question'] = q_texts[idx]
        if 'checkpoint' in lvl_data and 'questions' in lvl_data['checkpoint']:
            for idx, q in enumerate(lvl_data['checkpoint']['questions']):
                if idx < len(q_texts):
                    q['question'] = q_texts[idx]
        if 'checkpoint_test' in lvl_data:
            for idx, q in enumerate(lvl_data['checkpoint_test']):
                if idx < len(q_texts):
                    q['question'] = q_texts[idx]

# Apply to only the 8 requested pairs
apply_ui_questions('te-en', te_ui_questions)
apply_ui_questions('te-ta', te_ui_questions)
apply_ui_questions('te-hi', te_ui_questions)

apply_ui_questions('ta-te', ta_ui_questions)
apply_ui_questions('ta-hi', ta_ui_questions)

apply_ui_questions('hi-ta', hi_ui_questions)
apply_ui_questions('hi-te', hi_ui_questions)

apply_ui_questions('en-te', en_ui_questions)

# Save back to bilingualCourses.js
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

print("Successfully applied 100% strict UI language questions for all 8 requested pairs!")
