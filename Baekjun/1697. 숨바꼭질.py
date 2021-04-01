from collections import deque

def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
print(bfs())