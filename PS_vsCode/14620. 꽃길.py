N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

ans  = 10000

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

def ck(lst):    # a, b, c
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N

        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return 10000
        
        for w in range(5):
            flow.append((x + dx[w], y + dy[w]))
            ret += G[x + dx[w]][y + dy[w]]

    if len(set(flow)) != 15:
        return 10000

    return ret


for i in range(N * N):
    for j in range(i + 1, N * N):
        for k in range(j + 1, N * N):
            ans = min(ans, ck([i, j, k]))

print(ans)

"""
----- DFS 방식 -----

def cal_cost(candidate):
    cost = 0
    for date in candidate:
        y, x = date
        cost += lst[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cost += lst[ny][nx]
    return cost

def check(candidate, y, x):
    for data in candidate:
        temp = [data]
        for i in range(4):
            nx = data[1] + dx[i]
            ny = data[0] + dy[i]
            temp.append((ny, nx))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (ny, nx) in temp:
                return False
    return True

def dfs(N, candidate):
    global result
    if len(candidate) == 3:
        result = min(result, cal_cost(candidate))
        return
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if check(candidate, i, j):
                candidate.append((i, j))
                dfs(N, candidate)
                candidate.pop()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 3001
dfs(N, [])

print(result)
"""