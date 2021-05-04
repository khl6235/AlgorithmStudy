# Programmers - Hash - Camouflage
from collections import defaultdict
def solution(clothes):
    dict_cloth = defaultdict(list)
    for c in clothes:
        dict_cloth[c[1]].append(c[0])
    res = 1
    for _, v in dict_cloth.items():
        res *= len(v)+1
    return res-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes2))