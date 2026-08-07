import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import en from './locales/en.json';
import hi from './locales/hi.json';
import ta from './locales/ta.json';
import te from './locales/te.json';
import kn from './locales/kn.json';
import ml from './locales/ml.json';

export const SUPPORTED_LANGS = [
  { code: 'en', label: 'English' },
  { code: 'hi', label: 'हिन्दी' },
  { code: 'ta', label: 'தமிழ்' },
  { code: 'te', label: 'తెలుగు' },
  { code: 'kn', label: 'ಕನ್ನಡ' },
  { code: 'ml', label: 'മലയാളം' },
];

const resources = {
  en: { translation: en },
  hi: { translation: hi },
  ta: { translation: ta },
  te: { translation: te },
  kn: { translation: kn },
  ml: { translation: ml },
};

const savedUi = localStorage.getItem('literaai_ui_lang') || localStorage.getItem('literaai_lang') || 'en';
const initialUi = SUPPORTED_LANGS.some((l) => l.code === savedUi) ? savedUi : 'en';

i18n.use(initReactI18next).init({
  resources,
  lng: initialUi,
  fallbackLng: 'en',
  supportedLngs: SUPPORTED_LANGS.map((l) => l.code),
  interpolation: { escapeValue: false },
  react: { useSuspense: false },
});

function applyDocLang(lng) {
  document.documentElement.lang = lng;
  document.documentElement.dir = 'ltr';
}

applyDocLang(i18n.language);
i18n.on('languageChanged', applyDocLang);

export function setAppLanguage(code) {
  const safe = SUPPORTED_LANGS.some((l) => l.code === code) ? code : 'en';
  localStorage.setItem('literaai_ui_lang', safe);
  localStorage.setItem('literaai_lang', safe);
  return i18n.changeLanguage(safe);
}

export function getUILanguage() {
  return i18n.language || localStorage.getItem('literaai_ui_lang') || 'en';
}

export function getLearningLanguage(user) {
  if (user?.preferred_language) {
    return user.preferred_language;
  }
  return localStorage.getItem('literaai_learning_lang') || 'en';
}

export function setLearningLanguage(code) {
  const safe = SUPPORTED_LANGS.some((l) => l.code === code) ? code : 'en';
  localStorage.setItem('literaai_learning_lang', safe);
}

export default i18n;

