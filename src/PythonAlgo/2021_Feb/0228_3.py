# Programmers - Lv2 - Next Largest Number
from collections import Counter
def solution(n):
    bn = binary(n)
    one = Counter(bn)['1']
    for i in range(n+1, 1000001):
        if Counter(binary(i))['1'] == one:
            return i

def binary(n):
    res = ''
    while n > 0:
        res += '0' if n % 2 == 0 else '1'
        n = n // 2
    return res[::-1]

n = 78
n2 = 15
print(solution(n))
