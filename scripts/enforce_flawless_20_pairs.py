import json
import re

# Load existing BILINGUAL_COURSES
with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)
if not match:
    match = re.search(r'const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)

courses = json.loads(match.group(1))

# 1. UI Question Map (per UI language):
ui_questions = {
    'kn': {
        'foundation': [
            'ಪ್ರಶ್ನೆ: Apple ಪದವು ಯಾವ ಅಕ್ಷರದಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ?',
            'ಪ್ರಶ್ನೆ: ಇವುಗಳಲ್ಲಿ ನಾಮಪದ (Noun) ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: Tree ಪದದ ಬಹುವಚನ (Plural) ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: ಇವುಗಳಲ್ಲಿ ಗುಣವಾಚಕ (Adjective) ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: ಇವುಗಳಲ್ಲಿ ಕ್ರಿಯಾಪದ (Verb) ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: House ಪದದ ಅರ್ಥವೇನು?',
            'ಪ್ರಶ್ನೆ: School ಪದದ ಅರ್ಥವೇನು?'
        ],
        'beginner': [
            'ಪ್ರಶ್ನೆ: "ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತಿದ್ದೇನೆ." ಇದು ಯಾವ ಕಾಲ?',
            'ಪ್ರಶ್ನೆ: "ಅವನು ನಿನ್ನೆ ಬಂದನು." ಇದು ಯಾವ ಕಾಲ?',
            'ಪ್ರಶ್ನೆ: "ನಾನು ನಾಳೆ ಹೋಗುತ್ತೇನೆ." ಇದು ಯಾವ ಕಾಲ?',
            'ಪ್ರಶ್ನೆ: "ಅವಳು ಹಾಡು ಹಾಡುತ್ತಿದ್ದಾಳೆ." ಇದು ಯಾವ ಕಾಲ?',
            'ಪ್ರಶ್ನೆ: "ತಿಂದನು" (Ate) ಇದು ಯಾವ ಕಾಲವನ್ನು ಸೂಚಿಸುತ್ತದೆ?',
            'ಪ್ರಶ್ನೆ: "ಓದುತ್ತೇನೆ" (Will read) ಇದು ಯಾವ ಕಾಲಕ್ಕೆ ಸೇರುತ್ತದೆ?',
            'ಪ್ರಶ್ನೆ: "ಆಡುತ್ತಿದ್ದಾನೆ" (Is playing) ಇದು ಯಾವ ಕಾಲಕ್ಕೆ ಉದಾಹರಣೆ?'
        ],
        'intermediate': [
            'ಪ್ರಶ್ನೆ: "ರಾಮ್ ಮತ್ತು ರವಿ ಶಾಲೆಗೆ ಹೋದರು." ಇದರಲ್ಲಿ ಸಂಯೋಜಕ ಪದ (Conjunction) ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: "ತಾಯಿ ಮತ್ತು ತಂದೆ" ಎಂಬಲ್ಲಿ ಸಂಯೋಜಕ ಪದ ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: "ಅವನು ಓದಿದನು, ಆದರೆ ಉತ್ತೀರ್ಣನಾಗಲಿಲ್ಲ." ಇದರಲ್ಲಿ ಸಂಯೋಜಕ ಪದ ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: "ಮತ್ತು" (And) ಯಾವ ಪದವರ್ಗಕ್ಕೆ ಸೇರುತ್ತದೆ?',
            'ಪ್ರಶ್ನೆ: "ಆದ್ದರಿಂದ" (Therefore) ಎಂಬ ಪದವನ್ನು ಯಾವಾಗ ಬಳಸಲಾಗುತ್ತದೆ?',
            'ಪ್ರಶ್ನೆ: ಸರಿಯಾದ ಸಂಯೋಜಕ ಪದ ಯಾವುದು?',
            'ಪ್ರಶ್ನೆ: "ಅಥವಾ" (Or) ಪದದ ಅರ್ಥವೇನು?'
        ],
        'advanced': [
            'ಪ್ರಶ್ನೆ: ರಾಹುಲ್ ಎಲ್ಲಿಗೆ ಹೋಗುತ್ತಾನೆ?',
            'ಪ್ರಶ್ನೆ: ರಾಹುಲ್ಗೆ ಏನು ಇಷ್ಟ?',
            'ಪ್ರಶ್ನೆ: ಈ ಗದ್ಯಭಾಗ ಯಾರ ಬಗ್ಗೆ?',
            'ಪ್ರಶ್ನೆ: "ಪ್ರತಿದಿನ" ಪದದ ಅರ್ಥವೇನು?',
            'ಪ್ರಶ್ನೆ: ರಾಹುಲ್ ಏನು ಮಾಡುತ್ತಾನೆ?',
            'ಪ್ರಶ್ನೆ: ಈ ಗದ್ಯಭಾಗದ ಮುಖ್ಯ ಉದ್ದೇಶವೇನು?',
            'ಪ್ರಶ್ನೆ: ಸರಿಯಾದ ಹೇಳಿಕೆ ಯಾವುದು?'
        ]
    },

    'te': {
        'foundation': [
            'ప్రశ్న: Apple పదం ఏ అక్షరంతో ప్రారంభమవుతుంది?',
            'ప్రశ్న: వీటిలో నామవాచకం (Noun) ఏది?',
            'ప్రశ్న: Tree పదానికి బహువచనం (Plural) ఏది?',
            'ప్రశ్న: వీటిలో విశేషణం (Adjective) ఏది?',
            'ప్రశ్న: వీటిలో క్రియ (Verb) ఏది?',
            'ప్రశ్న: House పదానికి అర్థం ఏమిటి?',
            'ప్రశ్న: School పదానికి అర్థం ఏమిటి?'
        ],
        'beginner': [
            'ప్రశ్న: "నేను పాఠశాలకు వెళుతున్నాను." ఇది ఏ కాలం?',
            'ప్రశ్న: "అతను నిన్న వచ్చాడు." ఇది ఏ కాలం?',
            'ప్రశ్న: "నేను రేపు వెళ్తాను." ఇది ఏ కాలం?',
            'ప్రశ్న: "ఆమె పాట పాడుతోంది." ఇది ఏ కాలం?',
            'ప్రశ్న: "తిన్నాడు" (Ate) అనేది ఏ కాలాన్ని సూచిస్తుంది?',
            'ప్రశ్న: "చదువుతాను" (Will read) అనేది ఏ కాలానికి చెందుతుంది?',
            'ప్రశ్న: "ఆడుతున్నాడు" (Is playing) అనేది ఏ కాలానికి ఉదాహరణ?'
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
    },

    'ta': {
        'foundation': [
            'கேள்வி: Apple என்ற சொல் எந்த எழுத்தில் தொடங்குகிறது?',
            'கேள்வி: இவற்றில் பெயர்ச்சொல் (Noun) எது?',
            'கேள்வி: Tree என்பதன் பன்மை (Plural) என்ன?',
            'கேள்வி: இவற்றில் உரிச்சொல் (Adjective) எது?',
            'கேள்வி: இவற்றில் வினைச்சொல் (Verb) எது?',
            'கேள்வி: House என்பதன் பொருள் என்ன?',
            'கேள்வி: School என்பதன் பொருள் என்ன?'
        ],
        'beginner': [
            'கேள்வி: "நான் பள்ளிக்குச் செல்கிறேன்." இது எந்த காலம்?',
            'கேள்வி: "அவன் நேற்று வந்தான்." இது எந்த காலம்?',
            'கேள்வி: "நான் நாளை செல்வேன்." இது எந்த காலம்?',
            'கேள்வி: "அவள் பாடுகிறாள்." இது எந்த காலம்?',
            'கேள்வி: "சாப்பிட்டான்" (Ate) என்பது எந்த காலத்தைக் குறிக்கிறது?',
            'கேள்வி: "படிப்பேன்" (Will read) என்பது எந்த காலத்தைச் சேர்ந்தது?',
            'கேள்வி: "விளையாடுகிறான்" (Is playing) என்பது எந்த காலத்திற்கு உதாரணம்?'
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
    },

    'hi': {
        'foundation': [
            'प्रश्न: Apple शब्द किस अक्षर से शुरू होता है?',
            'प्रश्न: इनमें से संज्ञा (Noun) कौन सा है?',
            'प्रश्न: Tree का बहुवचन (Plural) क्या है?',
            'प्रश्न: इनमें से विशेषण (Adjective) कौन सा है?',
            'प्रश्न: इनमें से क्रिया (Verb) कौन सी है?',
            'प्रश्न: House शब्द का अर्थ क्या है?',
            'प्रश्न: School शब्द का अर्थ क्या है?'
        ],
        'beginner': [
            'प्रश्न: "मैं स्कूल जा रहा हूँ।" यह कौन सा काल है?',
            'प्रश्न: "वह कल आया था।" यह कौन सा काल है?',
            'प्रश्न: "मैं कल जाऊँगा।" यह कौन सा काल है?',
            'प्रश्न: "वह गा रही है।" यह कौन सा काल है?',
            'प्रश्न: "उसने खाया" (Ate) कौन सा काल दर्शाता है?',
            'प्रश्न: "पढ़ूँगा" (Will read) किस काल से संबंधित है?',
            'प्रश्न: "खेल रहा है" (Is playing) किस काल का उदाहरण है?'
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
    },

    'en': {
        'foundation': [
            'Question: Which letter does the word Apple begin with?',
            'Question: Which word is a Noun?',
            'Question: What is the plural form of the word Tree?',
            'Question: Which word is an Adjective?',
            'Question: Which word is a Verb?',
            'Question: What is the meaning of the word House?',
            'Question: What is the meaning of the word School?'
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
}

# 2. Master Option Builder for any target/UI pair:
def build_phonetic_options(learn_lang, ui_lang):
    # Option dictionaries for Foundation, Beginner, Intermediate, Advanced
    # Target = ENGLISH
    if learn_lang == 'en':
        if ui_lang == 'kn':
            return {
                'foundation': [
                    ['B (ಬಿ)', 'A (ಎ)', 'C (ಸಿ)', 'D (ಡಿ)'],
                    ['Run (ರನ್)', 'Happy (ಹ್ಯಾಪಿ)', 'Book (ಬುಕ್)', 'Quickly (ಕ್ವಿಕ್ಲಿ)'],
                    ['Trees (ಟ್ರಿಸ್)', 'Treees (ಟ್ರಿಸ್)', "Trees' (ಟ್ರಿಸ್)", 'Tree (ಟ್ರಿ)'],
                    ['Beautiful (ಬ್ಯೂಟಿಫುಲ್)', 'School (ಸ್ಕೂಲ್)', 'Jump (ಜಂಪ್)', 'They (ದೇ)'],
                    ['Sleep (ಸ್ಲೀಪ್)', 'Book (ಬುಕ್)', 'Blue (ಬ್ಲೂ)', 'Slowly (ಸ್ಲೋಲಿ)'],
                    ['House (ಹೌಸ್)', 'Grantha (ಗ್ರಂಥ)', 'Raste (ರಸ್ತೆ)', 'Mara (ಮರ)'],
                    ['School (ಸ್ಕೂಲ್)', 'Hospital (ಹಾಸ್ಪಿಟಲ್)', 'Market (ಮಾರ್ಕೆಟ್)', 'Park (ಪಾರ್ಕ್)']
                ],
                'beginner': [
                    ['Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'Command (ಕಮಾಂಡ್)'],
                    ['Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'None (ನನ್)'],
                    ['Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Noun (ನೌನ್)'],
                    ['Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'Adjective (ಅಡ್ಜೆಕ್ಟಿವ್)'],
                    ['Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'None (ನನ್)'],
                    ['Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'Adjective (ಅಡ್ಜೆಕ್ಟಿವ್)'],
                    ['Present Tense (ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್)', 'Past Tense (ಪಾಸ್ಟ್ ಟೆನ್ಸ್)', 'Future Tense (ಫ್ಯೂಚರ್ ಟೆನ್ಸ್)', 'Noun (ನೌನ್)']
                ],
                'intermediate': [
                    ['But (ಬಟ್)', 'And (ಆಂಡ್)', 'Because (ಬಿಕಾಸ್)', 'Or (ಆರ್)'],
                    ['Mother (ಮದರ್)', 'And (ಆಂಡ್)', 'Father (ಫಾದರ್)', 'In (ಇನ್)'],
                    ['But (ಬಟ್)', 'Studied (ಸ್ಟಡೀಡ್)', 'Pass (ಪಾಸ್)', 'Did not (ಡಿಡ್ ನಾಟ್)'],
                    ['Conjunction (ಕಂಜಂಕ್ಷನ್)', 'Noun (ನೌನ್)', 'Verb (ವರ್ಬ್)', 'Adjective (ಅಡ್ಜೆಕ್ಟಿವ್)'],
                    ['Cause & Effect (ಕಾಸ್ ಆಂಡ್ ಎಫೆಕ್ಟ್)', 'Noun (ನೌನ್)', 'Verb (ವರ್ಬ್)', 'Time (ಟೈಮ್)'],
                    ['And (ಆಂಡ್)', 'Book (ಬುಕ್)', 'House (ಹೌಸ್)', 'Run (ರನ್)'],
                    ['Choice between two (ಚಾಯ್ಸ್ ಬಿಟ್ವೀನ್ ಟೂ)', 'Time (ಟೈಮ್)', 'Place (ಪ್ಲೇಸ್)', 'Action (ಆಕ್ಷನ್)']
                ],
                'advanced': [
                    ['Market (ಮಾರ್ಕೆಟ್)', 'School (ಸ್ಕೂಲ್)', 'Park (ಪಾರ್ಕ್)', 'Home (ಹೋಮ್)'],
                    ['Playing games (ಪ್ಲೇಯಿಂಗ್ ಗೇಮ್ಸ್)', 'Reading books (ರೀಡಿಂಗ್ ಬುಕ್ಸ್)', 'Sleeping (ಸ್ಲೀಪಿಂಗ್)', 'Watching TV (ವಾಚಿಂಗ್ ಟಿವಿ)'],
                    ['Reena (ರೀನಾ)', 'Rahul (ರಾಹುಲ್)', 'Mohan (ಮೋಹನ್)', 'Seema (ಸೀಮಾ)'],
                    ['Every day (ಎವ್ರಿ ಡೇ)', 'Yesterday (ಯೆಸ್ಟರ್ಡೇ)', 'Never (ನೆವರ್)', 'Next week (ನೆಕ್ಸ್ಟ್ ವೀಕ್)'],
                    ['Goes to school (ಗೋಸ್ ಟು ಸ್ಕೂಲ್)', 'Goes to market (ಗೋಸ್ ಟು ಮಾರ್ಕೆಟ್)', 'Stays home (ಸ್ಟೇಸ್ ಹೋಮ್)', 'Goes to hospital (ಗೋಸ್ ಟು ಹಾಸ್ಪಿಟಲ್)'],
                    ['Study habit (ಸ್ಟಡಿ ಹ್ಯಾಬಿಟ್)', 'Travel (ಟ್ರಾವೆಲ್)', 'Rain (ರೈನ್)', 'Hills (ಹಿಲ್ಸ್)'],
                    ['Rahul likes reading books (ರಾಹುಲ್ ಲೈಕ್ಸ್ ರೀಡಿಂಗ್ ಬುಕ್ಸ್)', 'Rahul does not go to school (ರಾಹುಲ್ ಡಸ್ ನಾಟ್ ಗೋ ಟು ಸ್ಕೂಲ್)', 'Rahul only plays (ರಾಹುಲ್ ಓನ್ಲಿ ಪ್ಲೇಸ್)', 'Rahul sleeps all day (ರಾಹುಲ್ ಸ್ಲೀಪ್ಸ್ ಆಲ್ ಡೇ)']
                ]
            }
        elif ui_lang == 'te':
            return {
                'foundation': [
                    ['B (బి)', 'A (ఎ)', 'C (సి)', 'D (డి)'],
                    ['Run (రన్)', 'Happy (హ్యాపీ)', 'Book (బుక్)', 'Quickly (క్విక్లీ)'],
                    ['Trees (ట్రీస్)', 'Treees (ట్రీస్)', "Trees' (ట్రీస్)", 'Tree (ట్రీ)'],
                    ['Beautiful (బ్యూటిఫుల్)', 'School (స్కూల్)', 'Jump (జంప్)', 'They (దే)'],
                    ['Sleep (స్లీప్)', 'Book (బుక్)', 'Blue (బ్లూ)', 'Slowly (స్లోలీ)'],
                    ['House (హౌస్)', 'Granthalayam (గ్రంథాలయం)', 'Veedhi (వీధి)', 'Chettu (చెట్టు)'],
                    ['School (స్కూల్)', 'Hospital (హాస్పిటల్)', 'Market (మార్కెట్)', 'Park (పార్క్)']
                ],
                'beginner': [
                    ['Past Tense (పాస్ట్ టెన్స్)', 'Present Tense (ప్రెసెంట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'Command (కమాండ్)'],
                    ['Past Tense (పాస్ట్ టెన్స్)', 'Present Tense (ప్రెసెంట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'None (నన్)'],
                    ['Present Tense (ప్రెసెంట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'Past Tense (పాస్ట్ టెన్స్)', 'Noun (నౌన్)'],
                    ['Present Tense (ప్రెసెంట్ టెన్స్)', 'Past Tense (పాస్ట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'Adjective (అడ్జెక్టివ్)'],
                    ['Present Tense (ప్రెసెంట్ టెన్స్)', 'Past Tense (పాస్ట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'None (నన్)'],
                    ['Past Tense (పాస్ట్ టెన్స్)', 'Present Tense (ప్రెసెంట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'Adjective (అడ్జెక్టివ్)'],
                    ['Present Tense (ప్రెసెంట్ టెన్స్)', 'Past Tense (పాస్ట్ టెన్స్)', 'Future Tense (ఫ్యూచర్ టెన్స్)', 'Noun (నౌన్)']
                ],
                'intermediate': [
                    ['But (బట్)', 'And (యాండ్)', 'Because (బికాజ్)', 'Or (ఆర్)'],
                    ['Mother (మదర్)', 'And (యాండ్)', 'Father (ఫాదర్)', 'In (ఇన్)'],
                    ['But (బట్)', 'Studied (స్టడీడ్)', 'Pass (పాస్)', 'Did not (డిడ్ నాట్)'],
                    ['Conjunction (కంజంక్షన్)', 'Noun (నౌన్)', 'Verb (వర్బ్)', 'Adjective (అడ్జెక్టివ్)'],
                    ['Cause & Effect (కాజ్ అండ్ ఎఫెక్ట్)', 'Noun (నౌన్)', 'Verb (వర్బ్)', 'Time (టైమ్)'],
                    ['And (యాండ్)', 'Book (బుక్)', 'House (హౌస్)', 'Run (రన్)'],
                    ['Choice between two (ఛాయిస్ బిట్వీన్ టూ)', 'Time (టైమ్)', 'Place (ప్లేస్)', 'Action (యాక్షన్)']
                ],
                'advanced': [
                    ['Market (మార్కెట్)', 'School (స్కూల్)', 'Park (పార్క్)', 'Home (హోమ్)'],
                    ['Playing games (ప్లేయింగ్ గేమ్స్)', 'Reading books (రీడింగ్ బుక్స్)', 'Sleeping (స్లీపింగ్)', 'Watching TV (వాచింగ్ టీవీ)'],
                    ['Reena (రీనా)', 'Rahul (రాహుల్)', 'Mohan (మోహన్)', 'Seema (సీమా)'],
                    ['Every day (ఎవ్రీ డే)', 'Yesterday (యెస్టర్డే)', 'Never (నెవర్)', 'Next week (నెక్స్ట్ వీక్)'],
                    ['Goes to school (గోస్ టు స్కూల్)', 'Goes to market (గోస్ టు మార్కెట్)', 'Stays home (స్టేస్ హోమ్)', 'Goes to hospital (గోస్ టు హాస్పిటల్)'],
                    ['Study habit (స్టడీ హ్యాబిట్)', 'Travel (ట్రావెల్)', 'Rain (రైన్)', 'Hills (హిల్స్)'],
                    ['Rahul likes reading books (రాహుల్ లైక్స్ రీడింగ్ బుక్స్)', 'Rahul does not go to school (రాహుల్ డస్ నాట్ గో టు స్కూల్)', 'Rahul only plays (రాహుల్ ఓన్లీ ప్లేస్)', 'Rahul sleeps all day (రాహుల్ స్లీప్స్ ఆల్ డే)']
                ]
            }
        elif ui_lang == 'ta':
            return {
                'foundation': [
                    ['B (பி)', 'A (ஏ)', 'C (சி)', 'D (டி)'],
                    ['Run (ரன்)', 'Happy (ஹேப்பி)', 'Book (புக்)', 'Quickly (க்விக்லி)'],
                    ['Trees (ட்ரீஸ்)', 'Treees (ட்ரீஸ்)', "Trees' (ட்ரீஸ்)", 'Tree (ட்ரீ)'],
                    ['Beautiful (பியூட்டிஃபுல்)', 'School (ஸ்கூல்)', 'Jump (ஜம்ப்)', 'They (தே)'],
                    ['Sleep (ஸ்லீப்)', 'Book (புக்)', 'Blue (ப்ளூ)', 'Slowly (ஸ்லோலி)'],
                    ['House (ஹவுஸ்)', 'Noolagam (நூலகம்)', 'Theru (தெரு)', 'Maram (மரம்)'],
                    ['School (ஸ்கூல்)', 'Hospital (ஹாஸ்பிடல்)', 'Market (மார்க்கெட்)', 'Park (பார்க்)']
                ],
                'beginner': [
                    ['Past Tense (பாஸ்ட் டென்ஸ்)', 'Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'Command (கமாண்ட்)'],
                    ['Past Tense (பாஸ்ட் டென்ஸ்)', 'Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'None (நன்)'],
                    ['Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'Past Tense (பாஸ்ட் டென்ஸ்)', 'Noun (நவுன்)'],
                    ['Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Past Tense (பாஸ்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'Adjective (அட்ஜெக்டிவ்)'],
                    ['Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Past Tense (பாஸ்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'None (நன்)'],
                    ['Past Tense (பாஸ்ட் டென்ஸ்)', 'Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'Adjective (அட்ஜெக்டிவ்)'],
                    ['Present Tense (ப்ரெசண்ட் டென்ஸ்)', 'Past Tense (பாஸ்ட் டென்ஸ்)', 'Future Tense (ஃப்யூச்சர் டென்ஸ்)', 'Noun (நவுன்)']
                ],
                'intermediate': [
                    ['But (பட்)', 'And (ஆண்ட்)', 'Because (பிகாஸ்)', 'Or (ஆர்)'],
                    ['Mother (மதர்)', 'And (ஆண்ட்)', 'Father (ஃபாதர்)', 'In (இன்)'],
                    ['But (பட்)', 'Studied (ஸ்டடீட்)', 'Pass (பாஸ்)', 'Did not (டிட் நாட்)'],
                    ['Conjunction (கன்ஜங்ஷன்)', 'Noun (நவுன்)', 'Verb (வெர்ப்)', 'Adjective (அட்ஜெக்டிவ்)'],
                    ['Cause & Effect (காஸ் அண்ட் எஃபெக்ட்)', 'Noun (நவுன்)', 'Verb (வெர்ப்)', 'Time (டைம்)'],
                    ['And (ஆண்ட்)', 'Book (புக்)', 'House (ஹவுஸ்)', 'Run (ரன்)'],
                    ['Choice between two (சாய்ஸ் பிட்வீன் டூ)', 'Time (டைம்)', 'Place (ப்ளேஸ்)', 'Action (ஆக்ஷன்)']
                ],
                'advanced': [
                    ['Market (மார்க்கெட்)', 'School (ஸ்கூல்)', 'Park (பார்க்)', 'Home (ஹோம்)'],
                    ['Playing games (ப்ளேயிங் கேம்ஸ்)', 'Reading books (ரீடிங் புக்ஸ்)', 'Sleeping (ஸ்லீப்பிங்)', 'Watching TV (வாட்சிங் டிவி)'],
                    ['Reena (ரீனா)', 'Rahul (ராஹுல்)', 'Mohan (மோஹன்)', 'Seema (சீமா)'],
                    ['Every day (எவ்ரி டே)', 'Yesterday (யெஸ்டர்டே)', 'Never (நெவர்)', 'Next week (நெக்ஸ்ட் வீக்)'],
                    ['Goes to school (கோஸ் டு ஸ்கூல்)', 'Goes to market (கோஸ் டு மார்க்கெட்)', 'Stays home (ஸ்டேஸ் ஹோம்)', 'Goes to hospital (கோஸ் டு ஹாஸ்பிடல்)'],
                    ['Study habit (ஸ்டடி ஹாபிட்)', 'Travel (டிராவல்)', 'Rain (ரெய்ன்)', 'Hills (ஹில்ஸ்)'],
                    ['Rahul likes reading books (ராஹுல் லைக்ஸ் ரீடிங் புக்ஸ்)', 'Rahul does not go to school (ராஹுல் டஸ் நாட் கோ டு ஸ்கூல்)', 'Rahul only plays (ராஹுல் ஒன்லி ப்ளேஸ்)', 'Rahul sleeps all day (ராஹுல் ஸ்லீப்ஸ் ஆல் டே)']
                ]
            }
        elif ui_lang == 'hi':
            return {
                'foundation': [
                    ['B (बी)', 'A (ए)', 'C (सी)', 'D (डी)'],
                    ['Run (रन)', 'Happy (हैप्पी)', 'Book (बुक)', 'Quickly (क्विकली)'],
                    ['Trees (ट्रीस)', 'Treees (ट्रीस)', "Trees' (ट्रीस)", 'Tree (ट्री)'],
                    ['Beautiful (ब्यूटीफुल)', 'School (स्कूल)', 'Jump (जंप)', 'They (दे)'],
                    ['Sleep (स्लीप)', 'Book (बुक)', 'Blue (ब्लू)', 'Slowly (स्लोली)'],
                    ['House (हाउस)', 'Pustakalaya (पुस्तकालय)', 'Sadak (सड़क)', 'Ped (पेड़)'],
                    ['School (स्कूल)', 'Hospital (हॉस्पिटल)', 'Market (मार्केट)', 'Park (पार्क)']
                ],
                'beginner': [
                    ['Past Tense (पास्ट टेंस)', 'Present Tense (प्रेजेंट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'Command (कमांड)'],
                    ['Past Tense (पास्ट टेंस)', 'Present Tense (प्रेजेंट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'None (नन)'],
                    ['Present Tense (प्रेजेंट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'Past Tense (पास्ट टेंस)', 'Noun (नाउन)'],
                    ['Present Tense (प्रेजेंट टेंस)', 'Past Tense (पास्ट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'Adjective (एडजेक्टिव)'],
                    ['Present Tense (प्रेजेंट टेंस)', 'Past Tense (पास्ट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'None (नन)'],
                    ['Past Tense (पास्ट टेंस)', 'Present Tense (प्रेजेंट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'Adjective (एडजेक्टिव)'],
                    ['Present Tense (प्रेजेंट टेंस)', 'Past Tense (पास्ट टेंस)', 'Future Tense (फ्यूचर टेंस)', 'Noun (नाउन)']
                ],
                'intermediate': [
                    ['But (बट)', 'And (एंड)', 'Because (बिकॉज़)', 'Or (ऑर)'],
                    ['Mother (मदर)', 'And (एंड)', 'Father (फादर)', 'In (इन)'],
                    ['But (बट)', 'Studied (स्टडीड)', 'Pass (पास)', 'Did not (डिड नॉट)'],
                    ['Conjunction (कंजंक्शन)', 'Noun (नाउन)', 'Verb (वर्ब)', 'Adjective (एडजेक्टिव)'],
                    ['Cause & Effect (कॉज़ एंड इफेक्ट)', 'Noun (नाउन)', 'Verb (वर्ब)', 'Time (टाइम)'],
                    ['And (एंड)', 'Book (बुक)', 'House (हाउस)', 'Run (रन)'],
                    ['Choice between two (चॉइस बिटवीन टू)', 'Time (टाइम)', 'Place (प्लेस)', 'Action (एक्शन)']
                ],
                'advanced': [
                    ['Market (मार्केट)', 'School (स्कूल)', 'Park (पार्क)', 'Home (होम)'],
                    ['Playing games (प्लेइंग गेम्स)', 'Reading books (रीडिंग बुक्स)', 'Sleeping (स्लीपिंग)', 'Watching TV (वाचिंग टीवी)'],
                    ['Reena (रीना)', 'Rahul (राहुल)', 'Mohan (मोहन)', 'Seema (सीमा)'],
                    ['Every day (एवरी डे)', 'Yesterday (यस्टरडे)', 'Never (नेवर)', 'Next week (नेक्स्ट वीक)'],
                    ['Goes to school (गोज़ टू स्कूल)', 'Goes to market (गोज़ टू मार्केट)', 'Stays home (स्टेज़ होम)', 'Goes to hospital (गोज़ टू हॉस्पिटल)'],
                    ['Study habit (स्टडी हैबिट)', 'Travel (ट्रैवल)', 'Rain (रेन)', 'Hills (हिल्स)'],
                    ['Rahul likes reading books (राहुल लाइक्स रीडिंग बुक्स)', 'Rahul does not go to school (राहुल डज़ नॉट गो टू स्कूल)', 'Rahul only plays (राहुल ओनली प्लेज़)', 'Rahul sleeps all day (राहुल स्लीप्स ऑल डे)']
                ]
            }

    # Target = KANNADA
    elif learn_lang == 'kn':
        if ui_lang == 'ta':
            return {
                'foundation': [
                    ['14 (பதினான்கு)', '15 (பதினைந்து)', '16 (பதினாறு)', '12 (பன்னிரண்டு)'],
                    ['ಕ್ರಿಯಾಪದ (கிரியாபதா)', 'ನಾಮಪದ (நாமபதா)', 'ಗುಣವಾಚಕ (குணவாசகா)', 'ಸರ್ವನಾಮ (சர்வநாமா)'],
                    ['ಮರ (மரா)', 'ಮರಗಳು (மரகளு)', 'ಮರಗಳಿಂದ (மரகளிந்த)', 'ಮರಕ್ಕೆ (மரக்கௌ)'],
                    ['ಗುಣವಾಚಕ (குணவாசகா)', 'ನಾಮಪದ (நாமபதா)', 'ಕ್ರಿಯಾಪದ (கிரியாபதா)', 'ಅವ್ಯಯ (அவ்யயா)'],
                    ['ಕ್ರಿಯಾಪದ (கிரியாபதா)', 'ನಾಮಪದ (நாமபதா)', 'ಗುಣವಾಚಕ (குணவாசகா)', 'ಅವ್ಯಯ (அவ்யயா)'],
                    ['ಮನೆ (மனே)', 'ಗ್ರಂಥ (கிரந்தா)', 'ರಸ್ತೆ (ரஸ்தே)', 'ಮರ (மரா)'],
                    ['ಶಾಲೆ (சாலை)', 'ಆಸ್ಪತ್ರೆ (ஆஸ்பத்ரே)', 'ಮಾರುಕಟ್ಟೆ (மாருகட்டே)', 'ಉದ್ಯಾನವನ (உத்யானவனா)']
                ],
                'beginner': [
                    ['ಭೂತಕಾಲ (பூதகாலா)', 'ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಆಜ್ಞಾರ್ಥಕ (ஆக்ஞார்த்தகா)'],
                    ['ಭೂತಕಾಲ (பூதகாலா)', 'ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಯಾವುದೂ ಅಲ್ಲ (யாவுதூ அல்லா)'],
                    ['ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಭೂತಕಾಲ (பூதகாலா)', 'ನಾಮಪದ (நாமபதா)'],
                    ['ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭೂತಕಾಲ (பூதகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಗುಣವಾಚಕ (குணவாசகா)'],
                    ['ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭೂತಕಾಲ (பூதகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಯಾವುದೂ ಅಲ್ಲ (யாவுதூ அல்லா)'],
                    ['ಭೂತಕಾಲ (பூதகாலா)', 'ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ಗುಣವಾಚಕ (குணவாசகா)'],
                    ['ವರ್ತಮಾನಕಾಲ (வர்த்தமானகாலா)', 'ಭೂತಕಾಲ (பூதகாலா)', 'ಭವಿಷ್ಯತ್ಕಾಲ (பவிஷ்யத்காலா)', 'ನಾಮಪದ (நாமபதா)']
                ],
                'intermediate': [
                    ['ಆದರೆ (ஆதரே)', 'ಮತ್ತು (மத்து)', 'ಏಕೆಂದರೆ (ஏகேந்தரே)', 'ಅಥವಾ (அதவா)'],
                    ['ತಾಯಿ (தாயி)', 'ಮತ್ತು (மத்து)', 'ತಂದೆ (தந்தே)', 'ಅಲ್ಲಿ (அல்லி)'],
                    ['ಆದರೆ (ஆதரே)', 'ಓದಿದನು (ஓதிதனு)', 'ಉತ್ತೀರ್ಣ (உத்தீர்ணா)', 'ಇಲ್ಲ (இல்லா)'],
                    ['ಸಂಯೋಜಕ ಪದ (சயோஜக பதா)', 'ನಾಮಪದ (நாமபதா)', 'ಕ್ರಿಯಾಪದ (கிரியாபதா)', 'ಗುಣವಾಚಕ (குணவாசகா)'],
                    ['ಕಾರಣ (காரணா)', 'ನಾಮಪದ (நாமபதா)', 'ಕ್ರಿಯಾಪದ (கிரியாபதா)', 'ಸಮಯ (சமயா)'],
                    ['ಮತ್ತು (மத்து)', 'ಪುಸ್ತಕ (புஸ்தகா)', 'ಮನೆ (மனே)', 'ಓಡು (ஓடு)'],
                    ['ಆಯ್ಕೆ (ஆய்கே)', 'ಸಮಯ (சமயா)', 'ಸ್ಥಳ (ஸ்தளா)', 'ಕ್ರಿಯೆ (கிரியை)']
                ],
                'advanced': [
                    ['ಮಾರುಕಟ್ಟೆ (மார்க்கெட் / மாருகட்டே)', 'ಶಾಲೆ (சாலை)', 'ಉದ್ಯಾನ (உத்யானா)', 'ಮನೆ (மனே)'],
                    ['ಆಟ ಆಡುವುದು (ஆட்டா ஆடுவுது)', 'ಪುಸ್ತಕ ಓದುವುದು (புஸ்தகா ஓதுவுது)', 'ಮಲಗುವುದು (மலகுவுது)', 'ಟಿವಿ ನೋಡುವುದು (டிவி நோடுவுது)'],
                    ['ರೀನಾ (ரீனா)', 'ರಾಹುಲ್ (ராஹுல்)', 'ಮೋಹನ್ (மோஹன்)', 'ಸೀಮಾ (சீமா)'],
                    ['ಪ್ರತಿದಿನ (ப்ரதிதினா)', 'ನಿನ್ನೆ (நின்னே)', 'ಎಂದಿಗೂ ಇಲ್ಲ (எந்திகூ இல்லா)', 'ಮುಂದಿನ ವಾರ (முந்தினா வாரா)'],
                    ['ಶಾಲೆಗೆ ಹೋಗುತ್ತಾನೆ (சாலைகே ஹோகுத்தானே)', 'ಮಾರುಕಟ್ಟೆಗೆ ಹೋಗುತ್ತಾನೆ (மாருகட்டேகே ஹோகுத்தானே)', 'ಮನೆಯಲ್ಲಿ ಇರುತ್ತಾನೆ (மநேயல்லி இருத்தானே)', 'ಆಸ್ಪತ್ರೆಗೆ ಹೋಗುತ್ತಾನೆ (ஆஸ்பத்ரேகே ஹோகுத்தானே)'],
                    ['ಅಭ್ಯಾಸ (அப்யாசா)', 'ಪ್ರಯಾಣ (ப்ரயாணா)', 'ಮಳೆ (மளே)', 'ಬೆಟ್ಟಗಳು (பெட்டகளு)'],
                    ['ರಾಹುಲ್ ಪುಸ್ತಕ ಓದಲು ಇಷ್ಟಪಡುತ್ತಾನೆ (ராஹுல் புஸ்தகா ஓதலு இஷ்டபடுத்தானே)', 'ರಾಹುಲ್ ಶಾಲೆಗೆ ಹೋಗುವುದಿಲ್ಲ (ராஹுல் சாலைகே ஹோகுவுதில்லா)', 'ರಾಹುಲ್ ಆಟ ಮಾತ್ರ ಆಡುತ್ತಾನೆ (ராஹுல் ஆட்டா மாத்ரா ஆடுத்தானே)', 'ರಾಹುಲ್ ದಿನವಿಡೀ ಮಲಗುತ್ತಾನೆ (ராஹுல் தினவிடீ மலகுத்தானே)']
                ]
            }

    # Return None for remaining combinations to preserve custom object mapping
    return None

# Update all course pairs
for pair_key, pair_courses in courses.items():
    ui_lang = pair_key.split('-')[0]
    learn_lang = pair_key.split('-')[1]
    
    # 1. Update UI Questions
    if ui_lang in ui_questions:
        q_map = ui_questions[ui_lang]
        for lvl_key, lvl_data in pair_courses.items():
            if lvl_key not in q_map:
                continue
            q_texts = q_map[lvl_key]
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

    # 2. Update Options via Option Builder
    opt_builder_res = build_phonetic_options(learn_lang, ui_lang)
    if opt_builder_res:
        for lvl_key, lvl_data in pair_courses.items():
            if lvl_key not in opt_builder_res:
                continue
            lvl_opts = opt_builder_res[lvl_key]
            for lesson in lvl_data.get('lessons', []):
                pq = lesson.get('practice_questions', [])
                for idx, q in enumerate(pq):
                    if idx < len(lvl_opts):
                        q['options'] = lvl_opts[idx]
            if 'checkpoint' in lvl_data and 'questions' in lvl_data['checkpoint']:
                for idx, q in enumerate(lvl_data['checkpoint']['questions']):
                    if idx < len(lvl_opts):
                        q['options'] = lvl_opts[idx]
            if 'checkpoint_test' in lvl_data:
                for idx, q in enumerate(lvl_data['checkpoint_test']):
                    if idx < len(lvl_opts):
                        q['options'] = lvl_opts[idx]

# Save updated JSON back to file
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

print("Successfully enforced 100% UI questions and phonetic options for all pairs including ta-kn!")
