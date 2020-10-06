def spread(dusts):
    for y, x, value in dusts:
        mount = value // 5
        count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if lst[ny][nx] == -1:
                continue
            lst[ny][nx] += mount
            count += 1
        if count:
            lst[y][x] -= mount * count

def purifier(air):
    for i in range(2):
        if i == 0:
            y, x = air[i]
            for i in range(y-1, -1, -1):
                if i == y - 1:
                    lst[i][0] = 0
                else:
                    lst[i+1][0] = lst[i][0]
                    lst[i][0] = 0
            
            for i in range(1, C):
                lst[0][i-1] = lst[0][i]
                lst[0][i] = 0

            for i in range(1, y+1):
                lst[i-1][C-1] = lst[i][C-1]
                lst[i][C-1] = 0
            
            for i in range(C-2, 0, -1):
                lst[y][i+1] = lst[y][i]
                lst[y][i] = 0
        else:
            y, x = air[i]
            for i in range(y+1, R):
                if lst[i-1][0] == -1:
                    lst[i][0] = 0
                else:
                    lst[i-1][0] = lst[i][0]
                    lst[i][0] = 0
            
            for i in range(1, C):
                lst[R-1][i-1] = lst[R-1][i]
                lst[R-1][i] = 0

            for i in range(R-2, y-1, -1):
                lst[i+1][C-1] = lst[i][C-1]
                lst[i][C-1] = 0
            
            for i in range(C-2, 0, -1):
                lst[y][i+1] = lst[y][i]
                lst[y][i] = 0

R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

air = []
for _ in range(T):
    dusts = []
    for i in range(R):
        for j in range(C):
            if lst[i][j] > 0:
                dusts.append([i, j, lst[i][j]])
            elif lst[i][j] == -1:
                air.append([i, j])
    spread(dusts)
    purifier(air)
result = 0
for i in range(R):
    for j in range(C):
        if lst[i][j] == -1 or lst[i][j] == 0:
            continue
        result += lst[i][j]

print(result)