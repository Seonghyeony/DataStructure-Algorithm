import copy
from collections import deque

def bfs(board):
    global result, area
    flag = True
    visited = [[False for _ in range(M)] for _ in range(N)]
    ret = area - 3
    queue = copy.deepcopy(viruses)
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            if board[y][x] == '0':
                ret -= 1
            if ret < result:
                flag = False
                break
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board[ny][nx] != '1':
                    queue.append([ny, nx])
    if flag:
        result = max(result, ret)

def dfs(n):
    if n == 3:
        temp = copy.deepcopy(lst)
        bfs(temp)
        return
    
    for i in range(N):
        for j in range(M):
            if lst[i][j] == '0':
                lst[i][j] = '1'
                dfs(n + 1)
                lst[i][j] = '0'

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]

N, M = map(int, input().split())
lst = [list(map(str, input().split())) for _ in range(N)]
viruses = deque()
result = 0
area = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == '2':
            viruses.append([i, j])
        if lst[i][j] == '0':
            area += 1
dfs(0)
print(result)