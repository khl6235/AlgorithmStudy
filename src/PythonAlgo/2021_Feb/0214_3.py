# Programmers - Lv2 - Skill Tree
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        tmp = [letter for letter in st if letter in skill]
        answer += 1 if skill.startswith(''.join(tmp)) else 0
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))