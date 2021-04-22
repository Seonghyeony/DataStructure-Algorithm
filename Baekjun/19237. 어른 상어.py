# 1이상 M이하의 자연수. 낮을 수록 쎄다.
# 냄새는 상어가 k번 이동하면 사라짐
# 아무 냄새가 없는 칸으로 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸으로.
# 갈 수 있는 칸이 여러 개면. 우선순위를 따름.
# 1번 상어만 격자에 남게 되는 시간은?

# 1시간 5분 클리어!

dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
N, M, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]
direction = [0] + list(map(int, input().split()))
priority = [[[]] for _ in range(M)]

r, c = 0, 0
for _ in range(M*4):
    priority[r].append(list(map(int, input().split())))
    c += 1
    if c == 4:
        r += 1
        c = 0

for i in range(N):
    for j in range(N):
        if lst[i][j]:
            smell[i][j] = [lst[i][j], k]
            lst[i][j] = [lst[i][j], direction[lst[i][j]]]

def find_sharks():
    positions = []
    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0:
                positions.append([i, j])
    return positions


def sharks_move():
    sharks = find_sharks()
    for y, x in sharks:
        num, d = lst[y][x]
        nd_list = priority[num-1][d]
        flag = True
        for i in range(4):
            nd = nd_list[i]
            ny, nx = y + dy[nd], x + dx[nd]
            if 0 <= ny < N and 0 <= nx < N:
                # 주변에 냄새가 없는 곳이 있으면.
                if smell[ny][nx] == 0:
                    flag = False
                    # 상어가 이미 존재한다면
                    if lst[ny][nx] != 0:
                        # 자신이 번호가 작다면 (더 쎄다면)
                        if lst[ny][nx][0] > num:
                            # 상어 전진
                            lst[y][x], lst[ny][nx] = 0, [num, nd]
                        else:
                            # 자신이 약하면 그냥 쫒겨난다.
                            lst[y][x] = 0
                    else:
                        # 상어가 존재하지 않는다면
                        lst[y][x], lst[ny][nx] = 0, [num, nd]
                    break
        # 움직일 수 있는 곳이 없으면
        if flag:
            # 자신의 냄새가 있는 곳으로 간다.
            for i in range(4):
                nd = nd_list[i]
                ny, nx = y + dy[nd], x + dx[nd]
                if 0 <= ny < N and 0 <= nx < N:
                    # 자신의 냄새면
                    if smell[ny][nx][0] == num:
                        # 상어 전진
                        lst[y][x], lst[ny][nx] = 0, [num, nd]
                        break

def smell_process():
    # 이미 존재하는 냄새 1 줄이기
    for i in range(N):
        for j in range(N):
            if smell[i][j] != 0:
                smell[i][j][1] -= 1
                # 냄새가 0이면 삭제
                if smell[i][j][1] == 0:
                    smell[i][j] = 0
    
    # 상어가 존재하는 곳에 냄새 뿌리기
    sharks = find_sharks()
    for y, x in sharks:
        num, d = lst[y][x]
        smell[y][x] = [num, k]

time = 0
while True:
    time += 1
    sharks_move()

    temp = find_sharks()
    if len(temp) == 1:
        break

    smell_process()

    if time == 1000:
        time = -1
        break

print(time)
