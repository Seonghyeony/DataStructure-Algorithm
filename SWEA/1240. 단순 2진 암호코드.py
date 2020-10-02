T = int(input())

def isCode(ary):
    num = (ary[1] + ary[3] + ary[5] + ary[7]) * 3 + (ary[2] + ary[4] + ary[6]) + ary[8]
    if num % 10:
        return -1
    else:
        return sum(ary)

def check(lst, y, x):
    if x + 6 > M - 1:
        return False
    if x + 55 > M - 1:
        return False

    if lst[y][x+55] != '1':
        return False

    tmp = ''
    for i in range(7):
        tmp += lst[y][x+i]
    if code.get(tmp, -1) != -1:
        return True
    return False


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    if N < 5 or M < 56:
        print(f"#{test_case} {0}")
        continue

    code = { '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9 }

    y, x = -1, -1
    flag = 0
    for i in range(N):
        for j in range(M):
            if check(lst, i, j):
                y, x = i, j
                flag = 1
                break
        if flag:
            break
    
    array = [-1] * 9

    if y == -1 and x == -1:
        print(f"#{test_case} {0}")
        continue
    
    for i in range(1, 9):
        tmp = ''
        for j in range(7):
            tmp += lst[y][x+j]
        x += 7
        array[i] = code.get(tmp, -1)

    result = isCode(array) + 1
    print(f"#{test_case} {result}")



        
    
