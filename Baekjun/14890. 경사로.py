# 1시간 45분 소요.
def isSameRoad(array, idx):
    ret = []
    pre = array[idx][0]
    if array[idx].count(pre) == N:
        return True
    return False

def solve(array):
    global result

    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        # 길의 원소가 전부 같은 경우.
        if isSameRoad(array, i):
            result += 1
            continue
        # 길인지 아닌지 체크
        flag = True
        for j in range(1, N):
            diff = array[i][j-1] - array[i][j]
            # 내리막길
            if diff == 1:
                temp = False
                for k in range(L):
                    nx = j + k
                    if nx >= N:
                        temp = True
                        break
                    if array[i][nx] != array[i][j]:
                        temp = True
                        break
                    if visited[i][nx]:
                        temp = True
                        break
                    visited[i][nx] = True
                if temp:
                    flag = False
                    break
            # 오르막길
            elif diff == -1:
                temp = False
                for k in range(L):
                    nx = j - 1 - k
                    if nx < 0:
                        temp = True
                        break
                    if array[i][nx] != array[i][j-1]:
                        temp = True
                        break
                    if visited[i][nx]:
                        temp = True
                        break
                    visited[i][nx] = True
                if temp:
                    flag = False
                    break
            elif diff == 0:
                continue
            elif abs(diff) >= 2:
                flag = False
                break

        if flag:
            result += 1

N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = 0
lst2 = []

for j in range(N):
    temp = []
    for i in range(N):
        temp.append(lst[i][j])
    lst2.append(temp)

solve(lst)
solve(lst2)

print(result)
