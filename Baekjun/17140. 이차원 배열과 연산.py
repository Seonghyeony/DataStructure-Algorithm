# 55분 클리어!

def R():
    global n, m
    ret = [[] for _ in range(n)]
    for idx in range(n):
        number = {}
        for col in lst[idx]:
            if col != 0:
                if number.get(col, 0):
                    number[col] += 1
                else:
                    number[col] = 1
        number = sorted(number.items(), key=lambda x: (x[1], x[0]))
        for p, q in number:
            ret[idx].extend([p, q])

    for idx in range(n):
        if len(ret[idx]) > m:
            m = len(ret[idx])
    
    if m > 100:
        m = 100

    for idx in range(n):
        while len(ret[idx]) != m:
            ret[idx].append(0)
    return ret

def C():
    global n, m
    ret = [[] for _ in range(m)]
    for j in range(m):
        number = {}
        for i in range(n):
            if lst[i][j] != 0:
                if number.get(lst[i][j], 0):
                    number[lst[i][j]] += 1
                else:
                    number[lst[i][j]] = 1
        number = sorted(number.items(), key=lambda x: (x[1], x[0]))
        for p, q in number:
            ret[j].extend([p, q])
    
    for idx in range(m):
        if len(ret[idx]) > n:
            n = len(ret[idx])
    
    for idx in range(m):
        while len(ret[idx]) != n:
            ret[idx].append(0)

    if n > 100:
        n = 100
    
    trans = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            trans[j][i] = ret[i][j]
    
    return trans

r, c, k = map(int, input().split())
r, c = r-1, c-1
n, m = 3, 3
lst = [list(map(int, input().split())) for _ in range(n)]

time = 0
for _ in range(101):
    if r < n and c < m:
        if lst[r][c] == k:
            break
    if time == 101:
        break
    if n >= m:
        lst = R()
    else:
        lst = C()
    time += 1

if time == 101:
    print(-1)
else:
    print(time)
