# Programmers - Lv1 - New ID
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for ch in new_id:
        if(ch == '-' or ch == '_' or ch == '.' or (97 <= ord(ch) <= 122) or (48 <= ord(ch) <= 57)):
            if len(answer) > 0 and answer[-1] == '.' and ch == '.':
                continue
            answer += ch

    answer = answer.strip(".")
    if len(answer) == 0:
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip(".")
    if len(answer) <= 2:
        letter = answer[-1]
        while len(answer) < 3:
            answer += letter

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "=.="
print(solution(new_id))