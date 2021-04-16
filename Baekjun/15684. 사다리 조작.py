import sys
sys.setrecursionlimit(10**5)

# N개 세로선, M개 가로선, H개 각 세로선마다 가로선을 놓을 수 있는 위치
def ladder(y, x):
    for i in range(H+1):
        ny, nx = y + 1, x
        if ny == H:
            break
        if lst[ny][nx] == 1:
            for i in range(2):
                temp_y, temp_x = ny + dy[i], nx + dx[i]
                if temp_x > N:
                    continue
                if lst[temp_y][temp_x]:
                    ny, nx = temp_y, temp_x
                    break
        y, x = ny, nx
    return x

def isAddLine(y, x):
    if lst[y][x] == 0 and lst[y][x+1] == 0 and lst[y][x-1] == 0:
        if x + 2 <= N:
            if lst[y][x+2] == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def solve(n):
    global result
    if n >= 4:
        return

    flag = True
    for i in range(1, N+1):
        ret = ladder(0, i)
        if i != ret:
            flag = False
            for y in range(1, H+1):
                for x in range(1, N):
                    if lst[y][x] == 0:
                        if isAddLine(y, x):
                            lst[y][x], lst[y][x+1] = 1, 1
                            # for i in lst:
                            #     print(i)
                            # print()
                            solve(n+1)
                            lst[y][x], lst[y][x+1] = 0, 0

    if flag:
        if result > n:
            for i in lst:
                print(i)
            print()
            result = n
        return
    

dy, dx = [0, 0], [-1, 1]
N, M, H = map(int, input().split())
lst = [[0 for _ in range(N+1)] for _ in range(H+1)]
visited = []
result = 4
if M == 0:
    print(0)
else:
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a][b], lst[a][b+1] = 1, 1
    
    solve(0)
    if result <= 3:
        print(result)
    else:
        print(-1)
    

    
