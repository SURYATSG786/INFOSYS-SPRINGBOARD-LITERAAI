import json
import re
from build_ta_hi import build_ta_hi
from build_hi_ta import build_hi_ta

def build_te_en():
    levels = ['foundation', 'beginner', 'intermediate', 'advanced']
    titles = [
        'Course 1: Foundation (నా ఆంగ్ల అక్షరాస్యత ప్రయాణం)',
        'Course 2: Beginner (నా చుట్టూ ఉన్న ఆంగ్ల పదాలు)',
        'Course 3: Intermediate (పదజాలానికి కొత్త అడుగులు)',
        'Course 4: Advanced (నా ప్రపంచ ఆంగ్ల వాక్యాలు)'
    ]
    q_c1 = [
        {'question': 'ప్రశ్న: Apple అనే పదం ఏ అక్షరంతో ప్రారంభమవుతుంది?', 'options': ['B (బి)', 'A (ఎ)', 'C (సి)', 'D (డి)'], 'correct_index': 1, 'explanation': 'Apple అనేది A తో ప్రారంభమవుతుంది.'},
        {'question': 'ప్రశ్న: వీటిలో నామవాచకం (Noun) ఏది?', 'options': ['Run (రన్)', 'Happy (హ్యాపీ)', 'Book (బుక్)', 'Quickly (క్విక్లీ)'], 'correct_index': 2, 'explanation': 'Book నామవాచకం (Noun).'},
        {'question': 'ప్రశ్న: Tree అనే పదానికి బహువచనం (Plural) ఏది?', 'options': ['Trees (ట్రీస్)', 'Treees (ట్రీస్)', "Trees' (ట్రీస్)", 'Tree (ట్రీ)'], 'correct_index': 0, 'explanation': 'Tree యొక్క బహువచనం Trees.'},
        {'question': 'ప్రశ్న: వీటిలో విశేషణం (Adjective) ఏది?', 'options': ['Beautiful (బ్యూటిఫుల్)', 'School (స్కూల్)', 'Jump (జంప్)', 'They (దే)'], 'correct_index': 0, 'explanation': 'Beautiful అనేది విశేషణం.'},
        {'question': 'ప్రశ్న: వీటిలో క్రియ (Verb) ఏది?', 'options': ['Sleep (స్లీప్)', 'Book (బుక్)', 'Blue (బ్లూ)', 'Slowly (స్లోలీ)'], 'correct_index': 0, 'explanation': 'Sleep అనేది క్రియ (Verb).'},
        {'question': 'ప్రశ్న: House అనే పదానికి అర్థం ఏమిటి?', 'options': ['ఇల్లు (Home / హౌస్)', 'తోట (Garden)', 'కారు (Car)', 'పుస్తకం (Book)'], 'correct_index': 0, 'explanation': 'House అంటే ఇల్లు (Home).'},
        {'question': 'ప్రశ్న: School అనే పదానికి అర్థం ఏమిటి?', 'options': ['ఆసుపత్రి (Hospital)', 'పాఠశాల (Place for learning)', 'మార్కెట్ (Market)', 'పార్క్ (Park)'], 'correct_index': 1, 'explanation': 'School అంటే పాఠశాల.'}
    ]
    q_c2 = [
        {'question': 'ప్రశ్న: "I am going to school." ఇది ఏ కాలం?', 'options': ['Past Tense (భూతకాలం)', 'Present Tense (వర్తమాన కాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'Command (ఆజ్ఞార్థకం)'], 'correct_index': 1, 'explanation': 'Present Tense (వర్తమాన కాలం).'},
        {'question': 'ప్రశ్న: "He came yesterday." ఇది ఏ కాలం?', 'options': ['Past Tense (భూతకాలం)', 'Present Tense (వర్తమాన కాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'None (ఏదీ కాదు)'], 'correct_index': 0, 'explanation': 'Past Tense (భూతకాలం).'},
        {'question': 'ప్రశ్న: "I will go tomorrow." ఇది ఏ కాలం?', 'options': ['Present Tense (వర్తమాన కాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'Past Tense (భూతకాలం)', 'Noun (నామవాచకం)'], 'correct_index': 1, 'explanation': 'Future Tense (భవిష్యత్ కాలం).'},
        {'question': 'ప్రశ్న: "She is singing a song." ఇది ఏ కాలం?', 'options': ['Present Tense (వర్తమాన కాలం)', 'Past Tense (భూతకాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'Adjective (విశేషణం)'], 'correct_index': 0, 'explanation': 'Present Tense (వర్తమాన కాలం).'},
        {'question': 'ప్రశ్న: "Ate" ఏ కాలాన్ని సూచిస్తుంది?', 'options': ['Present Tense (వర్తమాన కాలం)', 'Past Tense (భూతకాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'None (ఏదీ కాదు)'], 'correct_index': 1, 'explanation': 'Past Tense (భూతకాలం).'},
        {'question': 'ప్రశ్న: "Will read" ఏ కాలానికి చెందుతుంది?', 'options': ['Past Tense (భూతకాలం)', 'Present Tense (వర్తమాన కాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'Adjective (విశేషణం)'], 'correct_index': 2, 'explanation': 'Future Tense (భవిష్యత్ కాలం).'},
        {'question': 'ప్రశ్న: "Is playing" ఏ కాలానికి ఉదాహరణ?', 'options': ['Present Tense (వర్తమాన కాలం)', 'Past Tense (భూతకాలం)', 'Future Tense (భవిష్యత్ కాలం)', 'Noun (నామవాచకం)'], 'correct_index': 0, 'explanation': 'Present Tense (వర్తమాన కాలం).'}
    ]
    q_c3 = [
        {'question': 'ప్రశ్న: "Ram and Ravi went to school." ఇందులో సంధాన పదం (Conjunction) ఏది?', 'options': ['But (బట్)', 'And (యాండ్)', 'Because (బికాజ్)', 'Or (ఆర్)'], 'correct_index': 1, 'explanation': 'And సంధాన పదం.'},
        {'question': 'ప్రశ్న: "Mother and Father" లో సంధాన పదం ఏది?', 'options': ['Mother (మదర్)', 'And (యాండ్)', 'Father (ఫాదర్)', 'In (ఇన్)'], 'correct_index': 1, 'explanation': 'And సంధాన పదం.'},
        {'question': 'ప్రశ్న: "He studied, but he did not pass." ఇందులో సంధాన పదం ఏది?', 'options': ['But (బట్)', 'Studied (స్టడీడ్)', 'Pass (పాస్)', 'Did not (డిడ్ నాట్)'], 'correct_index': 0, 'explanation': 'But సంధాన పదం.'},
        {'question': 'ప్రశ్న: "And" ఏ పదవర్గానికి చెందుతుంది?', 'options': ['Conjunction (సంధాన పదం)', 'Noun (నామవాచకం)', 'Verb (క్రియ)', 'Adjective (విశేషణం)'], 'correct_index': 0, 'explanation': 'And అనేది Conjunction.'},
        {'question': 'ప్రశ్న: "Therefore" అనే పదాన్ని ఎప్పుడు ఉపయోగిస్తారు?', 'options': ['కారణం మరియు ఫలితాన్ని తెలియజేయడానికి (Cause & Effect)', 'నామవాచకంగా (As a Noun)', 'క్రియగా (As a Verb)', 'కాలాన్ని సూచించడానికి (Time)'], 'correct_index': 0, 'explanation': 'Therefore కారణం మరియు ఫలితాన్ని తెలియజేయడానికి ఉపయోగిస్తారు.'},
        {'question': 'ప్రశ్న: సరైన సంధాన పదం (Conjunction) ఏది?', 'options': ['And (యాండ్)', 'Book (బుక్)', 'House (హౌస్)', 'Run (రన్)'], 'correct_index': 0, 'explanation': 'And సరైన సంధాన పదం.'},
        {'question': 'ప్రశ్న: "Or" అంటే ఏమిటి?', 'options': ['రెండు ఎంపికల్లో ఒకటి (Choice between two)', 'సమయం (Time)', 'స్థలం (Place)', 'క్రియ (Action)'], 'correct_index': 0, 'explanation': 'Or అంటే రెండు ఎంపికల్లో ఒకటి.'}
    ]
    q_c4 = [
        {'question': 'ప్రశ్న: Rahul ఎక్కడికి వెళ్తాడు?', 'options': ['Market (మార్కెట్)', 'School (స్కూల్ / పాఠశాల)', 'Park (పార్క్)', 'Home (ఇల్లు)'], 'correct_index': 1, 'explanation': 'Rahul పాఠశాలకు (School) వెళ్తాడు.'},
        {'question': 'ప్రశ్న: Rahul కు ఏమి ఇష్టం?', 'options': ['Games (ఆటలు)', 'Reading books (పుస్తకాలు చదవడం)', 'Sleeping (నిద్రపోవడం)', 'Watching TV (టీవీ చూడడం)'], 'correct_index': 1, 'explanation': 'Rahul కు పుస్తకాలు చదవడం (Reading books) చాలా ఇష్టం.'},
        {'question': 'ప్రశ్న: ఈ గద్యభాగం ఎవరి గురించి?', 'options': ['Sita (సీత)', 'Rahul (రాహుల్)', 'Mohan (మోహన్)', 'Lata (లత)'], 'correct_index': 1, 'explanation': 'ఈ గద్యభాగం Rahul గురించి.'},
        {'question': 'ప్రశ్న: "Every day" అంటే ఏమిటి?', 'options': ['ప్రతి రోజు (Daily)', 'నిన్న (Yesterday)', 'ఎప్పుడూ కాదు (Never)', 'వచ్చే వారం (Next week)'], 'correct_index': 0, 'explanation': 'Every day అంటే ప్రతి రోజు.'},
        {'question': 'ప్రశ్న: Rahul ఏమి చేస్తాడు?', 'options': ['Goes to school (పాఠశాలకు వెళ్తాడు)', 'Goes to market (మార్కెట్కు వెళ్తాడు)', 'Stays home (ఇంట్లో ఉంటాడు)', 'Goes to hospital (ఆసుపత్రికి వెళ్తాడు)'], 'correct_index': 0, 'explanation': 'Rahul పాఠశాలకు వెళ్తాడు (Goes to school).'},
        {'question': 'ప్రశ్న: ఈ గద్యభాగం యొక్క ప్రధాన భావం ఏమిటి?', 'options': ['Study and school habit (చదువు మరియు పాఠశాల అలవాటు)', 'Travel (ప్రయాణం)', 'Rain (వర్షం)', 'Hills (కొండలు)'], 'correct_index': 0, 'explanation': 'ప్రధాన భావం Study and school habit.'},
        {'question': 'ప్రశ్న: సరైన వాక్యం ఏది?', 'options': ['Rahul likes reading books. (రాహుల్కు పుస్తకాలు చదవడం ఇష్టం.)', 'Rahul does not go to school. (రాహుల్ పాఠశాలకు వెళ్లడు.)', 'Rahul always plays. (రాహుల్ ఎప్పుడూ ఆడుతుంటాడు.)', 'Rahul does not read. (రాహుల్ చదవడు.)'], 'correct_index': 0, 'explanation': 'Rahul likes reading books సరైన వాక్యం.'}
    ]
    all_q_sets = [q_c1, q_c2, q_c3, q_c4]
    res = {}
    for idx, lvl in enumerate(levels):
        q_list = all_q_sets[idx]
        for i, item in enumerate(q_list):
            item['id'] = f'te_en_{lvl[0]}_{i+1}'

        res[lvl] = {
            'id': f'{lvl}-te-en',
            'path': lvl,
            'lang': 'en',
            'uiLang': 'te',
            'title': titles[idx],
            'description': f'Learn EN curriculum with TE UI guidance ({lvl}).',
            'objective': f'Learn EN curriculum with TE UI guidance ({lvl}).',
            'lessons': [
                {
                    'id': f'{lvl}-te-en-l1',
                    'title': titles[idx],
                    'learning_goal': f'Learn EN curriculum with TE UI guidance ({lvl}).',
                    'teaching_content': 'Practice learning EN curriculum with TE guidance.',
                    'image_key': 'book',
                    'practice_questions': q_list
                }
            ],
            'checkpoint': {
                'min_pass_score': 70,
                'questions': q_list
            },
            'checkpoint_test': q_list
        }
    return res

def build_en_te():
    levels = ['foundation', 'beginner', 'intermediate', 'advanced']
    titles = [
        'Course 1: Foundation (My Telugu Literacy Journey)',
        'Course 2: Beginner (Telugu Words Around Me)',
        'Course 3: Intermediate (New Steps in Telugu Vocabulary)',
        'Course 4: Advanced (My World in Telugu Sentences)'
    ]
    q_c1 = [
        {'question': 'Question: How many vowels (అచ్చులు) are there in the Telugu alphabet?', 'options': ['14 (Fourteen)', '15 (Fifteen)', '16 (Sixteen)', '12 (Twelve)'], 'correct_index': 2, 'explanation': 'There are 16 vowels (అచ్చులు) in the Telugu alphabet.'},
        {'question': 'Question: What part of speech is the word “అమ్మ” (Amma)?', 'options': ['క్రియ (Verb)', 'నామవాచకం (Noun)', 'విశేషణం (Adjective)', 'సర్వనామం (Pronoun)'], 'correct_index': 1, 'explanation': '“అమ్మ” is a Noun (నామవాచకం).'},
        {'question': 'Question: What is the plural form of “చెట్టు” (Chettu)?', 'options': ['చెట్టు (Tree)', 'చెట్లు (Trees)', 'చెట్టులు (Chettulu)', 'చెట్ల (Chetla)'], 'correct_index': 1, 'explanation': 'The plural form of “చెట్టు” is “చెట్లు”.'},
        {'question': 'Question: What part of speech is “మంచి” (Manchi)?', 'options': ['విశేషణం (Adjective)', 'నామవాచకం (Noun)', 'క్రియ (Verb)', 'అవ్యయం (Invariable)'], 'correct_index': 0, 'explanation': '“మంచి” is an Adjective (విశేషణం).'},
        {'question': 'Question: What part of speech is “చదువుతున్నాను” (Chaduvutunnanu)?', 'options': ['నామవాచకం (Noun)', 'క్రియ (Verb)', 'విశేషణం (Adjective)', 'సర్వనామం (Pronoun)'], 'correct_index': 1, 'explanation': '“చదువుతున్నాను” is a Verb (క్రియ).'},
        {'question': 'Question: What is the meaning of the word “పుస్తకం” (Pustakam)?', 'options': ['ఇల్లు (House)', 'గ్రంథం (Book)', 'చెట్టు (Tree)', 'రహదారి (Road)'], 'correct_index': 1, 'explanation': '“పుస్తకం” means Book (గ్రంథం).'},
        {'question': 'Question: What is the meaning of the word “పాఠశాల” (Pathashala)?', 'options': ['ఆసుపత్రి (Hospital)', 'పాఠాలు నేర్చుకునే స్థలం (Place for learning)', 'మార్కెట్ (Market)', 'ఉద్యానవనం (Park)'], 'correct_index': 1, 'explanation': '“పాఠశాల” means Place for learning (School).'}
    ]
    q_c2 = [
        {'question': 'Question: “నేను పాఠశాలకు వెళుతున్నాను.” (I am going to school) — Which tense is this?', 'options': ['భూతకాలం (Past Tense)', 'వర్తమాన కాలం (Present Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'ఆజ్ఞార్థకం (Command)'], 'correct_index': 1, 'explanation': 'It is Present Tense (వర్తమాన కాలం).'},
        {'question': 'Question: “అతను నిన్న వచ్చాడు.” (He came yesterday) — Which tense is this?', 'options': ['భూతకాలం (Past Tense)', 'వర్తమాన కాలం (Present Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'లేదు (None)'], 'correct_index': 0, 'explanation': '“వచ్చాడు” is Past Tense (భూతకాలం).'},
        {'question': 'Question: “నేను రేపు వెళ్తాను.” (I will go tomorrow) — Which tense is this?', 'options': ['వర్తమాన కాలం (Present Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'భూతకాలం (Past Tense)', 'నామవాచకం (Noun)'], 'correct_index': 1, 'explanation': '“వెళ్తాను” is Future Tense (భవిష్యత్ కాలం).'},
        {'question': 'Question: “ఆమె పాట పాడుతోంది.” (She is singing a song) — Which tense is this?', 'options': ['వర్తమాన కాలం (Present Tense)', 'భూతకాలం (Past Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'విశేషణం (Adjective)'], 'correct_index': 0, 'explanation': 'It is Present Tense (వర్తమాన కాలం).'},
        {'question': 'Question: “తిన్నాడు” (Ate) — Which tense does this indicate?', 'options': ['వర్తమాన కాలం (Present Tense)', 'భూతకాలం (Past Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'లేదు (None)'], 'correct_index': 1, 'explanation': '“తిన్నాడు” indicates Past Tense (భూతకాలం).'},
        {'question': 'Question: “చదువుతాను” (Will read) — Which tense does this belong to?', 'options': ['భూతకాలం (Past Tense)', 'వర్తమాన కాలం (Present Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'విశేషణం (Adjective)'], 'correct_index': 2, 'explanation': '“చదువుతాను” is Future Tense (భవిష్యత్ కాలం).'},
        {'question': 'Question: “ఆడుతున్నాడు” (Is playing) — Which tense is this an example of?', 'options': ['వర్తమాన కాలం (Present Tense)', 'భూతకాలం (Past Tense)', 'భవిష్యత్ కాలం (Future Tense)', 'నామవాచకం (Noun)'], 'correct_index': 0, 'explanation': 'It is Present Tense (వర్తమాన కాలం).'}
    ]
    q_c3 = [
        {'question': 'Question: “రాము మరియు రవి పాఠశాలకు వెళ్లారు.” — Which word is the conjunction (సంధాన పదం)?', 'options': ['కానీ (But)', 'మరియు (And)', 'ఎందుకంటే (Because)', 'లేదా (Or)'], 'correct_index': 1, 'explanation': '“మరియు” is the conjunction.'},
        {'question': 'Question: In “అమ్మ మరియు నాన్న”, which word is the conjunction?', 'options': ['అమ్మ (Mother)', 'మరియు (And)', 'నాన్న (Father)', 'లో (In)'], 'correct_index': 1, 'explanation': '“మరియు” is the conjunction.'},
        {'question': 'Question: “అతను చదివాడు, కానీ ఉత్తీర్ణుడు కాలేదు.” — Which word is the conjunction?', 'options': ['కానీ (But)', 'చదివాడు (Studied)', 'ఉత్తీర్ణుడు (Passed)', 'కాలేదు (Did not)'], 'correct_index': 0, 'explanation': '“కానీ” is the conjunction.'},
        {'question': 'Question: What part of speech is “మరియు” (And)?', 'options': ['సంధాన పదం (Conjunction)', 'నామవాచకం (Noun)', 'క్రియ (Verb)', 'విశేషణం (Adjective)'], 'correct_index': 0, 'explanation': '“మరియు” is a Conjunction (సంధాన పదం).'},
        {'question': 'Question: When is the word “అందువల్ల” (Therefore) used?', 'options': ['కారణం మరియు ఫలితాన్ని తెలియజేయడానికి (To convey Cause and Effect)', 'నామవాచకంగా (As a Noun)', 'క్రియగా (As a Verb)', 'కాలాన్ని సూచించడానికి (To show Time)'], 'correct_index': 0, 'explanation': '“అందువల్ల” is used to convey cause and effect.'},
        {'question': 'Question: Which is a valid conjunction (సంధాన పదం)?', 'options': ['మరియు (And)', 'పుస్తకం (Book)', 'ఇల్లు (House)', 'పరుగెత్తు (Run)'], 'correct_index': 0, 'explanation': '“మరియు” is a valid conjunction.'},
        {'question': 'Question: What does “లేదా” (Or) mean?', 'options': ['రెండు ఎంపికల్లో ఒకటి (One of two options)', 'సమయం (Time)', 'స్థలం (Place)', 'క్రియ (Action)'], 'correct_index': 0, 'explanation': '“లేదా” means choice between options.'}
    ]
    q_c4 = [
        {'question': 'Question: Where does Rahul go?', 'options': ['మార్కెట్ (Market)', 'పాఠశాల (School)', 'పార్క్ (Park)', 'ఇల్లు (Home)'], 'correct_index': 1, 'explanation': 'Rahul goes to school (పాఠశాల).'},
        {'question': 'Question: What does Rahul like?', 'options': ['ఆటలు (Games)', 'పుస్తకాలు చదవడం (Reading books)', 'నిద్రపోవడం (Sleeping)', 'టీవీ చూడడం (Watching TV)'], 'correct_index': 1, 'explanation': 'Rahul likes reading books (పుస్తకాలు చదవడం).'},
        {'question': 'Question: Who is this passage about?', 'options': ['సీత (Sita)', 'రాహుల్ (Rahul)', 'మోహన్ (Mohan)', 'లత (Lata)'], 'correct_index': 1, 'explanation': 'This passage is about Rahul (రాహుల్).'},
        {'question': 'Question: What does “ప్రతిరోజూ” mean?', 'options': ['ప్రతి రోజు (Every day)', 'నిన్న (Yesterday)', 'ఎప్పుడూ కాదు (Never)', 'వచ్చే వారం (Next week)'], 'correct_index': 0, 'explanation': '“ప్రతిరోజూ” means Every day.'},
        {'question': 'Question: What does Rahul do?', 'options': ['పాఠశాలకు వెళ్తాడు (Goes to school)', 'మార్కెట్కు వెళ్తాడు (Goes to market)', 'ఇంట్లో ఉంటాడు (Stays home)', 'ఆసుపత్రికి వెళ్తాడు (Goes to hospital)'], 'correct_index': 0, 'explanation': 'Rahul goes to school (పాఠశాలకు వెళ్తాడు).'},
        {'question': 'Question: What is the main idea of this passage?', 'options': ['చదువు మరియు పాఠశాల అలవాటు (Study and school habit)', 'ప్రయాణం (Travel)', 'వర్షం (Rain)', 'కొండలు (Hills)'], 'correct_index': 0, 'explanation': 'The main idea is Study and school habit.'},
        {'question': 'Question: Which statement is correct?', 'options': ['రాహుల్కు పుస్తకాలు చదవడం ఇష్టం. (Rahul likes reading books.)', 'రాహుల్ పాఠశాలకు వెళ్లడు. (Rahul does not go to school.)', 'రాహుల్ ఎప్పుడూ ఆడుతుంటాడు. (Rahul always plays.)', 'రాహుల్ చదవడు. (Rahul does not read.)'], 'correct_index': 0, 'explanation': 'The correct statement is “రాహుల్కు పుస్తకాలు చదవడం ఇష్టం.”'}
    ]
    all_q_sets = [q_c1, q_c2, q_c3, q_c4]
    res = {}
    for idx, lvl in enumerate(levels):
        q_list = all_q_sets[idx]
        for i, item in enumerate(q_list):
            item['id'] = f'en_te_{lvl[0]}_{i+1}'

        res[lvl] = {
            'id': f'{lvl}-en-te',
            'path': lvl,
            'lang': 'te',
            'uiLang': 'en',
            'title': titles[idx],
            'description': f'Learn TE curriculum with EN UI guidance ({lvl}).',
            'objective': f'Learn TE curriculum with EN UI guidance ({lvl}).',
            'lessons': [
                {
                    'id': f'{lvl}-en-te-l1',
                    'title': titles[idx],
                    'learning_goal': f'Learn TE curriculum with EN UI guidance ({lvl}).',
                    'teaching_content': 'Practice learning TE curriculum with EN guidance.',
                    'image_key': 'book',
                    'practice_questions': q_list
                }
            ],
            'checkpoint': {
                'min_pass_score': 70,
                'questions': q_list
            },
            'checkpoint_test': q_list
        }
    return res

# Load existing BILINGUAL_COURSES from file
with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)
if not match:
    match = re.search(r'export const BILINGUAL_COURSES = ({[\s\S]*?});\n\nexport function getBilingualCourse', text)

courses = json.loads(match.group(1))

# Update only the 8 requested pairs
courses['ta-hi'] = build_ta_hi()
courses['hi-ta'] = build_hi_ta()
courses['te-en'] = build_te_en()
courses['en-te'] = build_en_te()

# Save updated JSON back to file
new_json_str = json.dumps(courses, indent=2, ensure_ascii=False)
idx = text.find('{')
end_idx = text.rfind('};')

new_file_content = f'export const BILINGUAL_COURSES = {new_json_str};\n\nexport function getBilingualCourse(courseIdOrPath, uiLang, learnLang) {{\n  if (!uiLang || !learnLang) return null;\n  const pairKey = uiLang + \'-\' + learnLang;\n  const pairCourses = BILINGUAL_COURSES[pairKey];\n  if (!pairCourses) return null;\n\n  const key = courseIdOrPath.split(\'-\')[0].trim();\n  const levelKey = key.toLowerCase();\n  \n  if (pairCourses[levelKey]) return pairCourses[levelKey];\n  \n  for (const lvl of [\'foundation\', \'beginner\', \'intermediate\', \'advanced\']) {{\n    if (courseIdOrPath.toLowerCase().includes(lvl)) return pairCourses[lvl];\n  }}\n  return null;\n}}\n\nexport function loadBilingualCoursesList(uiLang, learnLang) {{\n  if (!uiLang || !learnLang) return null;\n  const pairKey = uiLang + \'-\' + learnLang;\n  const pairCourses = BILINGUAL_COURSES[pairKey];\n  if (!pairCourses) return null;\n  return Object.values(pairCourses);\n}}\n'

with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print("Successfully updated requested pairs in bilingualCourses.js!")
