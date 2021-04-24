# A[r][c] 는 얼음의 양을 의미
# 1. 남아있는 얼음 A[r][c]의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

# 55분 클리어!

from collections import deque

def bfs(y, x):
    global visited
    queue = deque([[y, x]])
    ret = 0
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            ret += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 2**N and 0 <= nx < 2**N and lst[ny][nx] != 0 and not visited[ny][nx]:
                    queue.append([ny, nx])
    return ret


def storm(L):
    n = 2**L
    # 2**L x 2**L 크기의 부분격자로 나눈다.
    for y in range(0, 2**N, n):
        for x in range(0, 2**N, n):
            temp = [[0 for _ in range(n)] for _ in range(n)]
            # 모든 부분 격자를 시계 방향으로 90도 회전
            for i in range(n):
                for j in range(n):
                    temp[i][j] = lst[(y+n)-1-j][x+i]
            for i in range(n):
                for j in range(n):
                    lst[y+i][x+j] = temp[i][j]
    # 얼음 줄이기.
    # 줄일 얼음들.
    ices = []
    for y in range(2**N):
        for x in range(2**N):
            if lst[y][x] != 0:
                count = 0
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < 2**N and 0 <= nx < 2**N:
                        if lst[ny][nx] != 0:
                            count += 1
                if count <= 2:
                    ices.append([y, x])
    
    # 얼음 줄이기
    for y, x, in ices:
        if lst[y][x] == 0:
            continue
        lst[y][x] -= 1
    
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(2**N)]
stage = list(map(int, input().split()))

for L in stage:
    storm(L)

# for i in lst:
#     print(i)
# print()

# 남아있는 얼음의 합은?
print(sum(map(sum, lst)))
# 가장 큰 덩어리가 차지하는 칸의 개수는?
result = 0
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if lst[i][j] != 0 and not visited[i][j]:
            temp = bfs(i, j)
            if result < temp:
                result = temp
    
print(result)
