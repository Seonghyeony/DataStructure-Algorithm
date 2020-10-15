'''
처음 시작 칸 말 4개
말이 도착 칸으로 이동하면, 주사위에 나온 수와 관계 없이 이동 마침.
주사위: 5면체 1~5
도착 칸에 있지 않은 말을 하나 골라 이동.
말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가
'''
import copy

dice = list(map(int, input().split()))

# 이렇게 하면 중복되는 위치가 생긴다!
board = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]
branch = {
    (0, 5): (1, 0),
    (0, 10): (2, 0),
    (0, 15): (3, 0)
}
change = {
    (1, 7): (0, 20),
    (2, 3): (1, 4),
    (2, 4): (1, 5),
    (2, 5): (1, 6),
    (2, 6): (0, 20),
    (3, 4): (1, 4),
    (3, 5): (1, 5),
    (3, 6): (1, 6),
    (3, 7): (0, 20),
}

# y, x
pieces = [[0, 0], [0, 0], [0, 0], [0, 0]]
result = 0

def dfs(pieces, start, score):
    global result
    pieces = copy.deepcopy(pieces)
    #print(pieces)
    if start == 10:
        #print(score)
        result = max(result, score)
        return
    
    for idx in range(4):
        y, x = pieces[idx]
        ny, nx = y, x
        if y == -1 and x == -1:
            continue
        
        # 딕셔너리 .get 확인에서 시간이 오래걸린다. 유의.
        if not y == 0 and not board[y][x]:
            ny, nx = y, dice[start]
            if change.get((ny, nx), 0):
                ny, nx = change[(ny, nx)]
        else:
            ny, nx = y, x + dice[start]
            if branch.get((ny, nx), 0):
                ny, nx = branch[(ny, nx)]
            elif change.get((ny, nx), 0):
                ny, nx = change[(ny, nx)]
            else:
                if nx >= len(board[ny]):
                    ny, nx = -1, -1
        
        if ny == -1 and nx == -1:
            value = 0
            pieces[idx] = [ny, nx]
            dfs(pieces, start+1, score+value)
            pieces[idx] = [y, x]
        else:
            if [ny, nx] not in pieces:
                value = board[ny][nx]
                pieces[idx] = [ny, nx]
                dfs(pieces, start+1, score+value)
                pieces[idx] = [y, x]

dfs(pieces, 0, 0)

print(result)
