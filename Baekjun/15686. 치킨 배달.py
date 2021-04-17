# 빈칸 0, 집 1, 치킨 집 2
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리.
# 치킨 거리: abs(r1 - r2) + abs(c1 - c2)

# 가장 수익을 많이 낼 수 있는 치킨 집의 개수.
# 치킨 집 중에서 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값은?

from itertools import combinations

def distance(candidate):
    global result
    ret = 0
    for i in range(len(houses)):
        y, x = houses[i]
        value = float('inf')
        for j in range(len(candidate)):
            dy, dx = candidate[j]
            temp = abs(y - dy) + abs(x - dx)
            if value > temp:
                value = temp
        ret += value
        if ret > result:
            break
    return ret

def solve(candidate):
    global result
    ret = distance(candidate)
    if result > ret:
        result = ret
    return

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []

result = float('inf')

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            chickens.append([i, j])
        if lst[i][j] == 1:
            houses.append([i, j])

chickens = list(combinations(chickens, M))

for i in range(len(chickens)):
    solve(chickens[i])
print(result)


