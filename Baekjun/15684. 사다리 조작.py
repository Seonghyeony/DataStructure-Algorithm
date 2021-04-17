def check():
    for i in range(1, N+1):
        ck = i
        for j in range(1, H+1):
            if lst[j][i]:
                if i + 1 <= N:
                    i += 1
                    continue
            else:
                if lst[j][i-1]:
                    i -= 1
                    continue
        if i != ck:
            return False
    return True

def isAddLine(y, x):
    if lst[y][x-1] or lst[y][x+1]:
        return False
    return True
    

def solve(n):
    global result
    if check():
        if result > n:
            result = n
    elif n == 3 or result <= n:
        return

    for i in range(1, H+1):
        for j in range(1, N):
            if lst[i][j] == 0:
                if isAddLine(i, j):
                    lst[i][j] = 2
                    solve(n+1)
                    lst[i][j] = 0
    return

dx = [-1, 1]
N, M, H = map(int, input().split())
lst = [[0 for _ in range(N+1)] for _ in range(H+1)]
if M == 0:
    print(0)
    exit(0)

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1

result = 4
solve(0)

if result == 4:
    print(-1)
else:
    print(result)

