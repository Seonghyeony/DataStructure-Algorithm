def solve(y, x, d):
    global count
    flag = True
    for _ in range(4):
        d = (d - 1) % 4
        ny, nx = y + dy[d], x + dx[d]
        if not visited[ny][nx] and lst[ny][nx] == 0:
            flag = False
            visited[ny][nx] = True
            count += 1
            solve(ny, nx, d)
            return
    if flag:
        nd = (d + 2) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if lst[ny][nx] != 1:
            solve(ny, nx, d)
    return

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[r][c] = True
count = 1
solve(r, c, d)
print(count)
