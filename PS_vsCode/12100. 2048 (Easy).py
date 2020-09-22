# 혼자는 실패ㅠ

import copy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽으로 90도 회전
def rotate90(B, N):
    NB = copy.deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N - i - 1] = B[i][j]
    return NB

def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N - len(new_list))

def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count - 1))
        
        B = rotate90(B, N)

    return ret

print(dfs(N, Board, 5))


'''
import copy

def move(board, direct):
    if direct == 'L':
        for i in range(N):
            tmp = [e for e in board[i] if e]
            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                for j in range(1, N):
                    board[i][j] = 0
                board[i][0] = tmp[0]
            else:
                for index in range(len(tmp) - 1):
                    if tmp[index] == tmp[index + 1]:
                        tmp[index] *= 2
                        tmp[index + 1] = 0
                
                tmp = [data for data in tmp if data]
                t_count = 0
                for t in tmp:
                    board[i][t_count] = t
                    t_count += 1
                for j in range(t_count, N):
                    board[i][j] = 0
    elif direct == 'R':
        for i in range(N):
            tmp = [e for e in board[i] if e]
            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                for j in range(N - 1):
                    board[i][j] = 0
                board[i][-1] = tmp[0]
            else:
                for index in range(len(tmp) - 1, 0, -1):
                    if tmp[index] == tmp[index - 1]:
                        tmp[index] *= 2
                        tmp[index - 1] = 0
                
                tmp.reverse()
                tmp = [data for data in tmp if data]
                t_count = N - 1
                for t in tmp:
                    board[i][t_count] = t
                    t_count -= 1

                for j in range(t_count, -1, -1):
                    board[i][j] = 0

    elif direct == 'T':
        for i in range(N):
            tmp = []
            for j in range(N):
                if board[j][i]:
                    tmp.append(board[j][i])
            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                for j in range(1, N):
                    board[j][i] = 0
                board[0][i] = tmp[0]
            else:
                for index in range(len(tmp) - 1):
                    if tmp[index] == tmp[index + 1]:
                        tmp[index] *= 2
                        tmp[index + 1] = 0
                
                tmp = [data for data in tmp if data]
                t_count = 0
                for t in tmp:
                    board[t_count][i] = t
                    t_count += 1
                for j in range(t_count, N):
                    board[j][i] = 0
                    
    else:
        for i in range(N):
            tmp = []
            for j in range(N):
                if board[j][i]:
                    tmp.append(board[j][i])
            if len(tmp) == 0:
                continue
            elif len(tmp) == 1:
                for j in range(N - 1):
                    board[j][i] = 0
                board[-1][i] = tmp[0]
            else:
                for index in range(len(tmp) - 1):
                    if tmp[index] == tmp[index - 1]:
                        tmp[index] *= 2
                        tmp[index - 1] = 0
                
                tmp.reverse()
                tmp = [data for data in tmp if data]
                t_count = N - 1

                for t in tmp:
                    board[t_count][i] = t
                    t_count -= 1

                for j in range(t_count, -1, -1):
                    board[j][i] = 0

def process(candidate):
    maxNum = 0
    board = copy.deepcopy(lst)
    for direct in candidate:
        move(board, direct)
    print(candidate)
    print(board)
    for i in board:
        maxNum = max(maxNum, max(i))
    return maxNum

def dfs(candidate):
    global result
    if len(candidate) == 1:
        maxNum = process(candidate)
        result = max(result, maxNum)
        return

    for d in directions:
        candidate.append(d)
        dfs(candidate)
        candidate.pop()
    

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ['L', 'R', 'T', 'B']

result = 0
dfs([])
print(result)
'''