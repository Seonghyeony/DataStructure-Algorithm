# 33분 클리어!

from collections import deque

def move(arr):
    total = 0
    count = 0
    for y, x in countries:
        total += lst[y][x]
        count += 1
    people = total // count
    for y, x in countries:
        lst[y][x] = people

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    country = []
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            country.append([y, x])
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if L <= abs(lst[y][x] - lst[ny][nx]) <= R:
                        queue.append([ny, nx])
    return country

N, L, R = map(int, input().split())
dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
result = 0

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    united = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                united.append(bfs(i, j))

    flag = False
    for countries in united:
        if len(countries) > 1:
            move(countries)
            flag = True
    
    if flag:
        result += 1
        continue
    break

print(result)

