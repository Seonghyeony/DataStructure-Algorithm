# 말의 개수 K, 1~K 번
# 말은 원판 모양이고, 하나의 말 위에 다른 말을 올릴 수 있다.
# 각 칸은 흰, 빨, 파 중 하나
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동.
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동.
# 말 4개 이상 쌓이는 순간 게임 종료.
# 게임이 종료되는 턴의 번호는?!

# 0: 흰색, 1: 빨간색, 2: 파란색

# 1시간 20분 클리어!
'''
def change_d(d):
    if d == 1 or d == 2:
        return (d * 2) % 3
    else:
        return (d * 2 + 2) % 3 + 2


def white(num, y, x, ny, nx, num_d):
    global chess
    index = board[y][x].index(num)
    temp = board[y][x][index:]
    board[y][x] = board[y][x][:index]
    board[ny][nx].extend(temp)
    for number in temp:
        r, c, d = chess[number]
        if number == num:
            chess[number] = [ny, nx, num_d]
        else:
            chess[number] = [ny, nx, d]

def red(num, y, x, ny, nx, num_d):
    global chess
    index = board[y][x].index(num)
    temp = board[y][x][index:]
    temp.reverse()
    board[y][x] = board[y][x][:index]
    board[ny][nx].extend(temp)
    for number in temp:
        r, c, d = chess[number]
        if num == number:
            chess[number] = [ny, nx, num_d]
        else:
            chess[number] = [ny, nx, d]

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
chess = [[]]
time = 0
for num in range(1, K+1):
    r, c, d = map(int, input().split())
    r, c = r-1, c-1
    board[r][c].append(num)
    chess.append([r, c, d])

while True:
    flag = False
    time += 1
    for num in range(1, K+1):
        y, x, d = chess[num]
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            if lst[ny][nx] == 0:
                white(num, y, x, ny, nx, d)
            elif lst[ny][nx] == 1:
                red(num, y, x, ny, nx, d)
            elif lst[ny][nx] == 2:
                d = change_d(d)
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if lst[ny][nx] == 2:
                        chess[num] = [y, x, d]
                    elif lst[ny][nx] == 0:
                        white(num, y, x, ny, nx, d)
                    elif lst[ny][nx] == 1:
                        red(num, y, x, ny, nx, d)
                else:
                    chess[num] = [y, x, d]
        else:
            d = change_d(d)
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if lst[ny][nx] == 0:
                    white(num, y, x, ny, nx, d)
                elif lst[ny][nx] == 1:
                    red(num, y, x, ny, nx, d)
                elif lst[ny][nx] == 2:
                    chess[num] = [y, x, d]
            else:
                chess[num] = [y, x, d]
        
        p, q, dd = chess[num]
        if len(board[p][q]) >= 4:
            flag = True
            break

    if flag:
        break

    if time > 1000:
        time = -1
        break

print(time)
'''

import sys

def move(chess_num):
    x, y, z = chess[chess_num]
    nx, ny = x + dx[z], y + dy[z]

    if not 0<= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        
        chess[chess_num][2] = nz
        nx, ny = x + dx[nz], y + dy[nz]
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

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

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