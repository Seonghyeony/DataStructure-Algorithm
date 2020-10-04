def dfs(y, x, d):
    global result
    if lst[y][x] == 0:
        lst[y][x] = 2
        result += 1

    tmp = direct[d]

    for dy, dx, nd in tmp:
        ny, nx = y + dy, x + dx
        if ny <= 0 or ny >= N-1 or nx <= 0 or nx >= M-1:
            continue
        if lst[ny][nx] == 0 and lst[ny][nx] != 1:
            dfs(ny, nx, nd)
            return

    idx = (d + 2) % 4
    ny, nx = y + direct2[idx][0], x + direct2[idx][1]
    if ny <= 0 or ny >= N-1 or nx <= 0 or nx >= M-1:
        return
    elif lst[ny][nx] == 1:
        return
    else:
        dfs(ny, nx, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

direct = [[(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)], [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)], 
            [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)], [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]]

direct2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0
dfs(r, c, d)
print(result)




