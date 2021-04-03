def isPossibleConnecting(index, direct):
    length = len(lst)
    y, x = cores[index]
    if direct == 0:
        for dx in range(x + 1, length):
            if lst[y][dx]:
                return False
    if direct == 1:
        for dx in range(0, x):
            if lst[y][dx]:
                return False
    if direct == 2:
        for dy in range(y + 1, length):
            if lst[dy][x]:
                return False
    if direct == 3:
        for dy in range(0, y):
            if lst[dy][x]:
                return False
    return True

def connecting(index, direct):
    length = len(lst)
    y, x = cores[index]
    cost = 0
    if direct == 0:
        for dx in range(x + 1, length):
            lst[y][dx] = 2
            cost += 1
    if direct == 1:
        for dx in range(0, x):
            lst[y][dx] = 2
            cost += 1
    if direct == 2:
        for dy in range(y + 1, length):
            lst[dy][x] = 2
            cost += 1
    if direct == 3:
        for dy in range(0, y):
            lst[dy][x] = 2
            cost += 1
    return cost

def disconnecting(index, direct):
    length = len(lst)
    y, x = cores[index]
    if direct == 0:
        for dx in range(x + 1, length):
            lst[y][dx] = 0
    if direct == 1:
        for dx in range(0, x):
            lst[y][dx] = 0
    if direct == 2:
        for dy in range(y + 1, length):
            lst[dy][x] = 0
    if direct == 3:
        for dy in range(0, y):
            lst[dy][x] = 0

def isConnected(index):
    length = len(lst)
    y, x = cores[index]
    if y == 0 or x == 0 or y == length - 1 or x == length - 1:
        return True
    return False

def dfs(n, connected, cost):
    global count, result
    if n == len(cores):
        if connected > count:
            count = connected
            result = cost
        elif connected == count:
            result = min(result, cost)
        return
    
    # 이미 연결되어 있으면 연결 체크 후 넘긴다.
    if isConnected(n):
        dfs(n + 1, connected + 1, cost)
    else:
        flag = False
        # 4 방향 체크.
        for i in range(4):
            # 0: 동, 1: 서, 2: 남, 3: 북
            if isPossibleConnecting(n, i):
                flag = True
                connect_cost = connecting(n, i)
                dfs(n + 1, connected + 1, cost + connect_cost)
                disconnecting(n, i)
        # 4방향 연결 불가능 시 그냥 넘긴다.
        if not flag:
            dfs(n + 1, connected, cost)

T = int(input())
lst, cores = [], []
count, result = -1, float('inf')
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if lst[i][j]:
                cores.append([i, j])
    count, result = -1, float('inf')
    dfs(0, 0, 0)
    print('#{} {}'.format(test_case, result))
    
