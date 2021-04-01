from collections import deque

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for e in adj[start]:
        if not visited[e]:
            dfs(e)

def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                q.append(e)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
