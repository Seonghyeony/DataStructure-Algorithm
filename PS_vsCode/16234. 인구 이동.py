from collections import deque

directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x):
    move_q = deque()
    q.append([y, x])
    c[y][x] = 1
    people, cnt = 0, 0

    while q:
        y, x = q.popleft()
        move_q.append([y, x])
        people += lst[y][x]
        cnt += 1
        for dy, dx in directs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not c[ny][nx]:
                if l <= abs(lst[y][x] - lst[ny][nx]) <= r:
                    c[ny][nx] = cnt
                    q.append([ny, nx])

    while move_q:
        y, x = move_q.popleft()
        lst[y][x] = people // cnt
    
    if cnt == 1:
        return 0

    return 1

n, l, r = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
    q = deque()
    c = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                cnt += bfs(i, j)

    if not cnt:
        break

    ans += 1

print(ans)


'''
from collections import deque

def bfs(y, x):
    visited = set([(x, y)])
    queue = deque([(x, y)])
    """
    total: 연합의 인구 수
    num: 연합에서 나라의 갯수
    """
    total, num = 0, 0

    while queue:
        y, x = queue.popleft()
        total += lst[y][x]
        num += 1

        for dy, dx in directs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited and (ny, nx) not in total_visited:
                diff = abs(lst[ny][nx] - lst[y][x])
                if L <= diff <= R:
                    # BFS를 한 번이라도 탄 것이므로, is_move를 True로 변환.
                    global is_move
                    is_move = True

                    queue.append((ny, nx))
                    visited.add((ny, nx))
    return total // num, visited

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 0

while True:
    total_visited = set() # BFS 탐색에 한번이라도 들어간 경우, 재 탐색을 할 필요가 없으므로,
                          # 이 집합에 담아둔다.
    is_move = False
    unions = []

    for y in range(N):
        for x in range(N):
            if (y, x) not in total_visited:
                changed_num, visited = bfs(y, x)
                unions.append((changed_num, visited))
                total_visited |= visited
        
    #print(total_visited)
    #print(unions)

    for (changed_num, union) in unions:
        for country in union:
            y, x = country
            lst[y][x] = changed_num

    if not is_move:
        break

    answer += 1

print(answer)
'''