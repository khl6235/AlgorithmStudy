# Programmers - Stack/Queue - Printer
def solution(priorities, location):
    answer = 0
    queue = [(p, i) for i, p in enumerate(priorities)]
    while queue:
        tmp = queue.pop(0)
        if queue and tmp[0] < max(queue)[0]:
            queue.append(tmp)
        else:
            answer += 1
            if tmp[1] == location:
                return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))