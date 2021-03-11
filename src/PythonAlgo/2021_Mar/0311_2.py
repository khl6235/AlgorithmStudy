# Programmers - Lv2 - N LCM
from math import gcd
def solution(arr):
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b//gcd(a, b))
    return arr[0]

arr = [2,6,8,14]
arr2 = [1,2,3]
print(solution(arr2))