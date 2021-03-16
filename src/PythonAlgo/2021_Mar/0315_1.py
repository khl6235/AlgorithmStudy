# Programmers - Lv2 - Delivery
# Dijkstra, heapq
from collections import defaultdict
import heapq
def solution(N, road, K):
    answer = 0
    town = defaultdict(list)
    
    for v1, v2, w in road:
        town[v1].append((v2, w))
        town[v2].append((v1, w))

    for _, v in dijkstra(town, 1).items():
        answer += 1 if v <= K else 0
    
    return answer

def dijkstra(town, start):
    delivery = {node:float('inf') for node in town}
    heap = [(1, 0)]
    while heap:
        v_now, w_now = heapq.heappop(heap)
        if delivery[v_now] < w_now:
            continue
        delivery[v_now] = w_now
        for i in range(len(town[v_now])):
            v2, w2 = town[v_now][i]
            if w_now + w2 < delivery[v2]:
                heapq.heappush(heap, (v2, w_now+w2))
        
    return delivery
    

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
N2 = 6
road2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K2 = 4
print(solution(N2, road2, K2))