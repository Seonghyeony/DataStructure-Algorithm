# 택시가 빈칸에 있을 때, 상하좌우 이동가능.
# 특정 위치로 이동할 때 항상 최단경로로만 이동.
# 현재 위치에서 최단거리가 가장 짧은 승객을 고름. --> 힙 (청소년 상어와 비슷)
# 택시와 승객 같은 위치 -> 최단거리 0
# 1칸 이동할 때마다 연료 1 소모
# 목적지로 성공적으로 이동시키면 소모한 연료 양의 2배 충전
# 이동 도중에 연료 바닥 -> 실패 but, 이동시킨 동시에 연료 바닥 -> 성공.

import heapq
from collections import deque

def find_dest(start):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    min_dist = []
    dest_y, dest_x = person[start[1], start[2]]
    queue.append(start)
    ret = -1
    while queue:
        cnt, y, x = queue.popleft()
        if y == dest_y and x == dest_x:
            ret = cnt
            break
        
        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not lst[ny][nx] and not visited[ny][nx]:
                    queue.append([cnt+1, ny, nx])
    
    if ret == -1: # 갈 수 없는 경우
        return None
    return ret
        

def find_person(start):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    # min_dist는 heapq 구조. (cnt, y, x) 형태로 저장.
    min_dist = []
    queue.append(start)
    while queue:
        cnt, y, x = queue.popleft()

        if person.get((y, x), 0):
            heapq.heappush(min_dist, [cnt, y, x])

        if not visited[y][x]:
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not lst[ny][nx] and not visited[ny][nx]:
                    queue.append([cnt+1, ny, nx])

    if min_dist:
        return min_dist[0]
    else:
        return None

N, M, fuel = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
a, b = map(int, input().split())
texi_y, texi_x = a - 1, b - 1
person = {}
for _ in range(M):
    sy, sx, fy, fx = map(int, input().split())
    person[(sy-1, sx-1)] = (fy-1, fx-1)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while True:
    # 현재 위치에서 최단거리가 가장 짧은 승객을 고름
    next_min_person = find_person([0, texi_y, texi_x])
    
    # 태우러 갈 승객이 없는 경우
    if next_min_person is None:
        if person: # 하지만 승객이 남아 있을 때
            fuel = -1
        break

    dist, st_y, st_x = next_min_person
    if dist > fuel:
        fuel = -1
        break
    fuel -= dist
    
    # 승객 태우러 택시 이동
    texi_y, texi_x = st_y, st_x
    
    # 태운 승객의 목적지까지 거리 계산
    dist = find_dest([0, texi_y, texi_x])

    # 목적지로 갈 수 없는 경우
    if dist is None:
        fuel = -1
        break
    if dist > fuel:
        fuel = -1
        break
    fuel -= dist
    fuel += (dist * 2)

    # 목적지로 택시 이동
    texi_y, texi_x = person[(texi_y, texi_x)]
    
    # 승객 태우기 완료! 해당 노선은 지우기!
    del person[(st_y, st_x)]

print(fuel)




