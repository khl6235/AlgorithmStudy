# Programmers - Stack/Queue - Function Development
import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for p, s in zip(progresses, speeds):
        queue.append(math.ceil((100-p)/s))
    
    while queue:
        tmp = queue.pop(0)
        cnt = 1
        while queue and tmp >= queue[0]:
            queue.pop(0)
            cnt += 1
        answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]
print(solution(progresses2, speeds2))