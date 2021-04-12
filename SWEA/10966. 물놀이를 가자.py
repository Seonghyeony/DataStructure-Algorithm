from collections import deque

'''
def bfs(lst, r, c):
    global result
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque([[r, c, 0]])
    while queue:
        y, x, count = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and lst[ny][nx] == 'L':
                    if result[ny][nx] > count + 1:
                        result[ny][nx] = count + 1
                        queue.append([ny, nx, count + 1])


dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    result = [[float('inf') for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'W':
                bfs(lst, i, j)
    count = 0
    for i in range(N):
        for j in range(M):
            if result[i][j] != float('inf'):
                count += result[i][j]
    print('#{} {}'.format(test_case, count))
'''

def bfs():
    ''' W 인 것부터 다 체크를 하므로 min 비교가 필요없음. '''
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    lst = [list(input()) for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    
    bfs()
    result = 0
    for i in range(n):
        for j in range(m):
            result += visited[i][j]
    print('#{} {}'.format(test_case, result))

