T = int(input())

def lst_sum(lst):
    return int(''.join(lst))

def dfs(lst, count, visited):
    global result
    if count == 0:
        temp = lst_sum(lst)
        if result < temp:
            result = temp
        return

    for i in range(len(lst)):
        for j in range(len(lst)-1, i, -1):
            lst[i], lst[j] = lst[j], lst[i]
            tmp = ''.join(lst)
            if visited.get((tmp, count - 1), 1):
                visited[(tmp, count - 1)] = 0
                dfs(lst, count - 1, visited)
            lst[i], lst[j] = lst[j], lst[i]

def process(test_case):
    data, n = input().split()
    data = list(data)
    n = int(n)

    if len(data) == 1:
        print(f"#{test_case} {data[0]}")

    if len(data) == 2 and n % 2 != 0:
        data[0], data[1] = data[1], data[0]
        print(f"#{test_case} {''.join(data)}")
        return
    
    visited = {}
    dfs(data, n, visited)
    print(f"#{test_case} {result}")

for test_case in range(1, T + 1):
    result = -1
    process(test_case)