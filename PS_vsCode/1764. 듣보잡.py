N, M = map(int, input().split())
lst_a = [input() for _ in range(N)]
lst_b = [input() for _ in range(M)]
result = list(set(lst_a) & set(lst_b))
print(len(result))
for name in sorted(result):
    print(name)

