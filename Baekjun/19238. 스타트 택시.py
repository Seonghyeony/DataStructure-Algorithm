# 손님을 도착지로 데려줄 때마다 연료 충전, 연료 바닥나면 끝
# M 명 손님 목표, 항상 최단경로로 이동.
# 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
# 택시와 승객이 같은 위치면 거리 0
# 목적지로 이동시키면 소모한 연료 양의 2배가 충전.
# 이동하는 도중에 연료 바닥나면 이동 실패, 업무 끝. but, 이동시킨 동시에 연료가 바닥나면 성공한 것임.
# 다 이동 시키고 남은 연료 양은?

# 55분 클리어!

from collections import deque

def find_customer(y, x):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([[y, x, 0]])
    candidate = []
    while queue:
        y, x, count = queue.popleft()
        if not visited[y][x]:
            if lst[y][x] == 2:
                candidate.append([count, y, x])
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx] != 1:
                    queue.append([ny, nx, count+1])
    
    if len(candidate):
        candidate.sort()
        return candidate[0][1], candidate[0][2], candidate[0][0]
    else:
        return -1, -1, -1

def move_arrive(start_y, start_x, end_y, end_x):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([[start_y, start_x, 0]])
    while queue:
        y, x, count = queue.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            if y == end_y and x == end_x:
                return count
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx] != 1:
                    queue.append([ny, nx, count+1])
    return None

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M, fuel = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
taxi_y, taxi_x = map(int, input().split())
taxi_y, taxi_x = taxi_y-1, taxi_x-1
customers = dict()
for _ in range(M):
    start_y, start_x, end_y, end_x = map(int, input().split())
    start_y, start_x, end_y, end_x = start_y-1, start_x-1, end_y-1, end_x-1
    lst[start_y][start_x] = 2
    customers[(start_y, start_x)] = (end_y, end_x)

while True:
    # 가장 가까운 승객 거리
    customer_y, customer_x, spend = find_customer(taxi_y, taxi_x)
    # 승객을 다 태웠다?
    if customer_y == -1:
        break
    # 이동하는 도중에 연료가 바닥나면.
    if fuel < spend:
        fuel = -1
        break

    # 승객 태우러 이동
    fuel -= spend
    # 승객을 태운다.
    lst[customer_y][customer_x] = 0
    taxi_y, taxi_x = customer_y, customer_x
    
    # 도착지까지 거리는?
    arrive_y, arrive_x = customers[(taxi_y, taxi_x)]
    spend = move_arrive(taxi_y, taxi_x, arrive_y, arrive_x)

    # 도착지까지 못간다면1
    if spend is None:
        fuel = -1
        break

    # 도착지까지 가지 못한다면2
    if fuel < spend:
        fuel = -1
        break
    # 도착성공!
    taxi_y, taxi_x = arrive_y, arrive_x
    fuel -= spend
    #print("도착지 이동", spend)
    fuel += spend * 2

    #print(fuel)

if fuel == -1:
    print(-1)
else:
    flag = False
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                flag = True
                break
        if flag:
            break
    if flag:
        print(-1)
    else:
        print(fuel)
