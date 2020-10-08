from collections import deque

N, K = int(input()), int(input())
lst = [[0] * N for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 0: 빈 칸
# 1: 자신의 몸
# 2: 사과
for _ in range(K):
    y, x = map(int, input().split())
    lst[y-1][x-1] = 2

l = int(input())
rotations = deque()
for _ in range(l):
    t, d = input().split()
    rotations.append([int(t), d])
directions = [[3, 2], [2, 3], [0, 1], [1, 0]]
# 방향 - 0: 동 1: 서 2: 남 3: 북
direct = 0
# 몸 길이
length = 1
time = 0
lst[0][0] = 1
body = deque([(0, 0)])
finish = 0
y, x = 0, 0

def move(y, x, direct):
    global length
    global finish

    ny, nx = y + dy[direct], x + dx[direct]
    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        finish = 1
        return None, None
    
    if lst[ny][nx] == 2:
        lst[ny][nx] = 1
        body.append((ny, nx))
        length += 1
    elif lst[ny][nx] == 1:
        finish = 1
        return None, None
    else:
        lst[ny][nx] = 1
        body.append((ny, nx))
        ry, rx = body.popleft()
        lst[ry][rx] = 0

    return ny, nx


while True:
    if len(rotations) != 0 and time == rotations[0][0]:
        t, d = rotations.popleft()
        tmp = -1
        if d == 'L':
            tmp = 0
        else:
            tmp = 1
        direct = directions[direct][tmp]
    
    y, x = move(y, x, direct)
    time += 1

    # for i in lst:
    #     print(i)
    # print()

    if finish:
        break
    
print(time)