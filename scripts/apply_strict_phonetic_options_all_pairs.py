import json
import re

# Load existing BILINGUAL_COURSES
with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'export const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)
if not match:
    match = re.search(r'const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)

courses = json.loads(match.group(1))

# Phonetic Options Dictionary per (learnLang, uiLang):

# 1. LEARNING ENGLISH (learnLang = en)
en_options = {
    'kn': {
        'foundation': [
            ['B (ಬಿ)', 'A (ಎ)', 'C (ಸಿ)', 'D (ಡಿ)'],
            ['Run (ರನ್)', 'Happy (ಹ್ಯಾಪಿ)', 'Book (ಬುಕ್)', 'Quickly (ಕ್ವಿಕ್ಲಿ)'],
            ['Trees (ಟ್ರಿಸ್)', 'Treees (ಟ್ರಿಸ್)', "Trees' (ಟ್ರಿಸ್)", 'Tree (ಟ್ರಿ)'],
            ['Beautiful (ಬ್ಯೂಟಿಫುಲ್)', 'School (ಸ್ಕೂಲ್)', 'Jump (ಜಂಪ್)', 'They (ದೇ)'],
            ['Sleep (ಸ್ಲೀಪ್)', 'Book (ಬುಕ್)', 'Blue (ಬ್ಲೂ)', 'Slowly (ಸ್ಲೋಲಿ)'],
            ['Home (ಹೋಮ್)', 'Garden (ಗಾರ್ಡನ್)', 'Car (ಕಾರ್)', 'Book (ಬುಕ್)'],
            ['Hospital (ಹಾಸ್ಪಿಟಲ್)', 'School (ಸ್ಕೂಲ್)', 'Market (ಮಾರ್ಕೆಟ್)', 'Park (ಪಾರ್ಕ್)']
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
            ['But (బట్ / ಬಟ್)', 'Studied (ಸ್ಟಡೀಡ್)', 'Pass (ಪಾಸ್)', 'Did not (ಡಿಡ್ ನಾಟ್)'],
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
    },
    'te': {
        'foundation': [
            ['B (బి)', 'A (ఎ)', 'C (సి)', 'D (డి)'],
            ['Run (రన్)', 'Happy (హ్యాపీ)', 'Book (బుక్)', 'Quickly (క్విక్లీ)'],
            ['Trees (ట్రీస్)', 'Treees (ట్రీస్)', "Trees' (ట్రీస్)", 'Tree (ట్రీ)'],
            ['Beautiful (బ్యూటిఫుల్)', 'School (స్కూల్)', 'Jump (జంప్)', 'They (దే)'],
            ['Sleep (స్లీప్)', 'Book (బుక్)', 'Blue (బ్లూ)', 'Slowly (స్లోలీ)'],
            ['Home (హోమ్)', 'Garden (గార్డెన్)', 'Car (కార్)', 'Book (బుక్)'],
            ['Hospital (హాస్పిటల్)', 'School (స్కూల్)', 'Market (మార్కెట్)', 'Park (పార్క్)']
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
    },
    'ta': {
        'foundation': [
            ['B (பி)', 'A (ஏ)', 'C (சி)', 'D (டி)'],
            ['Run (ரன்)', 'Happy (ஹேப்பி)', 'Book (புக்)', 'Quickly (க்விக்லி)'],
            ['Trees (ட்ரீஸ்)', 'Treees (ட்ரீஸ்)', "Trees' (ட்ரீஸ்)", 'Tree (ட்ரீ)'],
            ['Beautiful (பியூட்டிஃபுல்)', 'School (ஸ்கூல்)', 'Jump (ஜம்ப்)', 'They (தே)'],
            ['Sleep (ஸ்லீப்)', 'Book (புக்)', 'Blue (ப்ளூ)', 'Slowly (ஸ்லோலி)'],
            ['Home (ஹோம்)', 'Garden (கார்டன்)', 'Car (கார்)', 'Book (புக்)'],
            ['Hospital (ஹாஸ்பிடல்)', 'School (ஸ்கூல்)', 'Market (மார்க்கெட்)', 'Park (பார்க்)']
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
    },
    'hi': {
        'foundation': [
            ['B (बी)', 'A (ए)', 'C (सी)', 'D (डी)'],
            ['Run (रन)', 'Happy (हैप्पी)', 'Book (बुक)', 'Quickly (क्विकली)'],
            ['Trees (ट्रीस)', 'Treees (ट्रीस)', "Trees' (ट्रीस)", 'Tree (ट्री)'],
            ['Beautiful (ब्यूटीफुल)', 'School (स्कूल)', 'Jump (जंप)', 'They (दे)'],
            ['Sleep (स्लीप)', 'Book (बुक)', 'Blue (ब्लू)', 'Slowly (स्लोली)'],
            ['Home (होम)', 'Garden (गार्डन)', 'Car (कार)', 'Book (बुक)'],
            ['Hospital (हॉस्पिटल)', 'School (स्कूल)', 'Market (मार्केट)', 'Park (पार्क)']
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
}

updated_count = 0
for pair_key, pair_courses in courses.items():
    ui_lang = pair_key.split('-')[0]
    learn_lang = pair_key.split('-')[1]
    
    # If learning English, apply phonetic English options
    if learn_lang == 'en' and ui_lang in en_options:
        opt_map = en_options[ui_lang]
        for lvl_key, lvl_data in pair_courses.items():
            if lvl_key not in opt_map:
                continue
            lvl_opts = opt_map[lvl_key]
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
        updated_count += 1

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

print(f"Successfully applied phonetic sound options across {updated_count} English-learning pairs!")
