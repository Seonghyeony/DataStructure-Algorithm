# 바이러스 활성 비활성
# M개를 활성 상태로 변경
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
# 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간은?!

# 30분 클리어!

from itertools import combinations
from collections import deque

def bfs(activate, count):
    global result
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    time, flag = 0, False
    for r, c in activate:
        queue.append([r, c, 0])
    while queue:
        y, x, second = queue.popleft()
        if not visited[y][x] and lst[y][x] != 1:
            if lst[y][x] == 0:
                count -= 1
                if second > time:
                    time = second
            if result < time:
                flag = True
                break
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] != 1 and not visited[ny][nx]:
                    queue.append([ny, nx, second + 1])
    if flag:
        return

    if count != 0:
        return
    else:
        if result > time:
            result = time

    return

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

viruses = []
result, count = float('inf'), 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            viruses.append([i, j])
        if lst[i][j] == 0:
            count += 1

if count == 0:
    print(0)
    exit(0)

viruses = combinations(viruses, M)

for activate in viruses:
    bfs(activate, count)

if result == float('inf'):
    print(-1)
else:
    print(result)


