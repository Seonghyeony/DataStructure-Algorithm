from collections import deque

test_case = int(input())
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0<= ny < n and 0 <= nx < m and lst[ny][nx] != 0 and not visited[ny][nx]:
                    queue.append([ny, nx])

for _ in range(test_case):
    m, n, k = map(int, input().split())
    lst = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        lst[y][x] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1 and not visited[i][j]:
                bfs([i, j])
                result += 1
    print(result)

