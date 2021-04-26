def dfs(n, value):
    global max_value, min_value
    if n == N:
        if max_value < value:
            max_value = value
        if min_value > value:
            min_value = value
        return
    
    if oper[0] > 0:
        oper[0] -= 1
        dfs(n+1, value + A[n])
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        dfs(n+1, value - A[n])
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        dfs(n+1, value * A[n])
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        if value < 0:
            value = -value // A[n]
            dfs(n+1, -value)
        else:
            dfs(n+1, value // A[n])
        oper[3] += 1

N = int(input())
A = list(map(int, input().split()))
# +, -, *, //
oper = list(map(int, input().split()))
max_value, min_value = float('-inf'), float('inf')
dfs(1, A[0])
print(max_value)
print(min_value)



'''
def dfs(index, res):
    global maxAns, minAns
    # 계산의 끝에 도달했을 때 최댓값과 최솟값이 될 수 있는지 판단한다.
    if index == N - 1:
        if minAns > res:
            minAns = res
        if maxAns < res:
            maxAns = res
        return res
    
    # 백트래킹 DFS로 순회
    for i in range(4):
        temp = res
        if operator[i] == 0:
            continue
        if i == 0:
            res += numArr[index+1]
        elif i == 1:
            res -= numArr[index+1]
        elif i == 2:
            res *= numArr[index+1]
        else:
            if res < 0:
                res = abs(res) // numArr[index+1] * -1
            else:
                res //= numArr[index+1]
        operator[i] -= 1
        dfs(index+1, res)
        operator[i] += 1
        res = temp
    
N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))
minAns = float('inf')
maxAns = float('-inf')

dfs(0, numArr[0])

print(maxAns)
print(minAns)
'''