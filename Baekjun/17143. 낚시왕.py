# 칸에는 상어가 최대 한마리, 상어는 크기와 속도를 가짐.
# 이동을 마친 후에는 한 칸에 상어가 두마리 이상 있을 수 있다.
# 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
# 낚시왕이 잡은 상어 크기의 합은?

def move():
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(len(sharks)):
        if sharks[i] == 0:
            continue
        y, x = sharks[i]
        z, s, d = lst[y][x]
        ny, nx = y, x
        for _ in range(s):
            if 0 <= ny + dy[d] <= R-1 and 0 <= nx + dx[d] <= C-1:
                ny, nx = ny + dy[d], nx + dx[d]
            else:
                if d == 1 or d == 2:
                    d = (d * 2) % 3
                else:
                    d = (d * 2 + 2) % 3 + 2
                ny, nx = ny + dy[d], nx + dx[d]

        if tmp[ny][nx] != 0:
            oz, os, od = tmp[ny][nx]
            if oz < z:
                tmp[ny][nx] = [z, s, d]
                sharks[i] = 0
            else:
                sharks[i] = 0
        else:
            tmp[ny][nx] = [z, s, d]
            sharks[i] = [ny, nx]
    return tmp


R, C, M = map(int, input().split())
lst = [[0 for _ in range(C)] for _ in range(R)]
sharks = []

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

result = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r-1, c-1, d
    lst[r][c] = [z, s, d]
    sharks.append([r, c])

fisher = -1
for _ in range(C):
    fisher += 1
    for i in range(R):
        if lst[i][fisher]:
            result += lst[i][fisher][0]
            lst[i][fisher] = 0
            idx = sharks.index([i, fisher])
            sharks[idx] = 0
            break
    lst = move()

print(result)

'''
def changeDirection(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2
    return None

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
R, C, M = map(int, input().split())
lst = [[[] for _ in range(C)] for _ in range(R)]
fisher = -1
for _ in range(M):
    # s 속력, d 방향, z 크기
    r, c, s, d, z = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    lst[r][c].append([s, d, z])

result = 0

for _ in range(C):
    # 낚시꾼 이동
    fisher += 1
    # 상어 잡는다.
    for y in range(R):
        if len(lst[y][fisher]):
            s, d, z = lst[y][fisher].pop(0)
            result += z
            break
    # 상어 이동
    sharks = []
    for i in range(R):
        for j in range(C):
            if len(lst[i][j]):
                s, d, z = lst[i][j].pop(0)
                y, x = i, j
                for _ in range(s):
                    if 0 <= y + dy[d] <= R-1 and 0 <= x + dx[d] <= C-1:
                        ny, nx = y + dy[d], x + dx[d]
                    else:
                        d = changeDirection(d)
                        ny, nx = y + dy[d], x + dx[d]
                    y, x = ny, nx
                sharks.append([y, x, s, d, z])

    for y, x, s, d, z in sharks:
        if len(lst[y][x]) == 0:
            lst[y][x].append([s, d, z])
        else:
            if lst[y][x][0][2] < z:
                lst[y][x] = [[s, d, z]]
    
    if fisher == C-1:
        break

print(result)
'''