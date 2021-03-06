# Programmers - Lv1 - P and Y num
def solution(s):
    answer = False
    p_num = 0
    y_num = 0
    for ch in s:
        if ord(ch) == 80 or ord(ch) == 112:
            p_num += 1
        elif ord(ch) == 89 or ord(ch) == 121:
            y_num += 1
        else:
            continue
    
    if p_num == y_num:
        answer = True
    
    return answer

s = "pPoooyY"
print(solution(s))