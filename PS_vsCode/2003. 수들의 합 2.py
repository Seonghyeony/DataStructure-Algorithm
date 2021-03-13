N, M = map(int, input().split())
A = list(map(int, input().split()))

left, right, result = 0, 0, 0
while right <= N-1:
    temp = sum(A[left:right+1])
    if temp == M:
        result += 1
        left += 1
        right += 1
    elif temp < M:
        right += 1
    else:
        left += 1
print(result)
