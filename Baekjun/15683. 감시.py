# 1시간 소요.

def detect(y, x, dy, dx):
    ret = 0
    while True:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] < 6:
                if lst[ny][nx] == 0:
                    lst[ny][nx] -= 1
                    ret += 1
                elif lst[ny][nx] < 0:
                    lst[ny][nx] -= 1
            else:
                break
        else:
            break
        y, x = ny, nx
    return ret

def reDetect(y, x, dy, dx):
    while True:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == 6:
                break
            if lst[ny][nx] < 0:
                lst[ny][nx] += 1
        else:
            break
        y, x = ny, nx      

def solve(n, safeArea):
    global result
    if n == K:
        # print("n == K", safeArea)
        if result > safeArea:
            result = safeArea
        return

    y, x, num = cctv[n]
    direct = direction[num]
    for i in range(len(direct)):
        detect_lst = direct[i]
        count = 0
        for j in range(len(detect_lst)):
            dy, dx = detect_lst[j]
            count += detect(y, x, dy, dx)
        # print(count)
        solve(n + 1, safeArea - count)
        for j in range(len(detect_lst)):
            dy, dx = detect_lst[j]
            reDetect(y, x, dy, dx)
    return

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cctv = []
direction = [
    [], 
    [[[0, 1]], [[1, 0]], [[0, -1]], [[-1, 0]]], 
    [[[0, -1], [0, 1]], [[1, 0], [-1, 0]]],
    [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
    [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]]], 
    [[[0, 1], [1, 0], [0, -1], [-1, 0]]]
]

safeArea = 0
result = float('inf')

for i in range(N):
    for j in range(M):
        if 0 < lst[i][j] < 6:
            cctv.append([i, j, lst[i][j]])
        if lst[i][j] == 0:
            safeArea += 1

K = len(cctv)
solve(0, safeArea)
print(result)
