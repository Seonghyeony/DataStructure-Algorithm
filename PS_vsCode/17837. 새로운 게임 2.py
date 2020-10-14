import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, z = chess[chess_num]
    nx = x + dx[z]
    ny = y + dy[z]

    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0
        
    chess_set = []
    for i, key in enumerate(chess_map[x][y]):
        if key == chess_num:
            chess_set.extend(chess_map[x][y][i:])
            chess_map[x][y] = chess_map[x][y][:i]
            break
    
    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]
    
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1

while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit(0)
    cnt += 1
print(-1)

''' 내것도 성공이긴 하지만 최적화 x
# 체스판 색은 흰색, 빨간색, 파란색 중 하나.

# 1 턴: 1번 말부터 K번 말까지 순서대로 이동.
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동.

# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임 종료.


n, k = map(int, input().split())
# 0: 흰 1: 빨 2: 파
board = [list(map(int, input().split())) for _ in range(n)]
state = [[[] for _ in range(n)] for _ in range(n)]
piece = []

# 동 서 북 남
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

time = 0

for idx in range(k):
    r, c, d = map(int, input().split())
    piece.append([r-1, c-1, d-1])
    state[r-1][c-1].append(idx)

# print("초기상태")
# for i in state:
#     print(i)
# print(piece)

while True:
    flag = False
    time += 1
    # print("time = ", time)
    for idx in range(k):
        y, x, d = piece[idx]
        ny, nx = y + dy[d], x + dx[d]

        # 말이 체스판을 벗어나는 경우 = 파란색과 같은 경우
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            
            ny, nx = y + dy[d], x + dx[d]

            if board[ny][nx] == 0:
                loc = state[y][x].index(idx)
                tmp = state[y][x][loc:]
                state[y][x] = state[y][x][:loc]
                if len(state[ny][nx]):
                    state[ny][nx].extend(tmp)
                else:
                    state[ny][nx] = tmp
                for index in tmp:
                    a, b, c = piece[index]
                    piece[index] = [ny, nx, c]
            elif board[ny][nx] == 1:
                loc = state[y][x].index(idx)
                tmp = state[y][x][loc:]
                tmp.reverse()
                state[y][x] = state[y][x][:loc]
                if len(state[ny][nx]):
                    state[ny][nx].extend(tmp)
                else:
                    state[ny][nx] = tmp
                for index in tmp:
                    a, b, c = piece[index]
                    piece[index] = [ny, nx, c]
            elif board[ny][nx] == 2:
                ny, nx = y, x
        # 이동하려는 칸이 흰색
        else:
            if board[ny][nx] == 0:
                loc = state[y][x].index(idx)
                tmp = state[y][x][loc:]
                state[y][x] = state[y][x][:loc]
                if len(state[ny][nx]):
                    state[ny][nx].extend(tmp)
                else:
                    state[ny][nx] = tmp
                for index in tmp:
                    a, b, c = piece[index]
                    piece[index] = [ny, nx, c]
            elif board[ny][nx] == 1:
                loc = state[y][x].index(idx)
                tmp = state[y][x][loc:]
                tmp.reverse()
                state[y][x] = state[y][x][:loc]
                if len(state[ny][nx]):
                    state[ny][nx].extend(tmp)
                else:
                    state[ny][nx] = tmp
                for index in tmp:
                    a, b, c = piece[index]
                    piece[index] = [ny, nx, c]
            elif board[ny][nx] == 2:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
                
                ny, nx = y + dy[d], x + dx[d]
                
                if 0 <= ny < n and 0 <= nx < n:
                    if board[ny][nx] == 0:
                        loc = state[y][x].index(idx)
                        tmp = state[y][x][loc:]
                        state[y][x] = state[y][x][:loc]
                        if len(state[ny][nx]):
                            state[ny][nx].extend(tmp)
                        else:
                            state[ny][nx] = tmp
                        for index in tmp:
                            a, b, c = piece[index]
                            piece[index] = [ny, nx, c]
                    elif board[ny][nx] == 1:
                        loc = state[y][x].index(idx)
                        tmp = state[y][x][loc:]
                        tmp.reverse()
                        state[y][x] = state[y][x][:loc]
                        if len(state[ny][nx]):
                            state[ny][nx].extend(tmp)
                        else:
                            state[ny][nx] = tmp
                        for index in tmp:
                            a, b, c = piece[index]
                            piece[index] = [ny, nx, c]
                    elif board[ny][nx] == 2:
                        ny, nx = y, x
                # 말이 체스판을 벗어나는 경우 = 파란색과 같은 경우
                else:
                    ny, nx = y, x
                
        
        # 말 정보 갱신
        piece[idx] = [ny, nx, d]

        # print(idx, "말 옮김 후 상태")
        # for i in state:
        #     print(i)

        # print("말 정보 갱신")
        # print(piece)

        # 말이 4개 이상 쌓이면 게임 종료!
        for i in range(n):
            for j in range(n):
                if len(state[i][j]) >= 4:
                    flag = True
                    break
        
    if flag:
        break
    else:
        if time == 1000:
            time = -1
            break
    
print(time)

'''