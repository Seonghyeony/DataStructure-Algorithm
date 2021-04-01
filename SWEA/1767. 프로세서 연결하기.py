from collections import deque

test_case = int(input())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def isEdge(y, x):
    if y == 0 or x == 0 or y == N - 1 or x == N - 1:
        return True
    return False

def minLength(y, x):
    ret = float('inf')
    # 동
    flag = False
    for dx in range(x-1, -1, -1):
        ny, nx = y, x + dx
        if (ny, nx) in cores:
            flag = True
            break
    if not flag:
        if x < ret:
            ret = x
    # 서
    flag = False
    for dx in range(x+1, N):
        ny, nx = y, x + dx
        if (ny, nx) in cores:
            flag = True
            break
    if not flag:
        if N - 1 - x < ret:
            ret = x - 1 - x
    # 남
    flag = False
    for dy in range(y+1, N):
        ny, nx = y + dy, x
        if (ny, nx) in cores:
            flag = True
            break
    if not flag:
        if N - 1 - y < ret:
            ret = N - 1 - y
    # 북
    flag = False
    for dy in range(y-1, -1, -1):
        ny, nx = y + dy, x
        if (ny, nx) in cores:
            flag = True
            break
    if not flag:
        if y < ret:
            ret = y
    
    if ret == float('inf'):
        return 0
    else:
        return ret

for T in range(1, test_case + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cores = [(i, j) for i in range(N) for j in range(N) if lst[i][j] == 1]
    result = 0
    for (y, x) in cores:
        if isEdge(y, x):
            continue
        result += minLength(y, x)
    print("#{} {}".format(T, result))
    
