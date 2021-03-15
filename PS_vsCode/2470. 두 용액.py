N = int(input())
A = list(map(int, input().split()))
A.sort()

left, right, value = 0, N-1, float('inf')
result_left, result_right = 0, N-1

while left < right:
    temp_value = abs(A[left] + A[right])
    if temp_value < value:
        value = temp_value
        result_left, result_right = left, right

    if temp_value == 0:
        break

    if A[left] + A[right] < 0:
        left += 1
    else:
        right -= 1

print(A[result_left], A[result_right])


