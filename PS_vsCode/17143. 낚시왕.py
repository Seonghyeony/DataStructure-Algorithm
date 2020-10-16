'''
0~n+2 - 상어 있는 칸은 1~n
방향, 속도
이동 마친 후에는 상어가 두마리 이상 있을 수 있음 --> 크기가 가장 큰 상어만 남는다.
'''
## 성공이지만 각 상어의 속력만큼 반복문을 돌려서 상어를 이동시키므로 시간이 많이 소요.
# 반복문을 안쓰는 방법은 밑의 주석 코드에 있음.(너무 복잡함,,,)
from collections import deque

R, C, M = map(int, input().split())
board = [[0 for _ in range(C+2)] for _ in range(R+1)]
sharks = []

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

result = 0

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    # 크기, 이동방향, 속력 순
    board[r][c] = [z, d, s]
    sharks.append([r, c])

# for i in board:
#     print(i)

fishing_y, fishing_x = 0, 0

def move():
    tmp = [[0 for _ in range(C+2)] for _ in range(R+1)]
    for i in range(len(sharks)):
        if sharks[i] == 0:
            continue

        y, x = sharks[i]
        # print(sharks[i])
        size, direct, speed = board[y][x]
        ny, nx = y, x
        for _ in range(speed):
            if 1 <= ny + dy[direct] <= R and 1 <= nx + dx[direct] <= C:
                ny, nx = ny + dy[direct], nx + dx[direct] 
            else:
                if direct == 1 or direct == 2:
                    direct = (direct * 2) % 3
                else:
                    direct = (direct * 2 + 2) % 3 + 2
                ny, nx = ny + dy[direct], nx + dx[direct]
        
        #print(ny, nx)
        if tmp[ny][nx] != 0:
            osize, odirect, ospeed = tmp[ny][nx]
            if osize < size:
                tmp[ny][nx] = [size, direct, speed]
                sharks[i] = 0
            else:
                sharks[i] = 0
        else:
            tmp[ny][nx] = [size, direct, speed]
            sharks[i] = [ny, nx]
    return tmp
    
while fishing_x != C+1:
    # 1. 오른쪽 한칸 이동
    fishing_x += 1
    # 2. 땅과 제일 가까운 상어를 잡고, 상어 제거
    for i in range(1, R+1):
        if board[i][fishing_x]:
            result += board[i][fishing_x][0]
            board[i][fishing_x] = 0
            idx = sharks.index([i, fishing_x])
            sharks[idx] = 0
            break
    # 3. 상어 이동
    board = move()
    # for i in board:
    #     print(i)
    # break

print(result)

'''
# 각 상어의 속력과 방향을 알기 때문에 반복문을 사용하지 않고 조건문으로 한 번에 이동하도록 구현
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dir(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    else: return 3

r, c, m = map(int, input().split())
a = [[0] * c for _ in range(r)]
q = []

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    a[x-1][y-1] = [s, d, z]
    q.append([x-1, y-1])

ans, rx, ry = 0, -1, -1

for col in range(c):
    for i in range(r):
        if a[i][col]:
            ans += a[i][col][2]
            a[i][col] = 0
            rx, ry = i, col
            break

    qlen = len(q)
    temp = [[0] * c for _ in range(r)]
    q2 = []

    for i in range(qlen):
        x, y = q[i]
        if x == rx and y == ry:
            continue
        s, d, z = a[x][y][0], a[x][y][1], a[x][y][2]

        if d == 1 or d == 2:
            nx, ny = x + s * dx[d-1], y
            if not 0 <= nx < r:
                temp_s = s
                if d == 1:
                    s -= x
                    x = 0
                else:
                    s -= r-1-x
                    x = r-1
                d = dir(d)
                f, g = s // (r-1), s % (r-1)
                if f % 2 == 0:
                    if x == 0:
                        nx = g
                    else:
                        nx = r-1-g
                else:
                    if x == 0:
                        nx = r-1-g
                    else:
                        nx = g
                    d = dir(d)
                s = temp_s
        else:
            nx, ny = x, y + s * dy[d-1]
            if not 0 <= ny < c:
                temp_s = s
                if d == 3:
                    s -= c-1-y
                    y = c-1
                else:
                    s -= y
                    y = 0
                d = dir(d)
                f, g = s // (c-1), s % (c-1)
                if f % 2 == 0:
                    if y == 0:
                        ny = g
                    else:
                        ny = c-1-g
                else:
                    if y == 0:
                        ny = c-1-g
                    else:
                        ny = g
                    d = dir(d)
                s = temp_s

        if temp[nx][ny]:
            if z > temp[nx][ny][2]:
                temp[nx][ny] = [s, d, z]
        else:
            temp[nx][ny] = [s, d, z]
            q2.append([nx, ny])
    a = temp
    q = q2

print(ans)
'''