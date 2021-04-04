from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
queue = deque()
lst = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    lst[r-1][c-1].append([m, s, d])
    queue.append([r-1, c-1])

for _ in range(K):
    temp = []
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for _ in range(len(lst[y][x])):
            m, s, d = lst[y][x].popleft()
            ny = (s * dy[d] + y) % N
            nx = (s * dx[d] + x) % N
            queue.append([ny, nx])
            temp.append([ny, nx, m, s, d])
    
    for y, x, m, s, d in temp:
        lst[y][x].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(lst[i][j]) > 1:
                nm, ns, odd, even, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(lst[i][j]):
                    nm += m
                    ns += s
                    if idx == 0:
                        if d % 2 == 0:
                            even = 1
                        else:
                            odd = 1
                    else:
                        if even == 1 and d % 2 == 1:
                            flag = 1
                        elif odd == 1 and d % 2 == 0:
                            flag = 1

                nm //= 5
                ns //= len(lst[i][j])
                lst[i][j] = deque()
                if nm != 0:
                    for idx in range(4):
                        nd = 2 * idx if flag == 0 else 2 * idx + 1
                        lst[i][j].append([nm, ns, nd])

result = 0
for i in range(N):
    for j in range(N):
        if lst[i][j]:
            for m, s, d in lst[i][j]:
                result += m
print(result)



'''
import copy
import math

def afterMoveIndex(y, x, s, d):
    dy, dx = direction[d]
    ny, nx = dy * s, dx * s
    ret_y, ret_x = 0, 0
    if y + ny < 0:
        ret_y = abs(y + ny) % N
    else:
        ret_y = (y + ny) % N
    if x + nx < 0:
        ret_x = abs(x + nx) % N
    else:
        ret_x = (x + nx) % N
    return ret_y, ret_x

def move():
    global fireball
    queue = []
    while fireball:
        y, x, m, s, d = fireball.pop(0)
        ny, nx = afterMoveIndex(y, x, s, d)
        queue.append([ny, nx, m, s, d])
    return queue

def collisionMove():
    global fireball
    array = [[[] for _ in range(N)] for _ in range(N)]
    queue = copy.deepcopy(fireball)
    temp = []
    ret = []
    while queue:
        y, x, m, s, d = queue.pop(0)
        if len(array[y][x]) and [y, x] not in temp:
            temp.append([y, x])
        array[y][x].append([m, s, d])

    while temp:
        y, x = temp.pop(0)
        nm, ns = 0, 0
        a, b, count = 0, 0, 0
        for dm, ds, dd in array[y][x]:
            nm += dm
            ns += ds
            if dd % 2 == 0:
                b += 1
            else:
                a += 1
            count += 1

        nm, ns = math.floor(nm / 5), math.floor(ns / count)
        # 질량이 0이면 사라짐.
        if nm == 0:
            array[y][x] = []
            continue
        if a == 0 or b == 0:
            # 0, 2, 4, 6 방향
            for i in range(0, 7, 2):
                # ny, nx = afterMoveIndex(y, x, ns, i)
                ret.append([y, x, nm, ns, i])
        else:
            # 1, 3, 5, 7
            for i in range(1, 8, 2):
                # ny, nx = afterMoveIndex(y, x, ns, i)
                ret.append([y, x, nm, ns, i])
    for i in range(N):
        for j in range(N):
            if len(array[i][j]) == 1:
                lst = array[i][j]
                ret.append([i, j, lst[0][0], lst[0][1], lst[0][2]])
    return ret

def isCollision():
    global fireball
    array = [[[] for _ in range(N)] for _ in range(N)]
    queue = copy.deepcopy(fireball)
    while queue:
        y, x, m, s, d = queue.pop(0)
        if len(array[y][x]):
            return True
        array[y][x].append([m, s, d])
    return False

def result():
    global fireball
    ret = 0
    queue = copy.deepcopy(fireball)
    # print("queue:", queue)
    for i in range(len(queue)):
        ret += queue[i][2]
    print(ret)

def dfs(n):
    global fireball
    if n == K:
        result()
        return
    if len(fireball) == 0:
        print(0)
        return
    
    fireball = move()
    if isCollision():
        fireball = collisionMove()
        dfs(n + 1)
    else:
        dfs(n + 1) 

N, M, K = map(int, input().split())
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
fireball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])
dfs(0)
'''