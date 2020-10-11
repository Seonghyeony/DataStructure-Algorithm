import copy
from itertools import combinations
from collections import deque


def bfs(lst, virus):
    lst = copy.deepcopy(lst)
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = virus
    for y, x in queue:
        lst[y][x] = 0

    time = 1

    notCount = 0
    while queue:
        tmp = []
        for y, x in queue:
            if not visited[y][x]:
                visited[y][x] = True
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]

                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if lst[ny][nx] == '.':
                            lst[ny][nx] = time
                            tmp.append([ny, nx])
                            notCount = 1
                        elif lst[ny][nx] == '*':
                            lst[ny][nx] = 0
                            tmp.append([ny, nx])
                            notCount = 1

        time += 1
        queue = tmp

    if not notCount:
        return 0

    ret = 0
    for i in lst:
        if i.count('.'):
            return None
        for num in i:
            if num == '-' or num == '*':
                continue
            ret = max(ret, num)
    return ret


N, M = map(int, input().split())
lst = [['.' for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
viruses = []

for i in range(N):
    array = list(map(int, input().split()))
    for j in range(N):
        if array[j] == 2:
            lst[i][j] = '*'
            viruses.append([i, j])
        elif array[j] == 1:
            lst[i][j] = '-'

viruses = list(combinations(viruses, M))

result = float('inf')
none_count = 0

for virus in viruses:
    flag = bfs(lst, list(virus))
    if flag is None:
        none_count += 1
        continue
    result = min(result, flag)

if none_count == len(viruses):
    result = -1

print(result)
