# Programmers - Lv1 - Reverse Array
def solution(n):
    answer = []
    q = n
    while(q > 0):
        m = q%10
        q = q//10
        answer.append(m)
    return answer

n = 12345
print(solution(n))