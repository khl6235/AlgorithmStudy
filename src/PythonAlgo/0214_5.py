# Programmers - Lv2 - Function Development
import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for i, v in enumerate(progresses):
        queue.append(math.ceil((100-v)/speeds[i]))

    while queue:
        front = queue.pop(0)
        cnt = 1
        while queue and front >= queue[0]:
            cnt += 1
            queue.pop(0)
        answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]
print(solution(progresses2, speeds2))