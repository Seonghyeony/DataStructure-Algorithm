def fibonacci(n):
    dp = [[0, 0] for _ in range(n + 1)]
    if n == 0:
        print(1, 0)
        return
    elif n == 1:
        print(0, 1)
        return
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    if n >= 2:
        for i in range(2, n + 1):
            dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
    print(dp[n][0], dp[n][1])


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    fibonacci(n)
