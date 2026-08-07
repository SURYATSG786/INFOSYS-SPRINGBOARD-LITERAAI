import fs from 'fs';
import path from 'path';

// 1. Read all 5 seed files
const seedFiles = {
  en: '/home/surya/Downloads/LiteralAI/backend/src/utils/seed_english_only.js',
  hi: '/home/surya/Downloads/LiteralAI/backend/src/utils/seed_hindi.js',
  ta: '/home/surya/Downloads/LiteralAI/backend/src/utils/seed_tamil.js',
  te: '/home/surya/Downloads/LiteralAI/backend/src/utils/seed_telugu.js',
  kn: '/home/surya/Downloads/LiteralAI/backend/src/utils/seed_kannada.js'
};

const seeds = {};

for (const [lang, file] of Object.entries(seedFiles)) {
  const text = fs.readFileSync(file, 'utf-8');
  const matches = [...text.matchAll(/question:\s*['"](.*?)['"][\s\S]*?options:\s*(\[[^\]]*\])[\s\S]*?correct_index:\s*(\d+)[\s\S]*?explanation:\s*['"](.*?)['"]/g)];
  seeds[lang] = matches.map(m => ({
    question: m[1],
    options: eval(m[2]),
    correct_index: parseInt(m[3]),
    explanation: m[4]
  }));
}

// 2. Phonetic Sound Transliteration Map for Target Options into UI Script
// Format: optionText -> { uiLang: phoneticSoundInUIScript }
const translit = {
  // English words -> Native Scripts
  'B': { kn: 'ಬಿ', te: 'బి', ta: 'பி', hi: 'बी' },
  'A': { kn: 'ಎ', te: 'ఎ', ta: 'ஏ', hi: 'ए' },
  'C': { kn: 'ಸಿ', te: 'సి', ta: 'சி', hi: 'सी' },
  'D': { kn: 'ಡಿ', te: 'డి', ta: 'டி', hi: 'डी' },
  'Run': { kn: 'ರನ್', te: 'రన్', ta: 'ரன்', hi: 'रन' },
  'Happy': { kn: 'ಹ್ಯಾಪಿ', te: 'హ్యాపీ', ta: 'ஹேப்பி', hi: 'हैप्पी' },
  'Book': { kn: 'ಬುಕ್', te: 'బుక్', ta: 'புக்', hi: 'बुक' },
  'Quickly': { kn: 'ಕ್ವಿಕ್ಲಿ', te: 'క్విక్లీ', ta: 'க்விக்லி', hi: 'क्विकली' },
  'Trees': { kn: 'ಟ್ರಿಸ್', te: 'ట్రీస్', ta: 'ட்ரீஸ்', hi: 'ट्रीस' },
  'Treees': { kn: 'ಟ್ರಿಸ್', te: 'ట్రీస్', ta: 'ட்ரீஸ்', hi: 'ट्रीस' },
  "Trees'": { kn: 'ಟ್ರಿಸ್', te: 'ట్రీస్', ta: 'ட்ரீஸ்', hi: 'ट्रीस' },
  'Tree': { kn: 'ಟ್ರಿ', te: 'ట్రీ', ta: 'ட்ரீ', hi: 'ट्री' },
  'Beautiful': { kn: 'ಬ್ಯೂಟಿಫುಲ್', te: 'బ్యూటిఫుల్', ta: 'பியூட்டிஃபுல்', hi: 'ब्यूटीफुल' },
  'School': { kn: 'ಸ್ಕೂಲ್', te: 'స్కూల్', ta: 'ஸ்கூல்', hi: 'स्कूल' },
  'Jump': { kn: 'ಜಂಪ್', te: 'జంప్', ta: 'ஜம்ப்', hi: 'जंप' },
  'They': { kn: 'ದೇ', te: 'దే', ta: 'தே', hi: 'दे' },
  'Sleep': { kn: 'ಸ್ಲೀಪ್', te: 'స్లీప్', ta: 'ஸ்லீப்', hi: 'स्लीप' },
  'Blue': { kn: 'ಬ್ಲೂ', te: 'బ్లూ', ta: 'ப்ளூ', hi: 'ब्लू' },
  'Slowly': { kn: 'ಸ್ಲೋಲಿ', te: 'స్లోలీ', ta: 'ஸ்லோலி', hi: 'स्लोली' },
  'House': { kn: 'ಹೌಸ್', te: 'హౌస్', ta: 'ஹவுஸ்', hi: 'हाउस' },
  'Library': { kn: 'ಲೈಬ್ರರಿ', te: 'లైబ్రరీ', ta: 'லைப்ரரி', hi: 'लाइब्रेरी' },
  'Road': { kn: 'ರೋಡ್', te: 'రోడ్', ta: 'ரோடு', hi: 'रोड' },
  'Hospital': { kn: 'ಹಾಸ್ಪಿಟಲ್', te: 'హాస్పిటల్', ta: 'ஹாஸ்பிடல்', hi: 'हॉस्पिटल' },
  'Market': { kn: 'ಮಾರ್ಕೆಟ್', te: 'మార్కెట్', ta: 'மார்க்கெட்', hi: 'मार्केट' },
  'Park': { kn: 'ಪಾರ್ಕ್', te: 'పార్క్', ta: 'பார்க்', hi: 'पार्क' },
  'Present Tense': { kn: 'ಪ್ರೆಸೆಂಟ್ ಟೆನ್ಸ್', te: 'ప్రెసెంట్ టెన్స్', ta: 'ப்ரெசண்ட் டென்ஸ்', hi: 'प्रेजेंट टेंस' },
  'Past Tense': { kn: 'ಪಾಸ್ಟ್ ಟೆನ್ಸ್', te: 'పాస్ట్ టెన్స్', ta: 'பாஸ்ட் டென்ஸ்', hi: 'पास्ट टेंस' },
  'Future Tense': { kn: 'ಫ್ಯೂಚರ್ ಟೆನ್ಸ್', te: 'ఫ్యూచర్ టెన్స్', ta: 'ஃப்யூச்சர் டென்ஸ்', hi: 'फ्यूचर टेंस' },
  'Command': { kn: 'ಕಮಾಂಡ್', te: 'కమాండ్', ta: 'கமாண்ட்', hi: 'कमांड' },
  'None': { kn: 'ನನ್', te: 'నన్', ta: 'நன்', hi: 'नन' },
  'Noun': { kn: 'ನೌನ್', te: 'నౌన్', ta: 'நவுன்', hi: 'नाउन' },
  'Adjective': { kn: 'ಅಡ್ಜೆಕ್ಟಿವ್', te: 'అడ్జెక్టివ్', ta: 'அட்ஜெக்டிவ்', hi: 'एडजेक्टिव' },
  'And': { kn: 'ಆಂಡ್', te: 'యాండ్', ta: 'ஆண்ட்', hi: 'एंड' },
  'But': { kn: 'ಬಟ್', te: 'బట్', ta: 'பட்', hi: 'बट' },
  'Because': { kn: 'ಬಿಕಾಸ್', te: 'బికాజ్', ta: 'பிகாஸ்', hi: 'बिकॉज़' },
  'Or': { kn: 'ಆರ್', te: 'ఆర్', ta: 'ஆர்', hi: 'ऑर' },
  'Mother': { kn: 'ಮದರ್', te: 'మదర్', ta: 'மதர்', hi: 'मदर' },
  'Father': { kn: 'ಫಾದರ್', te: 'ఫాదర్', ta: 'ஃபாதர்', hi: 'फादर' },
  'In': { kn: 'ಇನ್', te: 'ఇన్', ta: 'இன்', hi: 'इन' },
  'Studied': { kn: 'ಸ್ಟಡೀಡ್', te: 'స్టడీడ్', ta: 'ஸ்டடீட்', hi: 'स्टडीड' },
  'Pass': { kn: 'ಪಾಸ್', te: 'పాస్', ta: 'பாஸ்', hi: 'पास' },
  'Did not': { kn: 'ಡಿಡ್ ನಾಟ್', te: 'డిడ్ నాట్', ta: 'டிட் நாட்', hi: 'डिड नॉट' },
  'Conjunction': { kn: 'ಕಂಜಂಕ್ಷನ್', te: 'కంజంక్షన్', ta: 'கன்ஜங்ஷன்', hi: 'कंजंक्शन' },
  'To show cause and effect': { kn: 'ಕಾಸ್ ಆಂಡ್ ಎಫೆಕ್ಟ್', te: 'కాజ్ అండ్ ఎఫెక్ట్', ta: 'காஸ் அண்ட் எஃபெக்ட்', hi: 'कॉज़ एंड इफेक्ट' },
  'As a noun': { kn: 'ಆಸ್ ಎ ನೌನ್', te: 'ఆస్ ఎ నౌన్', ta: 'ஆஸ் எ நவுன்', hi: 'ऐज़ ए नाउन' },
  'As a verb': { kn: 'ಆಸ್ ಎ ವರ್ಬ್', te: 'ఆస్ ఎ వర్ಬ್', ta: 'ஆஸ் எ வெர்ப்', hi: 'ऐज़ ए वर्ब' },
  'To show time': { kn: 'ಟು ಶೋ ಟೈಮ್', te: 'టు షో టైమ్', ta: 'டு ஷோ டைம்', hi: 'टू शो टाइम' },
  'Choice between two options': { kn: 'ಚಾಯ್ಸ್ ಬಿಟ್ವೀನ್ ಟೂ', te: 'ఛాయిస్ బిట్వీన్ టూ', ta: 'சாய்ஸ் பிட்வீன் டூ', hi: 'चॉइस बिटवीन टू' },
  'Time': { kn: 'ಟೈಮ್', te: 'టైమ్', ta: 'டைம்', hi: 'टाइम' },
  'Place': { kn: 'ಪ್ಲೇಸ್', te: 'ప్లేస్', ta: 'ப்ளேஸ்', hi: 'प्लेस' },
  'Action': { kn: 'ಆಕ್ಷನ್', te: 'యాక్షన్', ta: 'ஆக்ஷன்', hi: 'एक्शन' },
  'Home': { kn: 'ಹೋಮ್', te: 'హోమ్', ta: 'ஹோம்', hi: 'होम' },
  'Playing games': { kn: 'ಪ್ಲೇಯಿಂಗ್ ಗೇಮ್ಸ್', te: 'ప్లేయింగ్ గేమ్స్', ta: 'ப்ளேயிங் கேம்ஸ்', hi: 'प्लेइंग गेम्स' },
  'Reading books': { kn: 'ರೀಡಿಂಗ್ ಬುಕ್ಸ್', te: 'రీడింగ్ బుక్స్', ta: 'ரீடிங் புக்ஸ்', hi: 'रीडिंग बुक्स' },
  'Sleeping': { kn: 'ಸ್ಲೀಪಿಂಗ್', te: 'స్లీపిಂಗ್', ta: 'ஸ்லீப்பிங்', hi: 'स्लीपिंग' },
  'Watching TV': { kn: 'ವಾಚಿಂಗ್ ಟಿವಿ', te: 'వాచింగ్ టీవీ', ta: 'வாட்சிங் டிவி', hi: 'वाचिंग टीवी' },
  'Reena': { kn: 'ರೀನಾ', te: 'రీనా', ta: 'ரீனா', hi: 'रीना' },
  'Rahul': { kn: 'ರಾಹುಲ್', te: 'రాహుల్', ta: 'ராஹுல்', hi: 'राहुल' },
  'Mohan': { kn: 'ಮೋಹನ್', te: 'మోహన్', ta: 'மோஹன்', hi: 'मोहन' },
  'Seema': { kn: 'ಸೀಮಾ', te: 'సీమా', ta: 'சீமா', hi: 'सीमा' },
  'Every day': { kn: 'ಎವ್ರಿ ಡೇ', te: 'ఎవ్రీ డే', ta: 'எவ்ரி டே', hi: 'एवरी डे' },
  'Yesterday': { kn: 'ಯೆಸ್ಟರ್ಡೇ', te: 'యెస్టర్డే', ta: 'யெஸ்டர்டே', hi: 'यस्टरडे' },
  'Never': { kn: 'ನೆವರ್', te: 'నెవర్', ta: 'நெவர்', hi: 'नेवर' },
  'Next week': { kn: 'ನೆಕ್ಸ್ಟ್ ವೀಕ್', te: 'నెక్స్ట్ వీక్', ta: 'நெக்ஸ்ட் வீக்', hi: 'नेक्स्ट वीक' },
  'Goes to school': { kn: 'ಗೋಸ್ ಟು ಸ್ಕೂಲ್', te: 'గోస్ టు స్కూల్', ta: 'கோஸ் டு ஸ்கூல்', hi: 'गोज़ टू स्कूल' },
  'Goes to market': { kn: 'ಗೋಸ್ ಟು ಮಾರ್ಕೆಟ್', te: 'గోస్ టు మార్కెట్', ta: 'கோஸ் டு மார்க்கெட்', hi: 'गोज़ टू मार्केट' },
  'Stays home': { kn: 'ಸ್ಟೇಸ್ ಹೋಮ್', te: 'స్టేస్ హోమ్', ta: 'ஸ்டேஸ் ஹோம்', hi: 'स्टेज़ होम' },
  'Goes to hospital': { kn: 'ಗೋಸ್ ಟು ಹಾಸ್ಪಿಟಲ್', te: 'గోస్ టు హాస్పిటల్', ta: 'கோஸ் டு ஹாஸ்பிடல்', hi: 'गोज़ टू हॉस्पिटल' },
  'Reading and school habit': { kn: 'ಸ್ಟಡಿ ಹ್ಯಾಬಿಟ್', te: 'స్టడీ హ్యాబిట్', ta: 'ஸ்டடி ஹாபிட்', hi: 'स्टडी हैबिट' },
  'Travel': { kn: 'ಟ್ರಾವೆಲ್', te: 'ట్రావెల్', ta: 'டிராவல்', hi: 'ट्रैवल' },
  'Rain': { kn: 'ರೈನ್', te: 'రైన్', ta: 'ரெய்ன்', hi: 'रेन' },
  'Hills': { kn: 'ಹಿಲ್ಸ್', te: 'హిల్స్', ta: 'ஹில்ஸ்', hi: 'हिल्स' },
  'Rahul likes reading books.': { kn: 'ರಾಹುಲ್ ಲೈಕ್ಸ್ ರೀಡಿಂಗ್ ಬುಕ್ಸ್', te: 'రాహుల్ లైక్స్ రీడింగ్ బుక్స్', ta: 'ராஹுல் லைக்ஸ் ரீடிங் புக்ஸ்', hi: 'राहुल लाइक्स रीडिंग बुक्स' },

  // Telugu Words -> Other UI Scripts
  'క్రియ': { en: 'Kriya', ta: 'கிரியா', hi: 'क्रिया', kn: 'ಕ್ರಿಯಾ' },
  'నామవాచకం': { en: 'Namavachakam', ta: 'நாமவாச்சகம்', hi: 'नामवाचकम', kn: 'ನಾಮವಾಚಕಂ' },
  'విశేషణం': { en: 'Visheshanam', ta: 'விஷேஷணம்', hi: 'विशेषणम', kn: 'ವಿಶೇಷಣಂ' },
  'సర్వనామం': { en: 'Sarvanamam', ta: 'சர்வநாமம்', hi: 'सर्वनामम', kn: 'ಸರ್ವನಾಮಂ' },
  'చెట్టు': { en: 'Chettu', ta: 'செட்டு', hi: 'चेट्टू', kn: 'ಚೆಟ್ಟು' },
  'చెట్లు': { en: 'Chetlu', ta: 'செட்லு', hi: 'चेट्लू', kn: 'ಚೆಟ್ಲು' },
  'చెట్టులు': { en: 'Chettulu', ta: 'செட்டுலு', hi: 'चेट्टूलू', kn: 'ಚೆಟ್ಟುಲು' },
  'చెట్ల': { en: 'Chetla', ta: 'செட்லா', hi: 'चेट्ला', kn: 'ಚೆಟ್ಲ' },
  'ఇల్లు': { en: 'Illu', ta: 'இல்லு', hi: 'इल्लू', kn: 'ಇಲ್ಲು' },
  'గ్రంథాలయం': { en: 'Granthalayam', ta: 'கிரந்தாலயம்', hi: 'ग्रंथालयं', kn: 'ಗ್ರಂಥಾಲಯಂ' },
  'వీధి': { en: 'Veedhi', ta: 'வீதி', hi: 'वीधि', kn: 'ವೀಧಿ' },
  'ఆసుపత్రి': { en: 'Aasupatri', ta: 'ஆசுபத்ரி', hi: 'आसुपत्री', kn: 'ಆಸ್ಪತ್ರೆ' },
  'పాఠశాల': { en: 'Pathashala', ta: 'பாடசாலா', hi: 'पाठशाला', kn: 'ಪಾಠಶಾಲಾ' },
  'మార్కెట్': { en: 'Market', ta: 'மார்க்கெட்', hi: 'मार्केट', kn: 'ಮಾರ್ಕೆಟ್' },
  'ఉద్యానవనం': { en: 'Udyanavanam', ta: 'உத்யானவனம்', hi: 'उद्यानवनम', kn: 'ಉದ್ಯಾನವನಂ' },
  'భూతకాలం': { en: 'Bhoothakalam', ta: 'பூதகாலம்', hi: 'भूतकालम', kn: 'ಭೂತಕಾಲಂ' },
  'వర్తమాన కాలం': { en: 'Varthamanakalam', ta: 'வர்த்தமானகாலம்', hi: 'वर्तमानकालम', kn: 'ವರ್ತಮಾನಕಾಲಂ' },
  'భవిష్యత్ కాలం': { en: 'Bhavishyathkalam', ta: 'பவிஷ்யத்காலம்', hi: 'भविष्यत्कालम', kn: 'ಭವಿಷ್ಯತ್ಕಾಲಂ' },
  'ఆజ్ఞార్థకం': { en: 'Aagnyaarthakam', ta: 'ஆக்ஞார்த்தகம்', hi: 'आज्ञार्थकम', kn: 'ಆಜ್ಞಾರ್ಥಕಂ' },
  'కానీ': { en: 'Kaani', ta: 'கானீ', hi: 'कानी', kn: 'ಕಾನೀ' },
  'మరియు': { en: 'Mariyu', ta: 'மரியு', hi: 'मरियु', kn: 'ಮರಿಯು' },
  'ఎందుకంటే': { en: 'Endukante', ta: 'எந்துகண்டே', hi: 'इंदुकंटे', kn: 'ಎಂದುಕಂಟೇ' },
  'లేదా': { en: 'Leda', ta: 'லேதா', hi: 'लेदा', kn: 'ಲೇದಾ' },
  'ఆటలు ఆడటం': { en: 'Aatalu aadatam', ta: 'ஆடலு ஆடம்', hi: 'आटलू आडटम', kn: 'ಆಟಲು ಆಡಟಂ' },
  'పుస్తకాలు చదవడం': { en: 'Pustakalu chadavadam', ta: 'புஸ்தகாலு சதுவடம்', hi: 'पुस्तकालू चदुवडम', kn: 'ಪುಸ್ತಕಾಲೂ ಚದುವಡಂ' },
  'నిద్రపోవడం': { en: 'Nidrapovadam', ta: 'நித்ரபோவடம்', hi: 'निद्रपोवडम', kn: 'ನಿದ್ರಪೋವಡಂ' },
  'టీవీ చూడడం': { en: 'TV choodadam', ta: 'டிவி சூடடம்', hi: 'टीवी चूडडम', kn: 'ಟಿವಿ ಚೂಡಡಂ' },

  // Tamil Words -> Other UI Scripts
  'வினைச்சொல்': { en: 'Vinaichol', te: 'వినైచ్చొల్', hi: 'विनैच्चोल', kn: 'ವಿನೈಚ್ಚೊಲ್' },
  'பெயர்ச்சொல்': { en: 'Peyarchol', te: 'పెయర్చ్చొల్', hi: 'पेयरच्चोल', kn: 'ಪೆಯರ್ಚ್ಚೊಲ್' },
  'உரிச்சொல்': { en: 'Urichol', te: 'ఉరిచ్చొల్', hi: 'उरिच्चोल', kn: 'ಉರಿಚ್ಚೊಲ್' },
  'இடைச்சொல்': { en: 'Idaichol', te: 'ఇడైచ్చొల్', hi: 'इडैच्चोल', kn: 'ಇಡೈಚ್ಚೊಲ್' },
  'மரம்': { en: 'Maram', te: 'మరమ్', hi: 'मरम', kn: 'ಮರಮ್' },
  'மரங்கள்': { en: 'Marangal', te: 'మరంగళ్', hi: 'मरंगल', kn: 'ಮರಂಗಳ್' },
  'மரங்கள்ல்': { en: 'Marangall', te: 'మరంగళ్ల్', hi: 'मरंगलल', kn: 'ಮರಂಗಳ್ಲ್' },
  'மரத்தால்': { en: 'Marathaal', te: 'మరత్తాల్', hi: 'मरत्ताल', kn: 'ಮರತ್ತಾಲ್' },
  'வீடு': { en: 'Veedu', te: 'వీడు', hi: 'वीडु', kn: 'ವೀಡು' },
  'நூலகம்': { en: 'Noolagam', te: 'నూలగమ్', hi: 'नूलगम', kn: 'ನೂಲಗಮ್' },
  'தெரு': { en: 'Theru', te: 'తెరు', hi: 'तेरु', kn: 'ತೆರು' },
  'ஆசுபத்திரி': { en: 'Aasupathiri', te: 'ఆసుపత్రి', hi: 'आसुपत्री', kn: 'ಆಸ್ಪತ್ರೆ' },
  'பள்ளி': { en: 'Palli', te: 'పళ్ళి', hi: 'पळ्ळि', kn: 'ಪಳ್ಳಿ' },
  'சந்தை': { en: 'Santhai', te: 'సందై', hi: 'संदै', kn: 'ಸಂದೈ' },
  'பூங்கா': { en: 'Poongaa', te: 'పూంగా', hi: 'पूंगा', kn: 'ಪೂಂಗಾ' },
  'இறந்த காலம்': { en: 'Irantha Kaalam', te: 'ఇరంద కాలమ్', hi: 'इरंद कालम', kn: 'ಇರಂದ ಕಾಲಮ್' },
  'நிகழ்காலம்': { en: 'Nigazh Kaalam', te: 'నిగళ్ కాలమ్', hi: 'निगळ् कालम', kn: 'ನಿಗಳ್ ಕಾಲಮ್' },
  'எதிர்காலம்': { en: 'Ethir Kaalam', te: 'ఎదిర్ కాలమ్', hi: 'एदिर कालम', kn: 'ಎದಿರ್ ಕಾಲಮ್' },
  'கட்டளை': { en: 'Kattalai', te: 'కట్టళై', hi: 'कट्टळै', kn: 'ಕಟ್ಟಳೈ' },
  'ஆனால்': { en: 'Aanaal', te: 'ఆనాల్', hi: 'आनाल', kn: 'ಆನಾಲ್' },
  'மற்றும்': { en: 'Mattrum', te: 'మట్రుమ్', hi: 'मटुरम', kn: 'ಮಟ್ರುಮ್' },
  'ஏனெனில்': { en: 'Aenenil', te: 'ఏనెనిల్', hi: 'एनेनिल', kn: 'ಏನೆನಿಲ್' },
  'அல்லது': { en: 'Allathu', te: 'అల్లదు', hi: 'अल्लदु', kn: 'ಅಲ್ಲದು' },
  'விளையாட்டு ஆடுதல்': { en: 'Vilaiyaattu aaduthal', te: 'విళైయాట్టు ఆడుతల్', hi: 'विळैयाट्टु आडुथल', kn: 'ವಿಳೈಯಾಟ್ಟು ಆಡುತಲ್' },
  'புத்தகங்கள் படித்தல்': { en: 'Puthangangal padithal', te: 'పుత్తగంగళ్ పడిత్తల్', hi: 'पुत्तगंगल पडित्तल', kn: 'ಪುತ್ತಗಂಗಳ್ ಪಡಿತ್ತಲ್' },
  'தூங்குவது': { en: 'Thoonguvathu', te: 'తూంగువదు', hi: 'तूंगुवदु', kn: 'ತೂಂಗುವದು' },
  'டிவி பார்ப்பது': { en: 'TV paarpathu', te: 'టీవీ పార్ప్పదు', hi: 'टीवी पारप्पदु', kn: 'ಟಿವಿ ಪಾರ್ಪ್ಪದು' },

  // Hindi Words -> Other UI Scripts
  'क्रिया': { en: 'Kriya', te: 'క్రియా', ta: 'கிரியா', kn: 'ಕ್ರಿಯಾ' },
  'संज्ञा': { en: 'Sangya', te: 'సంగ్న్యా', ta: 'சங்யா', kn: 'ಸಂಗ್ನ್ಯಾ' },
  'विशेषण': { en: 'Visheshana', te: 'విశేషణ్', ta: 'விஷேஷண்', kn: 'ವಿಶೇಷಣ್' },
  'सर्वनाम': { en: 'Sarvanama', te: 'సర్వనామ్', ta: 'சர்வநாம்', kn: 'ಸರ್ವನಾಮ್' },
  'लड़कियाँ': { en: 'Ladkiyan', te: 'లడ్కియాన్', ta: 'லட்கியான்', kn: 'ಲಡ್ಕಿಯಾನ್' },
  'लड़के': { en: 'Ladke', te: 'లడ్కే', ta: 'லட்கே', kn: 'ಲಡ್ಕೆ' },
  'लड़कों': { en: 'Ladkon', te: 'లడ్కోన్', ta: 'லட்கோன்', kn: 'ಲಡ್ಕೋನ್' },
  'लड़का': { en: 'Ladka', te: 'లడ్కా', ta: 'லட்கா', kn: 'ಲಡ್ಕಾ' },
  'घर': { en: 'Ghar', te: 'ఘర్', ta: 'கர்', kn: 'ಘರ್' },
  'पुस्तकालय': { en: 'Pustakalaya', te: 'పుస్తకాలయ్', ta: 'புஸ்தகாலய்', kn: 'ಪುಸ್ತಕಾಲಯ್' },
  'सड़क': { en: 'Sadak', te: 'సడక్', ta: 'சடக்', kn: 'ಸಡಕ್' },
  'पेड़': { en: 'Ped', te: 'పేడ్', ta: 'பேட்', kn: 'పేಡ್' },
  'अस्पताल': { en: 'Aspatal', te: 'అస్పతాల్', ta: 'அஸ்பதால்', kn: 'ಅಸ್ಪತಾಲ್' },
  'बाज़ार': { en: 'Bazaar', te: 'బాజార్', ta: 'பாஜார்', kn: 'ಬಾಜಾರ್' },
  'भूतकाल': { en: 'Bhootkaal', te: 'భూత్కాల్', ta: 'பூத்காள்', kn: 'ಭೂತ್ಕಾಲ್' },
  'वर्तमान काल': { en: 'Vartamaan kaal', te: 'వర్త్మాన్ కాల్', ta: 'வர்த்மான் காள்', kn: 'ವರ್ತ್ಮಾನ್ ಕಾಲ್' },
  'भविष्य काल': { en: 'Bhavishyat kaal', te: 'భవిష్యత్ కాల్', ta: 'பவிஷ்ய காள்', kn: 'ಭವಿಷ್ಯತ್ ಕಾಲ್' },
  'आज्ञार्थ': { en: 'Aagnyaarth', te: 'ఆజ్ఞార్థస్', ta: 'ஆக்யார்த்', kn: 'ಆಜ್ಞಾರ್ಥ್' },
  'लेकिन': { en: 'Lekin', te: 'లేకిన్', ta: 'லேகின்', kn: 'ಲೇಕಿನ್' },
  'और': { en: 'Aur', te: 'ఔర్', ta: 'அவுர்', kn: 'ಔರ್' },
  'क्योंकि': { en: 'Kyonki', te: 'క్యూంకి', ta: 'க்யோங்கி', kn: 'ಕ್ಯೋಂಕಿ' },
  'या': { en: 'Yaa', te: 'యా', ta: 'யா', kn: 'ಯಾ' },
  'खेलना': { en: 'Khelna', te: 'ఖేల్నా', ta: 'கேல்னா', kn: 'ಖೇಲ್ನಾ' },
  'किताबें पढ़ना': { en: 'Kitaben padhna', te: 'కితాబేన్ పఢనా', ta: 'கிதாபேன் படனா', kn: 'ಕಿತಾಬೇನ್ ಪಢನಾ' },
  'सोना': { en: 'Sona', te: 'సోనా', ta: 'சோனா', kn: 'ಸೋನಾ' },
  'टीवी देखना': { en: 'TV dekhna', te: 'టీవీ దేఖ్నా', ta: 'டீவி தேக்னா', kn: 'ಟಿವಿ ದೇಖ್ನಾ' },

  // Kannada Words -> Other UI Scripts
  'ಕ್ರಿಯಾಪದ': { en: 'Kriyapada', te: 'క్రియాపద', ta: 'கிரியாபதா', hi: 'क्रियापद' },
  'ನಾಮಪದ': { en: 'Namapada', te: 'నామపద', ta: 'நாமபதா', hi: 'नामपद' },
  'ಗುಣವಾಚಕ': { en: 'Gunavachaka', te: 'గుణవాచక', ta: 'குணவாசகா', hi: 'गुणवाचक' },
  'ಸರ್ವನಾಮ': { en: 'Sarvanama', te: 'సర్వనామ', ta: 'சர்வநாமா', hi: 'सर्वनाम' },
  'ಮರ': { en: 'Mara', te: 'మర', ta: 'மரா', hi: 'मरा' },
  'ಮರಗಳು': { en: 'Maragalu', te: 'మరగులు', ta: 'மரகளு', hi: 'मरागलू' },
  'ಮರಗಳ': { en: 'Maragala', te: 'మరగల', ta: 'மரகளா', hi: 'मरागला' },
  'ಮರವು': { en: 'Maravu', te: 'మరవు', ta: 'மரவு', hi: 'मरावू' },
  'ಮನೆ': { en: 'Mane', te: 'మనె', ta: 'மனே', hi: 'मने' },
  'ಗ್ರಂಥ': { en: 'Grantha', te: 'గ్రంథ', ta: 'கிரந்தா', hi: 'ग्रंथा' },
  'ರಸ್ತೆ': { en: 'Raste', te: 'రస్తె', ta: 'ரஸ்தே', hi: 'रस्ते' },
  'ಆಸ್ಪತ್ರೆ': { en: 'Aaspatre', te: 'ఆస్పత్రి', ta: 'ஆஸ்பத்ரே', hi: 'आस्पत्रे' },
  'ಕಲಿಯುವ ಸ್ಥಳ': { en: 'Kaliyuva sthala', te: 'కలియువ స్థల', ta: 'கலியுவ ஸ்தளா', hi: 'कलियुवा स्थला' },
  'ಶಾಲೆ': { en: 'Shale', te: 'శాలె', ta: 'சாலை', hi: 'शाले' },
  'ಮಾರುಕಟ್ಟೆ': { en: 'Marukatte', te: 'మారుకట్టె', ta: 'மாருகட்டே', hi: 'मारुकट्टे' },
  'ಉದ್ಯಾನ': { en: 'Udyana', te: 'ఉద్యాన', ta: 'உத்யானா', hi: 'उद्याना' },
  'ಉದ್ಯಾನವನ': { en: 'Udyanavana', te: 'ఉద్యానవన', ta: 'உத்யானவனா', hi: 'उद्यानवाना' },
  'ಭೂತಕಾಲ': { en: 'Bhoothakala', te: 'భూతకాల', ta: 'பூதகாலா', hi: 'भूतकाला' },
  'ವರ್ತಮಾನಕಾಲ': { en: 'Varthamanakala', te: 'వర్తమానకాల', ta: 'வர்த்தமானகாலா', hi: 'वर्तमानकाला' },
  'ಭವಿಷ್ಯತ್ಕಾಲ': { en: 'Bhavishyathkala', te: 'భవిష్యత్కాల', ta: 'பவிஷ்யத்காலா', hi: 'भविष्यत्काला' },
  'ಆಜ್ಞಾರ್ಥಕ': { en: 'Agnyarthaka', te: 'ఆజ్ఞార్థక', ta: 'ஆக்ஞார்த்தகா', hi: 'आज्ञार्थका' },
  'ಆದರೆ': { en: 'Adare', te: 'ఆదరె', ta: 'ஆதரே', hi: 'आदरे' },
  'ಮತ್ತು': { en: 'Mattu', te: 'మత్తు', ta: 'மத்து', hi: 'मत्तु' },
  'ಏಕೆಂದರೆ': { en: 'Ekendare', te: 'ఎకెందరె', ta: 'ஏகேந்தரே', hi: 'एकेंदरे' },
  'ಅಥವಾ': { en: 'Athava', te: 'అథవా', ta: 'அதவா', hi: 'अथवा' },
  'ಆಟ ಆಡುವುದು': { en: 'Aata aaduvudu', te: 'ఆట ఆడువుదు', ta: 'ஆட்டா ஆடுவுது', hi: 'आटा आडुवुदु' },
  'ಪುಸ್ತಕಗಳನ್ನು ಓದುವುದು': { en: 'Pustakagalanu oduvudu', te: 'పుస్తకగలనూ ఓదువుదు', ta: 'புஸ்தககளனூ ஓதுவுது', hi: 'पुस्तकगलनू ओदुवुदु' },
  'ನಿದ್ರೆ ಮಾಡುವುದು': { en: 'Nidre maaduvudu', te: 'నిద్రె మాడువుదు', ta: 'நித்ரே மாடுவுது', hi: 'निद्रे माडुवुदु' },
  'ದೂರದರ್ಶನ ನೋಡುವುದು': { en: 'Dooradarshana noduvudu', te: 'దూరదర్శన నోడువుదు', ta: 'தூர்தர்ஷனா நோடுவுது', hi: 'दूरदर्शन नोडुवुदु' }
};

// Transliterate function
function formatOption(opt, uiLang) {
  if (!opt) return opt;
  // If option is pure digits or single char like '14', '15', '16', '12', return as is or with digit translit
  if (/^\d+$/.test(opt.trim())) {
    return opt;
  }
  // Check if translit map has exact match
  if (translit[opt] && translit[opt][uiLang]) {
    return `${opt} (${translit[opt][uiLang]})`;
  }
  return opt;
}

// Build BILINGUAL_COURSES
const BILINGUAL_COURSES = {};

const langPairs = [
  'en-hi', 'en-ta', 'en-te', 'en-kn',
  'hi-en', 'hi-ta', 'hi-te', 'hi-kn',
  'ta-en', 'ta-hi', 'ta-te', 'ta-kn',
  'te-en', 'te-hi', 'te-ta', 'te-kn',
  'kn-en', 'kn-hi', 'kn-ta', 'kn-te'
];

for (const pair of langPairs) {
  const [uiLang, learnLang] = pair.split('-');
  const uiSeed = seeds[uiLang];
  const learnSeed = seeds[learnLang];

  const levels = ['foundation', 'beginner', 'intermediate', 'advanced'];
  const pairData = {};

  for (let lIdx = 0; lIdx < levels.length; lIdx++) {
    const lvlName = levels[lIdx];
    const startIndex = lIdx * 7;
    const endIndex = startIndex + 7;

    const uiSlice = uiSeed.slice(startIndex, endIndex);
    const learnSlice = learnSeed.slice(startIndex, endIndex);

    const questions = [];
    for (let i = 0; i < 7; i++) {
      const uQ = uiSlice[i];
      const lQ = learnSlice[i];

      // Format target options with phonetic brackets in UI script
      const rawOpts = lQ.options;
      const formattedOpts = rawOpts.map(o => formatOption(o, uiLang));

      questions.push({
        id: `${uiLang}_${learnLang}_${lvlName}_q${i+1}`,
        question: uQ.question,
        options: formattedOpts,
        correct_index: lQ.correct_index,
        explanation: `${uQ.question} -> ${formattedOpts[lQ.correct_index]}`
      });
    }

    // Structure lesson and checkpoint
    pairData[lvlName] = {
      id: `${lvlName}-${uiLang}-${learnLang}`,
      title: `Course ${lIdx+1}: ${lvlName.charAt(0).toUpperCase() + lvlName.slice(1)} (${uiLang.toUpperCase()} -> ${learnLang.toUpperCase()})`,
      description: `Learn ${learnLang.toUpperCase()} curriculum with ${uiLang.toUpperCase()} UI guidance.`,
      lessons: [
        {
          id: `lesson-1-${lvlName}-${uiLang}-${learnLang}`,
          title: `Lesson 1: Practice Questions`,
          practice_questions: questions
        }
      ],
      checkpoint: {
        id: `checkpoint-${lvlName}-${uiLang}-${learnLang}`,
        questions: questions
      },
      checkpoint_test: questions
    };
  }

  BILINGUAL_COURSES[pair] = pairData;
}

// Generate javascript file content
const jsonStr = JSON.stringify(BILINGUAL_COURSES, null, 2);

const fileContent = `export const BILINGUAL_COURSES = ${jsonStr};

export function getBilingualCourse(courseIdOrPath, uiLang, learnLang) {
  if (!uiLang || !learnLang) return null;
  const pairKey = uiLang + '-' + learnLang;
  const pairCourses = BILINGUAL_COURSES[pairKey];
  if (!pairCourses) return null;

  const key = courseIdOrPath.split('-')[0].trim();
  const levelKey = key.toLowerCase();
  
  if (pairCourses[levelKey]) return pairCourses[levelKey];
  
  for (const lvl of ['foundation', 'beginner', 'intermediate', 'advanced']) {
    if (courseIdOrPath.toLowerCase().includes(lvl)) return pairCourses[lvl];
  }
  return null;
}

export function loadBilingualCoursesList(uiLang, learnLang) {
  if (!uiLang || !learnLang) return null;
  const pairKey = uiLang + '-' + learnLang;
  const pairCourses = BILINGUAL_COURSES[pairKey];
  if (!pairCourses) return null;
  return Object.values(pairCourses);
}
`;

fs.writeFileSync('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', fileContent, 'utf-8');
console.log('FLAWLESSLY REBUILT BILINGUAL_COURSES FOR ALL 20 PAIRS FROM SEED FILES!');
