from collections import deque

def checkAroundPos(lst, aroundPos):
    """
    체크해야할 주변 원소들을 aroundPos에 넣으면서 주변에 지뢰의 갯수를 세어준다.
    지뢰면 더이상 그 방향을 탐색하지 않는다.
    """
    dy, dx = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

    while aroundPos:
        # 주변을 탐색해야 하는 pos
        y, x = aroundPos.pop(0)
        count = 0
        temp_around = []

        # 이미 탐색한 지점인 경우 pass
        if lst[y][x] != '.':
            continue

        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                value = lst[ny][nx]
                if value == '*':
                    count += 1
                elif value == '.':
                    temp_around.append([ny, nx])
        lst[y][x] = str(count)
        # 주변에 지뢰가 없는 pos일 경우만 주변도 탐색
        if count == 0:
            aroundPos.extend(temp_around)

def solve(lst, N):
    dy, dx = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    click_count = 0

    # 첫번째 순회
    # 주변 8면에 지뢰가 없는 위치를 우선으로 탐색
    for i in range(0, N*N):
        y, x = i // N, i % N
        # 이미 탐색했거나 지뢰의 경우 생략
        if lst[y][x] != '.':
            continue

        aroundPos = []
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            # 지뢰인 경우 체크
            if 0 <= ny < N and 0 <= nx < N:
                # 지뢰일 경우 다음으로 넘긴다.
                if lst[ny][nx] == '*':
                    break
                else:
                    aroundPos.append([ny, nx])
        else:
            # 모든 면이 지뢰가 아닐 경우에 클릭.
            click_count += 1
            lst[y][x] = '0'
            # 주변 탐색
            checkAroundPos(lst, aroundPos)

    # 두번째 순회
    # 주변이 지뢰가 하나라도 남아있고, 연쇄적으로 터지지 않은 경우 탐색
    for i in range(0, N*N):
        y, x = i // N, i % N
        if lst[y][x] == '.':
            click_count += 1
    
    return click_count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    print('#{} {}'.format(test_case, solve(lst, N)))
   
'''
# 클릭해도 퍼져나가지 않는 곳
def restTarget():
    global cnt
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '.':
                cnt += 1


# 주변에 지뢰가 하나도 없으면 클릭하고 하나라도 있으면 클릭하지 않고 건너뛴다.
def clickOrNot(y, x):
    global cnt
    next_target = []
    for k in range(8):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if lst[ny][nx] == '.':
                next_target.append([ny, nx])
            elif lst[ny][nx] == '*':
                break
        else:
            # 주변에 지뢰가 하나도 없어 else문으로 오게 되면
            if next_target: # 이 때 주변으로 갈 수 있는 경우가 있으면
                lst[y][x] = 'o' # 체크했다는 표시를 해줌.
                cnt += 1        # 클릭 횟수 더해줌.
                spread(next_target) # 주변으로 퍼져 나간다.

def spread(array):
    queue = deque(array)
    while queue:
        y, x = queue.popleft()
        lst[y][x] = 'o'     # 위 함수의 경우와 다르게 클릭해서 주변으로 퍼졌으므로 일단 체크가 됨.
        next_next_target = []
        for k in range(8):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if lst[ny][nx] == '.':
                    next_next_target.append([ny, nx])
                elif lst[ny][nx] == '*':
                    break
        else:
            # 주변에 지뢰가 없으면 또 다시 퍼져 나간다.
            spread(next_next_target)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    cnt = 0
    # 8 방향
    dy, dx = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '.':
                clickOrNot(i, j)
    
    restTarget()
    print('#{} {}'.format(test_case, cnt))
'''