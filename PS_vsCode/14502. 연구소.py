import copy
from collections import deque

def dfs2(lst):
    ret = 0
    queue = deque()
    visited2 = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if lst[y][x] == 2:
                queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if lst[ny][nx] == 0:
                lst[ny][nx] = 2
                queue.append((ny, nx))

    for i in lst:
        ret += i.count(0)
    return ret

def dfs(lst, wall):
    global result
    if wall == 0:
        array = copy.deepcopy(lst)
        result = max(result, dfs2(array))
        return
    
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                dfs(lst, wall - 1)
                lst[i][j] = 0


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = [[False for _ in range(M)] for _ in range(N)]

result = 0
dfs(lst, 3)
print(result)