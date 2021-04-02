from collections import deque

def bfs(start, visited):
    queue = deque([start])
    count = 0
    while queue:
        x = queue.popleft()
        if not visited[x]:
            visited[x] = True
            count += 1
            for nx in adj[x]:
                if not visited[nx]:
                    queue.append(nx)  
    return count

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

result = [0] * (n + 1)
for i in range(1, n + 1):
    check = [False] * (n + 1)
    result[i] = bfs(i, check)

max_count = max(result)
for i in range(1, n + 1):
    if result[i] == max_count:
        print(i, end=' ')