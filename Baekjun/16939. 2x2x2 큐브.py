import copy

def clockwise(arr):
    temp = arr[0][0]
    arr[0][0] = arr[1][0]
    arr[1][0] = arr[1][1]
    arr[1][1] = arr[0][1]
    arr[0][1] = temp

def U(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[0])
        temp = CUBE[1][0][0], CUBE[1][0][1]
        CUBE[1][0][0], CUBE[1][0][1] = CUBE[4][1][0], CUBE[4][0][0]
        CUBE[1][1][0], CUBE[1][0][0] = CUBE[5][1][1], CUBE[5][1][0]
        CUBE[5][1][1], CUBE[5][1][0] = CUBE[3][0][1], CUBE[3][1][1]
        CUBE[3][0][1], CUBE[3][1][1] = temp

def F(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[1])
        temp = CUBE[0][1][0], CUBE[0][1][1]
        CUBE[0][1][0], CUBE[0][1][1] = CUBE[3][1][0], CUBE[3][1][1]
        CUBE[3][1][0], CUBE[3][1][1] = CUBE[2][0][1], CUBE[2][0][0]
        CUBE[2][0][1], CUBE[2][0][0] = CUBE[4][1][0], CUBE[4][1][1]
        CUBE[4][1][0], CUBE[4][1][1] = temp


def D(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[2])
        temp = CUBE[1][1][0], CUBE[1][1][1]
        CUBE[1][1][0], CUBE[1][1][1] = CUBE[3][0][0], CUBE[3][1][0]
        CUBE[3][0][0], CUBE[3][1][0] = CUBE[5][0][1], CUBE[5][0][0]
        CUBE[5][0][1], CUBE[5][0][0] = CUBE[4][1][1], CUBE[4][0][1]
        CUBE[4][1][1], CUBE[4][0][1] = temp

def L(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[3])
        temp = CUBE[0][0][0], CUBE[0][1][0]
        CUBE[0][0][0], CUBE[0][1][0] = CUBE[5][0][0], CUBE[5][1][0]
        CUBE[5][0][0], CUBE[5][1][0] = CUBE[2][0][0], CUBE[2][1][0]
        CUBE[2][0][0], CUBE[2][1][0] = CUBE[1][0][0], CUBE[1][1][0]
        CUBE[1][0][0], CUBE[1][1][0] = temp

def R(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[4])
        temp = CUBE[0][0][1], CUBE[0][1][1]
        CUBE[0][0][1], CUBE[0][1][1] = CUBE[1][0][1], CUBE[1][1][1]
        CUBE[1][0][1], CUBE[1][1][1] = CUBE[2][0][1], CUBE[2][1][1]
        CUBE[2][0][1], CUBE[2][1][1] = CUBE[5][0][1], CUBE[5][1][1]
        CUBE[5][0][1], CUBE[5][1][1] = temp

def B(d):
    if d == 1:
        k = 1
    else:
        k = 3

    for _ in range(k):
        clockwise(CUBE[5])
        temp = CUBE[0][0][0], CUBE[0][0][1]
        CUBE[0][0][0], CUBE[0][0][1] = CUBE[4][0][0], CUBE[4][0][1]
        CUBE[4][0][0], CUBE[4][0][1] = CUBE[2][1][1], CUBE[2][1][0]
        CUBE[2][1][1], CUBE[2][1][0] = CUBE[3][0][0], CUBE[3][0][1]
        CUBE[3][0][0], CUBE[3][0][1] = temp

def check():
    for i in range(6):
        temp = CUBE[i][0][0]
        for j in range(2):
            for k in range(2):
                if CUBE[i][j][k] != temp:
                    return False
    return True

cube = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(6)]
# U F D L R B
lst = list(map(int, input().split()))

# for i in range(6):
#     for j in range(2):
#         for _ in range(2):
#             color = lst.pop(0)
#             cube[i][j].append(color)

cube[0][0][0] = lst[0]
cube[0][0][1] = lst[1]
cube[0][1][0] = lst[2]
cube[0][1][1] = lst[3]

cube[1][0][0] = lst[4]
cube[1][0][1] = lst[5]
cube[1][1][0] = lst[6]
cube[1][1][1] = lst[7]

cube[2][0][0] = lst[10]
cube[2][0][1] = lst[11]
cube[2][1][0] = lst[8]
cube[2][1][1] = lst[9]

cube[3][0][0] = lst[12]
cube[3][0][1] = lst[13]
cube[3][1][0] = lst[14]
cube[3][1][1] = lst[15]

cube[4][0][0] = lst[17]
cube[4][0][1] = lst[19]
cube[4][1][0] = lst[16]
cube[4][1][1] = lst[18]

cube[5][0][0] = lst[22]
cube[5][0][1] = lst[23]
cube[5][1][0] = lst[20]
cube[5][1][1] = lst[21]

for i in range(6):
    for j in range(2):
        CUBE = copy.deepcopy(cube)
        if i == 0:
            U(j)
        elif i == 1:
            F(j)
        elif i == 2:
            D(j)
        elif i == 3:
            L(j)
        elif i == 4:
            R(j)
        elif i == 5:
            B(j)

        if check():
            print(1)
            exit()

print(0)