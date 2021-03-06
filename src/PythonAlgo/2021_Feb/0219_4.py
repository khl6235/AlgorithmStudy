# Programmers - Lv2 - Menu Renewal
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    order = [list(o) for o in orders]
    for c in course:
        menu = []
        for o in order:
            menu += map(''.join, combinations(sorted(o), c))
        cntr = Counter(menu).most_common()
        answer += [m for m, c in cntr if c > 1 and c == cntr[0][1]]

    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))