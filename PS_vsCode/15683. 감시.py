import copy

def dfs(lst, start, cctv):
    global result
    if start == len(cctv):
        ret = 0
        for i in lst:
            ret += i.count(0)
        result = min(result, ret)
        return
    
    num, y, x = cctv[start]

    for d in direct[num]:
        tmp = copy.deepcopy(lst)
        for i in d:
            ny, nx = y + dy[i], x + dx[i]
            while N > ny and ny >= 0 and M > nx and nx >= 0:
                if tmp[ny][nx] == 6:
                    break
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
                
                ny += dy[i]
                nx += dx[i]
        dfs(tmp, start + 1, cctv)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0] # 북: 0 남: 1 서: 2 동: 3
dx = [0, 0, -1, 1]
direct = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
             [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]
cctv = []
result = float('inf')

for i in range(N):
    for j in range(M):
        if lst[i][j] not in [0, 6]:
            cctv.append([lst[i][j], i, j])

dfs(lst, 0, cctv)
print(result)