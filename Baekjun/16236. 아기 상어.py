# 물고기 M 마리, 아기 상어 1마리
# 한칸에 물고기 최대 1마리
# 초기 상어 크기: 2
# 자신보다 작은 물고기만 먹을 수 있고 자신의 크기보다 큰 물고기가 있는 칸으로 지나갈 수 없다.
# 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가!

# 42분 클리어!

from collections import deque

def bfs(y, x):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([y, x, 0])
    ret = []
    min_distance = float('inf')
    while queue:
        y, x, current_distance = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            if current_distance > 0:
                if current_distance <= min_distance and 0 < lst[y][x] < babySharkSize:
                    min_distance = current_distance
                    ret.append([current_distance, y, x])
                    continue
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if lst[ny][nx] <= babySharkSize:
                        queue.append([ny, nx, current_distance + 1])
    return ret

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
babySharkSize = 2
r, c = 0, 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            r, c = i, j
            break

result = 0
eat = 0
while True:
    eatable = bfs(r, c)
    if len(eatable) == 0:
        break

    eatable.sort()
    distance, y, x = eatable[0]
    lst[r][c], lst[y][x] = 0, 9
    r, c = y, x
    eat += 1
    result += distance

    if babySharkSize == eat:
        eat = 0
        babySharkSize += 1

print(result)