# 1 이 제일 강하다.
# 처음에는 자신의 위치에 냄새 뿌림, 1초마다 상하좌우로 이동. ** 냄새는 상어가 k번 이동하고 나면 사라짐
# 상어 이동 방향: 인접한 칸 중 아무 냄새가 없는 칸의 방향, * 없으면 자신의 냄새가 있는 칸의 방향.
# --> 가능한 칸이 여러개일 때.
# 상어 맨 처음에 방향은 입력 - 그 후에는 이동한 방향과 같음
# 이동 후 한 칸에 여러 마리의 상어가 있으면, 가장 작은 번호 빼고 다 격자 밖으로 쫓겨남(삭제).

''' 문제: 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는가? '''

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

a, shark = [], [[] for _ in range(m)]
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j]:
            shark[a[i][j]-1].extend([i, j])
            a[i][j] = [a[i][j], k]

d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])

dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = dir[i][d-1][j]
                nx, ny = x + dx[ndir], y + dy[ndir]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == 0:
                        flag = 1
                        break
            
            if flag == 0:
                for j in range(4):
                    ndir = dir[i][d-1][j]
                    nx, ny = x + dx[ndir], y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny][0] == i + 1:
                            break
            
            # check[nx][ny]에 이미 값이 있고 i + 1 보다 작다면 현재 상어를 없앤다.
            # 반대의 경우에는 이미 자리잡고 있던 상어를 없앤다.
            if check[nx][ny]:
                if check[nx][ny] < i + 1:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i + 1
                shark[i] = [nx, ny, ndir]

    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[i][j][1] -= 1
                if a[i][j][1] == 0:
                    a[i][j] = 0
    
    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            a[x][y] = [i+1, k]
    
    if shark.count(0) == m-1:
        print(ans)
        break





# for i in a:
#     print(i)
# print()
# for i in shark:
#     print(i)
# print()
# for i in dir:
#     print(i)
# print()

''' 내 풀이는 실패

# 1 2 3 4 : 위 아래 왼쪽 오른쪽
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

# direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
first_direct = [0] + list(map(int, input().split()))

smell = [[[] for _ in range(N)] for _ in range(N)]
sharks = [[] for _ in range(M+1)]

for i in range(N):
    for j in range(N):
        num = board[i][j]
        if num:
            smell[i][j].append([num, k])
            sharks[num].append([i, j, first_direct[num]])

priority_directs = [[] for _ in range(M+1)]

for i in range(1, M + 1):
    priority_directs[i].append([])
    for _ in range(4):
        priority_directs[i].append(list(map(int, input().split())))

def spread():
    for num in range(1, M+1):
        if len(sharks[num]) == 0:
            continue
        if sum(sharks[num][0]) == -3:
            continue

        y, x, d = sharks[num][0]

        if len(smell[y][x]) == 0 or smell[y][x][0][0] == num:
            # 향기 뿌리기
            smell[y][x].append([num, k])
        else:
            # 기존의 더 쎈 상어가 있으므로 격자 밖으로 쫓겨남.
            sharks[num][0] = [-1, -1, -1]


def smell_reduce():
    # 향기 한칸 줄이기 and k 값이 0 이면 삭제
    for i in range(N):
        for j in range(N):
            if len(smell[i][j]):
                smell[i][j][0][1] -= 1

                if smell[i][j][0][1] == 0:
                    del smell[i][j][0]

        
def move():
    for num in range(1, M+1):
        if len(sharks[num]) == 0:
            continue
        if sum(sharks[num][0]) == -3:
            continue

        y, x, d = sharks[num][0]
        priority_direct = priority_directs[num][d]

        # 이동할 칸.
        next_positions = []

        # 인접한 칸 중 아무 냄새도 없는 칸들 검색.
        for nd in priority_direct:
            ny, nx = y + dy[nd], x + dx[nd]
            if 0 <= ny < N and 0 <= nx < N:
                # print(ny, nx)
                if len(smell[ny][nx]) == 0:
                    # 인접한 칸 중 아무 냄새도 없는 칸들.
                    next_positions.append([ny, nx, nd])
                    break

        # 아무 냄새도 없는 칸이 없을 때, 자기의 냄새가 있는 곳으로.
        if len(next_positions) == 0:
            #print(1)
            for nd in priority_direct:
                ny, nx = y + dy[nd], x + dx[nd]
                if 0 <= ny < N and 0 <= nx < N:
                    if len(smell[ny][nx]) != 0:
                        #print(smell[ny][nx][0][0], num)
                        if smell[ny][nx][0][0] == num:
                            next_positions.append([ny, nx, nd])
                            break
        
        #print(next_positions)
        # 이동
        board[y][x] = 0
        sharks[num][0] = next_positions[0]

def state():
    for num, i in enumerate(sharks):
        if len(i) != 0 and sum(i[0]) != -3:
            y, x, d = i[0]
            board[y][x] = num


time = 0

while True:
    move()
    time += 1
    smell_reduce()
    spread()
    state()

    print("board")
    for i in board:
        print(i)
    print()

    print("smell")
    for i in smell:
        print(i)
    print()

    print("shark")

    for i in sharks:
        print(i)
    print()


    count = 0
    for i in sharks:
        if len(i) != 0 and sum(i[0]) != -3:
            count += 1
    
    if count == 1:
        break

    if time > 1000:
        time = -1
        break

print(time)
'''