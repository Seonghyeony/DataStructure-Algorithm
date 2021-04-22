# 1시간 42분 클리어!

N = int(input())

blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0

# 초록색으로 블록이 이동하는 함수
# 행이 가득 차있을 때 점수 얻고, 타일 사라짐.
# 사라진 후 블록이 사라진 행의 수만큼 아래로 이동
# 0, 1번 행에 블록이 있는지
# 있으면 블록이 있는 행의 수만큼 아래의 행에 있는 타일이 사라짐.
# 사라진 행의 수 만큼 아래로 이동.
# 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수 획득 후 연한 칸에 블록이 있는 경우 처리.

def isFullRow():
    ret = []
    for i in range(5, -1, -1):
        if green[i].count(0) == 0:
            return i
    return -1

def isExistRow_01():
    ret = 0
    for i in range(0, 2):
        if sum(green[i]) != 0:
            ret += 1
    return ret

def move_green(t, tile):
    global score
    # 타일의 열만 알고있으면 된다.
    tile_col = []
    for x, y in tile:
        tile_col.append(y)
    # 밑으로 이동
    row = 0
    for i in range(6):
        flag = False
        row = i
        for j in tile_col:
            if green[i][j]:
                flag = True
                row -= 1
                break
        if flag:
            break
    if len(tile_col) == 2:
        if tile_col[0] == tile_col[1]:
            green[row-1][tile_col[0]] = t
            green[row][tile_col[0]] = t
        else:
            for j in tile_col:
                green[row][j] = t
    else:
        for j in tile_col:
            green[row][j] = t
    
    # 행이 가득 차 있는지 확인; 차있는 행 리스트 리턴
    while True:
        fr = isFullRow()
        if fr == -1:
            break
        # 행 지운다.
        green[fr] = [0, 0, 0, 0]
        # 점수 추가
        score += 1
        # 위 행들 내린다.
        for i in range(fr-1, -1, -1):
            green[i+1] = green[i]
        green[0] = [0, 0, 0, 0]
        temp = 1

    
    # 0, 1번에 블록이 있는지 체크
    isExistRowCount = isExistRow_01()
    # 있으면 행의 수 만큼 밑의 행이 사라지고 내린다.
    if isExistRowCount:
        for _ in range(isExistRowCount):
            # 맨 밑 행 지운다.
            green[5] = [0, 0, 0, 0]
            # 위 행들 내린다.
            for i in range(4, -1, -1):
                green[i+1] = green[i]
            green[0] = [0, 0, 0, 0]

# 파란색으로 블록이 이동하는 함수
# 열이 가득 차 있으면 점수 얻고, 타일 사라짐
# 사라진 후 블로이 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동.
# 0, 1 열에 블록이 있으면 오른쪽 열에 있는 타일이 사라지고, 모든 블록이 열의 수만큼 이동.

def isFullCol():
    ret = []
    for j in range(5, -1, -1):
        flag = False
        for i in range(4):
            if blue[i][j] == 0:
                flag = True
                break
        if not flag:
            return j
    return -1

def isExistCol_01():
    ret = 0
    for j in range(2):
        for i in range(4):
            if blue[i][j] != 0:
                ret += 1
                break
    return ret


def move_blue(t, tile):
    global score
    # 타일의 행만 알고있으면 된다.
    tile_row = []
    for x, y in tile:
        tile_row.append(x)
    # 옆으로 이동
    col = 0
    for j in range(6):
        flag = False
        col = j
        for i in tile_row:
            if blue[i][j]:
                flag = True
                col -= 1
                break
        if flag:
            break
    if len(tile_row) == 2:
        if tile_row[0] == tile_row[1]:
            blue[tile_row[0]][col-1] = t
            blue[tile_row[0]][col] = t
        else:
            for i in tile_row:
                blue[i][col] = t
    else:
        for i in tile_row:
            blue[i][col] = t
    
    # 열이 가득 차 있는지 확인; 차있는 열 리스트 리턴
    while True:
        fc = isFullCol()
        if fc == -1:
            break
        # 열 지운다.
        for i in range(4):
            blue[i][fc] = 0
        # 점수 추가
        score += 1
        # 왼쪽 열들 오른쪽으로 민다.
        for j in range(fc-1, -1, -1):
            for i in range(4):
                blue[i][j+1] = blue[i][j]
        for i in range(4):
            blue[i][0] = 0
    
    # 0, 1번에 블록이 있는지 체크
    isExistColCount = isExistCol_01()
    # 있으면 열의 수 만큼 오른쪽 열이 사라지고 옆으로 민다.
    if isExistColCount:
        for _ in range(isExistColCount):
            # 맨 오른쪽 열 지운다.
            for i in range(4):
                blue[i][5] = 0
            # 옆 열들 오른쪽으로 민다.
            for j in range(4, -1, -1):
                for i in range(4):
                    blue[i][j+1] = blue[i][j]
            
            for i in range(4):
                blue[i][0] = 0

def getTile(t, x, y):
    if t == 1:
        return [[x, y]]
    elif t == 2:
        return [[x, y+1], [x, y]]
    else:
        return [[x+1, y], [x, y]]

for _ in range(N):
    # t = 1; 1x1 (x, y)
    # t = 2; 1x2 (x, y), (x, y+1)
    # t = 3; 2x1 (x, y), (x+1, y)
    t, x, y = map(int, input().split())
    tile = getTile(t, x, y)
    move_green(t, tile)
    move_blue(t, tile)

    # for i in blue:
    #     print('             ', end='')
    #     print(i)
    # print()
    # for i in green:
    #     print(i)
    # print()

print(score)
result = 0
for i in range(4):
    for j in range(6):
        if blue[i][j] != 0:
            result += 1
for i in range(6):
    for j in range(4):
        if green[i][j] != 0:
            result += 1
print(result)
