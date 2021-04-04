n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        continue
    values = []

    if i % 3 == 0:
        values.append(dp[i // 3] + 1)
    if i % 2 == 0:
        values.append(dp[i // 2] + 1)
    values.append(dp[i - 1] + 1)

    dp[i] = min(values)
print(dp[n])

'''
N = int(input())
dp = [float('inf') for _ in range(N + 1)]
dp[1] = 0
for i in range(1, N + 1):
    if i * 3 <= N:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 2 <= N:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i + 1 <= N:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
print(dp[N])
'''