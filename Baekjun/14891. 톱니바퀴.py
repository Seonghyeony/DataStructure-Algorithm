# N극 0, S극 1
# 1 시계방향, -1 반시계 방향
from collections import deque

wheel = [[]]
for _ in range(4):
    wheel.append(deque(list(input())))
K = int(input())
for _ in range(K):
    num, r = map(int, input().split())
    need_rotate = [[num, r]]

    pre_left = wheel[num][6]
    pre_right = wheel[num][2]
    current_num = num
    current_r = r
    # 왼쪽 검사
    while current_num - 1 > 0:
        current_num -= 1
        current_left = wheel[current_num][6]
        current_right = wheel[current_num][2]
        if pre_left != current_right:
            current_r = -(current_r)
            need_rotate.append([current_num, current_r])
            pre_left = current_left
            pre_right = current_right
        else:
            break
    
    pre_left = wheel[num][6]
    pre_right = wheel[num][2]
    current_num = num
    current_r = r
    # 오른쪽 검사
    while current_num + 1 < 5:
        current_num += 1
        current_left = wheel[current_num][6]
        current_right = wheel[current_num][2]
        if pre_right != current_left:
            current_r = -(current_r)
            need_rotate.append([current_num, current_r])
            pre_left = current_left
            pre_right = current_right
        else:
            break

    for number, nr in need_rotate:
        wheel[number].rotate(nr)

result = 0
n = 0
for i in range(1, 5):
    result += int(wheel[i][0]) * (2**n)
    n += 1

print(result)

