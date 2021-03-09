N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

lst = sorted(list(set(lst)), key=lambda x: (len(x), x))
for word in lst:
    print(word)