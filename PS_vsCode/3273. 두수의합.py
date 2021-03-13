n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = 0

left, right = 0, n-1

arr.sort()

while left != right:
    temp = arr[left] + arr[right]
    if temp == x:
        result += 1
        left += 1
    elif temp > x:
        right -= 1
    else:
        left += 1

print(result)