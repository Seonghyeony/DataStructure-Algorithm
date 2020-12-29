N, A = int(input()), list(map(int, input().split()))
A.sort()
# 만들 수 있는 최저
ans = 0

for num in A:
    if num <= ans + 1:
        ans += num
    else:
        break

print(ans+1)