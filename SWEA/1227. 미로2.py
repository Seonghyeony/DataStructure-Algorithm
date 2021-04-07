from collections import deque

def bfs(n, lst, r, c):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([[r, c]])
    while queue:
        y, x = queue.popleft()
        if lst[y][x] == '3':
            return True
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                    if lst[ny][nx] != '1':
                        queue.append([ny, nx])
    return False

        
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
for _ in range(10):
    test_case = int(input())
    N = 100
    lst = [list(input()) for _ in range(N)]
    flag = False
    sy, sx = 0, 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '2':
                sy, sx = i, j
                flag = True
                break
        if flag:
            break
    if bfs(N, lst, sy, sx):
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))