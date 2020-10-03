N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# dp[i] = i일까지 얻는 이익
dp = [0 for _ in range(N)]

for i in range(N):
    if i + lst[i][0] <= N:
        dp[i] = lst[i][1]
        for j in range(i):
            if j + lst[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + lst[i][1])
print(max(dp))
