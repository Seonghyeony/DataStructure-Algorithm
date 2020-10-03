for test_case in range(1, 11):
    t = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    x = 0
    y = 99

    for i in range(100):
        if lst[y][i] == 2:
            x = i
            break
    direct = [-1, 1]
    while y > 0:
        flag = 0
        for dx in direct:
            nx = x + dx
            if nx < 0 or nx > 99:
                continue
            while lst[y][nx]:
                flag = 1
                nx += dx
                if nx < 0 or nx > 99:
                    break
            nx -= dx
            x = nx
            if flag:
                break
        y -= 1

    print(f"#{test_case} {x}")

