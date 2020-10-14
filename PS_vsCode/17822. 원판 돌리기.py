# 원판 회전을 위해 deque를 사용하고, 인접한 숫자를 체크하기 위해 bfs를 활용한다.
# 1. 이차원 배열의 y값 범위는 0 < y < len(이차원 배열)
# 2. 이차원 배열의 x값이 양 끝값(0 또는 M)일 경우를 고려해서 코드를 완성해야 한다.

# deque rotate 양수 = 시계방향, 음수 = 반시계방향
from collections import deque
from itertools import chain

n, m, t = map(int, input().split())
maps = [[0 for _ in range(m)]]

# 1. 원판 회전시키기
def deque_rotate(maps, p, k):
    # 배수인 원판만 작업하기
    for idx in range(1, len(maps)): # len(maps) = n
        # 배수인 원판만 작업하기
        if idx % p == 0:
            maps[idx].rotate(k)
    return

def bfs(maps, y, x):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    value = maps[y][x]
    queue.append((y, x))
    visited = set()
    while queue:
        y, x = queue.popleft()
        visited.add((y, x))
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if nx == len(maps[0]):
                nx = 0
            if nx < 0:
                nx = len(maps[0]) - 1
            if 0 < ny < len(maps) and maps[ny][nx] == value and (ny, nx) not in visited:
                queue.append((ny, nx))
                visited.add((ny, nx))
    return visited

# 2. 원판 숫자 연산하기
def deque_calculate(maps):
    is_adj = False  # 인접한 수가 있는지 체크
    for y in range(1, len(maps)):
        for x in range(len(maps[0])):
            current = maps[y][x]
            if current == 0:
                continue
            # 인접하면서 같은 숫자 찾기
            adj = bfs(maps, y, x)
            # 인접하면서 같은 수가 존재하는 경우 = 좌표가 2개 이상
            if len(adj) > 1:
                # 인접한 수가 있으므로 flag True로 변경
                is_adj = True
                for ny, nx in adj:
                    maps[ny][nx] = 0
    
    # 전체 탐색했는데 인접한 수가 없는 경우
    # 모든 수가 전부 0일 경우 avg 계산 불가능
    if not is_adj and [i for i in chain(*maps) if i != 0]:
        avg = sum(chain(*maps)) / len([i for i in chain(*maps) if i != 0])
        for y in range(1, len(maps)):
            for x in range(len(maps[0])):
                if maps[y][x] != 0:
                    if maps[y][x] > avg:
                        maps[y][x] -= 1
                    elif maps[y][x] < avg:
                        maps[y][x] += 1

for _ in range(n):
    arr = deque(map(int, input().split()))
    maps.append(arr)


for _ in range(t):
    p, d, k = map(int, input().split())
    k = k if d == 0 else -k
    deque_rotate(maps, p, k)
    deque_calculate(maps)

print(sum(chain(*maps)))



'''테스트케이스는 전부 맞는데, 반례를 못찾겠다,,,, --> 방향 분석을 제대로 못했다!
from collections import deque

# 숫자는 반시계 방향
n, m, t = map(int, input().split())
# i 번째 판에 적힌 j 번째 수의 위치는 (i, j)로 표현
lst = [[0 for _ in range(m+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    # 번호가 x의 배수인 원판을 d방향으로 k칸 회전. d = 0 시계, d = 1 반시계
    # ex) x = 2 d = 0 k = 1
    x, d, k = map(int, input().split())
    while x <= n:
        queue = deque(lst[x][1:])
        for _ in range(k):
            if d == 0:
                queue.rotate(1)
            if d == 1:
                queue.rotate(-1)
        lst[x] = [0] + list(queue)
        x += x
    
    delete = set()

    for i in range(1, n+1):
        if lst[i][1] and lst[i][1] == lst[i][2]:
            delete.add((i, 1))
            delete.add((i, 2))
        if lst[i][1] and lst[i][1] == lst[i][m]:
            delete.add((i, 1))
            delete.add((i, m))

        if lst[i][m] and lst[i][m] == lst[i][m-1]:
            delete.add((i, m))
            delete.add((i, m-1))

        for j in range(2, m):
            if lst[i][j] and lst[i][j] == lst[i][j-1]:
                delete.add((i, j))
                delete.add((i, j-1))
            if lst[i][j] and lst[i][j] == lst[i][j+1]:
                delete.add((i, j))
                delete.add((i, j+1))

    for j in range(1, m+1):
        if lst[1][j] and lst[1][j] == lst[2][j]:
            delete.add((1, j))
            delete.add((2, j))
        if lst[n][j] and lst[n][j] == lst[n-1][j]:
            delete.add((n, j))
            delete.add((n-1, j))

    for i in range(2, n):
        for j in range(1, m+1):
            if lst[i][j] and lst[i][j] == lst[i-1][j]:
                delete.add((i, j))
                delete.add((i-1, j))
            if lst[i][j] and lst[i][j] == lst[i+1][j]:
                delete.add((i, j))
                delete.add((i+1, j))
    """
    tmp = []

    if len(delete):
        delete = list(delete)
        for i in range(len(delete)):
            y, x = delete[i]
            if lst[y][x] == 0:
                continue
            tmp.append((y, x))
    """
    if len(delete) == 0:
        count = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if lst[i][j]:
                    count += 1

        # 전부 0이 아닐 경우에만
        if count != 0:
            average = sum(map(sum, lst)) / count
            # print(average)

            for i in range(1, n+1):
                for j in range(1, m+1):
                    if lst[i][j]:
                        if lst[i][j] > average:
                            lst[i][j] -= 1
                        elif lst[i][j] < average:
                            lst[i][j] += 1
    else:
        for y, x in delete:
            lst[y][x] = 0


# print("원판 다 돌린 후")
# for i in lst:
#     print(i)
# print("결과")

# 1. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
#    1. 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
#    2. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.

# for i in lst:
#     print(i)

print(sum(map(sum, lst)))
'''