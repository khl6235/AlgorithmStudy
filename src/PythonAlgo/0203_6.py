# Programmers - Lv1 - String to Int
def solution(s):
    answer = 0
    if s[0] == '-':
        s = s[1:]
        answer = -int(s)
    elif s[0] == '+':
        s = s[1:]
        answer = int(s)
    else:
        answer = int(s)
    return answer

s = "+1234"
print(solution(s))