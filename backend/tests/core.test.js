import test from 'node:test';
import assert from 'node:assert/strict';
import { getPathFromScore, passwordStrengthOk, LANGUAGES, EDUCATION_LEVELS } from '../src/utils/auth.js';
import {
  scoreAssessment,
  getRecommendedCourse,
  getRecommendedCourses,
  getCourseById,
  scoreCheckpoint,
  getAssessmentQuestions,
  publicCourse,
  loadAssessments,
  loadCourses,
  isCompleteQuestion,
} from '../src/services/courses.js';

test('only 5 supported languages', () => {
  assert.deepEqual(LANGUAGES, ['en', 'hi', 'ta', 'te', 'kn']);
});

test('getPathFromScore maps bands correctly', () => {
  assert.equal(getPathFromScore(0), 'foundation');
  assert.equal(getPathFromScore(25), 'foundation');
  assert.equal(getPathFromScore(26), 'beginner');
  assert.equal(getPathFromScore(50), 'beginner');
  assert.equal(getPathFromScore(51), 'intermediate');
  assert.equal(getPathFromScore(75), 'intermediate');
  assert.equal(getPathFromScore(76), 'advanced');
  assert.equal(getPathFromScore(100), 'advanced');
});

test('passwordStrengthOk validates rules', () => {
  assert.equal(passwordStrengthOk('Password1'), true);
});

test('scoreAssessment uses answer_index', () => {
  const answers = Array.from({ length: 10 }, (_, i) => ({
    question_id: `nfe-${i + 1}`,
    answer_index: 99,
  }));
  answers[0].answer_index = 0; // Cow
  answers[1].answer_index = 1; // A
  answers[2].answer_index = 2; // Yellow
  const result = scoreAssessment('No Formal Education', answers);
  assert.equal(result.correct, 3);
  assert.equal(result.score, 30);
  assert.equal(result.path, 'beginner');
});

test('4 recommended courses per path', () => {
  assert.equal(loadCourses('en').length, 4);
  assert.equal(getRecommendedCourse(10).path, 'foundation');
  assert.equal(getRecommendedCourse(90).path, 'advanced');
});

test('assessment questions localize to Tamil without English fallback for question text', () => {
  const qs = getAssessmentQuestions('High School', 'ta');
  assert.equal(qs.length, 10);
  assert.match(qs[0].question, /ஊகம்|முடிவு|வாசகர்|படி/);
  assert.ok(qs[0].options.every((o) => typeof o === 'string' && o.length > 0));
  assert.ok(qs[0].image);
});

test('every assessment question is complete in all 5 languages', () => {
  for (const level of EDUCATION_LEVELS) {
    const bank = loadAssessments().find((a) => a.education_level === level);
    assert.ok(bank, level);
    assert.equal(bank.questions.length, 10, level);
    for (const q of bank.questions) {
      assert.equal(isCompleteQuestion(q), true, `${level}/${q.id}`);
    }
    for (const lang of LANGUAGES) {
      const qs = getAssessmentQuestions(level, lang);
      assert.equal(qs.length, 10, `${level}/${lang}`);
      for (const q of qs) {
        assert.ok(String(q.question || '').trim(), `${level}/${lang}/${q.id} question`);
        assert.equal(q.options.length, 4, `${level}/${lang}/${q.id} options`);
        assert.ok(q.options.every((o) => String(o || '').trim()), `${level}/${lang}/${q.id} empty option`);
      }
    }
  }
});

test('Primary School question 6 has text and options (regression)', () => {
  const qs = getAssessmentQuestions('Primary School', 'en');
  const q6 = qs.find((q) => q.id === 'ps-6');
  assert.ok(q6);
  assert.match(q6.question, /rhymes|cat/i);
  assert.equal(q6.options.length, 4);
  assert.ok(q6.options.includes('Hat'));
});

test('Tamil rhyme question must not use தொப்பி for பூனை (native ஓசை ஒற்றுமை)', () => {
  const bank = loadAssessments().find((a) => a.education_level === 'Primary School');
  const raw = bank.questions.find((q) => q.id === 'ps-6');
  assert.ok(raw);
  const taQ = raw.question.ta;
  const taCorrect = raw.options[raw.correct_index].ta;
  // Must not be the bad English cat/hat calque
  assert.equal(taCorrect === 'தொப்பி' && /பூனை/.test(taQ), false);
  assert.notEqual(taCorrect, 'தொப்பி');
  assert.match(taQ, /ஓசை|ஒற்றுமை|கல்|மலர்|வானம்/);
  assert.ok(['பல்', 'வளர்', 'கானம்'].includes(taCorrect), `unexpected Tamil rhyme answer: ${taCorrect}`);

  const ta = getAssessmentQuestions('Primary School', 'ta');
  const q6 = ta.find((q) => q.id === 'ps-6');
  assert.ok(q6);
  assert.equal(q6.options.includes('தொப்பி'), false);
  assert.ok(q6.options.includes(taCorrect));
});

test('foundation questions keep native prompts and answers semantically aligned', () => {
  const expectedFirstVowels = {
    hi: { courseId: 'foundation-hi', question: /मेरा पठन|साक्षरता|शब्द|प्रश्न|वर्णमाला/, answer: 'अ' },
    ta: { courseId: 'foundation-ta', question: /உயிரெழுத்துகள்|எழுத்து|மொழி/, answer: '12' },
    te: { courseId: 'foundation-te', question: /అచ్చులు|వర్ణమాల|అక్షరాస్యత|పదాలు|అక్షరాలు/, answer: '16' },
  };
  for (const [lang, expected] of Object.entries(expectedFirstVowels)) {
    const c = loadCourses(lang).find((course) => course.id === expected.courseId);
    assert.ok(c, `Course ${expected.courseId} must exist`);
    const q1 = c.lessons[0].practice_questions[0];
    const qText = typeof q1.question === 'object' ? q1.question[lang] : q1.question;
    assert.match(qText, expected.question, `${expected.courseId} Q1 ${lang} prompt`);
  }

  const oppositeTerms = {
    hi: /विपरीत/,
    ta: /எதிர்/,
    te: /వ్యతిరేక/,
    kn: /ವಿರುದ್ಧ/,
  };
  const soundAnswers = {
    hi: /^(?:बुह|कुह|दुह|अह|ति|द)$/,
    ta: /^(?:புஹ்|குஹ்|டுஹ்|அஹ்|தி)$/,
    te: /^(?:బుహ్|కుహ్|డుహ్|అహ్|ది)$/,
    kn: /^(?:ಬುಹ್|ಕುಹ್|ಡುಹ್|ಅಹ್|ದಿ)$/,
  };

  const foundationCourses = loadCourses().filter((course) => course.path === 'foundation');
  for (const course of foundationCourses) {
    const questions = [
      ...course.lessons.flatMap((lesson) => lesson.practice_questions || []),
      ...(course.checkpoint_test || []),
    ];
    for (const question of questions) {
      for (const lang of Object.keys(oppositeTerms)) {
        if (oppositeTerms[lang].test(question.question[lang])) {
          const answer = question.options[question.correct_index][lang];
          assert.doesNotMatch(
            answer,
            soundAnswers[lang],
            `${course.id}/${question.id} ${lang} opposite answer: ${answer}`,
          );
        }
      }
    }
  }
});

test('no placeholder-like options in any language (assessments + courses)', () => {
  const placeholder = /^(Wrong choice|Wrong option|தவறான தேர்வு|गलत विकल्प|తప్పు ఎంపిక|ತಪ್ಪು ಆಯ್ಕೆ|Placeholder|dummy)$/i;
  const langs = LANGUAGES;

  function checkOptions(options, path) {
    for (const opt of options || []) {
      if (typeof opt === 'string') {
        assert.equal(placeholder.test(opt.trim()), false, `${path}: ${opt}`);
      } else if (opt && typeof opt === 'object') {
        for (const lang of langs) {
          const v = String(opt[lang] || '').trim();
          assert.ok(v.length > 0, `${path}.${lang} empty`);
          assert.equal(placeholder.test(v), false, `${path}.${lang}: ${v}`);
        }
      }
    }
  }

  for (const level of EDUCATION_LEVELS) {
    const bank = loadAssessments().find((a) => a.education_level === level);
    assert.equal(bank.questions.length, 10, level);
    for (const q of bank.questions) {
      checkOptions(q.options, `${level}/${q.id}`);
    }
  }

  for (const course of loadCourses()) {
    for (const lesson of course.lessons) {
      for (const q of lesson.practice_questions || []) {
        checkOptions(q.options, `${course.id}/${q.id || 'pq'}`);
      }
    }
    for (const q of course.checkpoint_test || []) {
      checkOptions(q.options, `${course.id}/${q.id || 'cp'}`);
    }
  }
});

test('native assessment and course text has no Latin English letters', () => {
  const latin = /[A-Za-z]/;
  const nativeLangs = ['hi', 'ta', 'te', 'kn'];
  for (const level of EDUCATION_LEVELS) {
    const bank = loadAssessments().find((a) => a.education_level === level);
    for (const q of bank.questions) {
      for (const lang of nativeLangs) {
        assert.equal(latin.test(q.question[lang]), false, `${level}/${q.id} question.${lang}: ${q.question[lang]}`);
        q.options.forEach((opt, i) => {
          assert.equal(latin.test(opt[lang]), false, `${level}/${q.id} opt${i}.${lang}: ${opt[lang]}`);
        });
      }
    }
  }
  // Sample Primary Tamil past-tense question must use native verb, not English "go"
  const ta = getAssessmentQuestions('Primary School', 'ta');
  const ps1 = ta.find((q) => q.id === 'ps-1');
  assert.ok(ps1);
  assert.equal(/go|going|apple|article/i.test(ps1.question), false);
  assert.match(ps1.question, /போ/);
  assert.ok(ps1.options.every((o) => !/[A-Za-z]/.test(o)));
  assert.ok(ps1.options.includes('போனான்'));
  const ps3 = ta.find((q) => q.id === 'ps-3');
  assert.equal(/article|apple|___ apple/i.test(ps3.question), false);
  assert.ok(ps3.options.every((o) => !/[A-Za-z]/.test(o)));
  assert.equal(ps3.options.includes('தொப்பி'), false);

  function walk(obj, path = 'courses') {
    if (obj && typeof obj === 'object') {
      if (Object.prototype.hasOwnProperty.call(obj, 'en') && nativeLangs.some((l) => Object.prototype.hasOwnProperty.call(obj, l))) {
        for (const lang of nativeLangs) {
          if (typeof obj[lang] === 'string') {
            assert.equal(latin.test(obj[lang]), false, `${path}.${lang}: ${obj[lang].slice(0, 80)}`);
          }
        }
        return;
      }
      for (const [k, v] of Object.entries(obj)) walk(v, `${path}.${k}`);
    } else if (Array.isArray(obj)) {
      obj.forEach((v, i) => walk(v, `${path}[${i}]`));
    }
  }
  walk(loadCourses());
});

test('course content localizes', () => {
  const course = getRecommendedCourse(10, 'ta');
  const ta = publicCourse(course, 'ta');
  assert.match(ta.title, /என் மொழி|ஆற்றல்|எழுத்தறிவு|பயணம்|முதல்/);
  assert.ok(ta.lessons.length >= 1);
  assert.equal(ta.lessons[0].practice_questions[0].options.length, 4);
});

test('checkpoint scoring with indices', () => {
  const course = getRecommendedCourse(10);
  const fail = scoreCheckpoint(course.id, Array(10).fill(9));
  assert.equal(fail.passed, false);
  const perfect = course.checkpoint_test.map((q) => q.correct_index);
  const pass = scoreCheckpoint(course.id, perfect);
  assert.equal(pass.passed, true);
  assert.equal(pass.score, 100);
});

test('bilingual assessment mode kn-en (Kannada UI -> Learn English)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'en', 'kn');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"ಮೂ" ಎನ್ನುವ ಪ್ರಾಣಿ ಯಾವುದು?');
  assert.equal(qs[0].options[0], 'Cow (ಕೌ)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'en', 'kn');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode en-kn (English UI -> Learn Kannada)', () => {
  const qs = getAssessmentQuestions('Primary School', 'kn', 'en');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, 'What is the past tense of "go"?');
  assert.equal(qs[0].options[0], 'Hoodanu (ಹೋದನು)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('Primary School', answers, 'kn', 'en');
  assert.equal(score.score, 100);
});

test('same language mode kn-kn keeps original database questions', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'kn', 'kn');
  assert.equal(qs.length, 10);
  // Must be default localized Kannada questions, not cross-language set
  assert.notEqual(qs[0].id, 'kn_en_nfe_1');
  assert.notEqual(qs[0].id, 'en_kn_nfe_1');
});

test('bilingual assessment mode kn-ta (Kannada UI -> Learn Tamil)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'ta', 'kn');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"ಮೂ" ಎನ್ನುವ ಪ್ರಾಣಿ ಯಾವುದು?');
  assert.equal(qs[0].options[0], 'பசு (ಪಸು)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'ta', 'kn');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode ta-kn (Tamil UI -> Learn Kannada)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'kn', 'ta');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"மூ" என்று சொல்லும் விலங்கு எது?');
  assert.equal(qs[0].options[0], 'ಹಸು (ஹசு)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'kn', 'ta');
  assert.equal(score.score, 100);
});

test('same language mode ta-ta keeps original database questions', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'ta', 'ta');
  assert.equal(qs.length, 10);
  assert.notEqual(qs[0].id, 'ta_kn_nfe_1');
  assert.notEqual(qs[0].id, 'kn_ta_nfe_1');
});

test('bilingual assessment mode hi-kn (Hindi UI -> Learn Kannada)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'kn', 'hi');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"मू" बोलने वाला जानवर कौन सा है?');
  assert.equal(qs[0].options[0], 'ಹಸು (हसु)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'kn', 'hi');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode kn-hi (Kannada UI -> Learn Hindi)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'hi', 'kn');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"ಮೂ" बोलने वाला जानवर कौन सा है?');
  assert.equal(qs[0].options[0], 'गाय (ಗಾಯ್)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'hi', 'kn');
  assert.equal(score.score, 100);
});

test('same language mode hi-hi keeps original database questions', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'hi', 'hi');
  assert.equal(qs.length, 10);
  assert.notEqual(qs[0].id, 'hi_kn_nfe_1');
  assert.notEqual(qs[0].id, 'kn_hi_nfe_1');
});

test('same language mode en-en keeps original database questions', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'en', 'en');
  assert.equal(qs.length, 10);
  assert.notEqual(qs[0].id, 'en_kn_nfe_1');
  assert.notEqual(qs[0].id, 'kn_en_nfe_1');
});

test('same language mode te-te keeps original database questions', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'te', 'te');
  assert.equal(qs.length, 10);
  assert.notEqual(qs[0].id, 'hi_kn_nfe_1');
});

test('bilingual assessment mode en-ta (English UI -> Learn Tamil)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'ta', 'en');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, 'Which animal says "Moo"?');
  assert.equal(qs[0].options[0], 'Pasu (பசு)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'ta', 'en');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode ta-en (Tamil UI -> Learn English)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'en', 'ta');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"மூ" என்று சொல்லும் விலங்கு எது?');
  assert.equal(qs[0].options[0], 'Cow (காவ்)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'en', 'ta');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode te-ta (Telugu UI -> Learn Tamil)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'ta', 'te');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"మూ" అని చెప్పే జంతువు ఏది?');
  assert.equal(qs[0].options[0], 'பசு (పసు)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'ta', 'te');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode ta-te (Tamil UI -> Learn Telugu)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'te', 'ta');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"மூ" என்று சொல்லும் விலங்கு எது?');
  assert.equal(qs[0].options[0], 'ఆవు (ஆவு)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'te', 'ta');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode hi-ta (Hindi UI -> Learn Tamil)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'ta', 'hi');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"मू" बोलने वाला जानवर कौन सा है?');
  assert.equal(qs[0].options[0], 'பசு (पसु)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'ta', 'hi');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode ta-hi (Tamil UI -> Learn Hindi)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'hi', 'ta');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"மூ" என்று சொல்லும் விலங்கு எது?');
  assert.equal(qs[0].options[0], 'गाय (காய்)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'hi', 'ta');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode en-hi (English UI -> Learn Hindi)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'hi', 'en');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, 'Which animal says "Moo"?');
  assert.equal(qs[0].options[0], 'Gaay (गाय)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'hi', 'en');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode hi-en (Hindi UI -> Learn English)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'en', 'hi');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"मू" बोलने वाला जानवर कौन सा है?');
  assert.equal(qs[0].options[0], 'Cow (काउ)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'en', 'hi');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode te-en (Telugu UI -> Learn English)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'en', 'te');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"మూ" అని చెప్పే జంతువు ఏది?');
  assert.equal(qs[0].options[0], 'Cow (కౌ)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'en', 'te');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode en-te (English UI -> Learn Telugu)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'te', 'en');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, 'Which animal says "Moo"?');
  assert.equal(qs[0].options[0], 'Aavu (ఆవు)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'te', 'en');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode hi-te (Hindi UI -> Learn Telugu)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'te', 'hi');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"मू" बोलने वाला जानवर कौन सा है?');
  assert.equal(qs[0].options[0], 'ఆవు (आवु)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'te', 'hi');
  assert.equal(score.score, 100);
});

test('bilingual assessment mode te-hi (Telugu UI -> Learn Hindi)', () => {
  const qs = getAssessmentQuestions('No Formal Education', 'hi', 'te');
  assert.equal(qs.length, 10);
  assert.equal(qs[0].question, '"మూ" అని చెప్పే జంతువు ఏది?');
  assert.equal(qs[0].options[0], 'गाय (గాయ్)');

  const answers = qs.map((q) => ({ question_id: q.id, answer_index: q.correct_index }));
  const score = scoreAssessment('No Formal Education', answers, 'hi', 'te');
  assert.equal(score.score, 100);
});

test('bilingual course mode hi-en (Hindi UI -> Learn English)', () => {
  const courses = loadCourses('en', 'hi');
  assert.equal(courses.length, 4);

  const foundation = getCourseById('foundation', 'en', 'hi');
  assert.equal(foundation.lessons[0].practice_questions.length, 7);
  assert.equal(foundation.lessons[0].practice_questions[0].question, 'शब्द Apple किस अक्षर से शुरू होता है?');
  assert.equal(foundation.lessons[0].practice_questions[0].options[1], 'A (ए)');

  const beginner = getCourseById('beginner', 'en', 'hi');
  assert.equal(beginner.lessons[0].practice_questions.length, 7);
  assert.equal(beginner.lessons[0].practice_questions[0].question, '"I am going to school." यह कौन-सा काल है?');

  const intermediate = getCourseById('intermediate', 'en', 'hi');
  assert.equal(intermediate.lessons[0].practice_questions.length, 7);
  assert.equal(intermediate.lessons[0].practice_questions[0].question, 'कौन-सा शब्द दो विचारों को जोड़ता है?');

  const advanced = getCourseById('advanced', 'en', 'hi');
  assert.equal(advanced.lessons[0].practice_questions.length, 7);
  assert.equal(advanced.lessons[0].practice_questions[0].question, 'राहुल कहाँ जाता है?');
});

test('bilingual course mode en-hi (English UI -> Learn Hindi)', () => {
  const courses = loadCourses('hi', 'en');
  assert.equal(courses.length, 4);

  const foundation = getCourseById('foundation', 'hi', 'en');
  assert.equal(foundation.lessons[0].practice_questions.length, 7);
  assert.equal(foundation.lessons[0].practice_questions[0].question, 'How many vowels (स्वर) are there in the Hindi alphabet?');
  assert.equal(foundation.lessons[0].practice_questions[0].options[2], '13 (तेरह)');

  const beginner = getCourseById('beginner', 'hi', 'en');
  assert.equal(beginner.lessons[0].practice_questions.length, 7);
  assert.equal(beginner.lessons[0].practice_questions[0].question, '"मैं स्कूल जाता हूँ।" (Main school jaata hoon) — Which tense is this?');

  const intermediate = getCourseById('intermediate', 'hi', 'en');
  assert.equal(intermediate.lessons[0].practice_questions.length, 7);
  assert.equal(intermediate.lessons[0].practice_questions[0].question, '"राम ___ स्कूल गया।" (Ram ___ school gaya)');

  const advanced = getCourseById('advanced', 'hi', 'en');
  assert.equal(advanced.lessons[0].practice_questions.length, 7);
  assert.equal(advanced.lessons[0].practice_questions[0].question, 'Where does Rahul (राहुल) go?');
});

test('bilingual course mode ta-en (Tamil UI -> Learn English)', () => {
  const courses = loadCourses('en', 'ta');
  assert.equal(courses.length, 4);

  const foundation = getCourseById('foundation', 'en', 'ta');
  assert.equal(foundation.lessons[0].practice_questions.length, 7);
  assert.equal(foundation.lessons[0].practice_questions[0].question, 'தமிழ் மொழியில் உயிரெழுத்துகள் எத்தனை?');
  assert.equal(foundation.lessons[0].practice_questions[0].options[2], '12');

  const beginner = getCourseById('beginner', 'en', 'ta');
  assert.equal(beginner.lessons[0].practice_questions.length, 7);
  assert.equal(beginner.lessons[0].practice_questions[0].question, '"நான் பள்ளிக்கு செல்கிறேன்." இது எந்த காலம்?');

  const intermediate = getCourseById('intermediate', 'en', 'ta');
  assert.equal(intermediate.lessons[0].practice_questions.length, 7);
  assert.equal(intermediate.lessons[0].practice_questions[0].question, '"ரவி ___ பள்ளிக்கு சென்றான்."');

  const advanced = getCourseById('advanced', 'en', 'ta');
  assert.equal(advanced.lessons[0].practice_questions.length, 7);
  assert.equal(advanced.lessons[0].practice_questions[0].question, 'ராம் தினமும் எங்கு செல்கிறான்?');
});

test('bilingual course mode en-ta (English UI -> Learn Tamil)', () => {
  const courses = loadCourses('ta', 'en');
  assert.equal(courses.length, 4);

  const foundation = getCourseById('foundation', 'ta', 'en');
  assert.equal(foundation.lessons[0].practice_questions.length, 7);
  assert.equal(foundation.lessons[0].practice_questions[0].question, 'Which letter does the word Apple begin with?');
  assert.equal(foundation.lessons[0].practice_questions[0].options[1], 'A (அ)');

  const beginner = getCourseById('beginner', 'ta', 'en');
  assert.equal(beginner.lessons[0].practice_questions.length, 7);
  assert.equal(beginner.lessons[0].practice_questions[0].question, '"I am going to school." Which tense is this?');

  const intermediate = getCourseById('intermediate', 'ta', 'en');
  assert.equal(intermediate.lessons[0].practice_questions.length, 7);
  assert.equal(intermediate.lessons[0].practice_questions[0].question, 'Which word joins two ideas?');

  const advanced = getCourseById('advanced', 'ta', 'en');
  assert.equal(advanced.lessons[0].practice_questions.length, 7);
  assert.equal(advanced.lessons[0].practice_questions[0].question, 'Where does Rahul go?');
});









