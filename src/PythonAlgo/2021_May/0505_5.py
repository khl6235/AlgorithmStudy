# Programmers - Heap - Double Priority Queue
import heapq
def solution(operations):
    min_hq = [] # pop하면 원래대로 최솟값이 나옴
    max_hq = [] # pop하면 최댓값이 나옴
    for op in operations:
        opr = op.split(" ")
        print(opr[1])
        if opr[0] == 'I':
            num = int(opr[1])
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, (num*(-1), num))
        else:
            if len(min_hq) == 0: # necessary!
                pass
            elif opr[1] == "1":
                min_hq.remove(heapq.heappop(max_hq)[1])
            elif opr[1] == "-1":
                tmp = heapq.heappop(min_hq)
                max_hq.remove((tmp*(-1), tmp))
    
    if min_hq:
        return [heapq.heappop(max_hq)[1], heapq.heappop(min_hq)]
    else:
        return [0, 0]

operations = ["I 16","D 1"]
operations2 = ["I 7","I 5","I -5","D -1"]
print(solution(operations2))