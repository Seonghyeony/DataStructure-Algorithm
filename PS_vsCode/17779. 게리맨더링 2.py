N = int(input())
board = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

total = 0
res = float('inf')

# 기준점 x, y, d1, d2 정하고 그 결과값 찾기
total = sum(map(sum, board)) # 전체 합

def solve(x, y, d1, d2):
    # 경계선 정하기
    tmp = [[0] * (N + 1) for _ in range(N+1)]
    tmp[x][y] = 5

    for i in range(1, d1 + 1):
        tmp[x+i][y-i] = 5  # 1
        tmp[x+d2+i][y+d2-i] = 5  # 4

    for i in range(1, d2 + 1):
        tmp[x+i][y+i] = 5  # 2
        tmp[x+d1+i][y-d1+i] = 5  # 3

    # 선거구 합 구하기
    #1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    one = 0
    for r in range(1, x + d1):
        for c in range(1, y+1):
            if tmp[r][c] == 5:
                break
            one += board[r][c]

    #2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    two = 0
    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if tmp[r][c] == 5:
                break
            two += board[r][c]

    #3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    three = 0
    for r in range(x + d1, N + 1):
        for c in range(1, y-d1+d2):
            if tmp[r][c] == 5:
                break
            three += board[r][c]

    #4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    four = 0
    for r in range(x+d2+1, N + 1):
        for c in range(N, y-d1+d2-1, -1):
            if tmp[r][c] == 5:
                break
            four += board[r][c]

    five = total - one - two - three - four
    maxv = max(one, two, three, four, five)
    minv = min(one, two, three, four, five)

    return maxv-minv


#  d1, d2 ≥ 1, 1 ≤ x < x + d1 + d2 ≤ N, 1 ≤ y - d1 < y < y + d2 ≤ N
#  x + d1 + d2 ≤ N, 1 ≤ y - d1 < y < y + d2 ≤ N
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 > N:
                    continue
                if 1 > y - d1:
                    continue
                if y + d2 > N:
                    continue
                res = min(res, solve(x, y, d1, d2))

print(res)

'''
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

def count(area):
    a, b, c, d, e = 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            tmp = area[i+1][j+1]
            if tmp == 1:
                a += lst[i][j]
            elif tmp == 2:
                b += lst[i][j]
            elif tmp == 3:
                c += lst[i][j]
            elif tmp == 4:
                d += lst[i][j]
            else:
                e += lst[i][j]

    max_pop = max(a, b, c, d, e)
    min_pop = min(a, b, c, d, e)
    return max_pop, min_pop


def outofrange(x, y):
    if x < 1 or x >= N+1 or y < 1 or y >= N+1:
        return False
    return True


def divide(area, x, y, d1, d2):
    # 경계선과 경계선 안은 5번 선거구.
    for i in range(d1+1):
        if not outofrange(x+i, y-i):
            continue
        area[x+i][y-i] = 5
    for i in range(d2+1):
        if not outofrange(x+i, y+i):
            continue
        area[x+i][y+i] = 5
    for i in range(d1+1):
        if not outofrange(x+d2+i, y+d2-i):
            continue
        area[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        if not outofrange(x+d1+i, y-d1+i):
            continue
        area[x+d1+i][y-d1+i] = 5

    for i in range(1, N+1):
        flag = 0
        start = -1
        end = -1
        for j in range(1, N+1):
            if not flag and area[i][j] == 5:
                start = j
                flag = 1
            elif flag and area[i][j] == 5:
                end = j
                break
        if start == -1:
            continue
        if end == -1:
            continue
        for k in range(start, end+1):
            area[i][k] = 5 
    
    # 1번.
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if area[i][j] == 0:
                area[i][j] = 1

    # 2번.
    for i in range(1, x+d2+1):
        for j in range(y+1, N+1):
            if area[i][j] == 0:
                area[i][j] = 2

    # 3번.
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2):
            if area[i][j] == 0:
                area[i][j] = 3

    # 4번.
    for i in range(x+d2+1, N+1):
        for j in range(y-d1+d2, N+1):
            if area[i][j] == 0:
                area[i][j] = 4

    return area

def check(x, y, d1, d2):
    if d1 < 1 or d2 < 1:
        return False
    if x < 1 or x >= (x + d1 + d2) or (x + d1 + d2) > N:
        return False
    if y - d1 < 1 or y <= y - d1 or y + d2 > N:
        return False

    return True

def calc(tmp):
    global result
    x, y, d1, d2 = tmp

    area = [[0 for _ in range(N+1)] for _ in range(N+1)]
    area = divide(area, x, y, d1, d2)

    max_population, min_poppulation = count(area)
    result = min(result, max_population - min_poppulation)

def dfs(x, y, d1, d2):
    if check(x, y, d1, d2):
        array.add((x, y, d1, d2))
    else:
        return

    dfs(x+1, y, d1, d2)
    dfs(x, y+1, d1, d2)
    dfs(x, y, d1+1, d2)
    dfs(x, y, d1, d2+1)

result = float('inf')
array = set()
x, y, d1, d2 = 1, 2, 1, 1
dfs(x, y, d1, d2)

for i in array:
    calc(i)

print(result)
'''