def check(candidate):
    if len(candidate) == len(set(candidate)):
        return True
    return False

def dfs(x, candidate):
    if x == M:
        result.append(candidate[:])
        return
    for i in range(1, N+1):
        candidate.append(i)
        if check(candidate):
            dfs(x + 1, candidate)
        candidate.pop()


N, M = map(int, input().split())
result = []
dfs(0, [])
for i in result:
    print(' '.join(map(str, i)))