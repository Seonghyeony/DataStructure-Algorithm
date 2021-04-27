# 1 ~ N^2

def find_pos(arr):
    ret = []
    for y in range(N):
        for x in range(N):
            if lst[y][x] == 0:
                friends, empty = 0, 0
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if lst[ny][nx] in arr:
                            friends += 1
                        elif lst[ny][nx] == 0:
                            empty += 1
                ret.append([friends, empty, y, x])
    ret = sorted(ret, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    return ret[0][2], ret[0][3]

def getScore(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 10
    elif n == 3:
        return 100
    else:
        return 1000

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
students = []
#students_info = {}
lst = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N**2):
    temp = list(map(int, input().split()))
    students.append(temp)
    #students_info[temp[0]] = temp[1:]
    y, x = find_pos(temp[1:])
    lst[y][x] = temp[0]

result = 0
for y in range(N):
    for x in range(N):
        num = lst[y][x]
        friends = []
        for i in range(N**2):
            if students[i][0] == num:
                friends = students[i][1:]
                break
        count = 0
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if lst[ny][nx] in friends:
                    count += 1
        result += getScore(count)

print(result)


