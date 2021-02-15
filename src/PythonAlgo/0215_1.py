# Programmers - Lv2 - 124 world
def solution(n):
    answer = 0
    i = 0
    while n >= (3**i):
        n -= 3**i
        i += 1
    while i > 0:
        i -= 1
        answer += trans(n//3**i)*(10**i)
        n = n%(3**i)

    return str(answer)

def trans(n):
    return {0: 1, 1: 2, 2: 4}[n]

print(solution(41))