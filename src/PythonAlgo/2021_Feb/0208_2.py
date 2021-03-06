# Programmers - Lv1 - Digit Sum
def solution(n):
    answer = 0
    tmp = str(n)
    for i in range(0, len(tmp)):
        answer += int(tmp[i])
    return answer

n = 123
n2 = 987
print(solution(n2))