for test_case in range(1, 11):
    N = int(input())
    result = 1
    for i in range(N):
        lst = list(map(str, input().split()))
        if len(lst) > 3:
            if lst[1] not in '+-*/':
                result = 0
        else:
            if lst[1] in '+-*/':
                result = 0
    print('#{} {}'.format(test_case, result))

