N = int(input())
T, P = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * 25

for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i + T[i]] < dp[i] + P[i]:
        dp[i + T[i]] = dp[i] + P[i]

print(dp[N])


'''
N = int(input())
t, p = [0] * N, [0] * N
for i in range(N):
    t[i], p[i] = map(int, input().split())

dp = [0] * 25

for i in range(N):
    # 현재가 다음 날보다 보상이 높다면
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    # T일 후에 받게 될 금액이 현재의 보상보다 높다면
    if dp[i + t[i]] < dp[i] + p[i]:
        dp[i + t[i]] = dp[i] + p[i]
    print(dp)

print(dp[N])
'''