import copy

N, A = int(input()), list(map(int, input().split()))

dp = copy.deepcopy(A)
rev = [i for i in range(N)]
idx = 0

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i] and dp[i] < A[i] + dp[j]:
            dp[i] = A[i] + dp[j]
            #rev[i] = j

print(max(dp))
    #if dp[idx] < dp[i]:
    #    idx = i

# while rev[idx] != idx:
#     print(A[idx], sep=" ")
#     idx = rev[idx]

# print(A[idx])