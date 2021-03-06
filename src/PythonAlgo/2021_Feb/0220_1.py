# Programmers - Lv2 - Prime Number
from itertools import permutations
def solution(numbers):
    answer = 0
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))

    tmp = []
    for i in per:
        tmp.append(int("".join(i)))
    tmp = list(set(tmp))

    for t in tmp:
        answer += 1 if prime(t) else 0

    return answer

def prime(n):
    print(n)
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                return False
            
        return True

numbers = "17"
numbers2 = "011"
print(solution(numbers))