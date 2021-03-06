# Programmers - Lv1 - String Basic
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        for ch in s:
            if (48 <= ord(ch) <= 57):
                answer = True
            else:
                answer = False
                break
    return answer

s = "a234"
print(solution(s))