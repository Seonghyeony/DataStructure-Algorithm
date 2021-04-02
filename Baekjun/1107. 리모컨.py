n = int(input())
m = int(input())

buttons = {str(i) for i in range(10)}
if m:
    buttons -= set(map(str, input().split()))

channel = 100
# case1: 100번에서 +, - 로만 움직이는 경우
result = abs(n - channel)
# case2: 1,000,000 채널까지 브루트 포스 진행
# 500,000 채널까지 존재하므로 500,000 보다 크면서 모든 숫자의 경우를 거치는 1,000,000까지를 범위로 잡음
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in buttons:
            break
        elif j == len(num) - 1:
            result = min(result, abs(n - int(num)) + len(str(num)))

print(result)
