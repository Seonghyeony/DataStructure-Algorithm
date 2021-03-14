N = int(input())
M = int(input())
A = list(map(int, input().split()))

A.sort()
left, right, result = 0, N-1, 0

while left < right:
    temp = A[left] + A[right]
    if temp == M:
        result += 1
        left += 1
        right -= 1
    elif temp < M:
        left += 1
    else:
        right -= 1
print(result)
