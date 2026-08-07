with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'question: "கேள்வி: "मैं और तुम"' in line:
        lines[i] = line.replace('question: "கேள்வி: "मैं और तुम" (Main aur tum) இல் \'और\' என்பது?"', "question: 'கேள்வி: \"मैं और तुम\" (Main aur tum) இல் \\'और\\' என்பது?'")

with open('/home/surya/Downloads/LiteralAI/backend/src/data/bilingualCourses.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed line 3034!")
