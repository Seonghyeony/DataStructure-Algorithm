# 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다.
# 원판에는 M개의 정수. i번째 원판에 적힌 j번째 수의 위치는 (i, j)
# 회전은 독립적으로.

# 58분 클리어!

from collections import deque

def delete():
    candidate = set()
    for i in range(1, N+1):
        for j in range(M):
            if lst[i][j] != 0:
                if i == N:
                    if lst[N][j] == lst[N-1][j]:
                        if lst[N][j] != 0:
                            candidate.add((N, j))
                            candidate.add((N-1, j))
                elif 2 <= i < N:
                    if lst[i][j] == lst[i-1][j]:
                        candidate.add((i, j))
                        candidate.add((i-1, j))
                    if lst[i][j] == lst[i+1][j]:
                        candidate.add((i, j))
                        candidate.add((i+1, j))
                
                if lst[i][j] == lst[i][(j-1) % M]:
                    candidate.add((i, j))
                    candidate.add((i, (j-1) % M))
                if lst[i][j] == lst[i][(j+1) % M]:
                    candidate.add((i, j))
                    candidate.add((i, (j+1) % M))
    
    if len(candidate):
        for y, x in candidate:
            lst[y][x] = 0
        return True

    return False

def plusMinus():
    count = 0
    total = 0
    for i in range(1, N+1):
        total += sum(lst[i])
        for j in range(M):
            if lst[i][j] != 0:
                count += 1

    if total == 0 or count == 0:
        return
        
    avg = total / count
    for i in range(1, N+1):
        for j in range(M):
            if lst[i][j] != 0:
                if lst[i][j] > avg:
                    lst[i][j] -= 1
                elif lst[i][j] < avg:
                    lst[i][j] += 1


N, M, K = map(int, input().split())
lst = [deque()] + [deque(list(map(int, input().split()))) for _ in range(N)]

for _ in range(K):
    x, d, k = map(int, input().split())
    if d == 0:
        d = 1
    elif d == 1:
        d = -1
    
    temp_x = x
    while temp_x <= N:
        for _ in range(k):
            lst[temp_x].rotate(d)
        temp_x += x

    if not delete():
        plusMinus()

print(sum(map(sum, lst)))


        
    

