from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

score = 0

for num, direct in rotation:
    num -= 1
    gear_2 = gear[num][2]
    gear_6 = gear[num][6]
    gear[num].rotate(direct)
    tmp_direct = direct
    
    direct = tmp_direct
    for i in range(num-1, -1, -1):
        if gear[i][2] != gear_6:
            gear_6 = gear[i][6]
            gear[i].rotate(direct * -1)
            direct *= -1
        else:
            break

    direct = tmp_direct
    for i in range(num+1, 4):
        if gear[i][6] != gear_2:
            gear_2 = gear[i][2]
            gear[i].rotate(direct * -1)
            direct *= -1
        else:
            break

for i in range(4):
    if gear[i][0] == 1:
        score += (2**i)
print(score)





