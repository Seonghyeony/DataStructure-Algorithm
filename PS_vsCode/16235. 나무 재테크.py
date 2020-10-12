# 인덱스 1부터 시작
# 모든 칸의 처음 양분은 5
# 한 칸에 여러 개 나무 가능
# 4계절

# A = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
# food = [[0] * (N + 1)] + [[0] + [5 for _ in range(N)] for _ in range(N)]
# # (y, x): 위치, z: 나무의 나이
# tree = [[0] * (N + 1)] + [[0] + [0 for _ in range(N)] for _ in range(N)]

# python3 시간초과 pypy3 성공

direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m, k = map(int, input().split())
plus_a = [list(map(int, input().split())) for _ in range(n)]
a = [[5] * n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]  # 이 부분을 딕셔너리로 하면 더 빠르다고 한다.

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for year in range(k):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= a[i][j]:
                        a[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age // 2
                a[i][j] += dead_tree
                tree[i][j] = []
                tree[i][j].extend(temp_tree)
    
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for dx, dy in direct:
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)
    
    for i in range(n):
        for j in range(n):
            a[i][j] += plus_a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])

print(ans)


'''
시간초과 실패

from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = [[5 for _ in range(N)] for _ in range(N)]

direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# (y, x): 위치, z: 나무의 나이
tree = []

for _ in range(M):
    y, x, z = map(int, input().split())
    tree.append([y-1, x-1, z])

for i in range(1, K+1):
    # 봄: 자신의 나이만큼 양분 먹고 나이 1증가. 여러 개 있다면 나이가 어린 나무부터. 자신의 나이만큼 못먹으면 즉사.
    # 여름: 봄에 죽은 나무가 양분으로 변함. 죽은 나무의 // 2 값이 양분으로 추가.
    # 가을: 나이가 5의 배수인 나무 번식. 8개의 칸에 나이가 1인 나무.
    # 겨울: 땅에 양분 추가. 각 칸의 추가되는 양분의 양은 A[r][c], 입력으로 주어짐
    # 문제: K년 후 살아있는 나무의 갯수 출력.

    # tree, food, die_tree = spring(tree, food)

    grow_tree = []
    die_tree = []
    tree.sort()

    for i in tree:
        y, x, z = i
        if food[y][x] - z < 0:
            die_tree.append([y, x, z])
            continue
        food[y][x] -= z
        z += 1
        grow_tree.append([y, x, z])

    tree = grow_tree

    # food = summer(food, die_tree)

    for i in die_tree:
        y, x, z = i
        value = z // 2
        food[y][x] += value

    # tree = fall(tree)

    for i in tree:
        y, x, z = i
        if z % 5 == 0:
            for dy, dx in direct:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    tmp = [ny, nx, 1]
                    tree.append(tmp)

    # food = winter(A, food)
    # food = [[c + d for c, d in zip(a, b)] for a, b in zip(A, food)]
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

print(len(tree))
'''