from collections import deque

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
N, M, y, x, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
dice = [[0, 0, 0], deque([0, 0, 0]), [0, 0, 0], [0, 0, 0]]

def rotate(d):
    if d == 1:
        temp = dice[1].pop()
        dice[1].appendleft(dice[3][1])
        dice[3][1] = temp
    elif d == 2:
        temp = dice[1].popleft()
        dice[1].append(dice[3][1])
        dice[3][1] = temp
    elif d == 3:
        temp = dice[0][1]
        for i in range(1, 4):
            dice[i-1][1] = dice[i][1]
        dice[3][1] = temp
    elif d == 4:
        temp = dice[3][1]
        for i in range(2, -1, -1):
            dice[i+1][1] = dice[i][1]
        dice[0][1] = temp

for command in commands:
    ny, nx = y + dy[command], x + dx[command]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
        rotate(command)
        if lst[y][x] == 0:
            lst[y][x] = dice[3][1]
        else:
            dice[3][1] = lst[y][x]
            lst[y][x] = 0
        print(dice[1][1])
        
