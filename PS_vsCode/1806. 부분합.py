N, S = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 0
temp_A = 0
result = float('inf')

while True:
    if temp_A >= S:
        result = min(result, right - left)
        temp_A -= A[left]
        left += 1
    elif right == N:
        break
    else:
        temp_A += A[right]
        right += 1

if result == float('inf'):
    print(0)
else:
    print(result)