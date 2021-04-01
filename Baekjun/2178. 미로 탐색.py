from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * M for _ in range(N)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

while queue:
    y, x = queue.popleft()

    if y == N - 1 and x == M - 1:
        print(visited[y][x])
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if visited[ny][nx] == 0 and lst[ny][nx] == '1':
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))


