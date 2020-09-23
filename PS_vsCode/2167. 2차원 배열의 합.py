# 2차원 배열 누적합 구하는 방법 중요!!!

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# DP[i][j] = (1, 1)부터 (i, j)까지의 부분합
DP = [[0 for i in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1] + A[i - 1][j - 1]

K = int(input())
location = [list(map(int, input().split())) for _ in range(K)]

for i, j, x, y in location:
    print(DP[x][y] - DP[i - 1][y] - DP[x][j - 1] + DP[i - 1][j - 1])

