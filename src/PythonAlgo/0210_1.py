# Programmers - Lv1 - Budget
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
    return answer

d = [1,3,2,5,4]
budget = 9
d2 = [2,2,3,3]
budget2 = 10
print(solution(d2, budget2))