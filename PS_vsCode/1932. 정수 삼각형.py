N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = lst[0][0]

for i in range(1, N):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + lst[i][j]
print(max(dp[N-1]))
