'''
0~n+2 - 상어 있는 칸은 1~n
방향, 속도
이동 마친 후에는 상어가 두마리 이상 있을 수 있음 --> 크기가 가장 큰 상어만 남는다.
'''
from collections import deque
import heapq

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