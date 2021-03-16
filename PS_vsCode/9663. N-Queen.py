def check(x):
    for i in range(x):
        if row[i] == row[x]:
            return False
        if abs(row[i] - row[x]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            dfs(x + 1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)