N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
temp_sum = sum(A[0:K])
result = temp_sum

if K == 1:
    print(max(A))
else:
    while True:
        if count + K >= N:
            break
        temp_sum -= A[count]
        temp_sum += A[count+K]
        if result < temp_sum:
            result = temp_sum
        count += 1
    print(result)
