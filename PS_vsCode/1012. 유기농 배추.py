from collections import deque

T = int(input())

def check(x, y):
    if x < 0 or x >= M:
        return False
    
    if y < 0 or y >= N:
        return False
    
    return True

def bfs(start):
    candidate = deque()
    candidate.append(start)
    while candidate:
        y, x = candidate.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if check(nx, ny):
                    if lst[ny][nx] and not visited[ny][nx]:
                        candidate.append((ny, nx))

for _ in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        lst[Y][X] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] and not visited[i][j]:
                result += 1
                bfs((i, j))
    print(result)