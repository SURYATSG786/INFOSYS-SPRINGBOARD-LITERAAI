export const VOICE_PRACTICE_ITEMS = [
  {
    id: "sent_1",
    learning: {
      en: "I learn new words every single day.",
      ta: "நான் தினமும் புதிய சொற்களைக் கற்கிறேன்.",
      te: "నేను ప్రతిరోజూ కొత్త విషయాలు నేర్చుకుంటాను.",
      ml: "ഞാൻ ദിവസവും പുതിയ വാക്കുകൾ പഠിക്കുന്നു.",
      kn: "ನಾನು ಪ್ರತಿದಿನ ಹೊಸ ಪದಗಳನ್ನು ಕಲಿಯುತ್ತೇನೆ.",
      hi: "मैं रोज़ नई बातें सीखता हूँ।"
    }
  },
  {
    id: "sent_2",
    learning: {
      en: "Reading and writing empower our daily lives.",
      ta: "வாசிப்பும் எழுத்தும் நம் வாழ்க்கையை உயர்த்தும்.",
      te: "చదవడం మరియు రాయడం మన జీవితాన్ని మారుస్తుంది.",
      ml: "വായനയും എഴുത്തും നമ്മുടെ ജീവിതത്തെ മാറ്റുന്നു.",
      kn: "ಓದುವುದು ಮತ್ತು ಬರೆಯುವುದು ನಮ್ಮ ಜೀವನವನ್ನು ಬದಲಾಯಿಸುತ್ತದೆ.",
      hi: "पढ़ना और लिखना हमारे जीवन को बदल देता है।"
    }
  },
  {
    id: "sent_3",
    learning: {
      en: "Education is the foundation of human progress.",
      ta: "கல்வியே மனிதனின் மிகச்சிறந்த செல்வம் ஆகும்.",
      te: "చదువు మనిషికి నిజమైన సంపద.",
      ml: "വിദ്യാഭ്യാസമാണ് മനുഷ്യന്റെ ഏറ്റവും വലിയ സമ്പത്ത്.",
      kn: "ಶಿಕ್ಷಣವೇ ಮಾನವನ ಅತಿ ದೊಡ್ಡ ಆസ്ತಿಯಾಗಿದೆ.",
      hi: "शिक्षा से ही समाज का विकास होता है।"
    }
  },
  {
    id: "sent_4",
    learning: {
      en: "Knowledge opens doors to endless opportunities.",
      ta: "அறிவு நம் எதிர்காலத்தை பிரகாசமாக்கும்.",
      te: "జ్ఞానం మన భవిష్యత్తును వెలిగిస్తుంది.",
      ml: "അറിവ് നമ്മുടെ ഭാവി പ്രകാശപൂർണ്ണമാക്കുന്നു.",
      kn: "ಜ್ಞಾನವು നമ്മുടെ ಭವಿಷ್ಯವನ್ನು ಉಜ್ವಲಗೊಳಿಸುತ್ತದೆ.",
      hi: "ज्ञान इंसान की सबसे बड़ी ताकत है।"
    }
  },
  {
    id: "sent_5",
    learning: {
      en: "Consistent practice leads to lifelong confidence.",
      ta: "முயற்சி உடையார் இகழ்ச்சி அடையார்.",
      te: "కష్టపడి పనిచేస్తే విజయం నిశ్చయంగా వస్తుంది.",
      ml: "തുടർച്ചയായ പരിശീലനം വിജയത്തിലേക്ക് നയിക്കുന്നു.",
      kn: "ಸತತ ಶ್ರಮದಿಂದ ಯಶಸ್ಸು ಖಂಡಿತ ಸಿಗುತ್ತದೆ.",
      hi: "मेहनत और लगन से हर सपना पूरा होता है।"
    }
  }
];

export const VOICE_PRACTICE_SENTENCES = {
  hi: VOICE_PRACTICE_ITEMS.map((item) => item.learning.hi),
  ta: VOICE_PRACTICE_ITEMS.map((item) => item.learning.ta),
  te: VOICE_PRACTICE_ITEMS.map((item) => item.learning.te),
  kn: VOICE_PRACTICE_ITEMS.map((item) => item.learning.kn),
  ml: VOICE_PRACTICE_ITEMS.map((item) => item.learning.ml),
  en: VOICE_PRACTICE_ITEMS.map((item) => item.learning.en),
};

export function getVoicePracticeSentences(learningLang = 'en') {
  return VOICE_PRACTICE_SENTENCES[learningLang] || VOICE_PRACTICE_SENTENCES.en;
}

export function getVoicePracticeDetails(learningLang = 'en', uiLang = 'en') {
  const safeLearn = VOICE_PRACTICE_SENTENCES[learningLang] ? learningLang : 'en';
  const safeUi = VOICE_PRACTICE_SENTENCES[uiLang] ? uiLang : 'en';

  return VOICE_PRACTICE_ITEMS.map((item) => ({
    id: item.id,
    target: item.learning[safeLearn] || item.learning.en,
    translation: safeLearn !== safeUi ? item.learning[safeUi] || item.learning.en : null,
  }));
}

export default VOICE_PRACTICE_SENTENCES;
