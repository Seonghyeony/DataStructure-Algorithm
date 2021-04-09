from collections import deque

def bfs(y, x):
    queue = deque([[y, x]])
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx]:
                    queue.append([ny, nx])

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

for test_case in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = []
    direction = [[0, 1], [1, 0]]
    for i in range(N):
        for j in range(N):
            if lst[i][j] and not visited[i][j]:
                row, col = 0, 0
                for d in range(2):
                    count = 1
                    r, c = i, j
                    while True:
                        nr, nc = r + direction[d][0], c + direction[d][1]
                        if 0 <= nr < N and 0 <= nc < N and lst[nr][nc]:
                            count += 1
                            r, c = nr, nc
                        else:
                            break
                    if d == 0:
                        col = count
                    else:
                        row = count
                bfs(i, j)
                result.append([row * col, row, col])
    result = sorted(result, key=lambda x: (x[0], x[1]))
    print('#{} {}'.format(test_case, len(result)), end=' ')
    for size, r, c in result:
        print('{} {}'.format(r, c), end=' ')
    print()


            


                