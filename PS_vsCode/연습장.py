N = int(input())
answer = []
for k in range(2, 10):
    trans = []
    result = 1
    n = N
    while True:
        tmp = n
        if tmp < k:
            break
        value = tmp // k
        remain = tmp % k
        n = value
        trans.append(remain)
    trans.append(value)
    for i in trans:
        if i:
            result *= i
    answer.append([result, k])
answer.sort(reverse=True)
print(answer)