import copy

R, C, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
lst = copy.deepcopy(A)
# N: 행 개수, M: 열 개수
N, M = 3, 3
result = -1

if 0 <= (R-1) < N and 0 <= (C-1) < M and lst[R-1][C-1] == k:
    print(0)
else:
    for time in range(1, 101):
        if N >= M:  # R 연산
            tmp, length = [], 1
            for row in lst:
                number = {}
                for num in row:
                    if num == 0:
                        continue

                    if number.get(num, 0):
                        number[num] += 1
                    else:
                        number[num] = 1
                number = sorted(number.items(), key=lambda x: (x[1], x[0]))
                temp = []
                for v, c in number:
                    temp.extend([v, c])
                tmp.append(temp)

            for l in tmp:
                length = max(length, len(l))
            M = length

            lst = [[0 for _ in range(M)] for _ in range(N)]
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    lst[i][j] = tmp[i][j]

        else:  # C 연산
            tmp, length = [], 0
            for x in range(M):
                number = {}
                for y in range(N):
                    num = lst[y][x]
                    if num == 0:
                        continue

                    if number.get(num, 0):
                        number[num] += 1
                    else:
                        number[num] = 1
                number = sorted(number.items(), key=lambda x: (x[1], x[0]))
                temp = []
                for v, c in number:
                    temp.extend([v, c])
                tmp.append(temp)

            for l in tmp:
                length = max(length, len(l))
            N = length
            lst = [[0 for _ in range(M)] for _ in range(N)]

            for x in range(len(tmp)):
                for y in range(len(tmp[x])):
                    lst[y][x] = tmp[x][y]

        if 0 <= (R-1) < N and 0 <= (C-1) < M:
            if lst[R-1][C-1] == k:
                result = time
                break

    print(result)