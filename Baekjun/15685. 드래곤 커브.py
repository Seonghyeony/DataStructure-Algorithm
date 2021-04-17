def make_generation():
    global end_x, end_y
    size = len(dragon)

    for i in range(size-1, -1, -1):
        dir = (dragon[i] + 1) % 4

        end_x, end_y = end_x + dx[dir], end_y + dy[dir]

        a[end_x][end_y] = True

        dragon.append(dir)

max_int = 101
end_x, end_y = 0, 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dragon = []
result = 0
a = [[False for _ in range(max_int)] for _ in range(max_int)]
n = int(input())

for _ in range(n):
    y, x, d, g = map(int, input().split())
    dragon.clear()
    end_x, end_y = x, y
    a[end_x][end_y] = True
    end_x, end_y = x + dx[d], y + dy[d]
    a[end_x][end_y] = True

    dragon.append(d)

    for i in range(g):
        make_generation()

for i in range(max_int - 1):
    for j in range(max_int - 1):
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
            result += 1

print(result)
