# Programmers - Lv2 - Game Map Shortest
from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dq = deque()
    # dq에 아예 좌표값과 cnt 값을 같이 넣음
    dq.append((0, 0, 1))

    while dq:
        now_n, now_m, now_cnt = dq.popleft()
        maps[now_n][now_m] = 0
        for dn, dm in d:
            next_n = now_n + dn
            next_m = now_m + dm

            # 맨 끝 위치에 도달했을 때 바로 return
            if next_n == n-1 and next_m == m-1:
                return now_cnt+1

            # 범위 내에 있고 벽이 아닐 때, 이전 위치는 아예 0(벽)으로 만들어버리고 dq에 추가
            elif 0 <= next_n < n and 0 <= next_m < m and maps[next_n][next_m] == 1:
                maps[next_n][next_m] = 0
                dq.append((next_n, next_m, now_cnt+1))

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))