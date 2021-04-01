from collections import deque

def bfs(start):
    queue = deque([start])
    count = 0
    while queue:
        x = queue.popleft()
        if not visited[x]:
            if x != 1:
                count += 1
            visited[x] = True
            for nx in adj[x]:
                if not visited[nx]:
                    queue.append(nx)
    return count

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
visited = [False] * (n + 1)
print(bfs(1))
