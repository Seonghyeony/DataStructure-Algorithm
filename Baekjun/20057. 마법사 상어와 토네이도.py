from collections import deque

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ratios = [
            [[0, -2, 0.05], [-1, -1, 0.1], [1, -1, 0.1], [-1, 0, 0.07], [1, 0, 0.07], [-2, 0, 0.02], [2, 0, 0.02], [-1, 1, 0.01], [1, 1, 0.01], [0, -1]],
            [[2, 0, 0.05], [1, -1, 0.1], [1, 1, 0.1], [0, -1, 0.07], [0, 1, 0.07], [0, -2, 0.02], [0, 2, 0.02], [-1, -1, 0.01], [-1, 1, 0.01], [1, 0]],
            [[0, 2, 0.05], [-1, 1, 0.1], [1, 1, 0.1], [-1, 0, 0.07], [1, 0, 0.07], [-2, 0, 0.02], [2, 0, 0.02], [-1, -1, 0.01], [1, -1, 0.01], [0, 1]],
            [[-2, 0, 0.05], [-1, -1, 0.1], [-1, 1, 0.1], [0, -1, 0.07], [0, 1, 0.07], [0, -2, 0.02], [0, 2, 0.02], [1, -1, 0.01], [1, 1, 0.01], [-1, 0]]
        ]
queue = deque([0, 1, 2, 3])
y, x = N // 2, N // 2
count = 0
result = 0
while True:
    d = queue.popleft()
    if d == 0:
        count += 1
    length = count
    if d == 0 or d == 1:
        length = length * 2 - 1
    else:
        length = length * 2
    for _ in range(length):
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or nx < 0:
            y, x = ny, nx
            break
        ratio = ratios[d]
        temp = 0
        for i in range(9):
            r, c, per = ratio[i]
            r, c = ny + r, nx + c
            wind = int(lst[ny][nx] * per)
            if 0 <= r < N and 0 <= c < N:
                lst[r][c] += wind
            else:
                result += wind
            temp += wind
        wind = lst[ny][nx] - temp
        r, c = ratio[-1]
        r, c = ny + r, nx + c
        if 0 <= r < N and 0 <= c < N:
            lst[r][c] += wind
        else:
            result += wind
        lst[ny][nx] = 0
        y, x = ny, nx

    queue.append(d)
    if y < 0 or x < 0:
        break
    
print(result)
