# Programmers - Lv1 - Prime number
# 에라토스테네스의 체
def solution(n):
    answer = 0
    sieve = [True] * (n-1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i-2] == True:
            for j in range(i+i, n+1, i):
                sieve[j-2] = False

    for i in range(0, n-1):
        if sieve[i] == True:
            answer += 1
        
    return answer

print(solution(10))