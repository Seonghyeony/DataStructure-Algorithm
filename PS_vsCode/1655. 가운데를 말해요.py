import heapq

N = int(input())
left, right = [], [] # left: max_heap, right: min_heap

# 중앙값 기준으로 큰 값은 오른쪽, 작은 값은 왼쪽에 저장.
for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        # max_heap
        heapq.heappush(left, (-num, num))
    else:
        # min_heap
        heapq.heappush(right, (num, num))

    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우. left원소보다 right원소가 더 커야 하는 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])

