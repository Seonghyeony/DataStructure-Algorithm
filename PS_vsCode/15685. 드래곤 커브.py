N = int(input())
lst = [[0] * 101 for _ in range(101)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

result = 0

dragon = []

end_y, end_x = 0, 0

def make_curve():
    length = len(dragon)
    for i in range(length-1, -1, -1):
        direct = (dragon[i] + 1) % 4

        global end_y, end_x
        end_y = end_y + dy[direct]
        end_x = end_x + dx[direct]
        lst[end_y][end_x] = 1

        dragon.append(direct)

for _ in range(N):
    x, y, d, g = map(int, input().split())

    dragon.clear()
    end_y, end_x = y, x
    lst[end_y][end_x] = 1

    end_y, end_x = y + dy[d], x + dx[d]
    lst[end_y][end_x] = 1

    dragon.append(d)

    for _ in range(g):
        make_curve()

for i in range(100):
    for j in range(100):
        if lst[i][j] and lst[i+1][j] and lst[i][j+1] and lst[i+1][j+1]:
            result += 1

for i in lst:
    print(i)

print(result)


