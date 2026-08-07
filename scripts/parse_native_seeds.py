import json
import re

def parse_seed_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Regex to capture course objects
    courses = []
    # Find all question arrays in seed files
    # Match course id/title/path and questions
    course_blocks = re.findall(r'\{\s*id:\s*[\'\"](.*?)[\'\"][\s\S]*?questions:\s*(\[[\s\S]*?\])\s*,\s*\}', text)
    for c_id, q_text in course_blocks:
        q_matches = re.findall(r'\{\s*id:\s*[\'\"](.*?)[\'\"]\s*,\s*question:\s*[\'\"](.*?)[\'\"]\s*,\s*options:\s*(\[.*?\])\s*,\s*correct_index:\s*(\d+)\s*,\s*explanation:\s*[\'\"](.*?)[\'\"]', q_text)
        q_list = []
        for q_id, q_str, opts_str, c_idx, exp in q_matches:
            q_list.append({
                'id': q_id,
                'question': q_str,
                'options': eval(opts_str),
                'correct_index': int(c_idx),
                'explanation': exp
            })
        courses.append({
            'id': c_id,
            'questions': q_list
        })
    return courses

en_seed = parse_seed_js('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_english_only.js')
hi_seed = parse_seed_js('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_hindi.js')
ta_seed = parse_seed_js('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_tamil.js')
te_seed = parse_seed_js('/home/surya/Downloads/LiteralAI/backend/src/utils/seed_telugu.js')

print(f"Loaded seeds: EN={len(en_seed)}, HI={len(hi_seed)}, TA={len(ta_seed)}, TE={len(te_seed)}")
