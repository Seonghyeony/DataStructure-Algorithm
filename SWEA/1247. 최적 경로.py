def dfs(start, end, need_visit, visited, distance):
    global result
    if len(need_visit) == len(visited):
        last = abs(start[0] - end[0]) + abs(start[1] - end[1])
        result = min(result, distance + last)
        return
    
    ### 이미 값이 정답이 아니면 바로 패쓰.
    if result < distance:
        return
    for i in range(len(need_visit)):
        if need_visit[i] not in visited:
            visited.append(need_visit[i])
            current_distance = abs(start[0] - need_visit[i][0]) + abs(start[1] - need_visit[i][1])
            dfs(need_visit[i], end, need_visit, visited, distance + current_distance)
            visited.pop()

T = int(input())
result = float('inf')
for test_case in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    company = [0, 0]
    house = [0, 0]
    customers = []
    for i in range(0, 4, 2):
        if i == 0:
            company[0], company[1] = temp[i], temp[i+1]
        else:
            house[0], house[1] = temp[i], temp[i+1]
    for i in range(4, len(temp), 2):
        customers.append([temp[i], temp[i+1]])
    result = float('inf')
    dfs(company, house, customers, [], 0)
    print('#{} {}'.format(test_case, result))
    
