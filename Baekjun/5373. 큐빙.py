# 큐브 배열을 익히자.

import copy

def clockwise(arr): # 시계방향으로 k번 만큼 회전
    tmp = arr[0][0]
    arr[0][0] = arr[2][0]
    arr[2][0] = arr[2][2]
    arr[2][2] = arr[0][2]
    arr[0][2] = tmp

    tmp = arr[0][1]
    arr[0][1] = arr[1][0]
    arr[1][0] = arr[2][1]
    arr[2][1] = arr[1][2]
    arr[1][2] = tmp

def U(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[0])
        tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
        cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = tmp

def D(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[2])
        tmp = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
        cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = tmp

def R(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[4])
        tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = tmp

def L(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[3])
        tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp

def F(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[1])
        tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
        cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = tmp

def B(c):
    if c == '+':
        k = 1
    else:
        k = 3

    # U F D L R B
    for _ in range(k):
        clockwise(cube[5])
        tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[2][2][2], cube[2][2][1], cube[2][2][0]
        cube[2][2][2], cube[2][2][1], cube[2][2][0] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = tmp

CUBE = [[[] for _ in range(3)] for _ in range(6)]

# 큐브 초기화
s = 'wrygbo'    # U F D L R B
for i in range(6):
    for j in range(3):
        for _ in range(3):
            CUBE[i][j].append(s[i])

for _ in range(int(input())):
    n = int(input())
    cmd = input().split()
    cube = copy.deepcopy(CUBE)

    while cmd:
        c = cmd.pop(0)
        if c[0] == 'L':
            L(c[1])
        elif c[0]== 'D':
            D(c[1])
        elif c[0]== 'U':
            U(c[1])
        elif c[0]== 'F':
            F(c[1])
        elif c[0]== 'R':
            R(c[1])
        elif c[0]== 'B':
            B(c[1])
    
    for i in range(3):
        print(''.join(cube[0][i]))

'''
from collections import deque

def getPlane(c):
    if c == 'U':
        return up
    if c == 'D':
        return down
    if c == 'F':
        return front
    if c == 'B':
        return back
    if c == 'L':
        return left
    if c == 'R':
        return right

    return []

def rotatePlane(c, d):
    N = 3
    ret = [[0 for _ in range(N)] for _ in range(N)]
    lst = getPlane(c)
    if d > 0:
        for i in range(N):
            for j in range(N):
                ret[j][N-1-i] = lst[i][j]
    else:
        for i in range(N):
            for j in range(N):
                ret[N-1-j][i] = lst[i][j]
    
    if c == 'U':
        up = ret
    if c == 'D':
        down = ret
    if c == 'F':
        front = ret
    if c == 'B':
        back = ret
    if c == 'L':
        left = ret
    if c == 'R':
        right = ret

def rotateUp(d):
    if d > 0:
        temp = front[0]
        front[0] = right[0]
        for i in range(3):
            right[0][i] = back[0][3-i-1]
        for i in range(3):
            back[0][i] = left[0][3-i-1]
        left[0] = temp
    else:
        temp = front[0]
        front[0] = left[0]
        for i in range(3):
            left[0][i] = back[0][3-i-1]
        for i in range(3):
            back[0][i] = right[0][3-i-1]
        right[0] = temp

def rotateDown(d):
    if d > 0:
        temp = front[2]
        front[2] = left[2]
        for i in range(3):
            left[2][i] = back[2][3-i-1]
        for i in range(3):
            back[2][i] = right[2][3-i-1]
        right[2] = temp
    else:
        temp = front[2]
        front[2] = right[2]
        for i in range(3):
            right[2][i] = back[2][3-i-1]
        for i in range(3):
            back[2][i] = left[2][3-i-1]
        left[2] = temp

def rotateFront(d):
    if d > 0:
        temp = up[2]
        left_temp = []
        for i in range(3):
            left_temp.append(left[3-i-1][2])
        up[2] = left_temp
        for i in range(3):
            left[i][2] = down[2][i]
        right_temp = []
        for i in range(3):
            right_temp.append(right[3-i-1][0])
        down[2] = right_temp
        for i in range(3):
            right[i][0] = temp[i]
    else:
        temp = up[2]
        right_temp = []
        for i in range(3):
            right_temp.append(right[i][0])
        up[2] = right_temp
        for i in range(3):
            right[i][0] = down[2][3-i-1]
        left_temp = []
        for i in range(3):
            left_temp.append(left[i][2])
        down[2] = left_temp
        for i in range(3):
            left[i][2] = temp[3-i-1]

def rotateBack(d):
    if d > 0:
        temp = up[0]
        right_temp = []
        for i in range(3):
            right_temp.append(right[i][2])
        up[0] = right_temp
        for i in range(3):
            right[i][2] = down[0][3-i-1]
        left_temp = []
        for i in range(3):
            left_temp.append(left[i][0])
        down[0] = left_temp
        for i in range(3):
            left[i][0] = temp[3-i-1]
    else:
        temp = up[0]
        left_temp = []
        for i in range(3):
            left_temp.append(left[3-i-1][0])
        up[0] = left_temp
        for i in range(3):
            left[i][0] = down[0][i]
        right_temp = []
        for i in range(3):
            right_temp.append(right[3-i-1][2])
        down[0] = right_temp
        for i in range(3):
            right[i][2] = temp[i]

def rotateLeft(d):
    if d > 0:
        temp = []
        for i in range(3):
            temp.append(up[i][0])
        for i in range(3):
            up[i][0] = back[3-i-1][0]
        for i in range(3):
            back[i][0] = down[i][0]
        for i in range(3):
            down[i][0] = front[3-i-1][0]
        for i in range(3):
            front[i][0] = temp[i]
    else:
        temp = []
        for i in range(3):
            temp.append(up[i][0])
        for i in range(3):
            up[i][0] = front[i][0]
        for i in range(3):
            front[i][0] = down[3-i-1][0]
        for i in range(3):
            down[i][0] = back[i][0]
        for i in range(3):
            back[i][0] = temp[3-i-1]

def rotateRight(d):
    if d > 0:
        temp = []
        for i in range(3):
            temp.append(up[i][2])
        for i in range(3):
            up[i][2] = front[i][2]
        for i in range(3):
            front[i][2] = down[3-i-1][2]
        for i in range(3):
            down[i][2] = back[i][2]
        for i in range(3):
            back[i][2] = temp[3-i-1]
    else:
        temp = []
        for i in range(3):
            temp.append(up[i][2])
        for i in range(3):
            up[i][2] = back[3-i-1][2]
        for i in range(3):
            back[i][2] = down[i][2]
        for i in range(3):
            down[i][2] = front[3-i-1][2]
        for i in range(3):
            front[i][2] = temp[i]

def rotateCube(c, d):
    if c == 'U' or c == 'D':
        if c == 'U':
            rotateUp(d)
        else:
            rotateDown(d)
    elif c == 'F' or c == 'B':
        if c == 'F':
            rotateFront(d)
        else:
            rotateBack(d)
    else:
        if c == 'L':
            rotateLeft(d)
        else:
            rotateRight(d)

def printCube():
    print("up")
    for i in range(3):
        print(up[i])
    print("down")
    for i in range(3):
        print(down[i])
    print("front")
    for i in range(3):
        print(front[i])
    print("back")
    for i in range(3):
        print(back[i])
    print("left")
    for i in range(3):
        print(left[i])
    print("right")
    for i in range(3):
        print(right[i])

for test_case in range(1, int(input())+1):
    n = int(input())
    rotate = list(map(str, input().split()))
    up, down, front, back, left, right = [], [], [], [], [], []
    for i in range(3):
        up.append(['w', 'w', 'w'])
        down.append(['y', 'y', 'y'])
        front.append(['r', 'r', 'r'])
        back.append(['o', 'o', 'o'])
        left.append(['g', 'g', 'g'])
        right.append(['b', 'b', 'b'])
    
    for i in range(len(rotate)):
        string = rotate[i]
        if string[1] == '+':
            d = 1
        else:
            d = -1
        lst = getPlane(string[0])
        lst = rotatePlane(string[0], d)
        rotateCube(string[0], d)

        # if test_case == 2:
        #     printCube()
        # if i == 1:
        #     break

    # if test_case == 2:
    #     printCube()
    #     break

    for i in range(3):
        print(''.join(up[i]))

'''