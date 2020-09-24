N, A = int(input()), list(map(int, input().split()))
A.sort()
# 만들 수 있는 최저
ans = 0

for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans+1)