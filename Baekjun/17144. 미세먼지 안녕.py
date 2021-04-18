# 공기청정기는 항상 1번 열에 설치, 크기는 2행을 차지.
# 인접한 네 방향으로 미세먼지 확산 A[r][c] // 5
# T 초가 지난 후 방에 남아있는 미세먼지의 양은?

# 42분 소요!

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]

airfurify = []

for i in range(R):
    for j in range(C):
        if lst[i][j] == -1:
            airfurify.append([i, j])
            airfurify.append([i+1, j])
            break

# for i in lst:
#     print(i)
# print()

for _ in range(T):
    spread = []
    # 미세먼지 확산
    for y in range(R):
        for x in range(C):
            if lst[y][x] > 0:
                count = 0
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < R and 0 <= nx < C and lst[ny][nx] != -1:
                        spread.append([ny, nx, lst[y][x] // 5])
                        count += 1
                lst[y][x] = lst[y][x] - (lst[y][x] // 5) * count
    
    for y, x, value in spread:
        lst[y][x] += value

    # ## 공기 청정기 작동
    # # 공기 청정기 윗쪽
    y, x = airfurify[0]
    for i in range(y-1, 0, -1):
        lst[i][0] = lst[i-1][0]
    lst[0][0] = 0

    for j in range(1, C):
        lst[0][j-1] = lst[0][j]
    lst[0][C-1] = 0

    for i in range(1, y+1):
        lst[i-1][C-1] = lst[i][C-1]
    lst[y][C-1] = 0

    for j in range(C-2, 0, -1):
        lst[y][j+1] = lst[y][j]
    lst[y][1] = 0

    y, x = airfurify[1]
    # 공기 청정기 아래쪽
    for i in range(y+2, R):
        lst[i-1][0] = lst[i][0]
    lst[R-1][0] = 0

    for j in range(1, C):
        lst[R-1][j-1] = lst[R-1][j]
    lst[R-1][C-1] = 0

    for i in range(R-2, y-1, -1):
        lst[i+1][C-1] = lst[i][C-1]
    lst[y][C-1] = 0

    for j in range(C-2, 0, -1):
        lst[y][j+1] = lst[y][j]
    lst[y][1] = 0

    # for i in lst:
    #     print(i)
    # print()

result = 0
for i in lst:
    result += sum(i)
print(result+2)
