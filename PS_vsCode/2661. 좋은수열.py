import sys

def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def dfs(num):
    if len(num) == N:
        print(num)
        sys.exit()
    for i in '123':
        if check(num + str(i)):
            dfs(num + str(i))
    return

N = int(input())
dfs('1')