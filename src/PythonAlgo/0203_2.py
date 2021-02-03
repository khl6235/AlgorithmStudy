# Programmers - Lv1 - Training suit
def solution(n, lost, reserve):
    answer = 0
    std = list(range(1, n+1))
    lost.sort()
    reserve.sort()
    for l in lost:
        std[l-1] = 0
    for r in reserve:
        if std[r-1] == 0:
            std[r-1] = r
            continue
        if r > 1 and std[r-2] == 0:
            std[r-2] = r
        elif r < n-1 and std[r] == 0:
            std[r] = r

    for i in std:
        if i != 0:
            answer += 1
    return answer

n = 5
lost = [1,2,3,4,5]
reserve = [1,2,3,4,5]
print(solution(n, lost, reserve))