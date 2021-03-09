# 1. 해쉬
# 2. 이분탐색

import timeit

start_time = timeit.default_timer()

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
lst = list(map(int, input().split()))
for num in lst:
    start, end, flag = 0, N-1, False
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == num:
            flag = True
            break
        elif cards[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    print(1, end=' ') if flag else print(0, end=' ')

terminate_time = timeit.default_timer()

print("%f초 걸렸습니다." % (terminate_time - start_time))