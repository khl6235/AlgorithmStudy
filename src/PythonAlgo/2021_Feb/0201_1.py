# Programmers - Lv1 - Watermelon

def solution(n):
    answer = ''
    answer += '수박'*(n//2)
    if n%2 == 1:
        answer += '수'
    return answer

print(solution(7))