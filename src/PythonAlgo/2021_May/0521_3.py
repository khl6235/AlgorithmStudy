# BOJ 1260 - BFS - DFS&BFS
n, m, v = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

def bfs(v):
    q = [v]
    while q:
        v2 = q.pop(0)
        if not visited[v2]:
            print(v2, end=' ')
            visited[v2] = True
            for e in graph[v2]:
                if not visited[e]:
                    q.append(e)

for _ in range(m):
    n1, n2 = map(int, input().split(' '))
    graph[n1].append(n2)
    graph[n2].append(n1)

for g in graph:
    g.sort()

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)