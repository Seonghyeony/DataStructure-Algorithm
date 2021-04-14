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
def do_operation(oper, val1, val2):
    if oper == '+':
        return val1 + val2
    elif oper == '-':
        return val1 - val2
    elif oper == '*':
        return val1 * val2
    else:
        if val1 < 0:
            val1 = abs(val1)
            return -(val1 // val2)
        else:
            return val1 // val2

def dfs(operators, idx, sum):
    global result_max, result_min

    if idx == n:
        if result_max < sum:
            result_max = sum
        if result_min > sum:
            result_min = sum
        return
    
    for i in range(4):
        copied_operators = copy.deepcopy(operators)
        if copied_operators[i] > 0:
            copied_operators[i] -= 1
            dfs(copied_operators, idx+1, do_operation(op[i], sum, a[idx]))



n = int(input())
a = list(map(int, input().split()))
operators = list(map(int, input().split()))

op = ['+', '-', '*', '/']
result_max = float('-inf')
result_min = float('inf')

dfs(operators, 1, a[0])

print(result_max)
print(result_min)
'''