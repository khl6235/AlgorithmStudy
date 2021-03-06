# Programmers - Lv2 - Camouflage
from collections import Counter
def solution(clothes):
    answer = 1
    item = []
    for _, b in clothes:
        item.append(b)
    
    item = Counter(item)
    for i in item.values():
        answer *= (i+1)
    
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))