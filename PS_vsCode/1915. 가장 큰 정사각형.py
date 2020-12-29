N, M = map(int, input().split())
A = [[0] * (M + 1)]
# DP[i][j] = (i, j) 까지 왔을 때, 가장 큰 정사각형의 한 변의 길이
DP = [[0] * (M + 1) for _ in range(N + 1)]
result = 0

for i in range(1, N + 1):
    tmp = [0] + list(map(int, input()))
    A.append(tmp)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
            result = max(result, DP[i][j])

print(result**2)
