from itertools import combinations

def distance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            house.append([i, j])
        elif lst[i][j] == 2:
            chicken.append([i, j])

combi_chicken = []
for i in combinations(chicken, M):
    combi_chicken.append(i)

for i in range(len(combi_chicken)):
    ret = 0
    for hy, hx in house:
        tmp = float('inf')
        for num in range(M):
            cy, cx = combi_chicken[i][num]
            tmp = min(tmp, distance(hy, hx, cy, cx))
        ret += tmp
    result = min(result, ret)

print(result)
