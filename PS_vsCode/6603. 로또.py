'''def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(result[i], end=' ')
        print()
        return
    for i in range(start, len(lst)):
        result[depth] = lst[i]
        dfs(i + 1, depth + 1)
        result[depth] = 0

result = [0] * 13
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    del lst[0]
    dfs(0, 0)
    print()'''

from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    del lst[0]
    lst = list(combinations(lst, 6))
    for i in lst:
        print(' '.join(map(str, i)))
    print()