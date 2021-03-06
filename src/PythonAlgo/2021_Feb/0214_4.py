# Programmers - Lv2 - Printer
from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque([(v, i) for i, v in enumerate(priorities)])
    while dq:
        top = dq.popleft()
        if dq and top[0] < max(dq)[0]:
            dq.append(top)
        else:
            answer += 1
            if location == top[1]:
                break
    
    return answer

priorities = [2, 1, 3, 2]
location = 2
priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
print(solution(priorities2, location2))