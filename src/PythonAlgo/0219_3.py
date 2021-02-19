# Programmers - Lv2 - More Spicy
import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for sc in scoville:
        heapq.heappush(hq, sc)
    while hq[0] < K:
        first = heapq.heappop(hq)
        second = heapq.heappop(hq)
        heapq.heappush(hq, first+second*2)
        if len(hq) < 2 and hq[0] < K:
            return -1
        answer += 1
         
    return answer

scoville =[3, 1, 2, 9, 10, 12]
K = 7
scoville2 = [1, 2, 3]
K2 = 11
print(solution(scoville2, K2))