# Programmers - Lv2 - Number Expression
def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        answer += check(i, n)
    return answer

def check(i, n):
    tmp = 0
    while tmp < n:
        tmp += i
        i += 1
    
    return 1 if tmp == n else 0

n = 15
print(solution(n))