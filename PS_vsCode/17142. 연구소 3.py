import copy
from collections import deque

N, M = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
board = []
viruses = []
queue = deque()
K = 0

def bfs(dist):
    global result
    infect, times = 0, 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] != 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
                    if board[ny][nx] == 0:
                        infect += 1
                        times = dist[ny][nx]
    
    if infect == K:
        result = min(result, times)

def dfs(idx, count):
    if count == M:
        choice = copy.deepcopy(ck)
        dist = [[-1 for _ in range(N)] for _ in range(N)]
        for i in range(V):
            if choice[i]:
                y, x = viruses[i]
                queue.append((y, x))
                dist[y][x] = 0
        bfs(dist)
        return
    
    for i in range(idx, V):
        if not ck[i]:
            ck[i] = True
            dfs(i+1, count+1)
            ck[i] = False

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            viruses.append([i, j])
        elif tmp[j] == 0:
            K += 1
    board.append(tmp)

result = float('inf')
V = len(viruses)
ck = [False] * V
dfs(0, 0)
print(result if result != float('inf') else -1)



'''
from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
select = [False] * 10
q, v, k = deque(), [], 0

def bfs(dist):
    global ans
    infect, times = 0, 0
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if a[ny][nx] != 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
                if a[ny][nx] == 0:
                    infect += 1
                    times = dist[ny][nx]

    for i in dist:
        print(i)
    print()
    if infect == k:
        ans = min(ans, times)


def solve(idx, cnt, d):
    if cnt == m:
        dist = [[-1] * n for _ in range(n)]
        for i in range(d):
            if select[i]:
                y, x = v[i]
                q.append((y, x))
                dist[y][x] = 0
        bfs(dist)
        return
    
    for i in range(idx, d):
        if not select[i]:
            select[i] = True
            solve(i+1, cnt+1, d)
            select[i] = False


for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            v.append((i, j))
        if a[i][j] == 0:
            k += 1

ans = 10**9
solve(0, 0, len(v))
print(ans if ans != 10**9 else -1)
'''
'''
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
'''