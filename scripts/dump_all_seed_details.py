import json
import re

def parse_seed_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    courses = []
    # match each course object { id: '...', path: '...', questions: [...] }
    # split by { id:
    raw_courses = re.split(r'\{\s*id:\s*', content)[1:]
    for rc in raw_courses:
        lines = rc.split('\n')
        c_id = lines[0].split("'")[1] if "'" in lines[0] else lines[0].split('"')[1]
        
        # parse questions
        q_blocks = re.findall(r'question:\s*[\'\"](.*?)[\'\"][\s\S]*?options:\s*(\[[\s\S]*?\])[\s\S]*?correct_index:\s*(\d+)[\s\S]*?explanation:\s*[\'\"](.*?)[\'\"]', rc)
        q_list = []
        for q_text, opts_str, c_idx, exp in q_blocks:
            opts_clean = opts_str.replace('\n', '').replace('  ', '')
            try:
                opts = eval(opts_clean)
            except:
                opts = opts_clean
            q_list.append({
                'question': q_text,
                'options': opts,
                'correct_index': int(c_idx),
                'explanation': exp
            })
        courses.append({
            'id': c_id,
            'questions': q_list
        })
    return courses

seeds = {
    'en': parse_seed_file('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_english_only.js'),
    'hi': parse_seed_file('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_hindi.js'),
    'ta': parse_seed_file('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_tamil.js'),
    'te': parse_seed_file('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_telugu.js'),
    'kn': parse_seed_file('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_kannada.js')
}

with open('/home/surya/Downloads/LiteralAI/scripts/parsed_seeds.json', 'w', encoding='utf-8') as f:
    json.dump(seeds, f, indent=2, ensure_ascii=False)

print("Dumped all seed details to scripts/parsed_seeds.json!")
