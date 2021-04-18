# r-1, c-1
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# M 개의 나무. 같은 칸에 여러 개 가능.
# 4계절동안....
# 봄: 양분 먹고 나이 1 증가
# 같은 칸에 여러 개의 나무 -> 어린 나무부터 양분을 먹는다.
# 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없으면 그 나무는 양분을 먹지 못하고 즉사.
# 여름: 죽은 나무가 양분으로. 나이 // 2
# 가을: 나무 번식. 나이가 5의 배수일 때만. 인접한 8개의 칸에 나이 1 나무가 생김. 칸을 벗어난 곳은 x.
# 겨울: 로봇이 땅에 양분을 추가. 입력으로 주어짐
# K 년이 지난 후 땅에 살아있는 나무의 개수는?

''' 38분 클리어! '''

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
ground = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
nutrition = []
for _ in range(N):
    nutrition.append(list(map(int, input().split())))
for _ in range(M):
    y, x, z = map(int, input().split())
    trees[y-1][x-1].append(z)

for _ in range(K):
    # 봄
    die = []
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                queue = []
                nutri = 0
                trees[y][x].sort()
                for idx in range(len(trees[y][x])):
                    tree = trees[y][x][idx]
                    if ground[y][x] - tree >= 0:
                        ground[y][x] -= tree
                        queue.append(tree+1)
                    else:
                        nutri += (tree // 2)
                trees[y][x] = queue
                ground[y][x] += nutri
    #         die.append([y, x, nutri])
    
    # # 여름
    # for y, x, value in die:
    #     ground[y][x] += value

    # 가을
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                for i in range(len(trees[y][x])):
                    if trees[y][x][i] % 5 == 0:
                        for d in range(8):
                            ny, nx = y + dy[d], x + dx[d]
                            if 0 <= ny < N and 0 <= nx < N:
                                trees[ny][nx].append(1)
            ground[y][x] += nutrition[y][x]

    # 겨울
    # for y in range(N):
    #     for x in range(N):
    #         ground[y][x] += nutrition[y][x]

result = 0
for y in range(N):
    for x in range(N):
        if trees[y][x]:
            result += len(trees[y][x])

print(result)