# Programmers - Lv1 - Sum between 2 int
def solution(a, b):
    answer = 0
    if a < b:
        start = a
        end = b
    elif a > b:
        start = b
        end = a
    else:
        return a

    for i in range(start, end+1):
        answer += i
    return answer

print(solution(5, 3))