def calc(a, b):
    sum = 0
    for i in range(N):
        sum += a[i] * b[i]
    return sum

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
print(calc(A, B))
