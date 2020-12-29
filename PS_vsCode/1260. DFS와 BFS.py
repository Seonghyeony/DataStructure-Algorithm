from collections import deque

N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]

def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in adj[start]:
        if not visited[node]:
            dfs(node, visited)

def bfs(start, visited):
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        if not visited[current_node]:
            visited[current_node] = True
            print(current_node, end=' ')
            for node in adj[current_node]:
                if not visited[node]:
                    queue.append(node)

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (N + 1)
dfs(V, visited)
print()
visited = [False] * (N + 1)
bfs(V, visited)