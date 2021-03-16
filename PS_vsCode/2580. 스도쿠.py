import sys

def check(y, x, num):
    for i in range(9):
        if lst[y][i] == num:
            return False
    for i in range(9):
        if lst[i][x] == num:
            return False
    # ty = y - y % 3
    # tx = x - x % 3
    ty = y // 3 * 3
    tx = x // 3 * 3
    for p in range(3):
        for q in range(3):
            if lst[ty+p][tx+q] == num:
                return False
    return True

def dfs(index):
    if index == len(zeros):
        for i in lst:
            print(' '.join(map(str, i)))
        sys.exit(0)
        return

    for i in range(1, 10):
        ny = zeros[index][0]
        nx = zeros[index][1]

        if check(ny, nx, i):
            lst[ny][nx] = i
            dfs(index + 1)
            lst[ny][nx] = 0

lst = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if lst[i][j] == 0]
dfs(0)