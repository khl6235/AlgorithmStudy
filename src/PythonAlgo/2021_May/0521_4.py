# BOJ 2606 - DFS - Virus
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = -1
for _ in range(m):
    n1, n2 = map(int, input().split(' '))
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

dfs(1)
for v in visited:
    if v:
        cnt += 1

print(cnt)