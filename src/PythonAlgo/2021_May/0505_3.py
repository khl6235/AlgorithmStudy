# Programmers - Heap - More Spicy
import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for sc in scoville:
        heapq.heappush(hq, sc)
    
    while hq[0] < K:
        heapq.heappush(hq, heapq.heappop(hq)+heapq.heappop(hq)*2)
        if len(hq) < 2 and hq[0] < K:
            return -1
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))