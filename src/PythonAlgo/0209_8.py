# Programmers - Lv1 - N numbers with x terms
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

print(solution(-4, 2))