'''
from collections import deque

def rotate(a):
    length = len(a)
    result = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            result[j][length-i-1] = a[i][j]
    return result

def divide(n, l, y, x):
    if n == l:
        temp = []
        for i in range(y, y+n):
            temp.append(lst[i][x:x+n])
        temp = rotate(temp)
        p, q = 0, 0
        for i in range(y, y+n):
            q = 0
            for j in range(x, x+n):
                lst[i][j] = temp[p][q]
                q += 1
            p += 1
        return
    divide(n // 2, l, y, x)
    divide(n // 2, l, y, x + (n // 2))
    divide(n // 2, l, y + (n // 2), x)
    divide(n // 2, l, y + (n // 2), x + (n // 2))

def melting(n):
    melt = []
    for y in range(n):
        for x in range(n):
            count = 0
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if lst[ny][nx]:
                        count += 1
            if count <= 2:
                melt.append([y, x])

    for y, x in melt:
        if lst[y][x]:
            lst[y][x] -= 1

def bfs(n, r, c):
    global result2
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([r, c])
    ret = 0
    while queue:
        y, x = queue.popleft()
        if not visited[y][x] and lst[y][x]:
            visited[y][x] = True
            ret += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and lst[ny][nx]:
                    queue.append([ny, nx])
    result2 = max(result2, ret)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(2**N)]
qlist = list(map(int, input().split()))

for L in qlist:
    divide(2**N, 2**L, 0, 0)
    melting(2**N)

# for i in lst:
#     print(i)
# print()

result1 = 0
result2 = 0
for i in range(2**N):
    for j in range(2**N):
        if lst[i][j]:
            result1 += lst[i][j]
            bfs(2**N, i, j)
print(result1)
print(result2)
'''

import sys
sys.setrecursionlimit(10**5)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, q = map(int, input().split())
n = 2**n
ice = [list(map(int, input().split())) for _ in range(n)]

for L in list(map(int, input().split())):
    # 회전
    k = 2**L
    for y in range(0, n, k):
        for x in range(0, n, k):
            tmp = [ice[i][x:x+k] for i in range(y, y+k)]
            for i in range(k):
                for j in range(k):
                    ice[y + j][x + k - 1 - i] = tmp[i][j]
    
    # 인접한 얼음 카운팅
    cnt = [[0] * n for i in range(n)]
    for y in range(n):
        for x in range(n):
            for d in dir:
                ny, nx = y + d[0], x + d[1]
                if 0 <= ny < n and 0 <= nx < n and ice[ny][nx]:
                    cnt[y][x] += 1
    
    # 얼음 제거
    for y in range(n):
        for x in range(n):
            if ice[y][x] > 0 and cnt[y][x] < 3:
                ice[y][x] -= 1
    
# 남아있는 얼음의 합
print(sum(sum(i) for i in ice))

# (y, x)가 속한 덩어리의 크기
def dfs(y, x):
    ret = 1
    ice[y][x] = 0
    for d in dir:
        ny, nx = y + d[0], x + d[1]
        if 0 <= ny < n and 0 <= nx < n and ice[ny][nx]:
            ret += dfs(ny, nx)
    return ret

# 제일 큰 덩어리
ans = 0
for y in range(n):
    for x in range(n):
        if ice[y][x] > 0:
            ans = max(ans, dfs(y, x))

print(ans)