N, L, K = map(int, input().split())

hard = 0
easy = 0

for _ in range(1, N + 1):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

result = min(hard, K) * 140

if hard < K:
    result += min(K-hard, easy) * 100
print(result)
    
    