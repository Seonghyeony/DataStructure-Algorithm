dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
lst = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    lst[r-1][c-1] = [[m, s, d]]

def find_fireball():
    ret = []
    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0:
                ret.append([i, j])
    return ret

def find_twoFireball(arr):
    ret = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and len(arr[i][j]) >= 2:
                ret.append([i, j])
    return ret

def move():
    temp = [[0 for _ in range(N)] for _ in range(N)]
    fireballs = find_fireball()
    # 파이어볼 이동
    if len(fireballs) == 0:
        return lst
    for y, x in fireballs:
        for m, s, d in lst[y][x]:
            ny, nx = (y + (dy[d] * s)) % N, (x + (dx[d] * s)) % N
            if temp[ny][nx] == 0:
                temp[ny][nx] = [[m, s, d]]
            else:
                temp[ny][nx].append([m, s, d])

    # 2개 이상의 파이어볼이 있는 칸을 리턴
    twoFireball = find_twoFireball(temp)
    if len(twoFireball) == 0:
        return temp
    for y, x in twoFireball:
        total_m, total_s, count = 0, 0, 0
        odd, even = 0, 0
        for m, s, d in temp[y][x]:
            total_m += m
            total_s += s
            count += 1
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
        # 흩어진다.
        nm, ns = total_m // 5, total_s // count
        if nm == 0:
            temp[y][x] = 0
        else:
            temp[y][x] = []
            if odd == 0 or even == 0:
                for nd in range(0, 7, 2):
                    temp[y][x].append([nm, ns, nd])
            else:
                for nd in range(1, 8, 2):
                    temp[y][x].append([nm, ns, nd])
    return temp


for _ in range(K):
    # 모든 파이어볼 이동.
    lst = move()

result = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] != 0:
            for m, s, d in lst[i][j]:
                result += m

print(result)

    
