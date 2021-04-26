# 한 칸에는 물고기가 한 마리 존재.
# 물고기 번호 1 ~ 16. 방향은 8가지.
# 상어는 (0, 0) 물고기 먹고, 들어감. 상어 방향은 0,0 물고기와 같다.
# 이후 물고기 이동.
# 번호가 작은 물고기부터 이동.
# 이동 가능 칸: 빈칸, 다른 물고기가 있는 칸.
# 이동 불가능 칸: 상어 있는 칸, 경계 넘는 칸.
# 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전.
# 이동 불가능 하면 continue.
# 서로의 위치를 바꾸는 방식으로 이동.
# 물고기 이동 끝나면 상어 이동.
# 상어는 물고기가 없는 칸으로는 이동 불가. 한 번에 여러 개의 칸을 이동 가능.
# 이동할 수 있는 칸이 없으면, 집으로 감.
### 상어가 먹을 수 잇는 물고기 번호의 합의 최댓값은?! ###

import copy

def find_fish(arr, idx):
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] == idx:
                return (i, j)
    return None


def dfs(lst, sy, sx, value):
    arr = copy.deepcopy(lst)
    # 해당 물고기를 먹는다.
    value += arr[sy][sx][0]
    arr[sy][sx][0] = -1

    # 물고기 이동
    for idx in range(1, 17):
        fish = find_fish(arr, idx)
        if fish is None:
            continue
        y, x = fish
        number, d = arr[y][x]
        for j in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not (ny == y and nx == x):
                    array[y][x][0], array[ny][nx][0] = array[ny][nx][0], array[y][x][0]
                    array[y][x][1], array[ny][nx][1] = array[ny][nx][1], d
                    break
            d = (d + 1) % 8

N = 4
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
lst = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    temp = list(map(int, input().split()))
    c = 0
    for j in range(0, N*2, 2):
        a, b = temp[j], temp[j+1]-1
        lst[r][c] = [a, b]
        c += 1

result = float('-inf')
dfs(lst, 0, 0, 0)
print(result)





'''
import copy

def food(array, y, x):
    positions = []
    d = array[y][x][1]
    for i in range(1, N):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and 1 <= array[ny][nx][0] <= 16:
            positions.append([ny, nx])
        y, x = ny, nx
    return positions


def find_fish(array, index):
    for i in range(N):
        for j in range(N):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_fish(array, now_y, now_x):
    flag = False
    position = []
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        y, x = position[0], position[1]
        d = array[y][x][1]
        for j in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not (ny == now_y and nx == now_x):
                    array[y][x][0], array[ny][nx][0] = array[ny][nx][0], array[y][x][0]
                    array[y][x][1], array[ny][nx][1] = array[ny][nx][1], d
                    break
            d = (d + 1) % 8

def dfs(array, y, x, total):
    global answer
    array = copy.deepcopy(array)

    # 해당 위치의 물고기 먹기
    number = array[y][x][0]
    array[y][x][0] = -1

    # 물고기 이동
    move_fish(array, y, x)

    # 상어 이동할 수 있는 후보 확인
    candidate = food(array, y, x)

    # 해당 먹이 먹는 모든 과정 탐색
    answer = max(answer, total+number)
    for ny, nx in candidate:
        dfs(array, ny, nx, total+number)

N = 4
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
temp = [list(map(int, input().split())) for _ in range(N)]
array = [[None] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        array[i][j] = [temp[i][j*2], temp[i][j*2+1] - 1]

answer = 0
dfs(array, 0, 0, 0)
print(answer)
'''