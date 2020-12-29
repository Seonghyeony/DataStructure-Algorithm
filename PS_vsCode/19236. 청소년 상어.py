# 번호: 1 ~ 16
# 빈 칸과 다른 물고기가 있는 칸으로만 이동 가능.
# 방향이 이동할 수 있는 칸을 찾을 때까지 방향 45도 반시계 회전, 이동할 수 없으면 이동 x.
# 서로의 위치를 바꾸는 식으로 이동.
# 상어는 물고기가 없는 칸으로 이동 불가능.
import copy

def food(lst, y, x):
    positions = []
    direct = lst[y][x][1]
    for i in range(1, 4):
        ny, nx = y + dy[direct], x + dx[direct]
        if 0 <= ny < 4 and 0 <= nx < 4 and 1 <= lst[ny][nx][0] <= 16:
            positions.append([ny, nx])
        y, x = ny, nx
    return positions

def find_fish(lst, index):
    for i in range(4):
        for j in range(4):
            if lst[i][j][0] == index:
                return (i, j)
    return None

def move_fish(lst, now_y, now_x):
    position = []
    for i in range(1, 17):
        position = find_fish(lst, i)
        if position is None:
            continue
        y, x = position[0], position[1]
        direct = lst[y][x][1]  # 방향
        for j in range(8):
            ny, nx = y + dy[direct], x + dx[direct]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if not (ny == now_y and nx == now_x):
                    lst[y][x][0], lst[ny][nx][0] = lst[ny][nx][0], lst[y][x][0]
                    lst[y][x][1], lst[ny][nx][1] = lst[ny][nx][1], direct
                    break
            direct = (direct + 1) % 8

def dfs(lst, y, x, total):
    global result
    lst = copy.deepcopy(lst)

    number = lst[y][x][0]
    # 물고기를 먹는다.
    lst[y][x][0] = -1
    # 물고기 이동
    move_fish(lst, y, x)
    # 상어가 먹을 수 있는 물고기 파악
    eat_fish = food(lst, y, x)

    result = max(result, total + number)

    for next_y, next_x in eat_fish:
        dfs(lst, next_y, next_x, total + number) 


lst = [[] for _ in range(4)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        lst[i].append([tmp[j], tmp[j+1] - 1])

result = 0
dfs(lst, 0, 0, 0)
print(result)

'''
import copy

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

def food(array, y, x):  # 상어가 먹을 수 있는 후보 위치 반환.
    positions = []
    direction = array[y][x][1]
    for i in range(1, 4):
        ny, nx = y + dy[direction], x + dx[direction]
        if 0 <= ny < 4 and 0 <= nx < 4 and 1 <= array[ny][nx][0] <= 16:
            positions.append([ny, nx])
        y, x = ny, nx
    return positions

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
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
        dir = array[y][x][1]  # 방향
        for j in range(8):
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if not (ny == now_y and nx == now_x):  # 공간의 경계, 상어 있는 칸 확인
                    # 값 교체
                    array[y][x][0], array[ny][nx][0] = array[ny][nx][0], array[y][x][0]
                    array[y][x][1], array[ny][nx][1] = array[ny][nx][1], dir
                    break
            dir = (dir + 1) % 8

def dfs(array, y, x, total):
    global answer
    array = copy.deepcopy(array)

    # 해당 위치의 물고기 먹기
    number = array[y][x][0]
    array[y][x][0] = -1

    # 물고기 이동
    move_fish(array, y, x)

    # 상어 이동할 수 있는 후보 확인
    result = food(array, y, x)

    # 해당 먹이 먹는 모든 과정 탐색
    answer = max(answer, total + number)
    for next_y, next_x in result:
        dfs(array, next_y, next_x, total + number)


temp = [list(map(int, input().split())) for _ in range(4)]
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]

answer = 0
dfs(array, 0, 0, 0)
print(answer)
'''